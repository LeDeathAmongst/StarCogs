Streams
=======

Various commands relating to streaming platforms.

You can check if a Twitch, YouTube or Picarto stream is
currently live.

# ,twitchstream
Check if a Twitch channel is live.<br/>
 - Usage: `,twitchstream <channel_name>`
 - Checks: `server_only`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,youtubestream
Check if a YouTube channel is live.<br/>
 - Usage: `,youtubestream <channel_id_or_name>`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### channel_id_or_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,picarto
Check if a Picarto channel is live.<br/>
 - Usage: `,picarto <channel_name>`
 - Checks: `server_only`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,streamalert
Manage automated stream alerts.<br/>
 - Usage: `,streamalert`
 - Restricted to: `MOD`
 - Checks: `server_only`


## ,streamalert list
List all active stream alerts in this server.<br/>
 - Usage: `,streamalert list`


## ,streamalert youtube
Toggle alerts in this channel for a YouTube stream.<br/>
 - Usage: `,streamalert youtube <channel_name_or_id> [discord_channel=operator.attrgetter('channel')]`
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


## ,streamalert stop
Disable all stream alerts in this channel or server.<br/>

`,streamalert stop` will disable this channel's stream<br/>
alerts.<br/>

Do `,streamalert stop yes` to disable all stream alerts in<br/>
this server.<br/>
 - Usage: `,streamalert stop [_all=False]`
Extended Arg Info
> ### _all: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,streamalert twitch
Manage Twitch stream notifications.<br/>
 - Usage: `,streamalert twitch <channel_name> [discord_channel=operator.attrgetter('channel')]`
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


### ,streamalert twitch channel
Toggle alerts in this or the given channel for a Twitch stream.<br/>
 - Usage: `,streamalert twitch channel <channel_name> [discord_channel=operator.attrgetter('channel')]`
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


## ,streamalert picarto
Toggle alerts in this channel for a Picarto stream.<br/>
 - Usage: `,streamalert picarto <channel_name> [discord_channel=operator.attrgetter('channel')]`
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


# ,streamset
Manage stream alert settings.<br/>
 - Usage: `,streamset`
 - Restricted to: `MOD`


## ,streamset timer
Set stream check refresh time.<br/>
 - Usage: `,streamset timer <refresh_time>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### refresh_time: int
> ```
> A number without decimal places.
> ```


## ,streamset autodelete
Toggle alert deletion for when streams go offline.<br/>
 - Usage: `,streamset autodelete <on_off>`
 - Checks: `server_only`
Extended Arg Info
> ### on_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,streamset usebuttons
Toggle whether to use buttons for stream alerts.<br/>
 - Usage: `,streamset usebuttons`
 - Checks: `server_only`


## ,streamset ignoreschedule
Toggle excluding YouTube streams schedules from alerts.<br/>
 - Usage: `,streamset ignoreschedule`
 - Checks: `server_only`


## ,streamset mention
Manage mention settings for stream alerts.<br/>
 - Usage: `,streamset mention`
 - Checks: `server_only`


### ,streamset mention all
Toggle the `@​everyone` mention.<br/>
 - Usage: `,streamset mention all`
 - Aliases: `everyone`
 - Checks: `server_only`


### ,streamset mention role
Toggle a role mention.<br/>
 - Usage: `,streamset mention role <role>`
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


### ,streamset mention online
Toggle the `@​here` mention.<br/>
 - Usage: `,streamset mention online`
 - Aliases: `here`
 - Checks: `server_only`


## ,streamset youtubekey
Explain how to set the YouTube token.<br/>
 - Usage: `,streamset youtubekey`
 - Restricted to: `BOT_OWNER`


## ,streamset twitchtoken
Explain how to set the twitch token.<br/>
 - Usage: `,streamset twitchtoken`
 - Restricted to: `BOT_OWNER`


## ,streamset ignorereruns
Toggle excluding rerun streams from alerts.<br/>
 - Usage: `,streamset ignorereruns`
 - Checks: `server_only`


## ,streamset message
Manage custom messages for stream alerts.<br/>
 - Usage: `,streamset message`
 - Checks: `server_only`


### ,streamset message nomention
Set stream alert message when mentions are disabled.<br/>

Use `{stream}` in the message to insert the channel or username.<br/>
Use `{stream.display_name}` in the message to insert the channel's display name (on Twitch, this may be different from `{stream}`).<br/>

For example: `,streamset message nomention {stream.display_name} is live!`<br/>
 - Usage: `,streamset message nomention <message>`
 - Checks: `server_only`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,streamset message mention
Set stream alert message when mentions are enabled.<br/>

Use `{mention}` in the message to insert the selected mentions.<br/>
Use `{stream}` in the message to insert the channel or username.<br/>
Use `{stream.display_name}` in the message to insert the channel's display name (on Twitch, this may be different from `{stream}`).<br/>

For example: `,streamset message mention {mention}, {stream.display_name} is live!`<br/>
 - Usage: `,streamset message mention <message>`
 - Checks: `server_only`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,streamset message clear
Reset the stream alert messages in this server.<br/>
 - Usage: `,streamset message clear`
 - Checks: `server_only`


