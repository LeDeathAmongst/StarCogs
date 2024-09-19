from Star_Utils import Cog
from redbot.core import commands, Config
from redbot.core.bot import Red
from datetime import datetime
import discord
from .dashboard_integration import DashboardIntegration


class AdvancedLogger(DashboardIntegration, Cog):
    """A cog for advanced logging of various actions in a server"""

    def __init__(self, bot: Red):
        self.bot: Red = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_guild = {'member_log_channel': None, 'role_log_channel':
            None, 'role_permissions_log_channel': None,
            'message_log_channel': None, 'channel_log_channel': None,
            'channel_permissions_log_channel': None, 'webhook_log_channel':
            None, 'app_log_channel': None, 'voice_log_channel': None,
            'reaction_log_channel': None, 'emoji_log_channel': None,
            'kick_log_channel': None, 'ban_log_channel': None,
            'mute_log_channel': None, 'timeout_log_channel': None,
            'attachment_log_channel': None, 'link_log_channel': None,
            'slash_log_channel': None, 'guild_log_channel': None,
            'invite_log_channel': None, 'integration_log_channel': None,
            'typing_log_channel': None, 'thread_log_channel': None,
            'sticker_log_channel': None, 'scheduled_event_log_channel':
            None, 'stage_instance_log_channel': None, 'command_log_channel':
            None}
        self.config.register_guild(**default_guild)

    async def log_event(self, guild: discord.Guild, log_type: str, title:
        str, description: str, color: discord.Color=discord.Color.blue(),
        author: discord.Member=None):
        try:
            log_channel_id = await self.config.guild(guild).get_raw(
                log_type + '_log_channel')
            if log_channel_id:
                log_channel = self.bot.get_channel(log_channel_id)
                if log_channel:
                    embed = discord.Embed(title=title, description=
                        description, color=color, timestamp=datetime.utcnow())
                    if author:
                        embed.set_thumbnail(url=author.display_avatar.url)
                    await log_channel.send(embed=embed)
                else:
                    print(
                        f'Log channel not found for log type: {log_type} in guild {guild.name}'
                        )
            else:
                print(
                    f'No log channel set for log type: {log_type} in guild {guild.name}'
                    )
        except Exception as e:
            print(f'Failed to log event in guild {guild.name}: {e}')

    @commands.group()
    @commands.admin_or_permissions(manage_guild=True)
    async def logging(self, ctx):
        """Manage logging settings for various events in the server."""
        pass

    @logging.command()
    async def setchannel(self, ctx, log_type: str, channel: discord.TextChannel
        ):
        """Set the channel for logging events.

        **Valid log types**: member, role, role_permissions, message, channel, channel_permissions, webhook, app, voice, reaction, emoji, kick, ban, mute, timeout, attachment, link, slash, guild, invite, integration, typing, thread, sticker, scheduled_event, stage_instance, command

        **Example**:
        `[p]logging setchannel member #member-log`
        `[p]logging setchannel role #role-log`
        `[p]logging setchannel role_permissions #role-permissions-log`
        `[p]logging setchannel message #message-log`
        `[p]logging setchannel channel #channel-log`
        `[p]logging setchannel channel_permissions #channel-permissions-log`
        `[p]logging setchannel webhook #webhook-log`
        `[p]logging setchannel app #app-log`
        `[p]logging setchannel voice #voice-log`
        `[p]logging setchannel reaction #reaction-log`
        `[p]logging setchannel emoji #emoji-log`
        `[p]logging setchannel kick #kick-log`
        `[p]logging setchannel ban #ban-log`
        `[p]logging setchannel mute #mute-log`
        `[p]logging setchannel timeout #timeout-log`
        `[p]logging setchannel attachment #attachment-log`
        `[p]logging setchannel link #link-log`
        `[p]logging setchannel slash #slash-log`
        `[p]logging setchannel guild #guild-log`
        `[p]logging setchannel invite #invite-log`
        `[p]logging setchannel integration #integration-log`
        `[p]logging setchannel typing #typing-log`
        `[p]logging setchannel thread #thread-log`
        `[p]logging setchannel sticker #sticker-log`
        `[p]logging setchannel scheduled_event #scheduled_event-log`
        `[p]logging setchannel stage_instance #stage_instance-log`
        `[p]logging setchannel command #command-log`
        """
        valid_log_types = ['member', 'role', 'role_permissions', 'message',
            'channel', 'channel_permissions', 'webhook', 'app', 'voice',
            'reaction', 'emoji', 'kick', 'ban', 'mute', 'timeout',
            'attachment', 'link', 'slash', 'guild', 'invite', 'integration',
            'typing', 'thread', 'sticker', 'scheduled_event',
            'stage_instance', 'command']
        if log_type not in valid_log_types:
            await ctx.send(
                f"Invalid log type. Valid log types are: {', '.join(valid_log_types)}"
                )
            return
        await self.config.guild(ctx.guild).set_raw(log_type +
            '_log_channel', value=channel.id)
        await ctx.send(
            f'{log_type.capitalize()} logging channel set to {channel.mention}'
            )

    @logging.command()
    async def removechannel(self, ctx, log_type: str):
        """Remove the logging channel.

        **Valid log types**: member, role, role_permissions, message, channel, channel_permissions, webhook, app, voice, reaction, emoji, kick, ban, mute, timeout, attachment, link, slash, guild, invite, integration, typing, thread, sticker, scheduled_event, stage_instance, command

        **Example**:
        `[p]logging removechannel member`
        `[p]logging removechannel role`
        `[p]logging removechannel role_permissions`
        `[p]logging removechannel message`
        `[p]logging removechannel channel`
        `[p]logging removechannel channel_permissions`
        `[p]logging removechannel webhook`
        `[p]logging removechannel app`
        `[p]logging removechannel voice`
        `[p]logging removechannel reaction`
        `[p]logging removechannel emoji`
        `[p]logging removechannel kick`
        `[p]logging removechannel ban`
        `[p]logging removechannel mute`
        `[p]logging removechannel timeout`
        `[p]logging removechannel attachment`
        `[p]logging removechannel link`
        `[p]logging removechannel slash`
        `[p]logging removechannel guild`
        `[p]logging removechannel invite`
        `[p]logging removechannel integration`
        `[p]logging removechannel typing`
        `[p]logging removechannel thread`
        `[p]logging removechannel sticker`
        `[p]logging removechannel scheduled_event`
        `[p]logging removechannel stage_instance`
        `[p]logging removechannel command`
        """
        valid_log_types = ['member', 'role', 'role_permissions', 'message',
            'channel', 'channel_permissions', 'webhook', 'app', 'voice',
            'reaction', 'emoji', 'kick', 'ban', 'mute', 'timeout',
            'attachment', 'link', 'slash', 'guild', 'invite', 'integration',
            'typing', 'thread', 'sticker', 'scheduled_event',
            'stage_instance', 'command']
        if log_type not in valid_log_types:
            await ctx.send(
                f"Invalid log type. Valid log types are: {', '.join(valid_log_types)}"
                )
            return
        await self.config.guild(ctx.guild).set_raw(log_type +
            '_log_channel', value=None)
        await ctx.send(f'{log_type.capitalize()} logging channel removed')

    @commands.Cog.listener()
    async def on_command(self, ctx):
        """Log command usage."""
        guild = ctx.guild
        if guild:
            description = f"""**Command Used:** {ctx.command}
**User:** {ctx.author.mention} ({ctx.author.id})
**Channel:** {ctx.channel.mention}
**Message Content:** {ctx.message.content}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'command', 'Command Used',
                description, discord.Color.blue(), ctx.author)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return
        if before.content != after.content:
            guild = before.guild
            description = f"""**Message Edited in {before.channel.mention}**
