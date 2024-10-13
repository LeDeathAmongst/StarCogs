Cog to handle slash command feature requests.

# ,srequest
Base command for slash feature requests.<br/>
 - Usage: `,srequest`
 - Aliases: `sr`
## ,srequest submit
Request a new slash feature for the bot.<br/>
 - Usage: `,srequest submit <feature>`
Extended Arg Info
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,srequest status
Check the status of a slash feature request.<br/>
 - Usage: `,srequest status <request_id>`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,srequest channel
Set the channel for slash feature requests.<br/>
 - Usage: `,srequest channel <channel>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,srequest consider
Consider a slash feature request.<br/>
 - Usage: `,srequest consider <request_id> [reason]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,srequest deny
Deny a slash feature request.<br/>
 - Usage: `,srequest deny <request_id> [reason]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,srequest accept
Accept a slash feature request.<br/>
 - Usage: `,srequest accept <request_id> [reason]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
