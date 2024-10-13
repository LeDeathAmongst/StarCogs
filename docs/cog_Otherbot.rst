Otherbot
========

<<<<<<< HEAD
# <@1275521742961508432>otherbot
Otherbot configuration options.<br/>
 - Usage: `<@1275521742961508432>otherbot`
=======
# ,otherbot
Otherbot configuration options.<br/>
 - Usage: `,otherbot`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>otherbot pingrole
Sets the role to use for pinging. Leave blank to reset it.<br/>
 - Usage: `<@1275521742961508432>otherbot pingrole [role_name=None]`
=======
## ,otherbot pingrole
Sets the role to use for pinging. Leave blank to reset it.<br/>
 - Usage: `,otherbot pingrole [role_name=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### role_name: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>otherbot watch
Watch settings.<br/>
 - Usage: `<@1275521742961508432>otherbot watch`
 - Aliases: `watching`


### <@1275521742961508432>otherbot watch online
Manage online notifications.<br/>
 - Usage: `<@1275521742961508432>otherbot watch online`


#### <@1275521742961508432>otherbot watch online remove
Removes a bot currently tracked.<br/>
 - Usage: `<@1275521742961508432>otherbot watch online remove <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


#### <@1275521742961508432>otherbot watch online emoji
Choose which emoji that will be used for online messages.<br/>
 - Usage: `<@1275521742961508432>otherbot watch online emoji [emoji]`
Extended Arg Info
> ### emoji: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>otherbot watch online embed
Set wether you want to receive notifications in embed or not.<br/>
 - Usage: `<@1275521742961508432>otherbot watch online embed`


#### <@1275521742961508432>otherbot watch online add
Add a bot that will be tracked when it comes back online.<br/>
 - Usage: `<@1275521742961508432>otherbot watch online add <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


#### <@1275521742961508432>otherbot watch online list
Lists currently tracked bots.<br/>
 - Usage: `<@1275521742961508432>otherbot watch online list`


### <@1275521742961508432>otherbot watch offline
Manage offline notifications.<br/>
 - Usage: `<@1275521742961508432>otherbot watch offline`


#### <@1275521742961508432>otherbot watch offline list
Lists currently tracked bots.<br/>
 - Usage: `<@1275521742961508432>otherbot watch offline list`


#### <@1275521742961508432>otherbot watch offline add
Add a bot that will be tracked when it goes offline.<br/>
 - Usage: `<@1275521742961508432>otherbot watch offline add <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


#### <@1275521742961508432>otherbot watch offline embed
Set wether you want to receive notifications in embed or not.<br/>
 - Usage: `<@1275521742961508432>otherbot watch offline embed`


#### <@1275521742961508432>otherbot watch offline remove
Removes a bot currently tracked.<br/>
 - Usage: `<@1275521742961508432>otherbot watch offline remove <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


#### <@1275521742961508432>otherbot watch offline emoji
Choose which emoji that will be used for offline messages.<br/>
 - Usage: `<@1275521742961508432>otherbot watch offline emoji [emoji]`
Extended Arg Info
> ### emoji: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>otherbot channel
Sets the channel to report in.<br/>

Default to the current one.<br/>
 - Usage: `<@1275521742961508432>otherbot channel [channel=None]`
=======
## ,otherbot channel
Sets the channel to report in.<br/>

Default to the current one.<br/>
 - Usage: `,otherbot channel [channel=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


<<<<<<< HEAD
=======
## ,otherbot watch
Watch settings.<br/>
 - Usage: `,otherbot watch`
 - Aliases: `watching`


### ,otherbot watch offline
Manage offline notifications.<br/>
 - Usage: `,otherbot watch offline`


#### ,otherbot watch offline remove
Removes a bot currently tracked.<br/>
 - Usage: `,otherbot watch offline remove <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


#### ,otherbot watch offline list
Lists currently tracked bots.<br/>
 - Usage: `,otherbot watch offline list`


#### ,otherbot watch offline embed
Set wether you want to receive notifications in embed or not.<br/>
 - Usage: `,otherbot watch offline embed`


#### ,otherbot watch offline emoji
Choose which emoji that will be used for offline messages.<br/>
 - Usage: `,otherbot watch offline emoji [emoji]`
Extended Arg Info
> ### emoji: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,otherbot watch offline add
Add a bot that will be tracked when it goes offline.<br/>
 - Usage: `,otherbot watch offline add <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


### ,otherbot watch online
Manage online notifications.<br/>
 - Usage: `,otherbot watch online`


#### ,otherbot watch online remove
Removes a bot currently tracked.<br/>
 - Usage: `,otherbot watch online remove <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


#### ,otherbot watch online embed
Set wether you want to receive notifications in embed or not.<br/>
 - Usage: `,otherbot watch online embed`


#### ,otherbot watch online add
Add a bot that will be tracked when it comes back online.<br/>
 - Usage: `,otherbot watch online add <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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


#### ,otherbot watch online emoji
Choose which emoji that will be used for online messages.<br/>
 - Usage: `,otherbot watch online emoji [emoji]`
Extended Arg Info
> ### emoji: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,otherbot watch online list
Lists currently tracked bots.<br/>
 - Usage: `,otherbot watch online list`


>>>>>>> 9e308722 (Revamped and Fixed)
