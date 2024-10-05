SeinaTools
==========

Utility tools for [botname].

# <@1275521742961508432>spy
Yet another fun spy command.<br/>
 - Usage: `<@1275521742961508432>spy [server=None] [channel_member=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: Union[discord.server.Guild, int] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
> ### channel_member: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>botstat
Yet another botstat command for Starfire.<br/>
 - Usage: `<@1275521742961508432>botstat`
 - Restricted to: `BOT_OWNER`
 - Aliases: `botstatset`


## <@1275521742961508432>botstat embed
Toggle whether botstats should use embeds.<br/>
 - Usage: `<@1275521742961508432>botstat embed <true_or_false>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>screenshot
Screenshots a given url directly inside discord.<br/>
 - Usage: `<@1275521742961508432>screenshot <url> [wait=None]`
 - Restricted to: `BOT_OWNER`
 - Aliases: `ss`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### wait: Optional[int] = None
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>removebackground
Remove background from image url.<br/>
 - Usage: `<@1275521742961508432>removebackground <url>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `removebg and rembg`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>removebackground creds
Instructions to set the removebg API token.<br/>
 - Usage: `<@1275521742961508432>removebackground creds`
 - Aliases: `setapikey and setapi`


# <@1275521742961508432>spotify
View the specified (defaults to author) user's now playing spotify status from their discord activity.<br/>
 - Usage: `<@1275521742961508432>spotify [user=None]`
 - Checks: `server_only`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     


## <@1275521742961508432>spotify emoji
Set an emoji to be used with the spotify command.<br/>
 - Usage: `<@1275521742961508432>spotify emoji <emoji>`


## <@1275521742961508432>spotify creds
Instructions to set the jeyyapi API token.<br/>
 - Usage: `<@1275521742961508432>spotify creds`
 - Restricted to: `BOT_OWNER`
 - Aliases: `setpaikey and setapi`


# <@1275521742961508432>whatplaying
Closer lookup on what the specified user is playing.<br/>
 - Usage: `<@1275521742961508432>whatplaying [user=None]`
 - Aliases: `whatgame`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     


# <@1275521742961508432>crates
Get information about a package in Crates.io.<br/>
 - Usage: `<@1275521742961508432>crates <package_name>`
 - Aliases: `cargo, rustpkg, and crate`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>npm
Get information about a node.js module.<br/>
 - Usage: `<@1275521742961508432>npm <module_name>`
 - Aliases: `node, npmpkg, and nodepkg`
Extended Arg Info
> ### module_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>ruby
Get information about a rubygem package.<br/>
 - Usage: `<@1275521742961508432>ruby <package_name>`
 - Aliases: `rubygem, rubypkg, and rubygems`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


