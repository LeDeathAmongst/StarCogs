A cog to allow a user to execute a command by clicking on a reaction!

# ,reacttocommand (Hybrid Command)
Group of commands to use ReactToCommand.<br/>
 - Usage: `,reacttocommand`
 - Slash Usage: `/reacttocommand`
 - Restricted to: `BOT_OWNER`
 - Aliases: `rtc`
 - Checks: `server_only`
## ,reacttocommand add (Hybrid Command)
Add a reaction-command for a message.<br/>

There should be no prefix in the command.<br/>
The command will be invoked with the permissions of the user who clicked on the reaction.<br/>
This user must be able to see writing in the channel.<br/>
 - Usage: `,reacttocommand add <message> <emoji> <command>`
 - Slash Usage: `/reacttocommand add <message> <emoji> <command>`
 - Aliases: `+`
 - Checks: `server_only`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,reacttocommand purge (Hybrid Command)
Clear all reactions-commands for a server.<br/>
 - Usage: `,reacttocommand purge`
 - Slash Usage: `/reacttocommand purge`
 - Checks: `server_only`
## ,reacttocommand clear (Hybrid Command)
Clear all reactions-commands for a message.<br/>
 - Usage: `,reacttocommand clear <message>`
 - Slash Usage: `/reacttocommand clear <message>`
 - Checks: `server_only`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
## ,reacttocommand remove (Hybrid Command)
Remove a reaction-command for a message.<br/>
 - Usage: `,reacttocommand remove <message> <emoji>`
 - Slash Usage: `/reacttocommand remove <message> <emoji>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
