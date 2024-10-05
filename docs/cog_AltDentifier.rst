AltDentifier
============

Check new users with AltDentifier API

# <@1275521742961508432>altcheck
Check a user on AltDentifier.<br/>
 - Usage: `<@1275521742961508432>altcheck [member]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member = None
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


# <@1275521742961508432>altset
Manage AltDentifier Settings.<br/>
 - Usage: `<@1275521742961508432>altset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## <@1275521742961508432>altset channel
Set the channel to send AltDentifier join checks to.<br/>

This also works as a toggle, so if no channel is provided, it will disable join checks for this server.<br/>
 - Usage: `<@1275521742961508432>altset channel [channel=None]`
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


## <@1275521742961508432>altset settings
View AltDentifier Settings.<br/>
 - Usage: `<@1275521742961508432>altset settings`


## <@1275521742961508432>altset whitelist
Whitelist a user from AltDentifier actions.<br/>
 - Usage: `<@1275521742961508432>altset whitelist <user_id>`
 - Aliases: `wl`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>altset unwhitelist
Remove a user from the AltDentifier whitelist.<br/>
 - Usage: `<@1275521742961508432>altset unwhitelist <user_id>`
 - Aliases: `unwl`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>altset action
Specify what actions to take when a member joins and has a certain Trust Level.<br/>

Leave this empty to remove actions for the Level.<br/>
The available actions are:<br/>
`kick`<br/>
`ban`<br/>
`role` (don't say 'role' for this, pass an actual role)<br/>
 - Usage: `<@1275521742961508432>altset action <level> [action=None]`
Extended Arg Info
> ### action: Union[discord.role.Role, str] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


