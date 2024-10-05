PyLavPlayer
===========

A Media player using the PyLav library

# /search (Slash Command)
Search for a track, then play the selected response.<br/>
 - Usage: `/search <query> [source]`
 - `query:` (Required) The query to search for search query
 - `source:` (Optional) Where to search in

 - Checks: `Server Only`
Extended Arg Info
> ### query: str
> - Autocomplete: True
> 
> The query to search for search query
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### source: str
> - Autocomplete: False
> - Default: None
> - Choices: ['Deezer', 'YouTube Music', 'Spotify', 'Apple Music', 'SoundCloud', 'YouTube', 'Yandex Music']
> 
> Where to search in
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# /play (Slash Command)
Enqueue the specified query to be played.<br/>
 - Usage: `/play [query] [enqueue_type]`
 - `query:` (Optional) This argument is the query to play, a link or a search query.
 - `enqueue_type:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### query: str
> - Autocomplete: False
> - Default: None
> 
> This argument is the query to play, a link or a search query.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### enqueue_type: str
> - Autocomplete: False
> - Default: add_to_queue
> - Choices: ['Play Now', 'Play Next', 'Add to Queue']
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>playerset
Player settings commands<br/>
 - Usage: `<@1275521742961508432>playerset`


## <@1275521742961508432>playerset server
Server-specific settings.<br/>
 - Usage: `<@1275521742961508432>playerset server`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `server`
 - Checks: `server_only`


### <@1275521742961508432>playerset server dc
Set whether the bot should disconnect from the voice channel<br/>
 - Usage: `<@1275521742961508432>playerset server dc`


#### <@1275521742961508432>playerset server dc empty
Set whether I should disconnect from the voice channel when the queue is empty.<br/>

Arguments:<br/>
    - `<toggle>`: I should disconnect from the voice channel when the queue is empty.<br/>
    - `<duration>`: How long after the queue is empty should I disconnect?<br/>
    The Default is 60 seconds.<br/>
    Accept seconds, minutes, hours, days, and weeks.<br/>
    If no unit is specified, the duration is assumed to be seconds.<br/>
 - Usage: `<@1275521742961508432>playerset server dc empty <toggle> [after]`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


#### <@1275521742961508432>playerset server dc alone
Set whether I should disconnect from the voice channel when alone.<br/>

Arguments:<br/>
    - `<toggle>`: I should disconnect from the voice channel when it detects that it is<br/>
    alone.<br/>
    - `<duration>`: How longer after detecting should I disconnect?<br/>
    The Default is 60 seconds.<br/>
    Accept seconds, minutes, hours, days, and weeks.<br/>
    If no unit is specified, the duration is assumed to be seconds.<br/>
 - Usage: `<@1275521742961508432>playerset server dc alone <toggle> [after]`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset server lock
Restrict which channels where I can be used.<br/>
 - Usage: `<@1275521742961508432>playerset server lock`


#### <@1275521742961508432>playerset server lock voice
Restrict me only to join the specified voice channel.<br/>
 - Usage: `<@1275521742961508432>playerset server lock voice [channel]`
 - Aliases: `vc`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


#### <@1275521742961508432>playerset server lock commands
Restrict me only to accept PyLav commands executed from the specified channel.<br/>
 - Usage: `<@1275521742961508432>playerset server lock commands [channel]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### <@1275521742961508432>playerset server deafen
Set whether I should deafen myself when playing.<br/>
 - Usage: `<@1275521742961508432>playerset server deafen <toggle>`
 - Aliases: `deaf`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset server dj
Add, remove or show the disc jockey roles and users for this server.<br/>
 - Usage: `<@1275521742961508432>playerset server dj`


#### <@1275521742961508432>playerset server dj clear
Clear the disc jockey roles and users for this server.<br/>
 - Usage: `<@1275521742961508432>playerset server dj clear`


#### <@1275521742961508432>playerset server dj add
Add disc jockey roles or users to this server.<br/>
 - Usage: `<@1275521742961508432>playerset server dj add <roles_or_users>`


#### <@1275521742961508432>playerset server dj list
List the disc jockey roles and users for this server.<br/>
 - Usage: `<@1275521742961508432>playerset server dj list`


#### <@1275521742961508432>playerset server dj remove
Remove disc jockey roles or users in this server.<br/>
 - Usage: `<@1275521742961508432>playerset server dj remove <roles_or_users>`


### <@1275521742961508432>playerset server playlist
Specify a playlist to be used for autoplay.<br/>
 - Usage: `<@1275521742961508432>playerset server playlist <playlist>`


### <@1275521742961508432>playerset server shuffle
Set whether I should allow users to shuffle the queue<br/>
 - Usage: `<@1275521742961508432>playerset server shuffle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset server auto
Set whether the bot should automatically play songs when the queue is empty.<br/>
 - Usage: `<@1275521742961508432>playerset server auto <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset server autoshuffle
