# NoDMs Help

### nodms

**Description:** NoDMs configuration commands.

**Usage:** `<@1275521742961508432>nodms`

### nodms message

**Description:** NoDMs message trigger configuration commands.

**Usage:** `<@1275521742961508432>nodms message`

### nodms message toggle

**Description:** Toggle whether to send messages or not.

**Arguments**:
- `<true_or_false>` - enable/disable message triggers for nodms.

**Usage:** `<@1275521742961508432>nodms message toggle`

### nodms message set

**Description:** Configure the nodms message trigger.

**Arguments**:
- `<type>    `: whether to configure message for messages, commands or clear
the already configured type, using clear will reset both the messages
trigger and commands trigger to default.
- `<argument>`: the message to be sent by [botname], if argument is not
privided the type is reset to default instead.

**Blocks**:
`embed` - [Embed to be sent for the trigger message](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)

**Variables**:
- `{color}  `: [botname]'s default embed color (no parameters).
    - usage: `{color}`
- `{bot}    `: custom block for [botname] variables.
    - parameters: `id`, `name`, `nick`, `mention`, `avatar`, `created_at` or
    `verified`.
    - aliases: `{[botname]}`
    - usage: `{command(<parameter>)}`
- `{user}   `: the user to dm [botname].
    - parameters: `id`, `created_at`, `timestamp`, `name`, `nick`,  `avatar`
    or `mention` (if no parameter is used, defaults to `name`).
    - aliases: `{author}`
    - usage: `{user(<parameter>)}`
- `{channel}`: [botname]'s dm channel with the user/author.
    - parameters: `id`, `created_at` or `jump_url` (if no parameter is used,
    defaults to `jump_url`).
    - aliases: `{dm}`
    - usage: `{channel(<parameter>)}`
- `{command}`: the command that was blocked, this block is only available
    when the "commands" type is used.
    - parameters: `name`, `cog_name`, `description`, `aliases` or
    `qualified_name` (if no parameter is used, defaults to `qualified_name`).
    - usage: `{command(<parameter>)}`

**Examples**:
- `[p]nodms message set commands {embed(description):You're not allowed to use the {command(name)} command in {bot(name)}'s dms.}`
- `[p]nodms message set message {embed(description):You're not allowed to send messages in {bot(name)}'s dms.}`
- `[p]nodms message set commands You're not allowed to use the {command(name)} command in {bot(name)}'s dms.`
- `[p]nodms message set message You're not allowed to send messages in {bot(name)}'s dms.`

**Usage:** `<@1275521742961508432>nodms message set`

### nodms whitelist

**Description:** Configure the whitelist for nodms.

Warning: When the whitelist is in use, [botname] will ignore all
users/commands not in the list.

View the list using the `[p]nodms whitelist list <users/commands>` command,
and/or make sure to remove everyone from the list to disable the whitelist.

**Usage:** `<@1275521742961508432>nodms whitelist`

### nodms whitelist commands

**Description:** Add or remove commands from the whitelist.

**Arguments**:
- `<add_or_remove>`: add or remove commands from the whitelist.
- `<commands>     `: list of command names to be added/removed.

**Usage:** `<@1275521742961508432>nodms whitelist commands`

### nodms whitelist list

**Description:** View the whitelisted user/command list.

**Arguments**:
- `<option>`: whether to view the users or commands list.

**Usage:** `<@1275521742961508432>nodms whitelist list`

### nodms whitelist users

**Description:** Add or remove users from the whitelist.

**Arguments**:
- `<add_or_remove>`: add or remove users from the whitelist.
- `<users>        `: list of users to be added/removed.

**Usage:** `<@1275521742961508432>nodms whitelist users`

### nodms settings

**Description:** View the NoDMs configuration settings.

**Usage:** `<@1275521742961508432>nodms settings`

### nodms blacklist

**Description:** Configure the blacklist for nodms.

View the list using the `[p]nodms blacklist list <users/commands>` command,
and/or make sure to remove everyone from the list to disable the blacklist.

**Usage:** `<@1275521742961508432>nodms blacklist`

### nodms blacklist users

**Description:** Add or remove users from the blacklist.

**Arguments**:
- `<add_or_remove>`: add or remove users from the blacklist.
- `<users>        `: list of users to be added/removed.

**Usage:** `<@1275521742961508432>nodms blacklist users`

### nodms blacklist commands

**Description:** Add or remove commands from the blacklist.

**Arguments**:
- `<add_or_remove>`: add or remove commands from the blacklist.
- `<commands>     `: list of command names to be added/removed.

**Usage:** `<@1275521742961508432>nodms blacklist commands`

### nodms blacklist list

**Description:** View the blacklisted user/command list.

**Arguments**:
- `<option>`: whether to view the users or commands list.

**Usage:** `<@1275521742961508432>nodms blacklist list`

### nodms toggle

**Description:** Toggle whether to ignore DM messages and/or commands.

Enabling the `<type>` argument `all` and `messages`
will cause botname] to delete messages everytime someone
DMs [botname]. Unwanted behaviour may occur if
people try to spam the bot's DMs while these types
are enabled.

Message triggers are enabled by default, to disable
them use the `[p]nodms message toggle <true_or_false>`
command.

**Arguments**:
- `<true_or_false>` - enable/disable nodms for [botname].
- `<type>` - whether to enable messages, commands or (both) all.

**Usage:** `<@1275521742961508432>nodms toggle`

