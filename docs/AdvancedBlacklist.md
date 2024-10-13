An advanced blacklist cog for more control over your blacklist

# ,whitelist
Manage Starfire's whitelist<br/>
 - Usage: `,whitelist`
 - Restricted to: `BOT_OWNER`
 - Aliases: `allowlist`
## ,whitelist reason
Edit the reason for a whitelisted user.<br/>
 - Usage: `,whitelist reason <user> <reason>`
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,whitelist list
List the users on Starfire's whitelist<br/>
 - Usage: `,whitelist list`
## ,whitelist remove
Remove users from the whitelist.<br/>

**Arguments**<br/>
    - `users` The users to remove from the whitelist.<br/>
 - Usage: `,whitelist remove <users>`
 - Aliases: `del, delete, and rm`
Extended Arg Info
> ### *users: discord.user.User
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
## ,whitelist clear
Clear the whitelist<br/>
 - Usage: `,whitelist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,whitelist add
Add a user to the whitelist. These users cannot be bots.<br/>

**Arguments**<br/>
    - `users` The users to add to the whitelist.<br/>
    - `reason` The reason for adding these users to the whitelist. This argument is optional.<br/>
 - Usage: `,whitelist add <users> [reason]`
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,localwhitelist
Manage the local whitelist for your server.<br/>
 - Usage: `,localwhitelist`
 - Restricted to: `ADMIN`
 - Aliases: `localallowlist`
 - Checks: `server_only`
## ,localwhitelist clear
Clear the local whitelist<br/>
 - Usage: `,localwhitelist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,localwhitelist remove
Remove members/roles from the local whitelist<br/>

**Arguments**<br/>
    - `members` The members/roles to remove from the local whitelist.<br/>
 - Usage: `,localwhitelist remove <member_or_roles>`
 - Aliases: `del and delete`
Extended Arg Info
> ### *member_or_roles: Union[discord.member.Member, discord.role.Role]
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
## ,localwhitelist list
List the locally whitelisted members/roles<br/>
 - Usage: `,localwhitelist list`
## ,localwhitelist add
Add members and roles to the local whitelist.<br/>

This will disallow anyone not in the local whitelist or not in a role in the local whitelist from using Starfire.<br/>

Note, if you are an admin you must add yourself to the localwhitelist as to not lock yourself out of Starfire.<br/>

**Arguments**<br/>
    - `members_or_roles` The members/roles to add to the whitelist. Members cannot be bots.<br/>
    - `reason` The reason for adding these members/roles to the whitelist. This argument is optional.<br/>
 - Usage: `,localwhitelist add <members_or_roles> [reason]`
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,localwhitelist reason
Edit the reason for a locally whitelisted member/role<br/>

**Arguments**<br/>
    - `member_or_role` The member/role to edit the reason of. Members cannot be a bot.<br/>
    - `reason` The new reason for locally whitelisting the member/role.<br/>
 - Usage: `,localwhitelist reason <member_or_role> <reason>`
Extended Arg Info
> ### member_or_role: Union[discord.member.Member, discord.role.Role]
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,blacklist
Manage Starfire's blacklist<br/>
 - Usage: `,blacklist`
 - Restricted to: `BOT_OWNER`
 - Aliases: `blocklist`
## ,blacklist list
List the users in the blacklist.<br/>
 - Usage: `,blacklist list`
## ,blacklist log
Manage the log settings for AdvancedBlacklist.<br/>
 - Usage: `,blacklist log`
### ,blacklist log remove
Remove the channel for logging black/whitelistings<br/>
 - Usage: `,blacklist log remove`
### ,blacklist log set
Set the channel for logging black/whitelistings<br/>

**Arguments**<br/>
    - `channel` The channel or thread to use for logging.<br/>
 - Usage: `,blacklist log set <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,blacklist clear
Clear the blacklist<br/>
 - Usage: `,blacklist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,blacklist add
Add users to the blacklist.<br/>

**Arguments**<br/>
    - `users` The users to add to the blacklist. These cannot be bots.<br/>
    - `reason` The reason for adding these users to the blacklist. This is optional.<br/>
 - Usage: `,blacklist add <users> [reason]`
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,blacklist reason
Edit the reason for a user in the blacklist.<br/>

**Arguments**<br/>
    - `user` The user to edit the reason of.<br/>
    - `reason` The new reason for blacklisting this user.<br/>
 - Usage: `,blacklist reason <user> <reason>`
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,blacklist remove
Remove users from the blacklist.<br/>

**Arguments**<br/>
    - `users` The users to remove from the blacklist.<br/>
 - Usage: `,blacklist remove <users>`
 - Aliases: `del, delete, and rm`
Extended Arg Info
> ### *users: discord.user.User
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
# ,localblacklist
Manage the local blacklist for your server.<br/>
 - Usage: `,localblacklist`
 - Restricted to: `ADMIN`
 - Aliases: `localblocklist`
 - Checks: `server_only`
## ,localblacklist add
Add users to the local blacklist<br/>

**Arguments**<br/>
    - `members_or_roles` The members or roles to add to the local blacklist. Members cannot be bots<br/>
    - `reason` The reason for adding these members/roles to the blacklist. This is optional<br/>
 - Usage: `,localblacklist add <members_or_roles> [reason]`
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,localblacklist reason
Edit the reason for a member or role in the local blacklist.<br/>

**Arguments**<br/>
    - `member_or_role` The member/role to edit the reason of. Members cannot be a bot.<br/>
    - `reason` The new reason for blacklisting the member/role.<br/>
 - Usage: `,localblacklist reason <member_or_role> <reason>`
Extended Arg Info
> ### member_or_role: Union[discord.member.Member, discord.role.Role]
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,localblacklist clear
Clear the local blacklist<br/>
 - Usage: `,localblacklist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,localblacklist remove
Remove users from the local blacklist.<br/>

**Arguments**<br/>
    - `users` The users to remove from the local blacklist.<br/>
 - Usage: `,localblacklist remove <users>`
 - Aliases: `del, delete, and rm`
Extended Arg Info
> ### *users: Union[discord.member.Member, discord.role.Role]
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
## ,localblacklist list
List the members and roles in the local blacklist.<br/>
 - Usage: `,localblacklist list`
# ,advancedblacklistversion
Get the version of Advanced Blacklist that Starfire is running<br/>
 - Usage: `,advancedblacklistversion`
 - Aliases: `abversion`
