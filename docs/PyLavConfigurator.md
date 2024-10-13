Configure PyLav library settings

# ,plset
Change global settings for PyLav<br/>
 - Usage: `,plset`
 - Aliases: `plconfig`
## ,plset version
Show the version of the Cog and PyLav<br/>
 - Usage: `,plset version`
## ,plset dj
Checks if a user or role is considered a disc jockey<br/>
 - Usage: `,plset dj <role_or_member>`
 - Checks: `server_only`
Extended Arg Info
> ### role_or_member: Union[discord.role.Role, discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,plset info
Show the setting values<br/>
 - Usage: `,plset info`
## ,plset spotifyapi
Instructions on how to set the Spotify API Tokens<br/>
 - Usage: `,plset spotifyapi`
 - Restricted to: `BOT_OWNER`
## ,plset activity
Toggle whether or not I should update my Discord activity when playing tracks.<br/>
 - Usage: `,plset activity`
 - Restricted to: `BOT_OWNER`
## ,plset tracks
Set the local tracks folder for PyLav.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `,plset tracks <create> <folder>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### create: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### folder: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,plset stats
Manage active players<br/>
 - Usage: `,plset stats [server]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: discord.server.Guild = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## ,plset node
Change the managed node configuration<br/>
 - Usage: `,plset node`
 - Restricted to: `BOT_OWNER`
### ,plset node updates
Toggle the managed node auto updates on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `,plset node updates`
### ,plset node toggle
Toggle the managed node on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `,plset node toggle`
### ,plset node external
Change the bundled external nodes state<br/>
 - Usage: `,plset node external`
#### ,plset node external lavalink
Toggle the managed external lava.link node on/off<br/>
 - Usage: `,plset node external lavalink`
