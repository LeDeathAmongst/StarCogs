RoleUtils
=========

Useful role commands.

Includes massroling, role targeting, autoroling and reaction roles.

<<<<<<< HEAD
# <@1275521742961508432>reactrole
Base command for Reaction Role management.<br/>
 - Usage: `<@1275521742961508432>reactrole`


## <@1275521742961508432>reactrole bind
Bind a reaction role to an emoji on a message.<br/>
 - Usage: `<@1275521742961508432>reactrole bind <message> <emoji> <role>`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     


## <@1275521742961508432>reactrole create
=======
# ,reactrole
Base command for Reaction Role management.<br/>
 - Usage: `,reactrole`


## ,reactrole create
>>>>>>> 9e308722 (Revamped and Fixed)
Create a reaction role.<br/>

Emoji and role groups should be seperated by a ';' and have no space.<br/>

Example:<br/>
<<<<<<< HEAD
    - <@1275521742961508432>reactrole create 🎃;@SpookyRole 🅱️;MemeRole #role_channel Red<br/>
 - Usage: `<@1275521742961508432>reactrole create <emoji_role_groups> [channel=None] [color=None] [name]`
=======
    - ,reactrole create 🎃;@SpookyRole 🅱️;MemeRole #role_channel Red<br/>
 - Usage: `,reactrole create <emoji_role_groups> [channel=None] [color=None] [name]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### color: Optional[discord.colour.Colour] = None
> Converts to a :class:`~discord.Colour`.
> 
>     
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>reactrole clear
Clear all ReactRole data.<br/>
 - Usage: `<@1275521742961508432>reactrole clear`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>reactrole list
View the reaction roles on this server.<br/>
 - Usage: `<@1275521742961508432>reactrole list`


## <@1275521742961508432>reactrole delete
Delete an entire reaction role for a message.<br/>
 - Usage: `<@1275521742961508432>reactrole delete <message>`
=======
## ,reactrole list
View the reaction roles on this server.<br/>
 - Usage: `,reactrole list`


## ,reactrole delete
Delete an entire reaction role for a message.<br/>
 - Usage: `,reactrole delete <message>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `remove`
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     


<<<<<<< HEAD
### <@1275521742961508432>reactrole delete bind
Delete an emoji-role bind for a reaction role.<br/>
 - Usage: `<@1275521742961508432>reactrole delete bind <message> <emoji>`
=======
### ,reactrole delete bind
Delete an emoji-role bind for a reaction role.<br/>
 - Usage: `,reactrole delete bind <message> <emoji>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>autorole
Manage autoroles and sticky roles.<br/>
 - Usage: `<@1275521742961508432>autorole`
 - Checks: `server_only`


## <@1275521742961508432>autorole sticky

 - Usage: `<@1275521742961508432>autorole sticky`
 - Aliases: `stickyrole`


### <@1275521742961508432>autorole sticky set

 - Usage: `<@1275521742961508432>autorole sticky set <add_or_remove> <role>`
 - Aliases: `role`


### <@1275521742961508432>autorole sticky remove

 - Usage: `<@1275521742961508432>autorole sticky remove <users> <role>`


### <@1275521742961508432>autorole sticky add

 - Usage: `<@1275521742961508432>autorole sticky add <users> <role>`


## <@1275521742961508432>autorole humans
Manage autoroles for humans.<br/>
 - Usage: `<@1275521742961508432>autorole humans`


### <@1275521742961508432>autorole humans toggle
Toggle the human only autorole system.<br/>
 - Usage: `<@1275521742961508432>autorole humans toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>autorole humans add
Add a role to be added to all new humans on join.<br/>
 - Usage: `<@1275521742961508432>autorole humans add <role>`


### <@1275521742961508432>autorole humans remove
Remove an autorole for humans.<br/>
 - Usage: `<@1275521742961508432>autorole humans remove <role>`


