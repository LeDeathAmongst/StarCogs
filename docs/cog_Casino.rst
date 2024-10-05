Casino
======

# <@1275521742961508432>allin
Bets all your currency for a chance to win big!<br/>

The higher your multiplier the lower your odds of winning.<br/>
 - Usage: `<@1275521742961508432>allin <multiplier>`
 - Checks: `server_only`
Extended Arg Info
> ### multiplier: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>blackjack
Play a game of blackjack.<br/>

Blackjack supports doubling down, but not split.<br/>
 - Usage: `<@1275521742961508432>blackjack <bet>`
 - Aliases: `bj and 21`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>craps
Plays a modified version of craps<br/>

The player wins 7x their bet on a come-out roll of 7.<br/>
A comeout roll of 11 is an automatic win (standard mutlipliers apply).<br/>
The player will lose on a comeout roll of 2, 3, or 12.<br/>
Otherwise a point will be established. The player will keep<br/>
rolling until they hit a 7 (and lose) or their point number.<br/>

Every bet is considered a 'Pass Line' bet.<br/>
 - Usage: `<@1275521742961508432>craps <bet>`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>coin
Coin flip game with a 50/50 chance to win.<br/>

Pick heads or tails and place your bet.<br/>
 - Usage: `<@1275521742961508432>coin <bet> <choice>`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```
> ### choice: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>cups
Guess which cup of three is hiding the coin.<br/>

Must pick 1, 2, or 3.<br/>
 - Usage: `<@1275521742961508432>cups <bet> <cup>`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```
> ### cup: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>dice
Roll a set of dice and win on 2, 7, 11, 12.<br/>

Just place a bet. No need to pick a number.<br/>
 - Usage: `<@1275521742961508432>dice <bet>`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>double
Play a game of Double Or Nothing.<br/>

Continue to try to double your bet until<br/>
you cash out or lose it all.<br/>
 - Usage: `<@1275521742961508432>double <bet>`
 - Aliases: `don and x2`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>hilo
Pick high, low, or 7 in a dice rolling game.<br/>

Acceptable choices are high, hi, low, lo, 7, or seven.<br/>
 - Usage: `<@1275521742961508432>hilo <bet> <choice>`
 - Aliases: `hl`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```
> ### choice: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>war
Play a modified game of war.<br/>
 - Usage: `<@1275521742961508432>war <bet>`
 - Checks: `server_only`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>bjmock
Test function for blackjack<br/>

This will mock the blackjack game, allowing you to insert a player hand<br/>
and a dealer hand.<br/>

Example: <@1275521742961508432>bjmock 50 :clubs: 10, :diamonds: 10 | :clubs: Ace, :clubs: Queen<br/>
 - Usage: `<@1275521742961508432>bjmock <bet> <hands>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```
> ### hands: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>casino
Interacts with the Casino system.<br/>

Use help on Casino (upper case) for more commands.<br/>
 - Usage: `<@1275521742961508432>casino`
 - Checks: `server_only`


## <@1275521742961508432>casino wipe
Completely wipes casino data.<br/>
 - Usage: `<@1275521742961508432>casino wipe`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>casino admin
A list of Admin level and above commands for Casino.<br/>
 - Usage: `<@1275521742961508432>casino admin`
 - Restricted to: `ADMIN`


## <@1275521742961508432>casino info
Shows information about Casino.<br/>

Displays a list of games with their set parameters:<br/>
Access Levels, Maximum and Minimum bets, if it's open to play,<br/>
cooldowns, and multipliers. It also displays settings for the<br/>
server (or global) if enabled.<br/>
 - Usage: `<@1275521742961508432>casino info`


## <@1275521742961508432>casino resetuser
Reset a user's cooldowns, stats, or everything.<br/>
 - Usage: `<@1275521742961508432>casino resetuser <user>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### user: discord.member.Member
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


## <@1275521742961508432>casino resetinstance
Reset global/server cooldowns, settings, memberships, or everything.<br/>
 - Usage: `<@1275521742961508432>casino resetinstance`
 - Restricted to: `ADMIN`


## <@1275521742961508432>casino version
Shows the current Casino version.<br/>
 - Usage: `<@1275521742961508432>casino version`


## <@1275521742961508432>casino stats
Shows your play statistics for Casino<br/>
 - Usage: `<@1275521742961508432>casino stats [player=None]`
Extended Arg Info
> ### player: Union[discord.member.Member, discord.user.User] = None
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


## <@1275521742961508432>casino releasecredits
Approves pending currency for a user.<br/>

