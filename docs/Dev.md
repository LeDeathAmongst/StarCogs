# Dev Help

### mock

**Description:** Mock another user invoking a command.

The prefix must not be entered.

**Usage:** `<@1275521742961508432>mock`

### mockmsg

**Description:** Dispatch a message event as if it were sent by a different user.

Current message is used as a base (including attachments, embeds, etc.),
the content and author of the message are replaced with the given arguments.

Note: If `content` isn't passed, the message needs to contain embeds, attachments,
or anything else that makes the message non-empty.

**Usage:** `<@1275521742961508432>mockmsg`

### debug

**Description:** Evaluate a statement of python code.

The bot will always respond with the return value of the code.
If the return value of the code is a coroutine, it will be awaited,
and the result of that will be the bot's response.

Note: Only one statement may be evaluated. Using certain restricted
keywords, e.g. yield, will result in a syntax error. For multiple
lines or asynchronous code, see [p]repl or [p]eval.

The code can be within a codeblock, inline code or neither, as long as they are not mixed and they are formatted correctly.
You can upload a file with the code to be executed, or reply to a message containing the command, from any bot.

Environment Variables:
    `ctx`      - the command invocation context
    `bot`      - the bot object
    `channel`  - the current channel object
    `author`   - the command author's member object
    `guild`    - the current guild object
    `message`  - the command's message object
    `_`        - the result of the last dev command
    `aiohttp`  - the aiohttp library
    `asyncio`  - the asyncio library
    `discord`  - the discord.py library
    `commands` - the redbot.core.commands module
    `cf`       - the redbot.core.utils.chat_formatting module
(See `[p]setdev getenvironment` for more.)

**Usage:** `<@1275521742961508432>debug`

### eval

**Description:** Execute asynchronous code.

This command wraps code into the body of an async function and then
calls and awaits it. The bot will respond with anything printed to
stdout, as well as the return value of the function.

The code can be within a codeblock, inline code or neither, as long as they are not mixed and they are formatted correctly.
You can upload a file with the code to be executed, or reply to a message containing the command, from any bot.

Environment Variables:
    `ctx`      - the command invocation context
    `bot`      - the bot object
    `channel`  - the current channel object
    `author`   - the command author's member object
    `guild`    - the current guild object
    `message`  - the command's message object
    `_`        - the result of the last dev command
    `aiohttp`  - the aiohttp library
    `asyncio`  - the asyncio library
    `discord`  - the discord.py library
    `commands` - the redbot.core.commands module
    `cf`       - the redbot.core.utils.chat_formatting module
(See `[p]setdev getenvironment` for more.)

**Usage:** `<@1275521742961508432>eval`

### repl

**Description:** Open an interactive REPL.

The REPL will only recognise code as messages which start with a
backtick. This includes codeblocks, and as such multiple lines can be
evaluated.

Use `exit()` or `quit` to exit the REPL session, prefixed with
a backtick so they may be interpreted.

You can upload a file with the code to be executed, or reply to a message containing the same command, for any bot.

Environment Variables:
    `ctx`      - the command invocation context
    `bot`      - the bot object
    `channel`  - the current channel object
    `author`   - the command author's member object
    `guild`    - the current guild object
    `message`  - the command's message object
    `_`        - the result of the last dev command
    `aiohttp`  - the aiohttp library
    `asyncio`  - the asyncio library
    `discord`  - the discord.py library
    `commands` - the redbot.core.commands module
    `cf`       - the redbot.core.utils.chat_formatting module
(See `[p]setdev getenvironment` for more.)

**Usage:** `<@1275521742961508432>repl`

### replpause

**Description:** Pauses/resumes the REPL running in the current channel.

**Usage:** `<@1275521742961508432>replpause`

### bypasscooldowns

**Description:** Give bot owners the ability to bypass cooldowns.

Does not persist through restarts.

**Usage:** `<@1275521742961508432>bypasscooldowns`

### eshell

**Description:** Execute Shell commands.

This command wraps the shell command into a Python code to invoke them.

The code can be within a codeblock, inline code or neither, as long as they are not mixed and they are formatted correctly.
You can upload a file with the code to be executed, or reply to a message containing the command, from any bot.

**Usage:** `<@1275521742961508432>eshell`

### setdev

**Description:** Commands to configure Dev.

**Usage:** `<@1275521742961508432>setdev`

### setdev getenvironment

**Description:** Display all Dev environment values.

**Usage:** `<@1275521742961508432>setdev getenvironment`

### setdev resetlocals

**Description:** Reset its own locals in evals.

**Usage:** `<@1275521742961508432>setdev resetlocals`

### setdev outputmode

**Description:** Set the output mode. `repr` is to display the repr of the result. `repr_or_str` is to display in the same way, but a string as a string. `str` is to display the string of the result.

Default value: `repr`
Dev: `typing.Literal['repr', 'repr_or_str', 'str']`

**Usage:** `<@1275521742961508432>setdev outputmode`

### setdev downloaderalreadyagreed

**Description:** If enabled, Downloader will no longer prompt you to type `I agree` when adding a repo, even after a bot restart.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev downloaderalreadyagreed`

### setdev ansiformatting

**Description:** Use the `ansi` formatting for results.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev ansiformatting`

### setdev showsettings

**Description:** Show all settings for the cog with defaults and values.

**Usage:** `<@1275521742961508432>setdev showsettings`

### setdev autoimports

**Description:** Enable or disable auto imports.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev autoimports`

### setdev richtracebacks

**Description:** Use `rich` to display tracebacks.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev richtracebacks`

### setdev uselastlocals

**Description:** Use the last locals for each evals. Locals are only registered for `[p]eval`, but can be used in other commands.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev uselastlocals`

### setdev modalconfig

**Description:** Set all settings for the cog with a Discord Modal.

**Usage:** `<@1275521742961508432>setdev modalconfig`

### setdev useextendedenvironment

**Description:** Use my own Dev env with useful values.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev useextendedenvironment`

### setdev senddpyobjects

**Description:** If the result is an embed/file/attachment object or an iterable of these, send.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev senddpyobjects`

### setdev resetsetting

**Description:** Reset a setting.

**Usage:** `<@1275521742961508432>setdev resetsetting`

### setdev sendinteractive

**Description:** Send results with `commands.Context.send_interactive`, not a Menu.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdev sendinteractive`

