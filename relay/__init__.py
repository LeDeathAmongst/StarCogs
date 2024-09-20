from Star_Utils import Cog
from redbot.core.bot import Red
from .relay import Relay


async def setup(bot):
    await bot.add_cog(Relay(bot))
