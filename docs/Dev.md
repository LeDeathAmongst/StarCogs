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
# ,mimicmsg
Dispatch a message event as if it were sent by a different user.<br/>

Current message is used as a base (including attachments, embeds, etc.),<br/>
the content and author of the message are replaced with the given arguments.<br/>

Note: If `content` isn't passed, the message needs to contain embeds, attachments,<br/>
or anything else that makes the message non-empty.<br/>
 - Usage: `,mimicmsg <user> [content]`
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
# ,bypasscooldowns
Give bot owners the ability to bypass cooldowns.<br/>

Does not persist through restarts.<br/>
 - Usage: `,bypasscooldowns [toggle=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
