Trivia
======

Play trivia with friends!

# <@1275521742961508432>triviaset
Manage Trivia settings.<br/>
 - Usage: `<@1275521742961508432>triviaset`
 - Restricted to: `MOD`
 - Checks: `server_only`


## <@1275521742961508432>triviaset usespoilers
Set if bot will display the answers in spoilers.<br/>

If enabled, the bot will use spoilers to hide answers.<br/>
 - Usage: `<@1275521742961508432>triviaset usespoilers <enabled>`
Extended Arg Info
> ### enabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>triviaset botplays
Set whether or not the bot gains points.<br/>

If enabled, the bot will gain a point if no one guesses correctly.<br/>
 - Usage: `<@1275521742961508432>triviaset botplays <enabled>`
Extended Arg Info
> ### enabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>triviaset maxscore
Set the total points required to win.<br/>
 - Usage: `<@1275521742961508432>triviaset maxscore <score>`
Extended Arg Info
> ### score: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>triviaset showsettings
Show the current trivia settings.<br/>
 - Usage: `<@1275521742961508432>triviaset showsettings`


## <@1275521742961508432>triviaset payout
Set the payout multiplier.<br/>

This can be any positive decimal number. If a user wins trivia when at<br/>
least 3 members are playing, they will receive credits. Set to 0 to<br/>
disable.<br/>

The number of credits is determined by multiplying their total score by<br/>
this multiplier.<br/>
 - Usage: `<@1275521742961508432>triviaset payout <multiplier>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`


## <@1275521742961508432>triviaset custom
Manage Custom Trivia lists.<br/>
 - Usage: `<@1275521742961508432>triviaset custom`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>triviaset custom upload
Upload a trivia file.<br/>
 - Usage: `<@1275521742961508432>triviaset custom upload`
 - Restricted to: `BOT_OWNER`
 - Aliases: `add`


### <@1275521742961508432>triviaset custom delete
Delete a trivia file.<br/>
 - Usage: `<@1275521742961508432>triviaset custom delete <name>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `remove`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>triviaset custom list
List uploaded custom trivia.<br/>
 - Usage: `<@1275521742961508432>triviaset custom list`


## <@1275521742961508432>triviaset override
Allow/disallow trivia lists to override settings.<br/>
 - Usage: `<@1275521742961508432>triviaset override <enabled>`
Extended Arg Info
> ### enabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>triviaset revealanswer
Set whether or not the answer is revealed.<br/>

If enabled, the bot will reveal the answer if no one guesses correctly<br/>
in time.<br/>
 - Usage: `<@1275521742961508432>triviaset revealanswer <enabled>`
Extended Arg Info
> ### enabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>triviaset stopafter
Set how long until trivia stops due to no response.<br/>
 - Usage: `<@1275521742961508432>triviaset stopafter <seconds>`


## <@1275521742961508432>triviaset timelimit
Set the maximum seconds permitted to answer a question.<br/>
 - Usage: `<@1275521742961508432>triviaset timelimit <seconds>`


# <@1275521742961508432>trivia
Start trivia session on the specified category.<br/>

You may list multiple categories, in which case the trivia will involve<br/>
questions from all of them.<br/>
 - Usage: `<@1275521742961508432>trivia <categories>`
 - Checks: `server_only`
Extended Arg Info
> ### *categories: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>trivia stop
Stop an ongoing trivia session.<br/>
 - Usage: `<@1275521742961508432>trivia stop`


## <@1275521742961508432>trivia info
Get information about a trivia category.<br/>
 - Usage: `<@1275521742961508432>trivia info <category>`


## <@1275521742961508432>trivia list
List available trivia categories.<br/>
 - Usage: `<@1275521742961508432>trivia list`


## <@1275521742961508432>trivia leaderboard
Leaderboard for trivia.<br/>

Defaults to the top 10 of this server, sorted by total wins. Use<br/>
subcommands for a more customised leaderboard.<br/>
 - Usage: `<@1275521742961508432>trivia leaderboard`
 - Aliases: `lboard`


### <@1275521742961508432>trivia leaderboard server
Leaderboard for this server.<br/>

`<sort_by>` can be any of the following fields:<br/>
 - `wins`  : total wins<br/>
 - `avg`   : average score<br/>
 - `total` : total correct answers<br/>
 - `games` : total games played<br/>

`<top>` is the number of ranks to show on the leaderboard.<br/>
 - Usage: `<@1275521742961508432>trivia leaderboard server [sort_by=wins] [top=10]`
 - Checks: `server_only`
Extended Arg Info
> ### sort_by: str = 'wins'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### top: int = 10
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>trivia leaderboard global
Global trivia leaderboard.<br/>

`<sort_by>` can be any of the following fields:<br/>
 - `wins`  : total wins<br/>
 - `avg`   : average score<br/>
 - `total` : total correct answers from all sessions<br/>
 - `games` : total games played<br/>

`<top>` is the number of ranks to show on the leaderboard.<br/>
 - Usage: `<@1275521742961508432>trivia leaderboard global [sort_by=wins] [top=10]`
Extended Arg Info
> ### sort_by: str = 'wins'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### top: int = 10
> ```
> A number without decimal places.
> ```


