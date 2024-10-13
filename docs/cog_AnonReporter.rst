AnonReporter
============

<<<<<<< HEAD
# <@1275521742961508432>anonreporter
Anonreporter settings<br/>
 - Usage: `<@1275521742961508432>anonreporter`
 - Restricted to: `ADMIN`


## <@1275521742961508432>anonreporter channel
Set the channel used for server reports.<br/>
 - Usage: `<@1275521742961508432>anonreporter channel <channel>`
=======
# ,anonreporter
Anonreporter settings<br/>
 - Usage: `,anonreporter`
 - Restricted to: `ADMIN`


## ,anonreporter channel
Set the channel used for server reports.<br/>
 - Usage: `,anonreporter channel <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>anonreporter global
Set the channel for global reports.<br/>
 - Usage: `<@1275521742961508432>anonreporter global <channel>`
=======
## ,anonreporter global
Set the channel for global reports.<br/>
 - Usage: `,anonreporter global <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>anonreport
Report something anonymously (don't include text to report via DM)<br/>
 - Usage: `<@1275521742961508432>anonreport <server> <text>`
=======
# ,anonreport
Report something anonymously (don't include text to report via DM)<br/>
 - Usage: `,anonreport <server> <text>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>botreport
Report something to the bot owner anonymously.<br/>
 - Usage: `<@1275521742961508432>botreport <text>`
=======
# ,botreport
Report something to the bot owner anonymously.<br/>
 - Usage: `,botreport <text>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


