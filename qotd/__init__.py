from Star_Utils import Cog
from redbot.core.bot import Red
from .qotd import QOTD


def setup(bot):
    bot.add_cog(QOTD(bot))
