# AutoRoom Help

### autoroomset

**Description:** Configure the AutoRoom cog.

For a quick rundown on how to get started with this cog,
check out [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/autoroom/README.md)

**Usage:** `<@1275521742961508432>autoroomset`

### autoroomset create

**Description:** Create an AutoRoom Source.

Anyone joining an AutoRoom Source will automatically have a new
voice channel (AutoRoom) created in the destination category,
and then be moved into it.

**Usage:** `<@1275521742961508432>autoroomset create`

### autoroomset modify

**Description:** Modify an existing AutoRoom Source.

**Usage:** `<@1275521742961508432>autoroomset modify`

### autoroomset modify legacytextchannel

**Description:** Manage if a legacy text channel should be created as well.

**Usage:** `<@1275521742961508432>autoroomset modify legacytextchannel`

### autoroomset modify legacytextchannel enable

**Description:** Enable creating a legacy text channel with the AutoRoom.

**Usage:** `<@1275521742961508432>autoroomset modify legacytextchannel enable`

### autoroomset modify legacytextchannel disable

**Description:** Disable creating a legacy text channel with the AutoRoom.

**Usage:** `<@1275521742961508432>autoroomset modify legacytextchannel disable`

### autoroomset modify legacytextchannel topic

**Description:** Manage the legacy text channel topic.

**Usage:** `<@1275521742961508432>autoroomset modify legacytextchannel topic`

### autoroomset modify legacytextchannel topic set

**Description:** Set the legacy text channel topic.

- Example:
`This channel is only visible to members of your voice channel, and admins of this server. It will be deleted when everyone leaves. `

**Usage:** `<@1275521742961508432>autoroomset modify legacytextchannel topic set`

### autoroomset modify legacytextchannel topic disable

**Description:** Disable setting a legacy text channel topic.

**Usage:** `<@1275521742961508432>autoroomset modify legacytextchannel topic disable`

### autoroomset modify defaults

**Description:** Learn how AutoRoom defaults are set.

**Usage:** `<@1275521742961508432>autoroomset modify defaults`

### autoroomset modify name

**Description:** Set the default name format of an AutoRoom.

**Usage:** `<@1275521742961508432>autoroomset modify name`

### autoroomset modify name username

**Description:** Default format: PhasecoreX's Room.

Custom format example:
`{{username}}'s Room{% if dupenum > 1 %} ({{dupenum}}){% endif %}`

**Usage:** `<@1275521742961508432>autoroomset modify name username`

### autoroomset modify name custom

**Description:** A custom channel name.

Use `{{ expressions }}` to print variables and `{% statements %}` to do basic evaluations on variables.

Variables supported:
- `username` - AutoRoom Owner's username
- `game    ` - AutoRoom Owner's game
- `dupenum ` - An incrementing number that starts at 1, useful for un-duplicating channel names

Statements supported:
- `if/elif/else/endif`
- Example: `{% if dupenum > 1 %}DupeNum is {{dupenum}}, which is greater than 1{% endif %}`
- Another example: `{% if not game %}User isn't playing a game!{% endif %}`

It's kinda like Jinja2, but way simpler. Check out [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/autoroom/README.md) for more info.

**Usage:** `<@1275521742961508432>autoroomset modify name custom`

### autoroomset modify name game

**Description:** The users current playing game, otherwise the username format.

Custom format example:
`{{game}}{% if not game %}{{username}}'s Room{% endif %}{% if dupenum > 1 %} ({{dupenum}}){% endif %}`

**Usage:** `<@1275521742961508432>autoroomset modify name game`

### autoroomset modify specialperms

**Description:** Modify special AutoRoom permissions.

Remember, most permissions are automatically copied
from the AuthRoom Source over to the AutoRoom.
These are for configuring special cases.

**Usage:** `<@1275521742961508432>autoroomset modify specialperms`

### autoroomset modify specialperms sendmessage

