import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from discord.ext.commands import *
from typing import List, Union, Dict
from contextlib import suppress

# Define popular Discord activities with their respective application IDs
popular_activities = {
    "Watch Together": 880218394199220334,
    "Gartic Phone": 879863881349087252,
    "Amazon Music": 879863686565621790,
    "Rhythm": 880218832743055411,
    "Chess In The Park": 832012774040141894,
    "Know What I Meme": 950505761862189096
}

class DisconnectMembers(discord.ui.Select):
    def __init__(self, member: discord.Member):
        self.member = member
        self.guild = member.guild
        self.channel = member.voice.channel
        options = [
            discord.SelectOption(
                value=str(m.id),
                label=f"{m} ({m.id})"
            )
            for m in self.channel.members
        ]
        super().__init__(placeholder="Choose members...", min_values=1, max_values=len(self.channel.members), options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        disconnected, failed = 0, 0

        for member_id in self.values:
            member = self.guild.get_member(int(member_id))
            if member and member.voice and member.voice.channel == self.channel:
                try:
                    await member.move_to(None)
                    disconnected += 1
                except:
                    failed += 1
            else:
                failed += 1

        await interaction.followup.send(f"Successfully **disconnected** {disconnected} member(s) (`{failed}` failed)", ephemeral=True)

class ActivitySelection(discord.ui.Select):
    def __init__(self, member: discord.Member):
        self.member = member
        self.guild = member.guild
        self.channel = member.voice.channel
        options = [
            discord.SelectOption(
                value=activity["id"],
                label=activity["name"],
                emoji=activity["emoji"],
            )
            for activity in activity_types
        ]
        super().__init__(placeholder="Choose an activity...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        try:
            invite = await self.channel.create_invite(
                max_age=0,
                target_type=discord.InviteTarget.embedded_application,
                target_application_id=int(self.values[0]),
                reason=f"VoiceMeister: {self.member} started an activity",
            )
            await interaction.followup.send(f"[Click here to join the activity!]({invite.url})", ephemeral=True)
        except Exception:
            await interaction.followup.send("Failed to create an **invite** for the selected **activity**!", ephemeral=True)

class Interface(discord.ui.View):
    def __init__(self, bot: Red):
        self.bot = bot
        super().__init__(timeout=None)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        user_voice = interaction.user.voice
        if not user_voice:
            await interaction.response.send_message("You're not connected to a **voice channel**", ephemeral=True)
            return False

        owner_id = await self.bot.db.fetchval(
            """
            SELECT owner_id FROM voicemaster_channels
            WHERE channel_id = $1
            """,
            user_voice.channel.id,
        )

        if not owner_id:
            await interaction.response.send_message("You're not in a **VoiceMeister** channel!", ephemeral=True)
            return False

        if interaction.data["custom_id"] == "voicemeister:information":
            return True

        if interaction.user.id != owner_id:
            await interaction.response.send_message("You don't own this **voice channel**!", ephemeral=True)
            return False

        return True

    @discord.ui.button(label="Lock", style=discord.ButtonStyle.grey, custom_id="voicemeister:lock", emoji="<:Locked:1279848927587467447>")
    async def lock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            connect=False,
            reason=f"VoiceMeister: {interaction.user} locked voice channel",
        )
        await interaction.response.send_message("Your **voice channel** has been locked", ephemeral=True)

    @discord.ui.button(label="Unlock", style=discord.ButtonStyle.grey, custom_id="voicemeister:unlock", emoji="<:Unlocked:1279848944570073109>")
    async def unlock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            connect=None,
            reason=f"VoiceMeister: {interaction.user} unlocked voice channel",
        )
        await interaction.response.send_message("Your **voice channel** has been unlocked", ephemeral=True)

    @discord.ui.button(label="Ghost", style=discord.ButtonStyle.grey, custom_id="voicemeister:ghost", emoji="<:Crossed_Eye:1279848957475819723>")
    async def ghost(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            view_channel=False,
            reason=f"VoiceMeister: {interaction.user} made voice channel hidden",
        )
        await interaction.response.send_message("Your **voice channel** has been hidden", ephemeral=True)

    @discord.ui.button(label="Reveal", style=discord.ButtonStyle.grey, custom_id="voicemeister:reveal", emoji="<:Eye:1279848986299076728>")
    async def reveal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            view_channel=None,
            reason=f"VoiceMeister: {interaction.user} revealed voice channel",
        )
        await interaction.response.send_message("Your **voice channel** has been revealed", ephemeral=True)

    @discord.ui.button(label="Claim", style=discord.ButtonStyle.grey, custom_id="voicemeister:claim", emoji="<:Crown:1279848977658810451>")
    async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.bot.db.execute(
            """
            UPDATE voicemaster_channels
            SET owner_id = $2
            WHERE channel_id = $1
            """,
            interaction.user.voice.channel.id,
            interaction.user.id,
        )

        if interaction.user.voice.channel.name.endswith("channel"):
            try:
                await interaction.user.voice.channel.edit(
                    name=f"{interaction.user.display_name}'s channel"
                )
            except Exception:
                pass

        await interaction.response.send_message("You are now the owner of this **channel**!", ephemeral=True)

    @discord.ui.button(label="Disconnect", style=discord.ButtonStyle.grey, custom_id="voicemeister:disconnect")
    async def disconnect(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Interface(self.bot)
        view.add_item(DisconnectMembers(interaction.user))
        await interaction.response.send_message("Select members from the **dropdown** to disconnect.", view=view, ephemeral=True)

    @discord.ui.button(label="Activity", style=discord.ButtonStyle.grey, custom_id="voicemeister:activity")
    async def activity(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Interface(self.bot)
        view.add_item(ActivitySelection(interaction.user))
        await interaction.response.send_message("Select an activity from the **dropdown** to start!", view=view, ephemeral=True)

    @discord.ui.button(label="Information", style=discord.ButtonStyle.grey, custom_id="voicemeister:information", emoji="<:Information:1279848926383702056>")
    async def information(self, interaction: discord.Interaction, button: discord.ui.Button):
        with suppress(discord.InteractionResponded):
            await interaction.response.defer(ephemeral=True)

        channel = interaction.user.voice.channel

        embed = discord.Embed(
            color=discord.Color.neutral(),
            title=channel.name,
            description=(
                f"**Owner:** {interaction.user} (`{interaction.user.id}`)"
                + f"\n**Locked:** "
                + ("" if channel.permissions_for(interaction.guild.default_role).connect is False else "")
                + f"\n**Created:** {discord.utils.format_dt(channel.created_at, style='R')}"
                + f"\n**Bitrate:** {int(channel.bitrate / 1000)}kbps"
                + f"\n**Connected:** `{len(channel.members)}`"
                + (f"/`{channel.user_limit}`" if channel.user_limit else "")
            ),
        )
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)

        roles_permitted = [
            target for target, overwrite in channel.overwrites.items()
            if overwrite.connect is True and isinstance(target, discord.Role)
        ]
        if roles_permitted:
            embed.add_field(name="**Role Permitted**", value=", ".join(role.mention for role in roles_permitted), inline=False)

        members_permitted = [
            target for target, overwrite in channel.overwrites.items()
            if overwrite.connect is True and isinstance(target, discord.Member) and target != interaction.user
        ]
        if members_permitted:
            embed.add_field(name="**Member Permitted**", value=", ".join(member.mention for member in members_permitted), inline=False)

        await interaction.followup.send(embed=embed, ephemeral=True)

    @discord.ui.button(label="Increase", style=discord.ButtonStyle.grey, custom_id="voicemeister:increase", emoji="<:People:1279848931043573790>")
    async def increase(self, interaction: discord.Interaction, button: discord.ui.Button):
        limit = interaction.user.voice.channel.user_limit or 0

        if limit == 99:
            await interaction.response.send_message("Channel member limit cannot be more than **99 members**!", ephemeral=True)
            return

        await interaction.user.voice.channel.edit(
            user_limit=limit + 1,
            reason=f"VoiceMeister: {interaction.user} increased voice channel user limit",
        )
        await interaction.response.send_message(f"Your **voice channel**'s limit has been updated to `{limit + 1}`", ephemeral=True)

    @discord.ui.button(label="Decrease", style=discord.ButtonStyle.grey, custom_id="voicemeister:decrease", emoji="<:People:1279848931043573790>")
    async def decrease(self, interaction: discord.Interaction, button: discord.ui.Button):
        limit = interaction.user.voice.channel.user_limit or 0

        if limit == 0:
            await interaction.response.send_message("Channel member limit must be greater than **0 members**", ephemeral=True)
            return

        await interaction.user.voice.channel.edit(
            user_limit=limit - 1,
            reason=f"VoiceMeister: {interaction.user} decreased voice channel user limit",
        )
        if (limit - 1) == 0:
            await interaction.response.send_message("Your **voice channel**'s limit has been **removed**", ephemeral=True)
        else:
            await interaction.response.send_message(f"Your **voice channel**'s limit has been updated to `{limit - 1}`", ephemeral=True)

    @discord.ui.button(label="Delete Channel", style=discord.ButtonStyle.red, custom_id="voicemeister:delete", emoji="<:TrashCan:1279875131136806993>")
    async def delete_channel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.delete(reason=f"VoiceMeister: {interaction.user} deleted their voice channel")
        await interaction.response.send_message("Your **voice channel** has been deleted", ephemeral=True)

    @discord.ui.button(label="Create Text Channel", style=discord.ButtonStyle.blurple, custom_id="voicemeister:create_text", emoji="<:SpeachBubble:1279890650535428198>")
    async def create_text_channel(self, interaction: discord.Interaction, button: discord.ui.Button):
        category = interaction.user.voice.channel.category
        text_channel = await category.create_text_channel(f"{interaction.user.display_name}-text")
        await interaction.response.send_message(f"Text channel {text_channel.mention} created for your voice channel", ephemeral=True)

    @discord.ui.button(label="Reset Configurations", style=discord.ButtonStyle.red, custom_id="voicemeister:reset", emoji="<:reset:1280057459146362880>")
    async def reset_configurations(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.config.guild(interaction.guild).clear()
        await interaction.response.send_message("All **VoiceMeister** configurations have been reset", ephemeral=True)

class VoiceMeister(Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_guild(
            category_id=None,
            interface_id=None,
            channel_id=None,
            role_id=None,
            region=None,
            bitrate=None
        )
        self.bot.add_view(Interface(bot))

    @commands.group(name="voicemeister", aliases=["vm"], invoke_without_command=True)
    async def voicemeister(self, ctx: commands.Context):
        """VoiceMeister command group."""
        await ctx.send_help()

    @commands.command(name="activityinvite")
    async def activity_invite(self, ctx: commands.Context, activity_name: str):
        """Generate an invite for a popular Discord activity."""
        if not ctx.author.voice or not ctx.author.voice.channel:
            await ctx.send("You need to be in a voice channel to start an activity.")
            return

        activity_id = popular_activities.get(activity_name)
        if not activity_id:
            await ctx.send(f"Invalid activity name. Choose from: {', '.join(popular_activities.keys())}")
            return

        try:
            invite = await ctx.author.voice.channel.create_invite(
                max_age=0,
                target_type=discord.InviteTarget.embedded_application,
                target_application_id=activity_id,
                reason=f"VoiceMeister: {ctx.author} started an activity"
            )
            await ctx.send(f"Invite for **{activity_name}**: {invite.url}")
        except Exception as e:
            await ctx.send(f"Failed to create an invite for **{activity_name}**. Error: {str(e)}")

    @commands.command(name="setup")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def setup(self, ctx: commands.Context):
        """Setup VoiceMeister in the server."""
        category = await ctx.guild.create_category("Voice Channels")
        interface = await category.create_text_channel("interface")
        channel = await category.create_voice_channel("Join to Create")

        await self.config.guild(ctx.guild).category_id.set(category.id)
        await self.config.guild(ctx.guild).interface_id.set(interface.id)
        await self.config.guild(ctx.guild).channel_id.set(channel.id)

        embed = discord.Embed(
            title="VoiceMeister Interface",
            description="Click the buttons below to control your voice channel",
            color=discord.Color.blue()
        )
        await interface.send(embed=embed, view=Interface(self.bot))

        await ctx.send("VoiceMeister setup complete.")

    @Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if not after.channel:
            return

        if before and before.channel == after.channel:
            return

        config_data = await self.config.guild(member.guild).all()
        if config_data['channel_id'] != after.channel.id:
            return

        channel = await member.guild.create_voice_channel(
            name=f"{member.display_name}'s channel",
            category=member.guild.get_channel(config_data['category_id']) or after.channel.category,
            bitrate=config_data.get('bitrate', int(member.guild.bitrate_limit)),
            rtc_region=config_data.get('region'),
            reason=f"VoiceMeister: Created a voice channel for {member}",
        )

        try:
            await member.move_to(channel, reason="VoiceMeister: Created their own voice channel")
        except discord.HTTPException:
            await channel.delete(reason="VoiceMeister: Failed to move member")
            return

        await channel.set_permissions(
            member,
            read_messages=True,
            connect=True,
            reason=f"VoiceMeister: {member} created a new voice channel",
        )

        await self.bot.db.execute(
            """
            INSERT INTO voicemaster_channels (
                guild_id,
                channel_id,
                owner_id
            ) VALUES ($1, $2, $3)
            """,
            member.guild.id,
            channel.id,
            member.id,
        )

        role_id = config_data.get('role_id')
        if role_id and (role := member.guild.get_role(role_id)) and role not in member.roles:
            try:
                await member.add_roles(role, reason="VoiceMeister: Gave the owner the default role")
            except Exception:
                pass

    @Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if not before.channel:
            return

        if after and before.channel == after.channel:
            return

        role_id = await self.config.guild(member.guild).role_id()
        if role_id and role_id in (role.id for role in member.roles):
            try:
                await member.remove_roles(member.guild.get_role(role_id), reason="VoiceMeister: Removed the default role")
            except Exception:
                pass

        if list(filter(lambda m: not m.bot, before.channel.members)):
            return

        owner_id = await self.bot.db.fetchval(
            """
            DELETE FROM voicemaster_channels
            WHERE channel_id = $1
            RETURNING owner_id
            """,
            before.channel.id,
        )

        if not owner_id:
            return

        try:
            await before.channel.delete()
        except discord.HTTPException:
            pass

    @commands.command(name="claim")
    async def claim(self, ctx: commands.Context):
        """Claim an inactive voice channel."""
        await self.bot.db.execute(
            """
            UPDATE voicemaster_channels
            SET owner_id = $2
            WHERE channel_id = $1
            """,
            ctx.author.voice.channel.id,
            ctx.author.id,
        )

        if ctx.author.voice.channel.name.endswith("channel"):
            try:
                await ctx.author.voice.channel.edit(
                    name=f"{ctx.author.display_name}'s channel"
                )
            except Exception:
                pass

        await ctx.send("You are now the owner of this **channel**!")

    @commands.command(name="lock")
    async def lock(self, ctx: commands.Context):
        """Lock your voice channel."""
        await ctx.author.voice.channel.set_permissions(
            ctx.guild.default_role,
            connect=False,
            reason=f"VoiceMeister: {ctx.author} locked voice channel",
        )
        await ctx.send("Your **voice channel** has been locked")

    @commands.command(name="unlock")
    async def unlock(self, ctx: commands.Context):
        """Unlock your voice channel."""
        await ctx.author.voice.channel.set_permissions(
            ctx.guild.default_role,
            connect=None,
            reason=f"VoiceMeister: {ctx.author} unlocked voice channel",
        )
        await ctx.send("Your **voice channel** has been unlocked")

    @commands.command(name="ghost")
    async def ghost(self, ctx: commands.Context):
        """Hide your voice channel."""
        await ctx.author.voice.channel.set_permissions(
            ctx.guild.default_role,
            view_channel=False,
            reason=f"VoiceMeister: {ctx.author} made voice channel hidden",
        )
        await ctx.send("Your **voice channel** has been hidden")

    @commands.command(name="reveal")
    async def reveal(self, ctx: commands.Context):
        """Reveal your voice channel."""
        await ctx.author.voice.channel.set_permissions(
            ctx.guild.default_role,
            view_channel=None,
            reason=f"VoiceMeister: {ctx.author} revealed voice channel",
        )
        await ctx.send("Your **voice channel** has been revealed")

    @commands.command(name="increase")
    async def increase(self, ctx: commands.Context):
        """Increase the user limit of your voice channel."""
        limit = ctx.author.voice.channel.user_limit or 0

        if limit == 99:
            await ctx.send("Channel member limit cannot be more than **99 members**!")
            return

        await ctx.author.voice.channel.edit(
            user_limit=limit + 1,
            reason=f"VoiceMeister: {ctx.author} increased voice channel user limit",
        )
        await ctx.send(f"Your **voice channel**'s limit has been updated to `{limit + 1}`")

    @commands.command(name="decrease")
    async def decrease(self, ctx: commands.Context):
        """Decrease the user limit of your voice channel."""
        limit = ctx.author.voice.channel.user_limit or 0

        if limit == 0:
            await ctx.send("Channel member limit must be greater than **0 members**")
            return

        await ctx.author.voice.channel.edit(
            user_limit=limit - 1,
            reason=f"VoiceMeister: {ctx.author} decreased voice channel user limit",
        )
        if (limit - 1) == 0:
            await ctx.send("Your **voice channel**'s limit has been **removed**")
        else:
            await ctx.send(f"Your **voice channel**'s limit has been updated to `{limit - 1}`")

    @commands.command(name="delete")
    async def delete_channel(self, ctx: commands.Context):
        """Delete your voice channel."""
        await ctx.author.voice.channel.delete(reason=f"VoiceMeister: {ctx.author} deleted their voice channel")
        await ctx.send("Your **voice channel** has been deleted")

    @commands.command(name="create_text")
    async def create_text_channel(self, ctx: commands.Context):
        """Create a text channel linked to your voice channel."""
        category = ctx.author.voice.channel.category
        text_channel = await category.create_text_channel(f"{ctx.author.display_name}-text")
        await ctx.send(f"Text channel {text_channel.mention} created for your voice channel")

    @commands.command(name="reset")
    @commands.admin_or_permissions(administrator=True)
    async def reset_configurations(self, ctx: commands.Context):
        """Reset all VoiceMeister configurations."""
        await self.config.guild(ctx.guild).clear()
        await ctx.send("All **VoiceMeister** configurations have been reset")
