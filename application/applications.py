import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from Star_Utils import Cog, CogsUtils, Settings, Buttons, Menu, Modal, Dropdown
import asyncio
import datetime
import typing
import uuid

class QuestionType:
    TEXT = "text"
    YES_NO = "yes_no"

class ApplicationType:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions  # List of (question, type) tuples

class Application:
    def __init__(self, user_id, app_type, channel_id):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.app_type = app_type
        self.channel_id = channel_id
        self.answers = {}
        self.status = "In Progress"
        self.created_at = datetime.datetime.utcnow()
        self.last_updated = datetime.datetime.utcnow()

class Applications(Cog):
    """A complex application system for Discord servers."""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_guild = {
            "application_types": {},
            "log_channel": None,
            "application_category": None,
        }
        self.config.register_guild(**default_guild)
        self.applications = {}

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def appset(self, ctx: commands.Context):
        """Configure the application system."""
        pass

    @appset.command(name="setlogchannel")
    async def set_log_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for application logs."""
        await self.config.guild(ctx.guild).log_channel.set(channel.id)
        await ctx.send(f"Log channel set to {channel.mention}.")

    @appset.command(name="setcategory")
    async def set_application_category(self, ctx: commands.Context, category: discord.CategoryChannel):
        """Set the category for application channels."""
        await self.config.guild(ctx.guild).application_category.set(category.id)
        await ctx.send(f"Application category set to {category.name}.")

    @commands.command(name="apps")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def apps(self, ctx: commands.Context):
        """Manage application types and questions."""
        await self.add_application(ctx)

    async def add_application(self, ctx: commands.Context):
        questions = []
        while True:
            question_type = await self.get_question_type(ctx)
            question = await self.get_question(ctx)
            questions.append((question, question_type))

            if not await self.add_another_question(ctx):
                break

        app_name = await self.get_application_name(ctx)
        await self.save_application(ctx, app_name, questions)

    async def get_question_type(self, ctx: commands.Context):
        options = [
            discord.SelectOption(label="Text Question", value=QuestionType.TEXT),
            discord.SelectOption(label="Yes/No Question", value=QuestionType.YES_NO)
        ]
        select_menu = Dropdown(
            placeholder="What kind of question?",
            options=options,
            min_values=1,
            max_values=1
        )

        message = await ctx.send("Select the type of question:", view=select_menu)

        try:
            interaction, values = await select_menu.wait_result()
            await message.delete()
            return values[0]
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("Question creation timed out.")
            return None

    async def get_question(self, ctx: commands.Context):
        await ctx.send("What is the question?")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            message = await self.bot.wait_for('message', check=check, timeout=300.0)
            return message.content
        except asyncio.TimeoutError:
            await ctx.send("Question input timed out.")
            return None

    async def add_another_question(self, ctx: commands.Context):
        options = [
            discord.SelectOption(label="Yes", value="yes"),
            discord.SelectOption(label="No", value="no")
        ]
        select_menu = Dropdown(
            placeholder="Do you want to add another question?",
            options=options,
            min_values=1,
            max_values=1
        )

        message = await ctx.send("Do you want to add another question?", view=select_menu)

        try:
            interaction, values = await select_menu.wait_result()
            await message.delete()
            return values[0] == "yes"
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("Selection timed out.")
            return False

    async def get_application_name(self, ctx: commands.Context):
        await ctx.send("What is this application for? (This will be the name of the application type)")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            message = await self.bot.wait_for('message', check=check, timeout=300.0)
            return message.content
        except asyncio.TimeoutError:
            await ctx.send("Application name input timed out.")
            return None

    async def save_application(self, ctx: commands.Context, app_name: str, questions: typing.List[typing.Tuple[str, str]]):
        if not app_name:
            await ctx.send("Application creation cancelled due to missing name.")
            return

        async with self.config.guild(ctx.guild).application_types() as app_types:
            if app_name in app_types:
                await ctx.send(f"An application type named '{app_name}' already exists. Please choose a different name.")
                return

            app_types[app_name] = {"questions": questions}

        await ctx.send(f"Application '{app_name}' has been created with {len(questions)} questions.")

    @commands.command()
    @commands.guild_only()
    async def apply(self, ctx: commands.Context):
        """Start a new application."""
        app_types = await self.config.guild(ctx.guild).application_types()
        if not app_types:
            await ctx.send("No application types have been set up yet.")
            return

        options = [discord.SelectOption(label=name, value=name) for name in app_types.keys()]
        select_menu = Dropdown(
            placeholder="Choose an application type",
            options=options,
            min_values=1,
            max_values=1
        )

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: typing.List[str]):
            app_type = values[0]
            await self.start_application(interaction, app_type)

        select_menu.function = handle_selection
        await ctx.send("Please select an application type:", view=select_menu)

    async def start_application(self, interaction: discord.Interaction, app_type: str):
        guild = interaction.guild
        user = interaction.user

        app_types = await self.config.guild(guild).application_types()
        if app_type not in app_types:
            await interaction.response.send_message("Invalid application type.", ephemeral=True)
            return

        category_id = await self.config.guild(guild).application_category()
        category = guild.get_channel(category_id)
        if not category:
            await interaction.response.send_message("Application category not set up. Please contact an admin.", ephemeral=True)
            return

        channel_name = f"{app_type.lower()}-{user.name}-{user.discriminator}"
        channel = await guild.create_text_channel(channel_name, category=category)

        await channel.set_permissions(user, read_messages=True, send_messages=True)
        await channel.set_permissions(guild.default_role, read_messages=False)

        application = Application(user.id, app_type, channel.id)
        self.applications[channel.id] = application

        await interaction.response.send_message(f"Your application has been started in {channel.mention}", ephemeral=True)
        await self.send_application_questions(channel, app_types[app_type]["questions"])

    async def send_application_questions(self, channel: discord.TextChannel, questions: typing.List[typing.Tuple[str, str]]):
        await channel.send("Please answer the following questions:")
        for i, (question, q_type) in enumerate(questions, 1):
            await channel.send(f"**Question {i}:** {question}")

            if q_type == QuestionType.YES_NO:
                view = Dropdown(
                    placeholder="Select your answer",
                    options=[
                        discord.SelectOption(label="Yes", value="Yes"),
                        discord.SelectOption(label="No", value="No")
                    ],
                    min_values=1,
                    max_values=1
                )
                message = await channel.send("Please select your answer:", view=view)

                try:
                    interaction, values = await view.wait_result()
                    self.applications[channel.id].answers[i] = values[0]
                    await message.edit(content=f"You answered: {values[0]}", view=None)
                except asyncio.TimeoutError:
                    await channel.send("You took too long to answer. The application has been cancelled.")
                    await self.close_application(channel.id, "Timeout")
                    return
            else:
                def check(m):
                    return m.channel == channel and m.author.id == self.applications[channel.id].user_id

                try:
                    answer = await self.bot.wait_for('message', check=check, timeout=600)
                    self.applications[channel.id].answers[i] = answer.content
                except asyncio.TimeoutError:
                    await channel.send("You took too long to answer. The application has been cancelled.")
                    await self.close_application(channel.id, "Timeout")
                    return

        await self.finish_application(channel)

    async def finish_application(self, channel: discord.TextChannel):
        application = self.applications[channel.id]
        application.status = "Pending Review"
        application.last_updated = datetime.datetime.utcnow()

        embeds = await self.create_application_embeds(application)
        for embed in embeds:
            await channel.send(embed=embed)

        await channel.send("Your application has been submitted for review.")

        review_message = await channel.send("Please review this application:")
        approve_button = discord.ui.Button(style=discord.ButtonStyle.green, label="Approve", custom_id="approve")
        deny_button = discord.ui.Button(style=discord.ButtonStyle.red, label="Deny", custom_id="deny")
        more_info_button = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Request More Info", custom_id="more_info")

        view = Buttons(
            timeout=None,
            buttons=[approve_button, deny_button, more_info_button],
            function=self.handle_review_action
        )
        await review_message.edit(view=view)

        await self.log_application_event(channel.guild, "Application Submitted", application)

    async def handle_review_action(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]
        channel = interaction.channel
        application = self.applications[channel.id]

        if action == "approve":
            await self.approve_application(interaction, application)
        elif action == "deny":
            await self.deny_application(interaction, application)
        elif action == "more_info":
            await self.request_more_info(interaction, application)

    async def approve_application(self, interaction: discord.Interaction, application: Application):
        application.status = "Approved"
        application.last_updated = datetime.datetime.utcnow()
        await interaction.response.send_message("Application approved!")
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been approved!")
        await self.close_application(application.channel_id, "Approved")
        await self.log_application_event(interaction.guild, "Application Approved", application)

    async def deny_application(self, interaction: discord.Interaction, application: Application):
        application.status = "Denied"
        application.last_updated = datetime.datetime.utcnow()
        await interaction.response.send_message("Application denied.")
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been denied.")
        await self.close_application(application.channel_id, "Denied")
        await self.log_application_event(interaction.guild, "Application Denied", application)

    async def request_more_info(self, interaction: discord.Interaction, application: Application):
        modal = Modal(title="Request More Information")
        modal.add_item(discord.ui.TextInput(label="What additional information is needed?"))
        await interaction.response.send_modal(modal)

        try:
            modal_interaction = await self.bot.wait_for(
                "modal_submit",
                check=lambda i: i.custom_id == modal.custom_id and i.user.id == interaction.user.id,
                timeout=300.0
            )
        except asyncio.TimeoutError:
            await interaction.followup.send("Request timed out.", ephemeral=True)
            return

        additional_info_request = modal_interaction.data['components'][0]['components'][0]['value']
        await modal_interaction.response.send_message(f"Requesting additional information: {additional_info_request}")

        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Additional information is required for your {application.app_type} application:\n\n{additional_info_request}")

        application.status = "More Info Requested"
        application.last_updated = datetime.datetime.utcnow()
        await self.log_application_event(interaction.guild, "More Info Requested", application)

    async def close_application(self, channel_id: int, reason: str):
        application = self.applications.pop(channel_id, None)
        if not application:
            return

        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(f"This application is now closed. Reason: {reason}")
            await asyncio.sleep(10)
            await channel.delete()

    async def create_application_embeds(self, application: Application) -> typing.List[discord.Embed]:
        user = self.bot.get_user(application.user_id)
        embeds = []
        current_embed = discord.Embed(title=f"{application.app_type} Application", color=discord.Color.blue())
        current_embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url)
        current_embed.add_field(name="Status", value=application.status, inline=False)
        current_embed.add_field(name="Created At", value=application.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        current_embed.add_field(name="Last Updated", value=application.last_updated.strftime("%Y-%m-%d %H:%M:%S"), inline=False)

        for question, answer in application.answers.items():
            field_name = f"Question {question}"
            field_value = answer[:1021] + "..." if len(answer) > 1024 else answer
            if len(current_embed.fields) >= 25 or len(current_embed) + len(field_name) + len(field_value) > 6000:
                embeds.append(current_embed)
                current_embed = discord.Embed(title=f"{application.app_type} Application (Continued)", color=discord.Color.blue())
            current_embed.add_field(name=field_name, value=field_value, inline=False)

        embeds.append(current_embed)
        return embeds

    async def log_application_event(self, guild: discord.Guild, event: str, application: Application):
        log_channel_id = await self.config.guild(guild).log_channel()
        if not log_channel_id:
            return

        log_channel = guild.get_channel(log_channel_id)
        if not log_channel:
            return

        user = self.bot.get_user(application.user_id)
        embed = discord.Embed(title=f"Application Event: {event}", color=discord.Color.gold())
        embed.add_field(name="User", value=f"{user.name}#{user.discriminator}", inline=False)
        embed.add_field(name="Application Type", value=application.app_type, inline=False)
        embed.add_field(name="Status", value=application.status, inline=False)
        embed.add_field(name="Event Time", value=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), inline=False)

        await log_channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def appstats(self, ctx: commands.Context):
        """View application statistics."""
        guild_apps = [app for app in self.applications.values() if self.bot.get_channel(app.channel_id).guild.id == ctx.guild.id]
        total_apps = len(guild_apps)
        status_counts = {status: len([app for app in guild_apps if app.status == status]) for status in set(app.status for app in guild_apps)}

        embed = discord.Embed(title="Application Statistics", color=discord.Color.blue())
        embed.add_field(name="Total Applications", value=str(total_apps), inline=False)
        for status, count in status_counts.items():
            embed.add_field(name=f"{status} Applications", value=str(count), inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def appsearch(self, ctx: commands.Context, *, search_term: str):
        """Search for applications by user or type."""
        guild_apps = [app for app in self.applications.values() if self.bot.get_channel(app.channel_id).guild.id == ctx.guild.id]
        matching_apps = [
            app for app in guild_apps
            if search_term.lower() in self.bot.get_user(app.user_id).name.lower()
            or search_term.lower() in app.app_type.lower()
        ]

        if not matching_apps:
            await ctx.send("No matching applications found.")
            return

        embeds = []
        for app in matching_apps:
            embeds.extend(await self.create_application_embeds(app))

        await Menu(pages=embeds).start(ctx)
