Extended modlogs<br/>Works with core modlogset channel

# ,modlog
Toggle various extended modlog notifications<br/>

Requires the channel to be setup with `,modlogset modlog #channel`<br/>
Or can be sent to separate channels with `,modlog channel #channel event_name`<br/>
 - Usage: `,modlog`
 - Restricted to: `ADMIN`
 - Aliases: `modlogtoggle and modlogs`
 - Checks: `server_only`
## ,modlog member
Toggle individual member update settings.<br/>
 - Usage: `,modlog member`
 - Aliases: `members and memberchanges`
### ,modlog member settings
Show the current settings on member updates.<br/>
 - Usage: `,modlog member settings`
### ,modlog member roles
Toggle role updates for members.<br/>
 - Usage: `,modlog member roles`
 - Aliases: `role`
### ,modlog member all
Set all member update settings.<br/>

- `<set_to>` True or False what to set all the member update settings to.<br/>
 - Usage: `,modlog member all <set_to>`
Extended Arg Info
> ### set_to: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,modlog member nickname
Toggle nickname updates for member changes.<br/>
 - Usage: `,modlog member nickname`
 - Aliases: `nicknames`
### ,modlog member flags
Toggle flags updates for members.<br/>

This includes things like:<br/>
- `did_rejoin`<br/>
- `completed_onboarding`<br/>
- `bypasses_verification`<br/>
- `started_onboarding`<br/>
 - Usage: `,modlog member flags`
### ,modlog member timeout
Toggle timeout updates for members.<br/>

Note: Due to a discord limitation this will not update when a members<br/>
timeout has expired and may display a before timeout in the past.<br/>
 - Usage: `,modlog member timeout`
### ,modlog member pending
Toggle pending updates for members.<br/>
 - Usage: `,modlog member pending`
### ,modlog member avatar
Toggle avatar updates for member changes.<br/>
 - Usage: `,modlog member avatar`
## ,modlog channel
Set the channel for modlogs.<br/>

    - `<channel>` The text channel to send the events to.<br/>
    <br/>
- `[events...]` must be any of the following options (more than one event can be provided at once):<br/>
 - `channel_change` - Updates to channel name, etc.<br/>
 - `channel_create`<br/>
 - `channel_delete`<br/>
 - `commands_used`  - Bot command usage<br/>
 - `emoji_change`   - Emojis added or deleted<br/>
 - `server_change`   - Server settings changed<br/>
 - `message_edit`<br/>
 - `message_delete`<br/>
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.<br/>
 - `role_change`    - Role updates permissions, name, etc.<br/>
 - `role_create`<br/>
 - `role_delete`<br/>
 - `voice_change`   - Voice channel join/leave<br/>
 - `member_join`<br/>
 - `member_left`<br/>
 - `invite_created`<br/>
 - `invite_deleted`<br/>
 - `thread_create`<br/>
 - `thread_delete`<br/>
 - `thread_change`<br/>
 - `stickers_change`<br/>
 - Usage: `,modlog channel <channel> <events>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,modlog resetchannel
Reset the modlog event to the default modlog channel.<br/>
    <br/>
- `[events...]` must be any of the following options (more than one event can be provided at once):<br/>
 - `channel_change` - Updates to channel name, etc.<br/>
 - `channel_create`<br/>
 - `channel_delete`<br/>
 - `commands_used`  - Bot command usage<br/>
 - `emoji_change`   - Emojis added or deleted<br/>
 - `server_change`   - Server settings changed<br/>
 - `message_edit`<br/>
 - `message_delete`<br/>
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.<br/>
 - `role_change`    - Role updates permissions, name, etc.<br/>
 - `role_create`<br/>
 - `role_delete`<br/>
 - `voice_change`   - Voice channel join/leave<br/>
 - `member_join`<br/>
 - `member_left`<br/>
 - `invite_created`<br/>
 - `invite_deleted`<br/>
 - `thread_create`<br/>
 - `thread_delete`<br/>
 - `thread_change`<br/>
 - `stickers_change`<br/>
 - Usage: `,modlog resetchannel <events>`
## ,modlog all
Turn all logging options on or off.<br/>

- `<true_or_false>` True of False, what to set all loggable settings to.<br/>
 - Usage: `,modlog all <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,modlog ignore
