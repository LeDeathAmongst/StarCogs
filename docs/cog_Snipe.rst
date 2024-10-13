Snipe
=====

Bulk sniping deleted and edited messages, for moderation purpose!

<<<<<<< HEAD
# <@1275521742961508432>snipe (Hybrid Command)
Bulk snipe deleted messages.<br/>
 - Usage: `<@1275521742961508432>snipe <channel> [index=0]`
=======
# ,snipe (Hybrid Command)
Bulk snipe deleted messages.<br/>
 - Usage: `,snipe <channel> [index=0]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/snipe <channel> [index=0]`
 - Restricted to: `MOD`
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
> ### index: int = 0
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>snipe list (Hybrid Command)
List deleted messages.<br/>
 - Usage: `<@1275521742961508432>snipe list <channel> [member]`
=======
## ,snipe list (Hybrid Command)
List deleted messages.<br/>
 - Usage: `,snipe list <channel> [member]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/snipe list <channel> [member]`
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
> ### member: Union[discord.member.Member, discord.user.User] = None
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
## <@1275521742961508432>snipe index (Hybrid Command)
Snipe a deleted message.<br/>
 - Usage: `<@1275521742961508432>snipe index <channel> [index=0]`
=======
## ,snipe embeds (Hybrid Command)
Bulk snipe deleted messages with embeds.<br/>
 - Usage: `,snipe embeds <channel>`
 - Slash Usage: `/snipe embeds <channel>`
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


## ,snipe index (Hybrid Command)
Snipe a deleted message.<br/>
 - Usage: `,snipe index <channel> [index=0]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/snipe index <channel> [index=0]`
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
> ### index: int = 0
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>snipe rolesmentions (Hybrid Command)
Bulk snipe deleted messages with roles mentions.<br/>
 - Usage: `<@1275521742961508432>snipe rolesmentions <channel>`
 - Slash Usage: `/snipe rolesmentions <channel>`
=======
## ,snipe bulk (Hybrid Command)
Bulk snipe deleted messages.<br/>
 - Usage: `,snipe bulk <channel>`
 - Slash Usage: `/snipe bulk <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>snipe membersmentions (Hybrid Command)
Bulk snipe deleted messages with members mentions.<br/>
 - Usage: `<@1275521742961508432>snipe membersmentions <channel>`
 - Slash Usage: `/snipe membersmentions <channel>`
 - Aliases: `usersmentions`
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


## <@1275521742961508432>snipe embeds (Hybrid Command)
Bulk snipe deleted messages with embeds.<br/>
 - Usage: `<@1275521742961508432>snipe embeds <channel>`
 - Slash Usage: `/snipe embeds <channel>`
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


## <@1275521742961508432>snipe mentions (Hybrid Command)
Bulk snipe deleted messages with roles/users mentions.<br/>
 - Usage: `<@1275521742961508432>snipe mentions <channel>`
 - Slash Usage: `/snipe mentions <channel>`
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


## <@1275521742961508432>snipe member (Hybrid Command)
Bulk snipe deleted messages for the specified member.<br/>
 - Usage: `<@1275521742961508432>snipe member <channel> <member>`
=======
## ,snipe member (Hybrid Command)
Bulk snipe deleted messages for the specified member.<br/>
 - Usage: `,snipe member <channel> <member>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/snipe member <channel> <member>`
 - Aliases: `user`
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
> ### member: Union[discord.member.Member, discord.user.User]
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
## <@1275521742961508432>snipe bulk (Hybrid Command)
Bulk snipe deleted messages.<br/>
 - Usage: `<@1275521742961508432>snipe bulk <channel>`
 - Slash Usage: `/snipe bulk <channel>`
=======
## ,snipe rolesmentions (Hybrid Command)
Bulk snipe deleted messages with roles mentions.<br/>
 - Usage: `,snipe rolesmentions <channel>`
 - Slash Usage: `/snipe rolesmentions <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>esnipe (Hybrid Command)
Bulk snipe edited messages.<br/>
 - Usage: `<@1275521742961508432>esnipe <channel> [index=0]`
=======
## ,snipe membersmentions (Hybrid Command)
Bulk snipe deleted messages with members mentions.<br/>
 - Usage: `,snipe membersmentions <channel>`
 - Slash Usage: `/snipe membersmentions <channel>`
 - Aliases: `usersmentions`
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


## ,snipe mentions (Hybrid Command)
Bulk snipe deleted messages with roles/users mentions.<br/>
 - Usage: `,snipe mentions <channel>`
 - Slash Usage: `/snipe mentions <channel>`
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


# ,esnipe (Hybrid Command)
Bulk snipe edited messages.<br/>
 - Usage: `,esnipe <channel> [index=0]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/esnipe <channel> [index=0]`
 - Restricted to: `MOD`
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
> ### index: int = 0
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>esnipe mentions (Hybrid Command)
Bulk snipe edited messages with roles/users mentions.<br/>
 - Usage: `<@1275521742961508432>esnipe mentions <channel>`
 - Slash Usage: `/esnipe mentions <channel>`
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


## <@1275521742961508432>esnipe list (Hybrid Command)
List edited messages.<br/>
 - Usage: `<@1275521742961508432>esnipe list <channel> [member]`
 - Slash Usage: `/esnipe list <channel> [member]`
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
> ### member: Union[discord.member.Member, discord.user.User] = None
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


