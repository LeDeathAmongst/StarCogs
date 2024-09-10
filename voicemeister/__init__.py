import importlib
import sys
from redbot.core import errors
from redbot.core.bot import Red
from redbot.core.utils import get_end_user_data_statement
from .voicemeister import VoiceMeister
from .c_voicemeister import VoiceMeisterCommands
from .c_voicemeisterset import VoiceMeisterSet
from .vminterface import VMInterface

# Ensure Star_Utils is available
try:
    import Star_Utils
except ModuleNotFoundError:
    raise errors.CogLoadError(
        "The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/LeDeathAmongst/Star_Utils.git`. A restart of the bot isn't necessary."
    )

# Reload Star_Utils modules
modules = sorted([module for module in sys.modules if module.split('.')[0] == 'Star_Utils'], reverse=True)
for module in modules:
    try:
        importlib.reload(sys.modules[module])
    except ModuleNotFoundError:
        pass
del Star_Utils

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)

async def setup(bot: Red) -> None:
    voicemeister_cog = VoiceMeister(bot)
    voicemeister_commands_cog = VoiceMeisterCommands(bot)
    voicemeister_set_cog = VoiceMeisterSet(bot)
    vm_interface = VMInterface(bot)

    await bot.add_cog(voicemeister_cog)
    await bot.add_cog(voicemeister_commands_cog)
    await bot.add_cog(voicemeister_set_cog)
