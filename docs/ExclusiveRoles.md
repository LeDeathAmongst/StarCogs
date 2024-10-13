Exclusive Roles

# ,exclusivenow
Takes 2 Roles. Removes the second role if both roles are present on a user.<br/>
 - Usage: `,exclusivenow <role1> <role2>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role1: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### role2: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# ,setexclusive
Takes 2 Roles.<br/>
Removes the second role if the first role is assigned to a user in the future.<br/>
 - Usage: `,setexclusive <role1> <role2>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role1: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### role2: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# ,unexclusive
Takes 2 roles and removes their exclusivity<br/>
 - Usage: `,unexclusive <role1> <role2>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role1: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### role2: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# ,listexclusives
List all exclusive roles<br/>
 - Usage: `,listexclusives`
 - Restricted to: `ADMIN`
# ,retroscan
Scans the entire user list for roles that have been set as exclusive.<br/>
 - Usage: `,retroscan`
 - Restricted to: `ADMIN`