## <@1275521742961508432>autorole toggle
Toggle the auto role system.<br/>
 - Usage: `<@1275521742961508432>autorole toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>autorole remove
Remove an autorole.<br/>
 - Usage: `<@1275521742961508432>autorole remove <role>`


## <@1275521742961508432>autorole add
Add a role to be added to all new members on join.<br/>
 - Usage: `<@1275521742961508432>autorole add <role>`


## <@1275521742961508432>autorole bots
Manage autoroles for bots.<br/>
 - Usage: `<@1275521742961508432>autorole bots`


### <@1275521742961508432>autorole bots toggle
Toggle the bots only autorole system.<br/>
 - Usage: `<@1275521742961508432>autorole bots toggle <toggle>`
=======
## ,reactrole bind
Bind a reaction role to an emoji on a message.<br/>
 - Usage: `,reactrole bind <message> <emoji> <role>`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     


## ,reactrole clear
Clear all ReactRole data.<br/>
 - Usage: `,reactrole clear`
 - Restricted to: `BOT_OWNER`


# ,autorole
Manage autoroles and sticky roles.<br/>
 - Usage: `,autorole`
 - Checks: `server_only`


## ,autorole remove
Remove an autorole.<br/>
 - Usage: `,autorole remove <role>`


## ,autorole toggle
Toggle the auto role system.<br/>
 - Usage: `,autorole toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,autorole humans
Manage autoroles for humans.<br/>
 - Usage: `,autorole humans`


### ,autorole humans add
Add a role to be added to all new humans on join.<br/>
 - Usage: `,autorole humans add <role>`


### ,autorole humans remove
Remove an autorole for humans.<br/>
 - Usage: `,autorole humans remove <role>`


### ,autorole humans toggle
Toggle the human only autorole system.<br/>
 - Usage: `,autorole humans toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,autorole add
Add a role to be added to all new members on join.<br/>
 - Usage: `,autorole add <role>`


## ,autorole sticky

 - Usage: `,autorole sticky`
 - Aliases: `stickyrole`


### ,autorole sticky add

 - Usage: `,autorole sticky add <users> <role>`


### ,autorole sticky remove

 - Usage: `,autorole sticky remove <users> <role>`


### ,autorole sticky set

 - Usage: `,autorole sticky set <add_or_remove> <role>`
 - Aliases: `role`


## ,autorole bots
Manage autoroles for bots.<br/>
 - Usage: `,autorole bots`


### ,autorole bots toggle
Toggle the bots only autorole system.<br/>
 - Usage: `,autorole bots toggle <toggle>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
### <@1275521742961508432>autorole bots remove
Remove an autorole for bots.<br/>
 - Usage: `<@1275521742961508432>autorole bots remove <role>`


### <@1275521742961508432>autorole bots add
Add a role to be added to all new bots on join.<br/>
 - Usage: `<@1275521742961508432>autorole bots add <role>`


# <@1275521742961508432>role
Base command for modifying roles.<br/>

Invoking this command will add or remove the given role from the member, depending on whether they already had it.<br/>
 - Usage: `<@1275521742961508432>role <member> <role>`
 - Checks: `server_only`


## <@1275521742961508432>role colors
Sends the server's roles, ordered by color.<br/>
 - Usage: `<@1275521742961508432>role colors`


## <@1275521742961508432>role in
Add a role to all members of a another role.<br/>
 - Usage: `<@1275521742961508432>role in <target_role> <add_role>`


## <@1275521742961508432>role add
Add a role to a member.<br/>
 - Usage: `<@1275521742961508432>role add <member> <role>`


## <@1275521742961508432>role info
Get information about a role.<br/>
 - Usage: `<@1275521742961508432>role info <role>`


## <@1275521742961508432>role humans
Add a role to all humans (non-bots) in the server.<br/>
 - Usage: `<@1275521742961508432>role humans <role>`


## <@1275521742961508432>role rin
Remove a role from all members of a another role.<br/>
 - Usage: `<@1275521742961508432>role rin <target_role> <remove_role>`


