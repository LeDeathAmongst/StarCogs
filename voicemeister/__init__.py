from redbot.core.bot import Red

from .voicemeister import Interface
from .voicemeister import VoiceMeister

async def setup(bot: Red):
    await bot.add_cog(Interface(bot))
    await bot.add_cog(VoiceMeister(bot))
