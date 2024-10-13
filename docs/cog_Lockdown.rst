Lockdown
========

Locks down the current server

To get started, you will need to set up a role to be used when locking
down your server. This role needs to be above all roles it should affect
in the hierarchy as it will be used to determine who should be affected
by the lockdown and this role will be applied to each user. The 
role's permissions should be set up to deny access to things the affected 
users should not be able to do during a lockdown (such as sending messages, 
talking in voice channels, adding reactions, etc).

Once you've set up the role, you can create a new profile with
`[p]lockdownset addprofile` (which takes the role (ID, mention, or name)
as an argument).

Please note that `[p]lockdown` will not work if no profiles are
available as this cog depends on using roles to run a lockdown.

<<<<<<< HEAD
# <@1275521742961508432>lockdown
Enables lockdown for this server<br/>

A profile ID must be specified. To list profiles,<br/>
do `<@1275521742961508432>lockdownset listprofiles`<br/>
 - Usage: `<@1275521742961508432>lockdown <profile>`
=======
# ,lockdown
Enables lockdown for this server<br/>

A profile ID must be specified. To list profiles,<br/>
do `,lockdownset listprofiles`<br/>
 - Usage: `,lockdown <profile>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### profile: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>unlockdown
Ends the lockdown for this server<br/>
 - Usage: `<@1275521742961508432>unlockdown`
=======
# ,unlockdown
Ends the lockdown for this server<br/>
 - Usage: `,unlockdown`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>lockdownset
Settings for lockdown<br/>
 - Usage: `<@1275521742961508432>lockdownset`
=======
# ,lockdownset
Settings for lockdown<br/>
 - Usage: `,lockdownset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>lockdownset removeprofile
Removes the lockdown profile with the specified IDs<br/>

To see a list of profiles and their IDs,<br/>
do `<@1275521742961508432>lockdownset listprofiles`<br/>
 - Usage: `<@1275521742961508432>lockdownset removeprofile <profile_id>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### profile_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>lockdownset reset
Removes all lockdown profiles for the current server.<br/>
 - Usage: `<@1275521742961508432>lockdownset reset`
 - Restricted to: `GUILD_OWNER`


## <@1275521742961508432>lockdownset addprofile
=======
## ,lockdownset addprofile
>>>>>>> 9e308722 (Revamped and Fixed)
Adds a lockdown profile.<br/>

Role is the role to be applied when triggering a lockdown<br/>
with this profile.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>lockdownset addprofile <role>`
=======
 - Usage: `,lockdownset addprofile <role>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>lockdownset listprofiles
List all lockdown profiles for the server.<br/>
 - Usage: `<@1275521742961508432>lockdownset listprofiles`
=======
## ,lockdownset reset
Removes all lockdown profiles for the current server.<br/>
 - Usage: `,lockdownset reset`
 - Restricted to: `GUILD_OWNER`


## ,lockdownset removeprofile
Removes the lockdown profile with the specified IDs<br/>

To see a list of profiles and their IDs,<br/>
do `,lockdownset listprofiles`<br/>
 - Usage: `,lockdownset removeprofile <profile_id>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### profile_id: int
> ```
> A number without decimal places.
> ```


## ,lockdownset listprofiles
List all lockdown profiles for the server.<br/>
 - Usage: `,lockdownset listprofiles`
>>>>>>> 9e308722 (Revamped and Fixed)


