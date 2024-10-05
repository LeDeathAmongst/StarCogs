Cog to handle feature requests.

# <@1275521742961508432>frequest
Base command for feature requests.<br/>
 - Usage: `<@1275521742961508432>frequest`
 - Aliases: `fr`
## <@1275521742961508432>frequest accept
Accept a feature request.<br/>
 - Usage: `<@1275521742961508432>frequest accept <request_id> [reason]`
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
## <@1275521742961508432>frequest submit
Request a new feature for the bot.<br/>
 - Usage: `<@1275521742961508432>frequest submit <feature>`
Extended Arg Info
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>frequest consider
Consider a feature request.<br/>
 - Usage: `<@1275521742961508432>frequest consider <request_id> [reason]`
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
## <@1275521742961508432>frequest status
Check the status of a feature request.<br/>
 - Usage: `<@1275521742961508432>frequest status <request_id>`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>frequest channel
Set the channel for feature requests.<br/>
 - Usage: `<@1275521742961508432>frequest channel <channel>`
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
## <@1275521742961508432>frequest deny
Deny a feature request.<br/>
 - Usage: `<@1275521742961508432>frequest deny <request_id> [reason]`
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
