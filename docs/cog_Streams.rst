Streams
=======

Various commands relating to streaming platforms.

You can check if a Twitch, YouTube or Picarto stream is
currently live.

# <@1275521742961508432>twitchstream
Check if a Twitch channel is live.<br/>
 - Usage: `<@1275521742961508432>twitchstream <channel_name>`
 - Checks: `server_only`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>youtubestream
Check if a YouTube channel is live.<br/>
 - Usage: `<@1275521742961508432>youtubestream <channel_id_or_name>`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### channel_id_or_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>picarto
Check if a Picarto channel is live.<br/>
 - Usage: `<@1275521742961508432>picarto <channel_name>`
 - Checks: `server_only`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>streamalert
Manage automated stream alerts.<br/>
 - Usage: `<@1275521742961508432>streamalert`
 - Restricted to: `MOD`
 - Checks: `server_only`


## <@1275521742961508432>streamalert list
List all active stream alerts in this server.<br/>
 - Usage: `<@1275521742961508432>streamalert list`


## <@1275521742961508432>streamalert youtube
Toggle alerts in this channel for a YouTube stream.<br/>
 - Usage: `<@1275521742961508432>streamalert youtube <channel_name_or_id> [discord_channel=operator.attrgetter('channel')]`
Extended Arg Info
> ### channel_name_or_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### discord_channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>streamalert stop
Disable all stream alerts in this channel or server.<br/>

`<@1275521742961508432>streamalert stop` will disable this channel's stream<br/>
alerts.<br/>

Do `<@1275521742961508432>streamalert stop yes` to disable all stream alerts in<br/>
this server.<br/>
 - Usage: `<@1275521742961508432>streamalert stop [_all=False]`
Extended Arg Info
> ### _all: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>streamalert twitch
Manage Twitch stream notifications.<br/>
 - Usage: `<@1275521742961508432>streamalert twitch <channel_name> [discord_channel=operator.attrgetter('channel')]`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### discord_channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### <@1275521742961508432>streamalert twitch channel
Toggle alerts in this or the given channel for a Twitch stream.<br/>
 - Usage: `<@1275521742961508432>streamalert twitch channel <channel_name> [discord_channel=operator.attrgetter('channel')]`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### discord_channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>streamalert picarto
Toggle alerts in this channel for a Picarto stream.<br/>
 - Usage: `<@1275521742961508432>streamalert picarto <channel_name> [discord_channel=operator.attrgetter('channel')]`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### discord_channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


# <@1275521742961508432>streamset
Manage stream alert settings.<br/>
 - Usage: `<@1275521742961508432>streamset`
 - Restricted to: `MOD`


## <@1275521742961508432>streamset autodelete
Toggle alert deletion for when streams go offline.<br/>
 - Usage: `<@1275521742961508432>streamset autodelete <on_off>`
 - Checks: `server_only`
Extended Arg Info
> ### on_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>streamset usebuttons
Toggle whether to use buttons for stream alerts.<br/>
 - Usage: `<@1275521742961508432>streamset usebuttons`
 - Checks: `server_only`


## <@1275521742961508432>streamset ignoreschedule
Toggle excluding YouTube streams schedules from alerts.<br/>
 - Usage: `<@1275521742961508432>streamset ignoreschedule`
 - Checks: `server_only`


## <@1275521742961508432>streamset mention
Manage mention settings for stream alerts.<br/>
 - Usage: `<@1275521742961508432>streamset mention`
 - Checks: `server_only`


### <@1275521742961508432>streamset mention online
Toggle the `@​here` mention.<br/>
 - Usage: `<@1275521742961508432>streamset mention online`
 - Aliases: `here`
 - Checks: `server_only`


### <@1275521742961508432>streamset mention all
Toggle the `@​everyone` mention.<br/>
 - Usage: `<@1275521742961508432>streamset mention all`
 - Aliases: `everyone`
 - Checks: `server_only`


### <@1275521742961508432>streamset mention role
Toggle a role mention.<br/>
 - Usage: `<@1275521742961508432>streamset mention role <role>`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>streamset youtubekey
Explain how to set the YouTube token.<br/>
 - Usage: `<@1275521742961508432>streamset youtubekey`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>streamset ignorereruns
Toggle excluding rerun streams from alerts.<br/>
 - Usage: `<@1275521742961508432>streamset ignorereruns`
 - Checks: `server_only`


## <@1275521742961508432>streamset message
Manage custom messages for stream alerts.<br/>
 - Usage: `<@1275521742961508432>streamset message`
 - Checks: `server_only`


### <@1275521742961508432>streamset message clear
Reset the stream alert messages in this server.<br/>
 - Usage: `<@1275521742961508432>streamset message clear`
 - Checks: `server_only`


### <@1275521742961508432>streamset message mention
Set stream alert message when mentions are enabled.<br/>

Use `{mention}` in the message to insert the selected mentions.<br/>
Use `{stream}` in the message to insert the channel or username.<br/>
Use `{stream.display_name}` in the message to insert the channel's display name (on Twitch, this may be different from `{stream}`).<br/>

For example: `<@1275521742961508432>streamset message mention {mention}, {stream.display_name} is live!`<br/>
 - Usage: `<@1275521742961508432>streamset message mention <message>`
 - Checks: `server_only`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>streamset message nomention
Set stream alert message when mentions are disabled.<br/>

Use `{stream}` in the message to insert the channel or username.<br/>
Use `{stream.display_name}` in the message to insert the channel's display name (on Twitch, this may be different from `{stream}`).<br/>

For example: `<@1275521742961508432>streamset message nomention {stream.display_name} is live!`<br/>
 - Usage: `<@1275521742961508432>streamset message nomention <message>`
 - Checks: `server_only`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>streamset twitchtoken
Explain how to set the twitch token.<br/>
 - Usage: `<@1275521742961508432>streamset twitchtoken`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>streamset timer
Set stream check refresh time.<br/>
 - Usage: `<@1275521742961508432>streamset timer <refresh_time>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### refresh_time: int
> ```
> A number without decimal places.
> ```


