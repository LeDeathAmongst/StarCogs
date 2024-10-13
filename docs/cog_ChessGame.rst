ChessGame
=========

Cog to Play chess!

# ,chess
manage chess games<br/>
 - Usage: `,chess`


## ,chess move
move the next game piece, using Standard Algebraic Notation<br/>
 - Usage: `,chess move <game_name> <move>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### move: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,chess draw
draw related commands<br/>
 - Usage: `,chess draw`


### ,chess draw byagreement
Offer draw by agreement<br/>
 - Usage: `,chess draw byagreement <game_name>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,chess draw claim
if valid claim made to draw the game will end with no victor<br/>
 - Usage: `,chess draw claim <game_name> <claim_type>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### claim_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,chess list
list all available games<br/>
 - Usage: `,chess list`


## ,chess close
sub command to close a game<br/>
 - Usage: `,chess close <game_name> [channel=None] [no_confirmation=False]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### no_confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,chess start
start a new game<br/>

_Standard is the default when no game type is given_<br/>
__**1**__: Standard, Chess, Classical, Normal, Illegal, From Position<br/>
__**2**__: Suicide, Suicide chess<br/>
__**3**__: Giveaway, Giveaway chess, Give away, Give away chess<br/>
__**4**__: Antichess, Anti chess, Anti<br/>
__**5**__: Atomic, Atom, Atomic chess<br/>
__**6**__: King of the Hill, KOTH, kingOfTheHill<br/>
__**7**__: Racing Kings, Racing, Race, racingkings<br/>
__**8**__: Horde, Horde chess<br/>
__**9**__: Three-check, Three check, Threecheck, Three check chess, 3-check, 3 check, 3check<br/>
__**10**__: Crazyhouse, Crazy House, House, ZH<br/>
 - Usage: `,chess start <other_player> [game_name=None] [game_type=None]`
Extended Arg Info
> ### other_player: discord.member.Member
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
> ### game_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### game_type: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,chess scoreboard
scoreboard related commands<br/>
 - Usage: `,chess scoreboard`


### ,chess scoreboard list
list users scoreboard from highest to lowest<br/>

Scoreboard can be sorted by elo, wins, losses, or ties.<br/>
Scoreboard is sorted by wins by default.<br/>
 - Usage: `,chess scoreboard list [sort_by=wins]`
Extended Arg Info
> ### sort_by: str = 'wins'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,chess scoreboard increment
allows bot owner to increment (decrement if negative value passed) a player's score<br/>
 - Usage: `,chess scoreboard increment <player> <elo> <wins> <losses> <ties>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### player: discord.member.Member
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
> ### elo: int
> ```
> A number without decimal places.
> ```
> ### wins: int
> ```
> A number without decimal places.
> ```
> ### losses: int
> ```
> A number without decimal places.
> ```
> ### ties: int
> ```
> A number without decimal places.
> ```


### ,chess scoreboard find
find a player's score. If none is provided this will look for the requester's score<br/>
 - Usage: `,chess scoreboard find [player=None]`
Extended Arg Info
> ### player: discord.member.Member = None
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


### ,chess scoreboard clear
allows bot owner clear the scoreboard<br/>
 - Usage: `,chess scoreboard clear`
 - Restricted to: `BOT_OWNER`


#### ,chess scoreboard clear player
removes a particular player (or nonexistant id) from the scoreboard<br/>
 - Usage: `,chess scoreboard clear player <player>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### player: Union[discord.member.Member, int]
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


#### ,chess scoreboard clear all
remove **ALL** scores from the scoreboard<br/>
 - Usage: `,chess scoreboard clear all`
 - Restricted to: `BOT_OWNER`


## ,chess launch
start a new game<br/>

_Standard is the default when no game type is given_<br/>
__**1**__: Standard, Chess, Classical, Normal, Illegal, From Position<br/>
__**2**__: Suicide, Suicide chess<br/>
__**3**__: Giveaway, Giveaway chess, Give away, Give away chess<br/>
__**4**__: Antichess, Anti chess, Anti<br/>
__**5**__: Atomic, Atom, Atomic chess<br/>
__**6**__: King of the Hill, KOTH, kingOfTheHill<br/>
__**7**__: Racing Kings, Racing, Race, racingkings<br/>
__**8**__: Horde, Horde chess<br/>
__**9**__: Three-check, Three check, Threecheck, Three check chess, 3-check, 3 check, 3check<br/>
__**10**__: Crazyhouse, Crazy House, House, ZH<br/>
 - Usage: `,chess launch <player> <other_player> [game_name=None] [game_type=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### player: discord.member.Member
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
> ### other_player: discord.member.Member
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
> ### game_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### game_type: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,chess show
reposts the last gameboard state<br/>
 - Usage: `,chess show <game_name>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


