from Star_Utils import Cog
from redbot.core.bot import Red
from .eventlogger import EventLogger


async def setup(bot: Red):
    cog = EventLogger(bot)
    await bot.add_cog(cog)
