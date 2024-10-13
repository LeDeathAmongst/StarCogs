TicketTool
==========

A cog to manage a Tickets system!

# ,settickettool (Hybrid Command)
Configure TicketTool for your server.<br/>
 - Usage: `,settickettool`
 - Slash Usage: `/settickettool`
 - Restricted to: `ADMIN`
 - Aliases: `tickettoolset`
 - Checks: `server_only`


## ,settickettool ticketrole (Hybrid Command)
This role will be added automatically to open tickets owners.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.role.Role'>`<br/>
 - Usage: `,settickettool ticketrole <profile> <value>`
 - Slash Usage: `/settickettool ticketrole <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## ,settickettool forumchannel (Hybrid Command)
Set the forum channel where the opened tickets will be, or a text channel to use private threads. If it's set, `category_open` and `category_close` will be ignored (except for existing tickets).<br/>

Default value: `None`<br/>
Dev: `typing.Union[discord.channel.ForumChannel, discord.channel.TextChannel]`<br/>
 - Usage: `,settickettool forumchannel <profile> <value>`
 - Slash Usage: `/settickettool forumchannel <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: Union[discord.channel.ForumChannel, discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,settickettool custommessage (Hybrid Command)
This message will be sent in the ticket channel when the ticket is opened.<br/>

`{ticket_id}` - Ticket number<br/>
`{owner_display_name}` - user's nick or name<br/>
`{owner_name}` - user's name<br/>
`{owner_id}` - user's id<br/>
`{server_name}` - server's name<br/>
`{server_id}` - server's id<br/>
`{bot_display_name}` - bot's nick or name<br/>
`{bot_name}` - bot's name<br/>
`{bot_id}` - bot's id<br/>
`{shortdate}` - mm-dd<br/>
`{longdate}` - mm-dd-yyyy<br/>
`{time}` - hh-mm AM/PM according to bot host system time<br/>
`{emoji}` - The open/closed emoji.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,settickettool custommessage <profile> <value>`
 - Slash Usage: `/settickettool custommessage <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,settickettool deleteonclose (Hybrid Command)
Does closing the ticket directly delete it (with confirmation)?<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool deleteonclose <profile> <value>`
 - Slash Usage: `/settickettool deleteonclose <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool profileslist (Hybrid Command)
List the existing profiles.<br/>
 - Usage: `,settickettool profileslist`
 - Slash Usage: `/settickettool profileslist`
 - Aliases: `listprofiles`
 - Checks: `server_only`


## ,settickettool usercanclose (Hybrid Command)
Can the author of the ticket, if he/she does not have a role set up for the system, close the ticket himself?<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool usercanclose <profile> <value>`
 - Slash Usage: `/settickettool usercanclose <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool closeonleave (Hybrid Command)
If a user leaves the server, will all their open tickets be closed?<br/>

If the user then returns to the server, even if their ticket is still open, the bot will not automatically add them to the ticket.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool closeonleave <profile> <value>`
 - Slash Usage: `/settickettool closeonleave <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool categoryopen (Hybrid Command)
Set the category where the opened tickets will be.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.CategoryChannel'>`<br/>
 - Usage: `,settickettool categoryopen <profile> <value>`
 - Slash Usage: `/settickettool categoryopen <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,settickettool showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,settickettool showsettings <profile> [with_dev=False]`
 - Slash Usage: `/settickettool showsettings <profile> [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool enable (Hybrid Command)
Enable the system.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool enable <profile> <value>`
 - Slash Usage: `/settickettool enable <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool dynamicchannelname (Hybrid Command)
Set the template that will be used to name the channel when creating a ticket.<br/>

`{ticket_id}` - Ticket number<br/>
`{owner_display_name}` - user's nick or name<br/>
`{owner_name}` - user's name<br/>
`{owner_id}` - user's id<br/>
`{server_name}` - server's name<br/>
`{server_id}` - server's id<br/>
`{bot_display_name}` - bot's nick or name<br/>
`{bot_name}` - bot's name<br/>
`{bot_id}` - bot's id<br/>
`{shortdate}` - mm-dd<br/>
`{longdate}` - mm-dd-yyyy<br/>
`{time}` - hh-mm AM/PM according to bot host system time<br/>
`{emoji}` - The open/closed emoji.<br/>

Default value: `{emoji}-ticket-{ticket_id}`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,settickettool dynamicchannelname <profile> <value>`
 - Slash Usage: `/settickettool dynamicchannelname <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,settickettool logschannel (Hybrid Command)
Set the channel where the logs will be sent/saved.<br/>

Default value: `None`<br/>
Dev: `typing.Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]`<br/>
 - Usage: `,settickettool logschannel <profile> <value>`
 - Slash Usage: `/settickettool logschannel <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,settickettool resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,settickettool resetsetting <profile> <setting>`
 - Slash Usage: `/settickettool resetsetting <profile> <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,settickettool categoryclose (Hybrid Command)
