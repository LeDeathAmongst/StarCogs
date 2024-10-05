Useful role commands.<br/><br/>Includes massroling, role targeting, autoroling and reaction roles.

# <@1275521742961508432>reactrole
Base command for Reaction Role management.<br/>
 - Usage: `<@1275521742961508432>reactrole`
## <@1275521742961508432>reactrole clear
Clear all ReactRole data.<br/>
 - Usage: `<@1275521742961508432>reactrole clear`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>reactrole bind
Bind a reaction role to an emoji on a message.<br/>
 - Usage: `<@1275521742961508432>reactrole bind <message> <emoji> <role>`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
## <@1275521742961508432>reactrole delete
Delete an entire reaction role for a message.<br/>
 - Usage: `<@1275521742961508432>reactrole delete <message>`
 - Aliases: `remove`
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     
### <@1275521742961508432>reactrole delete bind
Delete an emoji-role bind for a reaction role.<br/>
 - Usage: `<@1275521742961508432>reactrole delete bind <message> <emoji>`
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     
## <@1275521742961508432>reactrole create
Create a reaction role.<br/>

Emoji and role groups should be seperated by a ';' and have no space.<br/>

Example:<br/>
    - <@1275521742961508432>reactrole create 🎃;@SpookyRole 🅱️;MemeRole #role_channel Red<br/>
 - Usage: `<@1275521742961508432>reactrole create <emoji_role_groups> [channel=None] [color=None] [name]`
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
## <@1275521742961508432>reactrole list
View the reaction roles on this server.<br/>
 - Usage: `<@1275521742961508432>reactrole list`
# <@1275521742961508432>autorole
Manage autoroles and sticky roles.<br/>
 - Usage: `<@1275521742961508432>autorole`
 - Checks: `server_only`
## <@1275521742961508432>autorole bots
Manage autoroles for bots.<br/>
 - Usage: `<@1275521742961508432>autorole bots`
### <@1275521742961508432>autorole bots add
Add a role to be added to all new bots on join.<br/>
 - Usage: `<@1275521742961508432>autorole bots add <role>`
### <@1275521742961508432>autorole bots toggle
Toggle the bots only autorole system.<br/>
 - Usage: `<@1275521742961508432>autorole bots toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### <@1275521742961508432>autorole bots remove
Remove an autorole for bots.<br/>
 - Usage: `<@1275521742961508432>autorole bots remove <role>`
## <@1275521742961508432>autorole sticky

 - Usage: `<@1275521742961508432>autorole sticky`
 - Aliases: `stickyrole`
### <@1275521742961508432>autorole sticky remove

 - Usage: `<@1275521742961508432>autorole sticky remove <users> <role>`
### <@1275521742961508432>autorole sticky set

 - Usage: `<@1275521742961508432>autorole sticky set <add_or_remove> <role>`
 - Aliases: `role`
### <@1275521742961508432>autorole sticky add

 - Usage: `<@1275521742961508432>autorole sticky add <users> <role>`
## <@1275521742961508432>autorole toggle
Toggle the auto role system.<br/>
 - Usage: `<@1275521742961508432>autorole toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>autorole humans
Manage autoroles for humans.<br/>
 - Usage: `<@1275521742961508432>autorole humans`
### <@1275521742961508432>autorole humans add
Add a role to be added to all new humans on join.<br/>
 - Usage: `<@1275521742961508432>autorole humans add <role>`
### <@1275521742961508432>autorole humans remove
Remove an autorole for humans.<br/>
 - Usage: `<@1275521742961508432>autorole humans remove <role>`
### <@1275521742961508432>autorole humans toggle
Toggle the human only autorole system.<br/>
 - Usage: `<@1275521742961508432>autorole humans toggle <toggle>`
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
# <@1275521742961508432>role
Base command for modifying roles.<br/>

Invoking this command will add or remove the given role from the member, depending on whether they already had it.<br/>
 - Usage: `<@1275521742961508432>role <member> <role>`
 - Checks: `server_only`
## <@1275521742961508432>role removemulti
Remove a role from multiple members.<br/>
 - Usage: `<@1275521742961508432>role removemulti <role> <members>`
## <@1275521742961508432>role rall
Remove a role from all members of the server.<br/>
 - Usage: `<@1275521742961508432>role rall <role>`
 - Aliases: `removeall`
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
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>role members
Sends a list of members in a role.<br/>

You can supply a custom formatting tagscript for each member.<br/>
The [member](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block) block is available to use, found on the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/index.html).<br/>

**Example:**<br/>
`<@1275521742961508432>role dump @admin <t:{member(timestamp)}> - {member(mention)}`<br/>
 - Usage: `<@1275521742961508432>role members <role> [formatting]`
 - Aliases: `dump`
Extended Arg Info
> ### formatting: str = '{member} - {member(id)}'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>role color
Change a role's color.<br/>
 - Usage: `<@1275521742961508432>role color <role> <color>`
 - Aliases: `colour`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
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
Extended Arg Info
> ### hoisted: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>role rbots
Remove a role from all bots in the server.<br/>
 - Usage: `<@1275521742961508432>role rbots <role>`
## <@1275521742961508432>role create
Creates a role.<br/>

Color and whether it is hoisted can be specified.<br/>
 - Usage: `<@1275521742961508432>role create [color=#000000] [hoist=False] [name]`
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
## <@1275521742961508432>role custom
Add/Remove roles to one or more users<br/>

You cannot add and remove the same Role<br/>

**Example:**<br/>
- `<@1275521742961508432>role custom inthedark.org --add role1 --remove role2`<br/>
- `<@1275521742961508432> role custom inthedark.org --add role1 "role to remove"`<br/>
 - Usage: `<@1275521742961508432>role custom <users> <flags>`
# <@1275521742961508432>multirole
Add multiple roles to a member.<br/>
 - Usage: `<@1275521742961508432>multirole <member> <roles>`
## <@1275521742961508432>multirole remove
Remove multiple roles from a member.<br/>
 - Usage: `<@1275521742961508432>multirole remove <member> <roles>`
