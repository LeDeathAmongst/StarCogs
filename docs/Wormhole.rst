Wormhole
========

# <@1275521742961508432>wormhole
Manage wormhole connections.<br/>
 - Usage: `<@1275521742961508432>wormhole`
 - Aliases: `wm`


## <@1275521742961508432>wormhole addwordfilter
Add a word to the wormhole word filter.<br/>
 - Usage: `<@1275521742961508432>wormhole addwordfilter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>wormhole close
Unlink the current channel from the wormhole network.<br/>
 - Usage: `<@1275521742961508432>wormhole close`


## <@1275521742961508432>wormhole open
Link the current channel to the wormhole network.<br/>
 - Usage: `<@1275521742961508432>wormhole open`


## <@1275521742961508432>wormhole name
Set the name mode for webhooks. Options: user, server, both<br/>
 - Usage: `<@1275521742961508432>wormhole name <mode>`
Extended Arg Info
> ### mode: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>wormhole globalblacklist
Prevent specific members from sending messages through the wormhole globally.<br/>
 - Usage: `<@1275521742961508432>wormhole globalblacklist <user>`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     


## <@1275521742961508432>wormhole unglobalblacklist
Command to remove a user from the global wormhole blacklist (Bot Owner Only).<br/>
 - Usage: `<@1275521742961508432>wormhole unglobalblacklist <user>`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     


## <@1275521742961508432>wormhole image
Set the image mode for webhooks. Options: user, server<br/>
 - Usage: `<@1275521742961508432>wormhole image <mode>`
Extended Arg Info
> ### mode: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>wormhole removementionbypass
Remove a user's bypass for the mention filter.<br/>
 - Usage: `<@1275521742961508432>wormhole removementionbypass <user>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     


## <@1275521742961508432>wormhole addmentionbypass
Allow a user to bypass the mention filter.<br/>
 - Usage: `<@1275521742961508432>wormhole addmentionbypass <user>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     


## <@1275521742961508432>wormhole removewordfilter
Remove a word from the wormhole word filter.<br/>
 - Usage: `<@1275521742961508432>wormhole removewordfilter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>wormhole webhook
Enable or disable the use of webhooks.<br/>
 - Usage: `<@1275521742961508432>wormhole webhook <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


