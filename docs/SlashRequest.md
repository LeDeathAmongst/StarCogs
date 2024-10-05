Cog to handle slash command feature requests.

# <@1275521742961508432>srequest
Base command for slash feature requests.<br/>
 - Usage: `<@1275521742961508432>srequest`
 - Aliases: `sr`
## <@1275521742961508432>srequest consider
Consider a slash feature request.<br/>
 - Usage: `<@1275521742961508432>srequest consider <request_id> [reason]`
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
## <@1275521742961508432>srequest status
Check the status of a slash feature request.<br/>
 - Usage: `<@1275521742961508432>srequest status <request_id>`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>srequest channel
Set the channel for slash feature requests.<br/>
 - Usage: `<@1275521742961508432>srequest channel <channel>`
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
## <@1275521742961508432>srequest accept
Accept a slash feature request.<br/>
 - Usage: `<@1275521742961508432>srequest accept <request_id> [reason]`
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
## <@1275521742961508432>srequest deny
Deny a slash feature request.<br/>
 - Usage: `<@1275521742961508432>srequest deny <request_id> [reason]`
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
## <@1275521742961508432>srequest submit
Request a new slash feature for the bot.<br/>
 - Usage: `<@1275521742961508432>srequest submit <feature>`
Extended Arg Info
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
