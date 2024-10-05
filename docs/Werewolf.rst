Werewolf
========

Base to host werewolf on a guild

# <@1275521742961508432>buildgame
Create game codes to run custom games.<br/>

Pick the roles or randomized roles you want to include in a game.<br/>

Note: The same role can be picked more than once.<br/>
 - Usage: `<@1275521742961508432>buildgame`


# <@1275521742961508432>wwset
Base command to adjust settings. Check help for command list.<br/>
 - Usage: `<@1275521742961508432>wwset`
 - Restricted to: `GUILD_OWNER`


## <@1275521742961508432>wwset channel
Assign the village channel<br/>
 - Usage: `<@1275521742961508432>wwset channel [channel=None]`
 - Checks: `server_only`
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


## <@1275521742961508432>wwset category
Assign the channel category<br/>
 - Usage: `<@1275521742961508432>wwset category [category_id=None]`
 - Checks: `server_only`
Extended Arg Info
> ### category_id: int = None
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>wwset role
Set the game role<br/>
This role should not be manually assigned<br/>
 - Usage: `<@1275521742961508432>wwset role [role=None]`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>wwset list
Lists current server settings<br/>
 - Usage: `<@1275521742961508432>wwset list`
 - Checks: `server_only`


## <@1275521742961508432>wwset logchannel
Assign the log channel<br/>
 - Usage: `<@1275521742961508432>wwset logchannel [channel=None]`
 - Checks: `server_only`
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


# <@1275521742961508432>ww
Base command for this cog. Check help for the commands list.<br/>
 - Usage: `<@1275521742961508432>ww`


## <@1275521742961508432>ww code
Adjusts the game code.<br/>

See `<@1275521742961508432>buildgame` to generate a new code<br/>
 - Usage: `<@1275521742961508432>ww code <code>`
 - Checks: `server_only`
Extended Arg Info
> ### code
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>ww forcejoin
Force someone to join a game of Werewolf<br/>
 - Usage: `<@1275521742961508432>ww forcejoin <target>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### target: discord.member.Member
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     


## <@1275521742961508432>ww join
Joins a game of Werewolf<br/>
 - Usage: `<@1275521742961508432>ww join`
 - Checks: `server_only`


## <@1275521742961508432>ww choose
Arbitrary decision making<br/>
Handled by game+role<br/>
Can be received by DM<br/>
 - Usage: `<@1275521742961508432>ww choose <data>`
Extended Arg Info
> ### data
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>ww search
Find custom roles by name, alignment, category, or ID<br/>
 - Usage: `<@1275521742961508432>ww search`


### <@1275521742961508432>ww search alignment
Search for a role by alignment<br/>
 - Usage: `<@1275521742961508432>ww search alignment <alignment>`
Extended Arg Info
> ### alignment: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>ww search name
Search for a role by name<br/>
 - Usage: `<@1275521742961508432>ww search name <name>`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>ww search index
Search for a role by ID<br/>
 - Usage: `<@1275521742961508432>ww search index <idx>`
Extended Arg Info
> ### idx: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>ww search category
Search for a role by category<br/>
 - Usage: `<@1275521742961508432>ww search category <category>`
Extended Arg Info
> ### category: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ww vote
Vote for a player by ID<br/>
 - Usage: `<@1275521742961508432>ww vote <target_id>`
 - Checks: `server_only`
Extended Arg Info
> ### target_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ww stop
Stops the current game<br/>
 - Usage: `<@1275521742961508432>ww stop`
 - Checks: `server_only`


## <@1275521742961508432>ww start
Checks number of players and attempts to start the game<br/>
 - Usage: `<@1275521742961508432>ww start`
 - Checks: `server_only`


## <@1275521742961508432>ww new
Create and join a new game of Werewolf<br/>
 - Usage: `<@1275521742961508432>ww new [game_code=None]`
 - Checks: `server_only`
Extended Arg Info
> ### game_code=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>ww quit
Quit a game of Werewolf<br/>
 - Usage: `<@1275521742961508432>ww quit`
 - Checks: `server_only`


