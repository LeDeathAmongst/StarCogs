import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from Star_Utils import Cog
import os
import datetime

class ModMail(Cog):
    """A modmail cog for Red-DiscordBot."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_guild = {
            "modmail_channel": None,
            "areply_name": "Support Team",
            "preconfigured_messages": {},
            "authorized_users": []
        }
        self.config.register_guild(**default_guild)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or not isinstance(message.channel, discord.DMChannel):
            return

        # User sent a DM to the bot
        for guild in self.bot.guilds:
            modmail_channel_id = await self.config.guild(guild).modmail_channel()
            if not modmail_channel_id:
                continue

            modmail_channel = guild.get_channel(modmail_channel_id)
            if modmail_channel is None:
                continue

            # Ensure only one thread per user
            existing_thread = discord.utils.get(modmail_channel.threads, name=f"ModMail-{message.author.id}")
            if existing_thread:
                thread = existing_thread
            else:
                thread = await modmail_channel.create_thread(name=f"ModMail-{message.author.id}", type=discord.ChannelType.public_thread)

                # Create and send the info embed
                roles = ', '.join([role.name for role in message.author.roles if role.name != "@everyone"])
                joined_at = message.author.joined_at.strftime("%Y-%m-%d %H:%M:%S")
                info_embed = discord.Embed(
                    title=message.author.display_name,
                    description=f"User ID: {message.author.id}",
                    color=discord.Color.blue()
                )
                info_embed.add_field(name="Roles", value=roles or "No roles", inline=False)
                info_embed.add_field(name="Joined The Server", value=joined_at, inline=False)
                await thread.send(embed=info_embed)

            # Send the message content
            content_embed = discord.Embed(
                description=message.content,
                color=discord.Color.blue()
            )
            content_embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
            await thread.send(embed=content_embed)
            break

    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    @commands.command()
    async def setmodmail(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the modmail channel for this server."""
        await self.config.guild(ctx.guild).modmail_channel.set(channel.id)
        await ctx.send(f"ModMail channel set to {channel.mention}")

    @commands.guild_only()
    @commands.mod_or_permissions(manage_messages=True)
    @commands.command(aliases=["r"])
    async def reply(self, ctx: commands.Context, *, response: str):
        """Reply to a user via ModMail from within a thread."""
        if ctx.channel.type != discord.ChannelType.public_thread:
            await ctx.send("This command can only be used within a modmail thread.")
            return

        user_id_str = ctx.channel.name.split("ModMail-")[-1]
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

        user_id_str = ctx.channel.name.split("ModMail-")[-1]
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
        await user.send(embed=embed)

        # Log the response in the thread
        await ctx.send(f"Reply sent to {user.mention}: {response}")

    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    @commands.command()
    async def setareplyname(self, ctx: commands.Context, *, name: str):
        """Set the name used for areply responses."""
        await self.config.guild(ctx.guild).areply_name.set(name)
        await ctx.send(f"Areply name set to {name}")

    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    @commands.group()
    async def snippet(self, ctx: commands.Context):
        """Manage pre-configured message snippets."""
        if ctx.invoked_subcommand is None:
            await ctx.send("Please specify a valid subcommand: add, send, edit, remove.")

    @snippet.command(name="add")
    async def snippet_add(self, ctx: commands.Context, name: str, *, message: str):
        """Add a new snippet."""
        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        preconfigured_messages[name] = message
        await self.config.guild(ctx.guild).preconfigured_messages.set(preconfigured_messages)
        await ctx.send(f"Snippet '{name}' added.")

    @snippet.command(name="send")
    async def snippet_send(self, ctx: commands.Context, name: str):
        """Send a snippet to a user from within a thread."""
        if ctx.channel.type != discord.ChannelType.public_thread:
            await ctx.send("This command can only be used within a modmail thread.")
            return

        user_id_str = ctx.channel.name.split("ModMail-")[-1]
        user = self.bot.get_user(int(user_id_str))

        if user is None:
            await ctx.send("User not found.")
            return

        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        if name not in preconfigured_messages:
            await ctx.send(f"No snippet found with name '{name}'.")
            return

        message = preconfigured_messages[name]

        # Send the snippet message to the user
        embed = discord.Embed(
            title=user.display_name,
            description=message,
            color=discord.Color.green()
        )
        await user.send(embed=embed)

        # Log the response in the thread
        await ctx.send(f"Snippet '{name}' sent to {user.mention}.")

    @snippet.command(name="edit")
    async def snippet_edit(self, ctx: commands.Context, name: str, *, new_content: str):
        """Edit an existing snippet."""
        preconfigured_messages = await self.config.guild(ctx.guild).preconfigured_messages()
        if name not in preconfigured_messages:
            await ctx.send(f"No snippet found with name '{name}'.")
            return

        preconfigured_messages[name] = new_content
        await self.config.guild(ctx.guild).preconfigured_messages.set(preconfigured_messages)
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
        await ctx.send(f"Snippet '{name}' removed.")

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

        # Collect messages from the async generator
        messages = [msg async for msg in ctx.channel.history(oldest_first=True)]
        log_content = "\n".join([f"{msg.created_at} - {msg.author}: {msg.content}" for msg in messages])
        log_filename = f"modmail_log_{ctx.channel.name}.txt"
        with open(log_filename, "w", encoding="utf-8") as log_file:
            log_file.write(log_content)

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
        existing_thread = discord.utils.get(modmail_channel.threads, name=f"ModMail-{user.id}")
        if existing_thread:
            await ctx.send(f"{user.display_name} already has an open thread.")
            return

        thread = await modmail_channel.create_thread(name=f"ModMail-{user.id}", type=discord.ChannelType.public_thread)

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
