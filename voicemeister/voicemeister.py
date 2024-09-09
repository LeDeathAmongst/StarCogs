from redbot.core import commands, Config
from redbot.core.bot import Red
import discord
from typing import Optional, Dict
from Star_Utils import Buttons, Dropdown, Cog, Settings

MAX_CHANNEL_NAME_LENGTH = 100
MAX_BITRATE = 96  # Maximum bitrate in kbps
DEFAULT_CHANNEL_NAME = "New Voice Channel"

DEFAULT_EMOJIS = {
    "lock": "<:Locked:1279848927587467447>",  # Locked
    "unlock": "<:Unlocked:1279848944570073109>",  # Unlocked
    "limit": "<:People:1279848931043573790>",  # People
    "hide": "<:Crossed_Eye:1279848957475819723>",  # Crossed_Eye
    "unhide": "<:Eye:1279848986299076728>",  # Eye
    "invite": "<:Invite:1279857570634272818>",  # Invite/Request Join
    "ban": "<:Hammer:1279848987922530365>",  # Hammer
    "permit": "<:Check_Mark:1279848948491747411>",  # Check_Mark
    "rename": "<:Pensil:1279848929126645879>",  # Pensil
    "bitrate": "<:Headphones:1279848994327232584>",  # Headphones
    "region": "<:Servers:1279848940786810891>",  # Servers
    "claim": "<:Crown:1279848977658810451>",  # Crown
    "transfer": "<:Person_With_Rotation:1279848936752021504>",  # Person_With_Rotation
    "info": "<:Information:1279848926383702056>",  # Info
    "delete": "<:TrashCan:1279875131136806993>",  # TrashCan
    "create_text": "<:SpeachBubble:1279890650535428198>",  # Speech Bubble
    "reset": "<:reset:1280057459146362880>"  # Reset
}

REGION_OPTIONS = [
    ("Automatic", None),
    ("Brazil", "brazil"),
    ("Hong Kong", "hongkong"),
    ("India", "india"),
    ("Japan", "japan"),
    ("Rotterdam", "rotterdam"),
    ("Russia", "russia"),
    ("Singapore", "singapore"),
    ("South Africa", "southafrica"),
    ("Sydney", "sydney"),
    ("US Central", "us-central"),
    ("US East", "us-east"),
    ("US South", "us-south"),
    ("US West", "us-west"),
]

