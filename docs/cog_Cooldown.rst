Cooldown
========

Add or remove cooldowns from/to commands

WARNING: Some cooldowns are meant to be in place, meaning that they should not be removed.
Any contributors to this cog are not at fault if it is used improperly, and is instead at
the fault of the person running the command.  By installing this cog, you agree to these terms.

# ,cooldown
Group command for working with cooldowns for commands.<br/>
 - Usage: `,cooldown`
 - Restricted to: `BOT_OWNER`


## ,cooldown add
Sets a cooldown for a command, allowing a certain amount of times in a certain amount of time for a certain type.  If a cooldown already exists for the specified command, then it will be overwritten and edited.<br/>

The command argument does not require quotes, as it consumes the rest in order to make cooldowns for subcommands easier.<br/>

Example: `,cooldown add 1 5s user ping`<br/>

The above example will limit a user to using the `ping` command every 5 seconds.<br/>

Example 2: `,cooldown add 5 10m server alias add`<br/>

The above example (number 2) will limit people in a server to using the `alias add` command to 5 times every 10 minutes.<br/>

Time Types:<br/>
-   S   =>  Seconds<br/>
-   M   =>  Minutes<br/>
-   H   =>  Hours<br/>
-   D   =>  Days<br/>

Bucket Types:<br/>
-   User<br/>
-   Channel<br/>
-   Guild<br/>
-   Global<br/>

Arguments:<br/>
-   Rate:      how many times<br/>
-   Per:       during how long<br/>
-   Type:      for what type<br/>
-   Command:   for what command.  Do not use a prefix, and does not work with aliases.  Please pass the actual command for the alias if you wish.<br/>
 - Usage: `,cooldown add <rate> <per> <btype> <command>`
Extended Arg Info
> ### rate: int
> ```
> A number without decimal places.
> ```
> ### per
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### btype
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,cooldown remove
Removes the cooldown from a command.<br/>

The cooldown can be one set from this cog or from inside the cog's code.<br/>

The command argument does not require quotes, as it consumes the rest in order to make cooldowns for subcommands easier.<br/>

Please do note however: some commands are meant to have cooldowns.  They may prevent something malicious from happening, or maybe your device from breaking or from being used too much.  I (Neuro Assassin <@473541068378341376>) or any other contributor to this cog take no responsibility for any complications that may result because of this.  Use at your own risk.<br/>

Note: Does not actually remove the command cooldown (undocumented), so instead it allows for the command to be run 100000 times every 1 second until the next boot up, where it will not be added (unless you are removing a cooldown from outside of this cog, then it will be kept after restart).<br/>
 - Usage: `,cooldown remove <command>`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


