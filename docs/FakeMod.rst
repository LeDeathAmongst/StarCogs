FakeMod
=======

Fake moderation tools to prank your friends!

# <@1275521742961508432>fakemodlogset
Manage fake modlog settings.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## <@1275521742961508432>fakemodlogset modlog
Set a channel as the fake modlog.<br/>

Omit [channel] to disable the fake modlog.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset modlog [channel=None]`
 - Aliases: `channel`
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


## <@1275521742961508432>fakemodlogset emoji
Set an emoji for a fake mod action.<br/>

The `action` should be either `warn`, `mute`, `kick`, or `ban`.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset emoji [action=None] [emoji=None]`


## <@1275521742961508432>fakemodlogset resetcases
Reset all fake modlog cases in this server.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset resetcases`


# <@1275521742961508432>worn
Fake warn a member for the specified reason.<br/>
 - Usage: `<@1275521742961508432>worn <member> [reason]`
 - Checks: `server_only`
Extended Arg Info
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>unworn
Fake unwarn a member for the specified reason.<br/>
 - Usage: `<@1275521742961508432>unworn <member> [reason]`
 - Checks: `server_only`
Extended Arg Info
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>myut
Fake mute a member.<br/>
 - Usage: `<@1275521742961508432>myut <member> [reason]`
 - Aliases: `moot`
 - Checks: `server_only`
Extended Arg Info
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>unmyut
Fake unmute a member.<br/>
 - Usage: `<@1275521742961508432>unmyut <member> [reason]`
 - Aliases: `unmoot`
 - Checks: `server_only`
Extended Arg Info
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>kik
Fake kick a member.<br/>
 - Usage: `<@1275521742961508432>kik <member> [reason]`
 - Aliases: `kek and keck`
 - Checks: `server_only`
Extended Arg Info
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>ben
Fake ban a user.<br/>
 - Usage: `<@1275521742961508432>ben <user> [reason]`
 - Aliases: `bam, bon, beam, and bean`
 - Checks: `server_only`
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>unben
Fake unban a user.<br/>
 - Usage: `<@1275521742961508432>unben <user> [reason]`
 - Aliases: `unbam, unbon, unbeam, and unbean`
 - Checks: `server_only`
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
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