**Before:** {before.content}
**After:** {after.content}
**Author:** {before.author.mention}
**Message ID:** {before.id}
**Channel ID:** {before.channel.id}
**Guild ID:** {before.guild.id}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'message', 'Message Edited',
                description, discord.Color.orange(), before.author)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        guild = message.guild
        description = f"""**Message Deleted in {message.channel.mention}**
**Content:** {message.content}
**Author:** {message.author.mention}
**Message ID:** {message.id}
**Channel ID:** {message.channel.id}
**Guild ID:** {message.guild.id}
**Timestamp:** <t:{int(message.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'message', 'Message Deleted',
            description, discord.Color.red(), message.author)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.is_expired():
            return
        if interaction.response.is_done():
            if (interaction.response.type == discord.
                InteractionResponseType.channel_message_with_source and
                interaction.response.is_ephemeral):
                guild = interaction.guild
                description = f"""**Ephemeral Message Sent in {interaction.channel.mention}**
**Content:** {interaction.response.message.content}
**Author:** {interaction.user.mention}
**Interaction ID:** {interaction.id}
**Channel ID:** {interaction.channel.id}
**Guild ID:** {interaction.guild.id}
**Timestamp:** <t:{int(interaction.created_at.timestamp())}:F>"""
                await self.log_event(guild, 'slash',
                    'Ephemeral Message Sent', description, discord.Color.
                    purple(), interaction.user)
            elif interaction.type == discord.InteractionType.application_command:
                guild = interaction.guild
                description = f"""**Slash Command Used in {interaction.channel.mention}**
