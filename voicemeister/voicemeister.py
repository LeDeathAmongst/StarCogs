from contextlib import suppress
from typing import Any, Optional, Tuple, List
import discord
from redbot.core import Config, checks, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import success, error, warning, info
from redbot.core.utils.predicates import MessagePredicate
from Star_Utils import Buttons, Dropdown, Cog, Settings, Loop
from .star_lib import Perms, SettingDisplay
import datetime
import asyncio
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests

MAX_CHANNEL_NAME_LENGTH = 100
BITRATE_OPTIONS = [8, 16, 24, 32, 48, 56, 64, 72, 80, 88, 96]  # Bitrate options in kbps
DEFAULT_CHANNEL_NAME = "Voice Legion"

DEFAULT_EMOJIS = {
    "lock": "<:Locked:1279848927587467447>",
    "unlock": "<:Unlocked:1279848944570073109>",
    "limit": "<:People:1279848931043573790>",
    "hide": "<:Crossed_Eye:1279848957475819723>",
    "unhide": "<:Eye:1279848986299076728>",
    "invite": "<:Invite:1279857570634272818>",
    "ban": "<:Hammer:1279848987922530365>",
    "permit": "<:Check_Mark:1279848948491747411>",
    "rename": "<:Pensil:1279848929126645879>",
    "bitrate": "<:Headphones:1279848994327232584>",
    "region": "<:Servers:1279848940786810891>",
    "claim": "<:Crown:1279848977658810451>",
    "transfer": "<:Person_With_Rotation:1279848936752021504>",
    "info": "<:Information:1279848926383702056>",
    "delete": "<:TrashCan:1279875131136806993>",
    "create_text": "<:SpeachBubble:1279890650535428198>"
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
        self.config.init_custom("VOICEMEISTER_SOURCE", 2)
        self.config.register_custom("VOICEMEISTER_SOURCE", default={})
        default_guild = {
            "lobby_channel": None,
            "category": None,
            "temp_channels": {},
            "user_limits": {},
            "banned_users": {},
            "allowed_users": {},
            "banned_roles": {},
            "allowed_roles": {},
            "owners": {},
            "linked_text_channels": {}
        }
        self.config.register_guild(**default_guild)

        self.settings = Settings(
            bot=bot,
            cog=self,
            config=None,  # Replace with actual config if needed
            group="guild",
            settings={
                "lobby_channel": {
                    "path": ["lobby_channel"],
                    "converter": int,
                    "command_name": "lobbychannel",
                    "label": "Lobby Channel",
                    "description": "Set the lobby channel for voice channel creation.",
                },
                "category": {
                    "path": ["category"],
                    "converter": int,
                    "command_name": "category",
                    "label": "Category",
                    "description": "Set the category for temporary voice channels.",
                },
                "temp_channels": {
                    "path": ["temp_channels"],
                    "converter": dict,
                    "command_name": "tempchannels",
                    "label": "Temporary Channels",
                    "description": "Manage temporary channels.",
                },
                "owners": {
                    "path": ["owners"],
                    "converter": dict,
                    "command_name": "owners",
                    "label": "Channel Owners",
                    "description": "Manage channel ownership.",
                },
                "linked_text_channels": {
                    "path": ["linked_text_channels"],
                    "converter": dict,
                    "command_name": "linkedtextchannels",
                    "label": "Linked Text Channels",
                    "description": "Manage linked text channels.",
                },
            }
        )

        # Initialize loops
        self.loops = []

    @commands.hybrid_command(name="interface", with_app_command=True)
    async def interface(self, ctx: commands.Context):
        """Open the voice interface."""
        image = await self._generate_interface_image(ctx)
        file = discord.File(fp=image, filename="interface.png")
        view = VoiceMeisterView(bot=self.bot, author=ctx.author, infinity=True)
        embed = discord.Embed(
            title="Voice Interface",
            description="Use these buttons to control your private voice!",
            color=discord.Color.blue()
        )
        embed.set_image(url="attachment://interface.png")
        await ctx.send(embed=embed, file=file, view=view, ephemeral=True)

    async def _generate_interface_image(self, ctx: commands.Context) -> BytesIO:
        """Generate an image for the interface description using Discord emojis."""
        actions = [
            ("lock", "Lock"),
            ("unlock", "Unlock"),
            ("hide", "Hide"),
            ("unhide", "Unhide"),
            ("limit", "Limit"),
            ("ban", "Ban"),
            ("permit", "Permit"),
            ("claim", "Claim"),
            ("transfer", "Transfer"),
            ("info", "Info"),
            ("rename", "Rename"),
            ("bitrate", "Bitrate"),
            ("region", "Region"),
            ("create_text", "Chat"),
            ("delete", "Delete"),
            ("invite", "Invite")
        ]

        # Calculate the size of each box
        box_width = 150
        box_height = 70
        padding = 10
        total_width = box_width * 4 + padding * 3
        total_height = box_height * 4 + padding * 3

        # Create the image with a transparent background
        image = Image.new("RGBA", (total_width, total_height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Use a default font provided by Pillow
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
        except IOError:
            font = ImageFont.load_default()

        # Use the bot's color for both border and text
        bot_color = ctx.me.color.to_rgb()

        # Draw the boxes, emojis, and names
        for i, (emoji_name, name) in enumerate(actions):
            x = (i % 4) * (box_width + padding)
            y = (i // 4) * (box_height + padding)
            draw.rectangle([x, y, x + box_width, y + box_height], outline=bot_color, width=2)

            # Fetch emoji image
            emoji_id = DEFAULT_EMOJIS[emoji_name].split(":")[2].strip(">")
            emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.png"
            response = requests.get(emoji_url)
            emoji_image = Image.open(BytesIO(response.content)).resize((30, 30))
            image.paste(emoji_image, (x + 5, y + (box_height - 30) // 2), emoji_image)

            # Draw the name next to the emoji
            text_bbox = font.getbbox(name)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            draw.text(
                (x + 40, y + (box_height - text_height) / 2),
                name,
                fill=bot_color,
                font=font
            )

        # Save the image to a BytesIO object
        image_bytes = BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes.seek(0)
        return image_bytes

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        guild_data = await self.config.guild(member.guild).all()
        lobby_channel_id = guild_data["lobby_channel"]
        category_id = guild_data["category"]
        temp_channels = guild_data["temp_channels"]
        banned_roles = guild_data["banned_roles"]
        owners = guild_data["owners"]

        # Check if the user has any banned role
        if after.channel and any(role.id in banned_roles.get(after.channel.id, []) for role in member.roles):
            await member.move_to(None)
            return

        # Join-to-Create feature
        if after.channel and after.channel.id == lobby_channel_id:
            # Create a temporary channel in the specified category
            category = member.guild.get_channel(category_id)
            if category is None or not isinstance(category, discord.CategoryChannel):
                await member.send("The category for creating temporary voice channels is not set or invalid.")
                return

            permissions = {
                member: discord.PermissionOverwrite(connect=True, manage_channels=True)
            }
            temp_channel = await category.create_voice_channel(
                name=f"{member.name}'s Channel", overwrites=permissions
            )
            temp_channels[temp_channel.id] = temp_channel.id
            owners[str(temp_channel.id)] = member.id  # Assign ownership
            await self.config.guild(member.guild).temp_channels.set(temp_channels)
            await self.config.guild(member.guild).owners.set(owners)

            # Move the member to the new channel
            await member.move_to(temp_channel)

        # Auto-delete temporary channels and manage ownership
        if before.channel and before.channel.id in temp_channels:
            if len(before.channel.members) == 0:
                # Delete the channel if it's empty
                await before.channel.delete()
                del temp_channels[before.channel.id]
                del owners[str(before.channel.id)]
                await self.config.guild(member.guild).temp_channels.set(temp_channels)
                await self.config.guild(member.guild).owners.set(owners)
            elif str(before.channel.id) in owners and owners[str(before.channel.id)] == member.id:
                # Transfer ownership if the owner leaves
                remaining_members = before.channel.members
                if remaining_members:
                    new_owner = remaining_members[0]
                    owners[str(before.channel.id)] = new_owner.id
                    new_channel_name = f"{new_owner.display_name}'s Channel"
                    await before.channel.edit(name=new_channel_name)
                    await self.config.guild(member.guild).owners.set(owners)

    async def locked(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Lock your VoiceMeister."""
        try:
            await channel.set_permissions(interaction.guild.default_role, connect=False)
            await interaction.response.send_message(content=f"{channel.name} is now locked.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def unlock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Unlock your VoiceMeister."""
        try:
            await channel.set_permissions(interaction.guild.default_role, connect=True)
            await interaction.response.send_message(content=f"{channel.name} is now unlocked.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def create_text_channel(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Create a temporary text channel linked to the voice channel."""
        try:
            linked_channels = await self.config.guild(channel.guild).linked_text_channels()
            if channel.id in linked_channels:
                existing_text_channel = channel.guild.get_channel(linked_channels[channel.id])
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

            # Log the linked text channel
            linked_channels[channel.id] = text_channel.id
            await self.config.guild(channel.guild).linked_text_channels.set(linked_channels)

            await interaction.response.send_message(content=f"Temporary text channel {text_channel.mention} created.", ephemeral=True)
        except discord.errors.HTTPException as e:
            if "Channel topic contains at least one word that is not allowed" in str(e):
                await interaction.response.send_message("Failed to set channel topic due to restricted words.", ephemeral=True)
            else:
                await self.handle_error(interaction, e)

    async def claim(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Claim ownership of the VoiceMeister if there is no current owner, or override if admin/owner."""
        try:
            owners = await self.config.guild(channel.guild).owners()
            current_owner_id = owners.get(str(channel.id))

            if current_owner_id is None or self._has_override_permissions(interaction.user):
                owners[str(channel.id)] = interaction.user.id
                await self.config.guild(channel.guild).owners.set(owners)
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
            linked_channels = await self.config.guild(channel.guild).linked_text_channels()
            text_channel_id = linked_channels.get(channel.id)
            if text_channel_id:
                text_channel = channel.guild.get_channel(text_channel_id)
                if text_channel:
                    await text_channel.delete()

            await channel.delete()
            await interaction.response.send_message(content="The channel has been deleted.", ephemeral=True)

            # Clean up the stored data
            if channel.id in linked_channels:
                del linked_channels[channel.id]
                await self.config.guild(channel.guild).linked_text_channels.set(linked_channels)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def transfer_ownership(self, interaction: discord.Interaction, channel: discord.VoiceChannel, new_owner: discord.Member):
        """Transfer ownership of the channel."""
        try:
            owners = await self.config.guild(channel.guild).owners()
            owners[str(channel.id)] = new_owner.id
            await self.config.guild(channel.guild).owners.set(owners)
            await channel.edit(name=f"{new_owner.display_name}'s Channel")
            await interaction.response.send_message(content=f"Ownership transferred to {new_owner.display_name}.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def _process_allow_deny(self, interaction: discord.Interaction, action: str, channel: discord.VoiceChannel):
        """Process allowing or denying users/roles access to the VoiceMeister."""
        try:
            text_channel = self.get_text_channel(channel)

            if action == "allow":
                await channel.set_permissions(interaction.guild.default_role, connect=True)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, read_messages=True)
                await interaction.response.send_message(content="The VoiceMeister is now public.", ephemeral=True)
            elif action == "deny":
                await channel.set_permissions(interaction.guild.default_role, connect=False)
                if text_channel:
                    await text_channel.set_permissions(interaction.guild.default_role, read_messages=False)
                await interaction.response.send_message(content="The VoiceMeister is now private.", ephemeral=True)
            else:
                await interaction.response.send_message(content="Invalid action.", ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def info(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Provide information about the current voice channel."""
        try:
            owners = await self.config.guild(channel.guild).owners()
            owner_id = owners.get(str(channel.id))
            owner = channel.guild.get_member(owner_id)
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
            embed.add_field(name="Allowed Members", value=allowed_users_text)
            embed.add_field(name="Denied Members", value=denied_users_text)
            embed.add_field(name="Bitrate", value=f"{bitrate} kbps")
            embed.add_field(name="Time Created", value=channel.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.add_field(name="Last Update", value=channel.edited_at.strftime("%Y-%m-%d %H:%M:%S") if channel.edited_at else "Never")
            embed.add_field(name="User Limit", value=user_limit)
            embed.add_field(name="Region", value=rtc_region)

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

    async def cog_unload(self):
        for loop in self.loops:
            loop.stop_all()

    def _has_override_permissions(self, user: discord.Member) -> bool:
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
    def _get_voicemeister_type(voicemeister: discord.VoiceChannel, role: discord.Role) -> str:
        """Get the type of access a role has in a VoiceMeister (public, locked, private, etc)."""
        view_channel = role.permissions.view_channel
        connect = role.permissions.connect
        if role in voicemeister.overwrites:
            overwrites_allow, overwrites_deny = voicemeister.overwrites[role].pair()
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
        linked_channels = self.config.guild(voice_channel.guild).linked_text_channels()
        text_channel_id = linked_channels.get(voice_channel.id)
        return voice_channel.guild.get_channel(text_channel_id)

    def is_name_valid(self, name: str) -> bool:
        """Check if the name is valid (not explicit or racist)."""
        banned_words = ["explicit_word1", "explicit_word2", "racist_word1"]
        return not any(banned_word in name.lower() for banned_word in banned_words)

    def check_perms_source_dest(
        self,
        source_channel: discord.VoiceChannel,
        dest_category: discord.CategoryChannel,
        with_manage_roles_guild: bool = False,
        with_legacy_text_channel: bool = False,
        with_optional_clone_perms: bool = False,
        detailed: bool = False
    ) -> Tuple[bool, bool, str]:
        """Check permissions for the source and destination channels."""
        # Define required and optional permissions
        required_perms = {
            "view_channel": True,
            "connect": True,
            "speak": True,
            "move_members": True,
            "manage_channels": True,
            "create_instant_invite": True
        }
        optional_perms = {
            "manage_roles": with_manage_roles_guild,
            "send_messages": with_legacy_text_channel,
            "read_message_history": with_legacy_text_channel
        }
        if with_optional_clone_perms:
            optional_perms.update({
                "view_channel": True,
                "connect": True,
                "speak": True,
                "move_members": True,
                "manage_channels": True,
                "create_instant_invite": True
            })

        def check_permissions(channel: discord.abc.GuildChannel, perms: dict) -> bool:
            permissions = channel.permissions_for(channel.guild.me)
            # If the bot has Administrator, it has all permissions
            if permissions.administrator:
                return True
            return all(getattr(permissions, perm, None) == value for perm, value in perms.items())

        # Check permissions for the source and destination
        if source_channel.permissions_for(source_channel.guild.me).administrator:
            return True, True, ""  # If admin, all permissions are implicitly granted

        source_required = check_permissions(source_channel, required_perms)
        dest_required = check_permissions(dest_category, required_perms)
        source_optional = check_permissions(source_channel, optional_perms)
        dest_optional = check_permissions(dest_category, optional_perms)

        # Determine if all required and optional permissions are met
        required_check = source_required and dest_required
        optional_check = source_optional and dest_optional

        # Generate a detailed report if needed
        details = ""
        if detailed and not required_check:
            missing_required = [
                perm for perm, value in required_perms.items()
                if not check_permissions(source_channel, {perm: value}) or not check_permissions(dest_category, {perm: value})
            ]
            missing_optional = [
                perm for perm, value in optional_perms.items()
                if not check_permissions(source_channel, {perm: value}) or not check_permissions(dest_category, {perm: value})
            ]
            if missing_required or missing_optional:
                details = (
                    f"Missing required permissions: {', '.join(missing_required)}\n"
                    f"Missing optional permissions: {', '.join(missing_optional)}"
                )

        return required_check, optional_check, details

    def get_template_data(self, member: discord.Member | discord.User) -> dict[str, str]:
        """Retrieve template data for a member or user."""
        return {
            "username": member.display_name,
            "mention": member.mention,
            "id": str(member.id),
            "game": member.activity.name if member.activity else "No Game"
        }

    def format_template_room_name(self, template: str, data: dict, num: int = 1) -> str:
        """Format a room name based on a template."""
        try:
            formatted_name = template.format(**data)
            if num > 1:
                formatted_name += f" ({num})"
            return formatted_name
        except KeyError as e:
            raise RuntimeError(f"Template variable {e} not found.")

    async def is_admin_or_admin_role(self, who: discord.Role | discord.Member) -> bool:
        """Check if a role or member is an admin."""
        if isinstance(who, discord.Member):
            return who.guild_permissions.administrator
        elif isinstance(who, discord.Role):
            return any(role.permissions.administrator for role in who.guild.roles if role.id == who.id)
        return False

    async def is_mod_or_mod_role(self, who: discord.Role | discord.Member) -> bool:
        """Check if a role or member is a moderator."""
        if isinstance(who, discord.Member):
            return who.guild_permissions.manage_guild
        elif isinstance(who, discord.Role):
            return any(role.permissions.manage_guild for role in who.guild.roles if role.id == who.id)
        return False

    async def get_all_voicemeister_source_configs(
        self, guild: discord.Guild
    ) -> dict[int, dict[str, Any]]:
        """Get all VoiceMeister source configurations."""
        return await self.config.custom("VOICEMEISTER_SOURCE", str(guild.id)).all()

    async def get_voicemeister_source_config(
        self, voicemeister_source: discord.VoiceChannel | discord.abc.GuildChannel | None
    ) -> dict[str, Any] | None:
        """Get a specific VoiceMeister source configuration."""
        if voicemeister_source:
            return await self.config.custom("VOICEMEISTER_SOURCE", str(voicemeister_source.guild.id), str(voicemeister_source.id)).all()
        return None

    async def get_voicemeister_info(
        self, voicemeister: discord.VoiceChannel | None
    ) -> dict[str, Any] | None:
        """Get information about a VoiceMeister channel."""
        if voicemeister:
            return {
                "name": voicemeister.name,
                "bitrate": voicemeister.bitrate,
                "user_limit": voicemeister.user_limit,
                "region": voicemeister.rtc_region
            }
        return None

    async def get_voicemeister_legacy_text_channel(
        self, voicemeister: discord.VoiceChannel | int | None
    ) -> discord.TextChannel | None:
        """Get the legacy text channel associated with a VoiceMeister."""
        if isinstance(voicemeister, discord.VoiceChannel):
            linked_channels = await self.config.guild(voicemeister.guild).linked_text_channels()
            text_channel_id = linked_channels.get(voicemeister.id)
            return voicemeister.guild.get_channel(text_channel_id)
        return None

    @staticmethod
    def check_if_member_or_role_allowed(
        channel: discord.VoiceChannel,
        member_or_role: discord.Member | discord.Role,
    ) -> bool:
        """Check if a member or role is allowed in a channel."""
        overwrites = channel.overwrites_for(member_or_role)
        return overwrites.connect is not False

    def get_member_roles(
        self, voicemeister_source: discord.VoiceChannel
    ) -> list[discord.Role]:
        """Get roles that can access a VoiceMeister source."""
        return [role for role in voicemeister_source.guild.roles if role in voicemeister_source.overwrites]

    async def get_bot_roles(self, guild: discord.Guild) -> list[discord.Role]:
        """Get roles associated with the bot."""
        bot_roles = await self.config.guild(guild).bot_access()
        return [guild.get_role(role_id) for role_id in bot_roles if guild.get_role(role_id)]

    @commands.group()
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def voicemeisterset(self, ctx: commands.Context) -> None:
        """Configure the VoiceMeister cog.

        For a quick rundown on how to get started with this cog,
        check out [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/voicemeister/README.md)
        """

    @voicemeisterset.command()
    async def settings(self, ctx: commands.Context) -> None:
        """Display current settings."""
        if not ctx.guild:
            return
        server_section = SettingDisplay("Server Settings")
        server_section.add(
            "Admin access all VoiceMeisters",
            await self.config.guild(ctx.guild).admin_access(),
        )
        server_section.add(
            "Moderator access all VoiceMeisters",
            await self.config.guild(ctx.guild).mod_access(),
        )
        bot_roles = ", ".join(
            [role.name for role in await self.get_bot_roles(ctx.guild)]
        )
        if bot_roles:
            server_section.add("Bot roles allowed in all VoiceMeisters", bot_roles)

        voicemeister_sections = []
        avcs = await self.get_all_voicemeister_source_configs(ctx.guild)
        for avc_id, avc_settings in avcs.items():
            source_channel = ctx.guild.get_channel(avc_id)
            if not isinstance(source_channel, discord.VoiceChannel):
                continue
            dest_category = ctx.guild.get_channel(avc_settings["dest_category_id"])
            voicemeister_section = SettingDisplay(f"VoiceMeister - {source_channel.name}")
            voicemeister_section.add(
                "Room type",
                avc_settings["room_type"].capitalize(),
            )
            voicemeister_section.add(
                "Destination category",
                f"#{dest_category.name}" if dest_category else "INVALID CATEGORY",
            )
            if avc_settings["legacy_text_channel"]:
                voicemeister_section.add(
                    "Legacy Text Channel",
                    "True",
                )
            if not avc_settings["perm_send_messages"]:
                voicemeister_section.add(
                    "Send Messages",
                    "False",
                )
            if not avc_settings["perm_owner_manage_channels"]:
                voicemeister_section.add(
                    "Owner Manage Channel",
                    "False",
                )
            member_roles = self.get_member_roles(source_channel)
            if member_roles:
                voicemeister_section.add(
                    "Member Roles" if len(member_roles) > 1 else "Member Role",
                    ", ".join(role.name for role in member_roles),
                )
            room_name_format = "Username"
            if avc_settings["channel_name_type"] in channel_name_template:
                room_name_format = avc_settings["channel_name_type"].capitalize()
            elif (
                avc_settings["channel_name_type"] == "custom"
                and avc_settings["channel_name_format"]
            ):
                room_name_format = f'Custom: "{avc_settings["channel_name_format"]}"'
            voicemeister_section.add("Room name format", room_name_format)
            voicemeister_sections.append(voicemeister_section)

        message = server_section.display(*voicemeister_sections)
        required_check, optional_check, _ = await self._check_all_perms(ctx.guild)
        if not required_check:
            message += "\n" + error(
                "It looks like I am missing one or more required permissions. "
                "Until I have them, the VoiceMeister cog may not function properly "
                "for all VoiceMeister Sources. "
                "Check `[p]voicemeisterset permissions` for more information."
            )
        elif not optional_check:
            message += "\n" + warning(
                "All VoiceMeisters will work correctly, as I have all of the required permissions. "
                "However, it looks like I am missing one or more optional permissions "
                "for one or more VoiceMeisters. "
                "Check `[p]voicemeisterset permissions` for more information."
            )
        await ctx.send(message)

    @voicemeisterset.command(aliases=["perms"])
    async def permissions(self, ctx: commands.Context) -> None:
        """Check that the bot has all needed permissions."""
        if not ctx.guild:
            return
        required_check, optional_check, details_list = await self._check_all_perms(
            ctx.guild, detailed=True
        )
        if not details_list:
            await ctx.send(
                info(
                    "You don't have any VoiceMeister Sources set up! "
                    "Set one up with `[p]voicemeisterset create` first, "
                    "then I can check what permissions I need for it."
                )
            )
            return

        if (
            len(details_list) > 1
            and not ctx.channel.permissions_for(ctx.guild.me).add_reactions
        ):
            await ctx.send(
                error(
                    "Since you have multiple VoiceMeister Sources, "
                    'I need the "Add Reactions" permission to display permission information.'
                )
            )
            return

        if not required_check:
            await ctx.send(
                error(
                    "It looks like I am missing one or more required permissions. "
                    "Until I have them, the VoiceMeister Source(s) in question will not function properly."
                    "\n\n"
                    "The easiest way of fixing this is just giving me these permissions as part of my server role, "
                    "otherwise you will need to give me these permissions on the VoiceMeister Source and destination "
                    "category, as specified below."
                )
            )
        elif not optional_check:
            await ctx.send(
                warning(
                    "It looks like I am missing one or more optional permissions. "
                    "All VoiceMeisters will work, however some extra features may not work. "
                    "\n\n"
                    "The easiest way of fixing this is just giving me these permissions as part of my server role, "
                    "otherwise you will need to give me these permissions on the destination category, "
                    "as specified below."
                    "\n\n"
                    "In the case of optional permissions, any permission on the VoiceMeister Source will be copied to "
                    "the created VoiceMeister, as if we were cloning the VoiceMeister Source. In order for this to work, "
                    "I need each permission to be allowed in the destination category (or server). "
                    "If it isn't allowed, I will skip copying that permission over."
                )
            )
        else:
            await ctx.send(success("Everything looks good here!"))

        if len(details_list) > 1:
            if (
                ctx.channel.permissions_for(ctx.guild.me).add_reactions
                and ctx.channel.permissions_for(ctx.guild.me).read_message_history
            ):
                await menu(ctx, details_list, DEFAULT_CONTROLS, timeout=60.0)
            else:
                for details in details_list:
                    await ctx.send(details)
        else:
            await ctx.send(details_list[0])

    @voicemeisterset.group()
    async def access(self, ctx: commands.Context) -> None:
        """Control access to all VoiceMeisters.

        Roles that are considered "admin" or "moderator" are
        set up with the commands `[p]set addadminrole`
        and `[p]set addmodrole` (plus the remove commands too)
        """

    @access.command(name="admin")
    async def access_admin(self, ctx: commands.Context) -> None:
        """Allow Admins to join locked/private VoiceMeisters."""
        if not ctx.guild:
            return
        admin_access = not await self.config.guild(ctx.guild).admin_access()
        await self.config.guild(ctx.guild).admin_access.set(admin_access)
        await ctx.send(
            success(
                f"Admins are {'now' if admin_access else 'no longer'} able to join (new) locked/private VoiceMeisters."
            )
        )

    @access.command(name="mod")
    async def access_mod(self, ctx: commands.Context) -> None:
        """Allow Moderators to join locked/private VoiceMeisters."""
        if not ctx.guild:
            return
        mod_access = not await self.config.guild(ctx.guild).mod_access()
        await self.config.guild(ctx.guild).mod_access.set(mod_access)
        await ctx.send(
            success(
                f"Moderators are {'now' if mod_access else 'no longer'} able to join (new) locked/private VoiceMeisters."
            )
        )

    @access.group(name="bot")
    async def access_bot(self, ctx: commands.Context) -> None:
        """Automatically allow bots into VoiceMeisters.

        The VoiceMeister Owner is able to freely allow or deny these roles as they see fit.
        """

    @access_bot.command(name="add")
    async def access_bot_add(self, ctx: commands.Context, role: discord.Role) -> None:
        """Allow a bot role into every VoiceMeister."""
        if not ctx.guild:
            return
        bot_role_ids = await self.config.guild(ctx.guild).bot_access()
        if role.id not in bot_role_ids:
            bot_role_ids.append(role.id)
            await self.config.guild(ctx.guild).bot_access.set(bot_role_ids)

        role_list = "\n".join(
            [role.name for role in await self.get_bot_roles(ctx.guild)]
        )
        await ctx.send(
            success(
                f"VoiceMeisters will now allow the following bot roles in by default:\n\n{role_list}"
            )
        )

    @access_bot.command(name="remove", aliases=["delete", "del"])
    async def access_bot_remove(
        self, ctx: commands.Context, role: discord.Role
    ) -> None:
        """Disallow a bot role from joining every VoiceMeister."""
        if not ctx.guild:
            return
        bot_role_ids = await self.config.guild(ctx.guild).bot_access()
        if role.id in bot_role_ids:
            bot_role_ids.remove(role.id)
            await self.config.guild(ctx.guild).bot_access.set(bot_role_ids)

        if bot_role_ids:
            role_list = "\n".join(
                [role.name for role in await self.get_bot_roles(ctx.guild)]
            )
            await ctx.send(
                success(
                    f"VoiceMeisters will now allow the following bot roles in by default:\n\n{role_list}"
                )
            )
        else:
            await ctx.send(
                success("New VoiceMeisters will not allow any extra bot roles in.")
            )

    @voicemeisterset.command(aliases=["enable", "add"])
    async def create(
        self,
        ctx: commands.Context,
        source_voice_channel: discord.VoiceChannel,
        dest_category: discord.CategoryChannel,
    ) -> None:
        """Create an VoiceMeister Source.

        Anyone joining an VoiceMeister Source will automatically have a new
        voice channel (VoiceMeister) created in the destination category,
        and then be moved into it.
        """
        if not ctx.guild:
            return
        perms_required, perms_optional, details = self.check_perms_source_dest(
            source_voice_channel, dest_category, detailed=True
        )
        if not perms_required or not perms_optional:
            await ctx.send(
                error(
                    "I am missing a permission that the VoiceMeister cog requires me to have. "
                    "Check below for the permissions I require in both the VoiceMeister Source "
                    "and the destination category. "
                    "Try creating the VoiceMeister Source again once I have these permissions."
                    "\n"
                    f"{details}"
                    "\n"
                    "The easiest way of doing this is just giving me these permissions as part of my server role, "
                    "otherwise you will need to give me these permissions on the source channel and destination "
                    "category, as specified above."
                )
            )
            return
        new_source: dict[str, str | int] = {"dest_category_id": dest_category.id}

        # Room type
        options = ["public", "locked", "private", "server"]
        pred = MessagePredicate.lower_contained_in(options, ctx)
        await ctx.send(
            "**Welcome to the setup wizard for creating an VoiceMeister Source!**"
            "\n"
            f"Users joining the {source_voice_channel.mention} VoiceMeister Source will have an VoiceMeister "
            f"created in the {dest_category.mention} category and be moved into it."
            "\n\n"
            "**VoiceMeister Type**"
            "\n"
            "VoiceMeisters can be one of the following types when created:"
            "\n"
            "`public ` - Visible and joinable by other users. The VoiceMeister Owner can kick/ban users out of them."
            "\n"
            "`locked ` - Visible, but not joinable by other users. The VoiceMeister Owner must allow users into their room."
            "\n"
            "`private` - Not visible or joinable by other users. The VoiceMeister Owner must allow users into their room."
            "\n"
            "`server ` - Same as a public VoiceMeister, but with no VoiceMeister Owner. "
            "No modifications can be made to the generated VoiceMeister."
            "\n\n"
            "What would you like these created VoiceMeisters to be by default? (`public`/`locked`/`private`/`server`)"
        )
        answer = None
        with suppress(asyncio.TimeoutError):
            await ctx.bot.wait_for("message", check=pred, timeout=60)
            answer = pred.result
        if answer is not None:
            new_source["room_type"] = options[answer]
        else:
            await ctx.send("No valid answer was received, canceling setup process.")
            return

        # Check perms room type
        perms_required, perms_optional, details = self.check_perms_source_dest(
            source_voice_channel,
            dest_category,
            with_manage_roles_guild=new_source["room_type"] != "server",
            detailed=True,
        )
        if not perms_required or not perms_optional:
            await ctx.send(
                error(
                    f"Since you want to have this VoiceMeister Source create {new_source['room_type']} VoiceMeisters, "
                    "I will need a few extra permissions. "
                    "Try creating the VoiceMeister Source again once I have these permissions."
                    "\n"
                    f"{details}"
                )
            )
            return

        # Channel name
        options = ["username", "game"]
        pred = MessagePredicate.lower_contained_in(options, ctx)
        await ctx.send(
            "**Channel Name**"
            "\n"
            "When an VoiceMeister is created, a name will be generated for it. How would you like that name to be generated?"
            "\n\n"
            f'`username` - Shows up as "{ctx.author.display_name}\'s Room"\n'
            "`game    ` - VoiceMeister Owner's playing game, otherwise `username`"
        )
        answer = None
        with suppress(asyncio.TimeoutError):
            await ctx.bot.wait_for("message", check=pred, timeout=60)
            answer = pred.result
        if answer is not None:
            new_source["channel_name_type"] = options[answer]
        else:
            await ctx.send("No valid answer was received, canceling setup process.")
            return

        # Save new source
        await self.config.custom(
            "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(source_voice_channel.id)
        ).set(new_source)
        await ctx.send(
            success(
                "Settings saved successfully!\n"
                "Check out `[p]voicemeisterset modify` for even more VoiceMeister Source settings, "
                "or to make modifications to your above answers."
            )
        )

    @voicemeisterset.command(aliases=["disable", "delete", "del"])
    async def remove(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
    ) -> None:
        """Remove an VoiceMeister Source."""
        if not ctx.guild:
            return
        await self.config.custom(
            "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
        ).clear()
        await ctx.send(
            success(
                f"**{voicemeister_source.mention}** is no longer an VoiceMeister Source channel."
            )
        )

    @voicemeisterset.group(aliases=["edit"])
    async def modify(self, ctx: commands.Context) -> None:
        """Modify an existing VoiceMeister Source."""

    @modify.command(name="category")
    async def modify_category(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
        dest_category: discord.CategoryChannel,
    ) -> None:
        """Set the category that VoiceMeisters will be created in."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).dest_category_id.set(dest_category.id)
            perms_required, perms_optional, details = self.check_perms_source_dest(
                voicemeister_source, dest_category, detailed=True
            )
            message = f"**{voicemeister_source.mention}** will now create new VoiceMeisters in the **{dest_category.mention}** category."
            if perms_required and perms_optional:
                await ctx.send(success(message))
            else:
                await ctx.send(
                    warning(
                        f"{message}"
                        "\n"
                        "Do note, this new category does not have sufficient permissions for me to make VoiceMeisters. "
                        "Until you fix this, the VoiceMeister Source will not work."
                        "\n"
                        f"{details}"
                    )
                )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify.group(name="type")
    async def modify_type(self, ctx: commands.Context) -> None:
        """Choose what type of VoiceMeister is created."""

    @modify_type.command(name="public")
    async def modify_type_public(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """Rooms will be open to all. VoiceMeister Owner has control over room."""
        await self._save_public_private(ctx, voicemeister_source, "public")

    @modify_type.command(name="locked")
    async def modify_type_locked(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """Rooms will be visible to all, but not joinable. VoiceMeister Owner can allow users in."""
        await self._save_public_private(ctx, voicemeister_source, "locked")

    @modify_type.command(name="private")
    async def modify_type_private(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """Rooms will be hidden. VoiceMeister Owner can allow users in."""
        await self._save_public_private(ctx, voicemeister_source, "private")

    @modify_type.command(name="server")
    async def modify_type_server(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """Rooms will be open to all, but the server owns the VoiceMeister (so they can't be modified)."""
        await self._save_public_private(ctx, voicemeister_source, "server")

    async def _save_public_private(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
        room_type: str,
    ) -> None:
        """Save the public/private setting."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).room_type.set(room_type)
            await ctx.send(
                success(
                    f"**{voicemeister_source.mention}** will now create `{room_type}` VoiceMeisters."
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify.group(name="name")
    async def modify_name(self, ctx: commands.Context) -> None:
        """Set the default name format of an VoiceMeister."""

    @modify_name.command(name="username")
    async def modify_name_username(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """Default format: PhasecoreX's Room.

        Custom format example:
        `{{username}}'s Room{% if dupenum > 1 %} ({{dupenum}}){% endif %}`
        """  # noqa: D401
        await self._save_room_name(ctx, voicemeister_source, "username")

    @modify_name.command(name="game")
    async def modify_name_game(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """The users current playing game, otherwise the username format.

        Custom format example:
        `{{game}}{% if not game %}{{username}}'s Room{% endif %}{% if dupenum > 1 %} ({{dupenum}}){% endif %}`
        """  # noqa: D401
        await self._save_room_name(ctx, voicemeister_source, "game")

    @modify_name.command(name="custom")
    async def modify_name_custom(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
        *,
        template: str,
    ) -> None:
        """A custom channel name.

        Use `{{ expressions }}` to print variables and `{% statements %}` to do basic evaluations on variables.

        Variables supported:
        - `username` - VoiceMeister Owner's username
        - `game    ` - VoiceMeister Owner's game
        - `dupenum ` - An incrementing number that starts at 1, useful for un-duplicating channel names

        Statements supported:
        - `if/elif/else/endif`
        - Example: `{% if dupenum > 1 %}DupeNum is {{dupenum}}, which is greater than 1{% endif %}`
        - Another example: `{% if not game %}User isn't playing a game!{% endif %}`

        It's kinda like Jinja2, but way simpler. Check out [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/voicemeister/README.md) for more info.
        """  # noqa: D401
        await self._save_room_name(ctx, voicemeister_source, "custom", template)

    async def _save_room_name(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
        room_type: str,
        template: str | None = None,
    ) -> None:
        """Save the room name type."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            data = self.get_template_data(ctx.author)
            if template:
                template = template.replace("\n", " ")
                try:
                    # Validate template
                    self.format_template_room_name(template, data)
                except RuntimeError as rte:
                    await ctx.send(
                        error(
                            "Hmm... that doesn't seem to be a valid template:"
                            "\n\n"
                            f"`{rte!s}`"
                            "\n\n"
                            "If you need some help, take a look at "
                            "[the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/voicemeister/README.md)."
                        )
                    )
                    return
                await self.config.custom(
                    "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
                ).channel_name_format.set(template)
            else:
                await self.config.custom(
                    "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
                ).channel_name_format.clear()
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).channel_name_type.set(room_type)
            message = (
                f"New VoiceMeisters created by **{voicemeister_source.mention}** "
                f"will use the **{room_type.capitalize()}** format"
            )
            if template:
                message += f":\n`{template}`"
            else:
                # Load preset template for display purposes
                template = channel_name_template[room_type]
                message += "."
            if "game" not in data:
                data["game"] = "Example Game"
            message += "\n\nExample room names:"
            for room_num in range(1, 4):
                message += (
                    f"\n{self.format_template_room_name(template, data, room_num)}"
                )
            await ctx.send(success(message))
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify.group(name="text")
    async def modify_text(
        self,
        ctx: commands.Context,
    ) -> None:
        """Configure sending an introductory message to the VoiceMeister text channel."""

    @modify_text.command(name="set")
    async def modify_text_set(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
        *,
        hint_text: str,
    ) -> None:
        """Send a message to the newly generated VoiceMeister text channel.

        This can have template variables and statements, which you can learn more
        about by looking at `[p]voicemeisterset modify name custom`, or by looking at
        [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/voicemeister/README.md).

        The only additional variable that may be useful here is the `mention` variable,
        which will insert the users mention (pinging them).

        - Example:
        `Hello {{mention}}! Welcome to your new VoiceMeister!`
        """
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            data = self.get_template_data(ctx.author)
            try:
                # Validate template
                hint_text_formatted = self.template.render(hint_text, data)
            except RuntimeError as rte:
                await ctx.send(
                    error(
                        "Hmm... that doesn't seem to be a valid template:"
                        "\n\n"
                        f"`{rte!s}`"
                        "\n\n"
                        "If you need some help, take a look at "
                        "[the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/voicemeister/README.md)."
                    )
                )
                return

            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).text_channel_hint.set(hint_text)

            await ctx.send(
                success(
                    f"New VoiceMeisters created by **{voicemeister_source.mention}** will have the following message sent in them:"
                    "\n\n"
                    f"{hint_text_formatted}"
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify_text.command(name="disable")
    async def modify_text_disable(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
    ) -> None:
        """Disable sending a message to the newly generated VoiceMeister text channel."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).text_channel_hint.clear()
            await ctx.send(
                success(
                    f"New VoiceMeisters created by **{voicemeister_source.mention}** will no longer have a message sent in them."
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify.group(name="specialperms")
    async def special_perms(self, ctx: commands.Context) -> None:
        """Modify special VoiceMeister permissions.

        Remember, most permissions are automatically copied
        from the AuthRoom Source over to the VoiceMeister.
        These are for configuring special cases.
        """

    @special_perms.command(name="ownermodify")
    async def owner_manage_channels(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """Allow VoiceMeister Owners to have the Manage Channels permission on their VoiceMeister."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            new_config_value = not await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).perm_owner_manage_channels()
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).perm_owner_manage_channels.set(new_config_value)
            await ctx.send(
                success(
                    f"VoiceMeister Owners are {'now' if new_config_value else 'no longer'} able to modify their VoiceMeister with native Discord controls."
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @special_perms.command(name="sendmessage")
    async def public_send_messages(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """Allow users to send messages in the VoiceMeister built in text channel."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            new_config_value = not await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).perm_send_messages()
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).perm_send_messages.set(new_config_value)
            await ctx.send(
                success(
                    f"Users are {'now' if new_config_value else 'no longer'} able to send messages in the VoiceMeister built in text channel."
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify.group(name="legacytextchannel")
    async def modify_legacytext(
        self,
        ctx: commands.Context,
    ) -> None:
        """Manage if a legacy text channel should be created as well."""

    @modify_legacytext.command(name="enable")
    async def modify_legacytext_enable(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
    ) -> None:
        """Enable creating a legacy text channel with the VoiceMeister."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).legacy_text_channel.set(value=True)
            await ctx.send(
                success(
                    f"New VoiceMeisters created by **{voicemeister_source.mention}** will now get their own legacy text channel."
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify_legacytext.command(name="disable")
    async def modify_legacytext_disable(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
    ) -> None:
        """Disable creating a legacy text channel with the VoiceMeister."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).legacy_text_channel.clear()
            await ctx.send(
                success(
                    f"New VoiceMeisters created by **{voicemeister_source.mention}** will no longer get their own legacy text channel."
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify_legacytext.group(name="topic")
    async def modify_legacytext_topic(
        self,
        ctx: commands.Context,
    ) -> None:
        """Manage the legacy text channel topic."""

    @modify_legacytext_topic.command(name="set")
    async def modify_legacytext_topic_set(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
        *,
        topic_text: str,
    ) -> None:
        """Set the legacy text channel topic.

        - Example:
        `This channel is only visible to members of your voice channel, and admins of this server. It will be deleted when everyone leaves. `
        """
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            data = self.get_template_data(ctx.author)
            try:
                # Validate template
                topic_text_formatted = self.template.render(topic_text, data)
            except RuntimeError as rte:
                await ctx.send(
                    error(
                        "Hmm... that doesn't seem to be a valid template:"
                        "\n\n"
                        f"`{rte!s}`"
                        "\n\n"
                        "If you need some help, take a look at "
                        "[the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/voicemeister/README.md)."
                    )
                )
                return

            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).text_channel_topic.set(topic_text)

            await ctx.send(
                success(
                    f"New VoiceMeisters created by **{voicemeister_source.mention}** will have the following message topic set:"
                    "\n\n"
                    f"{topic_text_formatted}"
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify_legacytext_topic.command(name="disable")
    async def modify_legacytext_topic_disable(
        self,
        ctx: commands.Context,
        voicemeister_source: discord.VoiceChannel,
    ) -> None:
        """Disable setting a legacy text channel topic."""
        if not ctx.guild:
            return
        if await self.get_voicemeister_source_config(voicemeister_source):
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
            ).text_channel_topic.clear()
            await ctx.send(
                success(
                    f"New VoiceMeisters created by **{voicemeister_source.mention}** will no longer have a topic set."
                )
            )
        else:
            await ctx.send(
                error(
                    f"**{voicemeister_source.mention}** is not an VoiceMeister Source channel."
                )
            )

    @modify.command(
        name="defaults", aliases=["bitrate", "memberrole", "other", "perms", "users"]
    )
    async def modify_defaults(self, ctx: commands.Context) -> None:
        """Learn how VoiceMeister defaults are set."""
        await ctx.send(
            info(
                "**Bitrate/User Limit**"
                "\n"
                "Default bitrate and user limit settings are copied from the VoiceMeister Source to the resulting VoiceMeister."
                "\n\n"
                "**Member Roles**"
                "\n"
                "Only members that can view and join an VoiceMeister Source will be able to join its resulting VoiceMeisters. "
                "If you would like to limit VoiceMeisters to only allow certain members, simply deny the everyone role "
                "from viewing/connecting to the VoiceMeister Source and allow your member roles to view/connect to it."
                "\n\n"
                "**Permissions**"
                "\n"
                "All permission overwrites (except for Manage Roles) will be copied from the VoiceMeister Source "
                "to the resulting VoiceMeister. Every permission overwrite you want copied over, regardless if it is "
                "allowed or denied, must be allowed for the bot. It can either be allowed for the bot in the "
                "destination category or server-wide with the roles it has. `[p]voicemeisterset permissions` will "
                "show what permissions will be copied over."
            )
        )

    async def _check_all_perms(
        self, guild: discord.Guild, *, detailed: bool = False
    ) -> tuple[bool, bool, list[str]]:
        """Check all permissions for all VoiceMeisters in a guild."""
        result_required = True
        result_optional = True
        result_list = []
        avcs = await self.get_all_voicemeister_source_configs(guild)
        for avc_id, avc_settings in avcs.items():
            voicemeister_source = guild.get_channel(avc_id)
            category_dest = guild.get_channel(avc_settings["dest_category_id"])
            if isinstance(voicemeister_source, discord.VoiceChannel) and isinstance(
                category_dest, discord.CategoryChannel
            ):
                (
                    required_check,
                    optional_check,
                    detail,
                ) = self.check_perms_source_dest(
                    voicemeister_source,
                    category_dest,
                    with_manage_roles_guild=avc_settings["room_type"] != "server",
                    with_legacy_text_channel=avc_settings["legacy_text_channel"],
                    with_optional_clone_perms=True,
                    detailed=detailed,
                )
                result_required = result_required and required_check
                result_optional = result_optional and optional_check
                if detailed:
                    result_list.append(detail)
                elif not result_required and not result_optional:
                    break
        return result_required, result_optional, result_list

# View Class for Control Panel

class VoiceMeisterView(Buttons):
    def __init__(self, bot: Red, author: discord.Member, infinity: bool = True):
        buttons = [
            {"emoji": DEFAULT_EMOJIS["lock"], "custom_id": "lock", "row": 0},
            {"emoji": DEFAULT_EMOJIS["unlock"], "custom_id": "unlock", "row": 0},
            {"emoji": DEFAULT_EMOJIS["hide"], "custom_id": "hide", "row": 0},
            {"emoji": DEFAULT_EMOJIS["unhide"], "custom_id": "unhide", "row": 0},
            {"emoji": DEFAULT_EMOJIS["limit"], "custom_id": "limit", "row": 1},
            {"emoji": DEFAULT_EMOJIS["ban"], "custom_id": "ban", "row": 1},
            {"emoji": DEFAULT_EMOJIS["permit"], "custom_id": "permit", "row": 1},
            {"emoji": DEFAULT_EMOJIS["claim"], "custom_id": "claim", "row": 1},
            {"emoji": DEFAULT_EMOJIS["transfer"], "custom_id": "transfer", "row": 2},
            {"emoji": DEFAULT_EMOJIS["info"], "custom_id": "info", "row": 2},
            {"emoji": DEFAULT_EMOJIS["rename"], "custom_id": "rename", "row": 2},
            {"emoji": DEFAULT_EMOJIS["bitrate"], "custom_id": "bitrate", "row": 2},
            {"emoji": DEFAULT_EMOJIS["region"], "custom_id": "region", "row": 3},
            {"emoji": DEFAULT_EMOJIS["create_text"], "custom_id": "create_text", "row": 3},
            {"emoji": DEFAULT_EMOJIS["delete"], "custom_id": "delete", "row": 3},
            {"emoji": DEFAULT_EMOJIS["invite"], "custom_id": "invite", "row": 3},
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
                owners = await self.bot.get_cog("VoiceMeister").config.guild(voice_channel.guild).owners()
                owner_id = owners.get(str(voice_channel.id))
                if interaction.data["custom_id"] == "info" or interaction.user.id == owner_id:
                    await handler(interaction, voice_channel)
                else:
                    await interaction.response.send_message("You are not the owner of this channel.", ephemeral=True)

    async def handle_lock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        if channel.overwrites_for(interaction.guild.default_role).connect is False:
            await interaction.response.send_message("The channel is already locked.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister").locked(interaction, channel)

    async def handle_unlock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        if channel.overwrites_for(interaction.guild.default_role).connect is True:
            await interaction.response.send_message("The channel is already unlocked.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister").unlock(interaction, channel)

    async def handle_user_limit(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(SetUserLimitModal(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_hide(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        if channel.overwrites_for(interaction.guild.default_role).view_channel is False:
            await interaction.response.send_message("The channel is already hidden.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister")._process_allow_deny(interaction, "private", channel)

    async def handle_unhide(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        if channel.overwrites_for(interaction.guild.default_role).view_channel is True:
            await interaction.response.send_message("The channel is already visible.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister")._process_allow_deny(interaction, "public", channel)

    async def handle_invite(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        invite = await channel.create_invite(max_uses=1, unique=True)
        await interaction.response.send_message(content=f"Here is your invite to the voice channel: {invite.url}", ephemeral=True)

    async def handle_ban(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a member to ban.", view=DenyAllowSelect(self.bot.get_cog("VoiceMeister"), channel, action="deny"), ephemeral=True)

    async def handle_permit(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a member to permit.", view=DenyAllowSelect(self.bot.get_cog("VoiceMeister"), channel, action="allow"), ephemeral=True)

    async def handle_rename(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(ChangeNameModal(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_bitrate(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a bitrate.", view=BitrateSelectView(self.bot.get_cog("VoiceMeister"), channel), ephemeral=True)

    async def handle_region(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").change_region(interaction, channel)

    async def handle_claim(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        owners = await self.bot.get_cog("VoiceMeister").config.guild(channel.guild).owners()
        current_owner_id = owners.get(str(channel.id))
        if current_owner_id == interaction.user.id:
            await interaction.response.send_message("You already own this channel.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister").claim(interaction, channel)

    async def handle_transfer(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a member to transfer ownership to.", view=TransferOwnershipSelect(self.bot.get_cog("VoiceMeister"), channel), ephemeral=True)

    async def handle_info(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").info(interaction, channel)

    async def handle_delete(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").delete_channel(interaction, channel)

    async def handle_create_text(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").create_text_channel(interaction, channel)

# Select Menus

class DenyAllowSelect(Dropdown):
    def __init__(self, cog, channel, action):
        user_options = [{"label": member.display_name, "value": str(member.id)} for member in channel.members]
        super().__init__(
            placeholder="Select a member",
            options=user_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel, "action": action},
            infinity=True
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
            function_kwargs={"cog": cog, "channel": channel},
            infinity=True
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel):
        try:
            selected_user_id = int(options[0])
            new_owner = channel.guild.get_member(selected_user_id)

            if new_owner:
                await cog.transfer_ownership(interaction, channel, new_owner)
        except Exception as e:
            await cog.handle_error(interaction, e)

class BitrateSelectView(Dropdown):
    def __init__(self, cog, channel):
        bitrate_options = [{"label": f"{bitrate} kbps", "value": str(bitrate)} for bitrate in BITRATE_OPTIONS]
        super().__init__(
            placeholder="Select Bitrate",
            options=bitrate_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel},
            infinity=True
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel):
        try:
            selected_bitrate = int(options[0])
            await channel.edit(bitrate=selected_bitrate * 1000)
            await interaction.response.send_message(f"Bitrate changed to {selected_bitrate} kbps.", ephemeral=True)
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
            if not bitrate_value.isdigit() or int(bitrate_value) > max(BITRATE_OPTIONS):
                await interaction.followup.send(f"Invalid bitrate. Please enter a value between 8 and {max(BITRATE_OPTIONS)} kbps.", ephemeral=True)
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
            function_kwargs={"cog": cog, "channel": channel},
            infinity=True
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
