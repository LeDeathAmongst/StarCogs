# ThreadOpener Help

### threadopener

**Description:** Manage ThreadOpener settings.

**Usage:** `<@1275521742961508432>threadopener`

### threadopener allowbots

**Description:** Allow/Disallow bots from auto-creating threads using Thread Opener.

**Usage:** `<@1275521742961508432>threadopener allowbots`

### threadopener toggle

**Description:** Toggle ThreadOpener enable or disable.

**Usage:** `<@1275521742961508432>threadopener toggle`

### threadopener name

**Description:** Change the default thread name for ThreadOpener.

(Supports TagScript)

**Attributes:**
- `{server}`: [Your guild/server.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)
- `{author}`: [Author of the thread.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{created}`: Formatted time string of when the thread was created.
- `{counter}`: Counter of how created thread. (Everytime a thread is created using ThreadOpener the counter goes up by 1.)

**Example:**
- `[p]threadopener name {author(name)}:{created}:{counter}`
- `[p]threadopener name {author(name)}-{counter}`

**Usage:** `<@1275521742961508432>threadopener name`

### threadopener message

**Description:** Manage thread opener notifications when they are opened.

**Usage:** `<@1275521742961508432>threadopener message`

### threadopener message buttons

**Description:** Toggle buttons from the thread opener notification message. (Enabled by default.)

**Usage:** `<@1275521742961508432>threadopener message buttons`

### threadopener message set

**Description:** Change the thread opener notification message.

(Supports Tagscript)

**Blocks:**
- [Assugnment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)
- [If Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#if-block)
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)
- [Command Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#command-block)

**Variable:**
- `{server}`: [Your guild/server.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)
- `{author}`: [Author of the message.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)
- `{color}`: [botname]'s default color.

**Example:**
```
{embed(description):Welcome to the thread.}
{embed(thumbnail):{member(avatar)}}
{embed(color):{color}}
```

**Usage:** `<@1275521742961508432>threadopener message set`

### threadopener message toggle

**Description:** Toggle the thread opener notification message.

**Usage:** `<@1275521742961508432>threadopener message toggle`

### threadopener archive

**Description:** Change the archive duration of threads.

- Use `0` to disable auto archive duration of threads.

**Usage:** `<@1275521742961508432>threadopener archive`

### threadopener slowmode

**Description:** Change the slowmode of threads.

- Use `0` to dsiable slowmode delay in threads.

**Usage:** `<@1275521742961508432>threadopener slowmode`

### threadopener blacklist

**Description:** Base command for Thread Opener blacklists.

**Commands:**
- `[p]threadopener blacklist users <add_or_remove> <users>`
- `[p]threadopener blacklist roles <add_or_remove> <roles>`

**Usage:** `<@1275521742961508432>threadopener blacklist`

### threadopener blacklist users

**Description:** Add or remove users for your guild's blacklist.

**Arguments:**
- `<add_or_remove>` should be either `add` to add users or `remove` to remove users.
- `<users>` users to be added.

**Example:**
- `[p]threadopener blacklist users add @inthedark.org`
- `[p]threadopener blacklist users remove @inthedark.org`

**Note:**
- You can add or remove multiple users at once.
- You can also use user ID instead of mentioning the user.

**Usage:** `<@1275521742961508432>threadopener blacklist users`

### threadopener blacklist roles

**Description:** Add or remove roles for your guild's blacklist.

**Arguments:**
- `<add_or_remove>` should be either `add` to add roles or `remove` to remove roles.
- `<users>` roles to be added.

**Example:**
- `[p]threadopener blacklist roles add @members`
- `[p]threadopener blacklist roles remove @members`

**Note:**
- You can add or remove multiple roles at once.
- You can also use role ID instead of mentioning the role.

**Usage:** `<@1275521742961508432>threadopener blacklist roles`

### threadopener blacklist list

**Description:** View the blacklist.

**Arguments:**
` `<users_or_roles>` should be either ``users`` to view the user blacklist
    or `roles` to view the role blacklist.

**Usage:** `<@1275521742961508432>threadopener blacklist list`

### threadopener showsettings

**Description:** Show ThreadOpener settings.

**Usage:** `<@1275521742961508432>threadopener showsettings`

### threadopener channels

**Description:** Add or remove channels for your guild.

**Arguments:**
- `<add_or_remove>` should be either `add` to add channels or `remove` to remove channels.
- `<channels>` channels to be added.

**Example:**
- `[p]threadopener channels add #channel`
- `[p]threadopener channels remove #channel`

**Note:**
- You can add or remove multiple channels at once.
- You can also use channel ID instead of mentioning the channel.

**Usage:** `<@1275521742961508432>threadopener channels`