**Command:** {interaction.data['name']}
**Author:** {interaction.user.mention}
**Interaction ID:** {interaction.id}
**Channel ID:** {interaction.channel.id}
**Guild ID:** {interaction.guild.id}
**Timestamp:** <t:{int(interaction.created_at.timestamp())}:F>"""
                await self.log_event(guild, 'slash', 'Slash Command Used',
                    description, discord.Color.blue(), interaction.user)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        description = f"""**Member Joined:** {member.mention} ({member})
**User ID:** {member.id}
**Account Created:** <t:{int(member.created_at.timestamp())}:F>
**Joined Server:** <t:{int(member.joined_at.timestamp())}:F>"""
        await self.log_event(guild, 'member', 'Member Joined', description,
            discord.Color.green(), member)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        description = f"""**Member Left:** {member.mention} ({member})
**User ID:** {member.id}
**Account Created:** <t:{int(member.created_at.timestamp())}:F>
**Joined Server:** <t:{int(member.joined_at.timestamp())}:F>
**Left Server:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'member', 'Member Left', description,
            discord.Color.red(), member)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        entry = await guild.audit_logs(action=discord.AuditLogAction.ban,
            limit=1).get()
        description = f"""**User:** {user.mention} ({user.id})
**Banned By:** {entry.user.mention} ({entry.user.id})
**Reason:** {entry.reason if entry.reason else 'No reason provided'}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'ban', 'User Banned', description,
            discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        entry = await guild.audit_logs(action=discord.AuditLogAction.unban,
            limit=1).get()
        description = f"""**User:** {user.mention} ({user.id})
**Unbanned By:** {entry.user.mention} ({entry.user.id})
**Reason:** {entry.reason if entry.reason else 'No reason provided'}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'ban', 'User Unbanned', description,
            discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_member_kick(self, guild, user):
        entry = await guild.audit_logs(action=discord.AuditLogAction.kick,
            limit=1).get()
        description = f"""**User:** {user.mention} ({user.id})
**Kicked By:** {entry.user.mention} ({entry.user.id})
**Reason:** {entry.reason if entry.reason else 'No reason provided'}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'kick', 'User Kicked', description,
            discord.Color.orange(), entry.user)

    @commands.Cog.listener()
    async def on_member_warn(self, guild, user):
        entry = await guild.audit_logs(action=discord.AuditLogAction.warn,
            limit=1).get()
        description = f"""**User:** {user.mention} ({user.id})
**Warned By:** {entry.user.mention} ({entry.user.id})
**Reason:** {entry.reason if entry.reason else 'No reason provided'}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'warn', 'User Warned', description,
            discord.Color.yellow(), entry.user)

    @commands.Cog.listener()
    async def on_member_mute(self, guild, user, duration):
        entry = await guild.audit_logs(action=discord.AuditLogAction.mute,
            limit=1).get()
        description = f"""**User:** {user.mention} ({user.id})
**Muted By:** {entry.user.mention} ({entry.user.id})
**Duration:** {duration}
**Reason:** {entry.reason if entry.reason else 'No reason provided'}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'mute', 'User Muted', description,
            discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_member_unmute(self, guild, user):
        entry = await guild.audit_logs(action=discord.AuditLogAction.unmute,
            limit=1).get()
        description = f"""**User:** {user.mention} ({user.id})
