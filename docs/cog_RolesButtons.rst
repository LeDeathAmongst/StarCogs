RolesButtons
============

A cog to have roles-buttons!

<<<<<<< HEAD
# <@1275521742961508432>rolesbuttons (Hybrid Command)
Group of commands to use RolesButtons.<br/>
 - Usage: `<@1275521742961508432>rolesbuttons`
=======
# ,rolesbuttons (Hybrid Command)
Group of commands to use RolesButtons.<br/>
 - Usage: `,rolesbuttons`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/rolesbuttons`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>rolesbuttons bulk (Hybrid Command)
Add roles-buttons for a message.<br/>

```<@1275521742961508432>rolesbuttons bulk <message> :reaction1:|@role1 :reaction2:|@role2 :reaction3:|@role3```
 - Usage: `<@1275521742961508432>rolesbuttons bulk <message> <roles_buttons>`
 - Slash Usage: `/rolesbuttons bulk <message> <roles_buttons>`
 - Checks: `server_only`


## <@1275521742961508432>rolesbuttons remove (Hybrid Command)
Remove a role-button for a message.<br/>

Use `<@1275521742961508432>rolesbuttons list <message>` to find the config identifier.<br/>
 - Usage: `<@1275521742961508432>rolesbuttons remove <message> <config_identifier>`
 - Slash Usage: `/rolesbuttons remove <message> <config_identifier>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### config_identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>rolesbuttons purge (Hybrid Command)
Clear all roles-buttons for a server.<br/>
 - Usage: `<@1275521742961508432>rolesbuttons purge`
 - Slash Usage: `/rolesbuttons purge`
 - Checks: `server_only`


## <@1275521742961508432>rolesbuttons mode (Hybrid Command)
=======
## ,rolesbuttons mode (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Choose a mode for the roles-buttons of a message.<br/>

Mode `add_or_remove`:<br/>
- Users get the role if they do not already have it, or lose it.<br/>
Mode `add_only`:<br/>
- Users can only get the role, but only manual action will remove it.<br/>
Mode `remove_only`:<br/>
- Users can only lose a role, and will not be able to get it again without a manual action.<br/>
Mode `replace`:<br/>
- Same as `add_or_remove`, but the roles from this message will be mutually exclusive, and getting one will remove the previous.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>rolesbuttons mode <message> <mode>`
=======
 - Usage: `,rolesbuttons mode <message> <mode>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/rolesbuttons mode <message> <mode>`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>rolesbuttons add (Hybrid Command)
=======
## ,rolesbuttons list (Hybrid Command)
List all roles-buttons of this server or display the settings for a specific one.<br/>
 - Usage: `,rolesbuttons list [message=None]`
 - Slash Usage: `/rolesbuttons list [message=None]`
 - Checks: `server_only`


## ,rolesbuttons purge (Hybrid Command)
Clear all roles-buttons for a server.<br/>
 - Usage: `,rolesbuttons purge`
 - Slash Usage: `/rolesbuttons purge`
 - Checks: `server_only`


## ,rolesbuttons bulk (Hybrid Command)
Add roles-buttons for a message.<br/>

```,rolesbuttons bulk <message> :reaction1:|@role1 :reaction2:|@role2 :reaction3:|@role3```
 - Usage: `,rolesbuttons bulk <message> <roles_buttons>`
 - Slash Usage: `/rolesbuttons bulk <message> <roles_buttons>`
 - Checks: `server_only`


## ,rolesbuttons clear (Hybrid Command)
Clear all roles-buttons for a message.<br/>
 - Usage: `,rolesbuttons clear <message>`
 - Slash Usage: `/rolesbuttons clear <message>`
 - Checks: `server_only`


## ,rolesbuttons remove (Hybrid Command)
Remove a role-button for a message.<br/>

Use `,rolesbuttons list <message>` to find the config identifier.<br/>
 - Usage: `,rolesbuttons remove <message> <config_identifier>`
 - Slash Usage: `/rolesbuttons remove <message> <config_identifier>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### config_identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,rolesbuttons add (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Add a role-button for a message.<br/>

(Use the number for the color.)<br/>
• `primary`: 1<br/>
• `secondary`: 2<br/>
• `success`: 3<br/>
• `danger`: 4<br/>
# Aliases<br/>
• `blurple`: 1<br/>
• `grey`: 2<br/>
• `gray`: 2<br/>
• `green`: 3<br/>
• `red`: 4<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>rolesbuttons add <message> <role> <emoji> [style_button=2] [text_button]`
=======
 - Usage: `,rolesbuttons add <message> <role> <emoji> [style_button=2] [text_button]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/rolesbuttons add <message> <role> <emoji> [style_button=2] [text_button]`
 - Aliases: `+`
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


<<<<<<< HEAD
## <@1275521742961508432>rolesbuttons clear (Hybrid Command)
Clear all roles-buttons for a message.<br/>
 - Usage: `<@1275521742961508432>rolesbuttons clear <message>`
 - Slash Usage: `/rolesbuttons clear <message>`
 - Checks: `server_only`


## <@1275521742961508432>rolesbuttons list (Hybrid Command)
List all roles-buttons of this server or display the settings for a specific one.<br/>
 - Usage: `<@1275521742961508432>rolesbuttons list [message=None]`
 - Slash Usage: `/rolesbuttons list [message=None]`
 - Checks: `server_only`


=======
>>>>>>> 9e308722 (Revamped and Fixed)
