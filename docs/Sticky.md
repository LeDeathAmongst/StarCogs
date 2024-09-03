# Sticky Help

### sticky

**Description:** Sticky a message to this channel.

**Usage:** `<@1275521742961508432>sticky`

### sticky toggleheader

**Description:** Toggle the header for stickied messages in this channel.

The header is enabled by default.

**Usage:** `<@1275521742961508432>sticky toggleheader`

### sticky existing

**Description:** Sticky an existing message to this channel.

This will try to sticky the content and embed of the message.
Attachments will not be added to the stickied message.

Stickying messages with multiple embeds may result in unexpected
behaviour, as the bot cannot send multiple rich embeds in a
single message.

**Usage:** `<@1275521742961508432>sticky existing`

### unsticky

**Description:** Remove the sticky message from this channel.

Deleting the sticky message will also unsticky it.

Do `[p]unsticky yes` to skip the confirmation prompt.

**Usage:** `<@1275521742961508432>unsticky`

