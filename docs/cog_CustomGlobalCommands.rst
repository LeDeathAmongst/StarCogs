CustomGlobalCommands
====================

Global custom commands.

# ,setgcom
Adds a global custom command<br/>
 - Usage: `,setgcom <command> <text>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,rmgcom
Removes a global custom command<br/>
 - Usage: `,rmgcom <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,lsgcom
Shows global custom commands list<br/>
 - Usage: `,lsgcom`


# ,agcom
Create aliases for Global Custom Commands<br/>
 - Usage: `,agcom [command=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,agcom rm
Remove an alias from a global cc<br/>
 - Usage: `,agcom rm <aliases>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### *aliases
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,agcom show
Shows aliases for a command, or the command bound to an alias<br/>
 - Usage: `,agcom show <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,agcom add
Add one or more aliases for a custom command<br/>
 - Usage: `,agcom add <command> <aliases>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *aliases
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


