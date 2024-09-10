from Star_Utils import Cog
from redbot.core.bot import Red
from .afk import AFK


async def setup(bot):
    await bot.add_cog(AFK(bot))