Ignore a channel from message delete/edit events and bot commands.<br/>

- `<channel>` the channel or category to ignore events in<br/>
 - Usage: `,modlog ignore <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.ForumChannel, discord.channel.CategoryChannel, discord.channel.VoiceChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,modlog delete
Delete logging settings.<br/>
 - Usage: `,modlog delete`
### ,modlog delete bulkdelete
Toggle bulk message delete notifications.<br/>
 - Usage: `,modlog delete bulkdelete`
### ,modlog delete cachedonly
Toggle message delete notifications for non-cached messages.<br/>

Delete notifications for non-cached messages<br/>
will only show channel info without content of deleted message or its author.<br/>
 - Usage: `,modlog delete cachedonly`
### ,modlog delete individual
Toggle individual message delete notifications for bulk message delete.<br/>
 - Usage: `,modlog delete individual`
### ,modlog delete ignorecommands
Toggle message delete notifications for valid bot command messages.<br/>
 - Usage: `,modlog delete ignorecommands`
## ,modlog settings
Show the servers current ExtendedModlog settings<br/>
 - Usage: `,modlog settings`
## ,modlog unignore
Unignore a channel from message delete/edit events and bot commands.<br/>

- `<channel>` the channel to unignore message delete/edit events.<br/>
 - Usage: `,modlog unignore <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.ForumChannel, discord.channel.CategoryChannel, discord.channel.VoiceChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,modlog emojiset
Set the emoji used in text modlogs.<br/>

    - `<new_emoji>` can be any discord emoji or unicode emoji the bot has access to use.<br/>
    <br/>
- `[events...]` must be any of the following options (more than one event can be provided at once):<br/>
 - `channel_change` - Updates to channel name, etc.<br/>
 - `channel_create`<br/>
 - `channel_delete`<br/>
 - `commands_used`  - Bot command usage<br/>
 - `emoji_change`   - Emojis added or deleted<br/>
 - `server_change`   - Server settings changed<br/>
 - `message_edit`<br/>
 - `message_delete`<br/>
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.<br/>
 - `role_change`    - Role updates permissions, name, etc.<br/>
 - `role_create`<br/>
 - `role_delete`<br/>
 - `voice_change`   - Voice channel join/leave<br/>
 - `member_join`<br/>
 - `member_left`<br/>
 - `invite_created`<br/>
 - `invite_deleted`<br/>
 - `thread_create`<br/>
 - `thread_delete`<br/>
 - `thread_change`<br/>
 - `stickers_change`<br/>
 - Usage: `,modlog emojiset <emoji> <events>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
## ,modlog colour
Set custom colours for modlog events<br/>

    - `<colour>` must be a hex code or a [built colour.](https://discordpy.readthedocs.io/en/latest/api.html#colour)<br/>
    <br/>
- `[events...]` must be any of the following options (more than one event can be provided at once):<br/>
 - `channel_change` - Updates to channel name, etc.<br/>
 - `channel_create`<br/>
 - `channel_delete`<br/>
 - `commands_used`  - Bot command usage<br/>
 - `emoji_change`   - Emojis added or deleted<br/>
 - `server_change`   - Server settings changed<br/>
 - `message_edit`<br/>
 - `message_delete`<br/>
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.<br/>
 - `role_change`    - Role updates permissions, name, etc.<br/>
 - `role_create`<br/>
 - `role_delete`<br/>
 - `voice_change`   - Voice channel join/leave<br/>
 - `member_join`<br/>
 - `member_left`<br/>
 - `invite_created`<br/>
 - `invite_deleted`<br/>
 - `thread_create`<br/>
 - `thread_delete`<br/>
 - `thread_change`<br/>
 - `stickers_change`<br/>
 - Usage: `,modlog colour <colour> <events>`
 - Aliases: `color`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
## ,modlog commandlevel
Set the level of commands to be logged.<br/>

- `[level...]` must include all levels you want from:<br/>
 - `NONE`<br/>
 - `MOD`<br/>
 - `ADMIN`<br/>
 - `GUILD_OWNER`<br/>
 - `BOT_OWNER`<br/>

These are the basic levels commands check for in permissions.<br/>
`NONE` is a command anyone has permission to use, where as `MOD`<br/>
can be `mod or permissions`<br/>
 - Usage: `,modlog commandlevel <level>`
 - Aliases: `commandslevel`
## ,modlog toggle
Turn on and off specific modlog actions<br/>

    - `<true_or_false>` Either on or off.<br/>
    <br/>
- `[events...]` must be any of the following options (more than one event can be provided at once):<br/>
 - `channel_change` - Updates to channel name, etc.<br/>
 - `channel_create`<br/>
 - `channel_delete`<br/>
 - `commands_used`  - Bot command usage<br/>
 - `emoji_change`   - Emojis added or deleted<br/>
 - `server_change`   - Server settings changed<br/>
 - `message_edit`<br/>
 - `message_delete`<br/>
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.<br/>
 - `role_change`    - Role updates permissions, name, etc.<br/>
 - `role_create`<br/>
 - `role_delete`<br/>
 - `voice_change`   - Voice channel join/leave<br/>
 - `member_join`<br/>
 - `member_left`<br/>
 - `invite_created`<br/>
 - `invite_deleted`<br/>
 - `thread_create`<br/>
 - `thread_delete`<br/>
 - `thread_change`<br/>
 - `stickers_change`<br/>
 - Usage: `,modlog toggle <true_or_false> <events>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,modlog bot
