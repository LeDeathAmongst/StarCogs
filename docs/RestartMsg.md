# ,warnrestart
Send a message to all Server Owners, except those in the ignore list, and restart the bot.<br/>
 - Usage: `,warnrestart <message>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,testmsg
Send a test message to a specific Server Owner without restarting the bot.<br/>
 - Usage: `,testmsg <server_id> <message>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,ignoreowner
Add a server's owner to the ignore list.<br/>
 - Usage: `,ignoreowner <server_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```
# ,unignoreowner
Remove a server's owner from the ignore list.<br/>
 - Usage: `,unignoreowner <server_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```
