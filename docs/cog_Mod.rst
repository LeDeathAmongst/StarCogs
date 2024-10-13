Mod
===

Mod with custom messages.

# ,slowmode
Changes thread's or text channel's slowmode setting.<br/>

Interval can be anything from 0 seconds to 6 hours.<br/>
Use without parameters to disable.<br/>
 - Usage: `,slowmode [interval]`
 - Checks: `bot_can_manage_channel and server_only`


# ,rename
Change a member's server nickname.<br/>

Leaving the nickname argument empty will remove it.<br/>
 - Usage: `,rename <member> [nickname]`
 - Restricted to: `ADMIN`
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
> ### nickname: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,userinfo
Show information about a member.<br/>

This includes fields for status, discord join date, server<br/>
join date, voice state and previous usernames/global display names/nicknames.<br/>

If the member has no roles, previous usernames, global display names, or server nicknames,<br/>
these fields will be omitted.<br/>
 - Usage: `,userinfo [member]`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member = None
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


# ,names
Show previous usernames, global display names, and server nicknames of a member.<br/>
 - Usage: `,names <member>`
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


# ,massban
Mass bans user(s) from the server.<br/>

`days` is the amount of days of messages to cleanup on massban.<br/>

Example:<br/>
   - `,massban 345628097929936898 57287406247743488 7 they broke all rules.`<br/>
    This will ban all the added userids and delete 7 days worth of their messages.<br/>

User IDs need to be provided in order to ban<br/>
using this command.<br/>
 - Usage: `,massban <user_ids> [days=None] [reason]`
 - Restricted to: `ADMIN`
 - Aliases: `hackban`
 - Checks: `server_only`
Extended Arg Info
> ### days: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,voicekick
Kick a member from a voice channel.<br/>
 - Usage: `,voicekick <member> [reason]`
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,voiceunban
Unban a user from speaking and listening in the server's voice channels.<br/>
 - Usage: `,voiceunban <member> [reason]`
 - Restricted to: `ADMIN`
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,voiceban
Ban a user from speaking and listening in the server's voice channels.<br/>
 - Usage: `,voiceban <member> [reason]`
 - Restricted to: `ADMIN`
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,moveignoredchannels
Move ignored channels and servers to core<br/>
 - Usage: `,moveignoredchannels`
 - Restricted to: `BOT_OWNER`


# ,movedeletedelay
Move deletedelay settings to core<br/>
 - Usage: `,movedeletedelay`
 - Restricted to: `BOT_OWNER`


# ,modset
Manage server administration settings.<br/>
 - Usage: `,modset`
 - Restricted to: `GUILD_OWNER`


## ,modset tempbanmessage
Set the message sent when a user is tempbanned.<br/>

**Blocks:**<br/>
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)<br/>
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)<br/>

