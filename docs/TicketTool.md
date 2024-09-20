# TicketTool Help

### settickettool

**Description:** Configure TicketTool for your server.

**Usage:** `<@1275521742961508432>settickettool`

### settickettool forumchannel

**Description:** Set the forum channel where the opened tickets will be, or a text channel to use private threads. If it's set, `category_open` and `category_close` will be ignored (except for existing tickets).

Default value: `None`
Dev: `typing.Union[discord.channel.ForumChannel, discord.channel.TextChannel]`

**Usage:** `<@1275521742961508432>settickettool forumchannel`

### settickettool profilerename

**Description:** Rename an existing profile.

**Usage:** `<@1275521742961508432>settickettool profilerename`

### settickettool categoryopen

**Description:** Set the category where the opened tickets will be.

Default value: `None`
Dev: `<class 'discord.channel.CategoryChannel'>`

**Usage:** `<@1275521742961508432>settickettool categoryopen`

### settickettool modlog

**Description:** Does the bot create an action in the bot modlog when a ticket is created?

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool modlog`

### settickettool logschannel

**Description:** Set the channel where the logs will be sent/saved.

Default value: `None`
Dev: `typing.Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]`

**Usage:** `<@1275521742961508432>settickettool logschannel`

### settickettool profileadd

**Description:** Create a new profile with defaults settings.

**Usage:** `<@1275521742961508432>settickettool profileadd`

### settickettool supportroles

**Description:** Users with this role will be able to participate and claim the ticket.

Default value: `[]`
Dev: `Greedy[Role]`

**Usage:** `<@1275521742961508432>settickettool supportroles`

### settickettool profileclone

**Description:** Clone an existing profile with his settings.

**Usage:** `<@1275521742961508432>settickettool profileclone`

### settickettool adminroles

**Description:** Users with this role will have full permissions for tickets, but will not be able to set up the cog.

Default value: `[]`
Dev: `Greedy[Role]`

**Usage:** `<@1275521742961508432>settickettool adminroles`

### settickettool viewroles

**Description:** Users with this role will only be able to read messages from the ticket, but not send them.

Default value: `[]`
Dev: `Greedy[Role]`

**Usage:** `<@1275521742961508432>settickettool viewroles`

### settickettool profileslist

**Description:** List the existing profiles.

**Usage:** `<@1275521742961508432>settickettool profileslist`

### settickettool ticketrole

**Description:** This role will be added automatically to open tickets owners.

Default value: `None`
Dev: `<class 'discord.role.Role'>`

**Usage:** `<@1275521742961508432>settickettool ticketrole`

### settickettool showsettings

**Description:** Show all settings for the cog with defaults and values.

**Usage:** `<@1275521742961508432>settickettool showsettings`

### settickettool profileremove

**Description:** Remove an existing profile.

**Usage:** `<@1275521742961508432>settickettool profileremove`

### settickettool categoryclose

**Description:** Set the category where the closed tickets will be.

Default value: `None`
Dev: `<class 'discord.channel.CategoryChannel'>`

**Usage:** `<@1275521742961508432>settickettool categoryclose`

### settickettool modalconfig

**Description:** Set all settings for the cog with a Discord Modal.

**Usage:** `<@1275521742961508432>settickettool modalconfig`

### settickettool custommessage

**Description:** This message will be sent in the ticket channel when the ticket is opened.

`{ticket_id}` - Ticket number
`{owner_display_name}` - user's nick or name
`{owner_name}` - user's name
`{owner_id}` - user's id
`{guild_name}` - guild's name
`{guild_id}` - guild's id
`{bot_display_name}` - bot's nick or name
`{bot_name}` - bot's name
`{bot_id}` - bot's id
`{shortdate}` - mm-dd
`{longdate}` - mm-dd-yyyy
`{time}` - hh-mm AM/PM according to bot host system time
`{emoji}` - The open/closed emoji.

Default value: `None`
Dev: `<class 'str'>`

**Usage:** `<@1275521742961508432>settickettool custommessage`

### settickettool custommodal

**Description:** Ask a maximum of 5 questions to the user who opens a ticket, with a Discord Modal.

**Example:**
```
[p]settickettool customodal <profile>
- label: What is the problem?
  style: 2 #  short = 1, paragraph = 2
  required: True
  default: None
  placeholder: None
  min_length: None
  max_length: None
```

Default value: `None`
Dev: `<class 'tickettool.utils.CustomModalConverter'>`

**Usage:** `<@1275521742961508432>settickettool custommodal`

### settickettool pingroles

**Description:** This role will be pinged automatically when the ticket is created, but does not give any additional permissions.

Default value: `[]`
Dev: `Greedy[Role]`

**Usage:** `<@1275521742961508432>settickettool pingroles`

### settickettool deleteonclose

**Description:** Does closing the ticket directly delete it (with confirmation)?

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool deleteonclose`

### settickettool renamechanneldropdown

