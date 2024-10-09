from Star_Utils import Cog
from redbot.core import commands, Config
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n
import discord
import typing
from typing, import Union
import asyncio
from datetime import datetime
from .dashboard_integration import DashboardIntegration

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

    @commands.guild_only()
    @commands.is_owner()
    @commands.bot_has_permissions(manage_channels=True)
    @commands.hybrid_group(name='setlog', invoke_without_command=True)
    async def setlog(self, ctx: commands.Context, event: str, channel: discord.TextChannel) -> None:
        """Set the logging channel for a specific event"""
        async with self.config.guild(ctx.guild).channels() as channels:
            channels[event] = channel.id
        await ctx.send(f'Logging channel for {event} set to {channel.mention}')

    @commands.guild_only()
    @commands.is_owner()
    @commands.bot_has_permissions(manage_channels=True)
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
                await self.event_queue.put((channel, embed))

    async def log_command(self, ctx, command_name: str):
        command_log_channel_id = await self.config.guild(ctx.guild).command_log_channel()
        if command_log_channel_id:
            channel = ctx.guild.get_channel(command_log_channel_id)
            if channel:
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
