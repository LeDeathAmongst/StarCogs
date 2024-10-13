Base to host werewolf on a guild

# ,buildgame
Create game codes to run custom games.<br/>

Pick the roles or randomized roles you want to include in a game.<br/>

Note: The same role can be picked more than once.<br/>
 - Usage: `,buildgame`
# ,wwset
Base command to adjust settings. Check help for command list.<br/>
 - Usage: `,wwset`
 - Restricted to: `GUILD_OWNER`
## ,wwset list
Lists current server settings<br/>
 - Usage: `,wwset list`
 - Checks: `server_only`
## ,wwset logchannel
Assign the log channel<br/>
 - Usage: `,wwset logchannel [channel=None]`
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
## ,wwset channel
Assign the village channel<br/>
 - Usage: `,wwset channel [channel=None]`
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
## ,wwset category
Assign the channel category<br/>
 - Usage: `,wwset category [category_id=None]`
 - Checks: `server_only`
Extended Arg Info
> ### category_id: int = None
> ```
> A number without decimal places.
> ```
## ,wwset role
Set the game role<br/>
This role should not be manually assigned<br/>
 - Usage: `,wwset role [role=None]`
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
# ,ww
Base command for this cog. Check help for the commands list.<br/>
 - Usage: `,ww`
## ,ww new
Create and join a new game of Werewolf<br/>
 - Usage: `,ww new [game_code=None]`
 - Checks: `server_only`
Extended Arg Info
> ### game_code=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,ww start
Checks number of players and attempts to start the game<br/>
 - Usage: `,ww start`
 - Checks: `server_only`
## ,ww quit
Quit a game of Werewolf<br/>
 - Usage: `,ww quit`
 - Checks: `server_only`
## ,ww code
Adjusts the game code.<br/>

See `,buildgame` to generate a new code<br/>
 - Usage: `,ww code <code>`
 - Checks: `server_only`
Extended Arg Info
> ### code
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,ww forcejoin
Force someone to join a game of Werewolf<br/>
 - Usage: `,ww forcejoin <target>`
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
## ,ww join
Joins a game of Werewolf<br/>
 - Usage: `,ww join`
 - Checks: `server_only`
## ,ww choose
Arbitrary decision making<br/>
Handled by game+role<br/>
Can be received by DM<br/>
 - Usage: `,ww choose <data>`
Extended Arg Info
> ### data
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,ww search
Find custom roles by name, alignment, category, or ID<br/>
 - Usage: `,ww search`
### ,ww search name
Search for a role by name<br/>
 - Usage: `,ww search name <name>`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,ww search index
Search for a role by ID<br/>
 - Usage: `,ww search index <idx>`
Extended Arg Info
> ### idx: int
> ```
> A number without decimal places.
> ```
### ,ww search alignment
Search for a role by alignment<br/>
 - Usage: `,ww search alignment <alignment>`
Extended Arg Info
> ### alignment: int
> ```
> A number without decimal places.
> ```
### ,ww search category
Search for a role by category<br/>
 - Usage: `,ww search category <category>`
Extended Arg Info
> ### category: int
> ```
> A number without decimal places.
> ```
## ,ww vote
Vote for a player by ID<br/>
 - Usage: `,ww vote <target_id>`
 - Checks: `server_only`
Extended Arg Info
> ### target_id: int
> ```
> A number without decimal places.
> ```
## ,ww stop
Stops the current game<br/>
 - Usage: `,ww stop`
 - Checks: `server_only`
