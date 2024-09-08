# ExtendedModLog Help

### modlog

**Description:** Toggle various extended modlog notifications

Requires the channel to be setup with `[p]modlogset modlog #channel`
Or can be sent to separate channels with `[p]modlog channel #channel event_name`

**Usage:** `<@1275521742961508432>modlog`

### modlog bot

**Description:** Bot filter settings.

**Usage:** `<@1275521742961508432>modlog bot`

### modlog bot change

**Description:** Toggle bots from being logged in user updates.

This includes roles and nickname.

**Usage:** `<@1275521742961508432>modlog bot change`

### modlog bot edits

**Description:** Toggle message edit notifications for bot users.

**Usage:** `<@1275521742961508432>modlog bot edits`

### modlog bot voice

**Description:** Toggle bots from being logged in voice state updates.

**Usage:** `<@1275521742961508432>modlog bot voice`

### modlog bot deletes

**Description:** Toggle message delete notifications for bot users.

This will not affect delete notifications for messages that aren't in bot's cache.

**Usage:** `<@1275521742961508432>modlog bot deletes`

### modlog resetchannel

**Description:**     Reset the modlog event to the default modlog channel.
    
- `[events...]` must be any of the following options (more than one event can be provided at once):
 - `channel_change` - Updates to channel name, etc.
 - `channel_create`
 - `channel_delete`
 - `commands_used`  - Bot command usage
 - `emoji_change`   - Emojis added or deleted
 - `guild_change`   - Server settings changed
 - `message_edit`
 - `message_delete`
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.
 - `role_change`    - Role updates permissions, name, etc.
 - `role_create`
 - `role_delete`
 - `voice_change`   - Voice channel join/leave
 - `member_join`
 - `member_left`
 - `invite_created`
 - `invite_deleted`
 - `thread_create`
 - `thread_delete`
 - `thread_change`
 - `stickers_change`

**Usage:** `<@1275521742961508432>modlog resetchannel`

### modlog commandlevel

**Description:** Set the level of commands to be logged.

- `[level...]` must include all levels you want from:
 - `NONE`
 - `MOD`
 - `ADMIN`
 - `GUILD_OWNER`
 - `BOT_OWNER`

These are the basic levels commands check for in permissions.
`NONE` is a command anyone has permission to use, where as `MOD`
can be `mod or permissions`

**Usage:** `<@1275521742961508432>modlog commandlevel`

### modlog unignore

**Description:** Unignore a channel from message delete/edit events and bot commands.

- `<channel>` the channel to unignore message delete/edit events.

**Usage:** `<@1275521742961508432>modlog unignore`

### modlog toggle

**Description:**     Turn on and off specific modlog actions

    - `<true_or_false>` Either on or off.
    
- `[events...]` must be any of the following options (more than one event can be provided at once):
 - `channel_change` - Updates to channel name, etc.
 - `channel_create`
 - `channel_delete`
 - `commands_used`  - Bot command usage
 - `emoji_change`   - Emojis added or deleted
 - `guild_change`   - Server settings changed
 - `message_edit`
 - `message_delete`
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.
 - `role_change`    - Role updates permissions, name, etc.
 - `role_create`
 - `role_delete`
 - `voice_change`   - Voice channel join/leave
 - `member_join`
 - `member_left`
 - `invite_created`
 - `invite_deleted`
 - `thread_create`
 - `thread_delete`
 - `thread_change`
 - `stickers_change`

**Usage:** `<@1275521742961508432>modlog toggle`

### modlog delete

**Description:** Delete logging settings.

**Usage:** `<@1275521742961508432>modlog delete`

### modlog delete individual

**Description:** Toggle individual message delete notifications for bulk message delete.

**Usage:** `<@1275521742961508432>modlog delete individual`

### modlog delete ignorecommands

**Description:** Toggle message delete notifications for valid bot command messages.

**Usage:** `<@1275521742961508432>modlog delete ignorecommands`

### modlog delete cachedonly

**Description:** Toggle message delete notifications for non-cached messages.

Delete notifications for non-cached messages
will only show channel info without content of deleted message or its author.

**Usage:** `<@1275521742961508432>modlog delete cachedonly`

### modlog delete bulkdelete

**Description:** Toggle bulk message delete notifications.

**Usage:** `<@1275521742961508432>modlog delete bulkdelete`

### modlog ignore

**Description:** Ignore a channel from message delete/edit events and bot commands.

- `<channel>` the channel or category to ignore events in

**Usage:** `<@1275521742961508432>modlog ignore`

### modlog emojiset

**Description:**     Set the emoji used in text modlogs.

    - `<new_emoji>` can be any discord emoji or unicode emoji the bot has access to use.
    
