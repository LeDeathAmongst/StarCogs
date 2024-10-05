AAA3A_utils
===========

Commands to manage all the cogs in AAA3A-cogs repo!

# <@1275521742961508432>aaa3a_utils (Hybrid Command)
All commands to manage all the cogs from AAA3A-cogs repo.<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils`
 - Slash Usage: `/aaa3a_utils`
 - Restricted to: `BOT_OWNER`
 - Aliases: `AAA3A_utils`


## <@1275521742961508432>aaa3a_utils senderrorwithsentry (Hybrid Command)
Send a recent error to the developer of AAA3A's cogs with Sentry (use the code given when the error has been triggered).<br/>

More details: https://aaa3a-cogs.readthedocs.io/en/latest/repo_telemetry.html<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils senderrorwithsentry <error>`
 - Slash Usage: `/aaa3a_utils senderrorwithsentry <error>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### error: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aaa3a_utils getdebugloopsstatus (Hybrid Command)
Get debug loops status for a cog from AAA3A-cogs.<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils getdebugloopsstatus <cog>`
 - Slash Usage: `/aaa3a_utils getdebugloopsstatus <cog>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### cog: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aaa3a_utils getlogs (Hybrid Command)
Get logs for a cog from AAA3A-cogs<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils getlogs <cog> [level=all]`
 - Slash Usage: `/aaa3a_utils getlogs <cog> [level=all]`
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


## <@1275521742961508432>aaa3a_utils getallfor (Hybrid Command)
Get all the necessary information to get support on a bot/repo/cog/command.<br/>
With a html file.<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils getallfor [all=None] [page=None] [repo=None] [check_updates=False] [cog=None] [command=None]`
 - Slash Usage: `/aaa3a_utils getallfor [all=None] [page=None] [repo=None] [check_updates=False] [cog=None] [command=None]`
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


## <@1275521742961508432>aaa3a_utils displaysentrymanualcommand (Hybrid Command)
Enable or disable displaying the command `<@1275521742961508432>AAA3A_utils senderrorwithsentry` in commands errors.<br/>

Defaults is `True`.<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils displaysentrymanualcommand <state>`
 - Slash Usage: `/aaa3a_utils displaysentrymanualcommand <state>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>aaa3a_utils replacementvarpaths (Hybrid Command)
Replace various var paths in texts sent by cog from AAA3A-cogs.<br/>

Defaults is `True`.<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils replacementvarpaths <state>`
 - Slash Usage: `/aaa3a_utils replacementvarpaths <state>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>aaa3a_utils resetconfig (Hybrid Command)
Reset Config for a cog from AAA3A-cogs.<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils resetconfig <cog> [confirmation=False]`
 - Slash Usage: `/aaa3a_utils resetconfig <cog> [confirmation=False]`
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


## <@1275521742961508432>aaa3a_utils telemetrywithsentry (Hybrid Command)
Enable or disable Telemetry with Sentry for all cogs from AAA3A-cogs.<br/>

More details: https://aaa3a-cogs.readthedocs.io/en/latest/repo_telemetry.html<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils telemetrywithsentry <state>`
 - Slash Usage: `/aaa3a_utils telemetrywithsentry <state>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>aaa3a_utils flags (Hybrid Command)
Use any command with flags.<br/>
 - Usage: `<@1275521742961508432>aaa3a_utils flags <content>`
 - Slash Usage: `/aaa3a_utils flags <content>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### content: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


