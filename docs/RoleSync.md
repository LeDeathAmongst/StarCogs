A cog that syncs roles and their properties across multiple servers.

# ,rolesync
Sync role states between servers<br/>
 - Usage: `,rolesync`
 - Restricted to: `BOT_OWNER`
 - Aliases: `rsync`
 - Checks: `server_only`
## ,rolesync forcesync

 - Usage: `,rolesync forcesync`
 - Aliases: `fsync`
## ,rolesync remove
Remove a role from being synced between servers.<br/>
 - Usage: `,rolesync remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,rolesync list
List synced roles<br/>
 - Usage: `,rolesync list`
## ,rolesync add
Add a role to sync between server<br/>

The role argument must be a role mention or ID.<br/>
The servers argument accepts server IDs<br/>
 - Usage: `,rolesync add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