**Unmuted By:** {entry.user.mention} ({entry.user.id})
**Reason:** {entry.reason if entry.reason else 'No reason provided'}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'unmute', 'User Unmuted', description,
            discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_member_timeout(self, guild, user, duration):
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            timeout, limit=1).get()
        description = f"""**User:** {user.mention} ({user.id})
**Timed Out By:** {entry.user.mention} ({entry.user.id})
**Duration:** {duration}
**Reason:** {entry.reason if entry.reason else 'No reason provided'}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'timeout', 'User Timed Out',
            description, discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_message_attachment(self, message):
        if message.attachments:
            guild = message.guild
            for attachment in message.attachments:
                description = f"""**Attachment Added:**
**User:** {message.author.mention} ({message.author.id})
**Channel:** {message.channel.mention}
**Attachment URL:** [Link]({attachment.url})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'attachment',
                    'Attachment Added', description, discord.Color.blue(),
                    message.author)

    @commands.Cog.listener()
    async def on_message_link(self, message):
        if any(word.startswith('http') for word in message.content.split()):
            guild = message.guild
            description = f"""**Link Added:**
**User:** {message.author.mention} ({message.author.id})
**Channel:** {message.channel.mention}
**Message Content:** {message.content}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'link', 'Link Added', description,
                discord.Color.blue(), message.author)

    @commands.Cog.listener()
    async def on_channel_permissions_update(self, channel, before, after):
        guild = channel.guild
        if before.overwrites != after.overwrites:
            added_permissions = []
            removed_permissions = []
            for target, perms in after.overwrites.items():
                before_perms = before.overwrites.get(target)
                if before_perms is None:
                    added_permissions.append((target, perms))
                elif perms != before_perms:
                    added = [perm for perm, value in perms if value and not
                        getattr(before_perms, perm)]
                    removed = [perm for perm, value in before_perms if 
                        value and not getattr(perms, perm)]
                    if added:
                        added_permissions.append((target, added))
                    if removed:
                        removed_permissions.append((target, removed))
            description = (
                f'**Permissions Updated for Channel {before.name}:**\n')
            if added_permissions:
                description += '**Permissions Added:**\n'
                for target, perms in added_permissions:
                    description += (
                        f"**{target}:** {', '.join(perm for perm in perms)}\n")
            if removed_permissions:
                description += '**Permissions Removed:**\n'
                for target, perms in removed_permissions:
                    description += (
                        f"**{target}:** {', '.join(perm for perm in perms)}\n")
            description += f"""**Channel ID:** {before.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'channel_permissions',
                'Channel Permissions Updated', description, discord.Color.
                blue())

    @commands.Cog.listener()
    async def on_role_permissions_update(self, role, before, after):
        guild = role.guild
        if before.permissions != after.permissions:
            added_permissions = [perm for perm, value in after.permissions if
                value and not getattr(before.permissions, perm)]
            removed_permissions = [perm for perm, value in before.
                permissions if value and not getattr(after.permissions, perm)]
            description = f'**Permissions Updated for Role {before.name}:**\n'
            if added_permissions:
                description += (
                    f"**Permissions Added:** {', '.join(added_permissions)}\n")
            if removed_permissions:
                description += (
                    f"**Permissions Removed:** {', '.join(removed_permissions)}\n"
                    )
            description += f"""**Role ID:** {before.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'role_permissions',
                'Role Permissions Updated', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_role_create(self, role):
        guild = role.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            role_create, limit=1).get()
        description = f"""**Role Created:** {role.mention} ({role.name})
**Role ID:** {role.id}
**Created By:** {entry.user.mention} ({entry.user.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'role', 'Role Created', description,
            discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_role_delete(self, role):
        guild = role.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            role_delete, limit=1).get()
        description = f"""**Role Deleted:** {role.name}
**Role ID:** {role.id}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'role', 'Role Deleted', description,
            discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_role_update(self, before, after):
        guild = before.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            role_update, limit=1).get()
        if before.name != after.name:
            description = f"""**Role Renamed:** {before.name} -> {after.name}
**Role ID:** {before.id}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'role', 'Role Renamed', description,
                discord.Color.blue(), entry.user)

    @commands.Cog.listener()
    async def on_webhook_create(self, webhook):
        guild = webhook.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            webhook_create, limit=1).get()
        description = f"""**Webhook Created:** {webhook.name}
**Webhook ID:** {webhook.id}
**Created By:** {entry.user.mention} ({entry.user.id})
**Channel:** {webhook.channel.mention}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'webhook', 'Webhook Created',
            description, discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_webhook_update(self, webhook):
        guild = webhook.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            webhook_update, limit=1).get()
        description = f"""**Webhook Updated:** {webhook.name}
