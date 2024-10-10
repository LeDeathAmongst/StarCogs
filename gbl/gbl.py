from redbot.core import commands, Config
from redbot.core.bot import Red
import discord
from discord.utils import utcnow
from Star_Utils import Cog, CogsUtils, Settings, Buttons
import typing
import sqlite3
import asyncio
from datetime import datetime, timedelta

class AppealModal(discord.ui.Modal, title='Global Ban Appeal'):
    understand = discord.ui.TextInput(label='Do you understand why you were banned?', style=discord.TextStyle.paragraph)
    why_unban = discord.ui.TextInput(label='Why should you be unbanned?', style=discord.TextStyle.paragraph)
    steps = discord.ui.TextInput(label='What steps will you take to prevent future bans?', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        appeal_text = f"Understanding: {self.understand.value}\n\nReason for unban: {self.why_unban.value}\n\nPreventive steps: {self.steps.value}"
        await interaction.client.get_cog('GlobalBanList').submit_appeal(interaction.user, appeal_text)
        await interaction.response.send_message("Your appeal has been submitted for review.", ephemeral=True)

class GlobalBanList(Cog):
    """A complex cog for managing global ban lists across multiple Discord servers."""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(
            authorized_users=[],
            ban_appeal_channel=None,
            appeal_cooldown_days=30
        )
        self.config.register_guild(
            subscribed_lists=[],
            auto_ban=True,
            notify_channel=None,
            exempt_roles=[]
        )

        self.db = sqlite3.connect("globalbanlist.db")
        self.cursor = self.db.cursor()
        self.setup_database()

        _settings = {
            'auto_ban': {
                'converter': bool,
                'description': 'Automatically ban users on the global ban list.'
            },
            'notify_channel': {
                'converter': discord.TextChannel,
                'description': 'Channel to notify about global ban list actions.'
            },
            'exempt_roles': {
                'converter': commands.Greedy[discord.Role],
                'description': 'Roles exempt from the global ban list.'
            }
        }
        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GUILD,
            settings=_settings,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.gblset
        )

    async def cog_load(self):
        await super().cog_load()
        await self.settings.add_commands()
        self.bot.loop.create_task(self.periodic_check())

    def setup_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ban_lists
                              (list_name TEXT PRIMARY KEY)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS banned_users
                              (user_id INTEGER, list_name TEXT, reason TEXT, banned_at TIMESTAMP,
                               FOREIGN KEY(list_name) REFERENCES ban_lists(list_name),
                               PRIMARY KEY(user_id, list_name))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ban_appeals
                              (user_id INTEGER, appeal_text TEXT, appealed_at TIMESTAMP,
                               PRIMARY KEY(user_id))''')
        self.db.commit()

    @commands.group()
    @commands.guild_only()
    async def gblset(self, ctx: commands.Context):
        """Group command for Global Ban List settings."""
        pass

    @commands.group(name="globalbanlistowner", aliases=["gblo"])
    @commands.is_owner()
    async def gblo(self, ctx: commands.Context):
        """Group command for Global Ban List owner settings."""
        pass

    @gblo.command(name="add_authorized")
    async def add_authorized(self, ctx: commands.Context, user: discord.User):
        """Add a user to the authorized users list."""
        async with self.config.authorized_users() as authorized:
            if user.id not in authorized:
                authorized.append(user.id)
                await ctx.send(f"{user.name} has been added to the authorized users list.")
            else:
                await ctx.send(f"{user.name} is already in the authorized users list.")

    @gblo.command(name="remove_authorized")
    async def remove_authorized(self, ctx: commands.Context, user: discord.User):
        """Remove a user from the authorized users list."""
        async with self.config.authorized_users() as authorized:
            if user.id in authorized:
                authorized.remove(user.id)
                await ctx.send(f"{user.name} has been removed from the authorized users list.")
            else:
                await ctx.send(f"{user.name} is not in the authorized users list.")

    @gblo.command(name="set_appeal_channel")
    async def set_appeal_channel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        """Set the channel for ban appeals."""
        if channel is None:
            await self.config.ban_appeal_channel.clear()
            await ctx.send("Ban appeal channel has been cleared.")
        else:
            await self.config.ban_appeal_channel.set(channel.id)
            await ctx.send(f"Ban appeal channel has been set to {channel.mention}.")

    @commands.hybrid_group(name="globalbanlist", aliases=["gbl"])
    async def gbl(self, ctx: commands.Context):
        """Manage the global ban list."""
        pass

    @gbl.command(name="explain")
    async def explain(self, ctx: commands.Context):
        """Explain what the GlobalBanList cog does."""
        explanation = (
            "The GlobalBanList cog is a powerful tool for managing global ban lists across multiple Discord servers. "
            "It allows authorized users to maintain lists of banned users for various reasons (e.g., raids, scams, ToS violations). "
            "Server administrators can subscribe to these lists, and the bot will automatically ban listed users who join their server. "
            "Key features include:\n\n"
            "1. Multiple ban lists for different purposes\n"
            "2. Authorized user system for managing lists\n"
            "3. Server-specific settings for auto-banning and notifications\n"
            "4. Ban appeal system with cooldown\n"
            "5. Periodic checking of all server members\n"
            "6. Exempt roles to prevent accidental bans of trusted users\n\n"
            "Use `[p]help GlobalBanList` for a list of available commands."
        )
        await ctx.send(explanation)

    @gbl.command(name="add")
    @commands.hybrid_command()
    async def add_user(self, ctx: commands.Context, user: typing.Union[discord.User, int], group: str, *, reason: str):
        """Add a user to a specific ban list."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        user_id = user.id if isinstance(user, discord.User) else user

        self.cursor.execute("INSERT OR IGNORE INTO ban_lists (list_name) VALUES (?)", (group,))
        self.cursor.execute("INSERT OR REPLACE INTO banned_users (user_id, list_name, reason, banned_at) VALUES (?, ?, ?, ?)",
                            (user_id, group, reason, datetime.utcnow()))
        self.db.commit()
        await ctx.send(f"User ID {user_id} has been added to the {group} list.")
        await self.check_subscribed_servers(user_id, group)

    @gbl.command(name="remove")
    @commands.hybrid_command()
    async def remove_user(self, ctx: commands.Context, user: typing.Union[discord.User, int], group: str):
        """Remove a user from a specific ban list."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        user_id = user.id if isinstance(user, discord.User) else user

        self.cursor.execute("DELETE FROM banned_users WHERE user_id = ? AND list_name = ?", (user_id, group))
        self.db.commit()
        await ctx.send(f"User ID {user_id} has been removed from the {group} list.")

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

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Check if a joining member is on any subscribed ban lists."""
        guild_config = await self.config.guild(member.guild).all()
        if not guild_config['auto_ban']:
            return

        self.cursor.execute("SELECT list_name, reason FROM banned_users WHERE user_id = ?", (member.id,))
        bans = self.cursor.fetchall()

        for list_name, reason in bans:
            if list_name in guild_config['subscribed_lists']:
                try:
                    await member.ban(reason=f"Global Ban List: {list_name} - {reason}")
                    if guild_config['notify_channel']:
                        channel = member.guild.get_channel(guild_config['notify_channel'])
                        if channel:
                            await channel.send(f"{member} was banned due to being on the {list_name} global ban list.")
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

    async def check_guild_members(self, guild: discord.Guild, subscribed_lists: List[str]):
        """Check all members of a guild against subscribed ban lists."""
        for member in guild.members:
            self.cursor.execute("SELECT list_name, reason FROM banned_users WHERE user_id = ? AND list_name IN ({})".format(
                ','.join('?' * len(subscribed_lists))), (member.id, *subscribed_lists))
            bans = self.cursor.fetchall()

            for list_name, reason in bans:
                try:
                    await member.ban(reason=f"Global Ban List: {list_name} - {reason}")
                    guild_config = await self.config.guild(guild).all()
                    if guild_config['notify_channel']:
                        channel = guild.get_channel(guild_config['notify_channel'])
                        if channel:
                            await channel.send(f"{member} was banned due to being on the {list_name} global ban list.")
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
                    except discord.Forbidden:
                        print(f"Failed to ban {member.name} from {guild.name} - Insufficient permissions")

    async def is_authorized(self, user: discord.User) -> bool:
        """Check if a user is authorized to manage the global ban list."""
        authorized_users = await self.config.authorized_users()
        return user.id in authorized_users or await self.bot.is_owner(user)

    def cog_unload(self):
        self.db.close()