- `[events...]` must be any of the following options (more than one event can be provided at once):
 - `channel_change` - Updates to channel name, etc.
 - `channel_create`
 - `channel_delete`
 - `commands_used`  - Bot command usage
 - `emoji_change`   - Emojis added or deleted
 - `guild_change`   - Server settings changed
 - `message_edit`
 - `message_delete`
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.
 - `role_change`    - Role updates permissions, name, etc.
 - `role_create`
 - `role_delete`
 - `voice_change`   - Voice channel join/leave
 - `member_join`
 - `member_left`
 - `invite_created`
 - `invite_deleted`
 - `thread_create`
 - `thread_delete`
 - `thread_change`
 - `stickers_change`

**Usage:** `<@1275521742961508432>modlog emojiset`

### modlog all

**Description:** Turn all logging options on or off.

- `<true_or_false>` True of False, what to set all loggable settings to.

**Usage:** `<@1275521742961508432>modlog all`

### modlog colour

**Description:**     Set custom colours for modlog events

    - `<colour>` must be a hex code or a [built colour.](https://discordpy.readthedocs.io/en/latest/api.html#colour)
    
- `[events...]` must be any of the following options (more than one event can be provided at once):
 - `channel_change` - Updates to channel name, etc.
 - `channel_create`
 - `channel_delete`
 - `commands_used`  - Bot command usage
 - `emoji_change`   - Emojis added or deleted
 - `guild_change`   - Server settings changed
 - `message_edit`
 - `message_delete`
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.
 - `role_change`    - Role updates permissions, name, etc.
 - `role_create`
 - `role_delete`
 - `voice_change`   - Voice channel join/leave
 - `member_join`
 - `member_left`
 - `invite_created`
 - `invite_deleted`
 - `thread_create`
 - `thread_delete`
 - `thread_change`
 - `stickers_change`

**Usage:** `<@1275521742961508432>modlog colour`

### modlog channel

**Description:**     Set the channel for modlogs.

    - `<channel>` The text channel to send the events to.
    
- `[events...]` must be any of the following options (more than one event can be provided at once):
 - `channel_change` - Updates to channel name, etc.
 - `channel_create`
 - `channel_delete`
 - `commands_used`  - Bot command usage
 - `emoji_change`   - Emojis added or deleted
 - `guild_change`   - Server settings changed
 - `message_edit`
 - `message_delete`
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.
 - `role_change`    - Role updates permissions, name, etc.
 - `role_create`
 - `role_delete`
 - `voice_change`   - Voice channel join/leave
 - `member_join`
 - `member_left`
 - `invite_created`
 - `invite_deleted`
 - `thread_create`
 - `thread_delete`
 - `thread_change`
 - `stickers_change`

**Usage:** `<@1275521742961508432>modlog channel`

### modlog settings

**Description:** Show the servers current ExtendedModlog settings

**Usage:** `<@1275521742961508432>modlog settings`

### modlog member

**Description:** Toggle individual member update settings.

**Usage:** `<@1275521742961508432>modlog member`

### modlog member avatar

**Description:** Toggle avatar updates for member changes.

**Usage:** `<@1275521742961508432>modlog member avatar`

### modlog member pending

**Description:** Toggle pending updates for members.

**Usage:** `<@1275521742961508432>modlog member pending`

### modlog member timeout

**Description:** Toggle timeout updates for members.

Note: Due to a discord limitation this will not update when a members
timeout has expired and may display a before timeout in the past.

**Usage:** `<@1275521742961508432>modlog member timeout`

### modlog member all

**Description:** Set all member update settings.

- `<set_to>` True or False what to set all the member update settings to.

**Usage:** `<@1275521742961508432>modlog member all`

### modlog member nickname

**Description:** Toggle nickname updates for member changes.

**Usage:** `<@1275521742961508432>modlog member nickname`

### modlog member flags

**Description:** Toggle flags updates for members.

This includes things like:
- `did_rejoin`
- `completed_onboarding`
- `bypasses_verification`
- `started_onboarding`

**Usage:** `<@1275521742961508432>modlog member flags`

### modlog member roles

**Description:** Toggle role updates for members.

**Usage:** `<@1275521742961508432>modlog member roles`

### modlog member settings

**Description:** Show the current settings on member updates.

**Usage:** `<@1275521742961508432>modlog member settings`

### modlog embeds

**Description:**     Set modlog events to use embeds or text

    - `<true_or_false>` The desired embed setting either on or off.
    
- `[events...]` must be any of the following options (more than one event can be provided at once):
 - `channel_change` - Updates to channel name, etc.
 - `channel_create`
 - `channel_delete`
 - `commands_used`  - Bot command usage
 - `emoji_change`   - Emojis added or deleted
 - `guild_change`   - Server settings changed
 - `message_edit`
 - `message_delete`
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.
 - `role_change`    - Role updates permissions, name, etc.
 - `role_create`
 - `role_delete`
 - `voice_change`   - Voice channel join/leave
 - `member_join`
 - `member_left`
 - `invite_created`
 - `invite_deleted`
 - `thread_create`
 - `thread_delete`
 - `thread_change`
 - `stickers_change`

**Usage:** `<@1275521742961508432>modlog embeds`

