DontPingStaff
=============

Punish users for pinging staff.

# <@1275521742961508432>dps
Dont ping staff.<br/>
 - Usage: `<@1275521742961508432>dps`
 - Restricted to: `ADMIN`


## <@1275521742961508432>dps removeroles
Manage roles to be removed from the user.<br/>
 - Usage: `<@1275521742961508432>dps removeroles`


### <@1275521742961508432>dps removeroles list
List the roles to be removed from the user.<br/>
 - Usage: `<@1275521742961508432>dps removeroles list`


### <@1275521742961508432>dps removeroles remove
Remove a role from being removed from the user.<br/>
 - Usage: `<@1275521742961508432>dps removeroles remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>dps removeroles add
Add a role to be removed from the user.<br/>
 - Usage: `<@1275521742961508432>dps removeroles add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>dps amount
Set how many pings are needed to trigger an action.<br/>
 - Usage: `<@1275521742961508432>dps amount <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>dps toggle
Toggle the module.<br/>
 - Usage: `<@1275521742961508432>dps toggle`


## <@1275521742961508432>dps muterole
Set a role to be used for muting.<br/>
 - Usage: `<@1275521742961508432>dps muterole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>dps whitelist
Manage whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist`
 - Aliases: `ignore`


### <@1275521742961508432>dps whitelist add
Add users/roles/channels to the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist add`


#### <@1275521742961508432>dps whitelist add role
Add roles to the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist add role [roles=None]`


#### <@1275521742961508432>dps whitelist add user
Add users to the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist add user [users=None]`


#### <@1275521742961508432>dps whitelist add channel
Add channels to the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist add channel [channels=None]`


### <@1275521742961508432>dps whitelist remove
Remove users/roles/channels from the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist remove`


#### <@1275521742961508432>dps whitelist remove role
Remove roles from the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist remove role [roles=None]`


#### <@1275521742961508432>dps whitelist remove channel
Remove channels from the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist remove channel [channels=None]`


#### <@1275521742961508432>dps whitelist remove user
Remove users from the whitelist.<br/>
 - Usage: `<@1275521742961508432>dps whitelist remove user [users=None]`


## <@1275521742961508432>dps addroles
Manage roles to be added to the user.<br/>
 - Usage: `<@1275521742961508432>dps addroles`


### <@1275521742961508432>dps addroles remove
Remove a role from being added to the user.<br/>
 - Usage: `<@1275521742961508432>dps addroles remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>dps addroles list
List the roles to be added to the user.<br/>
 - Usage: `<@1275521742961508432>dps addroles list`


### <@1275521742961508432>dps addroles add
Add a role to be added to the user.<br/>
 - Usage: `<@1275521742961508432>dps addroles add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>dps settings
Show the current settings.<br/>
 - Usage: `<@1275521742961508432>dps settings`


## <@1275521742961508432>dps per
Set how long to wait between actions.<br/>
 - Usage: `<@1275521742961508432>dps per <time>`


## <@1275521742961508432>dps action
Choose none, kick, ban, mute, addroles, removeroles as the action.<br/>
 - Usage: `<@1275521742961508432>dps action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>dps scope
Set the scope of the module.<br/>

**Scope**<br/>
- `server` - Enable DPS __**server-wide**__ by passing **server**.<br/>
- `category` - Enable DPS for a specific category by passing its **category ID**.<br/>
- `channel` - Enable DPS for a specific channel by passing its **channel ID**.<br/>

**Note**: You can specify multiple categories and channels, separated **by a space**. Running the command again will **override** the previous configuration.<br/>

**Example**<br/>
- To enable DPS for **specific channels**, **categories**, or a **mix of both**: `dps scope 123456789 123456789 123456789`<br/>
 - Usage: `<@1275521742961508432>dps scope <scope>`
 - Restricted to: `ADMIN`


## <@1275521742961508432>dps message
Set the message to be sent to the user.<br/>
 - Usage: `<@1275521742961508432>dps message <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>dps staffrole
Command for managing the staff role.<br/>
 - Usage: `<@1275521742961508432>dps staffrole`


### <@1275521742961508432>dps staffrole remove
Remove a role from the staff role.<br/>
 - Usage: `<@1275521742961508432>dps staffrole remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>dps staffrole list
List the staff roles.<br/>
 - Usage: `<@1275521742961508432>dps staffrole list`


### <@1275521742961508432>dps staffrole add
Add a role to the staff role.<br/>
 - Usage: `<@1275521742961508432>dps staffrole add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