**Description:** Allow users to send messages in the AutoRoom built in text channel.

**Usage:** `<@1275521742961508432>autoroomset modify specialperms sendmessage`

### autoroomset modify specialperms ownermodify

**Description:** Allow AutoRoom Owners to have the Manage Channels permission on their AutoRoom.

**Usage:** `<@1275521742961508432>autoroomset modify specialperms ownermodify`

### autoroomset modify text

**Description:** Configure sending an introductory message to the AutoRoom text channel.

**Usage:** `<@1275521742961508432>autoroomset modify text`

### autoroomset modify text set

**Description:** Send a message to the newly generated AutoRoom text channel.

This can have template variables and statements, which you can learn more
about by looking at `[p]autoroomset modify name custom`, or by looking at
[the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/autoroom/README.md).

The only additional variable that may be useful here is the `mention` variable,
which will insert the users mention (pinging them).

- Example:
`Hello {{mention}}! Welcome to your new AutoRoom!`

**Usage:** `<@1275521742961508432>autoroomset modify text set`

### autoroomset modify text disable

**Description:** Disable sending a message to the newly generated AutoRoom text channel.

**Usage:** `<@1275521742961508432>autoroomset modify text disable`

### autoroomset modify type

**Description:** Choose what type of AutoRoom is created.

**Usage:** `<@1275521742961508432>autoroomset modify type`

### autoroomset modify type locked

**Description:** Rooms will be visible to all, but not joinable. AutoRoom Owner can allow users in.

**Usage:** `<@1275521742961508432>autoroomset modify type locked`

### autoroomset modify type server

**Description:** Rooms will be open to all, but the server owns the AutoRoom (so they can't be modified).

**Usage:** `<@1275521742961508432>autoroomset modify type server`

### autoroomset modify type public

**Description:** Rooms will be open to all. AutoRoom Owner has control over room.

**Usage:** `<@1275521742961508432>autoroomset modify type public`

### autoroomset modify type private

**Description:** Rooms will be hidden. AutoRoom Owner can allow users in.

**Usage:** `<@1275521742961508432>autoroomset modify type private`

### autoroomset modify category

**Description:** Set the category that AutoRooms will be created in.

**Usage:** `<@1275521742961508432>autoroomset modify category`

### autoroomset access

**Description:** Control access to all AutoRooms.

Roles that are considered "admin" or "moderator" are
set up with the commands `[p]set addadminrole`
and `[p]set addmodrole` (plus the remove commands too)

**Usage:** `<@1275521742961508432>autoroomset access`

### autoroomset access mod

**Description:** Allow Moderators to join locked/private AutoRooms.

**Usage:** `<@1275521742961508432>autoroomset access mod`

### autoroomset access admin

**Description:** Allow Admins to join locked/private AutoRooms.

**Usage:** `<@1275521742961508432>autoroomset access admin`

### autoroomset access bot

**Description:** Automatically allow bots into AutoRooms.

The AutoRoom Owner is able to freely allow or deny these roles as they see fit.

**Usage:** `<@1275521742961508432>autoroomset access bot`

### autoroomset access bot add

**Description:** Allow a bot role into every AutoRoom.

**Usage:** `<@1275521742961508432>autoroomset access bot add`

### autoroomset access bot remove

**Description:** Disallow a bot role from joining every AutoRoom.

**Usage:** `<@1275521742961508432>autoroomset access bot remove`

### autoroomset permissions

**Description:** Check that the bot has all needed permissions.

**Usage:** `<@1275521742961508432>autoroomset permissions`

### autoroomset settings

**Description:** Display current settings.

**Usage:** `<@1275521742961508432>autoroomset settings`

### autoroomset remove

**Description:** Remove an AutoRoom Source.

**Usage:** `<@1275521742961508432>autoroomset remove`

### controlpanel

**Description:** Send the master control panel for the guild. Restricted to guild owner.

**Usage:** `<@1275521742961508432>controlpanel`

