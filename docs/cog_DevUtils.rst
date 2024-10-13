DevUtils
========

Various development utilities!

# ,devutils (Hybrid Command)
Various development utilities.<br/>
 - Usage: `,devutils`
 - Slash Usage: `/devutils`
 - Restricted to: `BOT_OWNER`


## ,devutils reloadmodule (Hybrid Command)
Force reload a module (to use code changes without restarting your bot).<br/>

⚠️ Please only use this if you know what you're doing.<br/>
 - Usage: `,devutils reloadmodule <modules>`
 - Slash Usage: `/devutils reloadmodule <modules>`


## ,devutils execute (Hybrid Command)
Execute multiple commands at once. Split them using |.<br/>
 - Usage: `,devutils execute [sequential=True] <commands_list>`
 - Slash Usage: `/devutils execute [sequential=True] <commands_list>`
Extended Arg Info
> ### sequential: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### commands_list: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,devutils stoptyping (Hybrid Command)
Stop all bot typing tasks.<br/>
 - Usage: `,devutils stoptyping`
 - Slash Usage: `/devutils stoptyping`


## ,devutils do (Hybrid Command)
Repeats a command a specified number of times.<br/>

`--sleep <int>` is an optional flag specifying how much time to wait between command invocations.<br/>
 - Usage: `,devutils do <times> [sequential=True] <command>`
 - Slash Usage: `/devutils do <times> [sequential=True] <command>`
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


## ,devutils rawrequest (Hybrid Command)
Display the JSON of a Discord object with a raw request.<br/>
 - Usage: `,devutils rawrequest <thing>`
 - Slash Usage: `/devutils rawrequest <thing>`
 - Aliases: `rawcontent`


## ,devutils timing (Hybrid Command)
Run a command timing execution and catching exceptions.<br/>
 - Usage: `,devutils timing <command>`
 - Slash Usage: `/devutils timing <command>`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,devutils bypass (Hybrid Command)
Bypass a command's checks and cooldowns.<br/>
 - Usage: `,devutils bypass <command>`
 - Slash Usage: `/devutils bypass <command>`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,devutils loglevel (Hybrid Command)
Change the logging level for a logger. If no name is provided, the root logger (`red`) is used.<br/>

Levels are the following:<br/>
- `0`: `CRITICAL`<br/>
- `1`: `ERROR`<br/>
- `2`: `WARNING`<br/>
- `3`: `INFO`<br/>
- `4`: `DEBUG`<br/>
- `5`: `VERBOSE`<br/>
- `6`: `TRACE`<br/>
 - Usage: `,devutils loglevel <level> [logger_name=red]`
 - Slash Usage: `/devutils loglevel <level> [logger_name=red]`
Extended Arg Info
> ### logger_name: str = 'red'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,devutils reinvoke (Hybrid Command)
Reinvoke a command message.<br/>

You may reply to a message to reinvoke it or pass a message ID/link.<br/>
The command will be invoked with the author and the channel of the specified message.<br/>
 - Usage: `,devutils reinvoke [message=None]`
 - Slash Usage: `/devutils reinvoke [message=None]`
Extended Arg Info
> ### message: discord.message.Message = None
> Converts to a :class:`discord.Message`.
> 
>     