## <@1275521742961508432>esnipe embeds (Hybrid Command)
Bulk snipe edited messages with embeds.<br/>
 - Usage: `<@1275521742961508432>esnipe embeds <channel>`
 - Slash Usage: `/esnipe embeds <channel>`
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


## <@1275521742961508432>esnipe index (Hybrid Command)
Snipe an edited message.<br/>
 - Usage: `<@1275521742961508432>esnipe index <channel> [index=0]`
 - Slash Usage: `/esnipe index <channel> [index=0]`
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
> ### index: int = 0
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>esnipe bulk (Hybrid Command)
Bulk snipe edited messages.<br/>
 - Usage: `<@1275521742961508432>esnipe bulk <channel>`
=======
## ,esnipe bulk (Hybrid Command)
Bulk snipe edited messages.<br/>
 - Usage: `,esnipe bulk <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/esnipe bulk <channel>`
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


<<<<<<< HEAD
## <@1275521742961508432>esnipe membersmentions (Hybrid Command)
Bulk snipe edited messages with members mentions.<br/>
 - Usage: `<@1275521742961508432>esnipe membersmentions <channel>`
 - Slash Usage: `/esnipe membersmentions <channel>`
 - Aliases: `usersmentions`
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


## <@1275521742961508432>esnipe rolesmentions (Hybrid Command)
Bulk snipe edited messages with roles mentions.<br/>
 - Usage: `<@1275521742961508432>esnipe rolesmentions <channel>`
 - Slash Usage: `/esnipe rolesmentions <channel>`
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


## <@1275521742961508432>esnipe member (Hybrid Command)
Bulk snipe edited messages for the specified member.<br/>
 - Usage: `<@1275521742961508432>esnipe member <channel> <member>`
=======
## ,esnipe member (Hybrid Command)
Bulk snipe edited messages for the specified member.<br/>
 - Usage: `,esnipe member <channel> <member>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/esnipe member <channel> <member>`
 - Aliases: `user`
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
> ### member: Union[discord.member.Member, discord.user.User]
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
# <@1275521742961508432>setsnipe (Hybrid Command)
Commands to configure Snipe.<br/>
 - Usage: `<@1275521742961508432>setsnipe`
=======
## ,esnipe embeds (Hybrid Command)
Bulk snipe edited messages with embeds.<br/>
 - Usage: `,esnipe embeds <channel>`
 - Slash Usage: `/esnipe embeds <channel>`
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


## ,esnipe mentions (Hybrid Command)
Bulk snipe edited messages with roles/users mentions.<br/>
 - Usage: `,esnipe mentions <channel>`
 - Slash Usage: `/esnipe mentions <channel>`
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


## ,esnipe membersmentions (Hybrid Command)
Bulk snipe edited messages with members mentions.<br/>
 - Usage: `,esnipe membersmentions <channel>`
 - Slash Usage: `/esnipe membersmentions <channel>`
 - Aliases: `usersmentions`
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


## ,esnipe list (Hybrid Command)
List edited messages.<br/>
 - Usage: `,esnipe list <channel> [member]`
 - Slash Usage: `/esnipe list <channel> [member]`
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
> ### member: Union[discord.member.Member, discord.user.User] = None
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


## ,esnipe index (Hybrid Command)
Snipe an edited message.<br/>
 - Usage: `,esnipe index <channel> [index=0]`
 - Slash Usage: `/esnipe index <channel> [index=0]`
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
> ### index: int = 0
> ```
> A number without decimal places.
> ```


## ,esnipe rolesmentions (Hybrid Command)
Bulk snipe edited messages with roles mentions.<br/>
 - Usage: `,esnipe rolesmentions <channel>`
 - Slash Usage: `/esnipe rolesmentions <channel>`
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


# ,setsnipe (Hybrid Command)
Commands to configure Snipe.<br/>
 - Usage: `,setsnipe`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setsnipe`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>setsnipe showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>setsnipe showsettings [with_dev=False]`
=======
## ,setsnipe showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setsnipe showsettings [with_dev=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setsnipe showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setsnipe modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `<@1275521742961508432>setsnipe modalconfig [confirmation=False]`
=======
## ,setsnipe ignored (Hybrid Command)
Set if the deleted and edited messages in this server will be ignored.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setsnipe ignored <value>`
 - Slash Usage: `/setsnipe ignored <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setsnipe resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setsnipe resetsetting <setting>`
 - Slash Usage: `/setsnipe resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,setsnipe modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setsnipe modalconfig [confirmation=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setsnipe modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setsnipe ignored (Hybrid Command)
Set if the deleted and edited messages in this server will be ignored.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setsnipe ignored <value>`
 - Slash Usage: `/setsnipe ignored <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setsnipe stats (Hybrid Command)
Show stats about Snipe cache.<br/>
 - Usage: `<@1275521742961508432>setsnipe stats`
=======
## ,setsnipe stats (Hybrid Command)
Show stats about Snipe cache.<br/>
 - Usage: `,setsnipe stats`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setsnipe stats`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>setsnipe resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `<@1275521742961508432>setsnipe resetsetting <setting>`
 - Slash Usage: `/setsnipe resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setsnipe ignoredchannels (Hybrid Command)
=======
## ,setsnipe ignoredchannels (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Set the channels in which deleted and edited messages will be ignored.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setsnipe ignoredchannels <value>`
=======
 - Usage: `,setsnipe ignoredchannels <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setsnipe ignoredchannels <value>`
 - Checks: `server_only`


