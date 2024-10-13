Useful role commands.<br/><br/>Includes massroling, role targeting, autoroling and reaction roles.

# ,reactrole
Base command for Reaction Role management.<br/>
 - Usage: `,reactrole`
## ,reactrole create
Create a reaction role.<br/>

Emoji and role groups should be seperated by a ';' and have no space.<br/>

Example:<br/>
    - ,reactrole create 🎃;@SpookyRole 🅱️;MemeRole #role_channel Red<br/>
 - Usage: `,reactrole create <emoji_role_groups> [channel=None] [color=None] [name]`
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
## ,reactrole list
View the reaction roles on this server.<br/>
 - Usage: `,reactrole list`
## ,reactrole delete
Delete an entire reaction role for a message.<br/>
 - Usage: `,reactrole delete <message>`
 - Aliases: `remove`
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     
### ,reactrole delete bind
Delete an emoji-role bind for a reaction role.<br/>
 - Usage: `,reactrole delete bind <message> <emoji>`
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     
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
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
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
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,role color
Change a role's color.<br/>
 - Usage: `,role color <role> <color>`
 - Aliases: `colour`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
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
Extended Arg Info
> ### hoisted: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,role create
Creates a role.<br/>

Color and whether it is hoisted can be specified.<br/>
 - Usage: `,role create [color=#000000] [hoist=False] [name]`
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
## ,role members
Sends a list of members in a role.<br/>

You can supply a custom formatting tagscript for each member.<br/>
The [member](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block) block is available to use, found on the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/index.html).<br/>

**Example:**<br/>
`,role dump @admin <t:{member(timestamp)}> - {member(mention)}`<br/>
 - Usage: `,role members <role> [formatting]`
 - Aliases: `dump`
Extended Arg Info
> ### formatting: str = '{member} - {member(id)}'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,role rbots
Remove a role from all bots in the server.<br/>
 - Usage: `,role rbots <role>`
## ,role custom
Add/Remove roles to one or more users<br/>

You cannot add and remove the same Role<br/>

**Example:**<br/>
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
