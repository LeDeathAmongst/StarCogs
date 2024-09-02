import discord
import asyncio
from redbot.core import commands, Config
from redbot.core.bot import Red
from typing import Dict
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

class TransferOwnership(discord.ui.Select):
    def __init__(self, member: discord.Member):
        self.member = member
        self.guild = member.guild
        self.channel = member.voice.channel
        options = [
            discord.SelectOption(
                value=str(m.id),
                label=f"{m} ({m.id})"
            )
            for m in self.channel.members if m != member
        ]
        super().__init__(placeholder="Choose a member to transfer ownership...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        member_id = int(self.values[0])
        new_owner = self.guild.get_member(member_id)
        if new_owner:
            await self.channel.set_permissions(new_owner, connect=True, read_messages=True)
            await self.channel.set_permissions(self.member, overwrite=None)
            await interaction.response.send_message(f"Ownership transferred to {new_owner.mention}.", ephemeral=True)
        else:
            await interaction.response.send_message("Failed to transfer ownership.", ephemeral=True)

class ActivitySelection(discord.ui.Select):
    def __init__(self, member: discord.Member):
        self.member = member
        self.guild = member.guild
        self.channel = member.voice.channel
        options = [
            discord.SelectOption(
                value=str(activity_id),
                label=activity_name
            )
            for activity_name, activity_id in popular_activities.items()
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

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:lock", emoji="<:Locked:1279848927587467447>")
    async def lock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            connect=False,
            reason=f"VoiceMeister: {interaction.user} locked voice channel",
        )
        await interaction.response.send_message("Your **voice channel** has been locked", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:unlock", emoji="<:Unlocked:1279848944570073109>")
    async def unlock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            connect=None,
            reason=f"VoiceMeister: {interaction.user} unlocked voice channel",
        )
        await interaction.response.send_message("Your **voice channel** has been unlocked", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:ghost", emoji="<:Crossed_Eye:1279848957475819723>")
    async def ghost(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            view_channel=False,
            reason=f"VoiceMeister: {interaction.user} made voice channel hidden",
        )
        await interaction.response.send_message("Your **voice channel** has been hidden", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:reveal", emoji="<:Eye:1279848986299076728>")
    async def reveal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.set_permissions(
            interaction.guild.default_role,
            view_channel=None,
            reason=f"VoiceMeister: {interaction.user} revealed voice channel",
        )
        await interaction.response.send_message("Your **voice channel** has been revealed", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:claim", emoji="<:Crown:1279848977658810451>")
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

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:disconnect", emoji="<:Hammer:1279848987922530365>")
    async def disconnect(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Interface(self.bot)
        view.add_item(DisconnectMembers(interaction.user))
        await interaction.response.send_message("Select members from the **dropdown** to disconnect.", view=view, ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:activity", emoji="<:Invite:1279857570634272818>")
    async def activity(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Interface(self.bot)
        view.add_item(ActivitySelection(interaction.user))
        await interaction.response.send_message("Select an activity from the **dropdown** to start!", view=view, ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:information", emoji="<:Information:1279848926383702056>")
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

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:increase", emoji="<:People:1279848931043573790>")
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

    @discord.ui.button(style=discord.ButtonStyle.grey, custom_id="voicemeister:decrease", emoji="<:People:1279848931043573790>")
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

    @discord.ui.button(style=discord.ButtonStyle.red, custom_id="voicemeister:delete", emoji="<:TrashCan:1279875131136806993>")
    async def delete_channel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.voice.channel.delete(reason=f"VoiceMeister: {interaction.user} deleted their voice channel")
        await interaction.response.send_message("Your **voice channel** has been deleted", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.blurple, custom_id="voicemeister:create_text", emoji="<:SpeachBubble:1279890650535428198>")
    async def create_text_channel(self, interaction: discord.Interaction, button: discord.ui.Button):
        category = interaction.user.voice.channel.category
        text_channel = await category.create_text_channel(f"{interaction.user.display_name}-text")
        await interaction.response.send_message(f"Text channel {text_channel.mention} created for your voice channel", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.red, custom_id="voicemeister:reset", emoji="<:reset:1280057459146362880>")
    async def reset_configurations(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.config.guild(interaction.guild).clear()
        await interaction.response.send_message("All **VoiceMeister** configurations have been reset", ephemeral=True)

    @discord.ui.select(placeholder="Transfer Ownership", options=[], custom_id="voicemeister:transfer")
    async def transfer_ownership(self, interaction: discord.Interaction, select: discord.ui.Select):
        view = Interface(self.bot)
        view.add_item(TransferOwnership(interaction.user))
        await interaction.response.send_message("Select a member from the **dropdown** to transfer ownership.", view=view, ephemeral=True)

class VoiceMeister(commands.Cog):
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

    @voicemeister.command(name="setup")
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

    @voicemeister.command(name="activityinvite")
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

    @voicemeister.command(name="setlimit")
    @commands.admin_or_permissions(manage_guild=True)
    async def setlimit(self, ctx: commands.Context, num: int):
        """Set the default channel limit for your server."""
        await self.config.guild(ctx.guild).set_raw("channel_limit", value=num)
        await ctx.send("You have changed the default channel limit for your server!")

    @voicemeister.command(name="lock")
    async def lock(self, ctx: commands.Context):
        """Lock your voice channel."""
        channel_id = await self.config.member(ctx.author).get_raw("channel_id", default=None)
        if channel_id is None:
            await ctx.send(f"{ctx.author.mention} You don't own a channel.")
            return

        channel = self.bot.get_channel(channel_id)
        await channel.set_permissions(ctx.guild.default_role, connect=False)
        await ctx.send(f'{ctx.author.mention} Voice chat locked!')

    @voicemeister.command(name="unlock")
    async def unlock(self, ctx: commands.Context):
        """Unlock your voice channel."""
        channel_id = await self.config.member(ctx.author).get_raw("channel_id", default=None)
        if channel_id is None:
            await ctx.send(f"{ctx.author.mention} You don't own a channel.")
            return

        channel = self.bot.get_channel(channel_id)
        await channel.set_permissions(ctx.guild.default_role, connect=True)
        await ctx.send(f'{ctx.author.mention} Voice chat unlocked!')

    @voicemeister.command(name="permit")
    async def permit(self, ctx: commands.Context, member: discord.Member):
        """Give a user permission to join your voice channel."""
        channel_id = await self.config.member(ctx.author).get_raw("channel_id", default=None)
        if channel_id is None:
            await ctx.send(f"{ctx.author.mention} You don't own a channel.")
            return

        channel = self.bot.get_channel(channel_id)
        await channel.set_permissions(member, connect=True)
        await ctx.send(f'{ctx.author.mention} You have permitted {member.name} to have access to the channel.')

    @voicemeister.command(name="reject")
    async def reject(self, ctx: commands.Context, member: discord.Member):
        """Remove a user's permission to join your voice channel."""
        channel_id = await self.config.member(ctx.author).get_raw("channel_id", default=None)
        if channel_id is None:
            await ctx.send(f"{ctx.author.mention} You don't own a channel.")
            return

        channel = self.bot.get_channel(channel_id)
        await channel.set_permissions(member, connect=False)
        await ctx.send(f'{ctx.author.mention} You have rejected {member.name} from accessing the channel.')

    @voicemeister.command(name="limit")
    async def limit(self, ctx: commands.Context, limit: int):
        """Set the user limit for your voice channel."""
        channel_id = await self.config.member(ctx.author).get_raw("channel_id", default=None)
        if channel_id is None:
            await ctx.send(f"{ctx.author.mention} You don't own a channel.")
            return

        channel = self.bot.get_channel(channel_id)
        await channel.edit(user_limit=limit)
        await ctx.send(f'{ctx.author.mention} You have set the channel limit to {limit}!')

    @voicemeister.command(name="name")
    async def name(self, ctx: commands.Context, *, name: str):
        """Change the name of your voice channel."""
        channel_id = await self.config.member(ctx.author).get_raw("channel_id", default=None)
        if channel_id is None:
            await ctx.send(f"{ctx.author.mention} You don't own a channel.")
            return

        channel = self.bot.get_channel(channel_id)
        await channel.edit(name=name)
        await ctx.send(f'{ctx.author.mention} You have changed the channel name to {name}!')

    @voicemeister.command(name="claim")
    async def claim(self, ctx: commands.Context):
        """Claim ownership of a voice channel if the owner has left."""
        channel = ctx.author.voice.channel
        if channel is None:
            await ctx.send(f"{ctx.author.mention} you're not in a voice channel.")
            return

        owner_id = await self.config.member_from_ids(ctx.guild.id, channel.id).get_raw("user_id", default=None)
        if owner_id is None or ctx.guild.get_member(owner_id) is not None:
            await ctx.send(f"{ctx.author.mention} This channel is already owned by someone!")
            return

        await self.config.member(ctx.author).set_raw("channel_id", value=channel.id)
        await ctx.send(f"{ctx.author.mention} You are now the owner of the channel!")
