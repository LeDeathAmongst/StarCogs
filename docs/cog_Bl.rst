Bl
==

A cog to manage a blacklist of users with links in hypertext.

<<<<<<< HEAD
# <@1275521742961508432>bl
Commands to manage the blacklist.<br/>
 - Usage: `<@1275521742961508432>bl`
 - Checks: `server_only`


## <@1275521742961508432>bl remove
Remove a user from the blacklist.<br/>
 - Usage: `<@1275521742961508432>bl remove <user>`
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


## <@1275521742961508432>bl check
Check if a user is in the blacklist.<br/>
 - Usage: `<@1275521742961508432>bl check <user>`
=======
# ,bl
Commands to manage the blacklist.<br/>
 - Usage: `,bl`
 - Checks: `server_only`


## ,bl check
Check if a user is in the blacklist.<br/>
 - Usage: `,bl check <user>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>bl addtrustedrole
Add a role to the trusted roles list.<br/>
 - Usage: `<@1275521742961508432>bl addtrustedrole <role>`
=======
## ,bl addtrustedrole
Add a role to the trusted roles list.<br/>
 - Usage: `,bl addtrustedrole <role>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>bl list
List all blacklisted users.<br/>
 - Usage: `<@1275521742961508432>bl list`


## <@1275521742961508432>bl removetrustedrole
Remove a role from the trusted roles list.<br/>
 - Usage: `<@1275521742961508432>bl removetrustedrole <role>`
=======
## ,bl remove
Remove a user from the blacklist.<br/>
 - Usage: `,bl remove <user>`
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


## ,bl removetrustedrole
Remove a role from the trusted roles list.<br/>
 - Usage: `,bl removetrustedrole <role>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>bl add
Add a user to the blacklist with a link.<br/>
 - Usage: `<@1275521742961508432>bl add <user> <link>`
=======
## ,bl list
List all blacklisted users.<br/>
 - Usage: `,bl list`


## ,bl add
Add a user to the blacklist with a link.<br/>
 - Usage: `,bl add <user> <link>`
>>>>>>> 9e308722 (Revamped and Fixed)
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
> ### link: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


