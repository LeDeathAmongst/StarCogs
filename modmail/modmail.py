import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from Star_Utils import Cog, CogsUtils, Settings
import io
from datetime import datetime

class ModMail(Cog):
    """A basic ModMail cog"""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_guild = {
            "modmail_channel": None,
            "log_channel": None,
            "areply_name": "Support Team",
            "preconfigured_messages": {},
            "authorized_users": [],
            "snippet_reply_method": "reply",  # Default method for snippets
            "modmail_enabled": True  # ModMail enabled by default
        }
        self.config.register_guild(**default_guild)

        # Initialize logger
        self.logger = CogsUtils.get_logger(cog=self)

        # Initialize settings
        settings_dict = {
            "modmail_channel": {
                "path": ["modmail_channel"],
                "converter": discord.TextChannel,
                "description": "Set the modmail channel for this server.",
                "usage": "channel",
                "command_name": "modmailchannel"
            },
            "log_channel": {
                "path": ["log_channel"],
                "converter": discord.TextChannel,
                "description": "Set the log channel for this server.",
                "usage": "channel",
                "command_name": "logchannel"
            },
            "areply_name": {
                "path": ["areply_name"],
                "converter": str,
                "description": "Set the areply title name.",
                "usage": "title",
                "command_name": "areplyname"
            },
            "snippet_reply_method": {
                "path": ["snippet_reply_method"],
                "converter": str,
                "description": "Set the method for sending snippets (reply/areply).",
                "usage": "method",
                "command_name": "snippetmethod"
            }
        }
        self.settings = Settings(bot=self.bot, cog=self, config=self.config, group=Config.GUILD, settings=settings_dict, guild_specific=True)

    async def cog_load(self):
        # Load snippet commands on cog load
        for guild in self.bot.guilds:
            await self.load_snippet_commands(guild)

    async def load_snippet_commands(self, guild: discord.Guild):
        """Load snippet commands for a specific guild."""
        preconfigured_messages = await self.config.guild(guild).preconfigured_messages()
        for name, message in preconfigured_messages.items():
            self.add_snippet_command(name, message, guild.id)

    def add_snippet_command(self, name: str, message: str, guild_id: int):
        """Dynamically add a snippet command."""
        async def snippet_command(ctx: commands.Context):
            """Send a snippet message."""
            if ctx.guild.id != guild_id:
                return

            # Get the user from the thread participants
            thread = ctx.channel
            if not isinstance(thread, discord.Thread):
                await ctx.send("This command can only be used within a modmail thread.")
                return

            user = None
            # Await the coroutine to get the members
            members = await thread.fetch_members()
            for thread_member in members:
                # Fetch the user associated with the ThreadMember
                member = await self.bot.fetch_user(thread_member.id)
                if not member.bot:
                    user = member
                    break

            if user is None:
                await ctx.send("User not found in this thread.")
                return

            # Determine the method for sending the snippet
            snippet_method = await self.config.guild(ctx.guild).snippet_reply_method()
            if snippet_method == "areply":
                areply_name = await self.config.guild(ctx.guild).areply_name()
                embed = discord.Embed(
                    title=areply_name,
                    description=message,
                    color=discord.Color.green()
                )
                if ctx.guild.icon:
                    embed.set_author(name=areply_name, icon_url=ctx.guild.icon.url)
                else:
                    embed.set_author(name=areply_name)
                footer_text = "Moderator/Admin"
            else:
                embed = discord.Embed(
                    title=ctx.author.display_name,
                    description=message,
                    color=discord.Color.green()
                )
                if ctx.author.avatar:
                    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                else:
                    embed.set_author(name=ctx.author.display_name)
                highest_role = max(ctx.author.roles, key=lambda r: r.position, default=None)
                footer_text = highest_role.name if highest_role else "No role"

            embed.set_footer(text=footer_text)
            await user.send(embed=embed)
            await ctx.send(f"Snippet '{name}' sent to {user.mention}.")

        # Add the command to the bot
        snippet_command.__name__ = f"snippet_{name}"
        command = commands.command(name=name)(snippet_command)
        self.bot.add_command(command)

    async def remove_snippet_command(self, name: str):
        """Remove a snippet command."""
        command_name = f"snippet_{name}"
        command = self.bot.get_command(command_name)
        if command:
            self.bot.remove_command(command_name)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        await self.load_snippet_commands(guild)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        preconfigured_messages = await self.config.guild(guild).preconfigured_messages()
        for name in preconfigured_messages:
            await self.remove_snippet_command(name)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or not isinstance(message.channel, discord.DMChannel):
            return

        # Check if ModMail is enabled
        for guild in self.bot.guilds:
            modmail_enabled = await self.config.guild(guild).modmail_enabled()
            if not modmail_enabled:
                continue

            modmail_channel_id = await self.config.guild(guild).modmail_channel()
            if not modmail_channel_id:
                continue

            modmail_channel = guild.get_channel(modmail_channel_id)
            if modmail_channel is None:
                continue

            # Ensure only one thread per user
            existing_thread = discord.utils.get(modmail_channel.threads, name=f"ModMail-{message.author.id}-{message.author.display_name}")
            if existing_thread:
                thread = existing_thread
            else:
                thread = await modmail_channel.create_thread(name=f"ModMail-{message.author.id}-{message.author.display_name}", type=discord.ChannelType.public_thread)

                # Fetch the Member object
                member = guild.get_member(message.author.id)
                if member:
                    roles = ', '.join([role.name for role in member.roles if role.name != "@everyone"])
                    joined_at = member.joined_at.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    roles = "No roles"
                    joined_at = "Unknown"

                # Create and send the info embed
                info_embed = discord.Embed(
                    title=message.author.display_name,
                    description=f"User ID: {message.author.id}",
                    color=discord.Color.blue()
                )
                info_embed.add_field(name="Roles", value=roles, inline=False)
                info_embed.add_field(name="Joined The Server", value=joined_at, inline=False)
                await thread.send(embed=info_embed)

            # Send the message content
            content_embed = discord.Embed(
                description=message.content,
                color=discord.Color.blue()
            )
            # Set the author's name and ID in the title, and their profile picture as the thumbnail
            if message.author.avatar:
                content_embed.set_author(name=f"{message.author.display_name} ({message.author.id})", icon_url=message.author.avatar.url)
            else:
                content_embed.set_author(name=f"{message.author.display_name} ({message.author.id})")
            await thread.send(embed=content_embed)
            break

    @commands.guild_only()
    @commands.group()
    async def config(self, ctx: commands.Context):
        """Configuration commands for modmail."""
        if ctx.invoked_subcommand is None:
            await ctx.send("Please specify a valid subcommand: channel, log, title, snippetmethod, toggle.")

    @config.command(name="channel")
    async def config_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the modmail channel for this server."""
        await self.config.guild(ctx.guild).modmail_channel.set(channel.id)
        await ctx.send(f"ModMail channel set to {channel.mention}")

    @config.command(name="log")
    async def config_log(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the log channel for this server."""
        await self.config.guild(ctx.guild).log_channel.set(channel.id)
        await ctx.send(f"Log channel set to {channel.mention}")

    @config.command(name="title")
    async def config_title(self, ctx: commands.Context, *, title: str):
        """Set the areply title name."""
        await self.config.guild(ctx.guild).areply_name.set(title)
        await ctx.send(f"Areply title name set to {title}")

    @config.command(name="snippetmethod")
    async def config_snippet_method(self, ctx: commands.Context, method: str):
        """Set the method for sending snippets (reply/areply)."""
        if method not in ["reply", "areply"]:
            await ctx.send("Invalid method. Please choose either 'reply' or 'areply'.")
            return
        await self.config.guild(ctx.guild).snippet_reply_method.set(method)
        await ctx.send(f"Snippet sending method set to {method}.")

    @config.command(name="toggle")
    async def config_toggle(self, ctx: commands.Context):
        """Toggle the ModMail system on or off for this server."""
        current_state = await self.config.guild(ctx.guild).modmail_enabled()
        new_state = not current_state
        await self.config.guild(ctx.guild).modmail_enabled.set(new_state)
        state_text = "enabled" if new_state else "disabled"
        await ctx.send(f"ModMail has been {state_text} for this server.")

    @commands.guild_only()
    @commands.mod_or_permissions(manage_messages=True)
    @commands.command(aliases=["r"])
    async def reply(self, ctx: commands.Context, *, response: str):
        """Reply to a user via ModMail from within a thread."""
        if ctx.channel.type != discord.ChannelType.public_thread:
            await ctx.send("This command can only be used within a modmail thread.")
            return

        user_id_str = ctx.channel.name.split("ModMail-")[1].split('-')[0]
        user = self.bot.get_user(int(user_id_str))

        if user is None:
            await ctx.send("User not found.")
            return

        # Send the response to the user
        embed = discord.Embed(
            title=user.display_name,
            description=response,
            color=discord.Color.green()
        )
        # Set the author's icon for the embed
        if ctx.author.avatar:
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        else:
            embed.set_author(name=ctx.author.display_name)

        # Add footer with user's highest hoisted role
        highest_role = max(ctx.author.roles, key=lambda r: r.position, default=None)
        footer_text = highest_role.name if highest_role else "No role"
        embed.set_footer(text=footer_text)

        await user.send(embed=embed)

        # Log the response in the thread
        await ctx.send(f"Reply sent to {user.mention}: {response}")

    @commands.guild_only()
    @commands.mod_or_permissions(manage_messages=True)
    @commands.command(aliases=["ar"])
    async def areply(self, ctx: commands.Context, *, response: str):
        """Reply to a user via ModMail with a generic support team title from within a thread."""
        if ctx.channel.type != discord.ChannelType.public_thread:
            await ctx.send("This command can only be used within a modmail thread.")
            return

        user_id_str = ctx.channel.name.split("ModMail-")[1].split('-')[0]
        user = self.bot.get_user(int(user_id_str))

        if user is None:
            await ctx.send("User not found.")
            return

        areply_name = await self.config.guild(ctx.guild).areply_name()

        # Send the response to the user
        embed = discord.Embed(
            title=areply_name,
            description=response,
            color=discord.Color.green()
        )
        # Set the author's icon for the embed if the guild has an icon
        if ctx.guild.icon:
            embed.set_author(name=areply_name, icon_url=ctx.guild.icon.url)
        else:
            embed.set_author(name=areply_name)

        # Add footer with user's highest hoisted role and "Moderator/Admin"
        highest_role = max(ctx.author.roles, key=lambda r: r.position, default=None)
        footer_text = f"{highest_role.name if highest_role else 'No role'} - Moderator/Admin"
        embed.set_footer(text=footer_text)

        await user.send(embed=embed)

        # Log the response in the thread
        await ctx.send(f"Reply sent to {user.mention}: {response}")

    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    @commands.group()
    async def snippet(self, ctx: commands.Context):
        """Manage pre-configured message snippets."""
        if ctx.invoked_subcommand is None:
            await ctx.send("Please specify a valid subcommand: add, list, edit, remove, view.")

    @snippet.command(name="add")
    async def snippet_add(self, ctx: commands.Context, name: str, *, message: str):
        """Add a new snippet."""
        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        if name in preconfigured_messages:
            await ctx.send("That snippet name is already in use. You can change it or use the existing one.")
            return

        preconfigured_messages[name] = message
        await self.config.guild(ctx.guild).preconfigured_messages.set(preconfigured_messages)
        self.add_snippet_command(name, message, ctx.guild.id)
        await ctx.send(f"Snippet '{name}' added.")

    @snippet.command(name="list")
    async def snippet_list(self, ctx: commands.Context):
        """List all snippets for the current server."""
        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        if not preconfigured_messages:
            await ctx.send("No snippets found for this server.")
            return

        snippet_list = "\n".join(preconfigured_messages.keys())
        await ctx.send(f"Snippets for this server:\n{snippet_list}")

    @snippet.command(name="edit")
    async def snippet_edit(self, ctx: commands.Context, name: str, *, new_content: str):
        """Edit an existing snippet."""
        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        if name not in preconfigured_messages:
            await ctx.send(f"No snippet found with name '{name}'.")
            return

        preconfigured_messages[name] = new_content
        await self.config.guild(ctx.guild).preconfigured_messages.set(preconfigured_messages)
        await self.remove_snippet_command(name)
        self.add_snippet_command(name, new_content, ctx.guild.id)
        await ctx.send(f"Snippet '{name}' updated.")

    @snippet.command(name="remove")
    async def snippet_remove(self, ctx: commands.Context, name: str):
        """Remove a snippet."""
        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        if name not in preconfigured_messages:
            await ctx.send(f"No snippet found with name '{name}'.")
            return

        del preconfigured_messages[name]
        await self.config.guild(ctx.guild).preconfigured_messages.set(preconfigured_messages)
        await self.remove_snippet_command(name)
        await ctx.send(f"Snippet '{name}' removed.")

    @snippet.command(name="view")
    async def snippet_view(self, ctx: commands.Context, name: str):
        """View a snippet's content."""
        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        if name not in preconfigured_messages:
            await ctx.send(f"No snippet found with name '{name}'.")
            return

        message = preconfigured_messages[name]
        embed = discord.Embed(
            title=f"Snippet `{name}`",
            description=message,
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.group()
    async def thread(self, ctx: commands.Context):
        """Manage threads."""
        if ctx.invoked_subcommand is None:
            await ctx.send("Please specify a valid subcommand: close, open, add.")

    @thread.command(name="close")
    @commands.mod_or_permissions(manage_messages=True)
    async def thread_close(self, ctx: commands.Context):
        """Close the modmail thread and generate a log."""
        if ctx.channel.type != discord.ChannelType.public_thread:
            await ctx.send("This command can only be used within a modmail thread.")
            return

        # Get the log channel ID from the config
        log_channel_id = await self.config.guild(ctx.guild).log_channel()
        log_channel = ctx.guild.get_channel(log_channel_id) if log_channel_id else None

        if log_channel:
            # Collect messages from the async generator
            messages = [msg async for msg in ctx.channel.history(oldest_first=True)]

            # Create HTML content
            html_content = "<html><head><title>ModMail Transcript</title></head><body>"
            html_content += f"<h2>Transcript for {ctx.channel.name}</h2>"
            html_content += "<ul>"

            for msg in messages:
                timestamp = msg.created_at.strftime("%Y-%m-%d %H:%M:%S")
                author = msg.author.display_name
                content = msg.content.replace('\n', '<br>')

                html_content += f"<li><strong>{timestamp} - {author}:</strong> {content}</li>"

                for embed in msg.embeds:
                    html_content += "<li><strong>Embed:</strong><ul>"
                    if embed.title:
                        html_content += f"<li><strong>Title:</strong> {embed.title}</li>"
                    if embed.description:
                        html_content += f"<li><strong>Description:</strong> {embed.description}</li>"
                    for field in embed.fields:
                        html_content += f"<li><strong>{field.name}:</strong> {field.value}</li>"
                    if embed.footer.text:
                        html_content += f"<li><strong>Footer:</strong> {embed.footer.text}</li>"
                    html_content += "</ul></li>"

            html_content += "</ul></body></html>"

            # Use io.BytesIO to create a file-like object
            log_file = io.BytesIO(html_content.encode('utf-8'))

            # Send the log file to the log channel
            await log_channel.send(content=f"Log for {ctx.channel.name}", file=discord.File(fp=log_file, filename=f"modmail-{ctx.channel.name}.html"))

        await ctx.send("This thread is now closed.")
        await ctx.channel.delete()

    @thread.command(name="open")
    async def thread_open(self, ctx: commands.Context, user: discord.Member = None):
        """Open a modmail thread with the server."""
        if ctx.channel.type != discord.ChannelType.text:
            await ctx.send("This command can only be used in a server text channel.")
            return

        if user is None:
            user = ctx.author

        modmail_channel_id = await self.config.guild(ctx.guild).modmail_channel()
        if not modmail_channel_id:
            await ctx.send("ModMail channel is not set for this server.")
            return

        modmail_channel = ctx.guild.get_channel(modmail_channel_id)
        if modmail_channel is None:
            await ctx.send("ModMail channel not found.")
            return

        # Ensure only one thread per user
        existing_thread = discord.utils.get(modmail_channel.threads, name=f"ModMail-{user.id}-{user.display_name}")
        if existing_thread:
            await ctx.send(f"{user.display_name} already has an open thread.")
            return

        thread = await modmail_channel.create_thread(name=f"ModMail-{user.id}-{user.display_name}", type=discord.ChannelType.public_thread)

        # Create and send the info embed
        roles = ', '.join([role.name for role in user.roles if role.name != "@everyone"])
        joined_at = user.joined_at.strftime("%Y-%m-%d %H:%M:%S")
        info_embed = discord.Embed(
            title=user.display_name,
            description=f"User ID: {user.id}",
            color=discord.Color.blue()
        )
        info_embed.add_field(name="Roles", value=roles or "No roles", inline=False)
        info_embed.add_field(name="Joined The Server", value=joined_at, inline=False)
        await thread.send(embed=info_embed)

        # Send DM to the user
        try:
            dm_embed = discord.Embed(
                title="Thread Opened",
                description=f"You opened a thread in `{ctx.guild.name}`. Please state your concerns here.",
                color=discord.Color.green()
            )
            await user.send(embed=dm_embed)
        except discord.HTTPException:
            await ctx.send(f"Could not send a DM to {user.display_name}.")

        await ctx.send(f"Modmail thread for {user.display_name} has been opened.")

    @thread.command(name="add")
    @commands.mod_or_permissions(manage_messages=True)
    async def thread_add(self, ctx: commands.Context, user: discord.User):
        """Add a user to receive replies for threads in the DMs."""
        authorized_users = await self.config.guild(ctx.guild).authorized_users()
        if user.id in authorized_users:
            await ctx.send(f"{user.display_name} is already authorized to receive thread replies.")
            return

        authorized_users.append(user.id)
        await self.config.guild(ctx.guild).authorized_users.set(authorized_users)
        await ctx.send(f"{user.display_name} has been added to receive thread replies.")

    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    @commands.command()
    async def setup(self, ctx: commands.Context):
        """Setup the modmail system with initial configuration."""
        questions = [
            "What channel for the threads?",
            "What channel for the logs? (Type `None` for no logs)",
            "What name for areply embed? (Type `None` for default 'Support Team')"
        ]
        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("Let's set up your ModMail system. Type `cancel` at any time to stop the setup.")

        for question in questions:
            await ctx.send(question)
            try:
                message = await self.bot.wait_for('message', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("Setup timed out. Please try again.")
                return

            if message.content.lower() == "cancel":
                await ctx.send("Setup has been cancelled.")
                return

            answers.append(message.content)

        # Process answers
        try:
            # Set modmail channel
            modmail_channel = discord.utils.get(ctx.guild.channels, mention=answers[0]) or ctx.guild.get_channel(int(answers[0]))
            if not modmail_channel or not isinstance(modmail_channel, discord.TextChannel):
                await ctx.send("Invalid channel for threads. Setup failed.")
                return
            await self.config.guild(ctx.guild).modmail_channel.set(modmail_channel.id)

            # Set log channel
            if answers[1].lower() != "none":
                log_channel = discord.utils.get(ctx.guild.channels, mention=answers[1]) or ctx.guild.get_channel(int(answers[1]))
                if not log_channel or not isinstance(log_channel, discord.TextChannel):
                    await ctx.send("Invalid channel for logs. Setup failed.")
                    return
                await self.config.guild(ctx.guild).log_channel.set(log_channel.id)
            else:
                await self.config.guild(ctx.guild).log_channel.set(None)

            # Set areply name
            areply_name = answers[2] if answers[2].lower() != "none" else "Support Team"
            await self.config.guild(ctx.guild).areply_name.set(areply_name)

            await ctx.send("ModMail setup complete!")
        except Exception as e:
            await ctx.send(f"An error occurred during setup: {e}")
