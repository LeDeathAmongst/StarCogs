Utility commands for PyLav

# ,plutils
Utility commands for PyLav<br/>
 - Usage: `,plutils`
## ,plutils slashes
Show the slashes available in the bot.<br/>

Author: TrustyJAID#0001 via code block on Discord channel.<br/>
 - Usage: `,plutils slashes`
## ,plutils decode
Decode the track base64 string into a JSON object<br/>
 - Usage: `,plutils decode <base64>`
Extended Arg Info
> ### base64: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,plutils trace
Start memory tracing<br/>

`,plutils trace 0` turns off tracing<br/>
`,plutils trace 1` turns on tracing<br/>
`,plutils trace` shows the current status of tracing<br/>
 - Usage: `,plutils trace [value=-1]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### value: int = -1
> ```
> A number without decimal places.
> ```
## ,plutils version
Show the version of the Cog and PyLav<br/>
 - Usage: `,plutils version`
## ,plutils logger
Set the logger level<br/>

Levels are the following:<br/>
0: Critical<br/>
1: Error<br/>
2: Warning<br/>
3: Info<br/>
4: Debug<br/>
5: Verbose<br/>
6: Trace<br/>
 - Usage: `,plutils logger <level>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### level: int
> ```
> A number without decimal places.
> ```
## ,plutils get
Get info about specific things<br/>
 - Usage: `,plutils get`
 - Checks: `requires_player`
### ,plutils get player
Get the API of the current track<br/>
 - Usage: `,plutils get player`
 - Restricted to: `BOT_OWNER`
### ,plutils get b64
Get the base64 of the current track<br/>
 - Usage: `,plutils get b64`
### ,plutils get source
Get the source of the current track<br/>
 - Usage: `,plutils get source`
### ,plutils get title
Get the title of the current track<br/>
 - Usage: `,plutils get title`
### ,plutils get author
Get the author of the current track<br/>
 - Usage: `,plutils get author`
## ,plutils cache
Manage the query cache<br/>
 - Usage: `,plutils cache`
 - Restricted to: `BOT_OWNER`
### ,plutils cache older
Clear the query cache older than a number of days<br/>
 - Usage: `,plutils cache older <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
### ,plutils cache query
Clear the query cache for a query<br/>
 - Usage: `,plutils cache query <query>`
### ,plutils cache size
Get the size of the query cache<br/>
 - Usage: `,plutils cache size`
### ,plutils cache clear
Clear the query cache<br/>
 - Usage: `,plutils cache clear`