Set whether I should shuffle the queue after adding every new song.<br/>
 - Usage: `<@1275521742961508432>playerset server autoshuffle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset server vol
Set the maximum volume a user can set.<br/>
 - Usage: `<@1275521742961508432>playerset server vol <volume>`
 - Aliases: `volume`
Extended Arg Info
> ### volume: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>playerset up
Removes a vote for a Player being down.<br/>

If enough (50% or more of currently active players) report issues, PyLav will automatically<br/>
switch to a different node or restart the current node where possible.<br/>

This command is only valid if your server previously voted for a node to be down and is now back up.<br/>
 - Usage: `<@1275521742961508432>playerset up`
 - Checks: `requires_player and invoker_is_dj`


## <@1275521742961508432>playerset global
Bot-wide settings.<br/>
 - Usage: `<@1275521742961508432>playerset global`
 - Restricted to: `BOT_OWNER`
 - Aliases: `owner`


### <@1275521742961508432>playerset global dc
Set whether I should disconnect from the voice channel.<br/>
 - Usage: `<@1275521742961508432>playerset global dc`


#### <@1275521742961508432>playerset global dc alone
Set whether I should disconnect from the voice channel when alone.<br/>

Arguments:<br/>
    - `<toggle>`: Whether I should disconnect from the voice channel when I detect that I am alone in a voice channel.<br/>
    - `<duration>`: How longer after detecting should the player be disconnected? The default is 60 seconds.<br/>
    Accepts second, minutes, hours, days and weeks.<br/>
    If no unit is specified, the duration is assumed to be given in seconds.<br/>
 - Usage: `<@1275521742961508432>playerset global dc alone <toggle> [after]`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


#### <@1275521742961508432>playerset global dc empty
Set whether I should disconnect from the voice channel when the queue is empty.<br/>

Arguments:<br/>
    - `<toggle>`: Whether I should disconnect from the voice channel when the queue is empty.<br/>
    - `<duration>`: How long after the queue is empty should the player be disconnected? The default is 60 seconds.<br/>
    Accepts second, minutes, hours, days and weeks (if no unit is specified, the duration is assumed to be given in seconds)<br/>
 - Usage: `<@1275521742961508432>playerset global dc empty <toggle> [after]`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset global auto
Set whether I should automatically play songs when the queue is empty.<br/>
 - Usage: `<@1275521742961508432>playerset global auto <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset global vol
Set the maximum volume a server can set<br/>
 - Usage: `<@1275521742961508432>playerset global vol <volume>`
 - Aliases: `volume`
Extended Arg Info
> ### volume: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>playerset global shuffle
Set whether I should allow users to shuffle the queue<br/>
 - Usage: `<@1275521742961508432>playerset global shuffle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset global autoshuffle
Set whether the server is allowed to enable auto shuffle.<br/>
 - Usage: `<@1275521742961508432>playerset global autoshuffle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>playerset global deafen
Set whether I should deafen myself when playing.<br/>
 - Usage: `<@1275521742961508432>playerset global deafen <toggle>`
 - Aliases: `deaf`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>playerset version
Show the version of the Cog and PyLav<br/>
 - Usage: `<@1275521742961508432>playerset version`


## <@1275521742961508432>playerset down
Notifies PyLav that a Player is having issues.<br/>

If enough (50% or more of currently playing players) report issues, PyLav will automatically<br/>
switch to a different node or restart the current node where possible.<br/>
 - Usage: `<@1275521742961508432>playerset down`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `requires_player and invoker_is_dj`


# <@1275521742961508432>play
Attempt to play the queries which you provide.<br/>

Separate multiple queries with a new line (`shift + enter`).<br/>

If you want to play a local track, you can specify the full path relative to the local tracks' folder.<br/>
For example, if my local tracks folder is: `/home/draper/music`.<br/>

I can play a single track with `track.mp3` or `/home/draper/music/track.mp3`.<br/>
I can play everything inside a folder with a `sub-folder/folder`.<br/>
I can play everything inside a folder and its sub-folders with the `all:` prefix, i.e. `all:sub-folder/folder`.<br/>

You can search specific services by using the following prefixes*:<br/>
`dzsearch:`  - Deezer<br/>
`spsearch:`  - Spotify<br/>
`amsearch:`  - Apple Music<br/>
`ytmsearch:` - YouTube Music<br/>
`ytsearch:`  - YouTube<br/>
`scsearch:`  - SoundCloud<br/>
`ymsearch:`  - Yandex Music<br/>

You can trigger text-to-speech by using the following prefixes*:<br/>
`speak:` - I will speak the query (limited to 200 characters)<br/>
`tts://` - I will speak the query<br/>
 - Usage: `<@1275521742961508432>play [query]`
 - Aliases: `p`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### query: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>bump
Plays the specified track from the queue.<br/>

If you specify the `after_current` argument, the track will be played after the current track; otherwise, it will replace the current track.<br/>
 - Usage: `<@1275521742961508432>bump <queue_number> [after_current=False]`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### queue_number: int
