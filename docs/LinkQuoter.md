# LinkQuoter Help

### linkquote

**Description:** Quote a message from a link.

**Usage:** `<@1275521742961508432>linkquote`

### setlinkquoter

**Description:** Commands to configure LinkQuoter.

**Usage:** `<@1275521742961508432>setlinkquoter`

### setlinkquoter enabled

**Description:** Toggle automatic link-quoting.

Enabling this will make [botname] attempt to quote any message link that is sent in this server.
[botname] will ignore any message that has `no quote` in it.
If the user doesn't have permission to view the channel that they link, it will not quote.

To enable quoting from other servers, run `[p]linkquoteset global`.

To prevent spam, links can be automatically quoted 3 times every 10 seconds.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setlinkquoter enabled`

### setlinkquoter deletemessage

**Description:** Toggle deleting of messages for automatic quoting.

If automatic quoting is enabled, then [botname] will also delete messages that contain links in them.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setlinkquoter deletemessage`

### setlinkquoter blacklistchannels

**Description:** Set the channels in which auto-quoting will be disabled.

Default value: `[]`
Dev: `Greedy[GuildChannel]`

**Usage:** `<@1275521742961508432>setlinkquoter blacklistchannels`

### setlinkquoter deletemessagebutton

**Description:** Toggle the delete message button on the quote messages.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setlinkquoter deletemessagebutton`

### setlinkquoter showsettings

**Description:** Show all settings for the cog with defaults and values.

**Usage:** `<@1275521742961508432>setlinkquoter showsettings`

### setlinkquoter deleteafter

**Description:** Set the time in seconds to delete the message after.

Default value: `0`
Dev: `<class 'int'>`

**Usage:** `<@1275521742961508432>setlinkquoter deleteafter`

### setlinkquoter whitelistchannels

**Description:** Set the channels in which auto-quoting will be enabled.

Default value: `[]`
Dev: `Greedy[GuildChannel]`

**Usage:** `<@1275521742961508432>setlinkquoter whitelistchannels`

### setlinkquoter webhooks

**Description:** Toggle sending message with the name and avatar of the Author of the quote (with webhooks)

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setlinkquoter webhooks`

### setlinkquoter crossserver

**Description:**  Toggle cross-server quoting.

Turning this setting on will allow this server to quote other servers, and other servers to quote this one.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setlinkquoter crossserver`

### setlinkquoter resetsetting

**Description:** Reset a setting.

**Usage:** `<@1275521742961508432>setlinkquoter resetsetting`

### setlinkquoter migratefromphen

**Description:** Migrate config from LinkQuoter by Phen.

**Usage:** `<@1275521742961508432>setlinkquoter migratefromphen`

### setlinkquoter modalconfig

**Description:** Set all settings for the cog with a Discord Modal.

**Usage:** `<@1275521742961508432>setlinkquoter modalconfig`

