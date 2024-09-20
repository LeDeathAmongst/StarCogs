# Mod Help

### slowmode

**Description:** Changes thread's or text channel's slowmode setting.

Interval can be anything from 0 seconds to 6 hours.
Use without parameters to disable.

**Usage:** `<@1275521742961508432>slowmode`

### rename

**Description:** Change a member's server nickname.

Leaving the nickname argument empty will remove it.

**Usage:** `<@1275521742961508432>rename`

### userinfo

**Description:** Show information about a member.

This includes fields for status, discord join date, server
join date, voice state and previous usernames/global display names/nicknames.

If the member has no roles, previous usernames, global display names, or server nicknames,
these fields will be omitted.

**Usage:** `<@1275521742961508432>userinfo`

### names

**Description:** Show previous usernames, global display names, and server nicknames of a member.

**Usage:** `<@1275521742961508432>names`

### massban

**Description:** Mass bans user(s) from the server.

`days` is the amount of days of messages to cleanup on massban.

Example:
   - `[p]massban 345628097929936898 57287406247743488 7 they broke all rules.`
    This will ban all the added userids and delete 7 days worth of their messages.

User IDs need to be provided in order to ban
using this command.

**Usage:** `<@1275521742961508432>massban`

### voicekick

**Description:** Kick a member from a voice channel.

**Usage:** `<@1275521742961508432>voicekick`

### voiceunban

**Description:** Unban a user from speaking and listening in the server's voice channels.

**Usage:** `<@1275521742961508432>voiceunban`

### voiceban

**Description:** Ban a user from speaking and listening in the server's voice channels.

**Usage:** `<@1275521742961508432>voiceban`

### modset

**Description:** Manage server administration settings.

**Usage:** `<@1275521742961508432>modset`

### modset showmessages

**Description:** Show the current messages for moderation commands.

**Usage:** `<@1275521742961508432>modset showmessages`

### modset deleterepeats

**Description:** Enable auto-deletion of repeated messages.

Must be between 2 and 20.

Set to -1 to disable this feature.

**Usage:** `<@1275521742961508432>modset deleterepeats`

### modset tracknicknames

**Description:** Toggle whether server nickname changes should be tracked.

This setting will be overridden if trackallnames is disabled.

**Usage:** `<@1275521742961508432>modset tracknicknames`

### modset kickmessage

**Description:** Set the message sent when a user is kicked.

**Blocks:**
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)

**Variables:**
- `{user}`: [member that was kicked.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{moderator}`: [modrator that kicked the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{reason}`: reason for the kick.
- `{guild}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)

**Usage:** `<@1275521742961508432>modset kickmessage`

### modset banmessage

**Description:** Set the message sent when a user is banned.

**Blocks:**
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)

**Variables:**
- `{user}`: [member that was banned.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{moderator}`: [modrator that banned the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{reason}`: reason for the ban.
- `{guild}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)
- `{days}`: number of days of messages deleted.

**Usage:** `<@1275521742961508432>modset banmessage`

### modset unbanmessage

**Description:** Set the message sent when a user is unbanned.

**Blocks:**
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)

