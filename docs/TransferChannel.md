A cog to transfer messages from a channel to another channel, with many options!

# ,transferchannel (Hybrid Command)
Transfer messages from a channel to another channel, with many options. This might take a long time.<br/>
You can specify the id of a channel from another server.<br/>

`source` is partial name or ID of the source channel<br/>
`destination` is partial name or ID of the destination channel<br/>
`way` is the used way<br/>
- `embed` Do you want to transfer the message as an embed?<br/>
- `webhook` Do you want to send the messages with webhooks (name and avatar of the original author)?<br/>
- `message`Do you want to transfer the message as a simple message?<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel`
 - Slash Usage: `/transferchannel`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `channeltransfer`
## ,transferchannel all (Hybrid Command)
Transfer all messages from a channel to another channel. This might take a long time.<br/>

Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel all <source> <destination> [way=webhooks] [exclude_users_and_roles=[]]`
 - Slash Usage: `/transferchannel all <source> <destination> [way=webhooks] [exclude_users_and_roles=[]]`
Extended Arg Info
> ### source: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,transferchannel before (Hybrid Command)
Transfer a part of the messages from a channel to another channel. This might take a long time.<br/>

Specify the before message (id or link) or a valid Discord snowflake.<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel before <source> <destination> <before> [way=webhooks] [exclude_users_and_roles=[]]`
 - Slash Usage: `/transferchannel before <source> <destination> <before> [way=webhooks] [exclude_users_and_roles=[]]`
Extended Arg Info
> ### source: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,transferchannel between (Hybrid Command)
Transfer a part of the messages from a channel to another channel. This might take a long time.<br/>

Specify the between messages (id or link) or a valid snowflake.<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel between <source> <destination> <before> <after> [way=webhooks] [exclude_users_and_roles=[]]`
 - Slash Usage: `/transferchannel between <source> <destination> <before> <after> [way=webhooks] [exclude_users_and_roles=[]]`
Extended Arg Info
> ### source: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,transferchannel bot (Hybrid Command)
Transfer a part of the messages from a channel to another channel. This might take a long time.<br/>

Specify the bool option.<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel bot <source> <destination> [bot=True] [limit=None] [way=webhooks] [exclude_users_and_roles=[]]`
 - Slash Usage: `/transferchannel bot <source> <destination> [bot=True] [limit=None] [way=webhooks] [exclude_users_and_roles=[]]`
Extended Arg Info
> ### source: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### bot: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### limit: Optional[int] = None
> ```
> A number without decimal places.
> ```
## ,transferchannel messages (Hybrid Command)
Transfer a part of the messages from a channel to another channel. This might take a long time.<br/>

Specify the number of messages since the end of the channel.<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel messages <source> <destination> <limit> [way=webhooks] [exclude_users_and_roles=[]]`
 - Slash Usage: `/transferchannel messages <source> <destination> <limit> [way=webhooks] [exclude_users_and_roles=[]]`
Extended Arg Info
> ### source: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### limit: int
> ```
> A number without decimal places.
> ```
## ,transferchannel user (Hybrid Command)
Transfer a part of the messages from a channel to another channel. This might take a long time.<br/>

Specify the user/member (id, name or mention).<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel user <source> <destination> <user> [limit=None] [way=webhooks]`
 - Slash Usage: `/transferchannel user <source> <destination> <user> [limit=None] [way=webhooks]`
Extended Arg Info
> ### source: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
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
> ### limit: Optional[int] = None
> ```
> A number without decimal places.
> ```
## ,transferchannel message (Hybrid Command)
Transfer a specific message to another channel. This might take a long time.<br/>

Specify the message to transfer, with its ID or its link.<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel message <message> <destination> [way=webhooks]`
 - Slash Usage: `/transferchannel message <message> <destination> [way=webhooks]`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,transferchannel after (Hybrid Command)
Transfer a part of the messages from a channel to another channel. This might take a long time.<br/>

Specify the after message (id or link) or a valid Discord snowflake.<br/>
Remember that transfering other users' messages does not respect the TOS.<br/>
 - Usage: `,transferchannel after <source> <destination> <after> [way=webhooks] [exclude_users_and_roles=[]]`
 - Slash Usage: `/transferchannel after <source> <destination> <after> [way=webhooks] [exclude_users_and_roles=[]]`
Extended Arg Info
> ### source: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
