# AutoDocs Help

This is a helpful description of the cog.

### makedocs

**Description:** Create a Markdown docs page for a cog and send to discord

**Arguments**
`cog_name:            `(str) The name of the cog you want to make docs for (Case Sensitive)
`replace_prefix:      `(bool) If True, replaces the `prefix` placeholder with the bots prefix
`replace_botname:     `(bool) If True, replaces the `botname` placeholder with the bots name
`extended_info:       `(bool) If True, include extra info like converters and their docstrings
`include_hidden:      `(bool) If True, includes hidden commands
`include_help:        `(bool) If True, includes the cog help text at the top of the docs
`max_privilege_level: `(str) Hide commands above specified privilege level
`min_privilege_level: `(str) Hide commands below specified privilege level
- (user, mod, admin, guildowner, botowner)
`csv_export:          `(bool) Include a csv with each command isolated per row for use as embeddings

**Note** If `all` is specified for cog_name, all currently loaded non-core cogs will have docs generated for
them and sent in a zip file

**Usage:** `<@1275521742961508432>makedocs`

### searchcmd

**Description:** Search for a specific command and get its documentation.

**Arguments**
`command_name: `(str) The name of the command you want to search for.

**Usage:** `<@1275521742961508432>searchcmd`

