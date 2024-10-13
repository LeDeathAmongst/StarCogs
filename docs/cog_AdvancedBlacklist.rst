AdvancedBlacklist
=================

An advanced blacklist cog for more control over your blacklist

<<<<<<< HEAD
# <@1275521742961508432>whitelist
Manage Starfire's whitelist<br/>
 - Usage: `<@1275521742961508432>whitelist`
=======
# ,whitelist
Manage Starfire's whitelist<br/>
 - Usage: `,whitelist`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `allowlist`


<<<<<<< HEAD
## <@1275521742961508432>whitelist add
Add a user to the whitelist. These users cannot be bots.<br/>

**Arguments**<br/>
    - `users` The users to add to the whitelist.<br/>
    - `reason` The reason for adding these users to the whitelist. This argument is optional.<br/>
 - Usage: `<@1275521742961508432>whitelist add <users> [reason]`
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>whitelist reason
Edit the reason for a whitelisted user.<br/>
 - Usage: `<@1275521742961508432>whitelist reason <user> <reason>`
=======
## ,whitelist reason
Edit the reason for a whitelisted user.<br/>
 - Usage: `,whitelist reason <user> <reason>`
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>whitelist list
List the users on Starfire's whitelist<br/>
 - Usage: `<@1275521742961508432>whitelist list`


## <@1275521742961508432>whitelist remove
=======
## ,whitelist list
List the users on Starfire's whitelist<br/>
 - Usage: `,whitelist list`


## ,whitelist remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove users from the whitelist.<br/>

**Arguments**<br/>
    - `users` The users to remove from the whitelist.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>whitelist remove <users>`
=======
 - Usage: `,whitelist remove <users>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>whitelist clear
Clear the whitelist<br/>
 - Usage: `<@1275521742961508432>whitelist clear [confirm=False]`
=======
## ,whitelist clear
Clear the whitelist<br/>
 - Usage: `,whitelist clear [confirm=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
# <@1275521742961508432>localwhitelist
Manage the local whitelist for your server.<br/>
 - Usage: `<@1275521742961508432>localwhitelist`
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `localallowlist`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>localwhitelist remove
=======
## ,localwhitelist clear
Clear the local whitelist<br/>
 - Usage: `,localwhitelist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,localwhitelist remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove members/roles from the local whitelist<br/>

**Arguments**<br/>
    - `members` The members/roles to remove from the local whitelist.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>localwhitelist remove <member_or_roles>`
=======
 - Usage: `,localwhitelist remove <member_or_roles>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>localwhitelist list
List the locally whitelisted members/roles<br/>
 - Usage: `<@1275521742961508432>localwhitelist list`


## <@1275521742961508432>localwhitelist add
=======
## ,localwhitelist list
List the locally whitelisted members/roles<br/>
 - Usage: `,localwhitelist list`


## ,localwhitelist add
>>>>>>> 9e308722 (Revamped and Fixed)
Add members and roles to the local whitelist.<br/>

This will disallow anyone not in the local whitelist or not in a role in the local whitelist from using Starfire.<br/>

Note, if you are an admin you must add yourself to the localwhitelist as to not lock yourself out of Starfire.<br/>

**Arguments**<br/>
    - `members_or_roles` The members/roles to add to the whitelist. Members cannot be bots.<br/>
    - `reason` The reason for adding these members/roles to the whitelist. This argument is optional.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>localwhitelist add <members_or_roles> [reason]`
=======
 - Usage: `,localwhitelist add <members_or_roles> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>localwhitelist reason
=======
## ,localwhitelist reason
>>>>>>> 9e308722 (Revamped and Fixed)
Edit the reason for a locally whitelisted member/role<br/>

**Arguments**<br/>
    - `member_or_role` The member/role to edit the reason of. Members cannot be a bot.<br/>
    - `reason` The new reason for locally whitelisting the member/role.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>localwhitelist reason <member_or_role> <reason>`
=======
 - Usage: `,localwhitelist reason <member_or_role> <reason>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>localwhitelist clear