class VoiceMeister(Cog):
    """Advanced voice channel control with join-to-create and more."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_guild = {
            "lobby_channel": None,
            "temp_channels": {},
            "user_limits": {},
            "banned_users": {},
            "allowed_users": {},
            "banned_roles": {},
            "allowed_roles": {},
            "owners": {}
        }
        self.config.register_guild(**default_guild)
        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=Config.GUILD,
            settings={
                "lobby_channel": {
                    "path": ["lobby_channel"],
                    "converter": discord.VoiceChannel,
                    "description": "Set the lobby channel for join-to-create.",
                }
            }
        )

    @commands.hybrid_command(name="setlobby", with_app_command=True)
    @commands.guild_only()
    @commands.admin_or_permissions(manage_channels=True)
    async def set_lobby(self, ctx: commands.Context, channel: discord.VoiceChannel):
        """Set the lobby channel for join-to-create."""
        await self.config.guild(ctx.guild).lobby_channel.set(channel.id)
        await ctx.send(f"Lobby channel set to {channel.name}.", ephemeral=True)

    @commands.hybrid_command(name="controlpanel", with_app_command=True)
    async def control_panel(self, ctx: commands.Context):
        """Open the voice control panel."""
        view = VoiceMeisterView(bot=self.bot, author=ctx.author, infinity=True)
        embed = discord.Embed(
            title="Voice Control Panel",
            description="\n".join([
                f"{DEFAULT_EMOJIS['lock']} Lock",
                f"{DEFAULT_EMOJIS['unlock']} Unlock",
                f"{DEFAULT_EMOJIS['limit']} User Limit",
                f"{DEFAULT_EMOJIS['hide']} Hide",
                f"{DEFAULT_EMOJIS['unhide']} Unhide",
                f"{DEFAULT_EMOJIS['invite']} Invite",
                f"{DEFAULT_EMOJIS['ban']} Ban",
                f"{DEFAULT_EMOJIS['permit']} Permit",
                f"{DEFAULT_EMOJIS['rename']} Rename",
                f"{DEFAULT_EMOJIS['bitrate']} Bitrate",
                f"{DEFAULT_EMOJIS['region']} Region",
                f"{DEFAULT_EMOJIS['claim']} Claim",
                f"{DEFAULT_EMOJIS['transfer']} Transfer",
                f"{DEFAULT_EMOJIS['info']} Info",
                f"{DEFAULT_EMOJIS['delete']} Delete Channel",
                f"{DEFAULT_EMOJIS['create_text']} Create Text Channel",
            ]),
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed, view=view, ephemeral=True)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        guild_data = await self.config.guild(member.guild).all()
        lobby_channel_id = guild_data["lobby_channel"]
        temp_channels = guild_data["temp_channels"]
        banned_roles = guild_data["banned_roles"]

        # Check if the user has any banned role
        if after.channel and any(role.id in banned_roles.get(after.channel.id, []) for role in member.roles):
            await member.move_to(None)
            return

        # Join-to-Create feature
        if after.channel and after.channel.id == lobby_channel_id:
            # Create a temporary channel
            category = after.channel.category
            permissions = {
                member: discord.PermissionOverwrite(connect=True, manage_channels=True)
            }
            temp_channel = await category.create_voice_channel(
                name=f"{member.name}'s Channel", overwrites=permissions
            )
            temp_channels[temp_channel.id] = temp_channel.id
            await self.config.guild(member.guild).temp_channels.set(temp_channels)

            # Move the member to the new channel
            await member.move_to(temp_channel)

        # Auto-delete temporary channels
        if before.channel and before.channel.id in temp_channels:
            if len(before.channel.members) == 0:
                await before.channel.delete()
                del temp_channels[before.channel.id]
                await self.config.guild(member.guild).temp_channels.set(temp_channels)

    async def locked(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Lock your AutoRoom."""
        try:
            await channel.set_permissions(interaction.guild.default_role, connect=False)
            await interaction.response.send_message(content=f"{channel.name} is now locked.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def unlock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Unlock your AutoRoom."""
        try:
            await channel.set_permissions(interaction.guild.default_role, connect=True)
            await interaction.response.send_message(content=f"{channel.name} is now unlocked.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def create_text_channel(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Create a temporary text channel linked to the voice channel."""
        try:
            existing_text_channel = self.get_text_channel(channel)
            if existing_text_channel:
                await interaction.response.send_message(f"You already have a linked text channel: {existing_text_channel.mention}.", ephemeral=True)
                return

            category = channel.category
            text_channel = await category.create_text_channel(
                name=f"{channel.name}-text",
                topic=f"Voice Channel ID: {channel.id}"
            )
            await text_channel.set_permissions(interaction.guild.default_role, read_messages=False)
            for member in channel.members:
                await text_channel.set_permissions(member, read_messages=True, send_messages=True)

            # Update the voice channel topic with the text channel ID
            await channel.edit(topic=f"Text Channel ID: {text_channel.id}")

            await interaction.response.send_message(content=f"Temporary text channel {text_channel.mention} created.", ephemeral=True)
        except discord.errors.HTTPException as e:
            if "Channel topic contains at least one word that is not allowed" in str(e):
                await interaction.response.send_message("Failed to set channel topic due to restricted words.", ephemeral=True)
            else:
                await self.handle_error(interaction, e)

    async def claim(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Claim ownership of the AutoRoom if there is no current owner, or override if admin/owner."""
        try:
            autoroom_info = await self.get_autoroom_info(channel)
            current_owner_id = autoroom_info.get("owner")

            if current_owner_id is None or self._has_override_permissions(interaction.user, autoroom_info):
                await self.config.channel(channel).owner.set(interaction.user.id)
                await channel.edit(name=f"{interaction.user.display_name}'s Channel")
                await interaction.response.send_message(content="You have claimed ownership of the channel.", ephemeral=True)
            else:
                current_owner = interaction.guild.get_member(current_owner_id)
                owner_name = current_owner.display_name if current_owner else "Unknown"
                await interaction.response.send_message(content=f"The channel is already owned by {owner_name}.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def delete_channel(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Delete the voice channel and linked text channel."""
        try:
            await channel.delete()
            await interaction.response.send_message(content="The channel has been deleted.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def transfer_ownership(self, interaction: discord.Interaction, channel: discord.VoiceChannel, new_owner: discord.Member):
        """Transfer ownership of the channel."""
        try:
            await self.config.channel(channel).owner.set(new_owner.id)
            await channel.edit(name=f"{new_owner.display_name}'s Channel")
            await interaction.response.send_message(content=f"Ownership transferred to {new_owner.display_name}.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def _process_allow_deny(self, interaction: discord.Interaction, action: str, channel: discord.VoiceChannel):
        """Process allowing or denying users/roles access to the AutoRoom."""
        try:
            text_channel = self.get_text_channel(channel)

            if action == "allow":
                await channel.set_permissions(interaction.guild.default_role, connect=True)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, read_messages=True)
                await interaction.response.send_message(content="The AutoRoom is now public.", ephemeral=True)
            elif action == "deny":
                await channel.set_permissions(interaction.guild.default_role, connect=False)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, read_messages=False)
                await interaction.response.send_message(content="The AutoRoom is now private.", ephemeral=True)
            elif action == "lock":
                await channel.set_permissions(interaction.guild.default_role, connect=False)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, send_messages=False)
                await interaction.response.send_message(content="The AutoRoom is now locked.", ephemeral=True)
            elif action == "unlock":
                await channel.set_permissions(interaction.guild.default_role, connect=True)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, send_messages=True)
                await interaction.response.send_message(content="The AutoRoom is now unlocked.", ephemeral=True)
            elif action == "private":
                await channel.set_permissions(interaction.guild.default_role, view_channel=False)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, view_channel=False)
                await interaction.response.send_message(content="The AutoRoom is now private.", ephemeral=True)
            elif action == "public":
                await channel.set_permissions(interaction.guild.default_role, view_channel=True)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, view_channel=True)
                await interaction.response.send_message(content="The AutoRoom is now public.", ephemeral=True)
            else:
                await interaction.response.send_message(content="Invalid action.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def info(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Provide information about the current voice channel."""
        try:
            autoroom_info = await self.get_autoroom_info(channel)
            owner_id = autoroom_info.get("owner")
            owner = interaction.guild.get_member(owner_id)
            owner_name = owner.display_name if owner else "None"
            owner_mention = owner.mention if owner else "None"

            channel_age = datetime.datetime.utcnow() - channel.created_at.replace(tzinfo=None)
            bitrate = channel.bitrate // 1000  # Convert to kbps
            user_limit = channel.user_limit or "Unlimited"
            rtc_region = channel.rtc_region or "Automatic"

            allowed_users = []
            denied_users = []
            for target, overwrite in channel.overwrites.items():
                if isinstance(target, discord.Member):
                    if overwrite.connect is True:
                        allowed_users.append(target.mention)
                    elif overwrite.connect is False:
                        denied_users.append(target.mention)

            allowed_users_text = ", ".join(allowed_users) if allowed_users else "No One"
            denied_users_text = ", ".join(denied_users) if denied_users else "No One"

            embed = discord.Embed(title=f"Info for {channel.name}", color=0x7289da)
            embed.add_field(name="Owner", value=f"{owner_name} ({owner_mention})")
            embed.add_field(name="Age", value=humanize_timedelta(timedelta=channel_age))
            embed.add_field(name="Bitrate", value=f"{bitrate} kbps")
            embed.add_field(name="User Limit", value=user_limit)
            embed.add_field(name="Region", value=rtc_region)
            embed.add_field(name="Private", value="Yes" if self._get_autoroom_type(channel, interaction.guild.default_role) == "private" else "No")
            embed.add_field(name="Allowed Users", value=allowed_users_text)
            embed.add_field(name="Denied Users", value=denied_users_text)

            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def change_region(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Change the region of the voice channel."""
        try:
            view = RegionSelectView(self, channel)
            await interaction.response.send_message("Select a region for the voice channel:", view=view, ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    def _has_override_permissions(self, user: discord.Member, autoroom_info: dict) -> bool:
        """Check if the user has override permissions."""
        if user.guild_permissions.administrator or user.id == user.guild.owner_id:
            return True
        return False

    @staticmethod
    def _get_current_voice_channel(member: discord.Member) -> Optional[discord.VoiceChannel]:
        """Get the member's current voice channel, or None if not in a voice channel."""
        if member.voice and isinstance(member.voice.channel, discord.VoiceChannel):
            return member.voice.channel
        return None

    @staticmethod
    def _get_autoroom_type(autoroom: discord.VoiceChannel, role: discord.Role) -> str:
        """Get the type of access a role has in an AutoRoom (public, locked, private, etc)."""
        view_channel = role.permissions.view_channel
        connect = role.permissions.connect
        if role in autoroom.overwrites:
            overwrites_allow, overwrites_deny = autoroom.overwrites[role].pair()
            if overwrites_allow.view_channel:
                view_channel = True
            if overwrites_allow.connect:
                connect = True
            if overwrites_deny.view_channel:
                view_channel = False
            if overwrites_deny.connect:
                connect = False
        if not view_channel and not connect:
            return "private"
        if view_channel and not connect:
            return "locked"
        return "public"

    async def handle_error(self, interaction: discord.Interaction, error: Exception):
        """Handle errors by sending a user-friendly message and optionally logging."""
        error_message = "An error occurred while processing your request. Please try again later."
        await interaction.response.send_message(content=error_message, ephemeral=True)

    def get_text_channel(self, voice_channel: discord.VoiceChannel) -> Optional[discord.TextChannel]:
        """Find a text channel associated with the voice channel."""
        category = voice_channel.category
        if category:
            for channel in category.channels:
                if isinstance(channel, discord.TextChannel) and channel.topic and f"Voice Channel ID: {voice_channel.id}" in channel.topic:
                    return channel
        return None

    def is_name_valid(self, name: str) -> bool:
        """Check if the name is valid (not explicit or racist)."""
        banned_words = ["explicit_word1", "explicit_word2", "racist_word1"]
        return not any(banned_word in name.lower() for banned_word in banned_words)

# View Class for Control Panel

class VoiceMeisterView(Buttons):
    def __init__(self, bot: Red, author: discord.Member, infinity: bool = True):
        buttons = [
            {"emoji": DEFAULT_EMOJIS["lock"], "custom_id": "lock"},
            {"emoji": DEFAULT_EMOJIS["unlock"], "custom_id": "unlock"},
            {"emoji": DEFAULT_EMOJIS["limit"], "custom_id": "limit"},
            {"emoji": DEFAULT_EMOJIS["hide"], "custom_id": "hide"},
            {"emoji": DEFAULT_EMOJIS["unhide"], "custom_id": "unhide"},
            {"emoji": DEFAULT_EMOJIS["invite"], "custom_id": "invite"},
            {"emoji": DEFAULT_EMOJIS["ban"], "custom_id": "ban"},
            {"emoji": DEFAULT_EMOJIS["permit"], "custom_id": "permit"},
            {"emoji": DEFAULT_EMOJIS["rename"], "custom_id": "rename"},
            {"emoji": DEFAULT_EMOJIS["bitrate"], "custom_id": "bitrate"},
            {"emoji": DEFAULT_EMOJIS["region"], "custom_id": "region"},
            {"emoji": DEFAULT_EMOJIS["claim"], "custom_id": "claim"},
            {"emoji": DEFAULT_EMOJIS["transfer"], "custom_id": "transfer"},
            {"emoji": DEFAULT_EMOJIS["info"], "custom_id": "info"},
            {"emoji": DEFAULT_EMOJIS["delete"], "custom_id": "delete"},
            {"emoji": DEFAULT_EMOJIS["create_text"], "custom_id": "create_text"},
        ]
        super().__init__(buttons=buttons, members=[author.id] + list(bot.owner_ids), function=self.on_button_click, infinity=infinity)
        self.bot = bot
        self.author = author

    async def on_button_click(self, view: Buttons, interaction: discord.Interaction):
        handlers = {
            "lock": self.handle_lock,
            "unlock": self.handle_unlock,
            "limit": self.handle_user_limit,
            "hide": self.handle_hide,
            "unhide": self.handle_unhide,
            "invite": self.handle_invite,
            "ban": self.handle_ban,
            "permit": self.handle_permit,
            "rename": self.handle_rename,
            "bitrate": self.handle_bitrate,
            "region": self.handle_region,
            "claim": self.handle_claim,
            "transfer": self.handle_transfer,
            "info": self.handle_info,
            "delete": self.handle_delete,
            "create_text": self.handle_create_text,
        }
        handler = handlers.get(interaction.data["custom_id"])
        if handler:
            voice_channel = self.bot.get_cog("VoiceMeister")._get_current_voice_channel(interaction.user)
            if voice_channel:
                await handler(interaction, voice_channel)

    async def handle_lock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").locked(interaction, channel)

    async def handle_unlock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").unlock(interaction, channel)

    async def handle_user_limit(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(SetUserLimitModal(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_hide(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister")._process_allow_deny(interaction, "private", channel)

    async def handle_unhide(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister")._process_allow_deny(interaction, "public", channel)

    async def handle_invite(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        invite = await channel.create_invite(max_uses=1, unique=True)
        await interaction.response.send_message(content=f"Here is your invite to the voice channel: {invite.url}", ephemeral=True)

    async def handle_ban(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(DenyAllowSelect(self.bot.get_cog("VoiceMeister"), channel, action="deny"))

    async def handle_permit(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(DenyAllowSelect(self.bot.get_cog("VoiceMeister"), channel, action="allow"))

    async def handle_rename(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(ChangeNameModal(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_bitrate(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(ChangeBitrateModal(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_region(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").change_region(interaction, channel)

    async def handle_claim(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").claim(interaction, channel)

    async def handle_transfer(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(TransferOwnershipSelect(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_info(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").info(interaction, channel)

    async def handle_delete(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").delete_channel(interaction, channel)

    async def handle_create_text(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").create_text_channel(interaction, channel)

# Select Menus

class DenyAllowSelect(Dropdown):
    def __init__(self, cog, channel, action):
        user_options = [{"label": member.display_name, "value": str(member.id)} for member in channel.guild.members]
        super().__init__(
            placeholder="Select a member",
            options=user_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel, "action": action}
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel, action):
        try:
            selected_user_id = int(options[0])
            user = channel.guild.get_member(selected_user_id)

            if user:
                permission = True if action == "allow" else False
                await channel.set_permissions(user, connect=permission)
                await interaction.response.send_message(f"{user.display_name} has been {'allowed' if permission else 'denied'} access to the channel.", ephemeral=True)
        except Exception as e:
            await cog.handle_error(interaction, e)

class TransferOwnershipSelect(Dropdown):
    def __init__(self, cog, channel):
        member_options = [{"label": member.display_name, "value": str(member.id)} for member in channel.members]
        super().__init__(
            placeholder="Select a new owner",
            options=member_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel}
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel):
        try:
            selected_user_id = int(options[0])
            new_owner = channel.guild.get_member(selected_user_id)

            if new_owner:
                await cog.transfer_ownership(interaction, channel, new_owner)
        except Exception as e:
            await cog.handle_error(interaction, e)

# Modal Classes

class ChangeBitrateModal(discord.ui.Modal, title="Change Bitrate"):
    def __init__(self, cog, channel):
        self.cog = cog
        self.channel = channel
        super().__init__()

    bitrate_value = discord.ui.TextInput(label="Bitrate (kbps)", custom_id="bitrate_value", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            bitrate_value = self.bitrate_value.value
            if not bitrate_value.isdigit() or int(bitrate_value) > MAX_BITRATE:
                await interaction.followup.send(f"Invalid bitrate. Please enter a value between 8 and {MAX_BITRATE} kbps.", ephemeral=True)
                return

            if self.channel:
                await self.channel.edit(bitrate=int(bitrate_value) * 1000)
                await interaction.followup.send(f"Bitrate changed to {bitrate_value} kbps.", ephemeral=True)
        except Exception as e:
            await self.cog.handle_error(interaction, e)

class ChangeNameModal(discord.ui.Modal, title="Change Channel Name"):
    def __init__(self, cog, channel):
        self.cog = cog
        self.channel = channel
        super().__init__()

    new_name = discord.ui.TextInput(label="New Channel Name", custom_id="new_channel_name", style=discord.TextStyle.short, max_length=MAX_CHANNEL_NAME_LENGTH)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            new_name = self.new_name.value
            if not self.cog.is_name_valid(new_name):
                await interaction.followup.send("The channel name contains inappropriate content. Please choose another name.", ephemeral=True)
                return

            if self.channel:
                await self.channel.edit(name=new_name)
                text_channel = self.cog.get_text_channel(self.channel)
                if text_channel:
                    await text_channel.edit(name=f"{new_name}-text")
                await interaction.followup.send(f"Channel name changed to {new_name}.", ephemeral=True)
        except Exception as e:
            await self.cog.handle_error(interaction, e)

class SetUserLimitModal(discord.ui.Modal, title="Set User Limit"):
    def __init__(self, cog, channel):
        self.cog = cog
        self.channel = channel
        super().__init__()

    user_limit_input = discord.ui.TextInput(label="User Limit (0 for Unlimited)", custom_id="user_limit_input", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            user_limit_value = self.user_limit_input.value
            if not user_limit_value.isdigit() or int(user_limit_value) < 0:
                await interaction.followup.send("Invalid user limit. Please enter a non-negative integer.", ephemeral=True)
                return

            user_limit = None if int(user_limit_value) == 0 else int(user_limit_value)
            await self.channel.edit(user_limit=user_limit)
            await interaction.followup.send(
                f"User limit set to {'Unlimited' if user_limit is None else str(user_limit) + ' members'}.",
                ephemeral=True
            )
        except Exception as e:
            await self.cog.handle_error(interaction, e)

class RegionSelectView(Dropdown):
    def __init__(self, cog, channel):
        region_options = [{"label": name, "value": region or "automatic"} for name, region in REGION_OPTIONS]
        super().__init__(
            placeholder="Select Region",
            options=region_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel}
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel):
        try:
            await interaction.response.defer(ephemeral=True)
            selected_region = options[0]
            rtc_region = None if selected_region == "automatic" else selected_region
            await channel.edit(rtc_region=rtc_region)
            await interaction.followup.send(f"Region changed to {selected_region if rtc_region else 'Automatic'}.", ephemeral=True)
        except Exception as e:
            await cog.handle_error(interaction, e)

async def setup(bot: Red):
    await bot.add_cog(VoiceMeister(bot))