Set the category where the closed tickets will be.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.CategoryChannel'>`<br/>
 - Usage: `,settickettool categoryclose <profile> <value>`
 - Slash Usage: `/settickettool categoryclose <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,settickettool auditlogs (Hybrid Command)
On all requests to the Discord api regarding the ticket (channel modification), does the bot send the name and id of the user who requested the action as the reason?<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool auditlogs <profile> <value>`
 - Slash Usage: `/settickettool auditlogs <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool adminroles (Hybrid Command)
Users with this role will have full permissions for tickets, but will not be able to set up the cog.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Role]`<br/>
 - Usage: `,settickettool adminroles <profile> <value>`
 - Slash Usage: `/settickettool adminroles <profile> <value>`
 - Checks: `server_only`


## ,settickettool supportroles (Hybrid Command)
Users with this role will be able to participate and claim the ticket.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Role]`<br/>
 - Usage: `,settickettool supportroles <profile> <value>`
 - Slash Usage: `/settickettool supportroles <profile> <value>`
 - Checks: `server_only`


## ,settickettool renamechanneldropdown (Hybrid Command)
With Dropdowns feature, rename the ticket channel with chosen reason.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool renamechanneldropdown <profile> <value>`
 - Slash Usage: `/settickettool renamechanneldropdown <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool viewroles (Hybrid Command)
Users with this role will only be able to read messages from the ticket, but not send them.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Role]`<br/>
 - Usage: `,settickettool viewroles <profile> <value>`
 - Slash Usage: `/settickettool viewroles <profile> <value>`
 - Checks: `server_only`


## ,settickettool message (Hybrid Command)
Send a message with a button to open a ticket or dropdown with possible reasons.<br/>

Examples:<br/>
- `,settickettool message <profile> #general "🐛|Report a bug|If you find a bug, report it here.|bug" "⚠️|Report a user|If you find a malicious user, report it here.|user"`<br/>
- `,settickettool <profile> 1234567890-0987654321`<br/>
 - Usage: `,settickettool message <profile> <channel> <message> <reason_options> [emoji=🎟️] [label=None]`
 - Slash Usage: `/settickettool message <profile> <channel> <message> <reason_options> [emoji=🎟️] [label=None]`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,settickettool modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,settickettool modalconfig <profile> [confirmation=False]`
 - Slash Usage: `/settickettool modalconfig <profile> [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool nbmax (Hybrid Command)
Sets the maximum number of open tickets a user can have on the system at any one time (for a profile only).<br/>

Default value: `5`<br/>
Dev: `Range[int, 1, None]`<br/>
 - Usage: `,settickettool nbmax <profile> <value>`
 - Slash Usage: `/settickettool nbmax <profile> <value>`
 - Checks: `server_only`


## ,settickettool createonreact (Hybrid Command)
Create a ticket when the reaction 🎟️ is set on any message on the server.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool createonreact <profile> <value>`
 - Slash Usage: `/settickettool createonreact <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool pingroles (Hybrid Command)
This role will be pinged automatically when the ticket is created, but does not give any additional permissions.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Role]`<br/>
 - Usage: `,settickettool pingroles <profile> <value>`
 - Slash Usage: `/settickettool pingroles <profile> <value>`
 - Checks: `server_only`


## ,settickettool profileadd (Hybrid Command)
Create a new profile with defaults settings.<br/>
 - Usage: `,settickettool profileadd <profile>`
 - Slash Usage: `/settickettool profileadd <profile>`
 - Aliases: `addprofile`
 - Checks: `server_only`
Extended Arg Info
> ### profile: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,settickettool profileremove (Hybrid Command)
Remove an existing profile.<br/>
 - Usage: `,settickettool profileremove <profile> [confirmation=False]`
 - Slash Usage: `/settickettool profileremove <profile> [confirmation=False]`
 - Aliases: `removeprofile`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool closeconfirmation (Hybrid Command)
Should the bot ask for confirmation before closing the ticket (deletion will necessarily have a confirmation)?<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool closeconfirmation <profile> <value>`
 - Slash Usage: `/settickettool closeconfirmation <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool modlog (Hybrid Command)
Does the bot create an action in the bot modlog when a ticket is created?<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,settickettool modlog <profile> <value>`
 - Slash Usage: `/settickettool modlog <profile> <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,settickettool profileclone (Hybrid Command)
Clone an existing profile with his settings.<br/>
 - Usage: `,settickettool profileclone <old_profile> <profile>`
 - Slash Usage: `/settickettool profileclone <old_profile> <profile>`
 - Aliases: `cloneprofile`
 - Checks: `server_only`
Extended Arg Info
> ### profile: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,settickettool custommodal (Hybrid Command)
Ask a maximum of 5 questions to the user who opens a ticket, with a Discord Modal.<br/>

**Example:**<br/>
```
,settickettool customodal <profile>
- label: What is the problem?
  style: 2 #  short = 1, paragraph = 2
  required: True
  default: None
  placeholder: None
  min_length: None
  max_length: None
