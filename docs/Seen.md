A cog to check when a member/role/channel/category/user/guild was last active!

# <@1275521742961508432>seen (Hybrid Command)
Check when a member/role/channel/category was last active!<br/>
 - Usage: `<@1275521742961508432>seen <_type> <show_details> <_object>`
 - Slash Usage: `/seen <_type> <show_details> <_object>`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### _object: Union[discord.member.Member, discord.role.Role, discord.channel.TextChannel, discord.channel.CategoryChannel]
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
## <@1275521742961508432>seen member (Hybrid Command)
Check when a member was last active!<br/>
 - Usage: `<@1275521742961508432>seen member <_type> <show_details> [member]`
 - Slash Usage: `/seen member <_type> <show_details> [member]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### member: Optional[discord.member.Member] = None
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
## <@1275521742961508432>seen hackmember (Hybrid Command)
Check when a old member was last active!<br/>
 - Usage: `<@1275521742961508432>seen hackmember <_type> <show_details> <user>`
 - Slash Usage: `/seen hackmember <_type> <show_details> <user>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
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
## <@1275521742961508432>seen configstats (Hybrid Command)
Get Config data stats.<br/>
 - Usage: `<@1275521742961508432>seen configstats`
 - Slash Usage: `/seen configstats`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>seen role (Hybrid Command)
Check when a role was last active!<br/>
 - Usage: `<@1275521742961508432>seen role <_type> <show_details> [role]`
 - Slash Usage: `/seen role <_type> <show_details> [role]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## <@1275521742961508432>seen hackuser (Hybrid Command)
Check when a old user was last active!<br/>
 - Usage: `<@1275521742961508432>seen hackuser <_type> <show_details> <user_id>`
 - Slash Usage: `/seen hackuser <_type> <show_details> <user_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### user_id: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>seen listener (Hybrid Command)
Enable or disable a listener.<br/>
 - Usage: `<@1275521742961508432>seen listener <state> <_types>`
 - Slash Usage: `/seen listener <state> <_types>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>seen ignoreme (Hybrid Command)
Asking Seen to ignore your actions.<br/>
 - Usage: `<@1275521742961508432>seen ignoreme`
 - Slash Usage: `/seen ignoreme`
## <@1275521742961508432>seen ignoreuser (Hybrid Command)
Ignore or unignore a specific user.<br/>
 - Usage: `<@1275521742961508432>seen ignoreuser <user>`
 - Slash Usage: `/seen ignoreuser <user>`
 - Restricted to: `BOT_OWNER`
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
## <@1275521742961508432>seen getdebugloopsstatus (Hybrid Command)
Get an embed for check loop status.<br/>
 - Usage: `<@1275521742961508432>seen getdebugloopsstatus`
 - Slash Usage: `/seen getdebugloopsstatus`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>seen purge (Hybrid Command)
Purge Config for a specified _type or all.<br/>
 - Usage: `<@1275521742961508432>seen purge <_type>`
 - Slash Usage: `/seen purge <_type>`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>seen migratefromseen (Hybrid Command)
Migrate Seen from Seen by Aikaterna.<br/>
 - Usage: `<@1275521742961508432>seen migratefromseen`
 - Slash Usage: `/seen migratefromseen`
 - Restricted to: `BOT_OWNER`
 - Aliases: `migratefromaika`
## <@1275521742961508432>seen channel (Hybrid Command)
Check when a channel was last active!<br/>
 - Usage: `<@1275521742961508432>seen channel <_type> <show_details> [channel=None]`
 - Slash Usage: `/seen channel <_type> <show_details> [channel=None]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## <@1275521742961508432>seen category (Hybrid Command)
Check when a category was last active!<br/>
 - Usage: `<@1275521742961508432>seen category <_type> <show_details> [category=None]`
 - Slash Usage: `/seen category <_type> <show_details> [category=None]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### category: Optional[discord.channel.CategoryChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## <@1275521742961508432>seen user (Hybrid Command)
Check when a user was last active!<br/>
 - Usage: `<@1275521742961508432>seen user <_type> <show_details> [user]`
 - Slash Usage: `/seen user <_type> <show_details> [user]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### user: Optional[discord.user.User] = None
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
## <@1275521742961508432>seen board (Hybrid Command)
View a Seen Board for members/roles/channels/categories/servers/users!<br/>

`bots` is a parameter for `members` and `users`. `include_role` and `exclude_role` are parameters for only `members`.<br/>
 - Usage: `<@1275521742961508432>seen board <_type> [_object=members] [reverse=False] [bots=None] [include_role=None] [exclude_role=None]`
 - Slash Usage: `/seen board <_type> [_object=members] [reverse=False] [bots=None] [include_role=None] [exclude_role=None]`
 - Checks: `server_only`
Extended Arg Info
> ### reverse: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### bots: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### include_role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### exclude_role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## <@1275521742961508432>seen server (Hybrid Command)
Check when a server was last active!<br/>
 - Usage: `<@1275521742961508432>seen server <_type> <show_details> [server]`
 - Slash Usage: `/seen server <_type> <show_details> [server]`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