Clear the local whitelist<br/>
 - Usage: `<@1275521742961508432>localwhitelist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>blacklist
Manage Starfire's blacklist<br/>
 - Usage: `<@1275521742961508432>blacklist`
=======
# ,blacklist
Manage Starfire's blacklist<br/>
 - Usage: `,blacklist`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `blocklist`


<<<<<<< HEAD
## <@1275521742961508432>blacklist clear
Clear the blacklist<br/>
 - Usage: `<@1275521742961508432>blacklist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>blacklist log
Manage the log settings for AdvancedBlacklist.<br/>
 - Usage: `<@1275521742961508432>blacklist log`


### <@1275521742961508432>blacklist log remove
Remove the channel for logging black/whitelistings<br/>
 - Usage: `<@1275521742961508432>blacklist log remove`


### <@1275521742961508432>blacklist log set
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
Set the channel for logging black/whitelistings<br/>

**Arguments**<br/>
    - `channel` The channel or thread to use for logging.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>blacklist log set <channel>`
=======
 - Usage: `,blacklist log set <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>blacklist add
=======
## ,blacklist clear
Clear the blacklist<br/>
 - Usage: `,blacklist clear [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,blacklist add
>>>>>>> 9e308722 (Revamped and Fixed)
Add users to the blacklist.<br/>

**Arguments**<br/>
    - `users` The users to add to the blacklist. These cannot be bots.<br/>
    - `reason` The reason for adding these users to the blacklist. This is optional.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>blacklist add <users> [reason]`
=======
 - Usage: `,blacklist add <users> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>blacklist reason
=======
## ,blacklist reason
>>>>>>> 9e308722 (Revamped and Fixed)
Edit the reason for a user in the blacklist.<br/>

**Arguments**<br/>
    - `user` The user to edit the reason of.<br/>
    - `reason` The new reason for blacklisting this user.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>blacklist reason <user> <reason>`
=======
 - Usage: `,blacklist reason <user> <reason>`
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>blacklist remove
=======
## ,blacklist remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove users from the blacklist.<br/>

**Arguments**<br/>
    - `users` The users to remove from the blacklist.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>blacklist remove <users>`
=======
 - Usage: `,blacklist remove <users>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>blacklist list
List the users in the blacklist.<br/>
 - Usage: `<@1275521742961508432>blacklist list`


# <@1275521742961508432>localblacklist
Manage the local blacklist for your server.<br/>
 - Usage: `<@1275521742961508432>localblacklist`
=======
# ,localblacklist
Manage the local blacklist for your server.<br/>
 - Usage: `,localblacklist`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `localblocklist`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>localblacklist reason
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
Edit the reason for a member or role in the local blacklist.<br/>

**Arguments**<br/>
    - `member_or_role` The member/role to edit the reason of. Members cannot be a bot.<br/>
    - `reason` The new reason for blacklisting the member/role.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>localblacklist reason <member_or_role> <reason>`
=======
 - Usage: `,localblacklist reason <member_or_role> <reason>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>localblacklist clear
Clear the local blacklist<br/>
 - Usage: `<@1275521742961508432>localblacklist clear [confirm=False]`
=======
## ,localblacklist clear
Clear the local blacklist<br/>
 - Usage: `,localblacklist clear [confirm=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>localblacklist remove
=======
## ,localblacklist remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove users from the local blacklist.<br/>

**Arguments**<br/>
    - `users` The users to remove from the local blacklist.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>localblacklist remove <users>`
=======
 - Usage: `,localblacklist remove <users>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>localblacklist list
List the members and roles in the local blacklist.<br/>
 - Usage: `<@1275521742961508432>localblacklist list`


## <@1275521742961508432>localblacklist add
Add users to the local blacklist<br/>

**Arguments**<br/>
    - `members_or_roles` The members or roles to add to the local blacklist. Members cannot be bots<br/>
    - `reason` The reason for adding these members/roles to the blacklist. This is optional<br/>
 - Usage: `<@1275521742961508432>localblacklist add <members_or_roles> [reason]`
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>advancedblacklistversion
Get the version of Advanced Blacklist that Starfire is running<br/>
 - Usage: `<@1275521742961508432>advancedblacklistversion`
=======
## ,localblacklist list
List the members and roles in the local blacklist.<br/>
 - Usage: `,localblacklist list`


# ,advancedblacklistversion
Get the version of Advanced Blacklist that Starfire is running<br/>
 - Usage: `,advancedblacklistversion`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `abversion`


