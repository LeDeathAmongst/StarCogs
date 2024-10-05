Configure PyLav library settings

# <@1275521742961508432>plset
Change global settings for PyLav<br/>
 - Usage: `<@1275521742961508432>plset`
 - Aliases: `plconfig`
## <@1275521742961508432>plset dj
Checks if a user or role is considered a disc jockey<br/>
 - Usage: `<@1275521742961508432>plset dj <role_or_member>`
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
## <@1275521742961508432>plset spotifyapi
Instructions on how to set the Spotify API Tokens<br/>
 - Usage: `<@1275521742961508432>plset spotifyapi`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>plset info
Show the setting values<br/>
 - Usage: `<@1275521742961508432>plset info`
## <@1275521742961508432>plset version
Show the version of the Cog and PyLav<br/>
 - Usage: `<@1275521742961508432>plset version`
## <@1275521742961508432>plset activity
Toggle whether or not I should update my Discord activity when playing tracks.<br/>
 - Usage: `<@1275521742961508432>plset activity`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>plset tracks
Set the local tracks folder for PyLav.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `<@1275521742961508432>plset tracks <create> <folder>`
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
## <@1275521742961508432>plset stats
Manage active players<br/>
 - Usage: `<@1275521742961508432>plset stats [server]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: discord.server.Guild = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## <@1275521742961508432>plset node
Change the managed node configuration<br/>
 - Usage: `<@1275521742961508432>plset node`
 - Restricted to: `BOT_OWNER`
### <@1275521742961508432>plset node updates
Toggle the managed node auto updates on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `<@1275521742961508432>plset node updates`
### <@1275521742961508432>plset node external
Change the bundled external nodes state<br/>
 - Usage: `<@1275521742961508432>plset node external`
#### <@1275521742961508432>plset node external lavalink
Toggle the managed external lava.link node on/off<br/>
 - Usage: `<@1275521742961508432>plset node external lavalink`
### <@1275521742961508432>plset node toggle
Toggle the managed node on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `<@1275521742961508432>plset node toggle`