**Description:** With Dropdowns feature, rename the ticket channel with chosen reason.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool renamechanneldropdown`

### settickettool message

**Description:** Send a message with a button to open a ticket or dropdown with possible reasons.

Examples:
- `[p]settickettool message <profile> #general "🐛|Report a bug|If you find a bug, report it here.|bug" "⚠️|Report a user|If you find a malicious user, report it here.|user"`
- `[p]settickettool <profile> 1234567890-0987654321`

**Usage:** `<@1275521742961508432>settickettool message`

### settickettool enable

**Description:** Enable the system.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool enable`

### settickettool dynamicchannelname

**Description:** Set the template that will be used to name the channel when creating a ticket.

`{ticket_id}` - Ticket number
`{owner_display_name}` - user's nick or name
`{owner_name}` - user's name
`{owner_id}` - user's id
`{guild_name}` - guild's name
`{guild_id}` - guild's id
`{bot_display_name}` - bot's nick or name
`{bot_name}` - bot's name
`{bot_id}` - bot's id
`{shortdate}` - mm-dd
`{longdate}` - mm-dd-yyyy
`{time}` - hh-mm AM/PM according to bot host system time
`{emoji}` - The open/closed emoji.

Default value: `{emoji}-ticket-{ticket_id}`
Dev: `<class 'str'>`

**Usage:** `<@1275521742961508432>settickettool dynamicchannelname`

### settickettool nbmax

**Description:** Sets the maximum number of open tickets a user can have on the system at any one time (for a profile only).

Default value: `5`
Dev: `Range[int, 1, None]`

**Usage:** `<@1275521742961508432>settickettool nbmax`

### settickettool usercanclose

**Description:** Can the author of the ticket, if he/she does not have a role set up for the system, close the ticket himself?

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool usercanclose`

### settickettool closeconfirmation

**Description:** Should the bot ask for confirmation before closing the ticket (deletion will necessarily have a confirmation)?

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool closeconfirmation`

### settickettool auditlogs

**Description:** On all requests to the Discord api regarding the ticket (channel modification), does the bot send the name and id of the user who requested the action as the reason?

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool auditlogs`

### settickettool resetsetting

**Description:** Reset a setting.

**Usage:** `<@1275521742961508432>settickettool resetsetting`

### settickettool createonreact

**Description:** Create a ticket when the reaction 🎟️ is set on any message on the server.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool createonreact`

### settickettool closeonleave

**Description:** If a user leaves the server, will all their open tickets be closed?

If the user then returns to the server, even if their ticket is still open, the bot will not automatically add them to the ticket.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>settickettool closeonleave`

### ticket

**Description:** Commands for using the Tickets system.

Many commands to manage tickets appear when you run help in a ticket channel.

**Usage:** `<@1275521742961508432>ticket`

### ticket export

**Description:** Export all the messages of an existing Ticket in html format.
Please note: all attachments and user avatars are saved with the Discord link in this file.

**Usage:** `<@1275521742961508432>ticket export`

### ticket lock

**Description:** Lock an existing Ticket.

**Usage:** `<@1275521742961508432>ticket lock`

### ticket claim

**Description:** Claim an existing Ticket.

**Usage:** `<@1275521742961508432>ticket claim`

### ticket close

**Description:** Close an existing Ticket.

**Usage:** `<@1275521742961508432>ticket close`

### ticket open

**Description:** Open an existing Ticket.

**Usage:** `<@1275521742961508432>ticket open`

### ticket rename

**Description:** Rename an existing Ticket.

**Usage:** `<@1275521742961508432>ticket rename`

### ticket delete

**Description:** Delete an existing Ticket.

If a logs channel is defined, an html file containing all the messages of this ticket will be generated.
(Attachments are not supported, as they are saved with their Discord link)

**Usage:** `<@1275521742961508432>ticket delete`

### ticket owner

**Description:** Change the owner of an existing Ticket.

**Usage:** `<@1275521742961508432>ticket owner`

### ticket removemember

**Description:** Remove a member to an existing Ticket.

**Usage:** `<@1275521742961508432>ticket removemember`

### ticket unclaim

**Description:** Unclaim an existing Ticket.

**Usage:** `<@1275521742961508432>ticket unclaim`

### ticket list

**Description:** List the existing Tickets for a profile. You can provide a status and/or a ticket owner.

**Usage:** `<@1275521742961508432>ticket list`

### ticket createfor

**Description:** Create a Ticket for a member.

If only one profile has been created on this server, you don't need to specify its name.

**Usage:** `<@1275521742961508432>ticket createfor`

### ticket addmember

**Description:** Add a member to an existing Ticket.

**Usage:** `<@1275521742961508432>ticket addmember`

### ticket unlock

**Description:** Unlock an existing locked Ticket.

**Usage:** `<@1275521742961508432>ticket unlock`

### ticket create

**Description:** Create a Ticket.

If only one profile has been created on this server, you don't need to specify its name.

**Usage:** `<@1275521742961508432>ticket create`

