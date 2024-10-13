Various developer utilities.

# ,do
Repeats a command a specified number of times.<br/>

`--sleep <int>` is an optional flag specifying how much time to wait between command invocations.<br/>
 - Usage: `,do <times> [sequential=True] <command>`
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
# ,execute
Execute multiple commands at once. Split them using |.<br/>
 - Usage: `,execute [sequential=False] <commands>`
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
# ,bypass
Bypass a command's checks and cooldowns.<br/>
 - Usage: `,bypass <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,timing
Run a command timing execution and catching exceptions.<br/>
 - Usage: `,timing <command_string>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,schedulecmd
Schedule a command to be done later.<br/>
 - Usage: `,schedulecmd <time> <command>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `taskcmd`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,reinvoke
Reinvoke a command message.<br/>

You may reply to a message to reinvoke it or pass a message ID/link.<br/>
 - Usage: `,reinvoke [message=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### message: discord.message.Message = None
> Converts to a :class:`discord.Message`.
> 
>     
# ,loglevel
Set the log output level.<br/>
 - Usage: `,loglevel <level>`
 - Restricted to: `BOT_OWNER`
