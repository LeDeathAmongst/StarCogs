import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from Star_Utils import Cog, CogsUtils, Settings
import io
from datetime import datetime
import re
import asyncio
import typing
from typing import List, Dict, Union, Literal
import random

class SnippetError(Exception):
    pass

class SnippetAlreadyExists(SnippetError):
    pass

class SnippetNotFound(SnippetError):
    pass

class SnippetResponseTooLong(SnippetError):
    pass

class SnippetObj:
    def __init__(self, **kwargs):
        self.config = kwargs.get("config")
        self.bot = kwargs.get("bot")
        self.db = self.config.guild

    async def get_snippets(self, guild: discord.Guild) -> dict:
        _snippets = await self.db(guild).get_raw("snippets", default={})
        return {k: v for k, v in _snippets.items() if _snippets[k]}

    async def create_snippet(self, ctx: commands.Context, name: str, response: Union[str, List[str]]):
        if await self.db(ctx.guild).get_raw("snippets", name, default=None):
            raise SnippetAlreadyExists()
        if isinstance(response, str) and len(response) > 2000:
            raise SnippetResponseTooLong()
        elif isinstance(response, list) and any(len(i) > 2000 for i in response):
            raise SnippetResponseTooLong()

        snippet_info = {
            "author": {"id": ctx.author.id, "name": str(ctx.author)},
            "name": name,
            "response": response,
        }
        await self.db(ctx.guild).set_raw("snippets", name, value=snippet_info)

    async def edit_snippet(self, ctx: commands.Context, name: str, response: Union[str, List[str]]):
        snippet_info = await self.db(ctx.guild).get_raw("snippets", name, default=None)
        if not snippet_info:
            raise SnippetNotFound()

        if isinstance(response, str) and len(response) > 2000:
            raise SnippetResponseTooLong()
        elif isinstance(response, list) and any(len(i) > 2000 for i in response):
            raise SnippetResponseTooLong()

        snippet_info["response"] = response
        await self.db(ctx.guild).set_raw("snippets", name, value=snippet_info)

    async def delete_snippet(self, ctx: commands.Context, name: str):
        if not await self.db(ctx.guild).get_raw("snippets", name, default=None):
            raise SnippetNotFound()
        await self.db(ctx.guild).set_raw("snippets", name, value=None)

    async def get_responses(self, ctx):
        await ctx.send("Enter responses for the snippet. Type `exit()` to finish.")
        responses = []
        while True:
            msg = await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            if msg.content.lower() == "exit()":
                break
            elif len(msg.content) > 2000:
                await ctx.send("Response is too long. Please enter a response under 2000 characters.")
                continue
            responses.append(msg.content)
        return responses

