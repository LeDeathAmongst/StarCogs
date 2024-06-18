import discord
from redbot.core import Config, commands

class StaffManager(commands.Cog):
    """Cog for managing staff members in a Discord server."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier="staffmanager", force_registration=True)
        self.config.register_global(staff_updates_channel=None, blacklist_channel=None)

    async def send_channel_not_set_message(self, ctx, command_name):
        """Send a message indicating that the required channel is not set."""
        if command_name == "staffblacklist":
            await ctx.send("Oops, you forgot to set the Blacklist channel! Make sure you set it with `[p]setblacklist`.")
        else:
            await ctx.send("Oops, you forgot to set the Staff Updates channel! Make sure you set it with `[p]setupdates`.")
        
    async def channel_is_set(self):
        """Check if the required channels are set."""
        staff_updates_channel = await self.config.staff_updates_channel()
        blacklist_channel = await self.config.blacklist_channel()
        if staff_updates_channel is None or blacklist_channel is None:
            return False
        return True
        
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setupdates(self, ctx, channel: discord.TextChannel):
        """Set the channel for staff update messages."""
        # Check if the channel is already set
        if await self.config.channel_is_set(ctx):
            await ctx.send(f"The Staff updates channel is already set to {channel.mention}")
            return

        # Set the new channel
        await self.config.staff_updates_channel.set(channel.id)
        await ctx.send(f"Staff updates channel set to {channel.mention}")


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setblacklist(self, ctx, channel: discord.TextChannel):
        """Set the channel for blacklist messages."""
        await self.config.blacklist_channel.set(channel.id)
        await ctx.send(f"Blacklist channel set to {channel.mention}")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unsetupdates(self, ctx):
        """Unset the staff updates channel."""
        await self.config.staff_updates_channel.set(None)
        await ctx.send("Staff updates channel has been unset.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unsetblacklist(self, ctx):
        """Unset the blacklist channel."""
        await self.config.blacklist_channel.set(None)
        await ctx.send("Blacklist channel has been unset.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handle command errors."""
        if isinstance(error, commands.CheckFailure):
            await self.send_channel_not_set_message(ctx, ctx.command.name)

    async def channel_is_set(self, ctx):
        """Check if the required channels are set."""
        staff_updates_channel = await self.config.staff_updates_channel()
        blacklist_channel = await self.config.blacklist_channel()
        if staff_updates_channel is None or blacklist_channel is None:
            return False
        return True

    async def send_channel_not_set_message(self, ctx, command_name):
        """Send a message indicating that a required channel is not set."""
        await ctx.send(f"The required channel for the `{command_name}` command is not set. Please set it first.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def fire(self, ctx, member: discord.Member, role: discord.Role):
        """Fire a staff member."""
        if not await self.channel_is_set(ctx):
            await self.send_channel_not_set_message(ctx, "fire")
            return

        await member.remove_roles(role)
        embed = discord.Embed(title="Staff Fired", color=discord.Color.red())
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="User ID", value=member.id, inline=False)
        channel_id = await self.config.staff_updates_channel()
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
        else:
            await self.send_channel_not_set_message(ctx, "fire")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def hire(self, ctx, member: discord.Member, role: discord.Role):
        """Hire a new staff member."""
        if not await self.channel_is_set(ctx):
            await self.send_channel_not_set_message(ctx, "hire")
            return

        await member.add_roles(role)
        embed = discord.Embed(title="Staff Hired", color=discord.Color.green())
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="User ID", value=member.id, inline=False)
        channel_id = await self.config.staff_updates_channel()
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
        else:
            await self.send_channel_not_set_message(ctx, "hire")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def demote(self, ctx, member: discord.Member, old_role: discord.Role, new_role: discord.Role):
        """Demote a staff member."""
        if not await self.channel_is_set(ctx):
            await self.send_channel_not_set_message(ctx, "demote")
            return

        await member.remove_roles(old_role)
        await member.add_roles(new_role)
        embed = discord.Embed(title="Staff Demoted", color=discord.Color.orange())
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="User ID", value=member.id, inline=False)
        channel_id = await self.config.staff_updates_channel()
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
        else:
            await self.send_channel_not_set_message(ctx, "demote")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def staffblacklist(self, ctx, member: discord.Member, reason: str, proof: str):
        """Blacklist a staff member."""
        if not await self.channel_is_set(ctx):
            await self.send_channel_not_set_message(ctx, "staffblacklist")
            return
        # Send a DM to the member before banning them
        try:
            await member.send(f"You have been blacklisted from {ctx.guild.name} for: {reason}. If you wish to appeal, please contact {ctx.guild.owner.mention} or the Support team.")
        except discord.Forbidden:
            await ctx.send(f"Failed to send a DM to {member.name}. They will still be blacklisted.")

        # Ban the member
        await member.ban(reason=reason)

        # Send an embed message to the blacklist_channel
        embed = discord.Embed(title="Staff Blacklisted", color=discord.Color.dark_red())
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="User ID", value=member.id, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Proof", value=proof, inline=False)
        channel_id = await self.config.blacklist_channel()
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
        else:
            await self.send_channel_not_set_message(ctx, "staffblacklist")

# Define the check function outside the class
async def channel_is_set(ctx):
    """Check if the required channels are set."""
    staff_updates_channel = await ctx.bot.get_cog("StaffManager").config.staff_updates_channel()
    blacklist_channel = await ctx.bot.get_cog("StaffManager").config.blacklist_channel()
    if staff_updates_channel is None or blacklist_channel is None:
        return False
    return True

def setup(bot):
    bot.add_cog(StaffManager(bot))
