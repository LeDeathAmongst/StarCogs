A cog to assign temporary roles to users, expiring after a set duration!

# ,temproles (Hybrid Command)
Assign TempRoles roles to users, expiring after a set time.<br/>
 - Usage: `,temproles`
 - Slash Usage: `/temproles`
 - Aliases: `temprole`
 - Checks: `server_only`
## ,temproles mylist (Hybrid Command)
List active Temp Roles for yourself.<br/>
 - Usage: `,temproles mylist`
 - Slash Usage: `/temproles mylist`
 - Checks: `server_only`
## ,temproles addallowedselftemprole (Hybrid Command)
Add an allowed self Temp Role.<br/>

**Parameters:**<br/>
- `min_duration`: The minimum duration for the self temp role. `none` to disable. Defaults is 1 day.<br/>
- `max_duration`: The minimum duration for the self temp role. `none` to disable. Defaults is 365 days.<br/>
 - Usage: `,temproles addallowedselftemprole <role> [min_duration=1 day, 0:00:00] [max_duration=365 days, 0:00:00]`
 - Slash Usage: `/temproles addallowedselftemprole <role> [min_duration=1 day, 0:00:00] [max_duration=365 days, 0:00:00]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles edit (Hybrid Command)
Edit a TempRole for a member, for a specified duration.<br/>
 - Usage: `,temproles edit <member> <role> <duration>`
 - Slash Usage: `/temproles edit <member> <role> <duration>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles logschannel (Hybrid Command)
Set the logs channel for Temp Roles.<br/>
 - Usage: `,temproles logschannel [logs_channel=None]`
 - Slash Usage: `/temproles logschannel [logs_channel=None]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### logs_channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,temproles addjoiningtemprole (Hybrid Command)
Add a joining Temp Role.<br/>

**Parameters:**<br/>
- `role`: The role to assign to new members.<br/>
- `duration`: The duration of the role.<br/>
 - Usage: `,temproles addjoiningtemprole <role> <duration>`
 - Slash Usage: `/temproles addjoiningtemprole <role> <duration>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles selflist (Hybrid Command)
Unassign/Remove an allowed self Temp Role from yourself.<br/>
 - Usage: `,temproles selflist`
 - Slash Usage: `/temproles selflist`
 - Checks: `server_only`
## ,temproles list (Hybrid Command)
List active Temp Roles on this server, for optional specified member and/or role.<br/>
 - Usage: `,temproles list [member=None] [role=None]`
 - Slash Usage: `/temproles list [member=None] [role=None]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
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
> ### role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles selfunassign (Hybrid Command)
Unassign/Remove an allowed self Temp Role from yourself.<br/>
 - Usage: `,temproles selfunassign <role>`
 - Slash Usage: `/temproles selfunassign <role>`
 - Aliases: `selfremove`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles removejoiningtemprole (Hybrid Command)
Remove a joining Temp Role.<br/>
 - Usage: `,temproles removejoiningtemprole <role>`
 - Slash Usage: `/temproles removejoiningtemprole <role>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles joiningtemproles (Hybrid Command)
List the joining Temp Roles.<br/>
 - Usage: `,temproles joiningtemproles`
 - Slash Usage: `/temproles joiningtemproles`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## ,temproles unassign (Hybrid Command)
Unassign/Remove a TempRole from a member.<br/>
 - Usage: `,temproles unassign <member> <role>`
 - Slash Usage: `/temproles unassign <member> <role>`
 - Restricted to: `ADMIN`
 - Aliases: `remove and -`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles assign (Hybrid Command)
Assign/Add a TempRole to a member, for a specified duration.<br/>
 - Usage: `,temproles assign <member> <role> <duration>`
 - Slash Usage: `/temproles assign <member> <role> <duration>`
 - Restricted to: `ADMIN`
 - Aliases: `add and +`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles removeallowedselftemprole (Hybrid Command)
Remove an allowed self Temp Role.<br/>
 - Usage: `,temproles removeallowedselftemprole <role>`
 - Slash Usage: `/temproles removeallowedselftemprole <role>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,temproles selfassign (Hybrid Command)
Assign/Add an allowed self Temp Role to yourself, for a specified duration.<br/>
 - Usage: `,temproles selfassign <role> <duration>`
 - Slash Usage: `/temproles selfassign <role> <duration>`
 - Aliases: `selfadd`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     