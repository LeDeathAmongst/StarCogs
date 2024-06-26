import discord
import aiohttp
import asyncio
import random
from redbot.core import commands, Config, checks
from redbot.core.bot import Red
from datetime import datetime, timedelta
import pytz

class RandomTopic(commands.Cog):
    """A cog to revive dead chats with random trivia questions."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        self.config.register_guild(
            role_id=None,
            channel_id=None,
            custom_name="Random Topic",
            scheduled_hour=None,
            scheduled_minute=None,
            scheduled_period=None,
            last_sent=None
        )
        self.session = aiohttp.ClientSession()
        self.timezone = pytz.timezone("US/Eastern")

    def cog_unload(self):
        asyncio.create_task(self.session.close())

    @commands.group()
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def rt(self, ctx):
        """Commands to configure Random Topic."""
        pass

    @rt.command()
    async def setrole(self, ctx, role: discord.Role):
        """Set the role to be pinged when a new topic is posted.

        Use this command to specify which role should be mentioned whenever a new random topic is generated and sent to the channel.
        """
        await self.config.guild(ctx.guild).role_id.set(role.id)
        await ctx.send(f"Role set to {role.name}", allowed_mentions=discord.AllowedMentions(roles=True))

    @rt.command()
    async def setchannel(self, ctx, channel: discord.TextChannel):
        """Set the channel where random topics will be sent.

        Use this command to specify which text channel the bot should use to send the random topics. Make sure to mention the channel.
        """
        await self.config.guild(ctx.guild).channel_id.set(channel.id)
        await ctx.send(f"Channel set to {channel.name}")

    @rt.command()
    async def setname(self, ctx, *, name: str):
        """Set a custom name for the Random Topic messages.

        Use this command to customize the name that will appear in the random topic messages. This can help personalize the bot's messages for your server.
        """
        await self.config.guild(ctx.guild).custom_name.set(name)
        await ctx.send(f"Custom name set to {name}")

    @rt.command()
    async def settime(self, ctx, hour: int, minute: int, period: str):
        """Set the time for daily topic posting (hour and minute in 12-hour format with AM/PM).

        Use this command to schedule a daily time for the bot to automatically send a random topic.
        The hour should be in 12-hour format (e.g., 2 for 2 PM) and the period should be 'AM' or 'PM'.
        """
        if period.upper() not in ["AM", "PM"]:
            return await ctx.send("Invalid period. Please use 'AM' or 'PM'.")

        if not (0 <= minute < 60):
            return await ctx.send("Invalid minute. Please use a value between 0 and 59.")

        await self.config.guild(ctx.guild).scheduled_hour.set(hour)
        await self.config.guild(ctx.guild).scheduled_minute.set(minute)
        await self.config.guild(ctx.guild).scheduled_period.set(period.upper())
        await ctx.send(f"Scheduled time set to {hour}:{minute:02d} {period.upper()} Eastern Time")

    @rt.command()
    async def sendtopic(self, ctx):
        """Send a random topic immediately.

        Use this command to manually trigger the bot to send a random topic to the configured channel. This can be useful if you want to revive a dead chat instantly.
        """
        await self.send_random_topic(ctx.guild)

    async def send_random_topic(self, guild: discord.Guild):
        role_id = await self.config.guild(guild).role_id()
        channel_id = await self.config.guild(guild).channel_id()
        custom_name = await self.config.guild(guild).custom_name()

        if channel_id is None:
            return

        channel = guild.get_channel(channel_id)
        if channel is None:
            return

        try:
            async with self.session.get("https://the-trivia-api.com/api/questions?limit=1") as resp:
                if resp.status != 200:
                    await channel.send("Failed to retrieve a random topic. Please try again later.")
                    return
                data = await resp.json()
                question = data[0]['question']
        except aiohttp.ClientError as e:
            await channel.send("There was an error connecting to the random topic service. Please try again later.")
            return

        role_mention = f"<@&{role_id}>" if role_id else ""
        prefix = (await self.bot.get_valid_prefixes(guild))[0]
        message = (
            f"If you want a new topic, run this command: `{prefix}rt sendtopic`"
        )

        embed = discord.Embed(
            title=custom_name,
            color=random.randint(0, 0xFFFFFF)
        )
        embed.add_field(name="Question", value=question, inline=False)
        embed.set_footer(text=message)

        if role_mention:
            await channel.send(role_mention, allowed_mentions=discord.AllowedMentions(roles=True))
        await channel.send(embed=embed)

    async def scheduled_task(self):
        await self.bot.wait_until_ready()
        while True:
            now = datetime.now(self.timezone)
            for guild in self.bot.guilds:
                scheduled_hour = await self.config.guild(guild).scheduled_hour()
                scheduled_minute = await self.config.guild(guild).scheduled_minute()
                scheduled_period = await self.config.guild(guild).scheduled_period()
                last_sent = await self.config.guild(guild).last_sent()

                if scheduled_hour is None or scheduled_minute is None or scheduled_period is None:
                    continue

                if scheduled_period == "PM" and scheduled_hour != 12:
                    scheduled_hour += 12
                elif scheduled_period == "AM" and scheduled_hour == 12:
                    scheduled_hour = 0

                scheduled_datetime = self.timezone.localize(datetime(
                    now.year, now.month, now.day, scheduled_hour, scheduled_minute
                ))
                if last_sent:
                    last_sent = datetime.strptime(last_sent, "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.utc).astimezone(self.timezone)
                else:
                    last_sent = now - timedelta(days=1)

                if now >= scheduled_datetime > last_sent:
                    await self.send_random_topic(guild)
                    await self.config.guild(guild).last_sent.set(now.strftime("%Y-%m-%d %H:%M:%S"))

            await asyncio.sleep(60)

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.scheduled_task())
