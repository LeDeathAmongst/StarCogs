PyLavUtils
==========

Utility commands for PyLav

# <@1275521742961508432>plutils
Utility commands for PyLav<br/>
 - Usage: `<@1275521742961508432>plutils`


## <@1275521742961508432>plutils version
Show the version of the Cog and PyLav<br/>
 - Usage: `<@1275521742961508432>plutils version`


## <@1275521742961508432>plutils get
Get info about specific things<br/>
 - Usage: `<@1275521742961508432>plutils get`
 - Checks: `requires_player`


### <@1275521742961508432>plutils get title
Get the title of the current track<br/>
 - Usage: `<@1275521742961508432>plutils get title`


### <@1275521742961508432>plutils get author
Get the author of the current track<br/>
 - Usage: `<@1275521742961508432>plutils get author`


### <@1275521742961508432>plutils get player
Get the API of the current track<br/>
 - Usage: `<@1275521742961508432>plutils get player`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>plutils get source
Get the source of the current track<br/>
 - Usage: `<@1275521742961508432>plutils get source`


### <@1275521742961508432>plutils get b64
Get the base64 of the current track<br/>
 - Usage: `<@1275521742961508432>plutils get b64`


## <@1275521742961508432>plutils cache
Manage the query cache<br/>
 - Usage: `<@1275521742961508432>plutils cache`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>plutils cache clear
Clear the query cache<br/>
 - Usage: `<@1275521742961508432>plutils cache clear`


### <@1275521742961508432>plutils cache older
Clear the query cache older than a number of days<br/>
 - Usage: `<@1275521742961508432>plutils cache older <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>plutils cache size
Get the size of the query cache<br/>
 - Usage: `<@1275521742961508432>plutils cache size`


### <@1275521742961508432>plutils cache query
Clear the query cache for a query<br/>
 - Usage: `<@1275521742961508432>plutils cache query <query>`


## <@1275521742961508432>plutils decode
Decode the track base64 string into a JSON object<br/>
 - Usage: `<@1275521742961508432>plutils decode <base64>`
Extended Arg Info
> ### base64: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>plutils trace
Start memory tracing<br/>

`<@1275521742961508432>plutils trace 0` turns off tracing<br/>
`<@1275521742961508432>plutils trace 1` turns on tracing<br/>
`<@1275521742961508432>plutils trace` shows the current status of tracing<br/>
 - Usage: `<@1275521742961508432>plutils trace [value=-1]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### value: int = -1
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>plutils logger
Set the logger level<br/>

Levels are the following:<br/>
0: Critical<br/>
1: Error<br/>
2: Warning<br/>
3: Info<br/>
4: Debug<br/>
5: Verbose<br/>
6: Trace<br/>
 - Usage: `<@1275521742961508432>plutils logger <level>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### level: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>plutils slashes
Show the slashes available in the bot.<br/>

Author: TrustyJAID#0001 via code block on Discord channel.<br/>
 - Usage: `<@1275521742961508432>plutils slashes`


