Dev
===

<<<<<<< HEAD
Various development focused utilities!

# <@1275521742961508432>mock
Mock another user invoking a command.<br/>

The prefix must not be entered.<br/>
 - Usage: `<@1275521742961508432>mock <user> <command>`
=======
Various development focused utilities.

# ,debug
Evaluate a statement of python code.<br/>

The bot will always respond with the return value of the code.<br/>
If the return value of the code is a coroutine, it will be awaited,<br/>
and the result of that will be the bot's response.<br/>

Note: Only one statement may be evaluated. Using certain restricted<br/>
keywords, e.g. yield, will result in a syntax error. For multiple<br/>
lines or asynchronous code, see ,repl or ,eval.<br/>

Environment Variables:<br/>
    `ctx`      - the command invocation context<br/>
    `bot`      - the bot object<br/>
    `channel`  - the current channel object<br/>
    `author`   - the command author's member object<br/>
    `server`    - the current server object<br/>
    `message`  - the command's message object<br/>
    `_`        - the result of the last dev command<br/>
    `aiohttp`  - the aiohttp library<br/>
    `asyncio`  - the asyncio library<br/>
    `discord`  - the discord.py library<br/>
    `commands` - the redbot.core.commands module<br/>
    `cf`       - the redbot.core.utils.chat_formatting module<br/>
 - Usage: `,debug <code>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,eval
Execute asynchronous code.<br/>

This command wraps code into the body of an async function and then<br/>
calls and awaits it. The bot will respond with anything printed to<br/>
stdout, as well as the return value of the function.<br/>

The code can be within a codeblock, inline code or neither, as long<br/>
as they are not mixed and they are formatted correctly.<br/>

Environment Variables:<br/>
    `ctx`      - the command invocation context<br/>
    `bot`      - the bot object<br/>
    `channel`  - the current channel object<br/>
    `author`   - the command author's member object<br/>
    `server`    - the current server object<br/>
    `message`  - the command's message object<br/>
    `_`        - the result of the last dev command<br/>
    `aiohttp`  - the aiohttp library<br/>
    `asyncio`  - the asyncio library<br/>
    `discord`  - the discord.py library<br/>
    `commands` - the redbot.core.commands module<br/>
    `cf`       - the redbot.core.utils.chat_formatting module<br/>
 - Usage: `,eval <body>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### body: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,repl
Open an interactive REPL.<br/>

The REPL will only recognise code as messages which start with a<br/>
backtick. This includes codeblocks, and as such multiple lines can be<br/>
evaluated.<br/>

Use `exit()` or `quit` to exit the REPL session, prefixed with<br/>
a backtick so they may be interpreted.<br/>

Environment Variables:<br/>
    `ctx`      - the command invocation context<br/>
    `bot`      - the bot object<br/>
    `channel`  - the current channel object<br/>
    `author`   - the command author's member object<br/>
    `server`    - the current server object<br/>
    `message`  - the command's message object<br/>
    `_`        - the result of the last dev command<br/>
    `aiohttp`  - the aiohttp library<br/>
    `asyncio`  - the asyncio library<br/>
    `discord`  - the discord.py library<br/>
    `commands` - the redbot.core.commands module<br/>
    `cf`       - the redbot.core.utils.chat_formatting module<br/>
 - Usage: `,repl`
 - Restricted to: `BOT_OWNER`


## ,repl pause
Pauses/resumes the REPL running in the current channel.<br/>
 - Usage: `,repl pause [toggle=None]`
 - Aliases: `resume`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


# ,mimic
Mimic another user invoking a command.<br/>

