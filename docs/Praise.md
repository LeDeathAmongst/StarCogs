Praise Kink style cog for Red-DiscordBot

# ,praise
Praise a user with a default or custom message.<br/>
 - Usage: `,praise [target=None] [custom_message]`
Extended Arg Info
> ### target: discord.member.Member = None
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
> ### custom_message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,praise role
Praise a role with a default or custom message.<br/>
 - Usage: `,praise role <target> [custom_message]`
Extended Arg Info
> ### target: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### custom_message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,praise remove
Remove a praise message by its UUID.<br/>
 - Usage: `,praise remove <praise_id>`
Extended Arg Info
> ### praise_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,praise list
List all praise messages.<br/>
 - Usage: `,praise list`
## ,praise add
Add a new praise message to the list.<br/>
 - Usage: `,praise add <new_praise>`
Extended Arg Info
> ### new_praise: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