## <@1275521742961508432>role rhumans
Remove a role from all humans (non-bots) in the server.<br/>
 - Usage: `<@1275521742961508432>role rhumans <role>`


## <@1275521742961508432>role all
Add a role to all members of the server.<br/>
 - Usage: `<@1275521742961508432>role all <role>`


## <@1275521742961508432>role remove
Remove a role from a member.<br/>
 - Usage: `<@1275521742961508432>role remove <member> <role>`


## <@1275521742961508432>role name
Change a role's name.<br/>
 - Usage: `<@1275521742961508432>role name <role> <name>`
=======
### ,autorole bots add
Add a role to be added to all new bots on join.<br/>
 - Usage: `,autorole bots add <role>`


### ,autorole bots remove
Remove an autorole for bots.<br/>
 - Usage: `,autorole bots remove <role>`


# ,role
Base command for modifying roles.<br/>

Invoking this command will add or remove the given role from the member, depending on whether they already had it.<br/>
 - Usage: `,role <member> <role>`
 - Checks: `server_only`


## ,role info
Get information about a role.<br/>
 - Usage: `,role info <role>`


## ,role humans
Add a role to all humans (non-bots) in the server.<br/>
 - Usage: `,role humans <role>`


## ,role rin
Remove a role from all members of a another role.<br/>
 - Usage: `,role rin <target_role> <remove_role>`


## ,role rhumans
Remove a role from all humans (non-bots) in the server.<br/>
 - Usage: `,role rhumans <role>`


## ,role all
Add a role to all members of the server.<br/>
 - Usage: `,role all <role>`


## ,role remove
Remove a role from a member.<br/>
 - Usage: `,role remove <member> <role>`


## ,role name
Change a role's name.<br/>
 - Usage: `,role name <role> <name>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>role color
Change a role's color.<br/>
 - Usage: `<@1275521742961508432>role color <role> <color>`
=======
## ,role color
Change a role's color.<br/>
 - Usage: `,role color <role> <color>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `colour`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>role target
Modify roles using 'targeting' args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `<@1275521742961508432>target`.<br/>
 - Usage: `<@1275521742961508432>role target`
 - Checks: `targeter_cog`


### <@1275521742961508432>role target add
Add a role to members using targeting args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `<@1275521742961508432>target`.<br/>
 - Usage: `<@1275521742961508432>role target add <role> <args>`


### <@1275521742961508432>role target remove
Remove a role from members using targeting args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `<@1275521742961508432>target`.<br/>
 - Usage: `<@1275521742961508432>role target remove <role> <args>`


## <@1275521742961508432>role bots
Add a role to all bots in the server.<br/>
 - Usage: `<@1275521742961508432>role bots <role>`


## <@1275521742961508432>role addmulti
Add a role to multiple members.<br/>
 - Usage: `<@1275521742961508432>role addmulti <role> <members>`


## <@1275521742961508432>role uniquemembers
View the total unique members between multiple roles.<br/>
 - Usage: `<@1275521742961508432>role uniquemembers <roles>`
 - Aliases: `um`


## <@1275521742961508432>role hoist
Toggle whether a role should appear seperate from other roles.<br/>
 - Usage: `<@1275521742961508432>role hoist <role> [hoisted=None]`
=======
## ,role target
Modify roles using 'targeting' args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `,target`.<br/>
 - Usage: `,role target`
 - Checks: `targeter_cog`


### ,role target remove
Remove a role from members using targeting args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `,target`.<br/>
 - Usage: `,role target remove <role> <args>`


### ,role target add
Add a role to members using targeting args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `,target`.<br/>
 - Usage: `,role target add <role> <args>`


## ,role bots
Add a role to all bots in the server.<br/>
 - Usage: `,role bots <role>`


## ,role addmulti
Add a role to multiple members.<br/>
 - Usage: `,role addmulti <role> <members>`


