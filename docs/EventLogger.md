Cog to log various Discord events

# ,setlog
Set the logging channel for a specific event<br/>
 - Usage: `,setlog <event> <channel>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### event: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog reactionadd
Channel for logging reaction add events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog reactionadd <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog resetsetting
Reset a setting.<br/>
 - Usage: `,setlog resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setlog serverchanneldelete
Channel for logging channel deletion events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverchanneldelete <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog memberremove
Channel for logging member remove events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog memberremove <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog messageedit
Channel for logging message edit events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog messageedit <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverstickerupdate
Channel for logging sticker update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverstickerupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog memberjoin
Channel for logging member join events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog memberjoin <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverroledelete
Channel for logging role deletion events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverroledelete <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog messagedelete
Channel for logging message deletion events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog messagedelete <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog reactionremove
Channel for logging reaction remove events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog reactionremove <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverchannelupdate
Channel for logging channel update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverchannelupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog bulkmessagedelete
Channel for logging bulk message deletion events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog bulkmessagedelete <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverchannelcreate
Channel for logging channel creation events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverchannelcreate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog categories
View the event categories and their events<br/>
 - Usage: `,setlog categories`
## ,setlog serverstickercreate
Channel for logging sticker creation events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverstickercreate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog userupdate
Channel for logging user update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog userupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverroleupdate
Channel for logging role update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverroleupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serveremojisupdate
Channel for logging emoji update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serveremojisupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog showsettings
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setlog showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setlog memberupdate
Channel for logging member update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog memberupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog integrationcreate
Channel for logging integration creation events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog integrationcreate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverrolecreate
Channel for logging role creation events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverrolecreate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog integrationupdate
Channel for logging integration update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog integrationupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog modalconfig
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setlog modalconfig [confirmation=False]`
 - Aliases: `configmodal`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setlog memberban
Channel for logging member ban events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog memberban <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverstickerdelete
Channel for logging sticker deletion events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverstickerdelete <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog serverchannelpinsupdate
Channel for logging channel pins update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog serverchannelpinsupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog voicestateupdate
Channel for logging voice state update events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog voicestateupdate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog invitedelete
Channel for logging invite deletion events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog invitedelete <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog memberunban
Channel for logging member unban events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog memberunban <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog integrationdelete
Channel for logging integration deletion events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog integrationdelete <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setlog invitecreate
Channel for logging invite creation events.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.channel.TextChannel'>`<br/>
 - Usage: `,setlog invitecreate <value>`
Extended Arg Info
> ### value: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# ,seteventlogger
Configure EventLogger for your server.<br/>
 - Usage: `,seteventlogger`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
