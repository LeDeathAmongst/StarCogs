from redbot.core.bot import Red

from .voicemeister import VoiceMeister

async def setup(bot):
    await bot.add_cog(VoiceMeister(bot))