class ModMail(Cog):
    """A basic ModMail cog with snippet management"""

    def __init__(self, bot: Red):
        self.bot = bot

        # Define the settings structure
        settings = {
            "modmail_channel": {
                "path": ["modmail_channel"],
                "converter": discord.TextChannel,
                "command_name": "channel",
                "label": "ModMail Channel",
                "description": "Set the modmail channel for this server.",
            },
            "log_channel": {
                "path": ["log_channel"],
                "converter": discord.TextChannel,
                "command_name": "log",
                "label": "Log Channel",
                "description": "Set the log channel for this server.",
            },
            "areply_name": {
                "path": ["areply_name"],
                "converter": str,
                "command_name": "title",
                "label": "Areply Name",
                "description": "Set the areply title name.",
            },
            "snippet_reply_method": {
                "path": ["snippet_reply_method"],
                "converter": Literal["reply", "areply"],
                "command_name": "snippetmethod",
                "label": "Snippet Reply Method",
                "description": "Set the method for sending snippets (reply/areply).",
            },
            "modmail_enabled": {
                "path": ["modmail_enabled"],
                "converter": bool,
                "command_name": "toggle",
                "label": "ModMail Enabled",
                "description": "Toggle the ModMail system on or off for this server.",
            },
            "close_embed": {
                "path": ["close_embed"],
                "converter": str,
                "command_name": "closeembed",
                "label": "Close Embed Message",
                "description": "Set the embed message for channel closure.",
            },
            "open_embed": {
                "path": ["open_embed"],
                "converter": str,
                "command_name": "openembed",
                "label": "Open Embed Message",
                "description": "Set the embed message for opening a modmail thread.",
                "default": "Thank you for contacting {server_name}! Staff will be with you shortly!"
            },
            "snippets": {
                "path": ["snippets"],
                "converter": dict,
                "command_name": "snippets",
                "label": "Snippets",
                "description": "Manage snippets.",
                "default": {}
            }
        }

        # Initialize Settings
        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=Config.get_conf(self, identifier=1234567890, force_registration=True),
            group=Config.GUILD,
            settings=settings,
            guild_specific=True
        )

        self.snippetobj = SnippetObj(config=self.settings.config, bot=self.bot)

        # Initialize logger
        self.logger = CogsUtils.get_logger(cog=self)

        # Temporary storage for user-server selections
        self.user_guild_selection = {}

    async def cog_load(self):
        # Load snippet commands on cog load
        for guild in self.bot.guilds:
            await self.load_snippet_commands(guild)

    async def load_snippet_commands(self, guild: discord.Guild):
        snippets = await self.snippetobj.get_snippets(guild)
        for name, snippet_info in snippets.items():
            self.add_snippet_command(name, snippet_info["response"], guild.id)

    def add_snippet_command(self, name: str, responses: Union[str, List[str]], guild_id: int):
        """Dynamically add a snippet command."""
        async def snippet_command(ctx: commands.Context):
            """Send a snippet response."""
            if ctx.guild.id != guild_id:
                return

            # Determine the response
            if isinstance(responses, list):
                response = random.choice(responses)
            else:
                response = responses

            # Extract user ID from the channel name
            if ctx.channel.name.startswith("modmail-"):
                user_id_str = ctx.channel.name.split("modmail-")[1]
                user = self.bot.get_user(int(user_id_str))

                if user:
                    try:
                        # Create the embed for the snippet response
                        embed = discord.Embed(
                            description=response,
                            color=discord.Color.green()
                        )

                        # Determine the snippet reply method
                        snippet_method = await self.settings.get_raw("snippet_reply_method", ctx.guild)
                        if snippet_method == "areply":
                            areply_name = await self.settings.get_raw("areply_name", ctx.guild)
                            embed.set_author(name=areply_name)
                            footer_text = "Moderator/Admin"
                        else:
                            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
                            highest_role = max(ctx.author.roles, key=lambda r: r.position, default=None)
                            footer_text = highest_role.name if highest_role else "No role"

                        embed.set_footer(text=footer_text)

                        # Send the embed to the user's DM
                        await user.send(embed=embed)
                        await ctx.send(f"Snippet '{name}' sent to {user.display_name}.")
                    except discord.HTTPException:
                        await ctx.send("Failed to send snippet to the user's DM.")
                else:
                    await ctx.send("User not found.")
            else:
                await ctx.send("This command can only be used within a modmail thread channel.")

        # Add the command to the bot
        snippet_command.__name__ = f"snippet_{name}"
        command = commands.command(name=name)(snippet_command)
        self.bot.add_command(command)

    @commands.group()
    async def snippet(self, ctx: commands.Context):
        """Manage snippets."""
        pass

    @snippet.command(name="create")
    async def snippet_create(self, ctx: commands.Context, name: str):
        """Create a new snippet."""
        responses = await self.snippetobj.get_responses(ctx)
        if not responses:
            await ctx.send("Snippet creation cancelled.")
            return
        try:
            await self.snippetobj.create_snippet(ctx, name=name, response=responses)
            self.add_snippet_command(name, responses, ctx.guild.id)
            await ctx.send(f"Snippet '{name}' created successfully.")
        except SnippetAlreadyExists:
            await ctx.send("A snippet with this name already exists.")
        except SnippetResponseTooLong:
            await ctx.send("One of the responses is too long.")

    @snippet.command(name="edit")
    async def snippet_edit(self, ctx: commands.Context, name: str):
        """Edit an existing snippet."""
        responses = await self.snippetobj.get_responses(ctx)
        if not responses:
            await ctx.send("Snippet editing cancelled.")
            return
        try:
            await self.snippetobj.edit_snippet(ctx, name=name, response=responses)
            await self.remove_snippet_command(name)
            self.add_snippet_command(name, responses, ctx.guild.id)
            await ctx.send(f"Snippet '{name}' edited successfully.")
        except SnippetNotFound:
            await ctx.send("Snippet not found.")
        except SnippetResponseTooLong:
            await ctx.send("One of the responses is too long.")

    async def remove_snippet_command(self, name: str):
        """Remove a snippet command."""
        command_name = f"snippet_{name}"
        command = self.bot.get_command(command_name)
        if command:
            self.bot.remove_command(command_name)

    @snippet.command(name="delete")
    async def snippet_delete(self, ctx: commands.Context, name: str):
        """Delete a snippet."""
        try:
            await self.snippetobj.delete_snippet(ctx, name=name)
            await self.remove_snippet_command(name)
            await ctx.send(f"Snippet '{name}' deleted successfully.")
        except SnippetNotFound:
            await ctx.send("Snippet not found.")

    @snippet.command(name="list")
    async def snippet_list(self, ctx: commands.Context):
        """List all snippets."""
        snippets = await self.snippetobj.get_snippets(ctx.guild)
        if not snippets:
            await ctx.send("No snippets found.")
            return
        snippet_list = "\n".join(snippets.keys())
        await ctx.send(f"Snippets:\n{snippet_list}")

    @snippet.command(name="show")
    async def snippet_show(self, ctx: commands.Context, name: str):
        """Show a snippet's responses."""
        snippets = await self.snippetobj.get_snippets(ctx.guild)
        snippet_info = snippets.get(name)
        if not snippet_info:
            await ctx.send("Snippet not found.")
            return
        responses = snippet_info["response"]
        if isinstance(responses, list):
            response_text = "\n".join(responses)
        else:
            response_text = responses
        await ctx.send(f"Snippet '{name}' responses:\n{response_text}")

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        await self.load_snippet_commands(guild)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        snippets = await self.snippetobj.get_snippets(guild)
        for name in snippets:
            await self.remove_snippet_command(name)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if isinstance(message.channel, discord.DMChannel):
            user_id = message.author.id

            # Check if the user has already selected a server
            if user_id in self.user_guild_selection:
                selected_guild = self.user_guild_selection[user_id]
                await self.handle_modmail_message(message, selected_guild)
                return

            # Filter for configured guilds only
            configured_guilds = [guild for guild in self.bot.guilds if guild.get_member(user_id) and await self.settings.get_raw("modmail_channel", guild)]

            if not configured_guilds:
                return

            # Check for existing threads in configured guilds
            for guild in configured_guilds:
                modmail_channel_id = await self.settings.get_raw("modmail_channel", guild)
                modmail_channel = guild.get_channel(modmail_channel_id)
                if modmail_channel:
                    thread_name = f"modmail-{user_id}"
                    existing_thread = discord.utils.get(modmail_channel.threads, name=thread_name)
                    if existing_thread:
                        self.user_guild_selection[user_id] = guild
                        await self.handle_modmail_message(message, guild)
                        return

            # If no existing thread, ask the user to choose a server
            if len(configured_guilds) == 1:
                # If there's only one configured server, use it automatically
                self.user_guild_selection[user_id] = configured_guilds[0]
                await self.handle_modmail_message(message, configured_guilds[0])
            else:
                # Ask the user to choose a server with reactions
                embed = discord.Embed(
                    title="Select a Server",
                    description="React with the corresponding number to select a server for ModMail.",
                    color=discord.Color.blue()
                )
                for i, guild in enumerate(configured_guilds):
                    embed.add_field(name=f"{i+1}. {guild.name}", value="\u200b", inline=False)

                selection_message = await message.author.send(embed=embed)

                # Add reactions for selection
                for i in range(len(configured_guilds)):
                    await selection_message.add_reaction(f"{i+1}\u20e3")

                def check_reaction(reaction, user):
                    return user == message.author and reaction.message.id == selection_message.id

                try:
                    reaction, user = await self.bot.wait_for('reaction_add', check=check_reaction, timeout=60.0)
                    selected_index = int(reaction.emoji[0]) - 1
                    if 0 <= selected_index < len(configured_guilds):
                        selected_guild = configured_guilds[selected_index]
                        self.user_guild_selection[user_id] = selected_guild

                        # Delete the selection message
                        await selection_message.delete()

                        # Handle the modmail message
                        await self.handle_modmail_message(message, selected_guild)
                    else:
                        await message.author.send("Invalid selection. Please try again.")
                except asyncio.TimeoutError:
                    await message.author.send("You did not respond in time. Please try again.")

    async def handle_modmail_message(self, message: discord.Message, guild: discord.Guild):
        """Handle incoming ModMail messages for a specific guild."""
        modmail_enabled = await self.settings.get_raw("modmail_enabled", guild)
        if not modmail_enabled:
            return

        modmail_channel_id = await self.settings.get_raw("modmail_channel", guild)
        modmail_channel = guild.get_channel(modmail_channel_id)
        if modmail_channel is None or not isinstance(modmail_channel, discord.TextChannel):
            return

        # Check if a thread already exists for this user
        thread_name = f"modmail-{message.author.id}"
        existing_thread = discord.utils.get(modmail_channel.threads, name=thread_name)
        if existing_thread:
            thread = existing_thread
        else:
            # Create a new thread under the specified channel
            thread = await modmail_channel.create_thread(
                name=thread_name,
                type=discord.ChannelType.public_thread,
                reason=f"ModMail for {message.author} ({message.author.id})"
            )

        # Send the message content
        content_embed = discord.Embed(
            description=message.content,
            color=discord.Color.blue()
        )
        if message.author.avatar:
            content_embed.set_author(name=f"{message.author.display_name} ({message.author.id})", icon_url=message.author.avatar.url)
        else:
            content_embed.set_author(name=f"{message.author.display_name} ({message.author.id})")

        imgur_links = re.findall(r'(https?://i\.imgur\.com/\S+\.(?:jpg|jpeg|png|gif))', message.content)
        if imgur_links:
            content_embed.set_image(url=imgur_links[0])

        await thread.send(embed=content_embed)

    @commands.guild_only()
    @commands.group()
    async def config(self, ctx: commands.Context):
        """Configuration commands for modmail."""
        pass

    @config.command(name="channel")
    async def config_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the modmail channel for this server."""
        await self.settings.set_raw("modmail_channel", channel.id, ctx.guild)
        await ctx.send(f"ModMail channel set to {channel.mention}")

    @config.command(name="log")
    async def config_log(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the log channel for this server."""
        await self.settings.set_raw("log_channel", channel.id, ctx.guild)
        await ctx.send(f"Log channel set to {channel.mention}")

    @config.command(name="title")
    async def config_title(self, ctx: commands.Context, *, title: str):
        """Set the areply title name."""
        await self.settings.set_raw("areply_name", title, ctx.guild)
        await ctx.send(f"Areply title name set to {title}")

    @config.command(name="snippetmethod")
    async def config_snippet_method(self, ctx: commands.Context, method: str):
        """Set the method for sending snippets (reply/areply)."""
        if method not in ["reply", "areply"]:
            await ctx.send("Invalid method. Please choose either 'reply' or 'areply'.")
            return
        await self.settings.set_raw("snippet_reply_method", method, ctx.guild)
        await ctx.send(f"Snippet sending method set to {method}.")

    @config.command(name="toggle")
    async def config_toggle(self, ctx: commands.Context):
        """Toggle the ModMail system on or off for this server."""
        current_state = await self.settings.get_raw("modmail_enabled", ctx.guild)
        new_state = not current_state
        await self.settings.set_raw("modmail_enabled", new_state, ctx.guild)
        state_text = "enabled" if new_state else "disabled"
        await ctx.send(f"ModMail has been {state_text} for this server.")

    @config.command(name="closeembed")
    async def config_close_embed(self, ctx: commands.Context, *, embed_message: str):
        """Set the embed message for channel closure."""
        await self.settings.set_raw("close_embed", embed_message, ctx.guild)
        await ctx.send("Close embed message set.")

    @config.command(name="openembed")
    async def config_open_embed(self, ctx: commands.Context, *, embed_message: str):
        """Set the embed message for opening a modmail thread."""
        await self.settings.set_raw("open_embed", embed_message, ctx.guild)
        await ctx.send("Open embed message set.")

    @commands.guild_only()
    @commands.mod_or_permissions(manage_messages=True)
    @commands.command(aliases=["r"])
    async def reply(self, ctx: commands.Context, *, response: str):
        """Reply to a user via ModMail from within a channel."""
        if not ctx.channel.name.startswith("modmail-"):
            await ctx.send("This command can only be used within a modmail channel.")
            return

        user_id_str = ctx.channel.name.split("modmail-")[1]
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
        if ctx.author.avatar:
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        else:
            embed.set_author(name=ctx.author.display_name)

        highest_role = max(ctx.author.roles, key=lambda r: r.position, default=None)
        footer_text = highest_role.name if highest_role else "No role"
        embed.set_footer(text=footer_text)

        await user.send(embed=embed)

        # Log the response in the channel
        await ctx.send(f"Reply sent to {user.mention}: {response}")

    @commands.guild_only()
    @commands.mod_or_permissions(manage_messages=True)
    @commands.command(aliases=["ar"])
    async def areply(self, ctx: commands.Context, *, response: str):
        """Reply to a user via ModMail with a generic support team title from within a channel."""
        if not ctx.channel.name.startswith("modmail-"):
            await ctx.send("This command can only be used within a modmail channel.")
            return

        user_id_str = ctx.channel.name.split("modmail-")[1]
        user = self.bot.get_user(int(user_id_str))

        if user is None:
            await ctx.send("User not found.")
            return

        areply_name = await self.settings.get_raw("areply_name", ctx.guild)

        # Send the response to the user
        embed = discord.Embed(
            title=areply_name,
            description=response,
            color=discord.Color.green()
        )
        if ctx.guild.icon:
            embed.set_author(name=areply_name, icon_url=ctx.guild.icon.url)
        else:
            embed.set_author(name=areply_name)

        footer_text = "Moderator/Admin"
        embed.set_footer(text=footer_text)

        await user.send(embed=embed)

        # Log the response in the channel
        await ctx.send(f"Reply sent to {user.mention}: {response}")

    @commands.guild_only()
    @commands.group()
    async def thread(self, ctx: commands.Context):
        """Manage modmail channels."""
        pass

    @thread.command(name="close")
    @commands.mod_or_permissions(manage_messages=True)
    async def thread_close(self, ctx: commands.Context, delay: str = None):
        """Close the modmail channel and generate a log. Optionally delay the closure with format like 10s, 10m, 10h."""
        if not ctx.channel.name.startswith("modmail-"):
            await ctx.send("This command can only be used within a modmail channel.")
            return

        # Parse the delay argument
        delay_seconds = 0
        if delay:
            match = re.match(r"(\d+)([smh])", delay)
            if match:
                amount = int(match.group(1))
                unit = match.group(2)
                if unit == 's':
                    delay_seconds = amount
                elif unit == 'm':
                    delay_seconds = amount * 60
                elif unit == 'h':
                    delay_seconds = amount * 3600
            else:
                await ctx.send("Invalid delay format. Please use formats like 10s, 10m, 10h.")
                return

        # Get the log channel ID from the settings
        log_channel_id = await self.settings.get_raw("log_channel", ctx.guild)
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

        close_embed_message = await self.settings.get_raw("close_embed", ctx.guild)

        user_id_str = ctx.channel.name.split("modmail-")[1]
        user = self.bot.get_user(int(user_id_str))

        if close_embed_message and user:
            close_embed = discord.Embed(description=close_embed_message, color=discord.Color.red())
            await user.send(embed=close_embed)

        if delay_seconds > 0:
            await ctx.send(f"This channel will close in {delay_seconds} seconds.")
            await asyncio.sleep(delay_seconds)
        else:
            await ctx.send("This channel is now closed.")

        # Forget the user's selected server
        user_id = int(user_id_str)
        if user_id in self.user_guild_selection:
            del self.user_guild_selection[user_id]

        await ctx.channel.delete()

    @thread.command(name="open")
    async def thread_open(self, ctx: commands.Context, user: discord.Member = None):
        """Open a modmail channel with the server."""
        if ctx.channel.type != discord.ChannelType.text:
            await ctx.send("This command can only be used in a server text channel.")
            return

        if user is None:
            user = ctx.author

        modmail_channel_id = await self.settings.get_raw("modmail_channel", ctx.guild)
        modmail_channel = ctx.guild.get_channel(modmail_channel_id)
        if modmail_channel is None or not isinstance(modmail_channel, discord.TextChannel):
            await ctx.send("ModMail channel is not set or invalid for this server.")
            return

        # Check if a thread already exists for this user
        thread_name = f"modmail-{user.id}"
        existing_thread = discord.utils.get(modmail_channel.threads, name=thread_name)
        if existing_thread:
            await ctx.send(f"{user.display_name} already has an open thread.")
            return

        thread = await modmail_channel.create_thread(
            name=thread_name,
            type=discord.ChannelType.public_thread,
            reason=f"ModMail for {user} ({user.id})"
        )

        # Store the thread reference
        self.user_guild_selection[user.id] = ctx.guild

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

        # Send the configured opening message to the user
        open_embed_message = await self.settings.get_raw("open_embed", ctx.guild)
        if open_embed_message:
            open_embed = discord.Embed(description=open_embed_message.format(server_name=ctx.guild.name), color=discord.Color.green())
            try:
                await user.send(embed=open_embed)
            except discord.HTTPException:
                await ctx.send(f"Could not send the opening message to {user.display_name}.")

        # Notify the server that the thread has been opened
        await ctx.send(f"Modmail thread for {user.display_name} has been opened.")

    @thread.command(name="add")
    @commands.mod_or_permissions(manage_messages=True)
    async def thread_add(self, ctx: commands.Context, user: discord.User):
        """Add a user to receive replies for channels in the DMs."""
        authorized_users = await self.settings.get_raw("authorized_users", ctx.guild)
        if user.id in authorized_users:
            await ctx.send(f"{user.display_name} is already authorized to receive channel replies.")
            return

        authorized_users.append(user.id)
        await self.settings.set_raw("authorized_users", authorized_users, ctx.guild)
        await ctx.send(f"{user.display_name} has been added to receive channel replies.")

    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    @commands.command()
    async def setup(self, ctx: commands.Context):
        """Setup the modmail system with initial configuration."""
        questions = [
            "What channel for the threads?",
            "What channel for the logs? (Type `None` for no logs)",
            "What name for areply embed? (Type `None` for default 'Support Team')",
            "What message to display on channel closure? (Type `None` for no message)",
            "What message to display when a modmail is opened? (Type `None` for no message)"
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
            await self.settings.set_raw("modmail_channel", modmail_channel.id, ctx.guild)

            # Set log channel
            if answers[1].lower() != "none":
                log_channel = discord.utils.get(ctx.guild.channels, mention=answers[1]) or ctx.guild.get_channel(int(answers[1]))
                if not log_channel or not isinstance(log_channel, discord.TextChannel):
                    await ctx.send("Invalid channel for logs. Setup failed.")
                    return
                await self.settings.set_raw("log_channel", log_channel.id, ctx.guild)
            else:
                await self.settings.set_raw("log_channel", None, ctx.guild)

            # Set areply name
            areply_name = answers[2] if answers[2].lower() != "none" else "Support Team"
            await self.settings.set_raw("areply_name", areply_name, ctx.guild)

            # Set close embed message
            close_embed_message = answers[3] if answers[3].lower() != "none" else None
            await self.settings.set_raw("close_embed", close_embed_message, ctx.guild)

            # Set open embed message
            open_embed_message = answers[4] if answers[4].lower() != "none" else None
            await self.settings.set_raw("open_embed", open_embed_message, ctx.guild)

            await ctx.send("ModMail setup complete!")
        except Exception as e:
            await ctx.send(f"An error occurred during setup: {e}")
