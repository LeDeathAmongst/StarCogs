BanAppeal
=========

# /appeal (Slash Command)
Appeal a ban<br/>
 - Usage: `/appeal`


<<<<<<< HEAD
# <@1275521742961508432>appealset
Set up ban appeal settings<br/>
 - Usage: `<@1275521742961508432>appealset`
=======
# ,appealset
Set up ban appeal settings<br/>
 - Usage: `,appealset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `aset`


<<<<<<< HEAD
## <@1275521742961508432>appealset questions
Set ban appeal questions<br/>
 - Usage: `<@1275521742961508432>appealset questions`
 - Aliases: `qs, question, and q`


### <@1275521742961508432>appealset questions add
Add a question<br/>
 - Usage: `<@1275521742961508432>appealset questions add <question>`
Extended Arg Info
> ### question: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>appealset questions remove
Remove a question<br/>
 - Usage: `<@1275521742961508432>appealset questions remove <index>`


### <@1275521742961508432>appealset questions list
List questions<br/>
 - Usage: `<@1275521742961508432>appealset questions list`


## <@1275521742961508432>appealset resetappeal
Reset the appeal status of all users<br/>
 - Usage: `<@1275521742961508432>appealset resetappeal [user=None]`
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>appealset managers
Set ban appeal managers<br/>
 - Usage: `<@1275521742961508432>appealset managers`
 - Aliases: `manager and m`


### <@1275521742961508432>appealset managers remove
Remove a manager<br/>
 - Usage: `<@1275521742961508432>appealset managers remove <manager>`
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


### <@1275521742961508432>appealset managers add
Add a manager<br/>
 - Usage: `<@1275521742961508432>appealset managers add <manager>`
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


### <@1275521742961508432>appealset managers list
List managers<br/>
 - Usage: `<@1275521742961508432>appealset managers list`


## <@1275521742961508432>appealset toggle
Toggle ban appeal settings<br/>
 - Usage: `<@1275521742961508432>appealset toggle`


## <@1275521742961508432>appealset response
Set the message sent to a user when a ban appeal is accepted or rejected<br/>

User `{server_name}` to be replaced with the server name<br/>
 - Usage: `<@1275521742961508432>appealset response <response_type> <response>`
=======
## ,appealset response
Set the message sent to a user when a ban appeal is accepted or rejected<br/>

User `{server_name}` to be replaced with the server name<br/>
 - Usage: `,appealset response <response_type> <response>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `responses and r`
Extended Arg Info
> ### response: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>appealset channel
Set ban appeal channel<br/>

This is the channel where all appeals will be sent.<br/>
 - Usage: `<@1275521742961508432>appealset channel <channel>`
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


## <@1275521742961508432>appealset banmessage
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
Set the message sent to a user when they are banned<br/>

Use `{server_name}` to be replaced with the server name<br/>
and `{user_install_link}` to be replaced with the bot install link<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>appealset banmessage [message]`
=======
 - Usage: `,appealset banmessage [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `bm`
Extended Arg Info
> ### message: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>appealset showsettings
Show ban appeal settings<br/>
 - Usage: `<@1275521742961508432>appealset showsettings`
 - Aliases: `ss`


=======
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


>>>>>>> 9e308722 (Revamped and Fixed)