The prefix must not be entered.<br/>
 - Usage: `,mimic <user> <command>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
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
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>mockmsg
=======
# ,mimicmsg
>>>>>>> 9e308722 (Revamped and Fixed)
Dispatch a message event as if it were sent by a different user.<br/>

Current message is used as a base (including attachments, embeds, etc.),<br/>
the content and author of the message are replaced with the given arguments.<br/>

Note: If `content` isn't passed, the message needs to contain embeds, attachments,<br/>
or anything else that makes the message non-empty.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>mockmsg <user> [content]`
=======
 - Usage: `,mimicmsg <user> [content]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
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
> ### content: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>debug (Hybrid Command)
Evaluate a statement of python code.<br/>

The bot will always respond with the return value of the code.<br/>
If the return value of the code is a coroutine, it will be awaited,<br/>
and the result of that will be the bot's response.<br/>

Note: Only one statement may be evaluated. Using certain restricted<br/>
keywords, e.g. yield, will result in a syntax error. For multiple<br/>
lines or asynchronous code, see <@1275521742961508432>repl or <@1275521742961508432>eval.<br/>

The code can be within a codeblock, inline code or neither, as long as they are not mixed and they are formatted correctly.<br/>
You can upload a file with the code to be executed, or reply to a message containing the command, from any bot.<br/>

Environment Variables:<br/>
    `ctx`      - the command invocation context<br/>
    `bot`      - the bot object<br/>
    `channel`  - the current channel object<br/>
    `author`   - the command author's member object<br/>
    `server`    - the current server object<br/>
    `message`  - the command's message object<br/>
    `_`        - the result of the last dev command<br/>
    `aiohttp`  - the aiohttp library<br/>
    `asyncio`  - the asyncio library<br/>
    `discord`  - the discord.py library<br/>
    `commands` - the redbot.core.commands module<br/>
    `cf`       - the redbot.core.utils.chat_formatting module<br/>
(See `<@1275521742961508432>setdev getenvironment` for more.)<br/>
 - Usage: `<@1275521742961508432>debug [code]`
 - Slash Usage: `/debug [code]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### code: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>eval (Hybrid Command)
Execute asynchronous code.<br/>

This command wraps code into the body of an async function and then<br/>
calls and awaits it. The bot will respond with anything printed to<br/>
stdout, as well as the return value of the function.<br/>

The code can be within a codeblock, inline code or neither, as long as they are not mixed and they are formatted correctly.<br/>
You can upload a file with the code to be executed, or reply to a message containing the command, from any bot.<br/>

Environment Variables:<br/>
    `ctx`      - the command invocation context<br/>
    `bot`      - the bot object<br/>
    `channel`  - the current channel object<br/>
    `author`   - the command author's member object<br/>
    `server`    - the current server object<br/>
    `message`  - the command's message object<br/>
    `_`        - the result of the last dev command<br/>
    `aiohttp`  - the aiohttp library<br/>
    `asyncio`  - the asyncio library<br/>
    `discord`  - the discord.py library<br/>
    `commands` - the redbot.core.commands module<br/>
    `cf`       - the redbot.core.utils.chat_formatting module<br/>