Bot filter settings.<br/>
 - Usage: `,modlog bot`
 - Aliases: `bots`
### ,modlog bot edits
Toggle message edit notifications for bot users.<br/>
 - Usage: `,modlog bot edits`
 - Aliases: `edit`
### ,modlog bot deletes
Toggle message delete notifications for bot users.<br/>

This will not affect delete notifications for messages that aren't in bot's cache.<br/>
 - Usage: `,modlog bot deletes`
 - Aliases: `delete`
### ,modlog bot change
Toggle bots from being logged in user updates.<br/>

This includes roles and nickname.<br/>
 - Usage: `,modlog bot change`
### ,modlog bot voice
Toggle bots from being logged in voice state updates.<br/>
 - Usage: `,modlog bot voice`
## ,modlog embeds
Set modlog events to use embeds or text<br/>

    - `<true_or_false>` The desired embed setting either on or off.<br/>
    <br/>
- `[events...]` must be any of the following options (more than one event can be provided at once):<br/>
 - `channel_change` - Updates to channel name, etc.<br/>
 - `channel_create`<br/>
 - `channel_delete`<br/>
 - `commands_used`  - Bot command usage<br/>
 - `emoji_change`   - Emojis added or deleted<br/>
 - `server_change`   - Server settings changed<br/>
 - `message_edit`<br/>
 - `message_delete`<br/>
 - `member_change`  - Member changes like roles added/removed, nicknames, etc.<br/>
 - `role_change`    - Role updates permissions, name, etc.<br/>
 - `role_create`<br/>
 - `role_delete`<br/>
 - `voice_change`   - Voice channel join/leave<br/>
 - `member_join`<br/>
 - `member_left`<br/>
 - `invite_created`<br/>
 - `invite_deleted`<br/>
 - `thread_create`<br/>
 - `thread_delete`<br/>
 - `thread_change`<br/>
 - `stickers_change`<br/>
 - Usage: `,modlog embeds <true_or_false> <events>`
 - Aliases: `embed`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