## ,role uniquemembers
View the total unique members between multiple roles.<br/>
 - Usage: `,role uniquemembers <roles>`
 - Aliases: `um`


## ,role hoist
Toggle whether a role should appear seperate from other roles.<br/>
 - Usage: `,role hoist <role> [hoisted=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### hoisted: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>role create
Creates a role.<br/>

Color and whether it is hoisted can be specified.<br/>
 - Usage: `<@1275521742961508432>role create [color=#000000] [hoist=False] [name]`
=======
## ,role create
Creates a role.<br/>

Color and whether it is hoisted can be specified.<br/>
 - Usage: `,role create [color=#000000] [hoist=False] [name]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### color: Optional[discord.colour.Colour] = <Colour value=0>
> Converts to a :class:`~discord.Colour`.
> 
>     
> ### hoist: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>role members
=======
## ,role members
>>>>>>> 9e308722 (Revamped and Fixed)
Sends a list of members in a role.<br/>

You can supply a custom formatting tagscript for each member.<br/>
The [member](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block) block is available to use, found on the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/index.html).<br/>

**Example:**<br/>
<<<<<<< HEAD
`<@1275521742961508432>role dump @admin <t:{member(timestamp)}> - {member(mention)}`<br/>
 - Usage: `<@1275521742961508432>role members <role> [formatting]`
=======
`,role dump @admin <t:{member(timestamp)}> - {member(mention)}`<br/>
 - Usage: `,role members <role> [formatting]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `dump`
Extended Arg Info
> ### formatting: str = '{member} - {member(id)}'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>role rbots
Remove a role from all bots in the server.<br/>
 - Usage: `<@1275521742961508432>role rbots <role>`


## <@1275521742961508432>role custom
=======
## ,role rbots
Remove a role from all bots in the server.<br/>
 - Usage: `,role rbots <role>`


## ,role custom
>>>>>>> 9e308722 (Revamped and Fixed)
Add/Remove roles to one or more users<br/>

You cannot add and remove the same Role<br/>

**Example:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>role custom inthedark.org --add role1 --remove role2`<br/>
- `<@1275521742961508432> role custom inthedark.org --add role1 "role to remove"`<br/>
 - Usage: `<@1275521742961508432>role custom <users> <flags>`


## <@1275521742961508432>role removemulti
Remove a role from multiple members.<br/>
 - Usage: `<@1275521742961508432>role removemulti <role> <members>`


## <@1275521742961508432>role rall
Remove a role from all members of the server.<br/>
 - Usage: `<@1275521742961508432>role rall <role>`
 - Aliases: `removeall`


# <@1275521742961508432>multirole
Add multiple roles to a member.<br/>
 - Usage: `<@1275521742961508432>multirole <member> <roles>`


## <@1275521742961508432>multirole remove
Remove multiple roles from a member.<br/>
 - Usage: `<@1275521742961508432>multirole remove <member> <roles>`
=======
- `,role custom inthedark.org --add role1 --remove role2`<br/>
- `, role custom inthedark.org --add role1 "role to remove"`<br/>
 - Usage: `,role custom <users> <flags>`


## ,role removemulti
Remove a role from multiple members.<br/>
 - Usage: `,role removemulti <role> <members>`


## ,role rall
Remove a role from all members of the server.<br/>
 - Usage: `,role rall <role>`
 - Aliases: `removeall`


## ,role colors
Sends the server's roles, ordered by color.<br/>
 - Usage: `,role colors`


## ,role in
Add a role to all members of a another role.<br/>
 - Usage: `,role in <target_role> <add_role>`


## ,role add
Add a role to a member.<br/>
 - Usage: `,role add <member> <role>`


# ,multirole
Add multiple roles to a member.<br/>
 - Usage: `,multirole <member> <roles>`


## ,multirole remove
Remove multiple roles from a member.<br/>
 - Usage: `,multirole remove <member> <roles>`
>>>>>>> 9e308722 (Revamped and Fixed)


