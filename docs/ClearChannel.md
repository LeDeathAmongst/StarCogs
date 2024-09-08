# ClearChannel Help

### clearchannel

**Description:** Delete ALL messages from the current channel by duplicating it and then deleting it.

For security reasons, only the server owner and the bot owner can use the command. Use the "permissions" cog for more options.
⚠ The channel will be cloned, and then **deleted**.

**Usage:** `<@1275521742961508432>clearchannel`

### setclearchannel

**Description:** Configure ClearChannel for your server.

**Usage:** `<@1275521742961508432>setclearchannel`

### setclearchannel promptmessage

**Description:** Specify a custom message to be sent to confirm the clearing of the channel.

Use the variables `{user_name}`, `{user_avatar_url}`, `{user_mention}`, `{user_id}`, `{channel_name}`, `{channel_mention}` and `{channel_id}`.

Default value: `...`
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`

**Usage:** `<@1275521742961508432>setclearchannel promptmessage`

### setclearchannel dmauthor

**Description:** If this option is enabled, the bot will try to send a dm to the author of the order to confirm that everything went well.

Default value: `...`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setclearchannel dmauthor`

### setclearchannel modalconfig

**Description:** Set all settings for the cog with a Discord Modal.

**Usage:** `<@1275521742961508432>setclearchannel modalconfig`

### setclearchannel channeldelete

**Description:** If this option is disabled, the bot will not delete the original channel: it will duplicate it as normal, but move it to the end of the server's channel list.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setclearchannel channeldelete`

### setclearchannel firstmessage

**Description:** If this option is enabled, the bot will send a message to the emptied channel to inform that it has been emptied.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setclearchannel firstmessage`

### setclearchannel showsettings

**Description:** Show all settings for the cog with defaults and values.

**Usage:** `<@1275521742961508432>setclearchannel showsettings`

### setclearchannel custommessage

**Description:** Specify a custom message to be sent from the link of another message or a json (https://discohook.org/ for example).

Use the variables `{user_name}`, `{user_avatar_url}`, `{user_mention}`, `{user_id}`, `{channel_name}`, `{channel_mention}` and `{channel_id}`.

Default value: `...`
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`

**Usage:** `<@1275521742961508432>setclearchannel custommessage`

### setclearchannel resetsetting

**Description:** Reset a setting.

**Usage:** `<@1275521742961508432>setclearchannel resetsetting`

