# Trivia Help

### triviaset

**Description:** Manage Trivia settings.

**Usage:** `<@1275521742961508432>triviaset`

### triviaset maxscore

**Description:** Set the total points required to win.

**Usage:** `<@1275521742961508432>triviaset maxscore`

### triviaset payout

**Description:** Set the payout multiplier.

This can be any positive decimal number. If a user wins trivia when at
least 3 members are playing, they will receive credits. Set to 0 to
disable.

The number of credits is determined by multiplying their total score by
this multiplier.

**Usage:** `<@1275521742961508432>triviaset payout`

### triviaset custom

**Description:** Manage Custom Trivia lists.

**Usage:** `<@1275521742961508432>triviaset custom`

### triviaset custom upload

**Description:** Upload a trivia file.

**Usage:** `<@1275521742961508432>triviaset custom upload`

### triviaset custom delete

**Description:** Delete a trivia file.

**Usage:** `<@1275521742961508432>triviaset custom delete`

### triviaset custom list

**Description:** List uploaded custom trivia.

**Usage:** `<@1275521742961508432>triviaset custom list`

### triviaset showsettings

**Description:** Show the current trivia settings.

**Usage:** `<@1275521742961508432>triviaset showsettings`

### triviaset override

**Description:** Allow/disallow trivia lists to override settings.

**Usage:** `<@1275521742961508432>triviaset override`

### triviaset botplays

**Description:** Set whether or not the bot gains points.

If enabled, the bot will gain a point if no one guesses correctly.

**Usage:** `<@1275521742961508432>triviaset botplays`

### triviaset stopafter

**Description:** Set how long until trivia stops due to no response.

**Usage:** `<@1275521742961508432>triviaset stopafter`

### triviaset timelimit

**Description:** Set the maximum seconds permitted to answer a question.

**Usage:** `<@1275521742961508432>triviaset timelimit`

### triviaset revealanswer

**Description:** Set whether or not the answer is revealed.

If enabled, the bot will reveal the answer if no one guesses correctly
in time.

**Usage:** `<@1275521742961508432>triviaset revealanswer`

### triviaset usespoilers

**Description:** Set if bot will display the answers in spoilers.

If enabled, the bot will use spoilers to hide answers.

**Usage:** `<@1275521742961508432>triviaset usespoilers`

### trivia

**Description:** Start trivia session on the specified category.

You may list multiple categories, in which case the trivia will involve
questions from all of them.

**Usage:** `<@1275521742961508432>trivia`

### trivia stop

**Description:** Stop an ongoing trivia session.

**Usage:** `<@1275521742961508432>trivia stop`

### trivia leaderboard

**Description:** Leaderboard for trivia.

Defaults to the top 10 of this server, sorted by total wins. Use
subcommands for a more customised leaderboard.

**Usage:** `<@1275521742961508432>trivia leaderboard`

### trivia leaderboard server

**Description:** Leaderboard for this server.

`<sort_by>` can be any of the following fields:
 - `wins`  : total wins
 - `avg`   : average score
 - `total` : total correct answers
 - `games` : total games played

`<top>` is the number of ranks to show on the leaderboard.

**Usage:** `<@1275521742961508432>trivia leaderboard server`

### trivia leaderboard global

**Description:** Global trivia leaderboard.

`<sort_by>` can be any of the following fields:
 - `wins`  : total wins
 - `avg`   : average score
 - `total` : total correct answers from all sessions
 - `games` : total games played

`<top>` is the number of ranks to show on the leaderboard.

**Usage:** `<@1275521742961508432>trivia leaderboard global`

### trivia list

**Description:** List available trivia categories.

**Usage:** `<@1275521742961508432>trivia list`

### trivia info

**Description:** Get information about a trivia category.

**Usage:** `<@1275521742961508432>trivia info`

