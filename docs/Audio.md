# Audio Help

### queue

**Description:** List the songs in the queue.

**Usage:** `<@1275521742961508432>queue`

### queue cleanself

**Description:** Removes all tracks you requested from the queue.

**Usage:** `<@1275521742961508432>queue cleanself`

### queue clean

**Description:** Removes songs from the queue if the requester is not in the voice channel.

**Usage:** `<@1275521742961508432>queue clean`

### queue clear

**Description:** Clears the queue.

**Usage:** `<@1275521742961508432>queue clear`

### queue search

**Description:** Search the queue.

**Usage:** `<@1275521742961508432>queue search`

### queue shuffle

**Description:** Shuffles the queue.

**Usage:** `<@1275521742961508432>queue shuffle`

### playlist

**Description:** Playlist configuration options.

Scope info:
​ ​ ​ ​ **Global**:
​ ​ ​ ​ ​ ​ ​ ​ Visible to all users of this bot.
​ ​ ​ ​ ​ ​ ​ ​ Only editable by bot owner.
​ ​ ​ ​ **Guild**:
​ ​ ​ ​ ​ ​ ​ ​ Visible to all users in this guild.
​ ​ ​ ​ ​ ​ ​ ​ Editable by bot owner, guild owner, guild admins, guild mods, DJ role and playlist creator.
​ ​ ​ ​ **User**:
​ ​ ​ ​ ​ ​ ​ ​ Visible to all bot users, if --author is passed.
​ ​ ​ ​ ​ ​ ​ ​ Editable by bot owner and the playlist creator.

**Usage:** `<@1275521742961508432>playlist`

### playlist list

**Description:** List saved playlists.

**Usage**:
​ ​ ​ ​ `[p]playlist list [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist list`
​ ​ ​ ​ `[p]playlist list --scope Global`
​ ​ ​ ​ `[p]playlist list --scope User`

**Usage:** `<@1275521742961508432>playlist list`

### playlist queue