**Variables:**
- `{user}`: [member that was tempbanned.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{moderator}`: [modrator that tempbanned the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{reason}`: reason for the tempban.
- `{guild}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)

**Usage:** `<@1275521742961508432>modset unbanmessage`

### modset reasons

**Description:** Set whether a reason is required for moderation actions.

**Usage:** `<@1275521742961508432>modset reasons`

### modset showsettings

**Description:** Show the current server administration settings.

**Usage:** `<@1275521742961508432>modset showsettings`

### modset defaultduration

**Description:** Set the default time to be used when a user is tempbanned.

Accepts: seconds, minutes, hours, days, weeks
`duration` must be greater than zero.

Examples:
    `[p]modset defaultduration 7d12h10m`
    `[p]modset defaultduration 7 days 12 hours 10 minutes`

**Usage:** `<@1275521742961508432>modset defaultduration`

### modset deletenames

**Description:** Delete all stored usernames, global display names, and server nicknames.

Examples:
- `[p]modset deletenames` - Did not confirm. Shows the help message.
- `[p]modset deletenames yes` - Deletes all stored usernames, global display names, and server nicknames.

**Arguments**

- `<confirmation>` This will default to false unless specified.

**Usage:** `<@1275521742961508432>modset deletenames`

### modset tempbanmessage

**Description:** Set the message sent when a user is tempbanned.

**Blocks:**
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)

**Variables:**
- `{user}`: [member that was tempbanned.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{moderator}`: [modrator that tempbanned the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{reason}`: reason for the tempban.
- `{guild}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)
- `{days}`: number of days of messages deleted.
- `{duration}`: duration of the tempban.

**Usage:** `<@1275521742961508432>modset tempbanmessage`

### modset hierarchy

**Description:** Toggle role hierarchy check for mods and admins.

**WARNING**: Disabling this setting will allow mods to take
actions on users above them in the role hierarchy!

This is enabled by default.

**Usage:** `<@1275521742961508432>modset hierarchy`

### modset dm

**Description:** Toggle whether a message should be sent to a user when they are kicked/banned.

If this option is enabled, the bot will attempt to DM the user with the guild name
and reason as to why they were kicked/banned.

**Usage:** `<@1275521742961508432>modset dm`

### modset defaultdays

**Description:** Set the default number of days worth of messages to be deleted when a user is banned.

The number of days must be between 0 and 7.

**Usage:** `<@1275521742961508432>modset defaultdays`

### modset trackallnames

**Description:** Toggle whether all name changes should be tracked.

Toggling this off also overrides the tracknicknames setting.

**Usage:** `<@1275521742961508432>modset trackallnames`

### modset mentionspam

**Description:** Manage the automoderation settings for mentionspam.

**Usage:** `<@1275521742961508432>modset mentionspam`

### modset mentionspam strict

**Description:** Setting to account for duplicate mentions.

If enabled all mentions will count including duplicated mentions.
If disabled only unique mentions will count.

Use this command without any parameter to see current setting.

**Usage:** `<@1275521742961508432>modset mentionspam strict`

### modset mentionspam warn

**Description:** Sets the autowarn conditions for mention spam.

Users will be warned if they send any messages which contain more than
`<max_mentions>` mentions.

`<max_mentions>` Must be 0 or greater. Set to 0 to disable this feature.

**Usage:** `<@1275521742961508432>modset mentionspam warn`

### modset mentionspam kick

**Description:** Sets the autokick conditions for mention spam.

Users will be kicked if they send any messages which contain more than
`<max_mentions>` mentions.

`<max_mentions>` Must be 0 or greater. Set to 0 to disable this feature.

**Usage:** `<@1275521742961508432>modset mentionspam kick`

### modset mentionspam ban

**Description:** Set the autoban conditions for mention spam.

Users will be banned if they send any message which contains more than
`<max_mentions>` mentions.

`<max_mentions>` Must be 0 or greater. Set to 0 to disable this feature.

**Usage:** `<@1275521742961508432>modset mentionspam ban`

### modset reinvite

**Description:** Toggle whether an invite will be sent to a user when unbanned.

If this is True, the bot will attempt to create and send a single-use invite
to the newly-unbanned user.

**Usage:** `<@1275521742961508432>modset reinvite`

### kick

**Description:** Kick a user.
Examples:
   - `[p]kick 428675506947227648 wanted to be kicked.`
    This will kick the user with ID 428675506947227648 from the server.
   - `[p]kick @Twentysix wanted to be kicked.`
    This will kick Twentysix from the server.
If a reason is specified, it will be the reason that shows up
in the audit log.

**Usage:** `<@1275521742961508432>kick`

### tempban

**Description:** Temporarily ban a user from this server.
`duration` is the amount of time the user should be banned for.
`days` is the amount of days of messages to cleanup on tempban.
Examples:
   - `[p]tempban @Twentysix Because I say so`
    This will ban Twentysix for the default amount of time set by an administrator.
   - `[p]tempban @Twentysix 15m You need a timeout`
    This will ban Twentysix for 15 minutes.
   - `[p]tempban 428675506947227648 1d2h15m 5 Evil person`
    This will ban the user with ID 428675506947227648 for 1 day 2 hours 15 minutes and will delete the last 5 days of their messages.

**Usage:** `<@1275521742961508432>tempban`

### softban

**Description:** Kick a user and delete 1 day's worth of their messages.

**Usage:** `<@1275521742961508432>softban`

### ban

**Description:** Ban a user from this server and optionally delete days of messages.

`days` is the amount of days of messages to cleanup on ban.

Examples:
   - `[p]ban 428675506947227648 7 Continued to spam after told to stop.`
    This will ban the user with ID 428675506947227648 and it will delete 7 days worth of messages.
   - `[p]ban @Twentysix 7 Continued to spam after told to stop.`
    This will ban Twentysix and it will delete 7 days worth of messages.

A user ID should be provided if the user is not a member of this server.
If days is not a number, it's treated as the first word of the reason.
Minimum 0 days, maximum 7. If not specified, the defaultdays setting will be used instead.

**Usage:** `<@1275521742961508432>ban`

### unban

**Description:** Unban a user from this server.
Requires specifying the target user's ID. To find this, you may either:
 1. Copy it from the mod log case (if one was created), or
 2. enable developer mode, go to Bans in this server's settings, right-
click the user and select 'Copy ID'.

**Usage:** `<@1275521742961508432>unban`

