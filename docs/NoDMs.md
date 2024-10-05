Restrict messages and/or commands in DMs.<br/><br/>Restrict messages or any commands in DMs from others, with various<br/>configuration settings.

# <@1275521742961508432>nodms
NoDMs configuration commands.<br/>
 - Usage: `<@1275521742961508432>nodms`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>nodms message
NoDMs message trigger configuration commands.<br/>
 - Usage: `<@1275521742961508432>nodms message`
### <@1275521742961508432>nodms message toggle
Toggle whether to send messages or not.<br/>

**Arguments**:<br/>
- `<true_or_false>` - enable/disable message triggers for nodms.<br/>
 - Usage: `<@1275521742961508432>nodms message toggle <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### <@1275521742961508432>nodms message set
Configure the nodms message trigger.<br/>

**Arguments**:<br/>
- `<type>    `: whether to configure message for messages, commands or clear<br/>
the already configured type, using clear will reset both the messages<br/>
trigger and commands trigger to default.<br/>
- `<argument>`: the message to be sent by Starfire, if argument is not<br/>
privided the type is reset to default instead.<br/>

**Blocks**:<br/>
`embed` - [Embed to be sent for the trigger message](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)<br/>

**Variables**:<br/>
- `{color}  `: Starfire's default embed color (no parameters).<br/>
    - usage: `{color}`<br/>
- `{bot}    `: custom block for Starfire variables.<br/>
    - parameters: `id`, `name`, `nick`, `mention`, `avatar`, `created_at` or<br/>
    `verified`.<br/>
    - aliases: `{Starfire}`<br/>
    - usage: `{command(<parameter>)}`<br/>
- `{user}   `: the user to dm Starfire.<br/>
    - parameters: `id`, `created_at`, `timestamp`, `name`, `nick`,  `avatar`<br/>
    or `mention` (if no parameter is used, defaults to `name`).<br/>
    - aliases: `{author}`<br/>
    - usage: `{user(<parameter>)}`<br/>
- `{channel}`: Starfire's dm channel with the user/author.<br/>
    - parameters: `id`, `created_at` or `jump_url` (if no parameter is used,<br/>
    defaults to `jump_url`).<br/>
    - aliases: `{dm}`<br/>
    - usage: `{channel(<parameter>)}`<br/>
- `{command}`: the command that was blocked, this block is only available<br/>
    when the "commands" type is used.<br/>
    - parameters: `name`, `cog_name`, `description`, `aliases` or<br/>
    `qualified_name` (if no parameter is used, defaults to `qualified_name`).<br/>
    - usage: `{command(<parameter>)}`<br/>

**Examples**:<br/>
- `<@1275521742961508432>nodms message set commands {embed(description):You're not allowed to use the {command(name)} command in {bot(name)}'s dms.}`<br/>
- `<@1275521742961508432>nodms message set message {embed(description):You're not allowed to send messages in {bot(name)}'s dms.}`<br/>
- `<@1275521742961508432>nodms message set commands You're not allowed to use the {command(name)} command in {bot(name)}'s dms.`<br/>
- `<@1275521742961508432>nodms message set message You're not allowed to send messages in {bot(name)}'s dms.`<br/>
 - Usage: `<@1275521742961508432>nodms message set <type> [argument]`
 - Aliases: `configure`
## <@1275521742961508432>nodms settings
View the NoDMs configuration settings.<br/>
 - Usage: `<@1275521742961508432>nodms settings`
 - Aliases: `showsettings, show, and ss`
## <@1275521742961508432>nodms blacklist
Configure the blacklist for nodms.<br/>

View the list using the `<@1275521742961508432>nodms blacklist list <users/commands>` command,<br/>
and/or make sure to remove everyone from the list to disable the blacklist.<br/>
 - Usage: `<@1275521742961508432>nodms blacklist`
 - Aliases: `bl and blocklist`
### <@1275521742961508432>nodms blacklist commands
Add or remove commands from the blacklist.<br/>

**Arguments**:<br/>
- `<add_or_remove>`: add or remove commands from the blacklist.<br/>
- `<commands>     `: list of command names to be added/removed.<br/>
 - Usage: `<@1275521742961508432>nodms blacklist commands <add_or_remove> <commands>`
 - Aliases: `command`
### <@1275521742961508432>nodms blacklist users
Add or remove users from the blacklist.<br/>

**Arguments**:<br/>
- `<add_or_remove>`: add or remove users from the blacklist.<br/>
- `<users>        `: list of users to be added/removed.<br/>
 - Usage: `<@1275521742961508432>nodms blacklist users <add_or_remove> <users>`
 - Aliases: `user`
Extended Arg Info
> ### *users: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
### <@1275521742961508432>nodms blacklist list
View the blacklisted user/command list.<br/>

**Arguments**:<br/>
- `<option>`: whether to view the users or commands list.<br/>
 - Usage: `<@1275521742961508432>nodms blacklist list <option>`
## <@1275521742961508432>nodms toggle
Toggle whether to ignore DM messages and/or commands.<br/>

Enabling the `<type>` argument `all` and `messages`<br/>
will cause botname] to delete messages everytime someone<br/>
DMs Starfire. Unwanted behaviour may occur if<br/>
people try to spam the bot's DMs while these types<br/>
are enabled.<br/>

Message triggers are enabled by default, to disable<br/>
them use the `<@1275521742961508432>nodms message toggle <true_or_false>`<br/>
command.<br/>

**Arguments**:<br/>
- `<true_or_false>` - enable/disable nodms for Starfire.<br/>
- `<type>` - whether to enable messages, commands or (both) all.<br/>
 - Usage: `<@1275521742961508432>nodms toggle <true_or_false> <type>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>nodms whitelist
Configure the whitelist for nodms.<br/>

Warning: When the whitelist is in use, Starfire will ignore all<br/>
users/commands not in the list.<br/>

View the list using the `<@1275521742961508432>nodms whitelist list <users/commands>` command,<br/>
and/or make sure to remove everyone from the list to disable the whitelist.<br/>
 - Usage: `<@1275521742961508432>nodms whitelist`
 - Aliases: `wl and allowlist`
### <@1275521742961508432>nodms whitelist users
Add or remove users from the whitelist.<br/>

**Arguments**:<br/>
- `<add_or_remove>`: add or remove users from the whitelist.<br/>
- `<users>        `: list of users to be added/removed.<br/>
 - Usage: `<@1275521742961508432>nodms whitelist users <add_or_remove> <users>`
 - Aliases: `user`
Extended Arg Info
> ### *users: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
### <@1275521742961508432>nodms whitelist list
View the whitelisted user/command list.<br/>

**Arguments**:<br/>
- `<option>`: whether to view the users or commands list.<br/>
 - Usage: `<@1275521742961508432>nodms whitelist list <option>`
### <@1275521742961508432>nodms whitelist commands
Add or remove commands from the whitelist.<br/>

**Arguments**:<br/>
- `<add_or_remove>`: add or remove commands from the whitelist.<br/>
- `<commands>     `: list of command names to be added/removed.<br/>
 - Usage: `<@1275521742961508432>nodms whitelist commands <add_or_remove> <commands>`
 - Aliases: `command`
