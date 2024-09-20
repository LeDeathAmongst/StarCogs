# DiscordEdit Help

### editvoicechannel

**Description:** Commands for edit a voice channel.

**Usage:** `<@1275521742961508432>editvoicechannel`

### editvoicechannel userlimit

**Description:** Edit voice channel user limit.

It must be a number between 0 and 99.

**Usage:** `<@1275521742961508432>editvoicechannel userlimit`

### editvoicechannel create

**Description:** Create a voice channel.

**Usage:** `<@1275521742961508432>editvoicechannel create`

### editvoicechannel syncpermissions

**Description:** Edit voice channel sync permissions.

**Usage:** `<@1275521742961508432>editvoicechannel syncpermissions`

### editvoicechannel overwrites

**Description:** Edit voice channel overwrites/permissions.

You may not specify `True` or `False` to reset the overwrite(s).
You must possess the permissions you wish to modify.

• `create_instant_invite`
• `manage_channels`
• `add_reactions`
• `priority_speaker`
• `stream`
• `read_messages`
• `send_messages`
• `send_tts_messages`
• `manage_messages`
• `embed_links`
• `attach_files`
• `read_message_history`
• `mention_everyone`
• `external_emojis`
• `connect`
• `speak`
• `mute_members`
• `deafen_members`
• `move_members`
• `use_voice_activation`
• `manage_roles`
• `manage_webhooks`
• `use_application_commands`
• `request_to_speak`
• `manage_threads`
• `create_public_threads`
• `create_private_threads`
• `external_stickers`
• `send_messages_in_threads`

**Usage:** `<@1275521742961508432>editvoicechannel overwrites`

### editvoicechannel bitrate

**Description:** Edit voice channel bitrate.

It must be a number between 8000 and
Level 1: 128000
Level 2: 256000
Level 3: 384000

**Usage:** `<@1275521742961508432>editvoicechannel bitrate`

### editvoicechannel name

**Description:** Edit voice channel name.

**Usage:** `<@1275521742961508432>editvoicechannel name`

### editvoicechannel slowmodedelay

**Description:** Edit voice channel slowmode delay.

Specifies the slowmode rate limit for user in this channel. A value of 0s disables slowmode. The maximum value possible is 21600s.

**Usage:** `<@1275521742961508432>editvoicechannel slowmodedelay`

### editvoicechannel view

**Description:** View and edit voice channel.

**Usage:** `<@1275521742961508432>editvoicechannel view`

### editvoicechannel delete

**Description:** Delete voice channel.

**Usage:** `<@1275521742961508432>editvoicechannel delete`

### editvoicechannel videoqualitymode

**Description:** Edit voice channel video quality mode.

auto = 1
full = 2

**Usage:** `<@1275521742961508432>editvoicechannel videoqualitymode`

### editvoicechannel clone

**Description:** Clone a voice channel.

**Usage:** `<@1275521742961508432>editvoicechannel clone`

### editvoicechannel list

**Description:** List all voice channels in the current guild.

**Usage:** `<@1275521742961508432>editvoicechannel list`

### editvoicechannel invite

**Description:** Create an invite for a voice channel.

`max_age`: How long the invite should last in days. If it's 0 then the invite doesn't expire.
`max_uses`: How many uses the invite could be used for. If it's 0 then there are unlimited uses.
`temporary`: Denotes that the invite grants temporary membership (i.e. they get kicked after they disconnect).
`unique`: Indicates if a unique invite URL should be created. Defaults to True. If this is set to False then it will return a previously created invite.

**Usage:** `<@1275521742961508432>editvoicechannel invite`

### editvoicechannel position

**Description:** Edit voice channel position.

Warning: Only voice channels are taken into account. Channel 1 is the highest positioned voice channel.
Channels cannot be moved to a position that takes them out of their current category.

**Usage:** `<@1275521742961508432>editvoicechannel position`

### editvoicechannel nsfw

**Description:** Edit voice channel nsfw.

**Usage:** `<@1275521742961508432>editvoicechannel nsfw`

### editvoicechannel category

**Description:** Edit voice channel category.

**Usage:** `<@1275521742961508432>editvoicechannel category`

### editthread

**Description:** Commands for edit a text channel.

**Usage:** `<@1275521742961508432>editthread`

### editthread pinned

**Description:** Edit thread pinned.

**Usage:** `<@1275521742961508432>editthread pinned`

### editthread list

**Description:** List all threads in the current guild.

