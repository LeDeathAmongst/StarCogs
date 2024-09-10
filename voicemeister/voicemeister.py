from contextlib import suppress
from typing import Any, Optional, Tuple, List, ClassVar
import discord
from redbot.core import Config, checks, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import success, error, warning, info
from redbot.core.utils.predicates import MessagePredicate
from Star_Utils import Buttons, Dropdown, Cog, Settings
from .star_template import Template
from .star_lib import Perms, SettingDisplay, delete
from .abc import ABC
import datetime
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests

MAX_CHANNEL_NAME_LENGTH = 100
BITRATE_OPTIONS = [8, 16, 24, 32, 48, 56, 64, 72, 80, 88, 96]  # Bitrate options in kbps

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

class CompositeMetaClass(type(commands.Cog), type(ABC)):
    """Allows the metaclass used for proper type detection to coexist with discord.py's metaclass."""

class VoiceMeister(Cog, metaclass=CompositeMetaClass):
    """Advanced voice channel control with join-to-create and more."""

    default_global_settings: ClassVar[dict[str, int]] = {"schema_version": 0}
    default_guild_settings: ClassVar[dict[str, bool | list[int]]] = {
        "admin_access": True,
        "mod_access": False,
        "bot_access": [],
    }
    default_voicemeister_source_settings: ClassVar[dict[str, int | str | None]] = {
        "dest_category_id": None,
        "room_type": "public",
        "legacy_text_channel": False,
        "text_channel_hint": None,
        "text_channel_topic": "",
        "channel_name_type": "username",
        "channel_name_format": "",
        "perm_owner_manage_channels": True,
        "perm_send_messages": True,
    }
    default_channel_settings: ClassVar[dict[str, int | list[int] | None]] = {
        "source_channel": None,
        "owner": None,
        "associated_text_channel": None,
        "denied": [],
    }
    extra_channel_name_change_delay = 4

    perms_bot_source: ClassVar[dict[str, bool]] = {
        "view_channel": True,
        "connect": True,
        "move_members": True,
    }
    perms_bot_dest: ClassVar[dict[str, bool]] = {
        "view_channel": True,
        "connect": True,
        "send_messages": True,
        "manage_channels": True,
        "manage_messages": True,
        "move_members": True,
    }

    perms_legacy_text: ClassVar[list[str]] = ["read_message_history", "read_messages"]
    perms_legacy_text_allow: ClassVar[dict[str, bool]] = dict.fromkeys(
        perms_legacy_text, True
    )
    perms_legacy_text_deny: ClassVar[dict[str, bool]] = dict.fromkeys(
        perms_legacy_text, False
    )
    perms_legacy_text_reset: ClassVar[dict[str, None]] = dict.fromkeys(
        perms_legacy_text, None
    )
    perms_voicemeister_owner_legacy_text: ClassVar[dict[str, bool]] = {
        **perms_legacy_text_allow,
        "manage_channels": True,
        "manage_messages": True,
    }
    perms_bot_dest_legacy_text = perms_voicemeister_owner_legacy_text

    def __init__(self, bot: Red):
        """Set up the cog."""
        super().__init__()
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(**self.default_global_settings)
        self.config.register_guild(**self.default_guild_settings)
        self.config.init_custom("VOICEMEISTER_SOURCE", 2)
        self.config.register_custom("VOICEMEISTER_SOURCE", **self.default_voicemeister_source_settings)
        self.config.register_channel(**self.default_channel_settings)

        self.settings = Settings(
            bot=bot,
            cog=self,
            config=self.config,
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
            }
        )

        # Define the image path
        self.image_path = "interface.png"

        self.template = Template()
        self.bucket_voicemeister_create = commands.CooldownMapping.from_cooldown(
            2, 60, lambda member: member
        )
        self.bucket_voicemeister_create_warn = commands.CooldownMapping.from_cooldown(
            1, 3600, lambda member: member
        )
        self.bucket_voicemeister_name = commands.CooldownMapping.from_cooldown(
            2, 600 + self.extra_channel_name_change_delay, lambda channel: channel
        )
        self.bucket_voicemeister_owner_claim = commands.CooldownMapping.from_cooldown(
            1, 120, lambda channel: channel
        )

    @commands.hybrid_command(name="interface", with_app_command=True)
    async def interface(self, ctx: commands.Context):
        """Open the voice interface."""
        # Check if the image file already exists
        if not os.path.exists(self.image_path):
            await self._generate_interface_image(ctx)

        file = discord.File(fp=self.image_path, filename="interface.png")
        view = VoiceMeisterView(bot=self.bot, author=ctx.author, infinity=True)
        embed = discord.Embed(
            title="Voice Interface",
            description="Use these buttons to control your private voice!",
            color=discord.Color.blue()
        )
        embed.set_image(url="attachment://interface.png")
        await ctx.send(embed=embed, file=file, view=view)

    async def _generate_interface_image(self, ctx: commands.Context):
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
            ("create_text", "WIP"),  # Changed from "Chat" to "WIP"
            ("delete", "Delete"),
            ("invite", "Invite")
        ]

        # Calculate dimensions
        num_columns = 4
        num_rows = (len(actions) + num_columns - 1) // num_columns
        box_width = 100
        box_height = 30
        padding = 7
        total_width = box_width * num_columns + padding * (num_columns - 1)
        total_height = box_height * num_rows + padding * (num_rows - 1)

        # Use the bot's color for the box background
        bot_color = ctx.me.color.to_rgb()

        # Create the image with a transparent background
        image = Image.new("RGBA", (total_width, total_height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Use a default font provided by Pillow
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)
        except IOError:
            font = ImageFont.load_default()

        def draw_rounded_rectangle(draw, xy, radius, fill, outline=None, width=1):
            """Draw a rounded rectangle."""
            x1, y1, x2, y2 = xy
            draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
            draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
            draw.pieslice([x1, y1, x1 + 2 * radius, y1 + 2 * radius], 180, 270, fill=fill)
            draw.pieslice([x2 - 2 * radius, y1, x2, y1 + 2 * radius], 270, 360, fill=fill)
            draw.pieslice([x1, y2 - 2 * radius, x1 + 2 * radius, y2], 90, 180, fill=fill)
            draw.pieslice([x2 - 2 * radius, y2 - 2 * radius, x2, y2], 0, 90, fill=fill)
            if outline:
                draw.arc([x1, y1, x1 + 2 * radius, y1 + 2 * radius], 180, 270, fill=outline, width=width)
                draw.arc([x2 - 2 * radius, y1, x2, y1 + 2 * radius], 270, 360, fill=outline, width=width)
                draw.arc([x1, y2 - 2 * radius, x1 + 2 * radius, y2], 90, 180, fill=outline, width=width)
                draw.arc([x2 - 2 * radius, y2 - 2 * radius, x2, y2], 0, 90, fill=outline, width=width)
                draw.line([x1 + radius, y1, x2 - radius, y1], fill=outline, width=width)
                draw.line([x1 + radius, y2, x2 - radius, y2], fill=outline, width=width)
                draw.line([x1, y1 + radius, x1, y2 - radius], fill=outline, width=width)
                draw.line([x2, y1 + radius, x2, y2 - radius], fill=outline, width=width)

        # Draw the boxes, emojis, and names
        for i, (emoji_name, name) in enumerate(actions):
            x = (i % num_columns) * (box_width + padding)
            y = (i // num_columns) * (box_height + padding)

            # Draw rounded rectangle with bot's color fill
            draw_rounded_rectangle(draw, [x, y, x + box_width, y + box_height], radius=10, fill=bot_color, outline=bot_color, width=2)

            # Fetch emoji image
            emoji_id = DEFAULT_EMOJIS[emoji_name].split(":")[2].strip(">")
            emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.png"
            response = requests.get(emoji_url)
            emoji_image = Image.open(BytesIO(response.content)).resize((20, 20))
            image.paste(emoji_image, (x + 5, y + (box_height - 20) // 2), emoji_image)

            # Draw the name next to the emoji
            text_bbox = font.getbbox(name)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            draw.text(
                (x + 30, y + (box_height - text_height) / 2),
                name,
                fill=(255, 255, 255),  # White text
                font=font
            )

        # Save the image to a file
        image.save(self.image_path, format="PNG")

    async def red_delete_data_for_user(self, *, _requester: str, _user_id: int) -> None:
        """Nothing to delete."""
        return

    async def initialize(self) -> None:
        """Perform setup actions before loading cog."""
        await self._migrate_config()
        self.bot.loop.create_task(self._cleanup_voicemeisters())

    async def _migrate_config(self) -> None:
        """Perform some configuration migrations."""
        schema_version = await self.config.schema_version()

        if schema_version < 1:
            # Migrate private -> room_type
            guild_dict = await self.config.all_guilds()
            for guild_id in guild_dict:
                avcs = await self.config.guild_from_id(guild_id).get_raw(
                    "auto_voice_channels", default={}
                )
                if avcs:
                    for avc_settings in avcs.values():
                        if "private" in avc_settings:
                            avc_settings["room_type"] = (
                                "private" if avc_settings["private"] else "public"
                            )
                            del avc_settings["private"]
                    await self.config.guild_from_id(guild_id).set_raw(
                        "auto_voice_channels", value=avcs
                    )
            await self.config.schema_version.set(1)

        if schema_version < 2:  # noqa: PLR2004
            # Migrate member_role -> per auto_voice_channel member_roles
            guild_dict = await self.config.all_guilds()
            for guild_id in guild_dict:
                await self.config.guild_from_id(guild_id).clear_raw("member_role")
            await self.config.schema_version.set(2)

        if schema_version < 4:  # noqa: PLR2004
            # Migrate to VOICEMEISTER_SOURCE custom config group
            guild_dict = await self.config.all_guilds()
            for guild_id in guild_dict:
                avcs = await self.config.guild_from_id(guild_id).get_raw(
                    "auto_voice_channels", default={}
                )
                for avc_id, avc_settings in avcs.items():
                    new_dict = {
                        "dest_category_id": avc_settings["dest_category_id"],
                        "room_type": avc_settings["room_type"],
                    }
                    # The rest of these were optional
                    if "channel_name_type" in avc_settings:
                        new_dict["channel_name_type"] = avc_settings[
                            "channel_name_type"
                        ]
                    await self.config.custom("VOICEMEISTER_SOURCE", guild_id, avc_id).set(
                        new_dict
                    )
                await self.config.guild_from_id(guild_id).clear_raw(
                    "auto_voice_channels"
                )
            await self.config.schema_version.set(4)

        if schema_version < 5:  # noqa: PLR2004
            # Upgrade room templates
            all_voicemeister_sources = await self.config.custom("VOICEMEISTER_SOURCE").all()
            for guild_id, guild_voicemeister_sources in all_voicemeister_sources.items():
                for (
                    avc_id,
                    voicemeister_source_config,
                ) in guild_voicemeister_sources.items():
                    if voicemeister_source_config.get("channel_name_format"):
                        # Change username and game template variables
                        new_template = (
                            voicemeister_source_config["channel_name_format"]
                            .replace("{username}", "{{username}}")
                            .replace("{game}", "{{game}}")
                        )
                        if voicemeister_source_config.get("increment_always"):
                            if "increment_format" in voicemeister_source_config:
                                # Always show number, custom format
                                new_template += voicemeister_source_config[
                                    "increment_format"
                                ].replace("{number}", "{{dupenum}}")
                            else:
                                # Always show number, default format
                                new_template += " ({{dupenum}})"
                        elif "increment_format" in voicemeister_source_config:
                            # Show numbers > 1, custom format
                            new_template += (
                                "{% if dupenum > 1 %}"
                                + voicemeister_source_config["increment_format"].replace(
                                    "{number}", "{{dupenum}}"
                                )
                                + "{% endif %}"
                            )
                        else:
                            # Show numbers > 1, default format
                            new_template += (
                                "{% if dupenum > 1 %} ({{dupenum}}){% endif %}"
                            )
                        await self.config.custom(
                            "VOICEMEISTER_SOURCE", guild_id, avc_id
                        ).channel_name_format.set(new_template)
                        await self.config.custom(
                            "VOICEMEISTER_SOURCE", guild_id, avc_id
                        ).clear_raw("increment_always")
                        await self.config.custom(
                            "VOICEMEISTER_SOURCE", guild_id, avc_id
                        ).clear_raw("increment_format")
            await self.config.schema_version.set(5)

        if schema_version < 6:  # noqa: PLR2004
            # Remove member roles
            all_voicemeister_sources = await self.config.custom("VOICEMEISTER_SOURCE").all()
            for guild_id, guild_voicemeister_sources in all_voicemeister_sources.items():
                for avc_id in guild_voicemeister_sources:
                    await self.config.custom(
                        "VOICEMEISTER_SOURCE", guild_id, avc_id
                    ).clear_raw("member_roles")
            await self.config.schema_version.set(6)

        if schema_version < 7:  # noqa: PLR2004
            # Remove auto text channels
            guild_dict = await self.config.all_guilds()
            for guild_id in guild_dict:
                await self.config.guild_from_id(guild_id).clear_raw("admin_access_text")
                await self.config.guild_from_id(guild_id).clear_raw("mod_access_text")
            all_voicemeister_sources = await self.config.custom("VOICEMEISTER_SOURCE").all()
            for guild_id, guild_voicemeister_sources in all_voicemeister_sources.items():
                for avc_id in guild_voicemeister_sources:
                    await self.config.custom(
                        "VOICEMEISTER_SOURCE", guild_id, avc_id
                    ).clear_raw("text_channel")
            await self.config.schema_version.set(7)

    async def _cleanup_voicemeisters(self) -> None:
        """Remove non-existent VoiceMeisters from the config."""
        await self.bot.wait_until_ready()
        voice_channel_dict = await self.config.all_channels()
        for voice_channel_id, voice_channel_settings in voice_channel_dict.items():
            voice_channel = self.bot.get_channel(voice_channel_id)
            if voice_channel:
                if isinstance(voice_channel, discord.VoiceChannel):
                    # Delete VoiceMeister if it is empty
                    await self._process_voicemeister_delete(voice_channel)
            else:
                # VoiceMeister has already been deleted, clean up legacy text channel if it still exists
                legacy_text_channel = await self.get_voicemeister_legacy_text_channel(
                    voice_channel_settings["associated_text_channel"]
                )
                if legacy_text_channel:
                    await legacy_text_channel.delete(
                        reason="VoiceMeister: Associated voice channel deleted."
                    )
                await self.config.channel_from_id(voice_channel_id).clear()

    @commands.Cog.listener()
    async def on_guild_channel_delete(
        self, guild_channel: discord.abc.GuildChannel
    ) -> None:
        """Clean up config when a VoiceMeister (or Source) is deleted (either by the bot or the user)."""
        if not isinstance(guild_channel, discord.VoiceChannel):
            return
        if await self.get_voicemeister_source_config(guild_channel):
            # VoiceMeister Source was deleted, remove configuration
            await self.config.custom(
                "VOICEMEISTER_SOURCE", str(guild_channel.guild.id), str(guild_channel.id)
            ).clear()
        else:
            # VoiceMeister was deleted, remove associated text channel if it exists
            legacy_text_channel = await self.get_voicemeister_legacy_text_channel(
                guild_channel
            )
            if legacy_text_channel:
                await legacy_text_channel.delete(
                    reason="VoiceMeister: Associated voice channel deleted."
                )
            await self.config.channel(guild_channel).clear()

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member: discord.Member,
        leaving: discord.VoiceState,
        joining: discord.VoiceState,
    ) -> None:
        """Do voice channel stuff when users move about channels."""
        if await self.bot.cog_disabled_in_guild(self, member.guild):
            return

        # If user left a VoiceMeister, do cleanup
        if isinstance(leaving.channel, discord.VoiceChannel):
            voicemeister_info = await self.get_voicemeister_info(leaving.channel)
            if voicemeister_info:
                deleted = await self._process_voicemeister_delete(leaving.channel)
                if not deleted:
                    # VoiceMeister wasn't deleted, so update text channel perms
                    await self._process_voicemeister_legacy_text_perms(leaving.channel)

                    if member.id == voicemeister_info["owner"]:
                        # There are still users left and the VoiceMeister Owner left.
                        # Start a countdown so that others can claim the VoiceMeister.
                        bucket = self.bucket_voicemeister_owner_claim.get_bucket(
                            leaving.channel
                        )
                        if bucket:
                            bucket.reset()
                            bucket.update_rate_limit()

        if isinstance(joining.channel, discord.VoiceChannel):
            # If user entered a VoiceMeister Source channel, create new VoiceMeister
            asc = await self.get_voicemeister_source_config(joining.channel)
            if asc:
                await self._process_voicemeister_create(joining.channel, asc, member)
            # If user entered a VoiceMeister, allow them into the associated text channel
            if await self.get_voicemeister_info(joining.channel):
                await self._process_voicemeister_legacy_text_perms(joining.channel)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        """Check joining users against existing VoiceMeisters, re-adds their deny override if missing."""
        for voicemeister_channel in member.guild.voice_channels:
            voicemeister_info = await self.get_voicemeister_info(voicemeister_channel)
            if voicemeister_info and member.id in voicemeister_info["denied"]:
                source_channel = member.guild.get_channel(
                    voicemeister_info["source_channel"]
                )
                asc = await self.get_voicemeister_source_config(source_channel)
                if not asc:
                    continue
                perms = Perms(voicemeister_channel.overwrites)
                perms.update(member, asc["perms"]["deny"])
                if perms.modified:
                    await voicemeister_channel.edit(
                        overwrites=perms.overwrites if perms.overwrites else {},
                        reason="VoiceMeister: Rejoining user, prevent deny evasion",
                    )

    async def _process_voicemeister_create(
        self,
        voicemeister_source: discord.VoiceChannel,
        voicemeister_source_config: dict[str, Any],
        member: discord.Member,
    ) -> None:
        """Create a voice channel for a member in a VoiceMeister Source channel."""
        # Check perms for guild, source, and dest
        guild = voicemeister_source.guild
        dest_category = guild.get_channel(voicemeister_source_config["dest_category_id"])
        if not isinstance(dest_category, discord.CategoryChannel):
            return
        required_check, optional_check, _ = self.check_perms_source_dest(
            voicemeister_source, dest_category
        )
        if not required_check or not optional_check:
            return

        # Check that user isn't spamming
        bucket = self.bucket_voicemeister_create.get_bucket(member)
        if bucket:
            retry_after = bucket.update_rate_limit()
            if retry_after:
                warn_bucket = self.bucket_voicemeister_create_warn.get_bucket(member)
                if warn_bucket:
                    if not warn_bucket.update_rate_limit():
                        with suppress(
                            discord.Forbidden,
                            discord.NotFound,
                            discord.HTTPException,
                        ):
                            await member.send(
                                "Hello there! It looks like you're trying to make a VoiceMeister."
                                "\n"
                                f"Please note that you are only allowed to make **{bucket.rate}** VoiceMeisters "
                                f"every **{humanize_timedelta(seconds=bucket.per)}**."
                                "\n"
                                f"You can try again in **{humanize_timedelta(seconds=max(retry_after, 1))}**."
                            )
                    return

        # Generate channel name
        taken_channel_names = [
            voice_channel.name for voice_channel in dest_category.voice_channels
        ]
        new_channel_name = self._generate_channel_name(
            voicemeister_source_config, member, taken_channel_names
        )

        # Generate overwrites
        perms = Perms()
        dest_perms = dest_category.permissions_for(dest_category.guild.me)
        source_overwrites = (
            voicemeister_source.overwrites if voicemeister_source.overwrites else {}
        )
        member_roles = self.get_member_roles(voicemeister_source)
        for target, permissions in source_overwrites.items():
            # We can't put manage_roles in overwrites, so just get rid of it
            permissions.update(manage_roles=None)
            # Check each permission for each overwrite target to make sure the bot has it allowed in the dest category
            failed_checks = {}
            for name, value in permissions:
                if value is not None:
                    permission_check_result = getattr(dest_perms, name)
                    if not permission_check_result:
                        # If the bot doesn't have the permission allowed in the dest category, just ignore it. Too bad!
                        failed_checks[name] = None
            if failed_checks:
                permissions.update(**failed_checks)
            perms.overwrite(target, permissions)
            if member_roles and target in member_roles:
                # If we have member roles and this target is one, apply VoiceMeister type permissions
                perms.update(target, voicemeister_source_config["perms"]["access"])

        # Update overwrites for default role to account for VoiceMeister type
        if member_roles:
            perms.update(guild.default_role, voicemeister_source_config["perms"]["deny"])
        else:
            perms.update(guild.default_role, voicemeister_source_config["perms"]["access"])

        # Bot overwrites
        perms.update(guild.me, self.perms_bot_dest)

        # VoiceMeister Owner overwrites
        if voicemeister_source_config["room_type"] != "server":
            perms.update(member, voicemeister_source_config["perms"]["owner"])

        # Admin/moderator/bot overwrites
        # Add bot roles to be allowed
        additional_allowed_roles = await self.get_bot_roles(guild)
        if await self.config.guild(guild).mod_access():
            # Add mod roles to be allowed
            additional_allowed_roles += await self.bot.get_mod_roles(guild)
        if await self.config.guild(guild).admin_access():
            # Add admin roles to be allowed
            additional_allowed_roles += await self.bot.get_admin_roles(guild)
        for role in additional_allowed_roles:
            # Add all the mod/admin roles, if required
            perms.update(role, voicemeister_source_config["perms"]["allow"])

        # Create new VoiceMeister
        new_voice_channel = await guild.create_voice_channel(
            name=new_channel_name,
            category=dest_category,
            reason="VoiceMeister: New VoiceMeister needed.",
            overwrites=perms.overwrites if perms.overwrites else {},
            bitrate=min(voicemeister_source.bitrate, int(guild.bitrate_limit)),
            user_limit=voicemeister_source.user_limit,
        )
        await self.config.channel(new_voice_channel).source_channel.set(
            voicemeister_source.id
        )
        if voicemeister_source_config["room_type"] != "server":
            await self.config.channel(new_voice_channel).owner.set(member.id)
        try:
            await member.move_to(
                new_voice_channel, reason="VoiceMeister: Move user to new VoiceMeister."
            )
        except discord.HTTPException:
            await self._process_voicemeister_delete(new_voice_channel)
            return

        # Create optional legacy text channel
        new_legacy_text_channel = None
        if voicemeister_source_config["legacy_text_channel"]:
            # Sanity check on required permissions
            for perm_name in self.perms_bot_dest_legacy_text:
                if not getattr(dest_perms, perm_name):
                    return
            # Generate overwrites
            perms = Perms()
            perms.update(guild.me, self.perms_bot_dest_legacy_text)
            perms.update(guild.default_role, self.perms_legacy_text_deny)
            if voicemeister_source_config["room_type"] != "server":
                perms.update(member, self.perms_voicemeister_owner_legacy_text)
            else:
                perms.update(member, self.perms_legacy_text_allow)
            # Admin/moderator overwrites
            additional_allowed_roles_text = []
            if await self.config.guild(guild).mod_access():
                # Add mod roles to be allowed
                additional_allowed_roles_text += await self.bot.get_mod_roles(guild)
            if await self.config.guild(guild).admin_access():
                # Add admin roles to be allowed
                additional_allowed_roles_text += await self.bot.get_admin_roles(guild)
            for role in additional_allowed_roles_text:
                # Add all the mod/admin roles, if required
                perms.update(role, self.perms_legacy_text_allow)
            # Create text channel
            text_channel_topic = self.template.render(
                voicemeister_source_config["text_channel_topic"],
                self.get_template_data(member),
            )
            new_legacy_text_channel = await guild.create_text_channel(
                name=new_channel_name.replace("'s ", " "),
                category=dest_category,
                topic=text_channel_topic,
                reason="VoiceMeister: New legacy text channel needed.",
                overwrites=perms.overwrites if perms.overwrites else {},
            )

            await self.config.channel(new_voice_channel).associated_text_channel.set(
                new_legacy_text_channel.id
            )

        # Send text chat hint if enabled
        if voicemeister_source_config["text_channel_hint"]:
            with suppress(RuntimeError):
                hint = self.template.render(
                    voicemeister_source_config["text_channel_hint"],
                    self.get_template_data(member),
                )
                if hint:
                    if new_legacy_text_channel:
                        await new_legacy_text_channel.send(hint)
                    else:
                        await new_voice_channel.send(hint)

    @staticmethod
    async def _process_voicemeister_delete(voice_channel: discord.VoiceChannel) -> bool:
        """Delete VoiceMeister if empty."""
        if (
            not voice_channel.members
            and voice_channel.permissions_for(voice_channel.guild.me).manage_channels
        ):
            with suppress(
                discord.NotFound
            ):  # Sometimes this happens when the user manually deletes their channel
                await voice_channel.delete(reason="VoiceMeister: Channel empty.")
                return True
        return False

    async def _process_voicemeister_legacy_text_perms(
        self, voicemeister: discord.VoiceChannel
    ) -> None:
        """Allow or deny a user access to the legacy text channel associated to a VoiceMeister."""
        legacy_text_channel = await self.get_voicemeister_legacy_text_channel(voicemeister)
        if not legacy_text_channel:
            return

        overwrites = dict(legacy_text_channel.overwrites)
        perms = Perms(overwrites)
        # Remove read perms for users not in voicemeister
        for member in overwrites:
            if (
                isinstance(member, discord.Member)
                and member not in voicemeister.members
                and member != voicemeister.guild.me
            ):
                perms.update(member, self.perms_legacy_text_reset)
        # Add read perms for users in voicemeister
        for member in voicemeister.members:
            perms.update(member, self.perms_legacy_text_allow)
        # Edit channel if overwrites were modified
        if perms.modified:
            await legacy_text_channel.edit(
                overwrites=perms.overwrites if perms.overwrites else {},
                reason="VoiceMeister: Legacy text channel permission update",
            )

    def _generate_channel_name(
        self,
        voicemeister_source_config: dict,
        member: discord.Member,
        taken_channel_names: list,
    ) -> str:
        """Return a channel name with an incrementing number appended to it, based on a formatting string."""
        template = None
        if voicemeister_source_config["channel_name_type"] in channel_name_template:
            template = channel_name_template[
                voicemeister_source_config["channel_name_type"]
            ]
        elif voicemeister_source_config["channel_name_type"] == "custom":
            template = voicemeister_source_config["channel_name_format"]
        template = template or channel_name_template["username"]

        data = self.get_template_data(member)
        new_channel_name = None
        attempt = 1
        with suppress(RuntimeError):
            new_channel_name = self.format_template_room_name(template, data, attempt)

        if not new_channel_name:
            # Either the user screwed with the template, or the template returned nothing. Use a default one instead.
            template = channel_name_template["username"]
            new_channel_name = self.format_template_room_name(template, data, attempt)

        # Check for duplicate names
        attempted_channel_names = []
        while (
            new_channel_name in taken_channel_names
            and new_channel_name not in attempted_channel_names
        ):
            attempt += 1
            attempted_channel_names.append(new_channel_name)
            new_channel_name = self.format_template_room_name(template, data, attempt)
        return new_channel_name

    @staticmethod
    def get_template_data(member: discord.Member | discord.User) -> dict[str, str]:
        """Return a dict of template data based on a member."""
        data = {"username": member.display_name, "mention": member.mention}
        if isinstance(member, discord.Member):
            for activity in member.activities:
                if activity.type == discord.ActivityType.playing:
                    data["game"] = activity.name or ""
                    break
        return data

    def format_template_room_name(self, template: str, data: dict, num: int = 1) -> str:
        """Return a formatted channel name, taking into account the 100 character channel name limit."""
        nums = {"dupenum": num}
        return self.template.render(
            template=template,
            data={**nums, **data},
        )[:100].strip()

    async def is_admin_or_admin_role(self, who: discord.Role | discord.Member) -> bool:
        """Check if a member (or role) is an admin (role).

        Also takes into account if the setting is enabled.
        """
        if await self.config.guild(who.guild).admin_access():
            if isinstance(who, discord.Role):
                return who in await self.bot.get_admin_roles(who.guild)
            if isinstance(who, discord.Member):
                return await self.bot.is_admin(who)
        return False

    async def is_mod_or_mod_role(self, who: discord.Role | discord.Member) -> bool:
        """Check if a member (or role) is a mod (role).

        Also takes into account if the setting is enabled.
        """
        if await self.config.guild(who.guild).mod_access():
            if isinstance(who, discord.Role):
                return who in await self.bot.get_mod_roles(who.guild)
            if isinstance(who, discord.Member):
                return await self.bot.is_mod(who)
        return False

    def check_perms_source_dest(
        self,
        voicemeister_source: discord.VoiceChannel,
        category_dest: discord.CategoryChannel,
        *,
        with_manage_roles_guild: bool = False,
        with_legacy_text_channel: bool = False,
        with_optional_clone_perms: bool = False,
        detailed: bool = False,
    ) -> tuple[bool, bool, str | None]:
        """Check if the permissions in a VoiceMeister Source and a destination category are sufficient."""
        source = voicemeister_source.permissions_for(voicemeister_source.guild.me)
        dest = category_dest.permissions_for(category_dest.guild.me)
        result_required = True
        result_optional = True
        # Required
        for perm_name in self.perms_bot_source:
            result_required = result_required and bool(getattr(source, perm_name))
        for perm_name in self.perms_bot_dest:
            result_required = result_required and bool(getattr(dest, perm_name))
        if with_manage_roles_guild:
            result_required = (
                result_required
                and category_dest.guild.me.guild_permissions.manage_roles
            )
        # Optional
        if with_legacy_text_channel:
            for perm_name in self.perms_bot_dest_legacy_text:
                result_optional = result_optional and getattr(dest, perm_name)
        clone_section = None
        if with_optional_clone_perms:
            clone_result, clone_section = self._check_perms_source_dest_optional(
                voicemeister_source, dest, detailed=detailed
            )
            result_optional = result_optional and clone_result
        result = result_required and result_optional
        if not detailed:
            return result_required, result_optional, None

        source_section = SettingDisplay("Required on Source Voice Channel")
        for perm_name in self.perms_bot_source:
            source_section.add(
                perm_name.capitalize().replace("_", " "), getattr(source, perm_name)
            )

        dest_section = SettingDisplay("Required on Destination Category")
        for perm_name in self.perms_bot_dest:
            dest_section.add(
                perm_name.capitalize().replace("_", " "), getattr(dest, perm_name)
            )
        voicemeister_sections = [dest_section]

        if with_manage_roles_guild:
            guild_section = SettingDisplay("Required in Guild")
            guild_section.add(
                "Manage roles", category_dest.guild.me.guild_permissions.manage_roles
            )
            voicemeister_sections.append(guild_section)

        if with_legacy_text_channel:
            text_section = SettingDisplay(
                "Optional on Destination Category (for legacy text channel)"
            )
            for perm_name in self.perms_bot_dest_legacy_text:
                text_section.add(
                    perm_name.capitalize().replace("_", " "), getattr(dest, perm_name)
                )
            voicemeister_sections.append(text_section)

        if clone_section:
            voicemeister_sections.append(clone_section)

        status_emoji = "\N{NO ENTRY SIGN}"
        if result:
            status_emoji = "\N{WHITE HEAVY CHECK MARK}"
        elif result_required:
            status_emoji = "\N{WARNING SIGN}\N{VARIATION SELECTOR-16}"
        result_str = (
            f"\n{status_emoji} Source VC: {voicemeister_source.mention} -> Dest Category: {category_dest.mention}"
            "\n"
            f"{source_section.display(*voicemeister_sections)}"
        )
        return result_required, result_optional, result_str

    @staticmethod
    def _check_perms_source_dest_optional(
        voicemeister_source: discord.VoiceChannel,
        dest_perms: discord.Permissions,
        *,
        detailed: bool = False,
    ) -> tuple[bool, SettingDisplay | None]:
        result = True
        checked_perms = {}
        source_overwrites = (
            voicemeister_source.overwrites if voicemeister_source.overwrites else {}
        )
        for permissions in source_overwrites.values():
            # We can't put manage_roles in overwrites, so just get rid of it
            # Also get rid of view_channel, connect, and send_messages, as we will be controlling those
            permissions.update(
                connect=None, manage_roles=None, view_channel=None, send_messages=None
            )
            # Check each permission for each overwrite target to make sure the bot has it allowed in the dest category
            for name, value in permissions:
                if value is not None and name not in checked_perms:
                    check_result = bool(getattr(dest_perms, name))
                    if not detailed and not check_result:
                        return False, None
                    checked_perms[name] = check_result
                    result = result and check_result
        if not detailed:
            return True, None
        clone_section = SettingDisplay(
            "Optional on Destination Category (for source clone)"
        )
        if checked_perms:
            for name, value in checked_perms.items():
                clone_section.add(name.capitalize().replace("_", " "), value)
            return result, clone_section
        return result, None

    async def get_all_voicemeister_source_configs(
        self, guild: discord.Guild
    ) -> dict[int, dict[str, Any]]:
        """Return a dict of all voicemeister source configs, cleaning up any invalid ones."""
        unsorted_list_of_configs = []
        configs = await self.config.custom(
            "VOICEMEISTER_SOURCE", str(guild.id)
        ).all()  # Does NOT return default values
        for channel_id in configs:
            channel = guild.get_channel(int(channel_id))
            if not isinstance(channel, discord.VoiceChannel):
                continue
            config = await self.get_voicemeister_source_config(channel)
            if config:
                unsorted_list_of_configs.append((channel.position, channel_id, config))
            else:
                await self.config.custom(
                    "VOICEMEISTER_SOURCE", str(guild.id), channel_id
                ).clear()
        result = {}
        for _, channel_id, config in sorted(
            unsorted_list_of_configs, key=lambda source_config: source_config[0]
        ):
            result[int(channel_id)] = config
        return result

    async def get_voicemeister_source_config(
        self, voicemeister_source: discord.VoiceChannel | discord.abc.GuildChannel | None
    ) -> dict[str, Any] | None:
        """Return the config for a voicemeister source, or None if not set up yet."""
        if not voicemeister_source:
            return None
        if not isinstance(voicemeister_source, discord.VoiceChannel):
            return None
        config = await self.config.custom(
            "VOICEMEISTER_SOURCE", str(voicemeister_source.guild.id), str(voicemeister_source.id)
        ).all()  # Returns default values
        if not config["dest_category_id"]:
            return None

        perms = {
            "allow": {
                "view_channel": True,
                "connect": True,
                "send_messages": config["perm_send_messages"],
            },
            "lock": {"view_channel": True, "connect": False, "send_messages": False},
            "deny": {"view_channel": False, "connect": False, "send_messages": False},
        }
        perms["owner"] = {
            **perms["allow"],
            "manage_channels": True if config["perm_owner_manage_channels"] else None,
            "manage_messages": True,
        }
        if config["room_type"] == "private":
            perms["access"] = perms["deny"]
        elif config["room_type"] == "locked":
            perms["access"] = perms["lock"]
        else:
            perms["access"] = perms["allow"]

        config["perms"] = perms
        return config

    async def get_voicemeister_info(
        self, voicemeister: discord.VoiceChannel | None
    ) -> dict[str, Any] | None:
        """Get info for a VoiceMeister, or None if the voice channel isn't a VoiceMeister."""
        if not voicemeister:
            return None
        if not await self.config.channel(voicemeister).source_channel():
            return None
        return await self.config.channel(voicemeister).all()

    async def get_voicemeister_legacy_text_channel(
        self, voicemeister: discord.VoiceChannel | int | None
    ) -> discord.TextChannel | None:
        """Get the VoiceMeister legacy test channel, if it exists and we have manage channels permission."""
        if isinstance(voicemeister, discord.VoiceChannel):
            voicemeister = voicemeister.id
        if not voicemeister:
            return None
        legacy_text_channel_id = await self.config.channel_from_id(
            voicemeister
        ).associated_text_channel()
        legacy_text_channel = (
            self.bot.get_channel(legacy_text_channel_id)
            if legacy_text_channel_id
            else None
        )
        if (
            isinstance(legacy_text_channel, discord.TextChannel)
            and legacy_text_channel.permissions_for(
                legacy_text_channel.guild.me
            ).manage_channels
        ):
            return legacy_text_channel
        return None

    @staticmethod
    def check_if_member_or_role_allowed(
        channel: discord.VoiceChannel,
        member_or_role: discord.Member | discord.Role,
    ) -> bool:
        """Check if a member/role is allowed to connect to a voice channel.

        Doesn't matter if they can't see it, it ONLY checks the connect permission.
        Mostly copied from https://github.com/Rapptz/discord.py/blob/master/discord/abc.py:GuildChannel.permissions_for()
        I needed the logic except the "if not base.read_messages:" part that removed all permissions.
        """
        if channel.guild.owner_id == member_or_role.id:
            return True

        default_role = channel.guild.default_role
        base = discord.Permissions(default_role.permissions.value)

        # Handle the role case first
        if isinstance(member_or_role, discord.Role):
            base.value |= member_or_role.permissions.value

            if base.administrator:
                return True

            # Apply @everyone allow/deny first since it's special
            with suppress(KeyError):
                default_allow, default_deny = channel.overwrites[default_role].pair()
                base.handle_overwrite(
                    allow=default_allow.value, deny=default_deny.value
                )

            if member_or_role.is_default():
                return base.connect

            with suppress(KeyError):
                role_allow, role_deny = channel.overwrites[member_or_role].pair()
                base.handle_overwrite(allow=role_allow.value, deny=role_deny.value)

            return base.connect

        member_roles = member_or_role.roles

        # Apply guild roles that the member has.
        for role in member_roles:
            base.value |= role.permissions.value

        # Guild-wide Administrator -> True for everything
        # Bypass all channel-specific overrides
        if base.administrator:
            return True

        # Apply @everyone allow/deny first since it's special
        with suppress(KeyError):
            default_allow, default_deny = channel.overwrites[default_role].pair()
            base.handle_overwrite(allow=default_allow.value, deny=default_deny.value)

        allows = 0
        denies = 0

        # Apply channel specific role permission overwrites
        for role, overwrite in channel.overwrites.items():
            if (
                isinstance(role, discord.Role)
                and role != default_role
                and role in member_roles
            ):
                allows |= overwrite.pair()[0].value
                denies |= overwrite.pair()[1].value

        base.handle_overwrite(allow=allows, deny=denies)

        # Apply member specific permission overwrites
        with suppress(KeyError):
            member_allow, member_deny = channel.overwrites[member_or_role].pair()
            base.handle_overwrite(allow=member_allow.value, deny=member_deny.value)

        if member_or_role.is_timed_out():
            # Timeout leads to every permission except VIEW_CHANNEL and READ_MESSAGE_HISTORY
            # being explicitly denied
            return False

        return base.connect

    def get_member_roles(
        self, voicemeister_source: discord.VoiceChannel
    ) -> list[discord.Role]:
        """Get member roles set on a VoiceMeister Source."""
        member_roles = []
        # If @everyone is allowed to connect to the source channel, there are no member roles
        if not self.check_if_member_or_role_allowed(
            voicemeister_source,
            voicemeister_source.guild.default_role,
        ):
            # If it isn't allowed, then member roles are being used
            member_roles.extend(
                role
                for role, overwrite in voicemeister_source.overwrites.items()
                if isinstance(role, discord.Role)
                and role != voicemeister_source.guild.default_role
                and overwrite.pair()[0].connect
            )
        return member_roles

    async def get_bot_roles(self, guild: discord.Guild) -> list[discord.Role]:
        """Get the additional bot roles that are added to each VoiceMeister."""
        bot_roles = []
        bot_role_ids = []
        some_roles_were_not_found = False
        for bot_role_id in await self.config.guild(guild).bot_access():
            bot_role = guild.get_role(bot_role_id)
            if bot_role:
                bot_roles.append(bot_role)
                bot_role_ids.append(bot_role_id)
            else:
                some_roles_were_not_found = True
        if some_roles_were_not_found:
            # Update the bot role list to remove nonexistent roles
            await self.config.guild(guild).bot_access.set(bot_role_ids)
        return bot_roles

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
        """Delete the voice channel."""
        try:
            await channel.delete()
            await interaction.response.send_message(content="The channel has been deleted.", ephemeral=True)

            # Clean up the stored data
            temp_channels = await self.config.guild(channel.guild).temp_channels()
            if channel.id in temp_channels:
                del temp_channels[channel.id]
                await self.config.guild(channel.guild).temp_channels.set(temp_channels)
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

    async def info(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Provide information about the current voice channel."""
        try:
            owners = await self.config.guild(channel.guild).owners()
            owner_id = owners.get(str(channel.id))

            # Fetch member info
            owner = channel.guild.get_member(owner_id) if owner_id else None
            owner_name = owner.display_name if owner else "None"
            owner_mention = owner.mention if owner else "None"

            # Channel information
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
            embed.add_field(name="User Limit", value=user_limit)
            embed.add_field(name="Region", value=rtc_region)

            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            await interaction.response.send_message(content=error_message, ephemeral=True)

    async def change_region(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Change the region of the voice channel."""
        try:
            view = RegionSelectView(self, channel)
            await interaction.response.send_message("Select a region for the voice channel:", view=view, ephemeral=True)
        except Exception as e:
            await self.handle_error(interaction, e)

    async def cog_unload(self):
        pass

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

    def is_name_valid(self, name: str) -> bool:
        """Check if the name is valid (not explicit or racist)."""
        banned_words = ["explicit_word1", "explicit_word2", "racist_word1"]
        return not any(banned_word in name.lower() for banned_word in banned_words)

    @commands.group(aliases=["vmset"])
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def voicemeisterset(self, ctx: commands.Context) -> None:
        """Configure the VoiceMeister cog."""

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
        """Default format: Star's Room.

        Custom format example:
        `{{username}}'s Room{% if dupenum > 1 %} ({{dupenum}}){% endif %}`
        """
        await self._save_room_name(ctx, voicemeister_source, "username")

    @modify_name.command(name="game")
    async def modify_name_game(
        self, ctx: commands.Context, voicemeister_source: discord.VoiceChannel
    ) -> None:
        """The user's current playing game, otherwise the username format.

        Custom format example:
        `{{game}}{% if not game %}{{username}}'s Room{% endif %}{% if dupenum > 1 %} ({{dupenum}}){% endif %}`
        """
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
        """
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
        about by looking at `[p]voicemeisterset modify name custom`.

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
        """Allow users to send messages in the VoiceMeister built-in text channel."""
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
                    f"Users are {'now' if new_config_value else 'no longer'} able to send messages in the VoiceMeister built-in text channel."
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
            {"emoji": DEFAULT_EMOJIS["create_text"], "custom_id": "wip", "row": 3},  # Changed custom_id to "wip"
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
            "wip": self.handle_wip,  # Added handler for WIP
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
        """Hide the channel by setting view permissions to False for @everyone."""
        try:
            overwrites = channel.overwrites_for(interaction.guild.default_role)
            if overwrites.view_channel is False:
                await interaction.response.send_message("The channel is already hidden.", ephemeral=True)
            else:
                overwrites.view_channel = False
                await channel.set_permissions(interaction.guild.default_role, overwrite=overwrites)
                await interaction.response.send_message("The channel is now hidden.", ephemeral=True)
        except Exception as e:
            await self.bot.get_cog("VoiceMeister").handle_error(interaction, e)

    async def handle_unhide(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Unhide the channel by setting view permissions to True for @everyone."""
        try:
            overwrites = channel.overwrites_for(interaction.guild.default_role)
            if overwrites.view_channel is True:
                await interaction.response.send_message("The channel is already visible.", ephemeral=True)
            else:
                overwrites.view_channel = True
                await channel.set_permissions(interaction.guild.default_role, overwrite=overwrites)
                await interaction.response.send_message("The channel is now visible.", ephemeral=True)
        except Exception as e:
            await self.bot.get_cog("VoiceMeister").handle_error(interaction, e)

    async def handle_invite(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        invite = await channel.create_invite(max_uses=5, unique=True)
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

    async def handle_wip(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Handle the WIP button interaction."""
        await interaction.response.send_message("This item is a Work In Progress! Check back soon!", ephemeral=True)

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