If this casino has maximum winnings threshold set, and a user makes a bet that<br/>
exceeds this amount, then they will have those credits with held. This command will<br/>
Allow you to release those credits back to the user. This system is designed to limit<br/>
earnings when a player may have found a way to cheat a game.<br/>
 - Usage: `<@1275521742961508432>casino releasecredits <player>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### player: Union[discord.member.Member, discord.user.User]
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


## <@1275521742961508432>casino memberships
Displays a list of server/global memberships.<br/>
 - Usage: `<@1275521742961508432>casino memberships`


# <@1275521742961508432>casinoset
Changes Casino settings<br/>
 - Usage: `<@1275521742961508432>casinoset`
 - Restricted to: `ADMIN`
 - Checks: `Casino and server_only`


## <@1275521742961508432>casinoset revokemem
Revoke an assigned membership.<br/>

Members will still keep this membership until the next auto cycle (5mins).<br/>
At that time, they will be re-evaluated and downgraded/upgraded appropriately.<br/>
 - Usage: `<@1275521742961508432>casinoset revokemem <player>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### player: Union[discord.member.Member, discord.user.User]
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


## <@1275521742961508432>casinoset cooldown
Sets the cooldown for a game.<br/>

You can use the format DD:HH:MM:SS to set a time, or just simply<br/>
type the number of seconds.<br/>
 - Usage: `<@1275521742961508432>casinoset cooldown <game> <cooldown>`
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### cooldown: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>casinoset min
Sets the minimum bid for a game.<br/>
 - Usage: `<@1275521742961508432>casinoset min <game> <minimum>`
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### minimum: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>casinoset gametoggle
Opens/Closes a specific game for use.<br/>
 - Usage: `<@1275521742961508432>casinoset gametoggle <game>`
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>casinoset toggle
Opens and closes the Casino for use.<br/>

This command only restricts the use of playing games.<br/>
 - Usage: `<@1275521742961508432>casinoset toggle`


## <@1275521742961508432>casinoset name
Sets the name of the Casino.<br/>

The casino name may only be 30 characters in length.<br/>
 - Usage: `<@1275521742961508432>casinoset name <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>casinoset oldstyle
Toggle between editing and sending new messages for casino games..<br/>
 - Usage: `<@1275521742961508432>casinoset oldstyle`


## <@1275521742961508432>casinoset assignmem
Manually assigns a membership to a user.<br/>

Users who are assigned a membership no longer need to meet the<br/>
requirements set. However, if the membership is revoked, then the<br/>
user will need to meet the requirements as usual.<br/>
 - Usage: `<@1275521742961508432>casinoset assignmem <player> <membership>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### player: Union[discord.member.Member, discord.user.User]
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
> ### membership: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>casinoset memdesigner
A process to create, edit, and delete memberships.<br/>
 - Usage: `<@1275521742961508432>casinoset memdesigner`
 - Restricted to: `ADMIN`


## <@1275521742961508432>casinoset payouttoggle
Turns on a payout limit.<br/>

The payout limit will withhold winnings from players until they are approved by the<br/>
appropriate authority. To set the limit, use payoutlimit.<br/>
 - Usage: `<@1275521742961508432>casinoset payouttoggle`


## <@1275521742961508432>casinoset payoutlimit
Sets a payout limit.<br/>

Users who exceed this amount will have their winnings witheld until they are<br/>
reviewed and approved by the appropriate authority. Limits are only triggered if<br/>
payout limits are ON. To turn on payout limits, use payouttoggle.<br/>
 - Usage: `<@1275521742961508432>casinoset payoutlimit <limit>`
Extended Arg Info
> ### limit: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>casinoset access
Sets the access level required to play a game.<br/>

Access levels are used in conjunction with memberships. To read more on using<br/>
access levels and memberships please refer to the casino wiki.<br/>
 - Usage: `<@1275521742961508432>casinoset access <game> <access>`
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### access: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>casinoset multiplier
Sets the payout multiplier for a game.<br/>
        <br/>
 - Usage: `<@1275521742961508432>casinoset multiplier <game> <multiplier>`
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### multiplier: float
> ```
> A number with or without decimal places.
> ```


## <@1275521742961508432>casinoset max
Sets the maximum bid for a game.<br/>
 - Usage: `<@1275521742961508432>casinoset max <game> <maximum>`
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### maximum: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>casinoset mode
Toggles Casino between global and local modes.<br/>

When casino is set to local mode, each server will have its own<br/>
unique data, and admin level commands can be used on that server.<br/>

When casino is set to global mode, data is linked between all servers<br/>
the bot is connected to. In addition, admin level commands can only be<br/>
used by the owner or co-owners.<br/>
 - Usage: `<@1275521742961508432>casinoset mode`
 - Restricted to: `BOT_OWNER`