**Webhook ID:** {webhook.id}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Channel:** {webhook.channel.mention}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'webhook', 'Webhook Updated',
            description, discord.Color.blue(), entry.user)

    @commands.Cog.listener()
    async def on_webhook_delete(self, webhook):
        guild = webhook.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            webhook_delete, limit=1).get()
        description = f"""**Webhook Deleted:** {webhook.name}
**Webhook ID:** {webhook.id}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Channel:** {webhook.channel.mention}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'webhook', 'Webhook Deleted',
            description, discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_app_add(self, integration):
        guild = integration.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            integration_create, limit=1).get()
        description = f"""**App Invited:** {integration.name}
**App ID:** {integration.id}
**Invited By:** {entry.user.mention} ({entry.user.id})
**Permissions Level:** {integration.permissions}
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'app', 'App Invited', description,
            discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_app_remove(self, integration):
        guild = integration.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            integration_delete, limit=1).get()
        description = f"""**App Removed:** {integration.name}
**App ID:** {integration.id}
**Removed By:** {entry.user.mention} ({entry.user.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'app', 'App Removed', description,
            discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = member.guild
        if before.channel != after.channel:
            if before.channel is None:
                description = f"""**{member.mention} joined voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice', 'Voice Channel Join',
                    description, discord.Color.green(), member)
            elif after.channel is None:
                description = f"""**{member.mention} left voice channel:** {before.channel.mention}
**User ID:** {member.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice', 'Voice Channel Leave',
                    description, discord.Color.red(), member)
            else:
                description = f"""**{member.mention} switched voice channel:** {before.channel.mention} -> {after.channel.mention}
**User ID:** {member.id}
**Before Channel ID:** {before.channel.id}
**After Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice', 'Voice Channel Switch',
                    description, discord.Color.blue(), member)
        if before.self_mute != after.self_mute:
            if after.self_mute:
                description = f"""**{member.mention} muted themselves in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Self Mute', description, discord.Color.
                    orange(), member)
            else:
                description = f"""**{member.mention} unmuted themselves in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Self Unmute', description, discord.Color
                    .green(), member)
        if before.self_deaf != after.self_deaf:
            if after.self_deaf:
                description = f"""**{member.mention} deafened themselves in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Self Deafen', description, discord.Color
                    .orange(), member)
            else:
                description = f"""**{member.mention} undeafened themselves in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Self Undeafen', description, discord.
                    Color.green(), member)
        if before.mute != after.mute:
            if after.mute:
                description = f"""**{member.mention} was server muted in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Server Mute', description, discord.Color
                    .red(), member)
            else:
                description = f"""**{member.mention} was server unmuted in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Server Unmute', description, discord.
                    Color.green(), member)
        if before.deaf != after.deaf:
            if after.deaf:
                description = f"""**{member.mention} was server deafened in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Server Deafen', description, discord.
                    Color.red(), member)
            else:
                description = f"""**{member.mention} was server undeafened in voice channel:** {after.channel.mention}
**User ID:** {member.id}
**Channel ID:** {after.channel.id}
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
                await self.log_event(guild, 'voice',
                    'Voice Channel Server Undeafen', description, discord.
                    Color.green(), member)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return
        guild = reaction.message.guild
        description = f"""**Reaction Added:** {reaction.emoji}
**Message ID:** {reaction.message.id}
**Channel:** {reaction.message.channel.mention}
**User:** {user.mention} ({user.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>
**Message Content:** {reaction.message.content}
**Message Link:** [Jump to Message]({reaction.message.jump_url})"""
        await self.log_event(guild, 'reaction', 'Reaction Added',
            description, discord.Color.green(), user)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.bot:
            return
        guild = reaction.message.guild
        description = f"""**Reaction Removed:** {reaction.emoji}
**Message ID:** {reaction.message.id}
**Channel:** {reaction.message.channel.mention}
**User:** {user.mention} ({user.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>
**Message Content:** {reaction.message.content}
**Message Link:** [Jump to Message]({reaction.message.jump_url})"""
        await self.log_event(guild, 'reaction', 'Reaction Removed',
            description, discord.Color.red(), user)

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        before_emojis = set(before)
        after_emojis = set(after)
        added_emojis = after_emojis - before_emojis
        removed_emojis = before_emojis - after_emojis
        updated_emojis = {emoji for emoji in before_emojis & after_emojis if
            emoji.name != next(e.name for e in after if e.id == emoji.id)}
        for emoji in added_emojis:
            entry = await guild.audit_logs(action=discord.AuditLogAction.
                emoji_create, limit=1).get()
            description = f"""**Emoji Added:** {emoji} ({emoji.name})
**Emoji ID:** {emoji.id}
**Added By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'emoji', 'Emoji Added', description,
                discord.Color.green(), entry.user)
        for emoji in removed_emojis:
            entry = await guild.audit_logs(action=discord.AuditLogAction.
                emoji_delete, limit=1).get()
            description = f"""**Emoji Removed:** {emoji} ({emoji.name})
