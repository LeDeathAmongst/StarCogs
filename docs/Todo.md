A simple todo list

# ,todo
Contains a list of commands to set and retrieve todo tasks <br/>
Use todo <id> to get a specific todo<br/>
 - Usage: `,todo <id_>`
Extended Arg Info
> ### id_: int
> ```
> A number without decimal places.
> ```
## ,todo list
List all your todos<br/>
 - Usage: `,todo list`
## ,todo removeall
Remove all your todo tasks<br/>
 - Usage: `,todo removeall <indices>`
 - Aliases: `clear`
Extended Arg Info
> ### *indices: int
> ```
> A number without decimal places.
> ```
## ,todo add
Add a new task to your todo list, DO NOT STORE SENSITIVE INFO HERE<br/>
 - Usage: `,todo add <task>`
Extended Arg Info
> ### task: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,todo menuset
Enable/Disable menus for todos<br/>
 - Usage: `,todo menuset <toggle>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,todo reorder
Reorder your todos using IDs to swap them<br/>
 - Usage: `,todo reorder <from_> <to>`
 - Aliases: `rearrange`
Extended Arg Info
> ### from_: int
> ```
> A number without decimal places.
> ```
> ### to: int
> ```
> A number without decimal places.
> ```
## ,todo random
Displays a random todo from your todo list<br/>
 - Usage: `,todo random`
 - Aliases: `r and rand`
## ,todo edit
Edit a todo quickly<br/>
 - Usage: `,todo edit <index> <task>`
Extended Arg Info
> ### index: int
> ```
> A number without decimal places.
> ```
> ### task: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,todo remove
Remove your todo tasks, supports multiple id removals as well<br/>
eg:,todo remove 1 2 3<br/>
 - Usage: `,todo remove <indices>`
 - Aliases: `delete`
Extended Arg Info
> ### *indices: int
> ```
> A number without decimal places.
> ```
## ,todo search
Quick search in your todos to find stuff fast<br/>
 - Usage: `,todo search <text>`
Extended Arg Info
> ### text
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
