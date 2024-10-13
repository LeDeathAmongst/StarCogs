Admin
=====

A collection of server administration utilities.

# ,addrole
Add a role to a user.<br/>

Use double quotes if the role contains spaces.<br/>
If user is left blank it defaults to the author of the command.<br/>
 - Usage: `,addrole <rolename> [user]`
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


# ,removerole
Remove a role from a user.<br/>

Use double quotes if the role contains spaces.<br/>
If user is left blank it defaults to the author of the command.<br/>
 - Usage: `,removerole <rolename> [user]`
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


# ,editrole
Edit role settings.<br/>
 - Usage: `,editrole`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


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
Edit a role's colour.<br/>

Use double quotes if the role contains spaces.<br/>
Colour must be in hexadecimal format.<br/>
[Online colour picker](http://www.w3schools.com/colors/colors_picker.asp)<br/>

Examples:<br/>
    `,editrole colour "The Transistor" #ff0000`<br/>
    `,editrole colour Test #ff9900`<br/>
 - Usage: `,editrole colour <role> <value>`
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


# ,announce
Announce a message to all servers the bot is in.<br/>
 - Usage: `,announce <message>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,announce cancel
Cancel a running announce.<br/>
 - Usage: `,announce cancel`


# ,announceset
Change how announcements are sent in this server.<br/>
 - Usage: `,announceset`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


## ,announceset channel
Change the channel where the bot will send announcements.<br/>
 - Usage: `,announceset channel <channel>`
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


## ,announceset clearchannel
Unsets the channel for announcements.<br/>
 - Usage: `,announceset clearchannel`


# ,selfrole
Add or remove a selfrole from yourself.<br/>

Server admins must have configured the role as user settable.<br/>
NOTE: The role is case sensitive!<br/>
 - Usage: `,selfrole <selfrole>`
 - Checks: `server_only`


## ,selfrole add
Add a selfrole to yourself.<br/>

Server admins must have configured the role as user settable.<br/>
NOTE: The role is case sensitive!<br/>
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
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


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
 - Restricted to: `BOT_OWNER`


