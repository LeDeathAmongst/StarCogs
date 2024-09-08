# RoleUtils Help

### reactrole

**Description:** Base command for Reaction Role management.

**Usage:** `<@1275521742961508432>reactrole`

### reactrole bind

**Description:** Bind a reaction role to an emoji on a message.

**Usage:** `<@1275521742961508432>reactrole bind`

### reactrole list

**Description:** View the reaction roles on this server.

**Usage:** `<@1275521742961508432>reactrole list`

### reactrole create

**Description:** Create a reaction role.

Emoji and role groups should be seperated by a ';' and have no space.

Example:
    - [p]reactrole create 🎃;@SpookyRole 🅱️;MemeRole #role_channel Red

**Usage:** `<@1275521742961508432>reactrole create`

### reactrole delete

**Description:** Delete an entire reaction role for a message.

**Usage:** `<@1275521742961508432>reactrole delete`

### reactrole delete bind

**Description:** Delete an emoji-role bind for a reaction role.

**Usage:** `<@1275521742961508432>reactrole delete bind`

### autorole

**Description:** Manage autoroles and sticky roles.

**Usage:** `<@1275521742961508432>autorole`

### autorole bots

**Description:** Manage autoroles for bots.

**Usage:** `<@1275521742961508432>autorole bots`

### autorole bots add

**Description:** Add a role to be added to all new bots on join.

**Usage:** `<@1275521742961508432>autorole bots add`

### autorole bots toggle

**Description:** Toggle the bots only autorole system.

**Usage:** `<@1275521742961508432>autorole bots toggle`

### autorole bots remove

**Description:** Remove an autorole for bots.

**Usage:** `<@1275521742961508432>autorole bots remove`

### autorole humans

**Description:** Manage autoroles for humans.

**Usage:** `<@1275521742961508432>autorole humans`

### autorole humans toggle

**Description:** Toggle the human only autorole system.

**Usage:** `<@1275521742961508432>autorole humans toggle`

### autorole humans add

**Description:** Add a role to be added to all new humans on join.

**Usage:** `<@1275521742961508432>autorole humans add`

### autorole humans remove

**Description:** Remove an autorole for humans.

**Usage:** `<@1275521742961508432>autorole humans remove`

### autorole add

**Description:** Add a role to be added to all new members on join.

**Usage:** `<@1275521742961508432>autorole add`

### autorole toggle

**Description:** Toggle the auto role system.

**Usage:** `<@1275521742961508432>autorole toggle`

### autorole sticky

**Description:** No description provided.

**Usage:** `<@1275521742961508432>autorole sticky`

### autorole sticky set

**Description:** No description provided.

**Usage:** `<@1275521742961508432>autorole sticky set`

### autorole sticky add

**Description:** No description provided.

**Usage:** `<@1275521742961508432>autorole sticky add`

### autorole sticky remove

**Description:** No description provided.

**Usage:** `<@1275521742961508432>autorole sticky remove`

### autorole remove

**Description:** Remove an autorole.

**Usage:** `<@1275521742961508432>autorole remove`

### role

**Description:** Base command for modifying roles.

Invoking this command will add or remove the given role from the member, depending on whether they already had it.

**Usage:** `<@1275521742961508432>role`

### role color

**Description:** Change a role's color.

**Usage:** `<@1275521742961508432>role color`

### role info

**Description:** Get information about a role.

**Usage:** `<@1275521742961508432>role info`

### role target

**Description:** Modify roles using 'targeting' args.

An explanation of Targeter and test commands to preview the members affected can be found with `[p]target`.

**Usage:** `<@1275521742961508432>role target`

### role target remove

**Description:** Remove a role from members using targeting args.

An explanation of Targeter and test commands to preview the members affected can be found with `[p]target`.

**Usage:** `<@1275521742961508432>role target remove`

### role target add

**Description:** Add a role to members using targeting args.

An explanation of Targeter and test commands to preview the members affected can be found with `[p]target`.

**Usage:** `<@1275521742961508432>role target add`

### role bots

**Description:** Add a role to all bots in the server.

**Usage:** `<@1275521742961508432>role bots`

### role addmulti

**Description:** Add a role to multiple members.

**Usage:** `<@1275521742961508432>role addmulti`

### role uniquemembers

**Description:** View the total unique members between multiple roles.

**Usage:** `<@1275521742961508432>role uniquemembers`

### role hoist

**Description:** Toggle whether a role should appear seperate from other roles.

**Usage:** `<@1275521742961508432>role hoist`

### role create

**Description:** Creates a role.

Color and whether it is hoisted can be specified.

**Usage:** `<@1275521742961508432>role create`

### role members

**Description:** Sends a list of members in a role.

You can supply a custom formatting tagscript for each member.
The [member](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block) block is available to use, found on the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/index.html).

**Example:**
`[p]role dump @admin <t:{member(timestamp)}> - {member(mention)}`

**Usage:** `<@1275521742961508432>role members`

### role rbots

**Description:** Remove a role from all bots in the server.

**Usage:** `<@1275521742961508432>role rbots`

### role custom

**Description:** Add/Remove roles to one or more users

You cannot add and remove the same Role

**Example:**
- `[p]role custom inthedark.org --add role1 --remove role2`
- `[p] role custom inthedark.org --add role1 "role to remove"`

**Usage:** `<@1275521742961508432>role custom`

### role removemulti

**Description:** Remove a role from multiple members.

**Usage:** `<@1275521742961508432>role removemulti`

### role rall

**Description:** Remove a role from all members of the server.

**Usage:** `<@1275521742961508432>role rall`

### role colors

**Description:** Sends the server's roles, ordered by color.

**Usage:** `<@1275521742961508432>role colors`

### role in

**Description:** Add a role to all members of a another role.

**Usage:** `<@1275521742961508432>role in`

### role add

**Description:** Add a role to a member.

**Usage:** `<@1275521742961508432>role add`

### role humans

**Description:** Add a role to all humans (non-bots) in the server.

**Usage:** `<@1275521742961508432>role humans`

### role rin

**Description:** Remove a role from all members of a another role.

**Usage:** `<@1275521742961508432>role rin`

### role rhumans

**Description:** Remove a role from all humans (non-bots) in the server.

**Usage:** `<@1275521742961508432>role rhumans`

### role all

**Description:** Add a role to all members of the server.

**Usage:** `<@1275521742961508432>role all`

### role remove

**Description:** Remove a role from a member.

**Usage:** `<@1275521742961508432>role remove`

### role name

**Description:** Change a role's name.

**Usage:** `<@1275521742961508432>role name`

### multirole

**Description:** Add multiple roles to a member.

**Usage:** `<@1275521742961508432>multirole`

### multirole remove

**Description:** Remove multiple roles from a member.

**Usage:** `<@1275521742961508432>multirole remove`

