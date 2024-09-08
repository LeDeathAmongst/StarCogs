# Purge Help

### purge

**Description:** Removes messages that meet a criteria.

Messages older than 14 days cannot be deleted.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Example:**
- `[p]purge 10`
- `[p]purge 2000`

**Usage:** `<@1275521742961508432>purge`

### purge emoji

**Description:** Removes all messages containing custom emoji.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge emoji 10`
- `[p]purge emoji 200`

**Usage:** `<@1275521742961508432>purge emoji`

### purge mine

**Description:** Removes my messages from the channel.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge mine 10`
- `[p]purge mine 2000`

**Usage:** `<@1275521742961508432>purge mine`

### purge between

**Description:** Delete the messages between Message One and Message Two, providing the messages IDs.

The first message ID should be the older message and the second one the newer.

**Arguments:**
- `<one>` The id of the message to cleanup after. This message won't be deleted.
- `<two>` The id of the message to cleanup before. This message won't be deleted.
- `<delete_pinned>` Whether to delete pinned messages or not. Defaults to False.

**Example:**
- `[p]cleanup between 123456789123456789 987654321987654321`

**Usage:** `<@1275521742961508432>purge between`

### purge links

**Description:** Removes all messages containing a link.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge links 10`
- `[p]purge links 2000`

**Usage:** `<@1275521742961508432>purge links`

### purge custom

**Description:** Remove messages that meet a criteria from the flags.

The following flags are valid.

`user:` Remove messages from the given user.
`contains:` Remove messages that contain a substring.
`prefix:` Remove messages that start with a string.
`suffix:` Remove messages that end with a string.
`after:` Search for messages that come after this message ID.
`before:` Search for messages that come before this message ID.
`bot: yes` Remove messages from bots. (not webhooks!)
`webhooks: yes` Remove messages from webhooks.
`embeds: yes` Remove messages that have embeds.
`files: yes` Remove messages that have attachments.
`emoji: yes` Remove messages that have custom emoji.
`reactions: yes` Remove messages that have reactions.
`require: any or all` Whether any or all flags should be met before deleting messages.

**Usage:** `<@1275521742961508432>purge custom`

### purge user

**Description:** Removes all messages by the member.

**Arguments:**
- `<member>`: The user to delete messages for.
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge user @member`
- `[p]purge user @member 2000`

**Usage:** `<@1275521742961508432>purge user`

### purge images

**Description:** Removes messages that have embeds or attachments.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge images 10`
- `[p]purge images 2000`

**Usage:** `<@1275521742961508432>purge images`

### purge bot

**Description:** Removes bot messages, optionally takes a prefix argument.

**Arguments:**
- `<prefix>`: The bot's prefix you want to remove.
- `<number`: The number of messages you want to delete. (Defaults to 100)
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge bot`
- `[p]purge bot ? 2000`

**Usage:** `<@1275521742961508432>purge bot`

### purge embeds

**Description:** Removes messages that have embeds in them.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge embeds 10`
- `[p]purge embeds 2000`

**Usage:** `<@1275521742961508432>purge embeds`

### purge self

**Description:** Removes your messages from the channel.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge self 10`
- `[p]purge self 2000`

**Usage:** `<@1275521742961508432>purge self`

### purge contains

**Description:** Removes all messages containing a text.
The text must be at least 3 characters long.

**Arguments:**
- `<text>`: the text to be removed.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge contains hi`
- `[p]purge contains bye`

**Usage:** `<@1275521742961508432>purge contains`

### purge reactions

**Description:** Removes all reactions from messages that have them.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge reactions 10`
- `[p]purge reactions 200`

**Usage:** `<@1275521742961508432>purge reactions`

### purge after

**Description:** Delete all messages after a specified message.

To get a message id, enable developer mode in Discord's
settings, 'appearance' tab. Then right click a message
and copy its id.
Replying to a message will cleanup all messages after it.

**Arguments:**
- `<message_id>` The id of the message to cleanup after. This message won't be deleted.
- `<delete_pinned>` Whether to delete pinned messages or not. Defaults to False

**Usage:** `<@1275521742961508432>purge after`

### purge before

**Description:** Deletes X messages before the specified message.

To get a message id, enable developer mode in Discord's
settings, 'appearance' tab. Then right click a message
and copy its id.
Replying to a message will cleanup all messages before it.

**Arguments:**
- `<message_id>` The id of the message to cleanup before. This message won't be deleted.
- `<number>` The max number of messages to cleanup. Must be a positive integer.
- `<delete_pinned>` Whether to delete pinned messages or not. Defaults to False

**Usage:** `<@1275521742961508432>purge before`

### purge duplicates

**Description:** Deletes duplicate messages in the channel from the last X messages and keeps only one copy.

**Arguments:**
- `<number>` The number of messages to check for duplicates. Must be a positive integer.

**Usage:** `<@1275521742961508432>purge duplicates`

### purge regex

**Description:** Removes messages that matches the regex pattern.

**Arguments:**
- `<pattern>`: The regex pattern to match.
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge regex (?i)(h(?:appy) 1`
- `[p]purge regex (?i)(h(?:appy) 10`

**Usage:** `<@1275521742961508432>purge regex`

### purge files

**Description:** Removes messages that have attachments in them.

**Arguments:**
- `<number`: The number of messages you want to delete.
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)

**Examples:**
- `[p]purge files 10`
- `[p]purge files 2000`

**Usage:** `<@1275521742961508432>purge files`

