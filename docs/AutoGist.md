# AutoGist Help

### autogistset

**Description:** AutoGist settings.

**Usage:** `<@1275521742961508432>autogistset`

### autogistset listoverridden

**Description:** List guild channels that don't use the default setting.

**Usage:** `<@1275521742961508432>autogistset listoverridden`

### autogistset listentohumans

**Description:** Make AutoGist listen to messages from humans in this server.

**Usage:** `<@1275521742961508432>autogistset listentohumans`

### autogistset listentoself

**Description:** Make the bot listen to messages from itself in this server.

See also: `[p]autogistset listentobots` command,
that makes the bot listen to other bots.

**Usage:** `<@1275521742961508432>autogistset listentoself`

### autogistset channeldefault

**Description:** Set whether AutoGist should by default listen to channels.

If default is set to True, bot will only listen to channels it was explicitly
allowed to listen to with `[p]autogistset allowchannels` command.

If default is set to False, bot will listen to all channels except the ones
it was explicitly blocked from listening to
with `[p]autogistset denychannels` command.

By default, guilds will not listen to any channel.
Use `[p]autogist channeldefault` without a setting to see current mode.

**Usage:** `<@1275521742961508432>autogistset channeldefault`

### autogistset listentobots

**Description:** Make AutoGist listen to messages from other bots in this server.

NOTE: To make bot listen to messages from itself,
you need to use `[p]autogistset listentoself` command.

**Usage:** `<@1275521742961508432>autogistset listentobots`

### autogistset token

**Description:** Instructions to set the GitHub API token.

**Usage:** `<@1275521742961508432>autogistset token`

### autogistset allowchannels

**Description:** Allow the bot to listen to the given channels.

**Usage:** `<@1275521742961508432>autogistset allowchannels`

### autogistset blockchannels

**Description:** Block the bot from listening to the given channels.

**Usage:** `<@1275521742961508432>autogistset blockchannels`

### autogistset extensions

**Description:** Settings for file extensions
that are required for AutoGist to upload file to Gist.

By default AutoGist will look for files with `.txt` and `.log` extensions.

**Usage:** `<@1275521742961508432>autogistset extensions`

### autogistset extensions remove

**Description:** Remove file extensions from the list.

Example:
`[p]autogist extensions remove txt .log` - removes `.txt` and `.log` extensions.

**Usage:** `<@1275521742961508432>autogistset extensions remove`

### autogistset extensions list

**Description:** List file extensions that are required for AutoGist to upload file to Gist.

**Usage:** `<@1275521742961508432>autogistset extensions list`

### autogistset extensions add

**Description:** Add file extensions to the list.

Example:
`[p]autogist extensions add txt .log` - adds `.txt` and `.log` extensions.

**Usage:** `<@1275521742961508432>autogistset extensions add`