**Removed By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'emoji', 'Emoji Removed',
                description, discord.Color.red(), entry.user)
        for emoji in updated_emojis:
            entry = await guild.audit_logs(action=discord.AuditLogAction.
                emoji_update, limit=1).get()
            description = f"""**Emoji Updated:** {emoji} ({emoji.name})
**Emoji ID:** {emoji.id}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'emoji', 'Emoji Updated',
                description, discord.Color.blue(), entry.user)

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        guild = invite.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            invite_create, limit=1).get()
        description = f"""**Invite Created:**
**Code:** {invite.code}
**Channel:** {invite.channel.mention}
**Inviter:** {entry.user.mention} ({entry.user.id})
**Max Uses:** {invite.max_uses}
**Max Age:** {invite.max_age}
**Temporary:** {invite.temporary}
**Created At:** <t:{int(invite.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'invite', 'Invite Created', description,
            discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        guild = invite.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            invite_delete, limit=1).get()
        description = f"""**Invite Deleted:**
**Code:** {invite.code}
**Channel:** {invite.channel.mention}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Max Uses:** {invite.max_uses}
**Max Age:** {invite.max_age}
**Temporary:** {invite.temporary}
**Created At:** <t:{int(invite.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'invite', 'Invite Deleted', description,
            discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_integration_create(self, integration):
        guild = integration.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            integration_create, limit=1).get()
        description = f"""**Integration Created:**
**Name:** {integration.name}
**Type:** {integration.type}
**Enabled:** {integration.enabled}
**Account:** {integration.account.name}
**Created By:** {entry.user.mention} ({entry.user.id})
**Created At:** <t:{int(integration.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'integration', 'Integration Created',
            description, discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_integration_update(self, integration):
        guild = integration.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            integration_update, limit=1).get()
        description = f"""**Integration Updated:**
**Name:** {integration.name}
**Type:** {integration.type}
**Enabled:** {integration.enabled}
**Account:** {integration.account.name}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Updated At:** <t:{int(integration.updated_at.timestamp())}:F>"""
        await self.log_event(guild, 'integration', 'Integration Updated',
            description, discord.Color.blue(), entry.user)

    @commands.Cog.listener()
    async def on_integration_delete(self, integration):
        guild = integration.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            integration_delete, limit=1).get()
        description = f"""**Integration Deleted:**
**Name:** {integration.name}
**Type:** {integration.type}
**Enabled:** {integration.enabled}
**Account:** {integration.account.name}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Deleted At:** <t:{int(integration.deleted_at.timestamp())}:F>"""
        await self.log_event(guild, 'integration', 'Integration Deleted',
            description, discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        if user.bot:
            return
        guild = channel.guild
        description = f"""**User Typing:** {user.mention}
**Channel:** {channel.mention}
**User ID:** {user.id}
**Timestamp:** <t:{int(when.timestamp())}:F>"""
        await self.log_event(guild, 'typing', 'User Typing', description,
            discord.Color.blue(), user)

    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        guild = thread.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            thread_create, limit=1).get()
        description = f"""**Thread Created:** {thread.mention} ({thread.name})
**Thread ID:** {thread.id}
**Parent Channel:** {thread.parent.mention}
**Created By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(thread.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'thread', 'Thread Created', description,
            discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_thread_delete(self, thread):
        guild = thread.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            thread_delete, limit=1).get()
        description = f"""**Thread Deleted:** {thread.name}
**Thread ID:** {thread.id}
**Parent Channel:** {thread.parent.mention}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'thread', 'Thread Deleted', description,
            discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_thread_update(self, before, after):
        guild = before.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            thread_update, limit=1).get()
        if before.name != after.name:
            description = f"""**Thread Renamed:** {before.name} -> {after.name}
**Thread ID:** {before.id}
**Parent Channel:** {before.parent.mention}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'thread', 'Thread Renamed',
                description, discord.Color.blue(), entry.user)

    @commands.Cog.listener()
    async def on_sticker_create(self, sticker):
        guild = sticker.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            sticker_create, limit=1).get()
        description = f"""**Sticker Created:** {sticker.name}
