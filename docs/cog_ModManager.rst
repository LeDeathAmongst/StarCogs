ModManager
==========

Force ban/kick users so that they stay in the ban/kick list
even if someone tries to manually unban them.

<<<<<<< HEAD
# <@1275521742961508432>modmanager
Mod Manager Commands.<br/>
 - Usage: `<@1275521742961508432>modmanager`
=======
# ,modmanager
Mod Manager Commands.<br/>
 - Usage: `,modmanager`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `mm, mmanager, and manager`
 - Cooldown: `1 per 10.0 seconds`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>modmanager modlog
Toggle the Mod Manager modlogs.<br/>
 - Usage: `<@1275521742961508432>modmanager modlog <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>modmanager clear
Clear the ban or kick list.<br/>
 - Usage: `<@1275521742961508432>modmanager clear <ban_or_kick>`


## <@1275521742961508432>modmanager list
Showcase the ban or kick list.<br/>
 - Usage: `<@1275521742961508432>modmanager list <ban_or_kick>`


## <@1275521742961508432>modmanager toggle
Toggle Mod Manager.<br/>
 - Usage: `<@1275521742961508432>modmanager toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>modmanager settings
Show the Mod Manager settings.<br/>
 - Usage: `<@1275521742961508432>modmanager settings`
 - Aliases: `show and showsettings`


## <@1275521742961508432>modmanager reason
Change the ban or kick reason.<br/>
 - Usage: `<@1275521742961508432>modmanager reason <ban_or_kick> <user> <reason>`
=======
## ,modmanager list
Showcase the ban or kick list.<br/>
 - Usage: `,modmanager list <ban_or_kick>`


## ,modmanager settings
Show the Mod Manager settings.<br/>
 - Usage: `,modmanager settings`
 - Aliases: `show and showsettings`


## ,modmanager clear
Clear the ban or kick list.<br/>
 - Usage: `,modmanager clear <ban_or_kick>`


## ,modmanager modlog
Toggle the Mod Manager modlogs.<br/>
 - Usage: `,modmanager modlog <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,modmanager toggle
Toggle Mod Manager.<br/>
 - Usage: `,modmanager toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,modmanager reason
Change the ban or kick reason.<br/>
 - Usage: `,modmanager reason <ban_or_kick> <user> <reason>`
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
## <@1275521742961508432>modmanager force
Force add users to the ban or kick list.<br/>
 - Usage: `<@1275521742961508432>modmanager force`


### <@1275521742961508432>modmanager force ban
Force add users to the ban list.<br/>
 - Usage: `<@1275521742961508432>modmanager force ban <add_or_remove> <users> [reason]`
Extended Arg Info
> ### reason: str = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>modmanager force kick
Force add users to the kick list.<br/>
 - Usage: `<@1275521742961508432>modmanager force kick <add_or_remove> <users> [reason]`
=======
## ,modmanager force
Force add users to the ban or kick list.<br/>
 - Usage: `,modmanager force`


### ,modmanager force kick
Force add users to the kick list.<br/>
 - Usage: `,modmanager force kick <add_or_remove> <users> [reason]`
Extended Arg Info
> ### reason: str = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,modmanager force ban
Force add users to the ban list.<br/>
 - Usage: `,modmanager force ban <add_or_remove> <users> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### reason: str = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


