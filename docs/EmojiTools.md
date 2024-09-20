# EmojiTools Help

### emojitools

**Description:** Various tools for managing custom emojis in servers.

`[p]emojitools add` has various tools to add emojis to the current server.
`[p]emojitools delete` lets you remove emojis from the server.
`[p]emojitools tozip` returns an instant `.zip` archive of emojis (w/o saving a folder permanently).
`[p]emojitools save` allows you to save emojis to folders **in the cog data path**: this requires storage!

**Usage:** `<@1275521742961508432>emojitools`

### emojitools delete

**Description:** Delete Server Custom Emojis

**Usage:** `<@1275521742961508432>emojitools delete`

### emojitools delete all

**Description:** Delete all specific custom emojis from the server.

**Usage:** `<@1275521742961508432>emojitools delete all`

### emojitools delete emojis

**Description:** Delete custom emojis from the server.

**Usage:** `<@1275521742961508432>emojitools delete emojis`

### emojitools tozip

**Description:** Get a `.zip` Archive of Emojis

**Usage:** `<@1275521742961508432>emojitools tozip`

### emojitools tozip emojis

**Description:** Get a `.zip` archive of the provided emojis.

The returned `.zip` archive can be used for the `[p]emojitools add fromzip` command.

**Usage:** `<@1275521742961508432>emojitools tozip emojis`

### emojitools tozip server

**Description:** Get a `.zip` archive of all custom emojis in the server.

The returned `.zip` archive can be used for the `[p]emojitools add fromzip` command.

**Usage:** `<@1275521742961508432>emojitools tozip server`

### emojitools save

**Description:** Save Custom Emojis to Folders

**IMPORTANT**: this **will** save folders to the cog data path, requiring storage in the machine the bot is hosted on.
The folders will be accessible to admin across all servers with access to this cog.
The other `EmojiTools` features that do **NOT** require storage, so disable this command group if you wish.
For large public bots, it is highly recommended to restrict usage of or disable this command group.

**Usage:** `<@1275521742961508432>emojitools save`

### emojitools save server

**Description:** Save to a folder all custom emojis from this server (folder name defaults to server name).

**Usage:** `<@1275521742961508432>emojitools save server`

### emojitools save emojis

**Description:** Save to a folder the specified custom emojis (can be from any server).

**Usage:** `<@1275521742961508432>emojitools save emojis`

### emojitools save remove

**Description:** Remove an EmojiTools folder.

**Usage:** `<@1275521742961508432>emojitools save remove`

### emojitools save folders

**Description:** List all your saved EmojiTools folders.

**Usage:** `<@1275521742961508432>emojitools save folders`

### emojitools save getzip

**Description:** Zip and upload an EmojiTools folder.

**Usage:** `<@1275521742961508432>emojitools save getzip`

### emojitools edit

**Description:** Edit Custom Emojis in the Server

**Usage:** `<@1275521742961508432>emojitools edit`

### emojitools edit name

**Description:** Edit the name of a custom emoji from this server.

**Usage:** `<@1275521742961508432>emojitools edit name`

### emojitools edit roles

**Description:** Edit the roles to which the usage of a custom emoji from this server is restricted.

**Usage:** `<@1275521742961508432>emojitools edit roles`

### emojitools add

**Description:** Add Custom Emojis to Server

**Usage:** `<@1275521742961508432>emojitools add`

### emojitools add emojis

**Description:** Add some emojis to this server.

**Usage:** `<@1275521742961508432>emojitools add emojis`

### emojitools add fromzip

**Description:** Add some emojis to this server from a provided .zip archive.

The `.zip` archive should extract to a folder, which contains files in the formats `.png`, `.jpg`, or `.gif`.
You can also use the `[p]emojitools tozip` command to get a zip archive, extract it, remove unnecessary emojis, then re-zip and upload.

**Usage:** `<@1275521742961508432>emojitools add fromzip`

### emojitools add fromimage

**Description:** Add an emoji to this server from a provided image.

The attached image should be in one of the following formats: `.png`, `.jpg`, or `.gif`.

**Usage:** `<@1275521742961508432>emojitools add fromimage`

### emojitools add allreactionsfrom

**Description:** Add emojis to this server from all reactions in a message.

**Usage:** `<@1275521742961508432>emojitools add allreactionsfrom`

### emojitools add emoji

**Description:** Add an emoji to this server (leave `name` blank to use the emoji's original name).

**Usage:** `<@1275521742961508432>emojitools add emoji`

### emojitools add fromreaction

**Description:** Add an emoji to this server from a specific reaction on a message.

**Usage:** `<@1275521742961508432>emojitools add fromreaction`

### emojitools info

**Description:** Get info about a custom emoji from this server.

**Usage:** `<@1275521742961508432>emojitools info`

