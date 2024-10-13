RequestGB
=========

Cog for handling global ban requests.

# ,requestgb
Group for global ban request commands.<br/>
 - Usage: `,requestgb [user_id=None] [proof]`
 - Aliases: `reqgb and rgb`
Extended Arg Info
> ### user_id: int = None
> ```
> A number without decimal places.
> ```
> ### proof: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,requestgb optout
Opt-out the server from the global ban feature.<br/>
 - Usage: `,requestgb optout`
 - Restricted to: `GUILD_OWNER`


## ,requestgb addtrusted
Add a trusted user who can approve/deny global ban requests.<br/>
 - Usage: `,requestgb addtrusted <user>`
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


## ,requestgb deny
Deny a global ban request.<br/>
 - Usage: `,requestgb deny <user_id> [deny_reason]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
> ### deny_reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,requestgb optin
Opt-in the server to the global ban feature.<br/>
 - Usage: `,requestgb optin`
 - Restricted to: `GUILD_OWNER`


## ,requestgb setreq
Set the channel for global ban notifications.<br/>
 - Usage: `,requestgb setreq <channel>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,requestgb approve
Approve a global ban request.<br/>
 - Usage: `,requestgb approve <user_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


## ,requestgb setlog
Set the log channel for global ban approvals.<br/>
 - Usage: `,requestgb setlog <channel>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