**Description:** Save the queue to a playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist queue playlist_name [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist queue MyGuildPlaylist`
​ ​ ​ ​ `[p]playlist queue MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist queue MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist queue`

### playlist update

**Description:** Updates all tracks in a playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist update playlist_name_OR_id [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist update MyGuildPlaylist`
​ ​ ​ ​ `[p]playlist update MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist update MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist update`

### playlist append

**Description:** Add a track URL, playlist link, or quick search to a playlist.

The track(s) will be appended to the end of the playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist append playlist_name_OR_id track_name_OR_url [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist append MyGuildPlaylist Hello by Adele`
​ ​ ​ ​ `[p]playlist append MyGlobalPlaylist Hello by Adele --scope Global`
​ ​ ​ ​ `[p]playlist append MyGlobalPlaylist Hello by Adele --scope Global --Author Draper#6666`

**Usage:** `<@1275521742961508432>playlist append`

### playlist info

**Description:** Retrieve information from a saved playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist info playlist_name_OR_id [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist info MyGuildPlaylist`
​ ​ ​ ​ `[p]playlist info MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist info MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist info`

### playlist download

**Description:** Download a copy of a playlist.

These files can be used with the `[p]playlist upload` command.
Red v2-compatible playlists can be generated by passing True
for the v2 variable.

**Usage**:
​ ​ ​ ​ `[p]playlist download playlist_name_OR_id [v2=True_OR_False] [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist download MyGuildPlaylist True`
​ ​ ​ ​ `[p]playlist download MyGlobalPlaylist False --scope Global`
​ ​ ​ ​ `[p]playlist download MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist download`

### playlist save

**Description:** Save a playlist from a url.

**Usage**:
​ ​ ​ ​ `[p]playlist save name url [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist save MyGuildPlaylist https://www.youtube.com/playlist?list=PLx0sYbCqOb8Q_CLZC2BdBSKEEB59BOPUM`
​ ​ ​ ​ `[p]playlist save MyGlobalPlaylist https://www.youtube.com/playlist?list=PLx0sYbCqOb8Q_CLZC2BdBSKEEB59BOPUM --scope Global`
​ ​ ​ ​ `[p]playlist save MyPersonalPlaylist https://open.spotify.com/playlist/1RyeIbyFeIJVnNzlGr5KkR --scope User`

**Usage:** `<@1275521742961508432>playlist save`

### playlist create

**Description:** Create an empty playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist create playlist_name [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist create MyGuildPlaylist`
​ ​ ​ ​ `[p]playlist create MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist create MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist create`

### playlist dedupe

**Description:** Remove duplicate tracks from a saved playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist dedupe playlist_name_OR_id [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist dedupe MyGuildPlaylist`
​ ​ ​ ​ `[p]playlist dedupe MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist dedupe MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist dedupe`

### playlist remove

**Description:** Remove a track from a playlist by url.

 **Usage**:
​ ​ ​ ​ `[p]playlist remove playlist_name_OR_id url [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist remove MyGuildPlaylist https://www.youtube.com/watch?v=MN3x-kAbgFU`
​ ​ ​ ​ `[p]playlist remove MyGlobalPlaylist https://www.youtube.com/watch?v=MN3x-kAbgFU --scope Global`
​ ​ ​ ​ `[p]playlist remove MyPersonalPlaylist https://www.youtube.com/watch?v=MN3x-kAbgFU --scope User`

**Usage:** `<@1275521742961508432>playlist remove`

### playlist upload

**Description:** Uploads a playlist file as a playlist for the bot.

V2 and old V3 playlist will be slow.
V3 Playlist made with `[p]playlist download` will load a lot faster.

**Usage**:
​ ​ ​ ​ `[p]playlist upload [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist upload`
​ ​ ​ ​ `[p]playlist upload --scope Global`
​ ​ ​ ​ `[p]playlist upload --scope User`

**Usage:** `<@1275521742961508432>playlist upload`

### playlist rename

**Description:** Rename an existing playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist rename playlist_name_OR_id new_name [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist rename MyGuildPlaylist RenamedGuildPlaylist`
​ ​ ​ ​ `[p]playlist rename MyGlobalPlaylist RenamedGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist rename MyPersonalPlaylist RenamedPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist rename`

### playlist delete

**Description:** Delete a saved playlist.

**Usage**:
​ ​ ​ ​ `[p]playlist delete playlist_name_OR_id [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist delete MyGuildPlaylist`
​ ​ ​ ​ `[p]playlist delete MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist delete MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist delete`

### playlist start

**Description:** Load a playlist into the queue.

**Usage**:
​ ​ ​ ​` [p]playlist start playlist_name_OR_id [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist start MyGuildPlaylist`
​ ​ ​ ​ `[p]playlist start MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]playlist start MyPersonalPlaylist --scope User`

**Usage:** `<@1275521742961508432>playlist start`

### playlist copy

**Description:** Copy a playlist from one scope to another.

**Usage**:
​ ​ ​ ​ `[p]playlist copy playlist_name_OR_id [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --from-scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --from-author [user]
​ ​ ​ ​ ​ ​ ​ ​ --from-guild [guild] **Only the bot owner can use this**

​ ​ ​ ​ ​ ​ ​ ​ --to-scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --to-author [user]
​ ​ ​ ​ ​ ​ ​ ​ --to-guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
​ ​ ​ ​ Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]playlist copy MyGuildPlaylist --from-scope Guild --to-scope Global`
​ ​ ​ ​ `[p]playlist copy MyGlobalPlaylist --from-scope Global --to-author Draper#6666 --to-scope User`
​ ​ ​ ​ `[p]playlist copy MyPersonalPlaylist --from-scope user --to-author Draper#6666 --to-scope Guild --to-guild Red - Discord Bot`

**Usage:** `<@1275521742961508432>playlist copy`

### play

**Description:** Play the specified track or search for a close match.

To play a local track, the query should be `<parentfolder>\<filename>`.
If you are the bot owner, use `[p]audioset info` to display your localtracks path.

**Usage:** `<@1275521742961508432>play`

### bumpplay

**Description:** Force play a URL or search for a track.

**Usage:** `<@1275521742961508432>bumpplay`

### genre

**Description:** Pick a Spotify playlist from a list of categories to start playing.

**Usage:** `<@1275521742961508432>genre`

### autoplay

**Description:** Starts auto play.

**Usage:** `<@1275521742961508432>autoplay`

### search

**Description:** Pick a track with a search.

Use `[p]search list <search term>` to queue all tracks found on YouTube. Use `[p]search sc
<search term>` to search on SoundCloud instead of YouTube.

**Usage:** `<@1275521742961508432>search`

### sing

**Description:** Make Red sing one of her songs.

**Usage:** `<@1275521742961508432>sing`

### audiostats

**Description:** Audio stats.

**Usage:** `<@1275521742961508432>audiostats`

### percent

**Description:** Queue percentage.

**Usage:** `<@1275521742961508432>percent`

### local

**Description:** Local playback commands.

**Usage:** `<@1275521742961508432>local`

### local folder

**Description:** Play all songs in a localtracks folder.

**Usage**:
​ ​ ​ ​ `[p]local folder`
​ ​ ​ ​ ​ ​ ​ ​ Open a menu to pick a folder to queue.

​ ​ `[p]local folder folder_name`
​ ​ ​ ​ ​ ​ ​ ​ Queues all of the tracks inside the folder_name folder.

**Usage:** `<@1275521742961508432>local folder`

### local search

**Description:** Search for songs across all localtracks folders.

**Usage:** `<@1275521742961508432>local search`

### local play

**Description:** Play a local track.

To play a local track, either use the menu to choose a track or enter in the track path directly with the play command.
To play an entire folder, use `[p]help local folder` for instructions.

**Usage**:
​ ​ ​ ​ `[p]local play`
​ ​ ​ ​ ​ ​ ​ ​ Open a menu to pick a track.

​ ​ ​ ​ `[p]play localtracks\album_folder\song_name.mp3`
​ ​ ​ ​ `[p]play album_folder\song_name.mp3`
​ ​ ​ ​ ​ ​ ​ ​ Use a direct link relative to the localtracks folder.

**Usage:** `<@1275521742961508432>local play`

### llset

**Description:** `Dangerous commands` Manage Lavalink node configuration settings.

This command block holds all commands to configure an unmanaged (user maintained) or managed (bot maintained) Lavalink node.

You should not mess with any command in here unless you have a valid reason to,
i.e. been told by someone in the Red-Discord Bot support server to do so.
All the commands in here have the potential to break the Audio cog.

**Usage:** `<@1275521742961508432>llset`

### llset host

**Description:** Set the Lavalink node host.

This command sets the connection host which Audio will use to connect to an unmanaged Lavalink node.

**Usage:** `<@1275521742961508432>llset host`

### llset java

**Description:** Change your Java executable path.

This command shouldn't need to be used most of the time, and is only useful if the host machine has conflicting Java versions.

If changing this make sure that the Java executable you set is supported by Audio.
The current supported versions are Java 17 and 11.

Enter nothing or "java" to reset it back to default.

**Usage:** `<@1275521742961508432>llset java`

### llset secured

**Description:** Set the Lavalink node connection to secured.

This toggle sets the connection type to secured or unsecured when connecting to an unmanaged Lavalink node.

**Usage:** `<@1275521742961508432>llset secured`

### llset reset

**Description:** Reset all `llset` changes back to their default values.

**Usage:** `<@1275521742961508432>llset reset`

### llset port

**Description:** Set the Lavalink node port.

This command sets the connection port which Audio will use to connect to an unmanaged Lavalink node.
Set port to -1 to disable the port and connect to the specified host via ports 80/443

**Usage:** `<@1275521742961508432>llset port`

### llset config

**Description:** Configure the managed Lavalink node runtime options.

All settings under this group will likely cause Audio to malfunction if changed from their defaults, only change settings here if you have been advised to by support.

**Usage:** `<@1275521742961508432>llset config`

### llset config token

**Description:** Set the managed Lavalink node's connection password.

This is the password required for Audio to connect to the managed Lavalink node.
The value by default is `youshallnotpass`.

**Usage:** `<@1275521742961508432>llset config token`

### llset config server

**Description:** Configure the managed node authorization and connection settings.

**Usage:** `<@1275521742961508432>llset config server`

### llset config server buffer

**Description:** `Dangerous command`  Set the managed Lavalink node JDA-NAS buffer size.

Only change this if you have been directly advised to, changing it can cause significant playback issues.

**Usage:** `<@1275521742961508432>llset config server buffer`

### llset config server framebuffer

**Description:** `Dangerous command` Set the managed Lavalink node framebuffer size.

Only change this if you have been directly advised to, changing it can cause significant playback issues.

**Usage:** `<@1275521742961508432>llset config server framebuffer`

### llset config bind

**Description:** `Dangerous command` Set the managed Lavalink node's binding IP address.

This value by default is `localhost` which will restrict the server to only localhost apps by default, changing this will likely break the managed Lavalink node if you don't know what you are doing.

**Usage:** `<@1275521742961508432>llset config bind`

### llset config port

**Description:** `Dangerous command` Set the managed Lavalink node's connection port.

This port is the port the managed Lavalink node binds to, you should only change this if there is a conflict with the default port because you already have an application using port 2333 on this device.

The value by default is `2333`.

**Usage:** `<@1275521742961508432>llset config port`

### llset config source

**Description:** `Dangerous command` Toggle audio sources on/off.

By default, all sources are enabled, you should only use commands here to disable a specific source if you have been advised to, disabling sources without background knowledge can cause Audio to break.

**Usage:** `<@1275521742961508432>llset config source`

### llset config source soundcloud

**Description:** Toggle Soundcloud source on or off.

This toggle controls the playback of all SoundCloud related content.

**Usage:** `<@1275521742961508432>llset config source soundcloud`

### llset config source youtube

**Description:** `Dangerous command` Toggle YouTube source on or off (this includes Spotify).

This toggle controls the playback of all YouTube and Spotify related content.

**Usage:** `<@1275521742961508432>llset config source youtube`

### llset config source local

**Description:** Toggle local file usage on or off.

This toggle controls the playback of all local track content, usually found inside the `localtracks` folder.

**Usage:** `<@1275521742961508432>llset config source local`

### llset config source http

**Description:** Toggle HTTP direct URL usage on or off.

This source is used to allow playback from direct HTTP streams (this does not affect direct URL playback for the other sources).

**Usage:** `<@1275521742961508432>llset config source http`

### llset config source bandcamp

**Description:** Toggle Bandcamp source on or off.

This toggle controls the playback of all Bandcamp related content.

**Usage:** `<@1275521742961508432>llset config source bandcamp`

### llset config source twitch

**Description:** Toggle Twitch source on or off.

This toggle controls the playback of all Twitch related content.

**Usage:** `<@1275521742961508432>llset config source twitch`

### llset config source vimeo

**Description:** Toggle Vimeo source on or off.

This toggle controls the playback of all Vimeo related content.

**Usage:** `<@1275521742961508432>llset config source vimeo`

### llset unmanaged

**Description:** Toggle using external (unmanaged) Lavalink nodes - requires an existing Lavalink node for Audio to work, if enabled.

This command disables the managed Lavalink server. If you do not have another Lavalink node set up, you will be unable to use Audio while this is enabled.

**Usage:** `<@1275521742961508432>llset unmanaged`

### llset yaml

**Description:** Uploads a copy of the application.yml file used by the managed Lavalink node.

**Usage:** `<@1275521742961508432>llset yaml`

### llset heapsize

**Description:** Set the managed Lavalink node maximum heap-size.

By default, this value is 50% of available RAM in the host machine represented by [1-1024][M|G] (256M, 256G for example)

This value only represents the maximum amount of RAM allowed to be used at any given point, and does not mean that the managed Lavalink node will always use this amount of RAM.

To reset this value to the default, run the command without any input.

**Usage:** `<@1275521742961508432>llset heapsize`

### llset password

**Description:** Set the Lavalink node password.

This command sets the connection password which Audio will use to connect to an unmanaged Lavalink node.

**Usage:** `<@1275521742961508432>llset password`

### llset info

**Description:** Display Lavalink connection settings.

**Usage:** `<@1275521742961508432>llset info`

### eq

**Description:** Equalizer management.

Band positions are 1-15 and values have a range of -0.25 to 1.0.
Band names are 25, 40, 63, 100, 160, 250, 400, 630, 1k, 1.6k, 2.5k, 4k,
6.3k, 10k, and 16k Hz.
Setting a band value to -0.25 nullifies it while +0.25 is double.

**Usage:** `<@1275521742961508432>eq`

### eq list

**Description:** List saved eq presets.

**Usage:** `<@1275521742961508432>eq list`

### eq delete

**Description:** Delete a saved eq preset.

**Usage:** `<@1275521742961508432>eq delete`

### eq set

**Description:** Set an eq band with a band number or name and value.

Band positions are 1-15 and values have a range of -0.25 to 1.0.
Band names are 25, 40, 63, 100, 160, 250, 400, 630, 1k, 1.6k, 2.5k, 4k,
6.3k, 10k, and 16k Hz.
Setting a band value to -0.25 nullifies it while +0.25 is double.

**Usage:** `<@1275521742961508432>eq set`

### eq load

**Description:** Load a saved eq preset.

**Usage:** `<@1275521742961508432>eq load`

### eq save

**Description:** Save the current eq settings to a preset.

**Usage:** `<@1275521742961508432>eq save`

### eq reset

**Description:** Reset the eq to 0 across all bands.

**Usage:** `<@1275521742961508432>eq reset`

### disconnect

**Description:** Disconnect from the voice channel.

**Usage:** `<@1275521742961508432>disconnect`

### now

**Description:** Now playing.

**Usage:** `<@1275521742961508432>now`

### pause

**Description:** Pause or resume a playing track.

**Usage:** `<@1275521742961508432>pause`

### prev

**Description:** Skip to the start of the previously played track.

**Usage:** `<@1275521742961508432>prev`

### seek

**Description:** Seek ahead or behind on a track by seconds or to a specific time.

Accepts seconds or a value formatted like 00:00:00 (`hh:mm:ss`) or 00:00 (`mm:ss`).

**Usage:** `<@1275521742961508432>seek`

### shuffle

**Description:** Toggle shuffle.

**Usage:** `<@1275521742961508432>shuffle`

### shuffle bumped

**Description:** Toggle bumped track shuffle.

Set this to disabled if you wish to avoid bumped songs being shuffled. This takes priority
over `[p]shuffle`.

**Usage:** `<@1275521742961508432>shuffle bumped`

### skip

**Description:** Skip to the next track, or to a given track number.

**Usage:** `<@1275521742961508432>skip`

### stop

**Description:** Stop playback and clear the queue.

**Usage:** `<@1275521742961508432>stop`

### summon

**Description:** Summon the bot to a voice channel.

**Usage:** `<@1275521742961508432>summon`

### volume

**Description:** Set the volume, 1% - 150%.

**Usage:** `<@1275521742961508432>volume`

### repeat

**Description:** Toggle repeat.

**Usage:** `<@1275521742961508432>repeat`

### remove

**Description:** Remove a specific track number from the queue.

**Usage:** `<@1275521742961508432>remove`

### bump

**Description:** Bump a track number to the top of the queue.

**Usage:** `<@1275521742961508432>bump`

### audioset

**Description:** Music configuration options.

**Usage:** `<@1275521742961508432>audioset`

### audioset lyrics

**Description:** Prioritise tracks with lyrics.

**Usage:** `<@1275521742961508432>audioset lyrics`

### audioset dailyqueue

**Description:** Toggle daily queues.

Daily queues creates a playlist for all tracks played today.

**Usage:** `<@1275521742961508432>audioset dailyqueue`

### audioset restrictions

**Description:** Manages the keyword whitelist and blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions`

### audioset restrictions global

**Description:** Manages the global keyword whitelist/blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions global`

### audioset restrictions global blacklist

**Description:** Manages the global keyword blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions global blacklist`

### audioset restrictions global blacklist delete

**Description:** Removes a keyword from the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions global blacklist delete`

### audioset restrictions global blacklist list

**Description:** List all keywords added to the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions global blacklist list`

### audioset restrictions global blacklist clear

**Description:** Clear all keywords added to the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions global blacklist clear`

### audioset restrictions global blacklist add

**Description:** Adds a keyword to the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions global blacklist add`

### audioset restrictions global whitelist

**Description:** Manages the global keyword whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions global whitelist`

### audioset restrictions global whitelist delete

**Description:** Removes a keyword from the whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions global whitelist delete`

### audioset restrictions global whitelist clear

**Description:** Clear all keywords from the whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions global whitelist clear`

### audioset restrictions global whitelist add

**Description:** Adds a keyword to the whitelist.

If anything is added to whitelist, it will blacklist everything else.

**Usage:** `<@1275521742961508432>audioset restrictions global whitelist add`

### audioset restrictions global whitelist list

**Description:** List all keywords added to the whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions global whitelist list`

### audioset restrictions blacklist

**Description:** Manages the keyword blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions blacklist`

### audioset restrictions blacklist list

**Description:** List all keywords added to the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions blacklist list`

### audioset restrictions blacklist clear

**Description:** Clear all keywords added to the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions blacklist clear`

### audioset restrictions blacklist add

**Description:** Adds a keyword to the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions blacklist add`

### audioset restrictions blacklist delete

**Description:** Removes a keyword from the blacklist.

**Usage:** `<@1275521742961508432>audioset restrictions blacklist delete`

### audioset restrictions whitelist

**Description:** Manages the keyword whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions whitelist`

### audioset restrictions whitelist clear

**Description:** Clear all keywords from the whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions whitelist clear`

### audioset restrictions whitelist list

**Description:** List all keywords added to the whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions whitelist list`

### audioset restrictions whitelist add

**Description:** Adds a keyword to the whitelist.

If anything is added to whitelist, it will blacklist everything else.

**Usage:** `<@1275521742961508432>audioset restrictions whitelist add`

### audioset restrictions whitelist delete

**Description:** Removes a keyword from the whitelist.

**Usage:** `<@1275521742961508432>audioset restrictions whitelist delete`

### audioset mycountrycode

**Description:** Set the country code for Spotify searches.

**Usage:** `<@1275521742961508432>audioset mycountrycode`

### audioset thumbnail

**Description:** Toggle displaying a thumbnail on audio messages.

**Usage:** `<@1275521742961508432>audioset thumbnail`

### audioset jukebox

**Description:** Set a price for queueing tracks for non-mods, 0 to disable.

**Usage:** `<@1275521742961508432>audioset jukebox`

### audioset restrict

**Description:** Toggle the domain restriction on Audio.

When toggled off, users will be able to play songs from non-commercial websites and links.
When toggled on, users are restricted to YouTube, SoundCloud, Vimeo, Twitch, and
Bandcamp links.

**Usage:** `<@1275521742961508432>audioset restrict`

### audioset maxvolume

**Description:** Set the maximum volume allowed in this server.

**Usage:** `<@1275521742961508432>audioset maxvolume`

### audioset dc

**Description:** Toggle the bot auto-disconnecting when done playing.

This setting takes precedence over `[p]audioset emptydisconnect`.

**Usage:** `<@1275521742961508432>audioset dc`

### audioset vote

**Description:** Percentage needed for non-mods to skip tracks, 0 to disable.

**Usage:** `<@1275521742961508432>audioset vote`

### audioset role

**Description:** Set the role to use for DJ mode.

**Usage:** `<@1275521742961508432>audioset role`

### audioset dj

**Description:** Toggle DJ mode.

DJ mode allows users with the DJ role to use audio commands.

**Usage:** `<@1275521742961508432>audioset dj`

### audioset cache

**Description:** Sets the caching level.

Level can be one of the following:

0: Disables all caching
1: Enables Spotify Cache
2: Enables YouTube Cache
3: Enables Lavalink Cache
5: Enables all Caches

If you wish to disable a specific cache use a negative number.

**Usage:** `<@1275521742961508432>audioset cache`

### audioset localpath

**Description:** Set the localtracks path if the Lavalink.jar is not run from the Audio data folder.

Leave the path blank to reset the path to the default, the Audio data directory.

**Usage:** `<@1275521742961508432>audioset localpath`

### audioset youtubeapi

**Description:** Instructions to set the YouTube API key.

**Usage:** `<@1275521742961508432>audioset youtubeapi`

### audioset cacheage

**Description:** Sets the cache max age.

This commands allows you to set the max number of days before an entry in the cache becomes
invalid.

**Usage:** `<@1275521742961508432>audioset cacheage`

### audioset autoplay

**Description:** Change auto-play setting.

**Usage:** `<@1275521742961508432>audioset autoplay`

### audioset autoplay reset

**Description:** Resets auto-play to the default playlist.

**Usage:** `<@1275521742961508432>audioset autoplay reset`

### audioset autoplay playlist

**Description:** Set a playlist to auto-play songs from.

**Usage**:
​ ​ ​ ​ `[p]audioset autoplay playlist playlist_name_OR_id [args]`

**Args**:
​ ​ ​ ​ The following are all optional:
​ ​ ​ ​ ​ ​ ​ ​ --scope <scope>
​ ​ ​ ​ ​ ​ ​ ​ --author [user]
​ ​ ​ ​ ​ ​ ​ ​ --guild [guild] **Only the bot owner can use this**

**Scope** is one of the following:
    ​Global
​ ​ ​ ​ Guild
​ ​ ​ ​ User

**Author** can be one of the following:
​ ​ ​ ​ User ID
​ ​ ​ ​ User Mention
​ ​ ​ ​ User Name#123

**Guild** can be one of the following:
​ ​ ​ ​ Guild ID
​ ​ ​ ​ Exact guild name

Example use:
​ ​ ​ ​ `[p]audioset autoplay playlist MyGuildPlaylist`
​ ​ ​ ​ `[p]audioset autoplay playlist MyGlobalPlaylist --scope Global`
​ ​ ​ ​ `[p]audioset autoplay playlist PersonalPlaylist --scope User --author Draper`

**Usage:** `<@1275521742961508432>audioset autoplay playlist`

### audioset autoplay toggle

**Description:** Toggle auto-play when there no songs in queue.

**Usage:** `<@1275521742961508432>audioset autoplay toggle`

### audioset status

**Description:** Enable/disable tracks' titles as status.

**Usage:** `<@1275521742961508432>audioset status`

### audioset maxlength

**Description:** Max length of a track to queue in seconds, 0 to disable.

Accepts seconds or a value formatted like 00:00:00 (`hh:mm:ss`) or 00:00 (`mm:ss`). Invalid
input will turn the max length setting off.

**Usage:** `<@1275521742961508432>audioset maxlength`

### audioset notify

**Description:** Toggle track announcement and other bot messages.

**Usage:** `<@1275521742961508432>audioset notify`

### audioset emptydisconnect

**Description:** Auto-disconnect from channel when bot is alone in it for x seconds, 0 to disable.

`[p]audioset dc` takes precedence over this setting.

**Usage:** `<@1275521742961508432>audioset emptydisconnect`

### audioset settings

**Description:** Show the current settings.

**Usage:** `<@1275521742961508432>audioset settings`

### audioset spotifyapi

**Description:** Instructions to set the Spotify API tokens.

**Usage:** `<@1275521742961508432>audioset spotifyapi`

### audioset persistqueue

**Description:** Toggle persistent queues.

Persistent queues allows the current queue to be restored when the queue closes.

**Usage:** `<@1275521742961508432>audioset persistqueue`

### audioset restart

**Description:** Restarts the lavalink connection.

**Usage:** `<@1275521742961508432>audioset restart`

### audioset emptypause

**Description:** Auto-pause after x seconds when room is empty, 0 to disable.

**Usage:** `<@1275521742961508432>audioset emptypause`

### audioset logs

**Description:** Sends the managed Lavalink node logs to your DMs.

**Usage:** `<@1275521742961508432>audioset logs`

### audioset countrycode

**Description:** Set the country code for Spotify searches.

**Usage:** `<@1275521742961508432>audioset countrycode`

### audioset globaldailyqueue

**Description:** Toggle global daily queues.

Global daily queues creates a playlist for all tracks played today.

**Usage:** `<@1275521742961508432>audioset globaldailyqueue`

### audioset autodeafen

**Description:** Toggle whether the bot will be auto deafened upon joining the voice channel.

**Usage:** `<@1275521742961508432>audioset autodeafen`

