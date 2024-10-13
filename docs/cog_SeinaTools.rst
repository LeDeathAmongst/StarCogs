SeinaTools
==========

Utility tools for [botname].

<<<<<<< HEAD
# <@1275521742961508432>spy
Yet another fun spy command.<br/>
 - Usage: `<@1275521742961508432>spy [server=None] [channel_member=None]`
=======
# ,spy
Yet another fun spy command.<br/>
 - Usage: `,spy [server=None] [channel_member=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>botstat
Yet another botstat command for Starfire.<br/>
 - Usage: `<@1275521742961508432>botstat`
=======
# ,botstat
Yet another botstat command for Starfire.<br/>
 - Usage: `,botstat`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `botstatset`


<<<<<<< HEAD
## <@1275521742961508432>botstat embed
Toggle whether botstats should use embeds.<br/>
 - Usage: `<@1275521742961508432>botstat embed <true_or_false>`
=======
## ,botstat embed
Toggle whether botstats should use embeds.<br/>
 - Usage: `,botstat embed <true_or_false>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
# <@1275521742961508432>screenshot
Screenshots a given url directly inside discord.<br/>
 - Usage: `<@1275521742961508432>screenshot <url> [wait=None]`
=======
# ,screenshot
Screenshots a given url directly inside discord.<br/>
 - Usage: `,screenshot <url> [wait=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>removebackground
Remove background from image url.<br/>
 - Usage: `<@1275521742961508432>removebackground <url>`
=======
# ,removebackground
Remove background from image url.<br/>
 - Usage: `,removebackground <url>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `removebg and rembg`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>removebackground creds
Instructions to set the removebg API token.<br/>
 - Usage: `<@1275521742961508432>removebackground creds`
 - Aliases: `setapikey and setapi`


# <@1275521742961508432>spotify
View the specified (defaults to author) user's now playing spotify status from their discord activity.<br/>
 - Usage: `<@1275521742961508432>spotify [user=None]`
=======
## ,removebackground creds
Instructions to set the removebg API token.<br/>
 - Usage: `,removebackground creds`
 - Aliases: `setapikey and setapi`


# ,spotify
View the specified (defaults to author) user's now playing spotify status from their discord activity.<br/>
 - Usage: `,spotify [user=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>spotify creds
Instructions to set the jeyyapi API token.<br/>
 - Usage: `<@1275521742961508432>spotify creds`
=======
## ,spotify emoji
Set an emoji to be used with the spotify command.<br/>
 - Usage: `,spotify emoji <emoji>`


## ,spotify creds
Instructions to set the jeyyapi API token.<br/>
 - Usage: `,spotify creds`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `setpaikey and setapi`


<<<<<<< HEAD
## <@1275521742961508432>spotify emoji
Set an emoji to be used with the spotify command.<br/>
 - Usage: `<@1275521742961508432>spotify emoji <emoji>`


# <@1275521742961508432>whatplaying
Closer lookup on what the specified user is playing.<br/>
 - Usage: `<@1275521742961508432>whatplaying [user=None]`
=======
# ,whatplaying
Closer lookup on what the specified user is playing.<br/>
 - Usage: `,whatplaying [user=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>crates
Get information about a package in Crates.io.<br/>
 - Usage: `<@1275521742961508432>crates <package_name>`
=======
# ,crates
Get information about a package in Crates.io.<br/>
 - Usage: `,crates <package_name>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `cargo, rustpkg, and crate`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>npm
Get information about a node.js module.<br/>
 - Usage: `<@1275521742961508432>npm <module_name>`
=======
# ,npm
Get information about a node.js module.<br/>
 - Usage: `,npm <module_name>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `node, npmpkg, and nodepkg`
Extended Arg Info
> ### module_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>ruby
Get information about a rubygem package.<br/>
 - Usage: `<@1275521742961508432>ruby <package_name>`
=======
# ,ruby
Get information about a rubygem package.<br/>
 - Usage: `,ruby <package_name>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `rubygem, rubypkg, and rubygems`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


