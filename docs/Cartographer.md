Backup & Restore tools for Discord servers.<br/><br/>This cog can backup & restore the following:<br/>- Bans (with reason)<br/>- Categories (permissions/order)<br/>- Text channels (permissions/order)<br/>- Voice channels (permissions/order)<br/>- Forum channels  (permissions/order)[Not posts]<br/>- Roles (permissions/color/name/icon and what members they're assigned to)<br/>- Emojis (name/roles)<br/>- Stickers (name/description)<br/>- Members (roles and nicknames)<br/>- Messages (Optional)<br/>- Server icon/banner/splash/discovery splash/description/name<br/>- All server verification/security settings

# ,cartographer
Open the Backup/Restore menu<br/>

This cog can backup & restore the following:<br/>
- Bans (including reason)<br/>
- Categories (permissions/order)<br/>
- Text channels (permissions/order)<br/>
- Voice channels (permissions/order)<br/>
- Forum channels  (permissions/order)[Not forum posts]<br/>
- Roles (permissions/color/name/icon and what members they're assigned to)<br/>
- Emojis (name/roles, Very slow and rate limit heavy)<br/>
- Stickers (name/description, Very slow and rate limit heavy)<br/>
- Members (roles and nicknames)<br/>
- Messages (Optional, can be disabled)<br/>
- Server icon/banner/splash/discovery splash/description/name<br/>
- All server verification/security settings<br/>
 - Usage: `,cartographer`
 - Aliases: `carto`
 - Checks: `server_only`
# ,cartographerset
Backup & Restore Tools<br/>
 - Usage: `,cartographerset`
 - Aliases: `cartoset`
 - Checks: `server_only`
## ,cartographerset backupstickers
Toggle backing up stickers<br/>

⚠️**Warning**⚠️<br/>
Restoring stickers is EXTREMELY rate-limited and can take a long time (like hours) for servers with many stickers.<br/>
 - Usage: `,cartographerset backupstickers`
 - Restricted to: `BOT_OWNER`
## ,cartographerset maxbackups
Set the max amount of backups a server can have<br/>
 - Usage: `,cartographerset maxbackups <max_backups>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### max_backups: int
> ```
> A number without decimal places.
> ```
## ,cartographerset restorelatest
Restore the latest backup for this server<br/>
 - Usage: `,cartographerset restorelatest`
## ,cartographerset wipebackups
Wipe all backups for all servers<br/>

This action cannot be undone!<br/>
 - Usage: `,cartographerset wipebackups <confirm>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,cartographerset backupemojis
Toggle backing up emojis<br/>

⚠️**Warning**⚠️<br/>
Restoring emojis is EXTREMELY rate-limited and can take a long time (like hours) for servers with many emojis.<br/>
 - Usage: `,cartographerset backupemojis`
 - Restricted to: `BOT_OWNER`
## ,cartographerset backup
Create a backup of this server<br/>

limit: How many messages to backup per channel (0 for None)<br/>
 - Usage: `,cartographerset backup [limit=0]`
Extended Arg Info
> ### limit: int = 0
> ```
> A number without decimal places.
> ```
## ,cartographerset backuproles
Toggle backing up roles<br/>

⚠️**Warning**⚠️<br/>
Any roles above the bot's role will not be restored.<br/>
 - Usage: `,cartographerset backuproles`
 - Restricted to: `BOT_OWNER`
## ,cartographerset backupmembers
Toggle backing up members<br/>

⚠️**Warning**⚠️<br/>
Restoring the roles of all members can be slow for large servers.<br/>
 - Usage: `,cartographerset backupmembers`
 - Restricted to: `BOT_OWNER`
## ,cartographerset messagelimit
Set the message backup limit per channel for auto backups<br/>

Set to 0 to disable message backups<br/>

⚠️**Warning**⚠️<br/>
Setting this to a high number can cause backups to be slow and take up a lot of space.<br/>
 - Usage: `,cartographerset messagelimit <limit>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### limit: int
> ```
> A number without decimal places.
> ```
## ,cartographerset autobackups
Enable/Disable allowing auto backups<br/>
 - Usage: `,cartographerset autobackups`
 - Restricted to: `BOT_OWNER`
## ,cartographerset allow
Add/Remove a server from the allow list<br/>
 - Usage: `,cartographerset allow <server>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: discord.server.Guild
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## ,cartographerset ignore
Add/Remove a server from the ignore list<br/>
 - Usage: `,cartographerset ignore <server>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: discord.server.Guild
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## ,cartographerset view
View current global settings<br/>
 - Usage: `,cartographerset view`
 - Restricted to: `BOT_OWNER`
