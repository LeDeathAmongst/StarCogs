FakeMod
=======

Fake moderation tools to prank your friends!

<<<<<<< HEAD
# <@1275521742961508432>fakemodlogset
Manage fake modlog settings.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset`
=======
# ,fakemodlogset
Manage fake modlog settings.<br/>
 - Usage: `,fakemodlogset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>fakemodlogset resetcases
Reset all fake modlog cases in this server.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset resetcases`


## <@1275521742961508432>fakemodlogset modlog
Set a channel as the fake modlog.<br/>

Omit [channel] to disable the fake modlog.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset modlog [channel=None]`
=======
## ,fakemodlogset modlog
Set a channel as the fake modlog.<br/>

Omit [channel] to disable the fake modlog.<br/>
 - Usage: `,fakemodlogset modlog [channel=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>fakemodlogset emoji
Set an emoji for a fake mod action.<br/>

The `action` should be either `warn`, `mute`, `kick`, or `ban`.<br/>
 - Usage: `<@1275521742961508432>fakemodlogset emoji [action=None] [emoji=None]`


# <@1275521742961508432>worn
Fake warn a member for the specified reason.<br/>
 - Usage: `<@1275521742961508432>worn <member> [reason]`
=======
## ,fakemodlogset emoji
Set an emoji for a fake mod action.<br/>

The `action` should be either `warn`, `mute`, `kick`, or `ban`.<br/>
 - Usage: `,fakemodlogset emoji [action=None] [emoji=None]`


## ,fakemodlogset resetcases
Reset all fake modlog cases in this server.<br/>
 - Usage: `,fakemodlogset resetcases`


# ,worn
Fake warn a member for the specified reason.<br/>
 - Usage: `,worn <member> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>unworn
Fake unwarn a member for the specified reason.<br/>
 - Usage: `<@1275521742961508432>unworn <member> [reason]`
=======
# ,unworn
Fake unwarn a member for the specified reason.<br/>
 - Usage: `,unworn <member> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>myut
Fake mute a member.<br/>
 - Usage: `<@1275521742961508432>myut <member> [reason]`
=======
# ,myut
Fake mute a member.<br/>
 - Usage: `,myut <member> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>unmyut
Fake unmute a member.<br/>
 - Usage: `<@1275521742961508432>unmyut <member> [reason]`
=======
# ,unmyut
Fake unmute a member.<br/>
 - Usage: `,unmyut <member> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>kik
Fake kick a member.<br/>
 - Usage: `<@1275521742961508432>kik <member> [reason]`
=======
# ,kik
Fake kick a member.<br/>
 - Usage: `,kik <member> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>ben
Fake ban a user.<br/>
 - Usage: `<@1275521742961508432>ben <user> [reason]`
=======
# ,ben
Fake ban a user.<br/>
 - Usage: `,ben <user> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>unben
Fake unban a user.<br/>
 - Usage: `<@1275521742961508432>unben <user> [reason]`
=======
# ,unben
Fake unban a user.<br/>
 - Usage: `,unben <user> [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


