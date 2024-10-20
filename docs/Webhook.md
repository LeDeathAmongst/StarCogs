Various webhook commands to create and send messages along webhooks!

# ,webhook (Hybrid Command)
Various webhook commands to create and send messages along webhooks.<br/>
 - Usage: `,webhook`
 - Slash Usage: `/webhook`
 - Restricted to: `ADMIN`
 - Aliases: `webhooks`
 - Checks: `server_only`
## ,webhook permissions (Hybrid Command)
Show all members in the server that have the permission `manage_webhooks`.<br/>
 - Usage: `,webhook permissions`
 - Slash Usage: `/webhook permissions`
 - Restricted to: `MOD`
 - Aliases: `perms`
 - Checks: `server_only`
## ,webhook session (Hybrid Command)
Initiate a session within this channel sending messages to a specified webhook link.<br/>
 - Usage: `,webhook session <webhook_link>`
 - Slash Usage: `/webhook session <webhook_link>`
 - Checks: `server_only`
## ,webhook reverse (Hybrid Command)

 - Usage: `,webhook reverse <channel> <member> [content]`
 - Slash Usage: `/webhook reverse <channel> <member> [content]`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### member: discord.member.Member
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
## ,webhook freverse (Hybrid Command)

 - Usage: `,webhook freverse <channel> <member> [content]`
 - Slash Usage: `/webhook freverse <channel> <member> [content]`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### member: discord.member.Member
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
## ,webhook clear (Hybrid Command)
Delete all webhooks in this server.<br/>
 - Usage: `,webhook clear [confirmation=False]`
 - Slash Usage: `/webhook clear [confirmation=False]`
 - Restricted to: `GUILD_OWNER`
 - Checks: `bot_has_server_permissions and server_only`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,webhook send (Hybrid Command)
Sends a message to the specified webhook using your display name and you avatar.<br/>
 - Usage: `,webhook send <webhook_link> <content>`
 - Slash Usage: `/webhook send <webhook_link> <content>`
 - Checks: `server_only`
## ,webhook reversed (Hybrid Command)

 - Usage: `,webhook reversed <channel> <message>`
 - Slash Usage: `/webhook reversed <channel> <message>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
## ,webhook custom (Hybrid Command)
Sends a message a channel as a webhook using a specified display name and a specified avatar url.<br/>

You can attach files to the command.<br/>
 - Usage: `,webhook custom <channel> <username> <avatar_url> [content]`
 - Slash Usage: `/webhook custom <channel> <username> <avatar_url> [content]`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### avatar_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,webhook say (Hybrid Command)
Sends a message in a channel as a webhook using your display name and your avatar.<br/>

You can attach files to the command.<br/>
 - Usage: `,webhook say <channel> [content]`
 - Slash Usage: `/webhook say <channel> [content]`
 - Aliases: `speak`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,webhook edit (Hybrid Command)
Edit a message sent by a webhook.<br/>

You can attach files to the command.<br/>
 - Usage: `,webhook edit <message> [content]`
 - Slash Usage: `/webhook edit <message> [content]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
> ### content: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,webhook closesession (Hybrid Command)
Close an ongoing webhook session in a channel.<br/>
 - Usage: `,webhook closesession [channel=None]`
 - Slash Usage: `/webhook closesession [channel=None]`
 - Aliases: `sessionclose`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,webhook create (Hybrid Command)
Creates a webhook in the channel specified with the name specified.<br/>

If no channel is specified then it will default to the current channel.<br/>
 - Usage: `,webhook create <channel> [webhook_name]`
 - Slash Usage: `/webhook create <channel> [webhook_name]`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### webhook_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,webhook clyde (Hybrid Command)
Sends a message a channel as a webhook using Clyde's display name and avatar.<br/>

You can attach files to the command.<br/>
 - Usage: `,webhook clyde <channel> [content]`
 - Slash Usage: `/webhook clyde <channel> [content]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,webhook sudo (Hybrid Command)
Sends a message in a channel as a webhook using the display name and the avatar of a specified member.<br/>

You can attach files to the command.<br/>
 - Usage: `,webhook sudo <channel> <member> [content]`
 - Slash Usage: `/webhook sudo <channel> <member> [content]`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### member: discord.member.Member
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