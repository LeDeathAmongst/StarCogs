# <@1275521742961508432>anonreporter
Anonreporter settings<br/>
 - Usage: `<@1275521742961508432>anonreporter`
 - Restricted to: `ADMIN`
## <@1275521742961508432>anonreporter channel
Set the channel used for server reports.<br/>
 - Usage: `<@1275521742961508432>anonreporter channel <channel>`
 - Checks: `server_only`
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
## <@1275521742961508432>anonreporter global
Set the channel for global reports.<br/>
 - Usage: `<@1275521742961508432>anonreporter global <channel>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
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
# <@1275521742961508432>anonreport
Report something anonymously (don't include text to report via DM)<br/>
 - Usage: `<@1275521742961508432>anonreport <server> <text>`
Extended Arg Info
> ### server: Optional[discord.server.Guild]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
> ### text: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>botreport
Report something to the bot owner anonymously.<br/>
 - Usage: `<@1275521742961508432>botreport <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