**Sticker ID:** {sticker.id}
**Created By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(sticker.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'sticker', 'Sticker Created',
            description, discord.Color.green(), entry.user)

    @commands.Cog.listener()
    async def on_sticker_delete(self, sticker):
        guild = sticker.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            sticker_delete, limit=1).get()
        description = f"""**Sticker Deleted:** {sticker.name}
**Sticker ID:** {sticker.id}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'sticker', 'Sticker Deleted',
            description, discord.Color.red(), entry.user)

    @commands.Cog.listener()
    async def on_sticker_update(self, before, after):
        guild = before.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            sticker_update, limit=1).get()
        if before.name != after.name:
            description = f"""**Sticker Renamed:** {before.name} -> {after.name}
**Sticker ID:** {before.id}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'sticker', 'Sticker Renamed',
                description, discord.Color.blue(), entry.user)

    @commands.Cog.listener()
    async def on_scheduled_event_create(self, event):
        guild = event.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            scheduled_event_create, limit=1).get()
        description = f"""**Scheduled Event Created:** {event.name}
**Event ID:** {event.id}
**Created By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(event.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'scheduled_event',
            'Scheduled Event Created', description, discord.Color.green(),
            entry.user)

    @commands.Cog.listener()
    async def on_scheduled_event_delete(self, event):
        guild = event.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            scheduled_event_delete, limit=1).get()
        description = f"""**Scheduled Event Deleted:** {event.name}
**Event ID:** {event.id}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'scheduled_event',
            'Scheduled Event Deleted', description, discord.Color.red(),
            entry.user)

    @commands.Cog.listener()
    async def on_scheduled_event_update(self, before, after):
        guild = before.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            scheduled_event_update, limit=1).get()
        if before.name != after.name:
            description = f"""**Scheduled Event Renamed:** {before.name} -> {after.name}
**Event ID:** {before.id}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'scheduled_event',
                'Scheduled Event Renamed', description, discord.Color.blue(
                ), entry.user)

    @commands.Cog.listener()
    async def on_stage_instance_create(self, stage_instance):
        guild = stage_instance.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            stage_instance_create, limit=1).get()
        description = f"""**Stage Instance Created:** {stage_instance.channel.mention} ({stage_instance.channel.name})
**Topic:** {stage_instance.topic}
**Channel ID:** {stage_instance.channel.id}
**Created By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(stage_instance.created_at.timestamp())}:F>"""
        await self.log_event(guild, 'stage_instance',
            'Stage Instance Created', description, discord.Color.green(),
            entry.user)

    @commands.Cog.listener()
    async def on_stage_instance_delete(self, stage_instance):
        guild = stage_instance.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            stage_instance_delete, limit=1).get()
        description = f"""**Stage Instance Deleted:** {stage_instance.channel.mention} ({stage_instance.channel.name})
**Topic:** {stage_instance.topic}
**Channel ID:** {stage_instance.channel.id}
**Deleted By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
        await self.log_event(guild, 'stage_instance',
            'Stage Instance Deleted', description, discord.Color.red(),
            entry.user)

    @commands.Cog.listener()
    async def on_stage_instance_update(self, before, after):
        guild = before.guild
        entry = await guild.audit_logs(action=discord.AuditLogAction.
            stage_instance_update, limit=1).get()
        if before.topic != after.topic:
            description = f"""**Stage Instance Topic Updated:** {before.topic} -> {after.topic}
**Channel:** {before.channel.mention} ({before.channel.name})
**Channel ID:** {before.channel.id}
**Updated By:** {entry.user.mention} ({entry.user.id})
**Guild:** {guild.name} ({guild.id})
**Timestamp:** <t:{int(datetime.utcnow().timestamp())}:F>"""
            await self.log_event(guild, 'stage_instance',
                'Stage Instance Topic Updated', description, discord.Color.
                blue(), entry.user)
