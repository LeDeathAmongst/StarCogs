MemberPrefix
============

A cog to allow a member to choose custom prefixes, just for them!

# ,memberprefix (Hybrid Command)
Sets Starfire's prefix(es) for you only.<br/>
Warning: This is not additive. It will replace all current prefixes.<br/>
The real prefixes will no longer work for you.<br/>

**Examples:**<br/>
    - `,memberprefix !`<br/>
    - `,memberprefix "! "` - Quotes are needed to use spaces in prefixes.<br/>
    - `,memberprefix ! ? .` - Sets multiple prefixes.<br/>
**Arguments:**<br/>
    - `<prefixes...>` - The prefixes the bot will respond for you only.<br/>
 - Usage: `,memberprefix <prefixes>`
 - Slash Usage: `/memberprefix <prefixes>`
 - Aliases: `memberprefixes`
 - Checks: `server_only`


# ,setmemberprefix (Hybrid Command)
Configure MemberPrefix.<br/>
 - Usage: `,setmemberprefix`
 - Slash Usage: `/setmemberprefix`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


## ,setmemberprefix resetmemberprefix (Hybrid Command)
Clear prefixes for a specified member in a specified server.<br/>
 - Usage: `,setmemberprefix resetmemberprefix <server> <user>`
 - Slash Usage: `/setmemberprefix resetmemberprefix <server> <user>`
 - Checks: `server_only`
Extended Arg Info
> ### server: discord.server.Guild
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
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


## ,setmemberprefix purge (Hybrid Command)
Clear all members prefixes for a specified server.<br/>
 - Usage: `,setmemberprefix purge <server>`
 - Slash Usage: `/setmemberprefix purge <server>`
 - Checks: `server_only`
Extended Arg Info
> ### server: discord.server.Guild
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     


