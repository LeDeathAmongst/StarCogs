Get a user's banner in an embed, with settings to manage the embed.

# ,banner (Hybrid Command)
Returns a user's banner as an embed.<br/>

> optional - [user] = `@mention` / `username` / `id`<br/>
 - Usage: `,banner [user=None]`
 - Slash Usage: `/banner [user=None]`
 - Checks: `server_only`
Extended Arg Info
> ### user: Union[discord.member.Member, discord.user.User, NoneType] = None
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
# ,banner_embed
Banner embed settings for bot owner.<br/>

> With this, you have the ability to change embed color or disable the embed altogether.<br/>
 - Usage: `,banner_embed`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
## ,banner_embed color
Set embed color for banner (defaults to role color)<br/>

> Use a hex color code or 'clear' to reset to the default color.<br/>
 - Usage: `,banner_embed color <color>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### color: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,banner_embed show
Enable or disable banner embed.<br/>

> Use `true` to enable embed or `false` to disable embed.<br/>
 - Usage: `,banner_embed show <show>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### show: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
