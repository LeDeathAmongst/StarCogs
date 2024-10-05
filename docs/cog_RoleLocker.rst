RoleLocker
==========

# <@1275521742961508432>rolelock
Base command for locking commands or cogs.<br/>
 - Usage: `<@1275521742961508432>rolelock`
 - Restricted to: `ADMIN`


## <@1275521742961508432>rolelock command
Lock a specific command behind roles.<br/>
 - Usage: `<@1275521742961508432>rolelock command <command_name> <roles>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>rolelock cog
Lock an entire cog behind roles.<br/>
 - Usage: `<@1275521742961508432>rolelock cog <cog_name> <roles>`
Extended Arg Info
> ### cog_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>rolelock removecommand
Remove a command from being locked.<br/>
 - Usage: `<@1275521742961508432>rolelock removecommand <command_name>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>rolelock cleartier
Clear all roles from the specified tier.<br/>
 - Usage: `<@1275521742961508432>rolelock cleartier <tier_name>`
Extended Arg Info
> ### tier_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>rolelock tierlist
List all tiers and the roles in them.<br/>
 - Usage: `<@1275521742961508432>rolelock tierlist`


## <@1275521742961508432>rolelock removecog
Remove a cog from being locked.<br/>
 - Usage: `<@1275521742961508432>rolelock removecog <cog_name>`
Extended Arg Info
> ### cog_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>rolelock tierinfo
Display detailed information about a specific tier.<br/>
 - Usage: `<@1275521742961508432>rolelock tierinfo <tier_name>`
Extended Arg Info
> ### tier_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>setrolelocker
Configure RoleLocker settings globally.<br/>
 - Usage: `<@1275521742961508432>setrolelocker`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>setrolelocker addtier
Add roles to a specific tier.<br/>
 - Usage: `<@1275521742961508432>setrolelocker addtier <tier_name> <roles>`
Extended Arg Info
> ### tier_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>setrolelocker setrolelimit
Set a maximum member count limit for a role.<br/>
 - Usage: `<@1275521742961508432>setrolelocker setrolelimit <role> <max_members>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### max_members: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>setrolelocker removetier
Remove roles from a specific tier.<br/>
 - Usage: `<@1275521742961508432>setrolelocker removetier <tier_name> <roles>`
Extended Arg Info
> ### tier_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


