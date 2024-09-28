import discord
import os
from redbot.core import commands, Config
from datetime import datetime, timedelta
import re
from Star_Utils import Cog

class WormHole(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier="wormhole", force_registration=True)
        self.config.register_global(
            linked_channels_list=[],
            global_blacklist=[],
            word_filters=[],
            mention_bypass_users=[],
            use_webhooks=True,
            image_mode="user",
            name_mode="user"
        )
        self.message_references = {}
        self.relayed_messages = {}
        self.user_ping_count = {}
        self.recent_messages = {}
        self.webhook_cache = {}

        self.bot.remove_command('command_to_remove')

    async def get_webhook(self, channel):
        if channel.id in self.webhook_cache:
            return self.webhook_cache[channel.id]
        webhooks = await channel.webhooks()
        for webhook in webhooks:
            if webhook.user == self.bot.user:
                self.webhook_cache[channel.id] = webhook
                return webhook
        webhook = await channel.create_webhook(name="Wormhole Relay")
        self.webhook_cache[channel.id] = webhook
        return webhook

    async def send_status_message(self, message, channel, title):
        linked_channels = await self.config.linked_channels_list()
        guild = channel.guild
        embed = discord.Embed(title=title, description=f"{guild.name}: {message}")
        for channel_id in linked_channels:
            relay_channel = self.bot.get_channel(channel_id)
            if relay_channel and relay_channel != channel:
                await relay_channel.send(embed=embed)

    async def send_mention_embed(self, mentioned_user, where, who, content):
        embed = discord.Embed(title="You got mentioned")
        embed.add_field(name="Where", value=where, inline=False)
        embed.add_field(name="Who", value=who, inline=False)
        embed.add_field(name="Content", value=content[:25] + ('...' if len(content) > 25 else ''), inline=False)
        try:
            await mentioned_user.send(embed=embed)
        except discord.Forbidden:
            pass

    @commands.group(name="wormhole", aliases=["wm"], invoke_without_command=True)
    async def wormhole(self, ctx):
        """Manage wormhole connections."""
        await ctx.send_help(ctx.command)

    @wormhole.command(name="open")
    async def wormhole_open(self, ctx):
        """Link the current channel to the wormhole network."""
        linked_channels = await self.config.linked_channels_list()
        if ctx.channel.id not in linked_channels:
            linked_channels.append(ctx.channel.id)
            await self.config.linked_channels_list.set(linked_channels)
            embed = discord.Embed(title="Success!", description="This channel has joined the ever-changing maelstrom that is the wormhole.")
            await ctx.send(embed=embed)
            await self.send_status_message(f"A faint signal was picked up from {ctx.channel.mention}, connection has been established.", ctx.channel, "Success!")
        else:
            embed = discord.Embed(title="ErRoR 404", description="This channel is already part of the wormhole.")
            await ctx.send(embed=embed)

    @wormhole.command(name="close")
    async def wormhole_close(self, ctx):
        """Unlink the current channel from the wormhole network."""
        linked_channels = await self.config.linked_channels_list()
        if ctx.channel.id in linked_channels:
            linked_channels.remove(ctx.channel.id)
            await self.config.linked_channels_list.set(linked_channels)
            embed = discord.Embed(title="Success!", description="This channel has been severed from the wormhole.")
            await ctx.send(embed=embed)
            await self.send_status_message(f"The signal from {ctx.channel.mention} has become too faint to be picked up, the connection was lost.", ctx.channel, "Success!")
        else:
            embed = discord.Embed(title="ErRoR 404", description="This channel is not part of the wormhole.")
            await ctx.send(embed=embed)

    @wormhole.command(name="ownerclose")
    @commands.is_owner()
    async def wormhole_ownerclose(self, ctx, channel_id: int):
        """Forcibly close a connection to the wormhole (Bot Owner Only)."""
        linked_channels = await self.config.linked_channels_list()
        if channel_id in linked_channels:
            linked_channels.remove(channel_id)
            await self.config.linked_channels_list.set(linked_channels)
            channel = self.bot.get_channel(channel_id)
            if channel:
                embed = discord.Embed(title="Success!", description=f"The channel {channel.mention} (ID: {channel_id}) has been forcibly severed from the wormhole.")
                await ctx.send(embed=embed)
                await self.send_status_message(f"The signal from {channel.mention} has been forcibly severed by the bot owner.", channel, "Success!")
            else:
                embed = discord.Embed(title="Success!", description=f"The channel ID {channel_id} has been forcibly severed from the wormhole.")
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="ErRoR 404", description=f"The channel ID {channel_id} is not part of the wormhole.")
            await ctx.send(embed=embed)

    @wormhole.command(name="servers")
    async def wormhole_servers(self, ctx):
        """List all servers connected to the wormhole."""
        linked_channels = await self.config.linked_channels_list()
        if not linked_channels:
            await ctx.send(embed=discord.Embed(title="Wormhole Servers", description="No channels are currently linked to the wormhole.", color=discord.Color.red()))
            return

        server_list = {}
        for channel_id in linked_channels:
            channel = self.bot.get_channel(channel_id)
            if channel:
                guild = channel.guild
                if guild not in server_list:
                    server_list[guild] = []
                server_list[guild].append(channel)

        if not server_list:
            await ctx.send(embed=discord.Embed(title="Wormhole Servers", description="No servers are currently linked to the wormhole.", color=discord.Color.red()))
            return

        embed = discord.Embed(title="Connected Servers", color=discord.Color.blue())
        description = ""
        for guild, channels in server_list.items():
            owner = guild.owner
            for channel in channels:
                description += (
                    f"**{guild.name}**\n"
                    f"Owner: {owner} (ID: {owner.id})\n"
                    f"Server ID: {guild.id}\n"
                    f"Channel: {channel.mention} (ID: {channel.id})\n\n"
                )
                if len(description) > 1800:
                    embed.description = description
                    await ctx.send(embed=embed)
                    embed = discord.Embed(title="Connected Servers", color=discord.Color.blue())
                    description = ""

        if description:
            embed.description = description
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if not message.guild:
            return
        if message.author.bot or not message.channel.permissions_for(message.guild.me).send_messages:
            return

        linked_channels = await self.config.linked_channels_list()

        if message.channel.id in linked_channels:
            global_blacklist = await self.config.global_blacklist()
            word_filters = await self.config.word_filters()

            if message.author.id in global_blacklist:
                return

            if any(word in message.content for word in word_filters):
                embed = discord.Embed(title="ErRoR 404", description="That word is not allowed.")
                await message.channel.send(embed=embed)
                await message.delete()
                return

            money_regex = r"[\$\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\]\d+(\.\d{1,2})?"
            if re.search(money_regex, message.content):
                try:
                    await message.author.kick(reason="Messages contained possible scam.")
                except discord.Forbidden:
                    await message.delete()
                    await message.channel.send(f"{message.author.name}, Your message contained a possible scam message. Please refrain from doing that in this server.")
                return

            if re.search(r"(discord\.gg/|discordapp\.com/invite/|discord\.me/|discord\.li/)", message.content):
                embed = discord.Embed(title="ErRoR 404", description="Invites are not allowed.")
                await message.channel.send(embed=embed)
                await message.delete()
                return

            display_name = message.author.display_name if message.author.display_name else message.author.name

            self.recent_messages[message.id] = {
                'author_id': message.author.id,
                'author_name': display_name,
                'guild_id': message.guild.id,
                'channel_id': message.channel.id,
                'timestamp': datetime.utcnow()
            }

            content = message.content
            content = content.replace("@everyone", "").replace("@here", "")

            mentioned_users = message.mentions
            mentioned_roles = message.role_mentions

            for user in mentioned_users:
                content = content.replace(f"<@{user.id}>", '')
            for role in mentioned_roles:
                content = content.replace(f"<@&{role.id}>", '')

            if not content.strip() and not message.attachments:
                await message.delete()
                return

            content = self.replace_emojis_with_urls(message.guild, content)

            use_webhooks = await self.config.use_webhooks()
            image_mode = await self.config.image_mode()
            name_mode = await self.config.name_mode()

            files = [await attachment.to_file() for attachment in message.attachments]

            if message.reference and message.reference.message_id in self.recent_messages:
                original_message_data = self.recent_messages[message.reference.message_id]
                reply_link = f"[Jump to message]({message.reference.jump_url})"
                content = f"*Replying to:* {reply_link}\n{content}"

            if use_webhooks:
                for channel_id in linked_channels:
                    if channel_id != message.channel.id:
                        relay_channel = self.bot.get_channel(channel_id)
                        if relay_channel:
                            webhook = await self.get_webhook(relay_channel)
                            if image_mode == "user":
                                avatar_url = message.author.avatar.url
                            else:
                                avatar_url = message.guild.icon.url if message.guild.icon else message.author.avatar.url

                            if name_mode == "user":
                                username = message.author.display_name
                            elif name_mode == "server":
                                username = message.guild.name
                            else:
                                username = f"{message.guild.name} - {message.author.display_name}"

                            await webhook.send(
                                content=content,
                                username=username,
                                avatar_url=avatar_url,
                                files=files
                            )
            else:
                for channel_id in linked_channels:
                    if channel_id != message.channel.id:
                        channel = self.bot.get_channel(channel_id)
                        if channel:
                            await channel.send(f"**{message.guild.name} - {display_name}:** {content}", files=files)

            for mentioned_user in mentioned_users:
                where = f"[Jump to message]({message.jump_url})"
                who = message.author.mention
                await self.send_mention_embed(mentioned_user, where, who, message.content)

        self.cleanup_old_messages()

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if not after.guild:
            return

        linked_channels = await self.config.linked_channels_list()

        if after.channel.id in linked_channels:
            display_name = after.author.display_name if after.author.display_name else after.author.name
            content = after.content
            content = content.replace("@everyone", "").replace("@here", "")

            mentioned_users = after.mentions
            mentioned_roles = after.role_mentions

            for user in mentioned_users:
                content = content.replace(f"<@{user.id}>", '')
            for role in mentioned_roles:
                content = content.replace(f"<@&{role.id}>", '')

            if any(word in content for word in await self.config.word_filters()):
                embed = discord.Embed(title="ErRoR 404", description="That word is not allowed.")
                await after.channel.send(embed=embed)
                await after.delete()
                return

            if not content.strip() and not after.attachments:
                await after.delete()
                return

            content = self.replace_emojis_with_urls(after.guild, content)

            for channel_id in linked_channels:
                if channel_id != after.channel.id:
                    channel = self.bot.get_channel(channel_id)
                    if channel:
                        if (before.id, channel_id) in self.relayed_messages:
                            relay_message_id = self.relayed_messages[(before.id, channel_id)]
                            relay_message = await channel.fetch_message(relay_message_id)
                            await relay_message.delete()
                            new_relay_message = await channel.send(f"**{after.guild.name} - {display_name} (edited):** {content}")
                            self.relayed_messages[(after.id, channel_id)] = new_relay_message.id

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if not message.guild:
            return

        linked_channels = await self.config.linked_channels_list()

        if message.channel.id in linked_channels:
            for channel_id in linked_channels:
                if channel_id != message.channel.id:
                    channel = self.bot.get_channel(channel_id)
                    if channel and (message.id, channel_id) in self.relayed_messages:
                        relay_message_id = self.relayed_messages[(message.id, channel_id)]
                        try:
                            relay_message = await channel.fetch_message(relay_message_id)
                            await relay_message.delete()
                        except discord.NotFound:
                            pass

        if message.id in self.recent_messages:
            del self.recent_messages[message.id]

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        linked_channels = await self.config.linked_channels_list()
        for channel_id in linked_channels:
            channel = self.bot.get_channel(channel_id)
            if channel:
                async for message in channel.history(limit=1000):
                    if message.author.id == user.id:
                        await message.delete()

    def replace_emojis_with_urls(self, guild, content):
        for emoji in guild.emojis:
            if str(emoji) in content:
                content = content.replace(str(emoji), str(emoji.url))
        return content

    def cleanup_old_messages(self):
        now = datetime.utcnow()
        cutoff = now - timedelta(hours=24)
        self.recent_messages = {msg_id: data for msg_id, data in self.recent_messages.items() if data['timestamp'] > cutoff}

    @wormhole.command(name="globalblacklist")
    async def wormhole_globalblacklist(self, ctx, user: discord.User):
        """Prevent specific members from sending messages through the wormhole globally."""
        if await self.bot.is_owner(ctx.author):
            global_blacklist = await self.config.global_blacklist()
            if user.id not in global_blacklist:
                global_blacklist.append(user.id)
                await self.config.global_blacklist.set(global_blacklist)
                embed = discord.Embed(title="Success!", description=f"{user.display_name} has been added to the global wormhole blacklist.")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="ErRoR 404", description=f"{user.display_name} is already in the global wormhole blacklist.")
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="ErRoR 404", description="You must be the bot owner to use this command.")
            await ctx.send(embed=embed)

    @wormhole.command(name="unglobalblacklist")
    async def wormhole_unglobalblacklist(self, ctx, user: discord.User):
        """Command to remove a user from the global wormhole blacklist (Bot Owner Only)."""
        if await self.bot.is_owner(ctx.author):
            global_blacklist = await self.config.global_blacklist()
            if user.id in global_blacklist:
                global_blacklist.remove(user.id)
                await self.config.global_blacklist.set(global_blacklist)
                embed = discord.Embed(title="Success!", description=f"{user.display_name} has been removed from the global wormhole blacklist.")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="ErRoR 404", description=f"{user.display_name} is not in the global wormhole blacklist.")
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="ErRoR 404", description="You must be the bot owner to use this command.")
            await ctx.send(embed=embed)

    @wormhole.command(name="addwordfilter")
    async def wormhole_addwordfilter(self, ctx, *, word: str):
        """Add a word to the wormhole word filter."""
        if await self.bot.is_owner(ctx.author):
            word_filters = await self.config.word_filters()
            if word not in word_filters:
                word_filters.append(word)
                await self.config.word_filters.set(word_filters)
                embed = discord.Embed(title="Success!", description=f"`{word}` has been added to the wormhole word filter.")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="ErRoR 404", description=f"`{word}` is already in the wormhole word filter.")
                await ctx.send(embed=embed)

    @wormhole.command(name="removewordfilter")
    async def wormhole_removewordfilter(self, ctx, *, word: str):
        """Remove a word from the wormhole word filter."""
        if await self.bot.is_owner(ctx.author):
            word_filters = await self.config.word_filters()
            if word in word_filters:
                word_filters.remove(word)
                await self.config.word_filters.set(word_filters)
                embed = discord.Embed(title="Success!", description=f"`{word}` has been removed from the wormhole word filter.")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="ErRoR 404", description=f"`{word}` is not in the wormhole word filter.")
                await ctx.send(embed=embed)

    @wormhole.command(name="addmentionbypass")
    @commands.is_owner()
    async def wormhole_addmentionbypass(self, ctx, user: discord.User):
        """Allow a user to bypass the mention filter."""
        mention_bypass_users = await self.config.mention_bypass_users()
        if user.id not in mention_bypass_users:
            mention_bypass_users.append(user.id)
            await self.config.mention_bypass_users.set(mention_bypass_users)
            embed = discord.Embed(title="Success!", description=f"{user.display_name} has been allowed to bypass the mention filter.")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="ErRoR 404", description=f"{user.display_name} is already allowed to bypass the mention filter.")
            await ctx.send(embed=embed)

    @wormhole.command(name="removementionbypass")
    @commands.is_owner()
    async def wormhole_removementionbypass(self, ctx, user: discord.User):
        """Remove a user's bypass for the mention filter."""
        mention_bypass_users = await self.config.mention_bypass_users()
        if user.id in mention_bypass_users:
            mention_bypass_users.remove(user.id)
            await self.config.mention_bypass_users.set(mention_bypass_users)
            embed = discord.Embed(title="Success!", description=f"{user.display_name} is no longer allowed to bypass the mention filter.")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="ErRoR 404", description=f"{user.display_name} is not allowed to bypass the mention filter.")
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        """Notify linked channels when a user is typing."""
        linked_channels = await self.config.linked_channels_list()
        if channel.id in linked_channels:
            for channel_id in linked_channels:
                if channel_id != channel.id:
                    relay_channel = self.bot.get_channel(channel_id)
                    if relay_channel:
                        await relay_channel.trigger_typing()
