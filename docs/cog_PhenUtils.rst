PhenUtils
=========

Various developer utilities.

<<<<<<< HEAD
# <@1275521742961508432>do
Repeats a command a specified number of times.<br/>

`--sleep <int>` is an optional flag specifying how much time to wait between command invocations.<br/>
 - Usage: `<@1275521742961508432>do <times> [sequential=True] <command>`
=======
# ,do
Repeats a command a specified number of times.<br/>

`--sleep <int>` is an optional flag specifying how much time to wait between command invocations.<br/>
 - Usage: `,do <times> [sequential=True] <command>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### times: int
> ```
> A number without decimal places.
> ```
> ### sequential: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>execute
Execute multiple commands at once. Split them using |.<br/>
 - Usage: `<@1275521742961508432>execute [sequential=False] <commands>`
=======
# ,execute
Execute multiple commands at once. Split them using |.<br/>
 - Usage: `,execute [sequential=False] <commands>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### sequential: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### commands
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>bypass
Bypass a command's checks and cooldowns.<br/>
 - Usage: `<@1275521742961508432>bypass <command>`
=======
# ,bypass
Bypass a command's checks and cooldowns.<br/>
 - Usage: `,bypass <command>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>timing
Run a command timing execution and catching exceptions.<br/>
 - Usage: `<@1275521742961508432>timing <command_string>`
=======
# ,timing
Run a command timing execution and catching exceptions.<br/>
 - Usage: `,timing <command_string>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>schedulecmd
Schedule a command to be done later.<br/>
 - Usage: `<@1275521742961508432>schedulecmd <time> <command>`
=======
# ,schedulecmd
Schedule a command to be done later.<br/>
 - Usage: `,schedulecmd <time> <command>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `taskcmd`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>reinvoke
Reinvoke a command message.<br/>

You may reply to a message to reinvoke it or pass a message ID/link.<br/>
 - Usage: `<@1275521742961508432>reinvoke [message=None]`
=======
# ,reinvoke
Reinvoke a command message.<br/>

You may reply to a message to reinvoke it or pass a message ID/link.<br/>
 - Usage: `,reinvoke [message=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### message: discord.message.Message = None
> Converts to a :class:`discord.Message`.
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>loglevel
Set the log output level.<br/>
 - Usage: `<@1275521742961508432>loglevel <level>`
=======
# ,loglevel
Set the log output level.<br/>
 - Usage: `,loglevel <level>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`