**Usage:** `<@1275521742961508432>editthread list`

### editthread removeuser

**Description:** Remove member from thread.

**Usage:** `<@1275521742961508432>editthread removeuser`

### editthread name

**Description:** Edit thread name.

**Usage:** `<@1275521742961508432>editthread name`

### editthread appliedtags

**Description:** Edit thread applied tags.

```
[p]editthread appliedtags "<name>|<emoji>|[moderated]"
[p]editthread appliedtags "Reporting|⚠️|True" "Bug|🐛"
```

**Usage:** `<@1275521742961508432>editthread appliedtags`

### editthread delete

**Description:** Delete a thread.

**Usage:** `<@1275521742961508432>editthread delete`

### editthread view

**Description:** View and edit thread.

**Usage:** `<@1275521742961508432>editthread view`

### editthread adduser

**Description:** Add member to thread.

**Usage:** `<@1275521742961508432>editthread adduser`

### editthread archived

**Description:** Edit thread archived.

**Usage:** `<@1275521742961508432>editthread archived`

### editthread invitable

**Description:** Edit thread invitable.

**Usage:** `<@1275521742961508432>editthread invitable`

### editthread slowmodedelay

**Description:** Edit thread slowmode delay.

**Usage:** `<@1275521742961508432>editthread slowmodedelay`

### editthread create

**Description:** Create a thread.

You'll join it automatically.

**Usage:** `<@1275521742961508432>editthread create`

### editthread locked

**Description:** Edit thread locked.

**Usage:** `<@1275521742961508432>editthread locked`

### editthread autoarchiveduration

**Description:** Edit thread auto archive duration.

**Usage:** `<@1275521742961508432>editthread autoarchiveduration`

### edittextchannel

**Description:** Commands for edit a text channel.

**Usage:** `<@1275521742961508432>edittextchannel`

### edittextchannel clone

**Description:** Clone a text channel.

**Usage:** `<@1275521742961508432>edittextchannel clone`

### edittextchannel invite

**Description:** Create an invite for a text channel.

`max_age`: How long the invite should last in days. If it's 0 then the invite doesn't expire.
`max_uses`: How many uses the invite could be used for. If it's 0 then there are unlimited uses.
`temporary`: Denotes that the invite grants temporary membership (i.e. they get kicked after they disconnect).
`unique`: Indicates if a unique invite URL should be created. Defaults to True. If this is set to False then it will return a previously created invite.

**Usage:** `<@1275521742961508432>edittextchannel invite`

### edittextchannel name

**Description:** Edit text channel name.

**Usage:** `<@1275521742961508432>edittextchannel name`

### edittextchannel defaultautoarchiveduration

**Description:** Edit text channel default auto archive duration.

The new default auto archive duration in minutes for threads created in this channel. Must be one of `60`, `1440`, `4320`, or `10080`.

**Usage:** `<@1275521742961508432>edittextchannel defaultautoarchiveduration`

### edittextchannel syncpermissions

**Description:** Edit text channel syncpermissions with category.

**Usage:** `<@1275521742961508432>edittextchannel syncpermissions`

### edittextchannel category

**Description:** Edit text channel category.

**Usage:** `<@1275521742961508432>edittextchannel category`

### edittextchannel view

**Description:** View and edit text channel.

**Usage:** `<@1275521742961508432>edittextchannel view`

### edittextchannel nsfw

**Description:** Edit text channel nsfw.

**Usage:** `<@1275521742961508432>edittextchannel nsfw`

### edittextchannel list

**Description:** List all text channels in the current guild.

**Usage:** `<@1275521742961508432>edittextchannel list`

### edittextchannel position

**Description:** Edit text channel position.

Warning: Only text channels are taken into account. Channel 1 is the highest positioned text channel.
Channels cannot be moved to a position that takes them out of their current category.

**Usage:** `<@1275521742961508432>edittextchannel position`

### edittextchannel defaultthreadslowmodedelay

**Description:** Edit text channel default thread slowmode delay.

The new default thread slowmode delay in seconds for threads created in this channel. Must be between 0 and 21600 (6 hours) seconds.

**Usage:** `<@1275521742961508432>edittextchannel defaultthreadslowmodedelay`

### edittextchannel overwrites

**Description:** Edit text channel overwrites/permissions.

You may not specify `True` or `False` to reset the permission(s).
You must possess the permissions you wish to modify.

