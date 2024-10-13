<<<<<<< HEAD
from Star_Utils import Cog, Settings, CogsUtils
=======
from Star_Utils import Cog
>>>>>>> 9e308722 (Revamped and Fixed)
from redbot.core import commands, Config
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n
import discord
import typing
<<<<<<< HEAD
from typing import Union, List
=======
>>>>>>> 9e308722 (Revamped and Fixed)
import asyncio
from datetime import datetime
from .dashboard_integration import DashboardIntegration

<<<<<<< HEAD
_ = Translator('EventLogger', __file__)

@cog_i18n(_)
class EventLogger(DashboardIntegration, Cog):
    """Cog to log various Discord events"""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)

        settings_dict = {
                "integration_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging integration creation events.",
                },
                "integration_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging integration deletion events.",
                },
                "integration_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging integration update events.",
                },
                "guild_channel_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel creation events.",
                },
                "guild_channel_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel deletion events.",
                },
                "guild_channel_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel update events.",
                },
                "guild_channel_pins_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel pins update events.",
                },
                "voice_state_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging voice state update events.",
                },
                "member_ban": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member ban events.",
                },
                "member_unban": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member unban events.",
                },
                "invite_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging invite creation events.",
                },
                "invite_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging invite deletion events.",
                },
                "message_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging message deletion events.",
                },
                "bulk_message_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging bulk message deletion events.",
                },
                "message_edit": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging message edit events.",
                },
                "reaction_add": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging reaction add events.",
                },
                "reaction_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging reaction remove events.",
                },
                "member_join": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member join events.",
                },
                "member_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member remove events.",
                },
                "member_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member update events.",
                },
                "user_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging user update events.",
                },
                "guild_role_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging role creation events.",
                },
                "guild_role_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging role deletion events.",
                },
                "guild_role_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging role update events.",
                },
                "guild_emojis_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging emoji update events.",
                },
                "guild_sticker_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging sticker creation events.",
                },
                "guild_sticker_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging sticker deletion events.",
                },
                "guild_sticker_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging sticker update events.",
                },
        }

        default_guild = {event: None for event in settings_dict.keys()}
        self.config.register_guild(**default_guild)

        self.logs = CogsUtils.get_logger(cog=self)

        self.event_queue = asyncio.Queue()
        self.bot.loop.create_task(self.process_event_queue())

        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GUILD,
            settings=settings_dict,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.setlog
        )

    async def cog_load(self) -> None:
        await super().cog_load()
        await self.settings.add_commands()
=======
_: Translator = Translator('EventLogger', __file__)

@cog_i18n(_)
class EventLogger(DashboardIntegration, commands.Cog):
    """Cog to log various Discord events"""

    def __init__(self, bot: Red) -> None:
        super().__init__(bot)
        self.bot = bot
        self.config: Config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_guild(channels={}, command_log_channel=None)
        self.event_queue = asyncio.Queue()
        self.bot.loop.create_task(self.process_event_queue())

    async def cog_load(self) -> None:
        await super().cog_load()
>>>>>>> 9e308722 (Revamped and Fixed)

    @commands.guild_only()
    @commands.is_owner()
    @commands.bot_has_permissions(manage_channels=True)
<<<<<<< HEAD
    @commands.group(name='setlog', invoke_without_command=True)
    async def setlog(self, ctx: commands.Context, event: str, channel: discord.TextChannel) -> None:
        """Set the logging channel for a specific event"""
        await self.config.guild(ctx.guild).set_raw(event, value=channel.id)
=======
    @commands.hybrid_group(name='setlog', invoke_without_command=True)
    async def setlog(self, ctx: commands.Context, event: str, channel: discord.TextChannel) -> None:
        """Set the logging channel for a specific event"""
        async with self.config.guild(ctx.guild).channels() as channels:
            channels[event] = channel.id
>>>>>>> 9e308722 (Revamped and Fixed)
        await ctx.send(f'Logging channel for {event} set to {channel.mention}')

    @commands.guild_only()
    @commands.is_owner()
    @commands.bot_has_permissions(manage_channels=True)
