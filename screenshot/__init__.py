from redbot.core import errors  # isort:skip
import importlib
import sys

try:
    import Star_Utils  # Attempt to import Star_Utils
except ModuleNotFoundError:
    raise errors.CogLoadError(
        "The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/LeDeathAmongst/Star_Utils.git`. A restart of the bot isn't necessary."
    )

# Reload Star_Utils modules if they are already loaded
modules = sorted(
    [module for module in sys.modules if module.split(".")[0] == "Star_Utils"], reverse=True
)
for module in modules:
    try:
        importlib.reload(sys.modules[module])
    except ModuleNotFoundError:
        pass
del Star_Utils

# Import Red and get_end_user_data_statement
from redbot.core.bot import Red  # isort:skip
from redbot.core.utils import get_end_user_data_statement

from .autodocsite import Screenshot  # Import your cog

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)

async def setup(bot: Red) -> None:
    cog = Screenshot(bot)

    await bot.add_cog(cog)
