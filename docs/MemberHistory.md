# ,memberhistory

 - Usage: `,memberhistory`
 - Aliases: `memhis`
 - Checks: `server_only`
## ,memberhistory ttl
Set the time to live for the stored files.<br/>
 - Usage: `,memberhistory ttl <time>`
 - Restricted to: `BOT_OWNER`
## ,memberhistory ignore
Add a user or role to the ignore list.<br/>
 - Usage: `,memberhistory ignore`
 - Restricted to: `ADMIN`
### ,memberhistory ignore globally
Add a user to the global ignore list.<br/>
 - Usage: `,memberhistory ignore globally <user>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `global`
Extended Arg Info
> ### user: discord.user.User
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
### ,memberhistory ignore server
Add a user or role to the ignore list.<br/>
 - Usage: `,memberhistory ignore server <user_or_role>`
 - Restricted to: `ADMIN`
 - Aliases: `server`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
## ,memberhistory unignore
Remove a user or role from the ignore list.<br/>
 - Usage: `,memberhistory unignore`
 - Restricted to: `ADMIN`
### ,memberhistory unignore server
Remove a user or role from the ignore list.<br/>
 - Usage: `,memberhistory unignore server <user_or_role>`
 - Restricted to: `ADMIN`
 - Aliases: `server`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
### ,memberhistory unignore globally
Remove a user from the global ignore list.<br/>
 - Usage: `,memberhistory unignore globally <user>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `global`
Extended Arg Info
> ### user: discord.user.User
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
## ,memberhistory storedusers
Get a list of all users with stored files.<br/>
 - Usage: `,memberhistory storedusers`
 - Restricted to: `BOT_OWNER`
## ,memberhistory purgeuser
Purge all stored files for a user.<br/>
 - Usage: `,memberhistory purgeuser <user>`
 - Restricted to: `BOT_OWNER`
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
## ,memberhistory showsettings
See the configured settings and additional data about MemberHistory.<br/>
 - Usage: `,memberhistory showsettings`
 - Restricted to: `ADMIN`
 - Aliases: `ss`
## ,memberhistory purge
Purge all stored files.<br/>
 - Usage: `,memberhistory purge`
 - Restricted to: `BOT_OWNER`
## ,memberhistory avatar
Scroll through the avatar history of a user.<br/>
 - Usage: `,memberhistory avatar`
### ,memberhistory avatar decoration

 - Usage: `,memberhistory avatar decoration [user=operator.attrgetter('author')] [page=1]`
 - Aliases: `deco, decor, and decorations`
Extended Arg Info
> ### user: discord.member.Member = operator.attrgetter('author')
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
### ,memberhistory avatar server

 - Usage: `,memberhistory avatar server [user=operator.attrgetter('author')] [page=1]`
Extended Arg Info
> ### user: discord.member.Member = operator.attrgetter('author')
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
### ,memberhistory avatar global

 - Usage: `,memberhistory avatar global [user=operator.attrgetter('author')] [page=1]`
Extended Arg Info
> ### user: discord.member.Member = operator.attrgetter('author')
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
## ,memberhistory toggle
Toggle the current state of member history.<br/>
 - Usage: `,memberhistory toggle`
 - Restricted to: `GUILD_OWNER`