• `create_instant_invite`
• `manage_channels`
• `add_reactions`
• `priority_speaker`
• `stream`
• `read_messages`
• `send_messages`
• `send_tts_messages`
• `manage_messages`
• `embed_links`
• `attach_files`
• `read_message_history`
• `mention_everyone`
• `external_emojis`
• `connect`
• `speak`
• `mute_members`
• `deafen_members`
• `move_members`
• `use_voice_activation`
• `manage_roles`
• `manage_webhooks`
• `use_application_commands`
• `request_to_speak`
• `manage_threads`
• `create_public_threads`
• `create_private_threads`
• `external_stickers`
• `send_messages_in_threads`

**Usage:** `<@1275521742961508432>edittextchannel overwrites`

### edittextchannel slowmodedelay

**Description:** Edit text channel slowmode delay.

Specifies the slowmode rate limit for user in this channel. A value of 0s disables slowmode. The maximum value possible is 21600s.

**Usage:** `<@1275521742961508432>edittextchannel slowmodedelay`

### edittextchannel type

**Description:** Edit text channel type.

`text`: 0
`news`: 5
Currently, only conversion between ChannelType.text and ChannelType.news is supported. This is only available to guilds that contain NEWS in Guild.features.

**Usage:** `<@1275521742961508432>edittextchannel type`

### edittextchannel delete

**Description:** Delete a text channel.

**Usage:** `<@1275521742961508432>edittextchannel delete`

### edittextchannel topic

**Description:** Edit text channel topic.

**Usage:** `<@1275521742961508432>edittextchannel topic`

### edittextchannel create

**Description:** Create a text channel.

**Usage:** `<@1275521742961508432>edittextchannel create`

### editrole

**Description:** Commands for edit a role.

**Usage:** `<@1275521742961508432>editrole`

### editrole delete

**Description:** Delete a role.

**Usage:** `<@1275521742961508432>editrole delete`

### editrole displayicon

**Description:** Edit role display icon.

`display_icon` can be an Unicode emoji, a custom emoji or an url. You can also upload an attachment.

**Usage:** `<@1275521742961508432>editrole displayicon`

### editrole mentionable

**Description:** Edit role mentionable.

**Usage:** `<@1275521742961508432>editrole mentionable`

### editrole color

**Description:** Edit role color.

**Usage:** `<@1275521742961508432>editrole color`

### editrole view

**Description:** View and edit role.

**Usage:** `<@1275521742961508432>editrole view`

### editrole name

**Description:** Edit role name.

**Usage:** `<@1275521742961508432>editrole name`

### editrole list

**Description:** List all roles in the current guild.

**Usage:** `<@1275521742961508432>editrole list`

### editrole create

**Description:** Create a role.

**Usage:** `<@1275521742961508432>editrole create`

### editrole permissions

**Description:** Edit role permissions.

You must possess the permissions you wish to modify.

• `create_instant_invite`
• `manage_channels`
• `add_reactions`
• `priority_speaker`
• `stream`
• `read_messages`
• `send_messages`
• `send_tts_messages`
• `manage_messages`
• `embed_links`
• `attach_files`
• `read_message_history`
• `mention_everyone`
• `external_emojis`
• `connect`
• `speak`
• `mute_members`
• `deafen_members`
• `move_members`
• `use_voice_activation`
• `manage_roles`
• `manage_webhooks`
• `use_application_commands`
• `request_to_speak`
• `manage_threads`
• `create_public_threads`
• `create_private_threads`
• `external_stickers`
• `send_messages_in_threads`

**Usage:** `<@1275521742961508432>editrole permissions`

### editrole position

**Description:** Edit role position.

Warning: The role with a position 1 is the highest role in the Discord hierarchy.

**Usage:** `<@1275521742961508432>editrole position`

### editrole hoist

**Description:** Edit role hoist.

**Usage:** `<@1275521742961508432>editrole hoist`

### editguild

**Description:** Commands for edit a guild.

**Usage:** `<@1275521742961508432>editguild`

### editguild name

**Description:** Edit guild name.

**Usage:** `<@1275521742961508432>editguild name`

### editguild discoverable

**Description:** Edit guild discoverable state.

**Usage:** `<@1275521742961508432>editguild discoverable`

### editguild create

**Description:** Create a guild with the bot as owner.

**Usage:** `<@1275521742961508432>editguild create`

### editguild splash

**Description:** Edit guild splash.

You can use an URL or upload an attachment.

**Usage:** `<@1275521742961508432>editguild splash`

### editguild banner

**Description:** Edit guild banner.