<<<<<<< HEAD
    @commands.group(name='seteventlogger', invoke_without_command=True)
    async def seteventlogger(self, ctx: commands.Context) -> None:
        """Configure EventLogger for your server."""
        pass

    async def create_embed(self, event: str, description: str, color: discord.Color = discord.Color.blue()):
        embed = discord.Embed(
            title=f"📝 {event.replace('_', ' ').title()}",
            description=description,
            color=color,
            timestamp=datetime.utcnow()
        )
        embed.set_footer(text=f"Event Logger | {self.bot.user.name}", icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        return embed

    async def log_event(self, guild: typing.Optional[discord.Guild], event: str, description: str, color: discord.Color = discord.Color.blue()):
        if guild is None:
            return
        channel_id = await self.config.guild(guild).get_raw(event, default=None)
        if channel_id:
            channel = guild.get_channel(channel_id)
            if channel:
                embed = await self.create_embed(event, description, color)
=======
    @commands.hybrid_group(name='seteventlogger', invoke_without_command=True)
    async def configuration(self, ctx: commands.Context) -> None:
        """Configure EventLogger for your server."""
        pass

    async def log_event(self, guild: typing.Optional[discord.Guild], event: str, description: str):
        if guild is None:
            return
        channels = await self.config.guild(guild).channels()
        channel_id = channels.get(event)
        if channel_id:
            channel = guild.get_channel(channel_id)
            if channel:
                embed = discord.Embed(
                    title=event.replace('_', ' ').title(),
                    description=description,
                    color=discord.Color.blue(),
                    timestamp=datetime.utcnow()
                )
>>>>>>> 9e308722 (Revamped and Fixed)
                await self.event_queue.put((channel, embed))

    async def log_command(self, ctx, command_name: str):
        command_log_channel_id = await self.config.guild(ctx.guild).command_log_channel()
        if command_log_channel_id:
            channel = ctx.guild.get_channel(command_log_channel_id)
            if channel:
<<<<<<< HEAD
                description = (
                    f"🔧 **Command Executed**\n\n"
                    f"**Command:** {command_name}\n"
                    f"**User:** {ctx.author} (ID: {ctx.author.id})\n"
                    f"**Channel:** {ctx.channel.mention} (ID: {ctx.channel.id})\n"
                    f"**Guild:** {ctx.guild.name} (ID: {ctx.guild.id})\n"
                    f"**Executed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
                )
                embed = await self.create_embed('Command Executed', description, discord.Color.green())
=======
                description = f"""**Command:** {command_name}
**User:** {ctx.author} ({ctx.author.id})
**Channel:** {ctx.channel} ({ctx.channel.id})
**Guild:** {ctx.guild.name} ({ctx.guild.id})"""
                embed = discord.Embed(
                    title='Command Executed',
                    description=description,
                    color=discord.Color.green(),
                    timestamp=datetime.utcnow()
                )
>>>>>>> 9e308722 (Revamped and Fixed)
                await self.event_queue.put((channel, embed))

    async def process_event_queue(self):
        while True:
            events = []
            while not self.event_queue.empty():
                events.append(await self.event_queue.get())
            for channel, embed in events:
                await channel.send(embed=embed)
            await asyncio.sleep(10)

    @setlog.command()
    async def categories(self, ctx):
        """View the event categories and their events"""
        event_categories = {
            'app': ['integration_create', 'integration_delete', 'integration_update'],
<<<<<<< HEAD
            'ban': ['member_ban', 'member_unban'],
            'channel': [
                'guild_channel_create', 'guild_channel_delete', 'guild_channel_update',
                'guild_channel_pins_update'
            ],
            'emoji': ['guild_emojis_update'],
            'invite': ['invite_create', 'invite_delete'],
            'message': ['bulk_message_delete', 'message_delete', 'message_edit'],
            'reaction': ['reaction_add', 'reaction_remove'],
            'role': ['guild_role_create', 'guild_role_delete', 'guild_role_update'],
            'sticker': ['guild_sticker_create', 'guild_sticker_delete', 'guild_sticker_update'],
            'user': [
                'member_join', 'member_remove', 'member_update', 'user_update'
            ],
            'voice': ['voice_state_update'],
=======
            'automod': ['automod_rule_create', 'automod_rule_delete', 'automod_rule_update'],
            'ban': ['member_ban', 'member_unban'],
            'channel': [
                'guild_channel_bitrate_update', 'guild_channel_create', 'guild_channel_delete',
                'guild_channel_name_update', 'guild_channel_nsfw_update', 'guild_channel_parent_update',
                'guild_channel_permissions_update', 'guild_channel_pins_update',
                'guild_channel_rtc_region_update', 'guild_channel_slowmode_update',
                'guild_channel_topic_update', 'guild_channel_type_update', 'guild_channel_user_limit_update',
                'guild_channel_video_quality_update', 'guild_channel_default_archive_duration_update',
                'guild_channel_default_thread_slowmode_update', 'guild_channel_default_reaction_emoji_update',
                'guild_channel_default_sort_order_update', 'guild_channel_forum_tags_update',
                'guild_channel_forum_layout_update'
            ],
            'commands': ['command_executed'],
            'emoji': ['guild_emoji_create', 'guild_emoji_delete', 'guild_emoji_update', 'guild_emojis_update'],
            'event': ['scheduled_event_create', 'scheduled_event_delete', 'scheduled_event_update',
                      'scheduled_event_user_add', 'scheduled_event_user_remove'],
            'invite': ['invite_create', 'invite_delete'],
            'message': ['bulk_message_delete', 'message_delete', 'message_edit'],
            'moderation': [
                'ban_add', 'ban_remove', 'case_delete', 'case_update', 'kick_add', 'kick_remove', 'mute_add',
                'mute_remove', 'report_create', 'reports_accept', 'reports_ignore', 'user_note_add',
                'user_note_remove', 'warn_add', 'warn_remove'
            ],
            'onboarding': [
                'guild_onboarding_channels_update', 'guild_onboarding_question_add',
                'guild_onboarding_question_remove', 'guild_onboarding_toggle', 'guild_onboarding_update'
            ],
            'reaction': ['reaction_add', 'reaction_remove'],
            'role': ['guild_role_create', 'guild_role_delete', 'guild_role_update'],
            'server': [
                'guild_afk_channel_update', 'guild_afk_timeout_update', 'guild_banner_update',
                'guild_boost_level_update', 'guild_boost_progress_bar_update', 'guild_description_update',
                'guild_discovery_splash_update', 'guild_explicit_content_filter_update', 'guild_features_update',
                'guild_icon_update', 'guild_message_notifications_update', 'guild_mfa_level_update',
                'guild_name_update', 'guild_partner_status_update', 'guild_preferred_locale_update',
                'guild_public_updates_channel_update', 'guild_rules_channel_update', 'guild_splash_update',
                'guild_system_channel_update', 'guild_vanity_url_update', 'guild_verification_level_update',
                'guild_verified_update', 'guild_widget_update'
            ],
            'soundboard': [
                'soundboard_sound_delete', 'soundboard_sound_emoji_update', 'soundboard_sound_name_update',
                'soundboard_sound_upload', 'soundboard_sound_volume_update'
            ],
            'sticker': ['guild_sticker_create', 'guild_sticker_delete', 'guild_sticker_update'],
            'thread': ['thread_create', 'thread_delete', 'thread_member_join', 'thread_member_remove', 'thread_update'],
            'typing': ['typing'],
            'user': [
                'member_update', 'user_avatar_update', 'user_roles_add', 'user_roles_remove', 'user_roles_update',
                'user_timeout', 'user_timeout_remove', 'user_update'
            ],
            'voice': ['voice_state_update'],
            'webhook': ['webhook_create', 'webhook_delete', 'webhook_update']
>>>>>>> 9e308722 (Revamped and Fixed)
        }
        embed = discord.Embed(title='Event Categories and Their Events', color=discord.Color.blue())
        for category, events in sorted(event_categories.items()):
            embed.add_field(name=category.capitalize(), value='\n'.join(sorted(events)), inline=False)
        await ctx.send(embed=embed)

<<<<<<< HEAD
    @commands.Cog.listener()
    async def on_integration_create(self, integration: discord.Integration):
        # Use getattr to safely get created_at, or use current time if not available
        created_at = getattr(integration, 'created_at', datetime.utcnow())

        description = (
            f"#  New Integration Added\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Account:** {integration.account.name} (ID: {integration.account.id})\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Created At:** <t:{int(created_at.timestamp())}:F>\n\n"
            f"[Integration Settings](https://discord.com/channels/{integration.guild.id}/integrations)"
        )
        await self.log_event(integration.guild, 'integration_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_integration_delete(self, integration: discord.Integration):
        description = (
            f"# 🗑️  Integration Removed\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Integration Settings](https://discord.com/channels/{integration.guild.id}/integrations)"
        )
        await self.log_event(integration.guild, 'integration_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_integration_update(self, integration: discord.Integration):
        description = (
            f"# 🔄 Integration Updated\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Integration Settings](https://discord.com/channels/{integration.guild.id}/integrations)"
        )
        await self.log_event(integration.guild, 'integration_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        description = (
            f"# 📢 New Channel Created\n\n"
            f"**Name:** {channel.name}\n"
            f"**ID:** `{channel.id}`\n"
            f"**Type:** `{channel.type}`\n"
            f"**Category:** {channel.category.name if channel.category else 'None'}\n"
            f"**Position:** {channel.position}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Go to Channel]({channel.jump_url}) | [Channel Settings](https://discord.com/channels/{channel.guild.id}/{channel.id}/edit)"
        )
        await self.log_event(channel.guild, 'guild_channel_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        description = (
            f"# 🗑️ Channel  Deleted\n\n"
            f"**Name:** {channel.name}\n"
            f"**ID:** `{channel.id}`\n"
            f"**Type:** `{channel.type}`\n"
            f"**Category:** {channel.category.name if channel.category else 'None'}\n"
            f"**Position:** {channel.position}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(channel.guild, 'guild_channel_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.category != after.category:
            changes.append(f"**Category:** {before.category.name if before.category else 'None'} → {after.category.name if after.category else 'None'}")
        if before.position != after.position:
            changes.append(f"**Position:** {before.position} → {after.position}")
        if isinstance(before, discord.TextChannel) and isinstance(after, discord.TextChannel):
            if before.topic != after.topic:
                changes.append(f"**Topic:** {before.topic} → {after.topic}")
            if before.slowmode_delay != after.slowmode_delay:
                changes.append(f"**Slowmode:** {before.slowmode_delay}s → {after.slowmode_delay}s")

        if changes:
            description = (
                f"# 🔄 Channel Updated\n\n"
                f"**Channel:** {after.name} (`{after.id}`)\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Go to Channel]({after.jump_url}) | [Channel Settings](https://discord.com/channels/{after.guild.id}/{after.id}/edit)"
            )
            await self.log_event(after.guild, 'guild_channel_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_pins_update(self, channel: discord.abc.GuildChannel, last_pin: typing.Optional[datetime]):
        description = (
            f"# 📌 Channel Pins Updated\n\n"
            f"**Channel:** {channel.name} (`{channel.id}`)\n"
            f"**Last Pin:** {'None' if last_pin is None else f'<t:{int(last_pin.timestamp())}:F>'}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Go to Channel]({channel.jump_url})"
        )
        await self.log_event(channel.guild, 'guild_channel_pins_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel != after.channel:
            if after.channel:
                action = f"joined {after.channel.mention}"
            elif before.channel:
                action = f"left {before.channel.mention}"
            else:
                return

            description = (
                f"# 🎙 ️ Voice State Updated\n\n"
                f"**Member:** {member.mention} ({member.name})\n"
                f"**Action:** {action}\n"
                f"**Self Mute:** {'Yes' if after.self_mute else 'No'}\n"
                f"**Self Deaf:** {'Yes' if after.self_deaf else 'No'}\n"
                f"**Server Mute:** {'Yes' if after.mute else 'No'}\n"
                f"**Server Deaf:** {'Yes' if after.deaf else 'No'}\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
            )
            await self.log_event(member.guild, 'voice_state_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        description = (
            f"# 🚫 Member Banned\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Account Created:** <t:{int(user.created_at.timestamp())}:F>\n"
            f"**Banned At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Audit Log](https://discord.com/channels/{guild.id}/audit-log?action_type=22)"
        )
        await self.log_event(guild, 'member_ban', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        description = (
            f"# 🔓 Member Unbanned\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Account Created:** <t:{int(user.created_at.timestamp())}:F>\n"
            f"**Unbanned At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Audit Log](https://discord.com/channels/{guild.id}/audit-log?action_type=23)"
        )
        await self.log_event(guild, 'member_unban', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        description = (
            f"# 📨 Invite Created\n\n"
            f"**Inviter:** {invite.inviter.mention} ({invite.inviter.name})\n"
            f"**Channel:** {invite.channel.mention}\n"
            f"**Code:** {invite.code}\n"
            f"**Max Uses:** {invite.max_uses if invite.max_uses else 'Unlimited'}\n"
            f"**Max Age:** {invite.max_age if invite.max_age else 'Never'}\n"
            f"**Temporary:** {'Yes' if invite.temporary else 'No'}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Use Invite](https://discord.gg/{invite.code})"
        )
        await self.log_event(invite.guild, 'invite_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_invite_delete(self, invite: discord.Invite):
        description = (
            f"# 🗑️ Invite  Deleted\n\n"
            f"**Channel:** {invite.channel.mention}\n"
            f"**Code:** {invite.code}\n"
            f"**Uses:** {invite.uses}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(invite.guild, 'invite_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.guild is None:
            return
        description = (
            f"# 🗑️  Message Deleted\n\n"
            f"**Author:** {message.author.mention} ({message.author.name})\n"
            f"**Channel:** {message.channel.mention}\n"
            f"**Created At:** <t:{int(message.created_at.timestamp())}:F>\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"**Content:**\n>>> {message.content[:1000]}"
        )
        await self.log_event(message.guild, 'message_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages: List[discord.Message]):
        if not messages:
            return
        guild = messages[0].guild
        if guild is None:
            return
        description = (
            f"# 🗑️ Bulk  Message Delete\n\n"
            f"**Channel:** {messages[0].channel.mention}\n"
            f"**Message Count:** {len(messages)}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"**Messages:**\n"
        )
        for message in messages[:10]:  # Limit to first 10 messages to avoid hitting character limits
            description += f"> {message.author.name}: {message.content[:100]}...\n"
        if len(messages) > 10:
            description += f"\n... and {len(messages) - 10} more messages."
        await self.log_event(guild, 'bulk_message_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.guild is None:
            return
        if before.content == after.content:
            return
        description = (
            f"# ✏️ Message Edited\n\n"
            f"**Author:** {before.author.mention} ({before.author.name})\n"
            f"**Channel:** {before.channel.mention}\n"
            f"**Created At:** <t:{int(before.created_at.timestamp())}:F>\n"
            f"**Edited At:** <t:{int(after.edited_at.timestamp() if after.edited_at else datetime.utcnow().timestamp())}:F>\n\n"
            f"**Before:**\n>>> {before.content[:500]}\n\n"
            f"**After:**\n>>> {after.content[:500]}\n\n"
            f"[Jump to Message]({after.jump_url})"
        )
        await self.log_event(before.guild, 'message_edit', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
        if reaction.message.guild is None:
            return

        if isinstance(reaction.message.channel, discord.abc.GuildChannel):
            channel_info = reaction.message.channel.mention
        else:
            channel_info = f"#{reaction.message.channel.name}" if hasattr(reaction.message.channel, 'name') else "Unknown Channel"

        description = (
            f"# 👍 Reaction Added\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**Channel:** {channel_info}\n"
            f"**Message:** [Jump to Message]({reaction.message.jump_url})\n"
            f"**Emoji:** {reaction.emoji}\n"
            f"**Added At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(reaction.message.guild, 'reaction_add', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
        if reaction.message.guild is None:
            return
        description = (
            f"# 👎 Reaction Removed\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**Channel:** {reaction.message.channel.mention}\n"
            f"**Message:** [Jump to Message]({reaction.message.jump_url})\n"
            f"**Emoji:** {reaction.emoji}\n"
            f"**Removed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(reaction.message.guild, 'reaction_remove', description, discord.Color.orange())

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        description = (
            f"# 👋 New Member\n\n"
            f"**Member:** {member.mention} ({member.name})\n"
            f"**ID:** `{member.id}`\n"
            f"**Account Created:** <t:{int(member.created_at.timestamp())}:R>\n"
            f"**Joined At:** <t:{int(member.joined_at.timestamp())}:F>\n"
            f"**Server Member Count:** {member.guild.member_count}\n\n"
            f"[Member Profile](https://discord.com/channels/@me/{member.id})"
        )
        await self.log_event(member.guild, 'member_join', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        description = (
            f"# 👋 Member Left\n\n"
            f"**Member:** {member.mention} ({member.name})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Joined At:** <t:{int(member.joined_at.timestamp())}:F>\n"
            f"**Account Created:** <t:{int(member.created_at.timestamp())}:F>\n"
            f"**Roles:** {', '.join([role.name for role in member.roles[1:]])}\n"
            f"**Left At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"Server Member Count: {member.guild.member_count}"
        )
        await self.log_event(member.guild, 'member_remove', description, discord.Color.orange())

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        print("Member updated event triggered")
        changes = []
        if before.nick != after.nick:
            changes.append(f"**Nickname:** {before.nick} → {after.nick}")
        if before.roles != after.roles:
            added_roles = set(after.roles) - set(before.roles)
            removed_roles = set(before.roles) - set(after.roles)
            if added_roles:
                changes.append(f"**Roles Added:** {', '.join(role.name for role in added_roles)}")
            if removed_roles:
                changes.append(f"**Roles Removed:** {', '.join(role.name for role in removed_roles)}")
        if before.avatar != after.avatar:
            changes.append(f"**Avatar:** [Before]({before.avatar.url}) → [After]({after.avatar.url})")

        if changes:
            description = (
                f"# 🔄 Member Updated\n\n"
                f"**Member:** {after.mention} ({after.name})\n"
                f"**Member ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Member Profile](https://discord.com/channels/@me/{after.id})"
            )
            await self.log_event(after.guild, 'member_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User):
        print("User updated event triggered")
        changes = []
        if before.name != after.name:
            changes.append(f"**Username:** {before.name} → {after.name}")
        if before.discriminator != after.discriminator:
            changes.append(f"**Discriminator:** {before.discriminator} → {after.discriminator}")
        if before.avatar != after.avatar:
            changes.append(f"**Avatar:** [Before]({before.display_avatar.url}) → [After]({after.display_avatar.url})")

        if changes:
            description = (
                f"# 🔄 User Updated\n\n"
                f"**User:** {after.mention} ({after.name})\n"
                f"**User ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[User Profile](https://discord.com/channels/@me/{after.id})"
            )
            await self.log_event(None, 'user_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_role_create(self, role: discord.Role):
        description = (
            f"# 🆕 Role Created\n\n"
            f"**Name:** {role.name}\n"
            f"**ID:** `{role.id}`\n"
            f"**Color:** {role.color}\n"
            f"**Permissions:** `{role.permissions.value}`\n"
            f"**Position:** {role.position}\n"
            f"**Mentionable:** {'Yes' if role.mentionable else 'No'}\n"
            f"**Hoisted:** {'Yes' if role.hoist else 'No'}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Role Settings](https://discord.com/channels/{role.guild.id}/roles/{role.id})"
        )
        await self.log_event(role.guild, 'guild_role_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.Role):
        description = (
            f"# 🗑️  Role Deleted\n\n"
            f"**Name:** {role.name}\n"
            f"**ID:** `{role.id}`\n"
            f"**Color:** {role.color}\n"
            f"**Permissions:** `{role.permissions.value}`\n"
            f"**Position:** {role.position}\n"
            f"**Mentionable:** {'Yes' if role.mentionable else 'No'}\n"
            f"**Hoisted:** {'Yes' if role.hoist else 'No'}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(role.guild, 'guild_role_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_role_update(self, before: discord.Role, after: discord.Role):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.color != after.color:
            changes.append(f"**Color:** {before.color} → {after.color}")
        if before.permissions != after.permissions:
            changes.append(f"**Permissions:** `{before.permissions.value}` → `{after.permissions.value}`")
        if before.hoist != after.hoist:
            changes.append(f"**Hoisted:** {'Yes' if before.hoist else 'No'} → {'Yes' if after.hoist else 'No'}")
        if before.mentionable != after.mentionable:
            changes.append(f"**Mentionable:** {'Yes' if before.mentionable else 'No'} → {'Yes' if after.mentionable else 'No'}")
        if before.position != after.position:
            changes.append(f"**Position:** {before.position} → {after.position}")

        if changes:
            description = (
                f"# 🔄 Role Updated\n\n"
                f"**Role:** {after.name}\n"
                f"**ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Role Settings](https://discord.com/channels/{after.guild.id}/roles/{after.id})"
            )
            await self.log_event(before.guild, 'guild_role_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild: discord.Guild, before: List[discord.Emoji], after: List[discord.Emoji]):
        added_emojis = [emoji for emoji in after if emoji not in before]
        removed_emojis = [emoji for emoji in before if emoji not in after]
        description = (
            f"# 😀 Guild Emojis Updated\n\n"
            f"**Added Emojis:** {', '.join([str(emoji) for emoji in added_emojis]) or 'None'}\n"
            f"**Removed Emojis:** {', '.join([str(emoji) for emoji in removed_emojis]) or 'None'}\n"
            f"**Total Emojis:** {len(after)}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Emoji Settings](https://discord.com/channels/{guild.id}/emojis)"
        )
        await self.log_event(guild, 'guild_emojis_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_sticker_create(self, sticker: discord.GuildSticker):
        description = (
            f"# 🆕 Sticker Created\n\n"
            f"**Name:** {sticker.name}\n"
            f"**ID:** `{sticker.id}`\n"
            f"**Description:** {sticker.description}\n"
            f"**Emoji:** {sticker.emoji}\n"
            f"**Created By:** {sticker.user.name if sticker.user else 'Unknown'} (`{sticker.user.id if sticker.user else 'Unknown'}`)\n"
            f"**Created At:** <t:{int(sticker.created_at.timestamp())}:F>\n\n"
            f"[Sticker URL]({sticker.url})"
        )
        await self.log_event(sticker.guild, 'guild_sticker_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_sticker_delete(self, sticker: discord.GuildSticker):
        description = (
            f"# 🗑️ St icker Deleted\n\n"
            f"**Name:** {sticker.name}\n"
            f"**ID:** `{sticker.id}`\n"
            f"**Description:** {sticker.description}\n"
            f"**Emoji:** {sticker.emoji}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(sticker.guild, 'guild_sticker_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_sticker_update(self, before: discord.GuildSticker, after: discord.GuildSticker):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.description != after.description:
            changes.append(f"**Description:** {before.description} → {after.description}")
        if before.emoji != after.emoji:
            changes.append(f"**Emoji:** {before.emoji} → {after.emoji}")

        if changes:
            description = (
                f"# 🔄 Sticker Updated\n\n"
                f"**Sticker:** {after.name}\n"
                f"**ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Sticker URL]({after.url})"
            )
            await self.log_event(after.guild, 'guild_sticker_update', description, discord.Color.blue())
=======
        @commands.Cog.listener()
        async def on_integration_create(self, integration: discord.Integration
            ):
            description = f"""**Integration:** {integration.name}
**Integration ID:** `{integration.id}`
**Guild:** ||{integration.guild.name} ({integration.guild.id})||
**Timestamp:** <t:{int(integration.created_at.timestamp())}:F>"""
            await self.log_event(integration.guild, 'integration_create',
                description)

        @commands.Cog.listener()
        async def on_integration_delete(self, integration: discord.Integration
            ):
            description = f"""**Integration:** {integration.name}
**Integration ID:** `{integration.id}`
**Guild:** ||{integration.guild.name} ({integration.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(integration.guild, 'integration_delete',
                description)

        @commands.Cog.listener()
        async def on_integration_update(self, integration: discord.Integration
            ):
            description = f"""**Integration:** {integration.name}
**Integration ID:** `{integration.id}`
**Guild:** ||{integration.guild.name} ({integration.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(integration.guild, 'integration_update',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_create(self, channel: discord.abc.
            GuildChannel):
            description = f"""**Channel:** {channel.name}
**Channel ID:** `{channel.id}`
**Channel Type:** {str(channel.type)}
**Guild:** ||{channel.guild.name} ({channel.guild.id})||
**Creator:** {channel.guild.me.name if channel.guild.me else 'N/A'}
**Creator ID:** ||{channel.guild.me.id if channel.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(channel.guild, 'guild_channel_create',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_delete(self, channel: discord.abc.
            GuildChannel):
            description = f"""**Channel:** {channel.name}
**Channel ID:** `{channel.id}`
**Channel Type:** {str(channel.type)}
**Guild:** ||{channel.guild.name} ({channel.guild.id})||
**Deleter:** {channel.guild.me.name if channel.guild.me else 'N/A'}
**Deleter ID:** ||{channel.guild.me.id if channel.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(channel.guild, 'guild_channel_delete',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_update(self, before: discord.abc.
            GuildChannel, after: discord.abc.GuildChannel):
            if before.position != after.position:
                return
            description = f"""**Before Channel:** {before.name}
**After Channel:** {after.name}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'guild_channel_update',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_pins_update(self, channel: discord.abc.
            GuildChannel, last_pin: discord.Message):
            description = f"""**Channel:** {channel.name}
**Channel ID:** `{channel.id}`
**Guild:** ||{channel.guild.name} ({channel.guild.id})||
**Last Pin:** {last_pin.content if last_pin else 'None'}
**Pinner:** {last_pin.author.name if last_pin else 'N/A'}
**Pinner ID:** ||{last_pin.author.id if last_pin else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(channel.guild, 'guild_channel_pins_update',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_name_update(self, before: discord.abc.
            GuildChannel, after: discord.abc.GuildChannel):
            description = f"""**Before Name:** {before.name}
**After Name:** {after.name}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'guild_channel_name_update',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_topic_update(self, before: discord.
            TextChannel, after: discord.TextChannel):
            description = f"""**Before Topic:** {before.topic}
**After Topic:** {after.topic}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'guild_channel_topic_update',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_nsfw_update(self, before: discord.abc.
            GuildChannel, after: discord.abc.GuildChannel):
            description = f"""**Before NSFW:** {before.is_nsfw()}
**After NSFW:** {after.is_nsfw()}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id} else `N/A`||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'guild_channel_nsfw_update',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_parent_update(self, before: discord.abc.
            GuildChannel, after: discord.abc.GuildChannel):
            description = f"""**Before Parent:** {before.category.name if before.category else 'None'}
**After Parent:** {after.category.name if after.category else 'None'}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'guild_channel_parent_update', description)

        @commands.Cog.listener()
        async def on_guild_channel_permissions_update(self, before: discord
            .abc.GuildChannel, after: discord.abc.GuildChannel):
            description = f"""**Before Permissions:** {str(before.overwrites)}
**After Permissions:** {str(after.overwrites)}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'guild_channel_permissions_update', description)

        @commands.Cog.listener()
        async def on_guild_channel_type_update(self, before: discord.abc.
            GuildChannel, after: discord.abc.GuildChannel):
            description = f"""**Before Type:** {str(before.type)}
**After Type:** {str(after.type)}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'guild_channel_type_update',
                description)

        @commands.Cog.listener()
        async def on_guild_channel_bitrate_update(self, before: discord.
            VoiceChannel, after: discord.VoiceChannel):
            description = f"""**Before Bitrate:** {before.bitrate}
**After Bitrate:** {after.bitrate}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'guild_channel_bitrate_update', description)

        @commands.Cog.listener()
        async def on_guild_channel_user_limit_update(self, before: discord.
            VoiceChannel, after: discord.VoiceChannel):
            description = f"""**Before User Limit:** {before.user_limit}
**After User Limit:** {after.user_limit}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'guild_channel_user_limit_update', description)

        @commands.Cog.listener()
        async def on_guild_channel_slowmode_update(self, before: discord.
            TextChannel, after: discord.TextChannel):
            description = f"""**Before Slowmode:** {before.slowmode_delay}
**After Slowmode:** {after.slowmode_delay}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'guild_channel_slowmode_update', description)

        @commands.Cog.listener()
        async def on_guild_channel_rtc_region_update(self, before: discord.
            VoiceChannel, after: discord.VoiceChannel):
            description = f"""**Before RTC Region:** {before.rtc_region}
**After RTC Region:** {after.rtc_region}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'guild_channel_rtc_region_update', description)

        @commands.Cog.listener()
        async def on_guild_channel_video_quality_update(self, before:
            discord.VoiceChannel, after: discord.VoiceChannel):
            description = f"""**Before Video Quality:** {before.video_quality_mode}
**After Video Quality:** {after.video_quality_mode}
**Channel ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'guild_channel_video_quality_update', description)

        @commands.Cog.listener()
        async def on_voice_state_update(self, member: discord.Member,
            before: discord.VoiceState, after: discord.VoiceState):
            description = f"""**Member:** {member.name} ({member.mention})
**Member ID:** `{member.id}`
**Guild:** ||{member.guild.name} ({member.guild.id})||
**Before Channel:** {str(before.channel) if before.channel else 'None'}
**After Channel:** {str(after.channel) if after.channel else 'None'}
**Before Mute:** {before.mute}
**After Mute:** {after.mute}
**Before Deaf:** {before.deaf}
**After Deaf:** {after.deaf}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(member.guild, 'voice_state_update',
                description)

        @commands.Cog.listener()
        async def on_automod_rule_create(self, rule: discord.AutoModRule):
            description = f"""**Rule:** {rule.name}
**Rule ID:** `{rule.id}`
**Guild:** ||{rule.guild.name} ({rule.guild.id})||
**Creator:** {rule.creator.name if rule.creator else 'N/A'}
**Creator ID:** ||{rule.creator.id if rule.creator else 'N/A'}||
**Timestamp:** <t:{int(rule.created_at.timestamp())}:F>"""
            await self.log_event(rule.guild, 'automod_rule_create', description
                )

        @commands.Cog.listener()
        async def on_automod_rule_delete(self, rule: discord.AutoModRule):
            description = f"""**Rule:** {rule.name}
**Rule ID:** `{rule.id}`
**Guild:** ||{rule.guild.name} ({rule.guild.id})||
**Deleter:** {rule.creator.name if rule.creator else 'N/A'}
**Deleter ID:** ||{rule.creator.id if rule.creator else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(rule.guild, 'automod_rule_delete', description
                )

        @commands.Cog.listener()
        async def on_automod_rule_update(self, before: discord.AutoModRule,
            after: discord.AutoModRule):
            description = f"""**Before Rule:** {before.name}
**After Rule:** {after.name}
**Rule ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.creator.name if before.creator else 'N/A'}
**Updater ID:** ||{before.creator.id if before.creator else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'automod_rule_update',
                description)

        @commands.Cog.listener()
        async def on_guild_emojis_update(self, guild: discord.Guild, before:
            list[discord.Emoji], after: list[discord.Emoji]):
            description = f"""**Guild:** ||{guild.name} ({guild.id})||
**Before Emojis:** {', '.join([emoji.name for emoji in before])}
**After Emojis:** {', '.join([emoji.name for emoji in after])}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'guild_emojis_update', description)

        @commands.Cog.listener()
        async def on_guild_emoji_create(self, emoji: discord.Emoji):
            description = f"""**Emoji:** {emoji} ({emoji.name})
**Emoji ID:** `{emoji.id}`
**Guild:** ||{emoji.guild.name} ({emoji.guild.id})||
**Creator:** {emoji.user.name if emoji.user else 'N/A'}
**Creator ID:** ||{emoji.user.id if emoji.user else 'N/A'}||
**Created At:** <t:{int(emoji.created_at.timestamp())}:F>"""
            embed = discord.Embed(title='Emoji Created', description=
                description, color=discord.Color.green(), timestamp=
                datetime.utcnow())
            embed.set_thumbnail(url=emoji.url)
            await self.log_event(emoji.guild, 'guild_emoji_create', description
                )

        @commands.Cog.listener()
        async def on_guild_emoji_delete(self, emoji: discord.Emoji):
            description = f"""**Emoji:** {emoji} ({emoji.name})
**Emoji ID:** `{emoji.id}`
**Guild:** ||{emoji.guild.name} ({emoji.guild.id})||
**Deleter:** {emoji.user.name if emoji.user else 'N/A'}
**Deleter ID:** ||{emoji.user.id if emoji.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            embed = discord.Embed(title='Emoji Deleted', description=
                description, color=discord.Color.red(), timestamp=datetime.
                utcnow())
            embed.set_thumbnail(url=emoji.url)
            await self.log_event(emoji.guild, 'guild_emoji_delete', description
                )

        @commands.Cog.listener()
        async def on_guild_emoji_update(self, before: discord.Emoji, after:
            discord.Emoji):
            description = f"""**Before Emoji:** {before} ({before.name})
**After Emoji:** {after} ({after.name})
**Emoji ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.user.name if before.user else 'N/A'}
**Updater ID:** ||{before.user.id if before.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            embed = discord.Embed(title='Emoji Updated', description=
                description, color=discord.Color.orange(), timestamp=
                datetime.utcnow())
            embed.set_thumbnail(url=after.url)
            await self.log_event(before.guild, 'guild_emoji_update',
                description)

        @commands.Cog.listener()
        async def on_scheduled_event_create(self, event: discord.ScheduledEvent
            ):
            description = f"""**Event:** {event.name}
**Event ID:** `{event.id}`
**Guild:** ||{event.guild.name} ({event.guild.id})||
**Creator:** {event.creator.name if event.creator else 'N/A'}
**Creator ID:** ||{event.creator.id if event.creator else 'N/A'}||
**Timestamp:** <t:{int(event.created_at.timestamp())}:F>"""
            await self.log_event(event.guild, 'scheduled_event_create',
                description)

        @commands.Cog.listener()
        async def on_scheduled_event_delete(self, event: discord.ScheduledEvent
            ):
            description = f"""**Event:** {event.name}
**Event ID:** `{event.id}`
**Guild:** ||{event.guild.name} ({event.guild.id})||
**Deleter:** {event.creator.name if event.creator else 'N/A'}
**Deleter ID:** ||{event.creator.id if event.creator else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(event.guild, 'scheduled_event_delete',
                description)

        @commands.Cog.listener()
        async def on_scheduled_event_update(self, before: discord.
            ScheduledEvent, after: discord.ScheduledEvent):
            description = f"""**Before Event:** {before.name}
**After Event:** {after.name}
**Event ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.creator.name if before.creator else 'N/A'}
**Updater ID:** ||{before.creator.id if before.creator else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'scheduled_event_update',
                description)

        @commands.Cog.listener()
        async def on_scheduled_event_user_add(self, event: discord.
            ScheduledEvent, user: discord.User):
            description = f"""**User:** {user.name}
**User ID:** `{user.id}`
**Event:** {event.name}
**Event ID:** `{event.id}`
**Guild:** ||{event.guild.name} ({event.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(event.guild, 'scheduled_event_user_add',
                description)

        @commands.Cog.listener()
        async def on_scheduled_event_user_remove(self, event: discord.
            ScheduledEvent, user: discord.User):
            description = f"""**User:** {user.name}
**User ID:** `{user.id}`
**Event:** {event.name}
**Event ID:** `{event.id}`
**Guild:** ||{event.guild.name} ({event.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(event.guild, 'scheduled_event_user_remove',
                description)

        @commands.Cog.listener()
        async def on_invite_create(self, invite: discord.Invite):
            description = f"""**Invite URL:** {invite.url}
**Invite ID:** `{invite.id}`
**Guild:** ||{invite.guild.name} ({invite.guild.id})||
**Channel:** {invite.channel.name}
**Channel ID:** `{invite.channel.id}`
**Creator:** {invite.inviter.name if invite.inviter else 'N/A'}
**Creator ID:** ||{invite.inviter.id if invite.inviter else 'N/A'}||
**Timestamp:** <t:{int(invite.created_at.timestamp())}:F>"""
            await self.log_event(invite.guild, 'invite_create', description)

        @commands.Cog.listener()
        async def on_invite_delete(self, invite: discord.Invite):
            description = f"""**Invite URL:** {invite.url}
**Invite ID:** `{invite.id}`
**Guild:** ||{invite.guild.name} ({invite.guild.id})||
**Channel:** {invite.channel.name}
**Channel ID:** `{invite.channel.id}`
**Deleter:** {invite.inviter.name if invite.inviter else 'N/A'}
**Deleter ID:** ||{invite.inviter.id if invite.inviter else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(invite.guild, 'invite_delete', description)

        @commands.Cog.listener()
        async def on_message_delete(self, message: discord.Message):
            if message.guild is None:
                return
            description = f"""**Message Content:** {message.content}
**Message ID:** `{message.id}`
**Author:** {message.author.name} ({message.author.mention})
**Author ID:** `{message.author.id}`
**Channel:** {message.channel.name}
**Channel ID:** `{message.channel.id}`
**Guild:** ||{message.guild.name} ({message.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(message.guild, 'message_delete', description)

        @commands.Cog.listener()
        async def on_bulk_message_delete(self, messages: list[discord.Message]
            ):
            if messages[0].guild is None:
                return
            description = f"""**Message Count:** {len(messages)}
**Channel:** {messages[0].channel.name}
**Channel ID:** `{messages[0].channel.id}`
**Guild:** ||{messages[0].guild.name} ({messages[0].guild.id})||
**Messages:** {', '.join([message.content for message in messages])}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(messages[0].guild, 'bulk_message_delete',
                description)

        @commands.Cog.listener()
        async def on_message_edit(self, before: discord.Message, after:
            discord.Message):
            if before.guild is None:
                return
            description = f"""**Before Content:** {before.content}
**After Content:** {after.content}
**Message ID:** `{before.id}`
**Author:** {before.author.name} ({before.author.mention})
**Author ID:** `{before.author.id}`
**Channel:** {before.channel.name}
**Channel ID:** `{before.channel.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'message_edit', description)

        @commands.Cog.listener()
        async def on_guild_role_create(self, role: discord.Role):
            description = f"""**Role:** {role.name}
**Role ID:** `{role.id}`
**Guild:** ||{role.guild.name} ({role.guild.id})||
**Creator:** {role.guild.me.name if role.guild.me else 'N/A'}
**Creator ID:** ||{role.guild.me.id if role.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(role.guild, 'guild_role_create', description)

        @commands.Cog.listener()
        async def on_guild_role_delete(self, role: discord.Role):
            description = f"""**Role:** {role.name}
**Role ID:** `{role.id}`
**Guild:** ||{role.guild.name} ({role.guild.id})||
**Deleter:** {role.guild.me.name if role.guild.me else 'N/A'}
**Deleter ID:** ||{role.guild.me.id if role.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(role.guild, 'guild_role_delete', description)

        @commands.Cog.listener()
        async def on_guild_role_update(self, before: discord.Role, after:
            discord.Role):
            description = f"""**Before Role:** {before.name}
**After Role:** {after.name}
**Role ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.guild.me.name if before.guild.me else 'N/A'}
**Updater ID:** ||{before.guild.me.id if before.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'guild_role_update', description
                )

        @commands.Cog.listener()
        async def on_member_ban(self, guild: discord.Guild, user: discord.User
            ):
            description = f"""**User:** {user.name} ({user.mention})
**User ID:** `{user.id}`
**Guild:** ||{guild.name} ({guild.id})||
**Banner:** {guild.me.name if guild.me else 'N/A'}
**Banner ID:** ||{guild.me.id if guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'member_ban', description)

        @commands.Cog.listener()
        async def on_member_unban(self, guild: discord.Guild, user: discord
            .User):
            description = f"""**User:** {user.name} ({user.mention})
**User ID:** `{user.id}`
**Guild:** ||{guild.name} ({guild.id})||
**Unbanner:** {guild.me.name if guild.me else 'N/A'}
**Unbanner ID:** ||{guild.me.id if guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'member_unban', description)

        @commands.Cog.listener()
        async def on_user_update(self, before: discord.User, after: discord
            .User):
            description = f"""**Before Name:** {before.name}
**After Name:** {after.name}
**User ID:** `{before.id}`
**Before Discriminator:** {before.discriminator}
**After Discriminator:** {after.discriminator}
**Before Avatar:** {str(before.avatar.url)}
**After Avatar:** {str(after.avatar.url)}
**Before Bot:** {before.bot}
**After Bot:** {after.bot}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(None, 'user_update', description)

        @commands.Cog.listener()
        async def on_member_update(self, before: discord.Member, after:
            discord.Member):
            description = f"""**Before Name:** {before.name}
**After Name:** {after.name}
**Member ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Before Nick:** {before.nick}
**After Nick:** {after.nick}
**Before Roles:** {', '.join([role.name for role in before.roles])}
**After Roles:** {', '.join([role.name for role in after.roles])}
**Before Status:** {str(before.status)}
**After Status:** {str(after.status)}
**Before Activity:** {str(before.activity)}
**After Activity:** {str(after.activity)}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'member_update', description)

        @commands.Cog.listener()
        async def on_user_roles_update(self, before: discord.Member, after:
            discord.Member):
            description = f"""**Member:** {before.name}
**Member ID:** `{before.id}`
**Before Roles:** {', '.join([role.name for role in before.roles])}
**After Roles:** {', '.join([role.name for role in after.roles])}
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'user_roles_update', description
                )

        @commands.Cog.listener()
        async def on_user_roles_add(self, member: discord.Member, role:
            discord.Role):
            description = f"""**Member:** {member.name}
**Member ID:** `{member.id}`
**Role Added:** {role.name}
**Role ID:** `{role.id}`
**Guild:** ||{member.guild.name} ({member.guild.id})||
**Adder:** {member.guild.me.name if member.guild.me else 'N/A'}
**Adder ID:** ||{member.guild.me.id if member.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(member.guild, 'user_roles_add', description)

        @commands.Cog.listener()
        async def on_user_roles_remove(self, member: discord.Member, role:
            discord.Role):
            description = f"""**Member:** {member.name}
**Member ID:** `{member.id}`
**Role Removed:** {role.name}
**Role ID:** `{role.id}`
**Guild:** ||{member.guild.name} ({member.guild.id})||
**Remover:** {member.guild.me.name if member.guild.me else 'N/A'}
**Remover ID:** ||{member.guild.me.id if member.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(member.guild, 'user_roles_remove', description
                )

        @commands.Cog.listener()
        async def on_user_avatar_update(self, before: discord.User, after:
            discord.User):
            description = f"""**User:** {before.name}
**User ID:** `{before.id}`
**Before Avatar:** {str(before.avatar.url)}
**After Avatar:** {str(after.avatar.url)}
**Guild:** ||{before.guild.name if before.guild else 'DM'} ({before.guild.id if before.guild else 'DM'})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'user_avatar_update',
                description)

        @commands.Cog.listener()
        async def on_user_timeout(self, member: discord.Member):
            description = f"""**Member:** {member.name}
**Member ID:** `{member.id}`
**Guild:** ||{member.guild.name} ({member.guild.id})||
**Timeout By:** {member.guild.me.name if member.guild.me else 'N/A'}
**Timeout By ID:** ||{member.guild.me.id if member.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(member.guild, 'user_timeout', description)

        @commands.Cog.listener()
        async def on_user_timeout_remove(self, member: discord.Member):
            description = f"""**Member:** {member.name}
**Member ID:** `{member.id}`
**Guild:** ||{member.guild.name} ({member.guild.id})||
**Timeout Removed By:** {member.guild.me.name if member.guild.me else 'N/A'}
**Timeout Removed By ID:** ||{member.guild.me.id if member.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(member.guild, 'user_timeout_remove',
                description)

        @commands.Cog.listener()
        async def on_webhook_update(self, channel: discord.abc.GuildChannel):
            description = f"""**Channel:** {channel.name}
**Channel ID:** `{channel.id}`
**Guild:** ||{channel.guild.name} ({channel.guild.id})||
**Updater:** {channel.guild.me.name if channel.guild.me else 'N/A'}
**Updater ID:** ||{channel.guild.me.id if channel.guild.me else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(channel.guild, 'webhook_update', description)

        @commands.Cog.listener()
        async def on_webhook_create(self, webhook: discord.Webhook):
            description = f"""**Webhook:** {webhook.name}
**Webhook ID:** `{webhook.id}`
**Channel:** {webhook.channel.name}
**Channel ID:** `{webhook.channel.id}`
**Guild:** ||{webhook.guild.name} ({webhook.guild.id})||
**Creator:** {webhook.user.name if webhook.user else 'N/A'}
**Creator ID:** ||{webhook.user.id if webhook.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(webhook.guild, 'webhook_create', description)

        @commands.Cog.listener()
        async def on_webhook_delete(self, webhook: discord.Webhook):
            description = f"""**Webhook:** {webhook.name}
**Webhook ID:** `{webhook.id}`
**Channel:** {webhook.channel.name}
**Channel ID:** `{webhook.channel.id}`
**Guild:** ||{webhook.guild.name} ({webhook.guild.id})||
**Deleter:** {webhook.user.name if webhook.user else 'N/A'}
**Deleter ID:** ||{webhook.user.id if webhook.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(webhook.guild, 'webhook_delete', description)

        @commands.Cog.listener()
        async def on_thread_create(self, thread: discord.Thread):
            description = f"""**Thread:** {thread.name}
**Thread ID:** `{thread.id}`
**Guild:** ||{thread.guild.name} ({thread.guild.id})||
**Creator:** {thread.owner.name if thread.owner else 'N/A'}
**Creator ID:** ||{thread.owner.id if thread.owner else 'N/A'}||
**Timestamp:** <t:{int(thread.created_at.timestamp())}:F>"""
            await self.log_event(thread.guild, 'thread_create', description)

        @commands.Cog.listener()
        async def on_thread_delete(self, thread: discord.Thread):
            description = f"""**Thread:** {thread.name}
**Thread ID:** `{thread.id}`
**Guild:** ||{thread.guild.name} ({thread.guild.id})||
**Deleter:** {thread.owner.name if thread.owner else 'N/A'}
**Deleter ID:** ||{thread.owner.id if thread.owner else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(thread.guild, 'thread_delete', description)

        @commands.Cog.listener()
        async def on_thread_update(self, before: discord.Thread, after:
            discord.Thread):
            description = f"""**Before Thread:** {before.name}
**After Thread:** {after.name}
**Thread ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.owner.name if before.owner else 'N/A'}
**Updater ID:** ||{before.owner.id if before.owner else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'thread_update', description)

        @commands.Cog.listener()
        async def on_thread_member_join(self, member: discord.ThreadMember):
            description = f"""**Member:** {member.name}
**Member ID:** `{member.id}`
**Thread:** {member.thread.name}
**Thread ID:** `{member.thread.id}`
**Guild:** ||{member.guild.name} ({member.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(member.guild, 'thread_member_join',
                description)

        @commands.Cog.listener()
        async def on_thread_member_remove(self, member: discord.ThreadMember):
            description = f"""**Member:** {member.name}
**Member ID:** `{member.id}`
**Thread:** {member.thread.name}
**Thread ID:** `{member.thread.id}`
**Guild:** ||{member.guild.name} ({member.guild.id})||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(member.guild, 'thread_member_remove',
                description)

        @commands.Cog.listener()
        async def on_guild_sticker_create(self, sticker: discord.Sticker):
            description = f"""**Sticker:** {sticker.name}
**Sticker ID:** `{sticker.id}`
**Guild:** ||{sticker.guild.name} ({sticker.guild.id})||
**Creator:** {sticker.user.name if sticker.user else 'N/A'}
**Creator ID:** ||{sticker.user.id if sticker.user else 'N/A'}||
**Timestamp:** <t:{int(sticker.created_at.timestamp())}:F>"""
            await self.log_event(sticker.guild, 'guild_sticker_create',
                description)

        @commands.Cog.listener()
        async def on_guild_sticker_delete(self, sticker: discord.Sticker):
            description = f"""**Sticker:** {sticker.name}
**Sticker ID:** `{sticker.id}`
**Guild:** ||{sticker.guild.name} ({sticker.guild.id})||
**Deleter:** {sticker.user.name if sticker.user else 'N/A'}
**Deleter ID:** ||{sticker.user.id if sticker.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(sticker.guild, 'guild_sticker_delete',
                description)

        @commands.Cog.listener()
        async def on_guild_sticker_update(self, before: discord.Sticker,
            after: discord.Sticker):
            description = f"""**Before Sticker:** {before.name}
**After Sticker:** {after.name}
**Sticker ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.user.name if before.user else 'N/A'}
**Updater ID:** ||{before.user.id if before.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild, 'guild_sticker_update',
                description)

        @commands.Cog.listener()
        async def on_soundboard_sound_upload(self, sound):
            description = f"""**Sound:** {sound.name}
**Sound ID:** `{sound.id}`
**Guild:** ||{sound.guild.name} ({sound.guild.id})||
**Uploader:** {sound.user.name if sound.user else 'N/A'}
**Uploader ID:** ||{sound.user.id if sound.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(sound.guild, 'soundboard_sound_upload',
                description)

        @commands.Cog.listener()
        async def on_soundboard_sound_name_update(self, before, after):
            description = f"""**Before Sound:** {before.name}
**After Sound:** {after.name}
**Sound ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.user.name if before.user else 'N/A'}
**Updater ID:** ||{before.user.id if before.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'soundboard_sound_name_update', description)

        @commands.Cog.listener()
        async def on_soundboard_sound_volume_update(self, before, after):
            description = f"""**Before Volume:** {before.volume}
**After Volume:** {after.volume}
**Sound ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.user.name if before.user else 'N/A'}
**Updater ID:** ||{before.user.id if before.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'soundboard_sound_volume_update', description)

        @commands.Cog.listener()
        async def on_soundboard_sound_emoji_update(self, before, after):
            description = f"""**Before Emoji:** {before.emoji}
**After Emoji:** {after.emoji}
**Sound ID:** `{before.id}`
**Guild:** ||{before.guild.name} ({before.guild.id})||
**Updater:** {before.user.name if before.user else 'N/A'}
**Updater ID:** ||{before.user.id if before.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(before.guild,
                'soundboard_sound_emoji_update', description)

        @commands.Cog.listener()
        async def on_soundboard_sound_delete(self, sound):
            description = f"""**Sound:** {sound.name}
**Sound ID:** `{sound.id}`
**Guild:** ||{sound.guild.name} ({sound.guild.id})||
**Deleter:** {sound.user.name if sound.user else 'N/A'}
**Deleter ID:** ||{sound.user.id if sound.user else 'N/A'}||
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(sound.guild, 'soundboard_sound_delete',
                description)

        @commands.Cog.listener()
        async def on_typing(self, channel: discord.abc.Messageable, user:
            Union[discord.User, discord.Member], when: datetime):
            if isinstance(channel, discord.DMChannel):
                return
            description = f"""**User:** {user.name} ({user.mention})
**User ID:** `{user.id}`
**Channel:** {channel.name}
**Channel ID:** `{channel.id}`
**Guild:** ||{channel.guild.name} ({channel.guild.id})||
**Timestamp:** <t:{int(when.timestamp())}:F>"""
            await self.log_event(channel.guild, 'typing', description)

        @commands.Cog.listener()
        async def on_reaction_add(self, reaction: discord.Reaction, user:
            discord.User):
            if reaction.message.guild is None:
                return
            description = f"""**User:** {user.name} ({user.mention})
**User ID:** `{user.id}`
**Message ID:** `{reaction.message.id}`
**Channel:** {reaction.message.channel.name}
**Channel ID:** `{reaction.message.channel.id}`
**Guild:** ||{reaction.message.guild.name} ({reaction.message.guild.id})||
**Emoji:** {reaction.emoji}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(reaction.message.guild, 'reaction_add',
                description)

        @commands.Cog.listener()
        async def on_reaction_remove(self, reaction: discord.Reaction, user:
            discord.User):
            if reaction.message.guild is None:
                return
            description = f"""**User:** {user.name} ({user.mention})
**User ID:** `{user.id}`
**Message ID:** `{reaction.message.id}`
**Channel:** {reaction.message.channel.name}
**Channel ID:** `{reaction.message.channel.id}`
**Guild:** ||{reaction.message.guild.name} ({reaction.message.guild.id})||
**Emoji:** {reaction.emoji}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(reaction.message.guild, 'reaction_remove',
                description)
>>>>>>> 9e308722 (Revamped and Fixed)