**Variables:**<br/>
- `{user}`: [member that was tempbanned.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{moderator}`: [modrator that tempbanned the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{reason}`: reason for the tempban.<br/>
- `{server}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)<br/>
- `{days}`: number of days of messages deleted.<br/>
- `{duration}`: duration of the tempban.<br/>
 - Usage: `,modset tempbanmessage <message>`
 - Checks: `server_only`


## ,modset hierarchy
Toggle role hierarchy check for mods and admins.<br/>

**WARNING**: Disabling this setting will allow mods to take<br/>
actions on users above them in the role hierarchy!<br/>

This is enabled by default.<br/>
 - Usage: `,modset hierarchy`
 - Checks: `server_only`


## ,modset dm
Toggle whether a message should be sent to a user when they are kicked/banned.<br/>

If this option is enabled, the bot will attempt to DM the user with the server name<br/>
and reason as to why they were kicked/banned.<br/>
 - Usage: `,modset dm [enabled=None]`
 - Checks: `server_only`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,modset defaultdays
Set the default number of days worth of messages to be deleted when a user is banned.<br/>

The number of days must be between 0 and 7.<br/>
 - Usage: `,modset defaultdays [days=0]`
 - Checks: `server_only`
Extended Arg Info
> ### days: int = 0
> ```
> A number without decimal places.
> ```


## ,modset trackallnames
Toggle whether all name changes should be tracked.<br/>

Toggling this off also overrides the tracknicknames setting.<br/>
 - Usage: `,modset trackallnames [enabled=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,modset mentionspam
Manage the automoderation settings for mentionspam.<br/>
 - Usage: `,modset mentionspam`
 - Checks: `server_only`


### ,modset mentionspam strict
Setting to account for duplicate mentions.<br/>

If enabled all mentions will count including duplicated mentions.<br/>
If disabled only unique mentions will count.<br/>

Use this command without any parameter to see current setting.<br/>
 - Usage: `,modset mentionspam strict [enabled=None]`
 - Checks: `server_only`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


### ,modset mentionspam warn
Sets the autowarn conditions for mention spam.<br/>

Users will be warned if they send any messages which contain more than<br/>
`<max_mentions>` mentions.<br/>

`<max_mentions>` Must be 0 or greater. Set to 0 to disable this feature.<br/>
 - Usage: `,modset mentionspam warn <max_mentions>`
 - Checks: `server_only`
Extended Arg Info
> ### max_mentions: int
> ```
> A number without decimal places.
> ```


### ,modset mentionspam kick
Sets the autokick conditions for mention spam.<br/>

Users will be kicked if they send any messages which contain more than<br/>
`<max_mentions>` mentions.<br/>

`<max_mentions>` Must be 0 or greater. Set to 0 to disable this feature.<br/>
 - Usage: `,modset mentionspam kick <max_mentions>`
 - Checks: `server_only`
Extended Arg Info
> ### max_mentions: int
> ```
> A number without decimal places.
> ```


### ,modset mentionspam ban
Set the autoban conditions for mention spam.<br/>

Users will be banned if they send any message which contains more than<br/>
`<max_mentions>` mentions.<br/>

`<max_mentions>` Must be 0 or greater. Set to 0 to disable this feature.<br/>
 - Usage: `,modset mentionspam ban <max_mentions>`
 - Checks: `server_only`
Extended Arg Info
> ### max_mentions: int
> ```
> A number without decimal places.
> ```


## ,modset reasons
Set whether a reason is required for moderation actions.<br/>
 - Usage: `,modset reasons <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,modset defaultduration
Set the default time to be used when a user is tempbanned.<br/>

Accepts: seconds, minutes, hours, days, weeks<br/>
`duration` must be greater than zero.<br/>

Examples:<br/>
    `,modset defaultduration 7d12h10m`<br/>
    `,modset defaultduration 7 days 12 hours 10 minutes`<br/>
 - Usage: `,modset defaultduration <duration>`
 - Checks: `server_only`


## ,modset reinvite
Toggle whether an invite will be sent to a user when unbanned.<br/>

If this is True, the bot will attempt to create and send a single-use invite<br/>
to the newly-unbanned user.<br/>
 - Usage: `,modset reinvite`
 - Checks: `server_only`


## ,modset tracknicknames
Toggle whether server nickname changes should be tracked.<br/>

This setting will be overridden if trackallnames is disabled.<br/>
 - Usage: `,modset tracknicknames [enabled=None]`
 - Checks: `server_only`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,modset deletenames
Delete all stored usernames, global display names, and server nicknames.<br/>

Examples:<br/>
- `,modset deletenames` - Did not confirm. Shows the help message.<br/>
- `,modset deletenames yes` - Deletes all stored usernames, global display names, and server nicknames.<br/>

**Arguments**<br/>

- `<confirmation>` This will default to false unless specified.<br/>
 - Usage: `,modset deletenames [confirmation=False]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,modset showmessages
Show the current messages for moderation commands.<br/>
 - Usage: `,modset showmessages`


## ,modset deleterepeats
Enable auto-deletion of repeated messages.<br/>

Must be between 2 and 20.<br/>

Set to -1 to disable this feature.<br/>
 - Usage: `,modset deleterepeats [repeats=None]`
 - Checks: `server_only`
Extended Arg Info
> ### repeats: int = None
> ```
> A number without decimal places.
> ```


## ,modset kickmessage
Set the message sent when a user is kicked.<br/>

**Blocks:**<br/>
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)<br/>
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)<br/>

