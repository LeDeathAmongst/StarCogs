Avatar
======

Get a user's global/guild avatar in an embed, with settings to manage the embed.

<<<<<<< HEAD
# <@1275521742961508432>avatar (Hybrid Command)
=======
# ,avatar (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Returns a user's avatar assets as an embed. (see help)<br/>

> optional - [user] = `@mention` / `username` / `id`<br/>
> optional - [type] = `global` / `server` / `deco` (default=global)<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>avatar <user> <type>`
=======
 - Usage: `,avatar <user> <type>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/avatar <user> <type>`
 - Checks: `server_only`
Extended Arg Info
> ### user: Union[discord.member.Member, discord.user.User, NoneType]
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
# <@1275521742961508432>avatar_embed
Avatar embed settings for bot owner.<br/>

> With this, you have the ability to change embed color or disable the embed altogether.<br/>
 - Usage: `<@1275521742961508432>avatar_embed`
=======
# ,avatar_embed
Avatar embed settings for bot owner.<br/>

> With this, you have the ability to change embed color or disable the embed altogether.<br/>
 - Usage: `,avatar_embed`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>avatar_embed color
Set embed color for avatar (defaults to role color)<br/>

> Use a hex color code or 'clear' to reset to the default color.<br/>
 - Usage: `<@1275521742961508432>avatar_embed color <color>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### color: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>avatar_embed show
Enable or disable avatar embed.<br/>

> Use `true` to enable embed or `false` to disable embed.<br/>
 - Usage: `<@1275521742961508432>avatar_embed show <show>`
=======
## ,avatar_embed show
Enable or disable avatar embed.<br/>

> Use `true` to enable embed or `false` to disable embed.<br/>
 - Usage: `,avatar_embed show <show>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### show: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
=======
## ,avatar_embed color
Set embed color for avatar (defaults to role color)<br/>

> Use a hex color code or 'clear' to reset to the default color.<br/>
 - Usage: `,avatar_embed color <color>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### color: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


>>>>>>> 9e308722 (Revamped and Fixed)
