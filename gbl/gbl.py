import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from Star_Utils import Cog, CogsUtils, Settings, Buttons, Menu
import sqlite3
import asyncio
from datetime import datetime

class UserOrID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            return await commands.UserConverter().convert(ctx, argument)
        except commands.UserNotFound:
            try:
                return int(argument)
            except ValueError:
                raise commands.BadArgument("Not a valid user or user ID.")

class AppealModal(discord.ui.Modal, title='Global Ban Appeal'):
    understand = discord.ui.TextInput(label='Do you understand why you were banned?', style=discord.TextStyle.paragraph)
    why_unban = discord.ui.TextInput(label='Why should you be unbanned?', style=discord.TextStyle.paragraph)
    steps = discord.ui.TextInput(label='What steps will you take to prevent future bans?', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        appeal_text = f"Understanding: {self.understand.value}\n\nReason for unban: {self.why_unban.value}\n\nPreventive steps: {self.steps.value}"
        await interaction.client.get_cog('GlobalBanList').submit_appeal(interaction.user, appeal_text)
        await interaction.response.send_message("Your appeal has been submitted for review.", ephemeral=True)

class DynamicListView(discord.ui.View):
    def __init__(self, cog, list_name):
        super().__init__(timeout=None)
        self.cog = cog
        self.list_name = list_name

    @discord.ui.button(label="Refresh", style=discord.ButtonStyle.green)
    async def refresh(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.update_embed(interaction)

    async def update_embed(self, interaction: discord.Interaction):
        embed = await self.cog.create_list_embed(self.list_name)
        await interaction.message.edit(embed=embed)

class GlobalBanList(Cog):
    """A complex cog for managing global ban lists across multiple Discord servers."""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(
            authorized_users=[],
            ban_appeal_channel=None,
            appeal_cooldown_days=30,
            owner_log_channel=None
        )
        self.config.register_guild(
            subscribed_lists=[],
            auto_ban=True,
            notify_channel=None,
            exempt_roles=[],
            general_log_channel=None
        )

        self.db = sqlite3.connect("globalbanlist.db")
        self.cursor = self.db.cursor()
        self.setup_database()

    async def cog_load(self):
        await super().cog_load()
        self.bot.loop.create_task(self.periodic_check())

    def setup_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ban_lists
                              (list_name TEXT PRIMARY KEY)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS banned_users
                              (user_id INTEGER, list_name TEXT, reason TEXT, proof TEXT, banned_at TIMESTAMP,
                               FOREIGN KEY(list_name) REFERENCES ban_lists(list_name),
                               PRIMARY KEY(user_id, list_name))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ban_appeals
                              (user_id INTEGER, appeal_text TEXT, appealed_at TIMESTAMP,
                               PRIMARY KEY(user_id))''')
        self.db.commit()

    @commands.group(name="globalbanlistowner", aliases=["gblo"])
    @commands.is_owner()
    async def gblo(self, ctx: commands.Context):
        """Group command for Global Ban List owner settings."""
        pass

    @gblo.command(name="addauth")
    async def addauth(self, ctx: commands.Context, user: discord.User):
        """Add a user to the authorized users list."""
        async with self.config.authorized_users() as authorized:
            if user.id not in authorized:
                authorized.append(user.id)
                await ctx.send(f"{user.name} has been added to the authorized users list.")
                await self.owner_log("Add Authorized User", ctx.author, f"Added {user.name} to authorized users")
            else:
                await ctx.send(f"{user.name} is already in the authorized users list.")

    @gblo.command(name="remauth")
    async def remauth(self, ctx: commands.Context, user: discord.User):
        """Remove a user from the authorized users list."""
        async with self.config.authorized_users() as authorized:
            if user.id in authorized:
                authorized.remove(user.id)
                await ctx.send(f"{user.name} has been removed from the authorized users list.")
                await self.owner_log("Remove Authorized User", ctx.author, f"Removed {user.name} from authorized users")
            else:
                await ctx.send(f"{user.name} is not in the authorized users list.")

    @gblo.command(name="setappealchannel")
    async def setappealchannel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        """Set the channel for ban appeals."""
        if channel is None:
            await self.config.ban_appeal_channel.clear()
            await ctx.send("Ban appeal channel has been cleared.")
        else:
            await self.config.ban_appeal_channel.set(channel.id)
            await ctx.send(f"Ban appeal channel has been set to {channel.mention}.")
        await self.owner_log("Set Appeal Channel", ctx.author, f"Set appeal channel to {channel.mention if channel else 'None'}")

    @gblo.command(name="setownerlog")
    async def setownerlog(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for owner logging."""
        await self.config.owner_log_channel.set(channel.id)
        await ctx.send(f"Owner log channel has been set to {channel.mention}.")
        await self.owner_log("Set Owner Log Channel", ctx.author, f"Set owner log channel to {channel.mention}")

    @gblo.command(name="displaylist")
    async def displaylist(self, ctx: commands.Context, list_name: str):
        """Display a dynamically updating embed for a specific ban list."""
        embed = await self.create_list_embed(list_name)
        view = DynamicListView(self, list_name)
        await ctx.send(embed=embed, view=view)

    @commands.hybrid_group(name="globalbanlist", aliases=["gbl"])
    async def gbl(self, ctx: commands.Context):
        """Manage the global ban list."""
        pass

    @gbl.command(name="add")
    async def add_user(self, ctx: commands.Context, user: UserOrID, group: str, reason: str, proof: str):
        """Add a user to a specific ban list."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        user_id = user.id if isinstance(user, discord.User) else user
        user_obj = self.bot.get_user(user_id) or await self.bot.fetch_user(user_id)

        self.cursor.execute("INSERT OR IGNORE INTO ban_lists (list_name) VALUES (?)", (group,))
        self.cursor.execute("INSERT OR REPLACE INTO banned_users (user_id, list_name, reason, proof, banned_at) VALUES (?, ?, ?, ?, ?)",
                            (user_id, group, reason, proof, datetime.utcnow()))
        self.db.commit()
        await ctx.send(f"User ID {user_id} has been added to the {group} list.")
        await self.check_subscribed_servers(user_id, group)
        await self.update_list_embeds(group)

        await self.owner_log("Add to Ban List", ctx.author, f"Added {user_obj} to {group} list")

    @gbl.command(name="remove")
    async def remove_user(self, ctx: commands.Context, user: UserOrID, group: str):
        """Remove a user from a specific ban list."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        user_id = user.id if isinstance(user, discord.User) else user
        user_obj = self.bot.get_user(user_id) or await self.bot.fetch_user(user_id)

        self.cursor.execute("DELETE FROM banned_users WHERE user_id = ? AND list_name = ?", (user_id, group))
        self.db.commit()
        await ctx.send(f"User ID {user_id} has been removed from the {group} list.")
        await self.update_list_embeds(group)

        await self.owner_log("Remove from Ban List", ctx.author, f"Removed {user_obj} from {group} list")

    @gbl.command(name="list")
    async def list_users(self, ctx: commands.Context, group: str = None):
        """List all users in a specific ban list or show available lists."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if group is None:
            # Show available lists
            self.cursor.execute("SELECT list_name FROM ban_lists")
            lists = self.cursor.fetchall()
            if not lists:
                await ctx.send("There are no ban lists available.")
                return
            lists_str = "\n".join([f"- {list_name[0]}" for list_name in lists])
            embed = discord.Embed(title="Available Ban Lists", description=lists_str, color=discord.Color.blue())
            await ctx.send(embed=embed)
            return

        # Check if the specified list exists
        self.cursor.execute("SELECT 1 FROM ban_lists WHERE list_name = ?", (group,))
        if not self.cursor.fetchone():
            await ctx.send(f"The list '{group}' does not exist. Use `{ctx.prefix}gbl list` to see available lists.")
            return

        self.cursor.execute("SELECT user_id, reason, proof, banned_at FROM banned_users WHERE list_name = ?", (group,))
        users = self.cursor.fetchall()

        if not users:
            await ctx.send(f"No users found in the {group} list.")
            return

        pages = []
        for i in range(0, len(users), 5):
            embed = discord.Embed(title=f"Users in {group} list", color=discord.Color.red())
            for user_id, reason, proof, banned_at in users[i:i+5]:
                user = self.bot.get_user(user_id) or await self.bot.fetch_user(user_id)
                embed.add_field(name=f"{user} ({user_id})", value=f"Reason: {reason}\nProof: {proof}\nBanned at: {banned_at}", inline=False)
            pages.append(embed)

        await Menu(pages=pages).start(ctx)

    @gbl.command(name="subscribe")
    @commands.has_permissions(administrator=True)
    async def subscribe(self, ctx: commands.Context, list_name: str):
        """Subscribe to a specific ban list."""
        async with self.config.guild(ctx.guild).subscribed_lists() as subscribed:
            if list_name not in subscribed:
                subscribed.append(list_name)
                await ctx.send(f"This server has been subscribed to the {list_name} list.")
                await self.owner_log("Subscribe", ctx.author, f"Subscribed to {list_name} list in {ctx.guild.name}")
            else:
                await ctx.send(f"This server is already subscribed to the {list_name} list.")

    @gbl.command(name="unsubscribe")
    @commands.has_permissions(administrator=True)
    async def unsubscribe(self, ctx: commands.Context, list_name: str):
        """Unsubscribe from a specific ban list."""
        async with self.config.guild(ctx.guild).subscribed_lists() as subscribed:
            if list_name in subscribed:
                subscribed.remove(list_name)
                await ctx.send(f"This server has been unsubscribed from the {list_name} list.")
                await self.owner_log("Unsubscribe", ctx.author, f"Unsubscribed from {list_name} list in {ctx.guild.name}")
            else:
                await ctx.send(f"This server is not subscribed to the {list_name} list.")

    @gbl.command(name="setgenerallog")
    @commands.has_permissions(administrator=True)
    async def setgenerallog(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for general logging in this server."""
        await self.config.guild(ctx.guild).general_log_channel.set(channel.id)
        await ctx.send(f"General log channel for this server has been set to {channel.mention}.")

    @gbl.command()
    async def appeal(self, ctx: commands.Context):
        """Submit an appeal for a global ban."""
        self.cursor.execute("SELECT 1 FROM banned_users WHERE user_id = ?", (ctx.author.id,))
        if not self.cursor.fetchone():
            await ctx.send("You are not on any global ban list.")
            return

        appeal_modal = AppealModal()
        await ctx.send_modal(appeal_modal)

    async def submit_appeal(self, user: discord.User, appeal_text: str):
        """Submit the appeal to the database and notify the appeal channel."""
        self.cursor.execute("INSERT OR REPLACE INTO ban_appeals (user_id, appeal_text, appealed_at) VALUES (?, ?, ?)",
                            (user.id, appeal_text, datetime.utcnow()))
        self.db.commit()
        await user.send("Your appeal has been submitted for review.")

        appeal_channel_id = await self.config.ban_appeal_channel()
        if appeal_channel_id:
            appeal_channel = self.bot.get_channel(appeal_channel_id)
            if appeal_channel:
                embed = discord.Embed(title="New Ban Appeal", color=discord.Color.blue())
                embed.add_field(name="User", value=f"{user} ({user.id})", inline=False)
                embed.add_field(name="Appeal", value=appeal_text, inline=False)

                buttons = Buttons(
                    timeout=600,
                    buttons=[
                        {"style": discord.ButtonStyle.green, "label": "Approve", "custom_id": "approve_appeal"},
                        {"style": discord.ButtonStyle.red, "label": "Deny", "custom_id": "deny_appeal"}
                    ],
                    members=[m.id for m in self.bot.owner_ids],
                    function=self.handle_appeal_decision
                )

                await appeal_channel.send(embed=embed, view=buttons)

        await self.owner_log("Appeal Submitted", user, f"Appeal text: {appeal_text}")

    async def handle_appeal_decision(self, view: Buttons, interaction: discord.Interaction):
        decision = "approved" if interaction.data["custom_id"] == "approve_appeal" else "denied"
        user_id = int(interaction.message.embeds[0].fields[0].value.split("(")[-1].split(")")[0])

        if decision == "approved":
            # Remove user from all ban lists
            self.cursor.execute("DELETE FROM banned_users WHERE user_id = ?", (user_id,))
            self.db.commit()

        user = self.bot.get_user(user_id)
        if user:
            await user.send(f"Your ban appeal has been {decision}.")

        await interaction.message.edit(content=f"Appeal {decision} by {interaction.user}", view=None)
        await self.owner_log("Appeal Decision", interaction.user, f"Appeal for user {user_id} was {decision}")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Check if a joining member is on any subscribed ban lists."""
        guild_config = await self.config.guild(member.guild).all()
        if not guild_config['auto_ban']:
            return

        self.cursor.execute("SELECT list_name, reason, proof FROM banned_users WHERE user_id = ?", (member.id,))
        bans = self.cursor.fetchall()

        for list_name, reason, proof in bans:
            if list_name in guild_config['subscribed_lists']:
                try:
                    await member.ban(reason=f"Global Ban List: {list_name} - {reason}")
                    if guild_config['notify_channel']:
                        channel = member.guild.get_channel(guild_config['notify_channel'])
                        if channel:
                            await channel.send(f"{member} was banned due to being on the {list_name} global ban list.")
                    await self.general_log(member.guild, "User Banned", member, list_name, reason, proof)
                except discord.Forbidden:
                    print(f"Failed to ban {member.name} from {member.guild.name} - Insufficient permissions")

    async def periodic_check(self):
        """Periodically check all servers for banned users."""
        while True:
            await asyncio.sleep(3600)  # Check every hour
            for guild in self.bot.guilds:
                guild_config = await self.config.guild(guild).all()
                if guild_config['auto_ban']:
                    await self.check_guild_members(guild, guild_config['subscribed_lists'])

    async def check_guild_members(self, guild: discord.Guild, subscribed_lists: list):
        """Check all members of a guild against subscribed ban lists."""
        for member in guild.members:
            self.cursor.execute("SELECT list_name, reason, proof FROM banned_users WHERE user_id = ? AND list_name IN ({})".format(
                ','.join('?' * len(subscribed_lists))), (member.id, *subscribed_lists))
            bans = self.cursor.fetchall()

            for list_name, reason, proof in bans:
                try:
                    await member.ban(reason=f"Global Ban List: {list_name} - {reason}")
                    guild_config = await self.config.guild(guild).all()
                    if guild_config['notify_channel']:
                        channel = guild.get_channel(guild_config['notify_channel'])
                        if channel:
                            await channel.send(f"{member} was banned due to being on the {list_name} global ban list.")
                    await self.general_log(guild, "User Banned", member, list_name, reason, proof)
                except discord.Forbidden:
                    print(f"Failed to ban {member.name} from {guild.name} - Insufficient permissions")

    async def check_subscribed_servers(self, user_id: int, group: str):
        """Check all subscribed servers for a newly banned user."""
        for guild in self.bot.guilds:
            guild_config = await self.config.guild(guild).all()
            if group in guild_config['subscribed_lists']:
                member = guild.get_member(user_id)
                if member:
                    try:
                        await member.ban(reason=f"Global Ban List: {group}")
                        if guild_config['notify_channel']:
                            channel = guild.get_channel(guild_config['notify_channel'])
                            if channel:
                                await channel.send(f"{member} was banned due to being added to the {group} global ban list.")
                        self.cursor.execute("SELECT reason, proof FROM banned_users WHERE user_id = ? AND list_name = ?", (user_id, group))
                        reason, proof = self.cursor.fetchone()
                        await self.general_log(guild, "User Banned", member, group, reason, proof)
                    except discord.Forbidden:
                        print(f"Failed to ban {member.name} from {guild.name} - Insufficient permissions")

    async def is_authorized(self, user: discord.User) -> bool:
        """Check if a user is authorized to manage the global ban list."""
        authorized_users = await self.config.authorized_users()
        return user.id in authorized_users or await self.bot.is_owner(user)

    async def owner_log(self, action: str, user: discord.User, details: str):
        """Log owner actions."""
        channel_id = await self.config.owner_log_channel()
        if not channel_id:
            return

        channel = self.bot.get_channel(channel_id)
        if not channel:
            return

        embed = discord.Embed(title="Owner Action Log", color=discord.Color.blue(), timestamp=datetime.utcnow())
        embed.add_field(name="Action", value=action, inline=False)
        embed.add_field(name="User", value=f"{user} ({user.id})", inline=False)
        embed.add_field(name="Details", value=details, inline=False)
        embed.set_footer(text=f"User ID: {user.id}")

        await channel.send(embed=embed)

    async def general_log(self, guild: discord.Guild, action: str, user: discord.User, list_name: str, reason: str, proof: str):
        """Log general actions for a specific guild."""
        channel_id = await self.config.guild(guild).general_log_channel()
        if not channel_id:
            return

        channel = guild.get_channel(channel_id)
        if not channel:
            return

        embed = discord.Embed(title="Global Ban List Log", color=discord.Color.red(), timestamp=datetime.utcnow())
        embed.add_field(name="Action", value=action, inline=False)
        embed.add_field(name="User", value=f"{user} ({user.id})", inline=False)
        embed.add_field(name="List", value=list_name, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Proof", value=proof, inline=False)
        embed.set_footer(text=f"User ID: {user.id}")

        await channel.send(embed=embed)

    async def create_list_embed(self, list_name: str):
        self.cursor.execute("SELECT user_id, reason, proof, banned_at FROM banned_users WHERE list_name = ? ORDER BY banned_at DESC", (list_name,))
        users = self.cursor.fetchall()

        embed = discord.Embed(title=f"Users in {list_name} list", color=discord.Color.red(), timestamp=datetime.utcnow())
        embed.set_footer(text=f"Total users: {len(users)}")

        if not users:
            embed.description = "No users found in this list."
            return embed

        for user_id, reason, proof, banned_at in users[:10]:  # Display top 10 most recent bans
            user = self.bot.get_user(user_id) or f"Unknown User ({user_id})"
            embed.add_field(
                name=f"{user}",
                value=f"Reason: {reason}\nProof: {proof}\nBanned at: {banned_at}",
                inline=False
            )

        if len(users) > 10:
            embed.set_footer(text=f"Showing 10 most recent out of {len(users)} total users")

        return embed

    async def update_list_embeds(self, list_name: str):
        for guild in self.bot.guilds:
            async for message in guild.text_channels.history(limit=None):
                if message.author == self.bot.user and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == f"Users in {list_name} list":
                        view = discord.utils.get(message.components, type=discord.ComponentType.view)
                        if isinstance(view, DynamicListView):
                            await view.update_embed(await self.bot.get_context(message))

    def cog_unload(self):
        self.db.close()
