# Casino Help

### allin

**Description:** Bets all your currency for a chance to win big!

The higher your multiplier the lower your odds of winning.

**Usage:** `<@1275521742961508432>allin`

### blackjack

**Description:** Play a game of blackjack.

Blackjack supports doubling down, but not split.

**Usage:** `<@1275521742961508432>blackjack`

### craps

**Description:** Plays a modified version of craps

The player wins 7x their bet on a come-out roll of 7.
A comeout roll of 11 is an automatic win (standard mutlipliers apply).
The player will lose on a comeout roll of 2, 3, or 12.
Otherwise a point will be established. The player will keep
rolling until they hit a 7 (and lose) or their point number.

Every bet is considered a 'Pass Line' bet.

**Usage:** `<@1275521742961508432>craps`

### coin

**Description:** Coin flip game with a 50/50 chance to win.

Pick heads or tails and place your bet.

**Usage:** `<@1275521742961508432>coin`

### cups

**Description:** Guess which cup of three is hiding the coin.

Must pick 1, 2, or 3.

**Usage:** `<@1275521742961508432>cups`

### dice

**Description:** Roll a set of dice and win on 2, 7, 11, 12.

Just place a bet. No need to pick a number.

**Usage:** `<@1275521742961508432>dice`

### double

**Description:** Play a game of Double Or Nothing.

Continue to try to double your bet until
you cash out or lose it all.

**Usage:** `<@1275521742961508432>double`

### hilo

**Description:** Pick high, low, or 7 in a dice rolling game.

Acceptable choices are high, hi, low, lo, 7, or seven.

**Usage:** `<@1275521742961508432>hilo`

### war

**Description:** Play a modified game of war.

**Usage:** `<@1275521742961508432>war`

### casino

**Description:** Interacts with the Casino system.

Use help on Casino (upper case) for more commands.

**Usage:** `<@1275521742961508432>casino`

### casino admin

**Description:** A list of Admin level and above commands for Casino.

**Usage:** `<@1275521742961508432>casino admin`

### casino info

**Description:** Shows information about Casino.

Displays a list of games with their set parameters:
Access Levels, Maximum and Minimum bets, if it's open to play,
cooldowns, and multipliers. It also displays settings for the
server (or global) if enabled.

**Usage:** `<@1275521742961508432>casino info`

### casino wipe

**Description:** Completely wipes casino data.

**Usage:** `<@1275521742961508432>casino wipe`

### casino resetinstance

**Description:** Reset global/server cooldowns, settings, memberships, or everything.

**Usage:** `<@1275521742961508432>casino resetinstance`

### casino stats

**Description:** Shows your play statistics for Casino

**Usage:** `<@1275521742961508432>casino stats`

### casino resetuser

**Description:** Reset a user's cooldowns, stats, or everything.

**Usage:** `<@1275521742961508432>casino resetuser`

### casino version

**Description:** Shows the current Casino version.

**Usage:** `<@1275521742961508432>casino version`

### casino memberships

**Description:** Displays a list of server/global memberships.

**Usage:** `<@1275521742961508432>casino memberships`

### casino releasecredits

**Description:** Approves pending currency for a user.

If this casino has maximum winnings threshold set, and a user makes a bet that
exceeds this amount, then they will have those credits with held. This command will
Allow you to release those credits back to the user. This system is designed to limit
earnings when a player may have found a way to cheat a game.

**Usage:** `<@1275521742961508432>casino releasecredits`

### casinoset

**Description:** Changes Casino settings

**Usage:** `<@1275521742961508432>casinoset`

### casinoset assignmem

**Description:** Manually assigns a membership to a user.

Users who are assigned a membership no longer need to meet the
requirements set. However, if the membership is revoked, then the
user will need to meet the requirements as usual.

**Usage:** `<@1275521742961508432>casinoset assignmem`

### casinoset memdesigner

**Description:** A process to create, edit, and delete memberships.

**Usage:** `<@1275521742961508432>casinoset memdesigner`

### casinoset oldstyle

**Description:** Toggle between editing and sending new messages for casino games..

**Usage:** `<@1275521742961508432>casinoset oldstyle`

### casinoset max

**Description:** Sets the maximum bid for a game.

**Usage:** `<@1275521742961508432>casinoset max`

### casinoset payouttoggle

**Description:** Turns on a payout limit.

The payout limit will withhold winnings from players until they are approved by the
appropriate authority. To set the limit, use payoutlimit.

**Usage:** `<@1275521742961508432>casinoset payouttoggle`

### casinoset min

**Description:** Sets the minimum bid for a game.

**Usage:** `<@1275521742961508432>casinoset min`

### casinoset access

**Description:** Sets the access level required to play a game.

Access levels are used in conjunction with memberships. To read more on using
access levels and memberships please refer to the casino wiki.

**Usage:** `<@1275521742961508432>casinoset access`

### casinoset revokemem

**Description:** Revoke an assigned membership.

Members will still keep this membership until the next auto cycle (5mins).
At that time, they will be re-evaluated and downgraded/upgraded appropriately.

**Usage:** `<@1275521742961508432>casinoset revokemem`

### casinoset gametoggle

**Description:** Opens/Closes a specific game for use.

**Usage:** `<@1275521742961508432>casinoset gametoggle`

### casinoset mode

**Description:** Toggles Casino between global and local modes.

When casino is set to local mode, each server will have its own
unique data, and admin level commands can be used on that server.

When casino is set to global mode, data is linked between all servers
the bot is connected to. In addition, admin level commands can only be
used by the owner or co-owners.

**Usage:** `<@1275521742961508432>casinoset mode`

### casinoset multiplier

**Description:** Sets the payout multiplier for a game.
        

**Usage:** `<@1275521742961508432>casinoset multiplier`

### casinoset cooldown

**Description:** Sets the cooldown for a game.

You can use the format DD:HH:MM:SS to set a time, or just simply
type the number of seconds.

**Usage:** `<@1275521742961508432>casinoset cooldown`

### casinoset name

**Description:** Sets the name of the Casino.

The casino name may only be 30 characters in length.

**Usage:** `<@1275521742961508432>casinoset name`

### casinoset toggle

**Description:** Opens and closes the Casino for use.

This command only restricts the use of playing games.

**Usage:** `<@1275521742961508432>casinoset toggle`

### casinoset payoutlimit

**Description:** Sets a payout limit.

Users who exceed this amount will have their winnings witheld until they are
reviewed and approved by the appropriate authority. Limits are only triggered if
payout limits are ON. To turn on payout limits, use payouttoggle.

**Usage:** `<@1275521742961508432>casinoset payoutlimit`

