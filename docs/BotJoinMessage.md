Cog to send a configurable message to the server owner when the bot joins a server.

# ,botjoinmessage
Commands to configure the bot join message.<br/>
 - Usage: `,botjoinmessage`
 - Restricted to: `BOT_OWNER`
 - Aliases: `bjm`
## ,botjoinmessage addfield
Add a field to the bot join message.<br/>
 - Usage: `,botjoinmessage addfield <name> <value> [inline=True]`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### inline: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,botjoinmessage listfields
List all fields in the bot join message.<br/>
 - Usage: `,botjoinmessage listfields`
## ,botjoinmessage settitle
Set the title of the bot join message.<br/>
 - Usage: `,botjoinmessage settitle <title>`
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,botjoinmessage preview
Preview the current bot join message.<br/>
 - Usage: `,botjoinmessage preview`
## ,botjoinmessage removefield
Remove a field from the bot join message.<br/>
 - Usage: `,botjoinmessage removefield <index>`
Extended Arg Info
> ### index: int
> ```
> A number without decimal places.
> ```
## ,botjoinmessage setcolor
Set the color of the bot join message.<br/>
 - Usage: `,botjoinmessage setcolor <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
## ,botjoinmessage editfield
Edit a field in the bot join message.<br/>
 - Usage: `,botjoinmessage editfield <index> [name=None] [value=None] [inline=None]`
Extended Arg Info
> ### index: int
> ```
> A number without decimal places.
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### value: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### inline: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
