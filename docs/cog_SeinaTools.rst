SeinaTools
==========

Utility tools for [botname].

# ,spy
Yet another fun spy command.<br/>
 - Usage: `,spy [server=None] [channel_member=None]`
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


# ,botstat
Yet another botstat command for Starfire.<br/>
 - Usage: `,botstat`
 - Restricted to: `BOT_OWNER`
 - Aliases: `botstatset`


## ,botstat embed
Toggle whether botstats should use embeds.<br/>
 - Usage: `,botstat embed <true_or_false>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


# ,screenshot
Screenshots a given url directly inside discord.<br/>
 - Usage: `,screenshot <url> [wait=None]`
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


# ,removebackground
Remove background from image url.<br/>
 - Usage: `,removebackground <url>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `removebg and rembg`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,removebackground creds
Instructions to set the removebg API token.<br/>
 - Usage: `,removebackground creds`
 - Aliases: `setapikey and setapi`


# ,spotify
View the specified (defaults to author) user's now playing spotify status from their discord activity.<br/>
 - Usage: `,spotify [user=None]`
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


## ,spotify emoji
Set an emoji to be used with the spotify command.<br/>
 - Usage: `,spotify emoji <emoji>`


## ,spotify creds
Instructions to set the jeyyapi API token.<br/>
 - Usage: `,spotify creds`
 - Restricted to: `BOT_OWNER`
 - Aliases: `setpaikey and setapi`


# ,whatplaying
Closer lookup on what the specified user is playing.<br/>
 - Usage: `,whatplaying [user=None]`
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


# ,crates
Get information about a package in Crates.io.<br/>
 - Usage: `,crates <package_name>`
 - Aliases: `cargo, rustpkg, and crate`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,npm
Get information about a node.js module.<br/>
 - Usage: `,npm <module_name>`
 - Aliases: `node, npmpkg, and nodepkg`
Extended Arg Info
> ### module_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,ruby
Get information about a rubygem package.<br/>
 - Usage: `,ruby <package_name>`
 - Aliases: `rubygem, rubypkg, and rubygems`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


