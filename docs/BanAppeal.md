# /appeal (Slash Command)
Appeal a ban<br/>
 - Usage: `/appeal`
# ,appealset
Set up ban appeal settings<br/>
 - Usage: `,appealset`
 - Restricted to: `ADMIN`
 - Aliases: `aset`
## ,appealset channel
Set ban appeal channel<br/>

This is the channel where all appeals will be sent.<br/>
 - Usage: `,appealset channel <channel>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,appealset resetappeal
Reset the appeal status of all users<br/>
 - Usage: `,appealset resetappeal [user=None]`
 - Aliases: `resetappeals`
Extended Arg Info
> ### user: Union[discord.user.User, int, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## ,appealset response
Set the message sent to a user when a ban appeal is accepted or rejected<br/>

User `{server_name}` to be replaced with the server name<br/>
 - Usage: `,appealset response <response_type> <response>`
 - Aliases: `responses and r`
Extended Arg Info
> ### response: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,appealset toggle
Toggle ban appeal settings<br/>
 - Usage: `,appealset toggle`
## ,appealset questions
Set ban appeal questions<br/>
 - Usage: `,appealset questions`
 - Aliases: `qs, question, and q`
### ,appealset questions add
Add a question<br/>
 - Usage: `,appealset questions add <question>`
Extended Arg Info
> ### question: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,appealset questions list
List questions<br/>
 - Usage: `,appealset questions list`
### ,appealset questions remove
Remove a question<br/>
 - Usage: `,appealset questions remove <index>`
## ,appealset banmessage
Set the message sent to a user when they are banned<br/>

Use `{server_name}` to be replaced with the server name<br/>
and `{user_install_link}` to be replaced with the bot install link<br/>
 - Usage: `,appealset banmessage [message]`
 - Aliases: `bm`
Extended Arg Info
> ### message: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,appealset showsettings
Show ban appeal settings<br/>
 - Usage: `,appealset showsettings`
 - Aliases: `ss`
## ,appealset managers
Set ban appeal managers<br/>
 - Usage: `,appealset managers`
 - Aliases: `manager and m`
### ,appealset managers remove
Remove a manager<br/>
 - Usage: `,appealset managers remove <manager>`
Extended Arg Info
> ### manager: Union[discord.member.Member, discord.role.Role]
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
### ,appealset managers list
List managers<br/>
 - Usage: `,appealset managers list`
### ,appealset managers add
Add a manager<br/>
 - Usage: `,appealset managers add <manager>`
Extended Arg Info
> ### manager: Union[discord.member.Member, discord.role.Role]
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
