Guild management tools.

# ,servermanager
Guild management commands.<br/>
 - Usage: `,servermanager`
 - Restricted to: `BOT_OWNER`
 - Aliases: `serverman, gman, and gm`
## ,servermanager whitelist
Guild whitelist management commands.<br/>
 - Usage: `,servermanager whitelist`
 - Aliases: `wl`
### ,servermanager whitelist add
Add servers to the whitelist.<br/>
 - Usage: `,servermanager whitelist add <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```
### ,servermanager whitelist remove
Remove servers from the whitelist.<br/>
 - Usage: `,servermanager whitelist remove <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```
### ,servermanager whitelist clear
Clear servers from the whitelist.<br/>
 - Usage: `,servermanager whitelist clear`
## ,servermanager settings
View server manager's settings.<br/>
 - Usage: `,servermanager settings`
## ,servermanager show
Show servers with details.<br/>
 - Usage: `,servermanager show`
 - Aliases: `view`
### ,servermanager show botfarms
Show bot farms.<br/>
 - Usage: `,servermanager show botfarms`
### ,servermanager show unchunked
Show unchunked servers.<br/>
 - Usage: `,servermanager show unchunked`
### ,servermanager show lessmembers
Show servers with less members than the minimum.<br/>
 - Usage: `,servermanager show lessmembers`
## ,servermanager blacklist
Guild blacklist management commands.<br/>
 - Usage: `,servermanager blacklist`
 - Aliases: `bl`
### ,servermanager blacklist remove
Remove servers from bot's blacklist.<br/>
 - Usage: `,servermanager blacklist remove <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```
### ,servermanager blacklist add
Blacklist bot from joining certain servers (autoleave)<br/>
 - Usage: `,servermanager blacklist add <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```
### ,servermanager blacklist clear
Clear servers from the blacklist.<br/>
 - Usage: `,servermanager blacklist clear`
## ,servermanager channel
Set a log channel for server joins/leaves.<br/>
 - Usage: `,servermanager channel [channel=None]`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,servermanager botratio
Set the bot ratio for servers for the bot to leave.<br/>

The ratio must be between 0-100, pass 0 to disable.<br/>
 - Usage: `,servermanager botratio [ratio=0]`
Extended Arg Info
> ### ratio: int = 0
> ```
> A number without decimal places.
> ```
## ,servermanager chunk
Chunk unchunked servers.<br/>
 - Usage: `,servermanager chunk <servers>`
Extended Arg Info
> ### *servers: discord.server.Guild
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## ,servermanager minmembers
Set how many members a server should have for the bot to stay in it.<br/>

Pass 0 to disable.<br/>
 - Usage: `,servermanager minmembers [min_members=0]`
 - Aliases: `minimummembers`
Extended Arg Info
> ### min_members: int = 0
> ```
> A number without decimal places.
> ```
## ,servermanager leave
Leave servers that (somehow) doesn't fulfill requirements.<br/>
 - Usage: `,servermanager leave`
### ,servermanager leave lessmembers
Leave servers with less members than the minimum.<br/>
 - Usage: `,servermanager leave lessmembers`
### ,servermanager leave blacklisted
Leave servers that are blacklisted.<br/>
 - Usage: `,servermanager leave blacklisted`
### ,servermanager leave botfarms
Leave bot farms.<br/>
 - Usage: `,servermanager leave botfarms`
## ,servermanager serverlock
Locks Starfire to its current servers only.<br/>
 - Usage: `,servermanager serverlock`
