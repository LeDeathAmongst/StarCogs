Talk as the bot

# /talk (Slash Command)
Send a message as the bot<br/>
 - Usage: `/talk <message> [hide] [mentions]`
 - `message:` (Required) The message to send
 - `hide:` (Optional) Show the command usage (default False)
 - `mentions:` (Optional) Allow the usage of User/Role mentions (default False)

 - Checks: `Server Only`
Extended Arg Info
> ### message: str
> - Autocomplete: False
> 
> The message to send
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### hide: bool
> - Autocomplete: False
> - Default: False
> 
> Show the command usage (default False)
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### mentions: bool
> - Autocomplete: False
> - Default: False
> 
> Allow the usage of User/Role mentions (default False)
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,talk
Send a message as the bot<br/>
 - Usage: `,talk <message>`
 - Restricted to: `MOD`
Extended Arg Info
> ### message
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,talkm
Send a message as the bot, with mentions enabled<br/>
 - Usage: `,talkm <message>`
 - Restricted to: `MOD`
Extended Arg Info
> ### message
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,talkd
Send a message as the bot, but delete the command message<br/>
 - Usage: `,talkd <message>`
 - Restricted to: `MOD`
Extended Arg Info
> ### message
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,talkmd
Send a message as the bot, with mentions enabled and delete the command message<br/>
 - Usage: `,talkmd <message>`
 - Restricted to: `MOD`
Extended Arg Info
> ### message
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,talkset
Configure settings<br/>
 - Usage: `,talkset`
 - Restricted to: `ADMIN`
## ,talkset everyone
Set the ability to mass mention using `everyone` or `here`<br/>
 - Usage: `,talkset everyone [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
