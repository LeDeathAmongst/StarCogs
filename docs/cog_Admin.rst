Admin
=====

A collection of server administration utilities.

<<<<<<< HEAD
# <@1275521742961508432>addrole
=======
# ,addrole
>>>>>>> 9e308722 (Revamped and Fixed)
Add a role to a user.<br/>

Use double quotes if the role contains spaces.<br/>
If user is left blank it defaults to the author of the command.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>addrole <rolename> [user]`
=======
 - Usage: `,addrole <rolename> [user]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### rolename: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### user: discord.member.Member = operator.attrgetter('author')
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


<<<<<<< HEAD
# <@1275521742961508432>removerole
=======
# ,removerole
>>>>>>> 9e308722 (Revamped and Fixed)
Remove a role from a user.<br/>

Use double quotes if the role contains spaces.<br/>
If user is left blank it defaults to the author of the command.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>removerole <rolename> [user]`
=======
 - Usage: `,removerole <rolename> [user]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### rolename: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### user: discord.member.Member = operator.attrgetter('author')
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


<<<<<<< HEAD
# <@1275521742961508432>editrole
Edit role settings.<br/>
 - Usage: `<@1275521742961508432>editrole`
=======
# ,editrole
Edit role settings.<br/>
 - Usage: `,editrole`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>editrole colour
=======
## ,editrole name
Edit a role's name.<br/>

Use double quotes if the role or the name contain spaces.<br/>

Example:<br/>
    `,editrole name "The Transistor" Test`<br/>
 - Usage: `,editrole name <role> <name>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,editrole colour
>>>>>>> 9e308722 (Revamped and Fixed)
Edit a role's colour.<br/>

Use double quotes if the role contains spaces.<br/>
Colour must be in hexadecimal format.<br/>
[Online colour picker](http://www.w3schools.com/colors/colors_picker.asp)<br/>

Examples:<br/>
<<<<<<< HEAD
    `<@1275521742961508432>editrole colour "The Transistor" #ff0000`<br/>
    `<@1275521742961508432>editrole colour Test #ff9900`<br/>
 - Usage: `<@1275521742961508432>editrole colour <role> <value>`
=======
    `,editrole colour "The Transistor" #ff0000`<br/>
    `,editrole colour Test #ff9900`<br/>
 - Usage: `,editrole colour <role> <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `color`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### value: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>editrole name
Edit a role's name.<br/>

Use double quotes if the role or the name contain spaces.<br/>

Example:<br/>
    `<@1275521742961508432>editrole name "The Transistor" Test`<br/>
 - Usage: `<@1275521742961508432>editrole name <role> <name>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>announce
Announce a message to all servers the bot is in.<br/>
 - Usage: `<@1275521742961508432>announce <message>`
=======
# ,announce
Announce a message to all servers the bot is in.<br/>
 - Usage: `,announce <message>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>announce cancel
Cancel a running announce.<br/>
 - Usage: `<@1275521742961508432>announce cancel`


# <@1275521742961508432>announceset
Change how announcements are sent in this server.<br/>
 - Usage: `<@1275521742961508432>announceset`
=======
## ,announce cancel
Cancel a running announce.<br/>
 - Usage: `,announce cancel`


# ,announceset
Change how announcements are sent in this server.<br/>
 - Usage: `,announceset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>announceset clearchannel
Unsets the channel for announcements.<br/>
 - Usage: `<@1275521742961508432>announceset clearchannel`


## <@1275521742961508432>announceset channel
Change the channel where the bot will send announcements.<br/>
 - Usage: `<@1275521742961508432>announceset channel <channel>`
=======
## ,announceset channel
Change the channel where the bot will send announcements.<br/>
 - Usage: `,announceset channel <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>selfrole
=======
## ,announceset clearchannel
Unsets the channel for announcements.<br/>
 - Usage: `,announceset clearchannel`


# ,selfrole
>>>>>>> 9e308722 (Revamped and Fixed)
Add or remove a selfrole from yourself.<br/>

Server admins must have configured the role as user settable.<br/>
NOTE: The role is case sensitive!<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>selfrole <selfrole>`
 - Checks: `server_only`


## <@1275521742961508432>selfrole remove
Remove a selfrole from yourself.<br/>

Server admins must have configured the role as user settable.<br/>
NOTE: The role is case sensitive!<br/>
 - Usage: `<@1275521742961508432>selfrole remove <selfrole>`


## <@1275521742961508432>selfrole list
Lists all available selfroles.<br/>
 - Usage: `<@1275521742961508432>selfrole list`


## <@1275521742961508432>selfrole add
=======
 - Usage: `,selfrole <selfrole>`
 - Checks: `server_only`


## ,selfrole add
>>>>>>> 9e308722 (Revamped and Fixed)
Add a selfrole to yourself.<br/>

Server admins must have configured the role as user settable.<br/>
NOTE: The role is case sensitive!<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>selfrole add <selfrole>`


# <@1275521742961508432>selfroleset
Manage selfroles.<br/>
 - Usage: `<@1275521742961508432>selfroleset`
 - Restricted to: `ADMIN`


## <@1275521742961508432>selfroleset clear
Clear the list of available selfroles for this server.<br/>
 - Usage: `<@1275521742961508432>selfroleset clear`


## <@1275521742961508432>selfroleset add
Add a role, or a selection of roles, to the list of available selfroles.<br/>

NOTE: The role is case sensitive!<br/>
 - Usage: `<@1275521742961508432>selfroleset add <roles>`
=======
 - Usage: `,selfrole add <selfrole>`


## ,selfrole remove
Remove a selfrole from yourself.<br/>

Server admins must have configured the role as user settable.<br/>
NOTE: The role is case sensitive!<br/>
 - Usage: `,selfrole remove <selfrole>`


## ,selfrole list
Lists all available selfroles.<br/>
 - Usage: `,selfrole list`


# ,selfroleset
Manage selfroles.<br/>
 - Usage: `,selfroleset`
 - Restricted to: `ADMIN`


## ,selfroleset add
Add a role, or a selection of roles, to the list of available selfroles.<br/>

NOTE: The role is case sensitive!<br/>
 - Usage: `,selfroleset add <roles>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>selfroleset remove
Remove a role, or a selection of roles, from the list of available selfroles.<br/>

NOTE: The role is case sensitive!<br/>
 - Usage: `<@1275521742961508432>selfroleset remove <roles>`


# <@1275521742961508432>serverlock
Lock a bot to its current servers only.<br/>
 - Usage: `<@1275521742961508432>serverlock`
=======
## ,selfroleset clear
Clear the list of available selfroles for this server.<br/>
 - Usage: `,selfroleset clear`


## ,selfroleset remove
Remove a role, or a selection of roles, from the list of available selfroles.<br/>

NOTE: The role is case sensitive!<br/>
 - Usage: `,selfroleset remove <roles>`


# ,serverlock
Lock a bot to its current servers only.<br/>
 - Usage: `,serverlock`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`


