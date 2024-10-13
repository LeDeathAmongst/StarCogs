AnonReporter
============

# ,anonreporter
Anonreporter settings<br/>
 - Usage: `,anonreporter`
 - Restricted to: `ADMIN`


## ,anonreporter channel
Set the channel used for server reports.<br/>
 - Usage: `,anonreporter channel <channel>`
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


## ,anonreporter global
Set the channel for global reports.<br/>
 - Usage: `,anonreporter global <channel>`
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


# ,anonreport
Report something anonymously (don't include text to report via DM)<br/>
 - Usage: `,anonreport <server> <text>`
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


# ,botreport
Report something to the bot owner anonymously.<br/>
 - Usage: `,botreport <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


