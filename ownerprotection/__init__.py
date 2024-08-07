from redbot.core.bot import Red
from .ownerprotection import OwnerProtection

async def setup(bot: Red):
    cog = OwnerProtection(bot)
    await cog.cog_load()
    bot.add_cog(cog)
