# SimpleSanction Help

### setsimplesanction

**Description:** Configure SimpleSanction for your server.

**Usage:** `<@1275521742961508432>setsimplesanction`

### setsimplesanction modalconfig

**Description:** Set all settings for the cog with a Discord Modal.

**Usage:** `<@1275521742961508432>setsimplesanction modalconfig`

### setsimplesanction resetsetting

**Description:** Reset a setting.

**Usage:** `<@1275521742961508432>setsimplesanction resetsetting`

### setsimplesanction usewarnsystem

**Description:** Use WarnSystem by Laggron for the sanctions.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setsimplesanction usewarnsystem`

### setsimplesanction thumbnail

**Description:** Set the embed thumbnail.

Default value: `https://i.imgur.com/Bl62rGd.png`
Dev: `<class 'str'>`

**Usage:** `<@1275521742961508432>setsimplesanction thumbnail`

### setsimplesanction finishmessage

**Description:** Send an embed after a sanction command execution.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setsimplesanction finishmessage`

### setsimplesanction showauthor

**Description:** Show the command author in embeds.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setsimplesanction showauthor`

### setsimplesanction reasonrequired

**Description:** Require a reason for each sanction (except userinfo).

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setsimplesanction reasonrequired`

### setsimplesanction actionconfirmation

**Description:** Require a confirmation for each sanction (except userinfo).

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setsimplesanction actionconfirmation`

### setsimplesanction showsettings

**Description:** Show all settings for the cog with defaults and values.

**Usage:** `<@1275521742961508432>setsimplesanction showsettings`

### sanction

**Description:** Sanction a member quickly and easily.

All arguments are optional and will be requested during the action if necessary. You must specify the parameters in this order.

Parameters:
- `user`: Server member.                            Who is the user concerned?
- `confirmation`: True or False.                Confirm the action directly. (Default is the recorded value)
- `show_author`: True or False.                 Do you want the bot to show in its embeds who is the author of the command/sanction? (Default is the recorded value)
- `finish_message`: True or False.              Do you want the bot to show an embed just before the action summarising the action and giving the sanctioned user and the reason? (Default is the recorded value)
- `fake_action`: True or False.             Do you want the command to do everything as usual, but (unintentionally) forget to execute the action?
- `duration`: Duration. (5d, 8h, 1m...) If you choose a TempBan, TempMute or TempMuteChanne, this value will be used for the duration of that action.
- `reason`: Text.                                       The reason for this action. (`not` to not specify one, unless the reason has been made falcutative in the parameters)

Short version: [p]sanction
Long version:  [p]sanction 10 @member true true true true true true 3d Spam.

**Usage:** `<@1275521742961508432>sanction`

### sanction 09

**Description:**  - ⏳ TempMute a member in all channels, including voice channels.

You can set a timed mute by providing a valid time before the reason.

Examples:
- `[p]sanction 9 @member 30m not`: 30 minutes mute for no reason.
- `[p]sanction 9 @member 5h Spam`: 5 hours mute for the reason "Spam".
- `[p]sanction 9 @member 3d Advertising`: 3 days mute for the reason "Advertising".

**Usage:** `<@1275521742961508432>sanction 09`

### sanction 04

**Description:**  - 🔂 SoftBan a member from this server.

This means that the user will be banned and immediately unbanned, so it will purge their messages in a period, in all channels.

Examples:
- `[p]sanction 4 @member not`: SoftBan for no reason
- `[p]sanction 4 @member Insults`: SoftBan for the reason "Insults"
- `[p]sanction 4 012345678987654321 Advertising`: SoftBan the user with the ID provided.

**Usage:** `<@1275521742961508432>sanction 04`

### sanction 00

**Description:** - Sanction a member quickly and easily.

Examples:
- `[p]sanction 0 @member`
- `[p]sanction 0 @member What are these roles?`
- `[p]sanction 0 012345678987654321`

**Usage:** `<@1275521742961508432>sanction 00`

### sanction 06

**Description:**  - 👢 Kick a member from this server.

Examples:
- `[p]sanction 6 @member not`: Kick for no reason.
- `[p]sanction 6 @member Insults`: Kick for the reason "Insults".
- `[p]sanction 6 012345678987654321 Advertising`: Kick the user with the ID provided.

**Usage:** `<@1275521742961508432>sanction 06`

### sanction 08

**Description:**  - 👊 Mute a member in this channel.

Examples:
- `[p]sanction 8 @member not`: Infinite mute for no reason.
- `[p]sanction 8 @member Spam`: Infinite mute for the reason "Spam".
- `[p]sanction 8 @member Advertising`: Infinite mute for the reason "Advertising".

**Usage:** `<@1275521742961508432>sanction 08`

### sanction 10

**Description:**  - ⌛ TempMute a member in this channel.

You can set a timed mute by providing a valid time before the reason.

Examples:
- `[p]sanction 10 @member 30m not`: 30 minutes mute for no reason.
- `[p]sanction 10 @member 5h Spam`: 5 hours mute for the reason "Spam".
- `[p]sanction 10 @member 3d Advertising`: 3 days mute for the reason "Advertising".

**Usage:** `<@1275521742961508432>sanction 10`

### sanction 03

**Description:**  - 🔨 Ban a member from this server.

It won't delete messages by default.

Examples:
- `[p]sanction 3 @member not`: Ban for no reason.
- `[p]sanction 3 @member Insults`: Ban for the reason "Insults".
- `[p]sanction 3 012345678987654321 Advertising`: Ban the user with the ID provided.

**Usage:** `<@1275521742961508432>sanction 03`

### sanction 05

**Description:**  - 💨 TempBan a member from this server.

It won't delete messages by default.
If you want to perform a temporary ban, provide the time before the reason.

Examples:
- `[p]sanction 5 @member not`: Ban for no reason.
- `[p]sanction 5 @member 7d Insults`: 7 days ban for the reason "Insults".
- `[p]sanction 5 012345678987654321 Advertising`: Ban the user with the ID provided.

**Usage:** `<@1275521742961508432>sanction 05`

### sanction 02

**Description:**  - ⚠️ Add a simple warning on a member.

Examples:
- `[p]sanction 2 @member not`: Warn for no reason.
- `[p]sanction 2 @member Insults`: Warn for the reason "Insults".
- `[p]sanction 2 012345678987654321 Advertising`: Warn the user with the ID provided.

**Usage:** `<@1275521742961508432>sanction 02`

### sanction 07

**Description:**  - 🔇 Mute a member in all channels, including voice channels.

Examples:
- `[p]sanction 7 @member not`: Infinite mute for no reason.
- `[p]sanction 7 @member Spam`:Infinite  mute for the reason "Spam".
- `[p]sanction 7 @member Advertising`: Infinite mute for the reason "Advertising".

**Usage:** `<@1275521742961508432>sanction 07`

### sanction 01

**Description:**  - ℹ️ Show informations about a member.

Examples:
- `[p]sanction 1 @member`: UserInfo for no reason.
- `[p]sanction 1 @member What are these roles?`: UserInfo for the reason "What are these roles?".
- `[p]sanction 1 012345678987654321`: UserInfo with the ID provided.

**Usage:** `<@1275521742961508432>sanction 01`

