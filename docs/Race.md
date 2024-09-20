# Race Help

### race

**Description:** Race related commands.

**Usage:** `<@1275521742961508432>race`

### race wipe

**Description:** This command will wipe ALL race data.

You are given a confirmation dialog when using this command.
If you decide to wipe your data, all stats and settings will be deleted.

**Usage:** `<@1275521742961508432>race wipe`

### race enter

**Description:** Allows you to enter the race.

This command will return silently if a race has already started.
By not repeatedly telling the user that they can't enter the race, this
prevents spam.

**Usage:** `<@1275521742961508432>race enter`

### race version

**Description:** Displays the version of race.

**Usage:** `<@1275521742961508432>race version`

### race bet

**Description:** Bet on a user in the race.

**Usage:** `<@1275521742961508432>race bet`

### race start

**Description:** Begins a new race.

You cannot start a new race until the active on has ended.

If you are the only player in the race, you will race against
your bot.

The user who started the race is automatically entered into the race.

**Usage:** `<@1275521742961508432>race start`

### race stats

**Description:** Display your race stats.

**Usage:** `<@1275521742961508432>race stats`

### setrace

**Description:** Race settings commands.

**Usage:** `<@1275521742961508432>setrace`

### setrace bet

**Description:** Bet settings for race.

**Usage:** `<@1275521742961508432>setrace bet`

### setrace bet max

**Description:** Sets the betting maximum.

**Usage:** `<@1275521742961508432>setrace bet max`

### setrace bet multiplier

**Description:** Sets the betting multiplier.

If the bot's economy mode is set to global instead of server-based, this setting is not available.

**Usage:** `<@1275521742961508432>setrace bet multiplier`

### setrace bet min

**Description:** Sets the betting minimum.

**Usage:** `<@1275521742961508432>setrace bet min`

### setrace bet toggle

**Description:** Toggles betting on and off.

**Usage:** `<@1275521742961508432>setrace bet toggle`

### setrace payoutmin

**Description:** Sets the number of players needed to payout prizes and bets.

This sets the required number of players needed to payout prizes.
If the number of racers aren't met, then nothing is paid out.

The person starting the race is not counted in this minimum number.
For example, if you are playing alone vs. the bot and the payout min
is set to 1, you need 1 human player besides the race starter for a
payout to occur.

If you want race to always pay out, then set players to 0.

**Usage:** `<@1275521742961508432>setrace payoutmin`

### setrace mode

**Description:** Changes the race mode.

Race can either be in normal mode or zoo mode.

Normal Mode:
    All racers are turtles.

Zoo Mode:
    Racers are randomly selected from a list of animals with
    different attributes.

**Usage:** `<@1275521742961508432>setrace mode`

### setrace prize

**Description:** Sets the prize pool for winners.

Set the prize to 0 if you do not wish any credits to be distributed.

When prize pooling is enabled (see `[p]setrace togglepool`) the prize 
will be distributed as follows:
    1st place 60%
    2nd place 30%
    3rd place 10%

Example:
    100 results in 60, 30, 10
    130 results in 78, 39, 13

When prize pooling is disabled, only first place will win, and they take
100% of the winnings.

**Usage:** `<@1275521742961508432>setrace prize`

### setrace togglepool

**Description:** Toggles on/off prize pooling.

Makes it so that prizes are pooled between 1st, 2nd, and 3rd.
It's a 60/30/10 split rounded to the nearest whole number.

There must be at least four human players, otherwise, only first
place wins.

**Usage:** `<@1275521742961508432>setrace togglepool`

### setrace wait

**Description:** Changes the wait time before a race starts.

This only affects the period where race is still waiting
for more participants to join the race.

**Usage:** `<@1275521742961508432>setrace wait`

