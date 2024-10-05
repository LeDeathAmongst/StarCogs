GuildManager
============

Guild management tools.

# <@1275521742961508432>servermanager
Guild management commands.<br/>
 - Usage: `<@1275521742961508432>servermanager`
 - Restricted to: `BOT_OWNER`
 - Aliases: `serverman, gman, and gm`


## <@1275521742961508432>servermanager minmembers
Set how many members a server should have for the bot to stay in it.<br/>

Pass 0 to disable.<br/>
 - Usage: `<@1275521742961508432>servermanager minmembers [min_members=0]`
 - Aliases: `minimummembers`
Extended Arg Info
> ### min_members: int = 0
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>servermanager leave
Leave servers that (somehow) doesn't fulfill requirements.<br/>
 - Usage: `<@1275521742961508432>servermanager leave`


### <@1275521742961508432>servermanager leave botfarms
Leave bot farms.<br/>
 - Usage: `<@1275521742961508432>servermanager leave botfarms`


### <@1275521742961508432>servermanager leave lessmembers
Leave servers with less members than the minimum.<br/>
 - Usage: `<@1275521742961508432>servermanager leave lessmembers`


### <@1275521742961508432>servermanager leave blacklisted
Leave servers that are blacklisted.<br/>
 - Usage: `<@1275521742961508432>servermanager leave blacklisted`


## <@1275521742961508432>servermanager whitelist
Guild whitelist management commands.<br/>
 - Usage: `<@1275521742961508432>servermanager whitelist`
 - Aliases: `wl`


### <@1275521742961508432>servermanager whitelist add
Add servers to the whitelist.<br/>
 - Usage: `<@1275521742961508432>servermanager whitelist add <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>servermanager whitelist remove
Remove servers from the whitelist.<br/>
 - Usage: `<@1275521742961508432>servermanager whitelist remove <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>servermanager whitelist clear
Clear servers from the whitelist.<br/>
 - Usage: `<@1275521742961508432>servermanager whitelist clear`


## <@1275521742961508432>servermanager blacklist
Guild blacklist management commands.<br/>
 - Usage: `<@1275521742961508432>servermanager blacklist`
 - Aliases: `bl`


### <@1275521742961508432>servermanager blacklist remove
Remove servers from bot's blacklist.<br/>
 - Usage: `<@1275521742961508432>servermanager blacklist remove <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>servermanager blacklist clear
Clear servers from the blacklist.<br/>
 - Usage: `<@1275521742961508432>servermanager blacklist clear`


### <@1275521742961508432>servermanager blacklist add
Blacklist bot from joining certain servers (autoleave)<br/>
 - Usage: `<@1275521742961508432>servermanager blacklist add <server_ids>`
Extended Arg Info
> ### *server_ids: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>servermanager chunk
Chunk unchunked servers.<br/>
 - Usage: `<@1275521742961508432>servermanager chunk <servers>`
Extended Arg Info
> ### *servers: discord.server.Guild
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     


## <@1275521742961508432>servermanager channel
Set a log channel for server joins/leaves.<br/>
 - Usage: `<@1275521742961508432>servermanager channel [channel=None]`
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


## <@1275521742961508432>servermanager show
Show servers with details.<br/>
 - Usage: `<@1275521742961508432>servermanager show`
 - Aliases: `view`


### <@1275521742961508432>servermanager show lessmembers
Show servers with less members than the minimum.<br/>
 - Usage: `<@1275521742961508432>servermanager show lessmembers`


### <@1275521742961508432>servermanager show unchunked
Show unchunked servers.<br/>
 - Usage: `<@1275521742961508432>servermanager show unchunked`


### <@1275521742961508432>servermanager show botfarms
Show bot farms.<br/>
 - Usage: `<@1275521742961508432>servermanager show botfarms`


## <@1275521742961508432>servermanager serverlock
Locks Starfire to its current servers only.<br/>
 - Usage: `<@1275521742961508432>servermanager serverlock`


## <@1275521742961508432>servermanager settings
View server manager's settings.<br/>
 - Usage: `<@1275521742961508432>servermanager settings`


## <@1275521742961508432>servermanager botratio
Set the bot ratio for servers for the bot to leave.<br/>

The ratio must be between 0-100, pass 0 to disable.<br/>
 - Usage: `<@1275521742961508432>servermanager botratio [ratio=0]`
Extended Arg Info
> ### ratio: int = 0
> ```
> A number without decimal places.
> ```


