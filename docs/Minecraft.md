A cog to display informations about Minecraft Java users and servers, and notify for each change of a server!

# ,minecraft (Hybrid Command)
Get informations about Minecraft Java.<br/>
 - Usage: `,minecraft`
 - Slash Usage: `/minecraft`
## ,minecraft editlastmessage (Hybrid Command)
Edit the last message sent for changes.<br/>
 - Usage: `,minecraft editlastmessage <channel> <state>`
 - Slash Usage: `/minecraft editlastmessage <channel> <state>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,minecraft forcecheck (Hybrid Command)
Force check Minecraft Java servers in Config.<br/>
 - Usage: `,minecraft forcecheck`
 - Slash Usage: `/minecraft forcecheck`
 - Restricted to: `BOT_OWNER`
## ,minecraft removeserver (Hybrid Command)
Remove a Minecraft Java server in Config.<br/>
 - Usage: `,minecraft removeserver <channel> <server_url>`
 - Slash Usage: `/minecraft removeserver <channel> <server_url>`
 - Restricted to: `ADMIN`
 - Aliases: `remove and -`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### server_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,minecraft getdebugloopsstatus (Hybrid Command)
Get an embed for check loop status.<br/>
 - Usage: `,minecraft getdebugloopsstatus`
 - Slash Usage: `/minecraft getdebugloopsstatus`
 - Restricted to: `BOT_OWNER`
## ,minecraft checkplayers (Hybrid Command)
Include players joining or leaving the server in notifications.<br/>
 - Usage: `,minecraft checkplayers <channel> <state>`
 - Slash Usage: `/minecraft checkplayers <channel> <state>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,minecraft getserver (Hybrid Command)
Get informations about a Minecraft Java server.<br/>
 - Usage: `,minecraft getserver <server_url>`
 - Slash Usage: `/minecraft getserver <server_url>`
Extended Arg Info
> ### server_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,minecraft addserver (Hybrid Command)
Add a Minecraft Java server in Config to get automatically new status.<br/>
 - Usage: `,minecraft addserver <channel> <server_url>`
 - Slash Usage: `/minecraft addserver <channel> <server_url>`
 - Restricted to: `ADMIN`
 - Aliases: `add and +`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### server_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,minecraft getplayerskin (Hybrid Command)
Get Minecraft Java player skin by name.<br/>
 - Usage: `,minecraft getplayerskin <player> [overlay=False]`
 - Slash Usage: `/minecraft getplayerskin <player> [overlay=False]`
Extended Arg Info
> ### overlay: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```