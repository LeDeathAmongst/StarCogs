A cog to allow a user to execute a command by clicking on a button!

# ,commandsbuttons (Hybrid Command)
Group of commands to use CommandsButtons.<br/>
 - Usage: `,commandsbuttons`
 - Slash Usage: `/commandsbuttons`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
## ,commandsbuttons bulk (Hybrid Command)
Add commands-buttons for a message.<br/>

```,commandsbuttons bulk <message> ":reaction1:|ping" ":reaction2:|ping" :reaction3:|ping"```
 - Usage: `,commandsbuttons bulk <message> <commands_buttons>`
 - Slash Usage: `/commandsbuttons bulk <message> <commands_buttons>`
 - Checks: `server_only`
## ,commandsbuttons list (Hybrid Command)
List all commands-buttons of this server or display the settings for a specific one.<br/>
 - Usage: `,commandsbuttons list [message=None]`
 - Slash Usage: `/commandsbuttons list [message=None]`
 - Checks: `server_only`
## ,commandsbuttons purge (Hybrid Command)
Clear all commands-buttons for a server.<br/>
 - Usage: `,commandsbuttons purge`
 - Slash Usage: `/commandsbuttons purge`
 - Checks: `server_only`
## ,commandsbuttons clear (Hybrid Command)
Clear all commands-buttons for a message.<br/>
 - Usage: `,commandsbuttons clear <message>`
 - Slash Usage: `/commandsbuttons clear <message>`
 - Checks: `server_only`
## ,commandsbuttons remove (Hybrid Command)
Remove a command-button for a message.<br/>

Use `,commandsbuttons list <message>` to find the config identifier.<br/>
 - Usage: `,commandsbuttons remove <message> <config_identifier>`
 - Slash Usage: `/commandsbuttons remove <message> <config_identifier>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### config_identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,commandsbuttons add (Hybrid Command)
Add a command-button for a message.<br/>

(Use the number for the color.)<br/>
• `primary`: 1<br/>
• `secondary`: 2<br/>
• `success`: 3<br/>
• `danger`: 4<br/>
# Aliases<br/>
• `blurple`: 1<br/>
• `grey`: 2<br/>
• `gray`: 2<br/>
• `green`: 3<br/>
• `red`: 4<br/>
 - Usage: `,commandsbuttons add <message> <command> <emoji> [style_button=2] [text_button]`
 - Slash Usage: `/commandsbuttons add <message> <command> <emoji> [style_button=2] [text_button]`
 - Aliases: `+`
 - Checks: `server_only`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
