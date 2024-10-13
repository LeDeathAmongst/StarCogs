DontPingStaff
=============

Punish users for pinging staff.

# ,dps
Dont ping staff.<br/>
 - Usage: `,dps`
 - Restricted to: `ADMIN`


## ,dps removeroles
Manage roles to be removed from the user.<br/>
 - Usage: `,dps removeroles`


### ,dps removeroles remove
Remove a role from being removed from the user.<br/>
 - Usage: `,dps removeroles remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### ,dps removeroles add
Add a role to be removed from the user.<br/>
 - Usage: `,dps removeroles add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### ,dps removeroles list
List the roles to be removed from the user.<br/>
 - Usage: `,dps removeroles list`


## ,dps settings
Show the current settings.<br/>
 - Usage: `,dps settings`


## ,dps staffrole
Command for managing the staff role.<br/>
 - Usage: `,dps staffrole`


### ,dps staffrole add
Add a role to the staff role.<br/>
 - Usage: `,dps staffrole add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### ,dps staffrole list
List the staff roles.<br/>
 - Usage: `,dps staffrole list`


### ,dps staffrole remove
Remove a role from the staff role.<br/>
 - Usage: `,dps staffrole remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## ,dps muterole
Set a role to be used for muting.<br/>
 - Usage: `,dps muterole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## ,dps scope
Set the scope of the module.<br/>

**Scope**<br/>
- `server` - Enable DPS __**server-wide**__ by passing **server**.<br/>
- `category` - Enable DPS for a specific category by passing its **category ID**.<br/>
- `channel` - Enable DPS for a specific channel by passing its **channel ID**.<br/>

**Note**: You can specify multiple categories and channels, separated **by a space**. Running the command again will **override** the previous configuration.<br/>

**Example**<br/>
- To enable DPS for **specific channels**, **categories**, or a **mix of both**: `dps scope 123456789 123456789 123456789`<br/>
 - Usage: `,dps scope <scope>`
 - Restricted to: `ADMIN`


## ,dps whitelist
Manage whitelist.<br/>
 - Usage: `,dps whitelist`
 - Aliases: `ignore`


### ,dps whitelist add
Add users/roles/channels to the whitelist.<br/>
 - Usage: `,dps whitelist add`


#### ,dps whitelist add user
Add users to the whitelist.<br/>
 - Usage: `,dps whitelist add user [users=None]`


#### ,dps whitelist add channel
Add channels to the whitelist.<br/>
 - Usage: `,dps whitelist add channel [channels=None]`


#### ,dps whitelist add role
Add roles to the whitelist.<br/>
 - Usage: `,dps whitelist add role [roles=None]`


### ,dps whitelist remove
Remove users/roles/channels from the whitelist.<br/>
 - Usage: `,dps whitelist remove`


#### ,dps whitelist remove channel
Remove channels from the whitelist.<br/>
 - Usage: `,dps whitelist remove channel [channels=None]`


#### ,dps whitelist remove user
Remove users from the whitelist.<br/>
 - Usage: `,dps whitelist remove user [users=None]`


#### ,dps whitelist remove role
Remove roles from the whitelist.<br/>
 - Usage: `,dps whitelist remove role [roles=None]`


## ,dps addroles
Manage roles to be added to the user.<br/>
 - Usage: `,dps addroles`


### ,dps addroles remove
Remove a role from being added to the user.<br/>
 - Usage: `,dps addroles remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### ,dps addroles list
List the roles to be added to the user.<br/>
 - Usage: `,dps addroles list`


### ,dps addroles add
Add a role to be added to the user.<br/>
 - Usage: `,dps addroles add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## ,dps per
Set how long to wait between actions.<br/>
 - Usage: `,dps per <time>`


## ,dps amount
Set how many pings are needed to trigger an action.<br/>
 - Usage: `,dps amount <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```


## ,dps toggle
Toggle the module.<br/>
 - Usage: `,dps toggle`


## ,dps action
Choose none, kick, ban, mute, addroles, removeroles as the action.<br/>
 - Usage: `,dps action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,dps message
Set the message to be sent to the user.<br/>
 - Usage: `,dps message <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