```

Default value: `None`<br/>
Dev: `<class 'tickettool.utils.CustomModalConverter'>`<br/>
 - Usage: `,settickettool custommodal <profile> <value>`
 - Slash Usage: `/settickettool custommodal <profile> <value>`
 - Checks: `server_only`


## ,settickettool profilerename (Hybrid Command)
Rename an existing profile.<br/>
 - Usage: `,settickettool profilerename <old_profile> <profile>`
 - Slash Usage: `/settickettool profilerename <old_profile> <profile>`
 - Aliases: `renameprofile`
 - Checks: `server_only`
Extended Arg Info
> ### profile: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,ticket (Hybrid Command)
Commands for using the Tickets system.<br/>

Many commands to manage tickets appear when you run help in a ticket channel.<br/>
 - Usage: `,ticket`
 - Slash Usage: `/ticket`
 - Checks: `server_only`


## ,ticket create (Hybrid Command)
Create a Ticket.<br/>

If only one profile has been created on this server, you don't need to specify its name.<br/>
 - Usage: `,ticket create [profile=None] [reason]`
 - Slash Usage: `/ticket create [profile=None] [reason]`
 - Aliases: `+`
 - Checks: `server_only`
Extended Arg Info
> ### reason: str = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket export (Hybrid Command)
Export all the messages of an existing Ticket in html format.<br/>
Please note: all attachments and user avatars are saved with the Discord link in this file.<br/>
 - Usage: `,ticket export`
 - Slash Usage: `/ticket export`
 - Checks: `TicketTool and server_only`


## ,ticket owner (Hybrid Command)
Change the owner of an existing Ticket.<br/>
 - Usage: `,ticket owner <new_owner> [reason]`
 - Slash Usage: `/ticket owner <new_owner> [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### new_owner: discord.member.Member
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
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket unclaim (Hybrid Command)
Unclaim an existing Ticket.<br/>
 - Usage: `,ticket unclaim [reason]`
 - Slash Usage: `/ticket unclaim [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket removemember (Hybrid Command)
Remove a member to an existing Ticket.<br/>
 - Usage: `,ticket removemember <members>`
 - Slash Usage: `/ticket removemember <members>`
 - Aliases: `remove`
 - Checks: `TicketTool and server_only`


## ,ticket addmember (Hybrid Command)
Add a member to an existing Ticket.<br/>
 - Usage: `,ticket addmember <members>`
 - Slash Usage: `/ticket addmember <members>`
 - Aliases: `add`
 - Checks: `TicketTool and server_only`


## ,ticket open (Hybrid Command)
Open an existing Ticket.<br/>
 - Usage: `,ticket open [reason]`
 - Slash Usage: `/ticket open [reason]`
 - Aliases: `reopen`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket unlock (Hybrid Command)
Unlock an existing locked Ticket.<br/>
 - Usage: `,ticket unlock [reason]`
 - Slash Usage: `/ticket unlock [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket createfor (Hybrid Command)
Create a Ticket for a member.<br/>

If only one profile has been created on this server, you don't need to specify its name.<br/>
 - Usage: `,ticket createfor <profile> <member> [reason]`
 - Slash Usage: `/ticket createfor <profile> <member> [reason]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
> ### reason: str = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket lock (Hybrid Command)
Lock an existing Ticket.<br/>
 - Usage: `,ticket lock [confirmation=None] [reason]`
 - Slash Usage: `/ticket lock [confirmation=None] [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket delete (Hybrid Command)
Delete an existing Ticket.<br/>

If a logs channel is defined, an html file containing all the messages of this ticket will be generated.<br/>
(Attachments are not supported, as they are saved with their Discord link)<br/>
 - Usage: `,ticket delete [confirmation=False] [reason]`
 - Slash Usage: `/ticket delete [confirmation=False] [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket rename (Hybrid Command)
Rename an existing Ticket.<br/>
 - Usage: `,ticket rename <new_name> [reason]`
 - Slash Usage: `/ticket rename <new_name> [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### new_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket list (Hybrid Command)
List the existing Tickets for a profile. You can provide a status and/or a ticket owner.<br/>
 - Usage: `,ticket list <profile> <status> <owner>`
 - Slash Usage: `/ticket list <profile> <status> <owner>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### owner: Optional[discord.member.Member]
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


## ,ticket claim (Hybrid Command)
Claim an existing Ticket.<br/>
 - Usage: `,ticket claim [member=None] [reason]`
 - Slash Usage: `/ticket claim [member=None] [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### member: Optional[discord.member.Member] = None
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
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,ticket close (Hybrid Command)
Close an existing Ticket.<br/>
 - Usage: `,ticket close [confirmation=None] [reason]`
 - Slash Usage: `/ticket close [confirmation=None] [reason]`
 - Checks: `TicketTool and server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: Optional[str] = 'No reason provided.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


