from Star_Utils import Cog, Settings
from redbot.core import commands, Config
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n
import discord
import typing
from typing import Union
import asyncio
from datetime import datetime
from .dashboard_integration import DashboardIntegration

_ = Translator('EventLogger', __file__)

@cog_i18n(_)
class EventLogger(Cog):
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
                "command_log_channel": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging command usage events.",
                },
                "typing": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging typing events.",
                },
                "thread_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging thread creation events.",
                },
                "automod_rule_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging automod rule creation events.",
                },
                "automod_rule_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging automod rule deletion events.",
                },
                "automod_rule_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging automod rule update events.",
                },
                "guild_emoji_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging emoji creation events.",
                },
                "guild_emoji_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging emoji deletion events.",
                },
                "guild_emoji_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging emoji update events.",
                },
                "scheduled_event_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging scheduled event creation.",
                },
                "scheduled_event_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging scheduled event deletion.",
                },
                "scheduled_event_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging scheduled event updates.",
                },
                "scheduled_event_user_add": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging users added to scheduled events.",
                },
                "scheduled_event_user_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging users removed from scheduled events.",
                },
                "user_roles_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging user role updates.",
                },
                "user_roles_add": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging roles added to users.",
                },
                "user_roles_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging roles removed from users.",
                },
                "user_avatar_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging user avatar updates.",
                },
                "user_timeout": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging user timeout events.",
                },
                "user_timeout_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging user timeout removal events.",
                },
                "webhook_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging webhook update events.",
                },
                "webhook_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging webhook creation events.",
                },
                "webhook_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging webhook deletion events.",
                },
                "thread_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging thread deletion events.",
                },
                "thread_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging thread update events.",
                },
                "thread_member_join": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging thread member join events.",
                },
                "thread_member_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging thread member remove events.",
                },
                "soundboard_sound_upload": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging soundboard sound upload events.",
                },
                "soundboard_sound_name_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging soundboard sound name update events.",
                },
                "soundboard_sound_volume_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging soundboard sound volume update events.",
                },
                "soundboard_sound_emoji_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging soundboard sound emoji update events.",
                },
                "soundboard_sound_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging soundboard sound deletion events.",
                },
        }

        default_guild = {event: None for event in settings_dict.keys()}
        self.config.register_guild(**default_guild)

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
            commands_group=self.seteventlogger
        )

    async def cog_load(self) -> None:
        await super().cog_load()
        await self.settings.add_commands()

    @commands.guild_only()
    @commands.is_owner()
    @commands.bot_has_permissions(manage_channels=True)
    @commands.group(name='setlog', invoke_without_command=True)
    async def setlog(self, ctx: commands.Context, event: str, channel: discord.TextChannel) -> None:
        """Set the logging channel for a specific event"""
        async with self.config.guild(ctx.guild).channels() as channels:
            channels[event] = channel.id
        await ctx.send(f'Logging channel for {event} set to {channel.mention}')

    @commands.guild_only()
    @commands.is_owner()
    @commands.bot_has_permissions(manage_channels=True)
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
        embed.set_footer(text=f"Event Logger | {self.bot.user.name}", icon_url=self.bot.user.avatar_url)
        return embed

    async def log_event(self, guild: typing.Optional[discord.Guild], event: str, description: str, color: discord.Color = discord.Color.blue()):
        if guild is None:
            return
        channels = await self.config.guild(guild).channels()
        channel_id = channels.get(event)
        if channel_id:
            channel = guild.get_channel(channel_id)
            if channel:
                embed = await self.create_embed(event, description, color)
                await self.event_queue.put((channel, embed))

    async def log_command(self, ctx, command_name: str):
        command_log_channel_id = await self.config.guild(ctx.guild).command_log_channel()
        if command_log_channel_id:
            channel = ctx.guild.get_channel(command_log_channel_id)
            if channel:
                description = (
                    f"🔧 **Command Executed**\n\n"
                    f"**Command:** {command_name}\n"
                    f"**User:** {ctx.author} (ID: {ctx.author.id})\n"
                    f"**Channel:** {ctx.channel.mention} (ID: {ctx.channel.id})\n"
                    f"**Guild:** {ctx.guild.name} (ID: {ctx.guild.id})\n"
                    f"**Executed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
                )
                embed = await self.create_embed('Command Executed', description, discord.Color.green())
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
        }
        embed = discord.Embed(title='Event Categories and Their Events', color=discord.Color.blue())
        for category, events in sorted(event_categories.items()):
            embed.add_field(name=category.capitalize(), value='\n'.join(sorted(events)), inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_integration_create(self, integration: discord.Integration):
        description = (
            f"🆕 **New Integration Added**\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Account:** {integration.account.name} (ID: {integration.account.id})\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Created At:** <t:{int(integration.created_at.timestamp())}:F>"
        )
        await self.log_event(integration.guild, 'integration_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_integration_delete(self, integration: discord.Integration):
        description = (
            f"🗑️ **Integration  Removed**\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(integration.guild, 'integration_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_integration_update(self, integration: discord.Integration):
        description = (
            f"🔄 **Integration Updated**\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(integration.guild, 'integration_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        description = (
            f"📢 **New Channel Created**\n\n"
            f"**Name:** {channel.name}\n"
            f"**ID:** `{channel.id}`\n"
            f"**Type:** {str(channel.type)}\n"
            f"**Category:** {channel.category.name if channel.category else 'None'}\n"
            f"**Position:** {channel.position}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(channel.guild, 'guild_channel_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        description = (
            f"🗑 ️ **Channel Deleted**\n\n"
            f"**Name:** {channel.name}\n"
            f"**ID:** `{channel.id}`\n"
            f"**Type:** {str(channel.type)}\n"
            f"**Category:** {channel.category.name if channel.category else 'None'}\n"
            f"**Position:** {channel.position}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(channel.guild, 'guild_channel_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        if before.position != after.position:
            return
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.category != after.category:
            changes.append(f"**Category:** {before.category.name if before.category else 'None'} → {after.category.name if after.category else 'None'}")
        if isinstance(before, discord.TextChannel) and isinstance(after, discord.TextChannel):
            if before.topic != after.topic:
                changes.append(f"**Topic:** {before.topic} → {after.topic}")
            if before.slowmode_delay != after.slowmode_delay:
                changes.append(f"**Slowmode:** {before.slowmode_delay}s → {after.slowmode_delay}s")
        description = (
            f"🔄 **Channel Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_pins_update(self, channel: discord.abc.GuildChannel, last_pin: discord.Message):
        description = (
            f"📌 **Channel Pins Updated**\n\n"
            f"**Channel:** {channel.name} (`{channel.id}`)\n"
            f"**Last Pin:** {last_pin.content if last_pin else 'None'}\n"
            f"**Pinner:** {last_pin.author.name if last_pin else 'N/A'} (`{last_pin.author.id if last_pin else 'N/A'}`)\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(channel.guild, 'guild_channel_pins_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_name_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        description = (
            f"✏️ **Channel Name Updated**\n\n"
            f"**Before:** {before.name}\n"
            f"**After:** {after.name}\n"
            f"**Channel ID:** `{before.id}`\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_name_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_topic_update(self, before: discord.TextChannel, after: discord.TextChannel):
        description = (
            f"📝 **Channel Topic Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {before.topic}\n"
            f"**After:** {after.topic}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_topic_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_nsfw_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        description = (
            f"🔞 **Channel NSFW Status Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {'NSFW' if before.is_nsfw() else 'Not NSFW'}\n"
            f"**After:** {'NSFW' if after.is_nsfw() else 'Not NSFW'}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_nsfw_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_parent_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        description = (
            f"📁 **Channel Category Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {before.category.name if before.category else 'None'}\n"
            f"**After:** {after.category.name if after.category else 'None'}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_parent_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_permissions_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        description = (
            f"🔒 **Channel Permissions Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_permissions_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_type_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        description = (
            f"🔄 **Channel Type Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {str(before.type)}\n"
            f"**After:** {str(after.type)}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_type_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_bitrate_update(self, before: discord.VoiceChannel, after: discord.VoiceChannel):
        description = (
            f"🎙 ️ **Voice Channel Bitrate Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {before.bitrate} bps\n"
            f"**After:** {after.bitrate} bps\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_bitrate_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_user_limit_update(self, before: discord.VoiceChannel, after: discord.VoiceChannel):
        description = (
            f"👥 **Voice Channel User Limit Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {before.user_limit}\n"
            f"**After:** {after.user_limit}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_user_limit_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_slowmode_update(self, before: discord.TextChannel, after: discord.TextChannel):
        description = (
            f"⏱️ **Channel Slowmode Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {before.slowmode_delay}s\n"
            f"**After:** {after.slowmode_delay}s\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_slowmode_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_rtc_region_update(self, before: discord.VoiceChannel, after: discord.VoiceChannel):
        description = (
            f"🌍 **Voice Channel Region Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {before.rtc_region}\n"
            f"**After:** {after.rtc_region}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_rtc_region_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_video_quality_update(self, before: discord.VoiceChannel, after: discord.VoiceChannel):
        description = (
            f"🎥 **Voice Channel Video Quality Updated**\n\n"
            f"**Channel:** {after.name} (`{after.id}`)\n"
            f"**Before:** {before.video_quality_mode}\n"
            f"**After:** {after.video_quality_mode}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_channel_video_quality_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        description = (
            f"🎙 ️ **Voice State Updated**\n\n"
            f"**Member:** {member.name} (`{member.id}`)\n"
            f"**Before Channel:** {before.channel.name if before.channel else 'None'}\n"
            f"**After Channel:** {after.channel.name if after.channel else 'None'}\n"
            f"**Muted:** {before.mute} → {after.mute}\n"
            f"**Deafened:** {before.deaf} → {after.deaf}\n"
            f"**Self Muted:** {before.self_mute} → {after.self_mute}\n"
            f"**Self Deafened:** {before.self_deaf} → {after.self_deaf}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(member.guild, 'voice_state_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_automod_rule_create(self, rule: discord.AutoModRule):
        description = (
            f"🛡️ **Auto Mod Rule Created**\n\n"
            f"**Rule Name:** {rule.name}\n"
            f"**Rule ID:** `{rule.id}`\n"
            f"**Creator:** {rule.creator.name} (`{rule.creator.id}`)\n"
            f"**Trigger Type:** {rule.trigger_type}\n"
            f"**Created At:** <t:{int(rule.created_at.timestamp())}:F>"
        )
        await self.log_event(rule.guild, 'automod_rule_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_automod_rule_delete(self, rule: discord.AutoModRule):
        description = (
            f"🗑️  **AutoMod Rule Deleted**\n\n"
            f"**Rule Name:** {rule.name}\n"
            f"**Rule ID:** `{rule.id}`\n"
            f"**Creator:** {rule.creator.name} (`{rule.creator.id}`)\n"
            f"**Trigger Type:** {rule.trigger_type}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(rule.guild, 'automod_rule_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_automod_rule_update(self, before: discord.AutoModRule, after: discord.AutoModRule):
        description = (
            f"🔄 **AutoMod Rule Updated**\n\n"
            f"**Rule Name:** {after.name}\n"
            f"**Rule ID:** `{after.id}`\n"
            f"**Creator:** {after.creator.name} (`{after.creator.id}`)\n"
            f"**Trigger Type:** {after.trigger_type}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(after.guild, 'automod_rule_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild: discord.Guild, before: list[discord.Emoji], after: list[discord.Emoji]):
        added_emojis = [emoji for emoji in after if emoji not in before]
        removed_emojis = [emoji for emoji in before if emoji not in after]
        description = (
            f"😀 **Guild Emojis Updated**\n\n"
            f"**Added Emojis:** {', '.join([str(emoji) for emoji in added_emojis]) or 'None'}\n"
            f"**Removed Emojis:** {', '.join([str(emoji) for emoji in removed_emojis]) or 'None'}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(guild, 'guild_emojis_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_emoji_create(self, emoji: discord.Emoji):
        description = (
            f"😀 **New Emoji Created**\n\n"
            f"**Emoji:** {emoji}\n"
            f"**Name:** {emoji.name}\n"
            f"**ID:** `{emoji.id}`\n"
            f"**Created By:** {emoji.user.name if emoji.user else 'Unknown'} (`{emoji.user.id if emoji.user else 'Unknown'}`)\n"
            f"**Created At:** <t:{int(emoji.created_at.timestamp())}:F>"
        )
        await self.log_event(emoji.guild, 'guild_emoji_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_emoji_delete(self, emoji: discord.Emoji):
        description = (
            f"🗑 ️ **Emoji Deleted**\n\n"
            f"**Emoji:** {emoji}\n"
            f"**Name:** {emoji.name}\n"
            f"**ID:** `{emoji.id}`\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(emoji.guild, 'guild_emoji_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_emoji_update(self, before: discord.Emoji, after: discord.Emoji):
        description = (
            f"🔄 **Emoji Updated**\n\n"
            f"**Emoji:** {after}\n"
            f"**Before Name:** {before.name}\n"
            f"**After Name:** {after.name}\n"
            f"**ID:** `{after.id}`\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(after.guild, 'guild_emoji_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_scheduled_event_create(self, event: discord.ScheduledEvent):
        description = (
            f"📅 **Scheduled Event Created**\n\n"
            f"**Name:** {event.name}\n"
            f"**Description:** {event.description}\n"
            f"**Start Time:** <t:{int(event.start_time.timestamp())}:F>\n"
            f"**End Time:** {f'<t:{int(event.end_time.timestamp())}:F>' if event.end_time else 'Not specified'}\n"
            f"**Location:** {event.location}\n"
            f"**Creator:** {event.creator.name} (`{event.creator.id}`)\n"
            f"**Created At:** <t:{int(event.created_at.timestamp())}:F>"
        )
        await self.log_event(event.guild, 'scheduled_event_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_scheduled_event_delete(self, event: discord.ScheduledEvent):
        description = (
            f"🗑️  **Scheduled Event Deleted**\n\n"
            f"**Name:** {event.name}\n"
            f"**Description:** {event.description}\n"
            f"**Start Time:** <t:{int(event.start_time.timestamp())}:F>\n"
            f"**End Time:** {f'<t:{int(event.end_time.timestamp())}:F>' if event.end_time else 'Not specified'}\n"
            f"**Location:** {event.location}\n"
            f"**Creator:** {event.creator.name} (`{event.creator.id}`)\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(event.guild, 'scheduled_event_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_scheduled_event_update(self, before: discord.ScheduledEvent, after: discord.ScheduledEvent):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.description != after.description:
            changes.append(f"**Description:** {before.description} → {after.description}")
        if before.start_time != after.start_time:
            changes.append(f"**Start Time:** <t:{int(before.start_time.timestamp())}:F> → <t:{int(after.start_time.timestamp())}:F>")
        if before.end_time != after.end_time:
            changes.append(f"**End Time:** {f'<t:{int(before.end_time.timestamp())}:F>' if before.end_time else 'Not specified'} → {f'<t:{int(after.end_time.timestamp())}:F>' if after.end_time else 'Not specified'}")
        if before.location != after.location:
            changes.append(f"**Location:** {before.location} → {after.location}")

        description = (
            f"🔄 **Scheduled Event Updated**\n\n"
            f"**Event:** {after.name}\n"
            f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(after.guild, 'scheduled_event_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_scheduled_event_user_add(self, event: discord.ScheduledEvent, user: discord.User):
        description = (
            f"👤 **User Subscribed to Event**\n\n"
            f"**Event:** {event.name}\n"
            f"**User:** {user.name} (`{user.id}`)\n"
            f"**Subscribed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(event.guild, 'scheduled_event_user_add', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_scheduled_event_user_remove(self, event: discord.ScheduledEvent, user: discord.User):
        description = (
            f"👤 **User Unsubscribed from Event**\n\n"
            f"**Event:** {event.name}\n"
            f"**User:** {user.name} (`{user.id}`)\n"
            f"**Unsubscribed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(event.guild, 'scheduled_event_user_remove', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        description = (
            f"🔗 **Invite Created**\n\n"
            f"**Invite URL:** {invite.url}\n"
            f"**Inviter:** {invite.inviter.name} (`{invite.inviter.id}`)\n"
            f"**Channel:** {invite.channel.name} (`{invite.channel.id}`)\n"
            f"**Max Uses:** {invite.max_uses if invite.max_uses else 'Unlimited'}\n"
            f"**Expires At:** {f'<t:{int(invite.expires_at.timestamp())}:F>' if invite.expires_at else 'Never'}\n"
            f"**Created At:** <t:{int(invite.created_at.timestamp())}:F>"
        )
        await self.log_event(invite.guild, 'invite_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_invite_delete(self, invite: discord.Invite):
        description = (
            f"🗑 ️ **Invite Deleted**\n\n"
            f"**Invite URL:** {invite.url}\n"
            f"**Inviter:** {invite.inviter.name} (`{invite.inviter.id}`) if invite.inviter else 'Unknown'\n"
            f"**Channel:** {invite.channel.name} (`{invite.channel.id}`)\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(invite.guild, 'invite_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.guild is None:
            return
        description = (
            f"🗑️  **Message Deleted**\n\n"
            f"**Author:** {message.author.name} (`{message.author.id}`)\n"
            f"**Channel:** {message.channel.name} (`{message.channel.id}`)\n"
            f"**Content:** {message.content}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(message.guild, 'message_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages: list[discord.Message]):
        if messages[0].guild is None:
            return
        description = (
            f"🗑️ ** Bulk Message Delete**\n\n"
            f"**Channel:** {messages[0].channel.name} (`{messages[0].channel.id}`)\n"
            f"**Message Count:** {len(messages)}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(messages[0].guild, 'bulk_message_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.guild is None:
            return
        if before.content == after.content:
            return
        description = (
            f"✏️ **Message Edited**\n\n"
            f"**Author:** {before.author.name} (`{before.author.id}`)\n"
            f"**Channel:** {before.channel.name} (`{before.channel.id}`)\n"
            f"**Before:** {before.content}\n"
            f"**After:** {after.content}\n"
            f"**Edited At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'message_edit', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_role_create(self, role: discord.Role):
        description = (
            f"🎭 **Role Created**\n\n"
            f"**Name:** {role.name}\n"
            f"**ID:** `{role.id}`\n"
            f"**Color:** {role.color}\n"
            f"**Permissions:** {role.permissions.value}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(role.guild, 'guild_role_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.Role):
        description = (
            f"🗑️ **Role  Deleted**\n\n"
            f"**Name:** {role.name}\n"
            f"**ID:** `{role.id}`\n"
            f"**Color:** {role.color}\n"
            f"**Permissions:** {role.permissions.value}\n"
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
            changes.append(f"**Permissions:** {before.permissions.value} → {after.permissions.value}")
        if before.hoist != after.hoist:
            changes.append(f"**Hoisted:** {before.hoist} → {after.hoist}")
        if before.mentionable != after.mentionable:
            changes.append(f"**Mentionable:** {before.mentionable} → {after.mentionable}")

        description = (
            f"🔄 **Role Updated**\n\n"
            f"**Role:** {after.name}\n"
            f"**ID:** `{after.id}`\n"
            f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'guild_role_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        description = (
            f"🔨 **Member Banned**\n\n"
            f"**User:** {user.name} ({user.mention})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Account Created:** <t:{int(user.created_at.timestamp())}:F>\n"
            f"**Banned At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(guild, 'member_ban', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        description = (
            f"🔓 **Member Unbanned**\n\n"
            f"**User:** {user.name} ({user.mention})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Account Created:** <t:{int(user.created_at.timestamp())}:F>\n"
            f"**Unbanned At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(guild, 'member_unban', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User):
        changes = []
        if before.name != after.name:
            changes.append(f"**Username:** {before.name} → {after.name}")
        if before.discriminator != after.discriminator:
            changes.append(f"**Discriminator:** {before.discriminator} → {after.discriminator}")
        if before.avatar != after.avatar:
            changes.append(f"**Avatar:** [Before]({before.avatar_url}) → [After]({after.avatar_url})")

        if changes:
            description = (
                f"👤 **User Updated**\n\n"
                f"**User:** {after.name} ({after.mention})\n"
                f"**User ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
            )
            await self.log_event(None, 'user_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
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

        if changes:
            description = (
                f"📝 **Member Updated**\n\n"
                f"**Member:** {after.name} ({after.mention})\n"
                f"**Member ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
            )
            await self.log_event(after.guild, 'member_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_user_roles_update(self, before: discord.Member, after: discord.Member):
        added_roles = set(after.roles) - set(before.roles)
        removed_roles = set(before.roles) - set(after.roles)

        description = (
            f"🎭 **User Roles Updated**\n\n"
            f"**Member:** {after.name} ({after.mention})\n"
            f"**Member ID:** `{after.id}`\n"
        )

        if added_roles:
            description += f"**Roles Added:** {', '.join(role.name for role in added_roles)}\n"
        if removed_roles:
            description += f"**Roles Removed:** {', '.join(role.name for role in removed_roles)}\n"

        description += f"\n**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        await self.log_event(after.guild, 'user_roles_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_user_roles_add(self, member: discord.Member, role: discord.Role):
        description = (
            f"➕ **Role Added to User**\n\n"
            f"**Member:** {member.name} ({member.mention})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Role Added:** {role.name} (ID: {role.id})\n"
            f"**Added At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(member.guild, 'user_roles_add', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_user_roles_remove(self, member: discord.Member, role: discord.Role):
        description = (
            f"➖ **Role Removed from User**\n\n"
            f"**Member:** {member.name} ({member.mention})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Role Removed:** {role.name} (ID: {role.id})\n"
            f"**Removed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(member.guild, 'user_roles_remove', description, discord.Color.orange())

    @commands.Cog.listener()
    async def on_user_avatar_update(self, before: discord.User, after: discord.User):
        description = (
            f"🖼️  **User Avatar Updated**\n\n"
            f"**User:** {after.name} ({after.mention})\n"
            f"**User ID:** `{after.id}`\n"
            f"**Old Avatar:** [Link]({before.avatar_url})\n"
            f"**New Avatar:** [Link]({after.avatar_url})\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(None, 'user_avatar_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_user_timeout(self, member: discord.Member):
        description = (
            f"⏳ **User Timed Out**\n\n"
            f"**Member:** {member.name} ({member.mention})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Timeout Until:** <t:{int(member.timed_out_until.timestamp())}:F>\n"
            f"**Timed Out At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(member.guild, 'user_timeout', description, discord.Color.orange())

    @commands.Cog.listener()
    async def on_user_timeout_remove(self, member: discord.Member):
        description = (
            f"⌛ **User Timeout Removed**\n\n"
            f"**Member:** {member.name} ({member.mention})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Timeout Removed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(member.guild, 'user_timeout_remove', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_webhook_update(self, channel: discord.abc.GuildChannel):
        description = (
            f"🔗 **Webhook Updated**\n\n"
            f"**Channel:** {channel.name} ({channel.mention})\n"
            f"**Channel ID:** `{channel.id}`\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(channel.guild, 'webhook_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_webhook_create(self, webhook: discord.Webhook):
        description = (
            f"🆕 **Webhook Created**\n\n"
            f"**Webhook Name:** {webhook.name}\n"
            f"**Webhook ID:** `{webhook.id}`\n"
            f"**Channel:** {webhook.channel.name} ({webhook.channel.mention})\n"
            f"**Created At:** <t:{int(webhook.created_at.timestamp())}:F>"
        )
        await self.log_event(webhook.guild, 'webhook_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_webhook_delete(self, webhook: discord.Webhook):
        description = (
            f"🗑️ ** Webhook Deleted**\n\n"
            f"**Webhook Name:** {webhook.name}\n"
            f"**Webhook ID:** `{webhook.id}`\n"
            f"**Channel:** {webhook.channel.name} ({webhook.channel.mention})\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(webhook.guild, 'webhook_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_thread_create(self, thread: discord.Thread):
        description = (
            f"🧵 **Thread Create d**\n\n"
            f"**Thread Name:** {thread.name}\n"
            f"**Thread ID:** `{thread.id}`\n"
            f"**Parent Channel:** {thread.parent.name} ({thread.parent.mention})\n"
            f"**Created At:** <t:{int(thread.created_at.timestamp())}:F>"
        )
        await self.log_event(thread.guild, 'thread_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_thread_delete(self, thread: discord.Thread):
        description = (
            f"🗑️ **Threa d Deleted**\n\n"
            f"**Thread Name:** {thread.name}\n"
            f"**Thread ID:** `{thread.id}`\n"
            f"**Parent Channel:** {thread.parent.name} ({thread.parent.mention})\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(thread.guild, 'thread_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_thread_update(self, before: discord.Thread, after: discord.Thread):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.archived != after.archived:
            changes.append(f"**Archived:** {before.archived} → {after.archived}")
        if before.locked != after.locked:
            changes.append(f"**Locked:** {before.locked} → {after.locked}")
        if before.slowmode_delay != after.slowmode_delay:
            changes.append(f"**Slowmode Delay:** {before.slowmode_delay} → {after.slowmode_delay}")

        if changes:
            description = (
                f"🔄 **Thread Updated**\n\n"
                f"**Thread:** {after.name}\n"
                f"**Thread ID:** `{after.id}`\n"
                f"**Parent Channel:** {after.parent.name} ({after.parent.mention})\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
            )
            await self.log_event(after.guild, 'thread_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_thread_member_join(self, member: discord.ThreadMember):
        description = (
            f"➕ **Member Joined Thread**\n\n"
            f"**Member:** {member.name} ({member.mention})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Thread:** {member.thread.name}\n"
            f"**Thread ID:** `{member.thread.id}`\n"
            f"**Joined At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(member.thread.guild, 'thread_member_join', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_thread_member_remove(self, member: discord.ThreadMember):
        description = (
            f"➖ **Member Left Thread**\n\n"
            f"**Member:** {member.name} ({member.mention})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Thread:** {member.thread.name}\n"
            f"**Thread ID:** `{member.thread.id}`\n"
            f"**Left At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(member.thread.guild, 'thread_member_remove', description, discord.Color.orange())

    @commands.Cog.listener()
    async def on_guild_sticker_create(self, sticker: discord.GuildSticker):
        description = (
            f"🆕 **Sticker Created**\n\n"
            f"**Sticker Name:** {sticker.name}\n"
            f"**Sticker ID:** `{sticker.id}`\n"
            f"**Description:** {sticker.description}\n"
            f"**Emoji:** {sticker.emoji}\n"
            f"**Created At:** <t:{int(sticker.created_at.timestamp())}:F>"
        )
        await self.log_event(sticker.guild, 'guild_sticker_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_sticker_delete(self, sticker: discord.GuildSticker):
        description = (
            f"🗑️  **Sticker Deleted**\n\n"
            f"**Sticker Name:** {sticker.name}\n"
            f"**Sticker ID:** `{sticker.id}`\n"
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
                f"🔄 **Sticker Updated**\n\n"
                f"**Sticker:** {after.name}\n"
                f"**Sticker ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
            )
            await self.log_event(after.guild, 'guild_sticker_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_soundboard_sound_upload(self, sound):
        description = (
            f"🔊 **Soundboard Sound Uploaded**\n\n"
            f"**Sound Name:** {sound.name}\n"
            f"**Sound ID:** `{sound.id}`\n"
            f"**Uploader:** {sound.user.name} ({sound.user.mention})\n"
            f"**Uploaded At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(sound.guild, 'soundboard_sound_upload', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_soundboard_sound_name_update(self, before, after):
        description = (
            f"✏️ **Soundboard Sound Name Updated**\n\n"
            f"**Old Name:** {before.name}\n"
            f"**New Name:** {after.name}\n"
            f"**Sound ID:** `{before.id}`\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'soundboard_sound_name_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_soundboard_sound_volume_update(self, before, after):
        description = (
            f"🔊 **Soundboard Sound Volume Updated**\n\n"
            f"**Sound Name:** {before.name}\n"
            f"**Sound ID:** `{before.id}`\n"
            f"**Old Volume:** {before.volume}\n"
            f"**New Volume:** {after.volume}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'soundboard_sound_volume_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_soundboard_sound_emoji_update(self, before, after):
        description = (
            f"😀 **Soundboard Sound Emoji Updated**\n\n"
            f"**Sound Name:** {before.name}\n"
            f"**Sound ID:** `{before.id}`\n"
            f"**Old Emoji:** {before.emoji}\n"
            f"**New Emoji:** {after.emoji}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(before.guild, 'soundboard_sound_emoji_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_soundboard_sound_delete(self, sound):
        description = (
            f"🗑 ️ **Soundboard Sound Deleted**\n\n"
            f"**Sound Name:** {sound.name}\n"
            f"**Sound ID:** `{sound.id}`\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(sound.guild, 'soundboard_sound_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_typing(self, channel: discord.abc.Messageable, user: Union[discord.User, discord.Member], when: datetime):
        if isinstance(channel, discord.DMChannel):
            return
        description = (
            f"⌨️ **User Started Typing**\n\n"
            f"**User:** {user.name} ({user.mention})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Channel:** {channel.name} ({channel.mention})\n"
            f"**Started Typing At:** <t:{int(when.timestamp())}:F>"
        )
        await self.log_event(channel.guild, 'typing', description, discord.Color.light_grey())

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        if reaction.message.guild is None:
            return
        description = (
            f"➕ **Reaction Added**\n\n"
            f"**User:** {user.name} ({user.mention})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Message ID:** `{reaction.message.id}`\n"
            f"**Channel:** {reaction.message.channel.name} ({reaction.message.channel.mention})\n"
            f"**Emoji:** {reaction.emoji}\n"
            f"**Added At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(reaction.message.guild, 'reaction_add', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: discord.Reaction, user: discord.User):
        if reaction.message.guild is None:
            return
        description = (
            f"➖ **Reaction Removed**\n\n"
            f"**User:** {user.name} ({user.mention})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Message ID:** `{reaction.message.id}`\n"
            f"**Channel:** {reaction.message.channel.name} ({reaction.message.channel.mention})\n"
            f"**Emoji:** {reaction.emoji}\n"
            f"**Removed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(reaction.message.guild, 'reaction_remove', description, discord.Color.orange())