You can use an URL or upload an attachment.

**Usage:** `<@1275521742961508432>editguild banner`

### editguild discoverysplash

**Description:** Edit guild discovery splash.

You can use an URL or upload an attachment.

**Usage:** `<@1275521742961508432>editguild discoverysplash`

### editguild owner

**Description:** Edit guild owner (if the bot is bot owner).

**Usage:** `<@1275521742961508432>editguild owner`

### editguild ruleschannel

**Description:** Edit guild rules channel.

**Usage:** `<@1275521742961508432>editguild ruleschannel`

### editguild publicupdateschannel

**Description:** Edit guild public updates channel.

**Usage:** `<@1275521742961508432>editguild publicupdateschannel`

### editguild invitesdisabled

**Description:** Edit guild invites disabled state.

**Usage:** `<@1275521742961508432>editguild invitesdisabled`

### editguild clone

**Description:** Clone a guild.

**Usage:** `<@1275521742961508432>editguild clone`

### editguild preferredlocale

**Description:** Edit guild preferred locale.

american_english = 'en-US'
british_english = 'en-GB'
bulgarian = 'bg'
chinese = 'zh-CN'
taiwan_chinese = 'zh-TW'
croatian = 'hr'
czech = 'cs'
danish = 'da'
dutch = 'nl'
finnish = 'fi'
french = 'fr'
german = 'de'
greek = 'el'
hindi = 'hi'
hungarian = 'hu'
italian = 'it'
japanese = 'ja'
korean = 'ko'
lithuanian = 'lt'
norwegian = 'no'
polish = 'pl'
brazil_portuguese = 'pt-BR'
romanian = 'ro'
russian = 'ru'
spain_spanish = 'es-ES'
swedish = 'sv-SE'
thai = 'th'
turkish = 'tr'
ukrainian = 'uk'
vietnamese = 'vi'

**Usage:** `<@1275521742961508432>editguild preferredlocale`

### editguild view

**Description:** View and edit guild.

**Usage:** `<@1275521742961508432>editguild view`

### editguild description

**Description:** Edit guild description.

**Usage:** `<@1275521742961508432>editguild description`

### editguild icon

**Description:** Edit guild icon.

You can use an URL or upload an attachment.

**Usage:** `<@1275521742961508432>editguild icon`

### editguild afktimeout

**Description:** Edit guild afk timeout.

**Usage:** `<@1275521742961508432>editguild afktimeout`

### editguild defaultnotifications

**Description:** Edit guild notification level.

**Usage:** `<@1275521742961508432>editguild defaultnotifications`

### editguild raidalertsdisabled

**Description:** Edit guild invites raid alerts disabled state.

**Usage:** `<@1275521742961508432>editguild raidalertsdisabled`

### editguild widgetchannel

**Description:** Edit guild invites widget channel.

**Usage:** `<@1275521742961508432>editguild widgetchannel`

### editguild safetyalertschannel

**Description:** Edit guild invites safety alerts channel.

**Usage:** `<@1275521742961508432>editguild safetyalertschannel`

### editguild vanitycode

**Description:** Edit guild vanity code.

**Usage:** `<@1275521742961508432>editguild vanitycode`

### editguild explicitcontentfilter

**Description:** Edit guild explicit content filter.

**Usage:** `<@1275521742961508432>editguild explicitcontentfilter`

### editguild widgetenabled

**Description:** Edit guild invites widget enabled state.

**Usage:** `<@1275521742961508432>editguild widgetenabled`

### editguild community

**Description:** Edit guild community state.

**Usage:** `<@1275521742961508432>editguild community`

### editguild systemchannelflags

**Description:** Edit guild system channel flags.

**Usage:** `<@1275521742961508432>editguild systemchannelflags`

### editguild verificationlevel

**Description:** Edit guild verification level.

**Usage:** `<@1275521742961508432>editguild verificationlevel`

### editguild premiumprogressbarenabled

**Description:** Edit guild premium progress bar enabled.

**Usage:** `<@1275521742961508432>editguild premiumprogressbarenabled`

### editguild delete

**Description:** Delete guild (if the bot is owner).

**Usage:** `<@1275521742961508432>editguild delete`

### editguild afkchannel

**Description:** Edit guild afkchannel.

**Usage:** `<@1275521742961508432>editguild afkchannel`

### editguild systemchannel

**Description:** Edit guild system channel.

**Usage:** `<@1275521742961508432>editguild systemchannel`

