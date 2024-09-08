from redbot.core import commands, Config
from redbot.core.bot import Red
import discord
from typing import Optional, Dict
from Star_Utils import Buttons, Dropdown, Cog, Settings

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
        view = VoiceControlView(bot=self.bot, author=ctx.author)
        await ctx.send("Voice Control Panel", view=view, ephemeral=True)

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

class VoiceControlView(Buttons):
    def __init__(self, bot: Red, author: discord.Member):
        buttons = [
            {"label": "🔒 Lock", "style": discord.ButtonStyle.primary, "custom_id": "lock"},
            {"label": "🔓 Unlock", "style": discord.ButtonStyle.danger, "custom_id": "unlock"},
            {"label": "👁 ️ Hide", "style": discord.ButtonStyle.secondary, "custom_id": "hide"},
            {"label": "👥 Unhide", "style": discord.ButtonStyle.secondary, "custom_id": "unhide"},
            {"label": "🔊 User Limit", "style": discord.ButtonStyle.secondary, "custom_id": "userlimit"},
            {"label": "🚫 Ban", "style": discord.ButtonStyle.secondary, "custom_id": "ban"},
            {"label": "✅ Permit", "style": discord.ButtonStyle.secondary, "custom_id": "permit"},
            {"label": "✏️ Rename", "style": discord.ButtonStyle.secondary, "custom_id": "rename"},
            {"label": "🌍 Region", "style": discord.ButtonStyle.secondary, "custom_id": "region"},
            {"label": "👑 Claim", "style": discord.ButtonStyle.secondary, "custom_id": "claim"},
            {"label": "🔄 Transfer", "style": discord.ButtonStyle.secondary, "custom_id": "transfer"},
        ]
        super().__init__(timeout=180, buttons=buttons, members=[author.id] + list(bot.owner_ids), function=self.on_button_click)
        self.bot = bot
        self.author = author

    async def on_button_click(self, view: Buttons, interaction: discord.Interaction):
        handlers = {
            "lock": self.handle_lock,
            "unlock": self.handle_unlock,
            "hide": self.handle_hide,
            "unhide": self.handle_unhide,
            "userlimit": self.handle_userlimit,
            "ban": self.handle_ban,
            "permit": self.handle_permit,
            "rename": self.handle_rename,
            "region": self.handle_region,
            "claim": self.handle_claim,
            "transfer": self.handle_transfer,
        }
        handler = handlers.get(interaction.data["custom_id"])
        if handler:
            await handler(interaction)

    async def handle_lock(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        channel = interaction.user.voice.channel
        await channel.set_permissions(interaction.guild.default_role, connect=False)
        await interaction.response.send_message(f"{channel.name} is now locked.", ephemeral=True)

    async def handle_unlock(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        channel = interaction.user.voice.channel
        await channel.set_permissions(interaction.guild.default_role, connect=True)
        await interaction.response.send_message(f"{channel.name} is now unlocked.", ephemeral=True)

    async def handle_hide(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        channel = interaction.user.voice.channel
        await channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await interaction.response.send_message(f"{channel.name} is now hidden.", ephemeral=True)

    async def handle_unhide(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        channel = interaction.user.voice.channel
        await channel.set_permissions(interaction.guild.default_role, view_channel=True)
        await interaction.response.send_message(f"{channel.name} is now visible.", ephemeral=True)

    async def handle_userlimit(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        # Create a select menu for user limit using Dropdown
        options = [{"label": str(i), "value": str(i)} for i in range(1, 100)]
        view = Dropdown(
            placeholder="Select user limit...",
            options=options,
            function=self.set_user_limit,
            function_kwargs={"interaction": interaction}
        )
        await interaction.response.send_message("Choose a user limit:", view=view, ephemeral=True)

    async def set_user_limit(self, view: Dropdown, interaction: discord.Interaction, options: list):
        limit = int(options[0])
        channel = interaction.user.voice.channel
        await channel.edit(user_limit=limit)
        await interaction.followup.send(f"User limit for {channel.name} is now {limit}.", ephemeral=True)

    async def handle_ban(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        # Create a select menu for banning users and roles
        user_options = [{"label": member.display_name, "value": str(member.id)} for member in interaction.guild.members]
        role_options = [{"label": role.name, "value": str(role.id)} for role in interaction.guild.roles]
        options = user_options + role_options
        view = Dropdown(
            placeholder="Select user or role to ban...",
            options=options,
            function=self.ban_user_or_role,
            function_kwargs={"interaction": interaction}
        )
        await interaction.response.send_message("Choose a user or role to ban:", view=view, ephemeral=True)

    async def ban_user_or_role(self, view: Dropdown, interaction: discord.Interaction, options: list):
        selected_id = int(options[0])
        channel = interaction.user.voice.channel

        if interaction.guild.get_member(selected_id):
            # It's a user
            banned_users = await self.config.guild(interaction.guild).banned_users()
            banned_users[channel.id] = banned_users.get(channel.id, []) + [selected_id]
            await self.config.guild(interaction.guild).banned_users.set(banned_users)
            member = interaction.guild.get_member(selected_id)
            await interaction.followup.send(f"{member.display_name} is banned from {channel.name}.", ephemeral=True)
        else:
            # It's a role
            banned_roles = await self.config.guild(interaction.guild).banned_roles()
            banned_roles[channel.id] = banned_roles.get(channel.id, []) + [selected_id]
            await self.config.guild(interaction.guild).banned_roles.set(banned_roles)
            role = interaction.guild.get_role(selected_id)
            await interaction.followup.send(f"Role {role.name} is banned from {channel.name}.", ephemeral=True)

    async def handle_permit(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        # Create a select menu for allowing users and roles
        user_options = [{"label": member.display_name, "value": str(member.id)} for member in interaction.guild.members]
        role_options = [{"label": role.name, "value": str(role.id)} for role in interaction.guild.roles]
        options = user_options + role_options
        view = Dropdown(
            placeholder="Select user or role to permit...",
            options=options,
            function=self.permit_user_or_role,
            function_kwargs={"interaction": interaction}
        )
        await interaction.response.send_message("Choose a user or role to permit:", view=view, ephemeral=True)

    async def permit_user_or_role(self, view: Dropdown, interaction: discord.Interaction, options: list):
        selected_id = int(options[0])
        channel = interaction.user.voice.channel

        if interaction.guild.get_member(selected_id):
            # It's a user
            allowed_users = await self.config.guild(interaction.guild).allowed_users()
            allowed_users[channel.id] = allowed_users.get(channel.id, []) + [selected_id]
            await self.config.guild(interaction.guild).allowed_users.set(allowed_users)
            member = interaction.guild.get_member(selected_id)
            await interaction.followup.send(f"{member.display_name} is permitted to join {channel.name}.", ephemeral=True)
        else:
            # It's a role
            allowed_roles = await self.config.guild(interaction.guild).allowed_roles()
            allowed_roles[channel.id] = allowed_roles.get(channel.id, []) + [selected_id]
            await self.config.guild(interaction.guild).allowed_roles.set(allowed_roles)
            role = interaction.guild.get_role(selected_id)
            await interaction.followup.send(f"Role {role.name} is permitted to join {channel.name}.", ephemeral=True)

    async def handle_rename(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        # Prompt for new channel name
        await interaction.response.send_message("Please enter the new name for the channel:", ephemeral=True)
        msg = await self.bot.wait_for(
            "message",
            check=lambda m: m.author == interaction.user and m.channel == interaction.channel,
            timeout=30
        )
        new_name = msg.content

        channel = interaction.user.voice.channel
        await channel.edit(name=new_name)
        await interaction.followup.send(f"Voice channel renamed to {new_name}.", ephemeral=True)

    async def handle_region(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        # Create a select menu for region using Dropdown
        regions = [region for region in discord.VoiceRegion]
        options = [{"label": region.name, "value": region.value} for region in regions]
        view = Dropdown(
            placeholder="Select region...",
            options=options,
            function=self.set_region,
            function_kwargs={"interaction": interaction}
        )
        await interaction.response.send_message("Choose a region:", view=view, ephemeral=True)

    async def set_region(self, view: Dropdown, interaction: discord.Interaction, options: list):
        region_value = options[0]
        channel = interaction.user.voice.channel
        await channel.edit(rtc_region=region_value)
        await interaction.followup.send(f"Region for {channel.name} is now {region_value}.", ephemeral=True)

    async def handle_claim(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        channel = interaction.user.voice.channel
        owners = await self.config.guild(interaction.guild).owners()
        if channel.id not in owners:
            owners[channel.id] = interaction.user.id
            await self.config.guild(interaction.guild).owners.set(owners)
            await interaction.response.send_message(f"You have claimed ownership of {channel.name}.", ephemeral=True)
        else:
            await interaction.response.send_message(f"{channel.name} already has an owner.", ephemeral=True)

    async def handle_transfer(self, interaction: discord.Interaction):
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("You are not connected to a voice channel.", ephemeral=True)
            return

        channel = interaction.user.voice.channel
        owners = await self.config.guild(interaction.guild).owners()
        if owners.get(channel.id) == interaction.user.id:
            # Create a select menu for transferring ownership using Dropdown
            options = [{"label": member.display_name, "value": str(member.id)} for member in channel.members]
            view = Dropdown(
                placeholder="Select member to transfer ownership...",
                options=options,
                function=self.transfer_ownership,
                function_kwargs={"interaction": interaction}
            )
            await interaction.response.send_message("Choose a member to transfer ownership:", view=view, ephemeral=True)
        else:
            await interaction.response.send_message("You are not the owner of this voice channel.", ephemeral=True)

    async def transfer_ownership(self, view: Dropdown, interaction: discord.Interaction, options: list):
        member_id = int(options[0])
        channel = interaction.user.voice.channel
        owners = await self.config.guild(interaction.guild).owners()
        owners[channel.id] = member_id
        await self.config.guild(interaction.guild).owners.set(owners)
        member = interaction.guild.get_member(member_id)
        await interaction.followup.send(f"Ownership of {channel.name} transferred to {member.display_name}.", ephemeral=True)

async def setup(bot: Red):
    await bot.add_cog(VoiceMeister(bot))
