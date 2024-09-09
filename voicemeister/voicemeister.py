from contextlib import suppress
from typing import Any, ClassVar, Optional, Tuple, List
import discord
from redbot.core import Config, checks, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import humanize_timedelta, success, error, warning, info
from redbot.core.utils.predicates import MessagePredicate
from Star_Utils import Buttons, Dropdown, Cog, Settings
import datetime
import asyncio

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

    @commands.hybrid_command(name="interface", with_app_command=True)
    async def interface(self, ctx: commands.Context):
        """Open the voice interface."""
        view = VoiceMeisterView(bot=self.bot, author=ctx.author, infinity=True)
        embed = discord.Embed(
            title="Voice Interface",
            description=self._fancy_interface_description(),
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed, view=view, ephemeral=True)

    def _fancy_interface_description(self) -> str:
        """Generate a fancy interface description with boxes and emojis."""
        actions = [
            ("lock", "Lock"),
            ("unlock", "Unlock"),
            ("hide", "Unhide"),
            ("hide", "Hide"),
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
        description = ""
        for emoji, name in actions:
            description += f"**{DEFAULT_EMOJIS[emoji]} {name}**\n"
        return description

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        guild_data = await self.config.guild(member.guild).all()
        lobby_channel_id = guild_data["lobby_channel"]
        category_id = guild_data["category"]
        temp_channels = guild_data["temp_channels"]
        banned_roles = guild_data["banned_roles"]

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
        """Claim ownership of the AutoRoom if there is no current owner, or override if admin/owner."""
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
        source_required = check_permissions(source_channel, required_perms)
        dest_required = check_permissions(dest_category, required_perms)
        source_optional = check_permissions(source_channel, optional_perms)
        dest_optional = check_permissions(dest_category, optional_perms)

        # Determine if all required and optional permissions are met
        required_check = source_required and dest_required
        optional_check = source_optional and dest_optional

        # Generate a detailed report if needed
        details = ""
        if detailed:
            missing_required = [perm for perm, value in required_perms.items() if not value]
            missing_optional = [perm for perm, value in optional_perms.items() if not value]
            details = (
                f"Missing required permissions: {', '.join(missing_required)}\n"
                f"Missing optional permissions: {', '.join(missing_optional)}"
            )

        return required_check, optional_check, details

    @commands.group(aliases=["vmset"])
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def voicemeisterset(self, ctx: commands.Context) -> None:
        """Configure the VoiceMeister cog."""

    @voicemeisterset.command()
    async def settings(self, ctx: commands.Context) -> None:
        """Display current settings."""
        await self.settings.show_settings(ctx)

    @voicemeisterset.command(aliases=["enable", "add"])
    async def create(
        self,
        ctx: commands.Context,
        source_voice_channel: discord.VoiceChannel,
        dest_category: discord.CategoryChannel,
    ) -> None:
        """Create a VoiceMeister Source.

        Anyone joining a VoiceMeister Source will automatically have a new
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
            "**Welcome to the setup wizard for creating a VoiceMeister Source!**"
            "\n"
            f"Users joining the {source_voice_channel.mention} VoiceMeister Source will have a VoiceMeister "
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
            "When a VoiceMeister is created, a name will be generated for it. How would you like that name to be generated?"
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
        """Remove a VoiceMeister Source."""
        if not ctx.guild:
            return
        await self.config.custom(
            "VOICEMEISTER_SOURCE", str(ctx.guild.id), str(voicemeister_source.id)
        ).clear()
        await ctx.send(
            success(
                f"**{voicemeister_source.mention}** is no longer a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
                )
            )

    @modify.group(name="name")
    async def modify_name(self, ctx: commands.Context) -> None:
        """Set the default name format of a VoiceMeister."""

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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                    f"**{voicemeister_source.mention}** is not a VoiceMeister Source channel."
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
                "Only members that can view and join a VoiceMeister Source will be able to join its resulting VoiceMeisters. "
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
    ) -> Tuple[bool, bool, List[str]]:
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

class BitrateSelectView(Dropdown):
    def __init__(self, cog, channel):
        bitrate_options = [{"label": f"{bitrate} kbps", "value": str(bitrate)} for bitrate in BITRATE_OPTIONS]
        super().__init__(
            placeholder="Select Bitrate",
            options=bitrate_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel}
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
