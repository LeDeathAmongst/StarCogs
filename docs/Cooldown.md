# Cooldown Help

### cooldown

**Description:** Group command for working with cooldowns for commands.

**Usage:** `<@1275521742961508432>cooldown`

### cooldown add

**Description:** Sets a cooldown for a command, allowing a certain amount of times in a certain amount of time for a certain type.  If a cooldown already exists for the specified command, then it will be overwritten and edited.

The command argument does not require quotes, as it consumes the rest in order to make cooldowns for subcommands easier.

Example: `[p]cooldown add 1 5s user ping`

The above example will limit a user to using the `ping` command every 5 seconds.

Example 2: `[p]cooldown add 5 10m guild alias add`

The above example (number 2) will limit people in a guild to using the `alias add` command to 5 times every 10 minutes.

Time Types:
-   S   =>  Seconds
-   M   =>  Minutes
-   H   =>  Hours
-   D   =>  Days

Bucket Types:
-   User
-   Channel
-   Guild
-   Global

Arguments:
-   Rate:      how many times
-   Per:       during how long
-   Type:      for what type
-   Command:   for what command.  Do not use a prefix, and does not work with aliases.  Please pass the actual command for the alias if you wish.

**Usage:** `<@1275521742961508432>cooldown add`

### cooldown remove

**Description:** Removes the cooldown from a command.

The cooldown can be one set from this cog or from inside the cog's code.

The command argument does not require quotes, as it consumes the rest in order to make cooldowns for subcommands easier.

Please do note however: some commands are meant to have cooldowns.  They may prevent something malicious from happening, or maybe your device from breaking or from being used too much.  I (Neuro Assassin <@473541068378341376>) or any other contributor to this cog take no responsibility for any complications that may result because of this.  Use at your own risk.

Note: Does not actually remove the command cooldown (undocumented), so instead it allows for the command to be run 100000 times every 1 second until the next boot up, where it will not be added (unless you are removing a cooldown from outside of this cog, then it will be kept after restart).

**Usage:** `<@1275521742961508432>cooldown remove`

