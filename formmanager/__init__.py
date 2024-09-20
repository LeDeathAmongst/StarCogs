from Star_Utils import Cog
from redbot.core.bot import Red
from .formmanager import FormManager


async def setup(bot):
    await bot.add_cog(FormManager(bot))