> ```
> A number without decimal places.
> ```
> ### after_current: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>playnext
Enqueue a track at the top of the queue.<br/>
 - Usage: `<@1275521742961508432>playnext <query>`
 - Aliases: `pn`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>remove
Remove the specified track from the queue.<br/>

If you specify the `remove_duplicates` argument, all tracks that are the same as your URL or the index track will be removed.<br/>
 - Usage: `<@1275521742961508432>remove <track_url_or_index> [remove_duplicates=False]`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### track_url_or_index: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### remove_duplicates: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>__PyLavPlayer_volume_change_by

 - Usage: `<@1275521742961508432>__PyLavPlayer_volume_change_by <change_by>`
 - Checks: `always_hidden`
Extended Arg Info
> ### change_by: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>connect (Hybrid Command)
Request that I connect to the specified channel or your current channel.<br/>
 - Usage: `<@1275521742961508432>connect [channel]`
 - Slash Usage: `/connect [channel]`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### channel: Optional[discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


# <@1275521742961508432>np (Hybrid Command)
Shows which track is currently being played on this server.<br/>
 - Usage: `<@1275521742961508432>np [to_dm=False]`
 - Slash Usage: `/np [to_dm=False]`
 - Aliases: `now`
 - Checks: `requires_player and server_only`
Extended Arg Info
> ### to_dm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>skip (Hybrid Command)
Skips the current track.<br/>
 - Usage: `<@1275521742961508432>skip`
 - Slash Usage: `/skip`
 - Checks: `invoker_is_dj, requires_player, and server_only`


# <@1275521742961508432>stop (Hybrid Command)
Stops the player and clears the queue.<br/>
 - Usage: `<@1275521742961508432>stop`
 - Slash Usage: `/stop`
 - Checks: `invoker_is_dj, requires_player, and server_only`


# <@1275521742961508432>dc (Hybrid Command)
Request that I disconnect from the current voice channel.<br/>
 - Usage: `<@1275521742961508432>dc`
 - Slash Usage: `/dc`
 - Aliases: `disconnect`
 - Checks: `invoker_is_dj and requires_player`


# <@1275521742961508432>queue (Hybrid Command)
Shows the current queue for this server.<br/>
 - Usage: `<@1275521742961508432>queue`
 - Slash Usage: `/queue`
 - Aliases: `q`
 - Checks: `requires_player and server_only`


# <@1275521742961508432>shuffle (Hybrid Command)
Shuffles the current queue.<br/>
 - Usage: `<@1275521742961508432>shuffle`
 - Slash Usage: `/shuffle`
 - Checks: `invoker_is_dj, requires_player, and server_only`


# <@1275521742961508432>repeat (Hybrid Command)
Set whether to repeat the current song or queue.<br/>

If no argument is given, the current repeat mode will be toggled between the current track and off.<br/>
 - Usage: `<@1275521742961508432>repeat [queue=None]`
 - Slash Usage: `/repeat [queue=None]`
 - Checks: `invoker_is_dj, requires_player, and server_only`
Extended Arg Info
> ### queue: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>pause (Hybrid Command)
Pause the player<br/>
 - Usage: `<@1275521742961508432>pause`
 - Slash Usage: `/pause`
 - Checks: `invoker_is_dj, requires_player, and server_only`


# <@1275521742961508432>resume (Hybrid Command)
Resume the player<br/>
 - Usage: `<@1275521742961508432>resume`
 - Slash Usage: `/resume`
 - Checks: `invoker_is_dj, requires_player, and server_only`


# <@1275521742961508432>volume (Hybrid Command)
Set the current volume for the player.<br/>

The volume is a percentage value between 0% and 1,000%, where 100% is the default volume.<br/>
 - Usage: `<@1275521742961508432>volume <volume>`
 - Slash Usage: `/volume <volume>`
 - Checks: `invoker_is_dj, requires_player, and server_only`
Extended Arg Info
> ### volume: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>seek (Hybrid Command)
Seek the current track.<br/>

Seek can either be a number of seconds, a timestamp, or a specific percentage of the track.<br/>

Examples:<br/>
`<@1275521742961508432>seek 10` Seeks 10 seconds forward<br/>
`<@1275521742961508432>seek -20` Seeks 20 seconds backwards<br/>
`<@1275521742961508432>seek 0:30` Seeks to 0:30<br/>
`<@1275521742961508432>seek 50%` Seeks to 50% of the track<br/>
 - Usage: `<@1275521742961508432>seek <seek>`
 - Slash Usage: `/seek <seek>`
 - Checks: `invoker_is_dj, requires_player, and server_only`
Extended Arg Info
> ### seek: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>prev (Hybrid Command)
Play previously played tracks.<br/>

A history of the last 100 tracks played is kept.<br/>
 - Usage: `<@1275521742961508432>prev`
 - Slash Usage: `/prev`
 - Aliases: `previous`
 - Checks: `invoker_is_dj, requires_player, and server_only`


