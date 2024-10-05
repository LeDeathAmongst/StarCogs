Star_Utils
==========

Commands to manage all the cogs in StarCogs repo!

# <@1275521742961508432>star_utils (Hybrid Command)
All commands to manage all the cogs from StarCogs repo.<br/>
 - Usage: `<@1275521742961508432>star_utils`
 - Slash Usage: `/star_utils`
 - Restricted to: `BOT_OWNER`
 - Aliases: `Star_Utils`


## <@1275521742961508432>star_utils senderrorwithsentry (Hybrid Command)
Send a recent error to the developer of Star's cogs with Sentry (use the code given when the error has been triggered).<br/>

More details: https://StarCogs.readthedocs.io/en/latest/repo_telemetry.html<br/>
 - Usage: `<@1275521742961508432>star_utils senderrorwithsentry <error>`
 - Slash Usage: `/star_utils senderrorwithsentry <error>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### error: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>star_utils resetconfig (Hybrid Command)
Reset Config for a cog from StarCogs.<br/>
 - Usage: `<@1275521742961508432>star_utils resetconfig <cog> [confirmation=False]`
 - Slash Usage: `/star_utils resetconfig <cog> [confirmation=False]`
 - Restricted to: `BOT_OWNER`
 - Aliases: `clearconfig`
Extended Arg Info
> ### cog: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>star_utils displaysentrymanualcommand (Hybrid Command)
Enable or disable displaying the command `<@1275521742961508432>Star_Utils senderrorwithsentry` in commands errors.<br/>

Defaults is `True`.<br/>
 - Usage: `<@1275521742961508432>star_utils displaysentrymanualcommand <state>`
 - Slash Usage: `/star_utils displaysentrymanualcommand <state>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>star_utils getallfor (Hybrid Command)
Get all the necessary information to get support on a bot/repo/cog/command.<br/>
With a html file.<br/>
 - Usage: `<@1275521742961508432>star_utils getallfor [all=None] [page=None] [repo=None] [check_updates=False] [cog=None] [command=None]`
 - Slash Usage: `/star_utils getallfor [all=None] [page=None] [repo=None] [check_updates=False] [cog=None] [command=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### page: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### repo: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### check_updates: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### command: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>star_utils telemetrywithsentry (Hybrid Command)
Enable or disable Telemetry with Sentry for all cogs from StarCogs.<br/>

More details: https://StarCogs.readthedocs.io/en/latest/repo_telemetry.html<br/>
 - Usage: `<@1275521742961508432>star_utils telemetrywithsentry <state>`
 - Slash Usage: `/star_utils telemetrywithsentry <state>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>star_utils flags (Hybrid Command)
Use any command with flags.<br/>
 - Usage: `<@1275521742961508432>star_utils flags <content>`
 - Slash Usage: `/star_utils flags <content>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### content: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>star_utils getdebugloopsstatus (Hybrid Command)
Get debug loops status for a cog from StarCogs.<br/>
 - Usage: `<@1275521742961508432>star_utils getdebugloopsstatus <cog>`
 - Slash Usage: `/star_utils getdebugloopsstatus <cog>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### cog: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>star_utils replacementvarpaths (Hybrid Command)
Replace various var paths in texts sent by cog from StarCogs.<br/>

Defaults is `True`.<br/>
 - Usage: `<@1275521742961508432>star_utils replacementvarpaths <state>`
 - Slash Usage: `/star_utils replacementvarpaths <state>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>star_utils getlogs (Hybrid Command)
Get logs for a cog from StarCogs<br/>
 - Usage: `<@1275521742961508432>star_utils getlogs <cog> [level=all]`
 - Slash Usage: `/star_utils getlogs <cog> [level=all]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### cog: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### level: str = 'all'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


