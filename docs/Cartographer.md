# Cartographer Help

### cartographer

**Description:** Open the Backup/Restore menu

This cog can backup & restore the following:
- Bans (including reason)
- Categories (permissions/order)
- Text channels (permissions/order)
- Voice channels (permissions/order)
- Forum channels  (permissions/order)[Not forum posts]
- Roles (permissions/color/name/icon and what members they're assigned to)
- Emojis (name/roles, Very slow and rate limit heavy)
- Stickers (name/description, Very slow and rate limit heavy)
- Members (roles and nicknames)
- Messages (Optional, can be disabled)
- Server icon/banner/splash/discovery splash/description/name
- All server verification/security settings

**Usage:** `<@1275521742961508432>cartographer`

### cartographerset

**Description:** Backup & Restore Tools

**Usage:** `<@1275521742961508432>cartographerset`

### cartographerset backupmembers

**Description:** Toggle backing up members

⚠️**Warning**⚠️
Restoring the roles of all members can be slow for large servers.

**Usage:** `<@1275521742961508432>cartographerset backupmembers`

### cartographerset restorelatest

**Description:** Restore the latest backup for this server

**Usage:** `<@1275521742961508432>cartographerset restorelatest`

### cartographerset messagelimit

**Description:** Set the message backup limit per channel for auto backups

Set to 0 to disable message backups

⚠️**Warning**⚠️
Setting this to a high number can cause backups to be slow and take up a lot of space.

**Usage:** `<@1275521742961508432>cartographerset messagelimit`

### cartographerset autobackups

**Description:** Enable/Disable allowing auto backups

**Usage:** `<@1275521742961508432>cartographerset autobackups`

### cartographerset backupemojis

**Description:** Toggle backing up emojis

⚠️**Warning**⚠️
Restoring emojis is EXTREMELY rate-limited and can take a long time (like hours) for servers with many emojis.

**Usage:** `<@1275521742961508432>cartographerset backupemojis`

### cartographerset allow

**Description:** Add/Remove a server from the allow list

**Usage:** `<@1275521742961508432>cartographerset allow`

### cartographerset ignore

**Description:** Add/Remove a server from the ignore list

**Usage:** `<@1275521742961508432>cartographerset ignore`

### cartographerset view

**Description:** View current global settings

**Usage:** `<@1275521742961508432>cartographerset view`

### cartographerset maxbackups

**Description:** Set the max amount of backups a server can have

**Usage:** `<@1275521742961508432>cartographerset maxbackups`

### cartographerset backupstickers

**Description:** Toggle backing up stickers

⚠️**Warning**⚠️
Restoring stickers is EXTREMELY rate-limited and can take a long time (like hours) for servers with many stickers.

**Usage:** `<@1275521742961508432>cartographerset backupstickers`

### cartographerset wipebackups

**Description:** Wipe all backups for all servers

This action cannot be undone!

**Usage:** `<@1275521742961508432>cartographerset wipebackups`

### cartographerset backup

**Description:** Create a backup of this server

limit: How many messages to backup per channel (0 for None)

**Usage:** `<@1275521742961508432>cartographerset backup`

### cartographerset backuproles

**Description:** Toggle backing up roles

⚠️**Warning**⚠️
Any roles above the bot's role will not be restored.

**Usage:** `<@1275521742961508432>cartographerset backuproles`

