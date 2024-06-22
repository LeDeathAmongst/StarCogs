import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_timedelta
import asyncio

class Jail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_guild(jail_role=None, jail_channel=None, jailed_users={})

    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def setrole(self, ctx, role: discord.Role):
        """Set the jail role."""
        await self.config.guild(ctx.guild).jail_role.set(role.id)
        await ctx.send(f"Jail role set to {role.name}")

    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_channels=True)
    async def setjail(self, ctx, channel: discord.TextChannel):
        """Set the jail channel."""
        await self.config.guild(ctx.guild).jail_channel.set(channel.id)

        # Remove access of the jail role to all channels but the jail channel
        jail_role_id = await self.config.guild(ctx.guild).jail_role()
        if not jail_role_id:
            await ctx.send("Jail role is not set. Please set it first using `setrole`.")
            return
        jail_role = ctx.guild.get_role(jail_role_id)
        if not jail_role:
            await ctx.send("Jail role not found. Please set it again using `setrole`.")
            return

        for chan in ctx.guild.channels:
            if chan == channel:
                await chan.set_permissions(jail_role, read_messages=True, send_messages=True)
            else:
                await chan.set_permissions(jail_role, read_messages=False, send_messages=False)

        await ctx.send(f"Jail channel set to {channel.name} and permissions updated.")

    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def jail(self, ctx, user: discord.Member, time: str):
        """Jail a user for a specified time."""
        jail_role_id = await self.config.guild(ctx.guild).jail_role()
        jail_channel_id = await self.config.guild(ctx.guild).jail_channel()
        if not jail_role_id or not jail_channel_id:
            await ctx.send("Jail role or jail channel is not set. Please set them using `setrole` and `setjail`.")
            return
        jail_role = ctx.guild.get_role(jail_role_id)
        if not jail_role:
            await ctx.send("Jail role not found. Please set it again using `setrole`.")
            return

        # Parse time
        time_seconds = self.parse_time(time)
        if time_seconds is None:
            await ctx.send("Invalid time format. Please use a valid format like `1h`, `30m`, etc.")
            return

        # Save user's roles
        original_roles = [role.id for role in user.roles if role != ctx.guild.default_role]
        await self.config.guild(ctx.guild).jailed_users.set_raw(user.id, value=original_roles)

        # Remove all roles and add jail role
        await user.remove_roles(*[role for role in user.roles if role != ctx.guild.default_role])
        await user.add_roles(jail_role)

        await ctx.send(f"{user.mention} has been jailed for {humanize_timedelta(seconds=time_seconds)}.")

        # Wait for the specified time
        await asyncio.sleep(time_seconds)

        # Free the user after the time is up
        await self.free_user(ctx.guild, user)

    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def free(self, ctx, user: discord.Member):
        """Free a jailed user immediately."""
        await self.free_user(ctx.guild, user)
        await ctx.send(f"{user.mention} has been freed.")

    async def free_user(self, guild, user):
        jail_role_id = await self.config.guild(guild).jail_role()
        if not jail_role_id:
            return
        jail_role = guild.get_role(jail_role_id)
        if not jail_role:
            return

        # Remove jail role and restore original roles
        await user.remove_roles(jail_role)
        original_roles = await self.config.guild(guild).jailed_users.get_raw(user.id, default=[])
        roles = [guild.get_role(role_id) for role_id in original_roles if guild.get_role(role_id)]
        await user.add_roles(*roles)

        # Remove user from jailed users list
        await self.config.guild(guild).jailed_users.clear_raw(user.id)

    def parse_time(self, time_str):
        units = {'h': 3600, 'm': 60, 's': 1}
        try:
            return int(time_str[:-1]) * units[time_str[-1]]
        except (ValueError, KeyError):
            return None

def setup(bot):
    bot.add_cog(Jail(bot))
