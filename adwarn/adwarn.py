import discord
from redbot.core import commands, Config
from redbot.core.bot import Red

class AdWarn(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)  # Replace with a unique identifier
        self.config.register_guild(warn_channel=None)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def adwarn(self, ctx, user: discord.Member, channel: discord.TextChannel, *, reason: str):
        """Warn a user and send an embed to the default warning channel."""
        warn_channel_id = await self.config.guild(ctx.guild).warn_channel()
        if warn_channel_id:
            warn_channel = self.bot.get_channel(warn_channel_id)
            if warn_channel:
                # Create the embed message
                embed = discord.Embed(title="You were warned!", color=discord.Color.red())
                embed.add_field(name="User", value=user.mention, inline=True)
                embed.add_field(name="In", value=channel.mention, inline=True)
                embed.add_field(name="Reason", value=reason, inline=False)

                # Send the embed to the specified warning channel
                await warn_channel.send(embed=embed)
            else:
                await ctx.send("Warning channel not found. Please set it again using `[p]warnset channel`.")
        else:
            await ctx.send("No warning channel has been set. Please set it using `[p]warnset channel`.")

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def warnset(self, ctx):
        """Settings for the warning system."""
        pass

    @warnset.command()
    async def channel(self, ctx, channel: discord.TextChannel):
        """Set the default channel for warnings."""
        await self.config.guild(ctx.guild).warn_channel.set(channel.id)
        await ctx.send(f"Warning channel has been set to {channel.mention}")

    @warnset.command()
    async def show(self, ctx):
        """Show the current warning channel."""
        channel_id = await self.config.guild(ctx.guild).warn_channel()
        if channel_id:
            channel = self.bot.get_channel(channel_id)
            await ctx.send(f"The current warning channel is {channel.mention}")
        else:
            await ctx.send("No warning channel has been set.")

def setup(bot: Red):
    bot.add_cog(AdWarn(bot))
