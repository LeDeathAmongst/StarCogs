A cog to delete ALL messages of a channel!<br/><br/>⚠ The channel will be cloned, and then **deleted**.

# ,clearchannel (Hybrid Command)
Delete ALL messages from the current channel by duplicating it and then deleting it.<br/>

For security reasons, only the server owner and the bot owner can use the command. Use the "permissions" cog for more options.<br/>
⚠ The channel will be cloned, and then **deleted**.<br/>
 - Usage: `,clearchannel [confirmation=False]`
 - Slash Usage: `/clearchannel [confirmation=False]`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `nuke and purgefilth`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,setclearchannel (Hybrid Command)
Configure ClearChannel for your server.<br/>
 - Usage: `,setclearchannel`
 - Slash Usage: `/setclearchannel`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `clearchannelset`
 - Checks: `server_only`
## ,setclearchannel custommessage (Hybrid Command)
Specify a custom message to be sent from the link of another message or a json (https://discohook.org/ for example).<br/>

Use the variables `{user_name}`, `{user_avatar_url}`, `{user_mention}`, `{user_id}`, `{channel_name}`, `{channel_mention}` and `{channel_id}`.<br/>

Default value: `...`<br/>
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`<br/>
 - Usage: `,setclearchannel custommessage <value>`
 - Slash Usage: `/setclearchannel custommessage <value>`
 - Checks: `server_only`
## ,setclearchannel promptmessage (Hybrid Command)
Specify a custom message to be sent to confirm the clearing of the channel.<br/>

Use the variables `{user_name}`, `{user_avatar_url}`, `{user_mention}`, `{user_id}`, `{channel_name}`, `{channel_mention}` and `{channel_id}`.<br/>

Default value: `...`<br/>
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`<br/>
 - Usage: `,setclearchannel promptmessage <value>`
 - Slash Usage: `/setclearchannel promptmessage <value>`
 - Checks: `server_only`
## ,setclearchannel channeldelete (Hybrid Command)
If this option is disabled, the bot will not delete the original channel: it will duplicate it as normal, but move it to the end of the server's channel list.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setclearchannel channeldelete <value>`
 - Slash Usage: `/setclearchannel channeldelete <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setclearchannel modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setclearchannel modalconfig [confirmation=False]`
 - Slash Usage: `/setclearchannel modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setclearchannel showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setclearchannel showsettings [with_dev=False]`
 - Slash Usage: `/setclearchannel showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setclearchannel dmauthor (Hybrid Command)
If this option is enabled, the bot will try to send a dm to the author of the order to confirm that everything went well.<br/>

Default value: `...`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setclearchannel dmauthor <value>`
 - Slash Usage: `/setclearchannel dmauthor <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setclearchannel resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setclearchannel resetsetting <setting>`
 - Slash Usage: `/setclearchannel resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setclearchannel firstmessage (Hybrid Command)
If this option is enabled, the bot will send a message to the emptied channel to inform that it has been emptied.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setclearchannel firstmessage <value>`
 - Slash Usage: `/setclearchannel firstmessage <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
