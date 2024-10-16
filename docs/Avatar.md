Get a user's global/guild avatar in an embed, with settings to manage the embed.

# ,avatar (Hybrid Command)
Returns a user's avatar assets as an embed. (see help)<br/>

> optional - [user] = `@mention` / `username` / `id`<br/>
> optional - [type] = `global` / `server` / `deco` (default=global)<br/>
 - Usage: `,avatar <user> <type>`
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
# ,avatar_embed
Avatar embed settings for bot owner.<br/>

> With this, you have the ability to change embed color or disable the embed altogether.<br/>
 - Usage: `,avatar_embed`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
## ,avatar_embed show
Enable or disable avatar embed.<br/>

> Use `true` to enable embed or `false` to disable embed.<br/>
 - Usage: `,avatar_embed show <show>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### show: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
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