**Variables:**<br/>
- `{user}`: [member that was kicked.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{moderator}`: [modrator that kicked the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{reason}`: reason for the kick.<br/>
- `{server}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)<br/>
 - Usage: `,modset kickmessage <message>`
 - Checks: `server_only`


## ,modset banmessage
Set the message sent when a user is banned.<br/>

**Blocks:**<br/>
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)<br/>
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)<br/>

**Variables:**<br/>
- `{user}`: [member that was banned.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{moderator}`: [modrator that banned the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{reason}`: reason for the ban.<br/>
- `{server}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)<br/>
- `{days}`: number of days of messages deleted.<br/>
 - Usage: `,modset banmessage <message>`
 - Checks: `server_only`


## ,modset unbanmessage
Set the message sent when a user is unbanned.<br/>

**Blocks:**<br/>
- [Assignment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)<br/>
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)<br/>

**Variables:**<br/>
- `{user}`: [member that was tempbanned.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{moderator}`: [modrator that tempbanned the member.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{reason}`: reason for the tempban.<br/>
- `{server}`: [server](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)<br/>
 - Usage: `,modset unbanmessage <message>`
 - Checks: `server_only`


## ,modset showsettings
Show the current server administration settings.<br/>
 - Usage: `,modset showsettings`


# ,kick (Hybrid Command)
Kick a user.<br/>
Examples:<br/>
   - `,kick 428675506947227648 wanted to be kicked.`<br/>
    This will kick the user with ID 428675506947227648 from the server.<br/>
   - `,kick @Twentysix wanted to be kicked.`<br/>
    This will kick Twentysix from the server.<br/>
If a reason is specified, it will be the reason that shows up<br/>
in the audit log.<br/>
 - Usage: `,kick <member> [reason]`
 - Slash Usage: `/kick <member> [reason]`
 - Restricted to: `ADMIN`
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,tempban (Hybrid Command)
Temporarily ban a user from this server.<br/>
`duration` is the amount of time the user should be banned for.<br/>
`days` is the amount of days of messages to cleanup on tempban.<br/>
Examples:<br/>
   - `,tempban @Twentysix Because I say so`<br/>
    This will ban Twentysix for the default amount of time set by an administrator.<br/>
   - `,tempban @Twentysix 15m You need a timeout`<br/>
    This will ban Twentysix for 15 minutes.<br/>
   - `,tempban 428675506947227648 1d2h15m 5 Evil person`<br/>
    This will ban the user with ID 428675506947227648 for 1 day 2 hours 15 minutes and will delete the last 5 days of their messages.<br/>
 - Usage: `,tempban <member> [duration=None] [days=None] [reason]`
 - Slash Usage: `/tempban <member> [duration=None] [days=None] [reason]`
 - Restricted to: `ADMIN`
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
> ### days: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,softban (Hybrid Command)
Kick a user and delete 1 day's worth of their messages.<br/>
 - Usage: `,softban <member> [reason]`
 - Slash Usage: `/softban <member> [reason]`
 - Restricted to: `ADMIN`
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,ban (Hybrid Command)
Ban a user from this server and optionally delete days of messages.<br/>

`days` is the amount of days of messages to cleanup on ban.<br/>

Examples:<br/>
   - `,ban 428675506947227648 7 Continued to spam after told to stop.`<br/>
    This will ban the user with ID 428675506947227648 and it will delete 7 days worth of messages.<br/>
   - `,ban @Twentysix 7 Continued to spam after told to stop.`<br/>
    This will ban Twentysix and it will delete 7 days worth of messages.<br/>

A user ID should be provided if the user is not a member of this server.<br/>
If days is not a number, it's treated as the first word of the reason.<br/>
Minimum 0 days, maximum 7. If not specified, the defaultdays setting will be used instead.<br/>
 - Usage: `,ban <user> [days=None] [reason]`
 - Slash Usage: `/ban <user> [days=None] [reason]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
> ### days: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,unban (Hybrid Command)
Unban a user from this server.<br/>
Requires specifying the target user's ID. To find this, you may either:<br/>
 1. Copy it from the mod log case (if one was created), or<br/>
 2. enable developer mode, go to Bans in this server's settings, right-<br/>
click the user and select 'Copy ID'.<br/>
 - Usage: `,unban <user_id> [reason]`
 - Slash Usage: `/unban <user_id> [reason]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


