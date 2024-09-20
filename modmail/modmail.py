import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from Star_Utils import Cog

class ModMail(Cog):
    """A modmail cog for Red-DiscordBot."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_guild = {
            "modmail_channel": None
        }
        self.config.register_guild(**default_guild)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or not isinstance(message.channel, discord.DMChannel):
            return

        # User sent a DM to the bot
        for guild in self.bot.guilds:
            modmail_channel_id = await self.config.guild(guild).modmail_channel()
            if not modmail_channel_id:
                continue

            modmail_channel = guild.get_channel(modmail_channel_id)
            if modmail_channel is None:
                continue

            # Create or get the thread for this user
            thread = await modmail_channel.create_thread(name=f"ModMail-{message.author.name}", type=discord.ChannelType.public_thread)
            embed = discord.Embed(
                title="New ModMail Message",
                description=message.content,
                color=discord.Color.blue()
            )
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
            await thread.send(embed=embed)
            break

    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    @commands.command()
    async def setmodmail(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the modmail channel for this server."""
        await self.config.guild(ctx.guild).modmail_channel.set(channel.id)
        await ctx.send(f"ModMail channel set to {channel.mention}")

    @commands.guild_only()
    @commands.mod_or_permissions(manage_messages=True)
    @commands.command()
    async def reply(self, ctx: commands.Context, user_id: int, *, response: str):
        user = self.bot.get_user(user_id)
        if user is None:
            await ctx.send("User not found.")
            return

        # Send the response to the user
        embed = discord.Embed(
            title="ModMail Reply",
            description=response,
            color=discord.Color.green()
        )
        await user.send(embed=embed)

        # Log the response in the thread
        modmail_channel_id = await self.config.guild(ctx.guild).modmail_channel()
        if modmail_channel_id:
            modmail_channel = ctx.guild.get_channel(modmail_channel_id)
            thread = discord.utils.get(modmail_channel.threads, name=f"ModMail-{user.display_name}")
            if thread:
                await thread.send(f"Reply sent to {user.mention}: {response}")
            else:
                await ctx.send("No active thread found for this user.")
        else:
            await ctx.send("ModMail channel not set.")

    @commands.guild_only()
    @commands.mod_or_permissions(manage_messages=True)
    @commands.command()
    async def close_thread(self, ctx: commands.Context, user_id: int):
        modmail_channel_id = await self.config.guild(ctx.guild).modmail_channel()
        if modmail_channel_id:
            modmail_channel = ctx.guild.get_channel(modmail_channel_id)
            thread = discord.utils.get(modmail_channel.threads, name=f"ModMail-{ctx.author.display_name}")
            if thread:
                await thread.send("This thread is now closed.")
                await thread.delete()
                await ctx.send("Thread closed successfully.")
            else:
                await ctx.send("No active thread found for this user.")
        else:
            await ctx.send("ModMail channel not set.")