(See `<@1275521742961508432>setdev getenvironment` for more.)<br/>
 - Usage: `<@1275521742961508432>eval [body]`
 - Slash Usage: `/eval [body]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### body: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>repl (Hybrid Command)
Open an interactive REPL.<br/>

The REPL will only recognise code as messages which start with a<br/>
backtick. This includes codeblocks, and as such multiple lines can be<br/>
evaluated.<br/>

Use `exit()` or `quit` to exit the REPL session, prefixed with<br/>
a backtick so they may be interpreted.<br/>

You can upload a file with the code to be executed, or reply to a message containing the same command, for any bot.<br/>

Environment Variables:<br/>
    `ctx`      - the command invocation context<br/>
    `bot`      - the bot object<br/>
    `channel`  - the current channel object<br/>
    `author`   - the command author's member object<br/>
    `server`    - the current server object<br/>
    `message`  - the command's message object<br/>
    `_`        - the result of the last dev command<br/>
    `aiohttp`  - the aiohttp library<br/>
    `asyncio`  - the asyncio library<br/>
    `discord`  - the discord.py library<br/>
    `commands` - the redbot.core.commands module<br/>
    `cf`       - the redbot.core.utils.chat_formatting module<br/>
(See `<@1275521742961508432>setdev getenvironment` for more.)<br/>
 - Usage: `<@1275521742961508432>repl`
 - Slash Usage: `/repl`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>replpause (Hybrid Command)
Pauses/resumes the REPL running in the current channel.<br/>
 - Usage: `<@1275521742961508432>replpause [toggle=None]`
 - Slash Usage: `/replpause [toggle=None]`
 - Restricted to: `BOT_OWNER`
 - Aliases: `replresume`
Extended Arg Info
=======
# ,bypasscooldowns
Give bot owners the ability to bypass cooldowns.<br/>

Does not persist through restarts.<br/>
 - Usage: `,bypasscooldowns [toggle=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
>>>>>>> 9e308722 (Revamped and Fixed)
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
# <@1275521742961508432>bypasscooldowns (Hybrid Command)
Give bot owners the ability to bypass cooldowns.<br/>

Does not persist through restarts.<br/>
 - Usage: `<@1275521742961508432>bypasscooldowns [toggle=None] [time]`
 - Slash Usage: `/bypasscooldowns [toggle=None] [time]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### toggle: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>eshell (Hybrid Command)
Execute Shell commands.<br/>

This command wraps the shell command into a Python code to invoke them.<br/>

The code can be within a codeblock, inline code or neither, as long as they are not mixed and they are formatted correctly.<br/>
You can upload a file with the code to be executed, or reply to a message containing the command, from any bot.<br/>
 - Usage: `<@1275521742961508432>eshell [silent=False] [command]`
 - Slash Usage: `/eshell [silent=False] [command]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### silent: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### command: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>setdev (Hybrid Command)
Commands to configure Dev.<br/>
 - Usage: `<@1275521742961508432>setdev`
 - Slash Usage: `/setdev`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>setdev getenvironment (Hybrid Command)
Display all Dev environment values.<br/>
 - Usage: `<@1275521742961508432>setdev getenvironment [show_values=True]`
 - Slash Usage: `/setdev getenvironment [show_values=True]`
 - Aliases: `getenv, getformattedenvironment, and getformattedenv`
Extended Arg Info
> ### show_values: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `<@1275521742961508432>setdev resetsetting <setting>`
 - Slash Usage: `/setdev resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setdev sendinteractive (Hybrid Command)
Send results with `commands.Context.send_interactive`, not a Menu.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev sendinteractive <value>`
 - Slash Usage: `/setdev sendinteractive <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev uselastlocals (Hybrid Command)
Use the last locals for each evals. Locals are only registered for `<@1275521742961508432>eval`, but can be used in other commands.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev uselastlocals <value>`
 - Slash Usage: `/setdev uselastlocals <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev senddpyobjects (Hybrid Command)
If the result is an embed/file/attachment object or an iterable of these, send.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev senddpyobjects <value>`
 - Slash Usage: `/setdev senddpyobjects <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev ansiformatting (Hybrid Command)
Use the `ansi` formatting for results.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev ansiformatting <value>`
 - Slash Usage: `/setdev ansiformatting <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev useextendedenvironment (Hybrid Command)
Use my own Dev env with useful values.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev useextendedenvironment <value>`
 - Slash Usage: `/setdev useextendedenvironment <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>setdev showsettings [with_dev=False]`
 - Slash Usage: `/setdev showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev autoimports (Hybrid Command)
Enable or disable auto imports.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev autoimports <value>`
 - Slash Usage: `/setdev autoimports <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev outputmode (Hybrid Command)
Set the output mode. `repr` is to display the repr of the result. `repr_or_str` is to display in the same way, but a string as a string. `str` is to display the string of the result.<br/>

Default value: `repr`<br/>
Dev: `typing.Literal['repr', 'repr_or_str', 'str']`<br/>
 - Usage: `<@1275521742961508432>setdev outputmode <value>`
 - Slash Usage: `/setdev outputmode <value>`


## <@1275521742961508432>setdev downloaderalreadyagreed (Hybrid Command)
If enabled, Downloader will no longer prompt you to type `I agree` when adding a repo, even after a bot restart.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev downloaderalreadyagreed <value>`
 - Slash Usage: `/setdev downloaderalreadyagreed <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `<@1275521742961508432>setdev modalconfig [confirmation=False]`
 - Slash Usage: `/setdev modalconfig [confirmation=False]`
 - Aliases: `configmodal`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev richtracebacks (Hybrid Command)
Use `rich` to display tracebacks.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdev richtracebacks <value>`
 - Slash Usage: `/setdev richtracebacks <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdev resetlocals (Hybrid Command)
Reset its own locals in evals.<br/>
 - Usage: `<@1275521742961508432>setdev resetlocals`
 - Slash Usage: `/setdev resetlocals`
 - Aliases: `rlocals`


=======
>>>>>>> 9e308722 (Revamped and Fixed)
