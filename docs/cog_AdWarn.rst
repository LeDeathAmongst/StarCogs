AdWarn
======

<<<<<<< HEAD
# <@1275521742961508432>adwarn
Warn a user and send an embed to the default warning channel.<br/>
 - Usage: `<@1275521742961508432>adwarn <user> <reason>`
=======
# ,adwarn
Warn a user and send an embed to the default warning channel.<br/>
 - Usage: `,adwarn <user> <reason>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### user: discord.member.Member
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>removewarn
Remove a specific warning from a user by its UUID.<br/>
 - Usage: `<@1275521742961508432>removewarn <user> <warning_id>`
=======
# ,removewarn
Remove a specific warning from a user by its UUID.<br/>
 - Usage: `,removewarn <user> <warning_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### user: discord.member.Member
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
> ### warning_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>warncount
Get the total number of warnings a user has.<br/>
 - Usage: `<@1275521742961508432>warncount <user>`
=======
# ,warncount
Get the total number of warnings a user has.<br/>
 - Usage: `,warncount <user>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### user: discord.member.Member
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
# <@1275521742961508432>clearwarns
Clear all warnings for a user.<br/>
 - Usage: `<@1275521742961508432>clearwarns <user>`
=======
# ,clearwarns
Clear all warnings for a user.<br/>
 - Usage: `,clearwarns <user>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>unadwarn
Clear the most recent warning for a user.<br/>
 - Usage: `<@1275521742961508432>unadwarn <user>`
=======
# ,unadwarn
Clear the most recent warning for a user.<br/>
 - Usage: `,unadwarn <user>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### user: discord.member.Member
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
# <@1275521742961508432>editaw
Edit a specific warning by its UUID.<br/>
 - Usage: `<@1275521742961508432>editaw <user> <warning_id> <new_reason>`
=======
# ,editaw
Edit a specific warning by its UUID.<br/>
 - Usage: `,editaw <user> <warning_id> <new_reason>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### user: discord.member.Member
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
> ### warning_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### new_reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>topwarners
Show the top 5 users who have issued the most warnings in the current server.<br/>
 - Usage: `<@1275521742961508432>topwarners`


# <@1275521742961508432>modwarns
Show the number of warnings issued by a moderator and who they have warned in the current server.<br/>
 - Usage: `<@1275521742961508432>modwarns <moderator>`
=======
# ,topwarners
Show the top 5 users who have issued the most warnings in the current server.<br/>
 - Usage: `,topwarners`


# ,modwarns
Show the number of warnings issued by a moderator and who they have warned in the current server.<br/>
 - Usage: `,modwarns <moderator>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### moderator: discord.member.Member
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
# <@1275521742961508432>adboard
Show all users who have issued warnings and how many they have issued.<br/>
 - Usage: `<@1275521742961508432>adboard`


# <@1275521742961508432>warnset
Settings for the warning system.<br/>
 - Usage: `<@1275521742961508432>warnset`
 - Checks: `server_only`


## <@1275521742961508432>warnset threshold
Set an action for a specific warning count threshold.<br/>
 - Usage: `<@1275521742961508432>warnset threshold <warning_count> <action>`
=======
# ,adboard
Show all users who have issued warnings and how many they have issued.<br/>
 - Usage: `,adboard`


# ,warnset
Settings for the warning system.<br/>
 - Usage: `,warnset`
 - Checks: `server_only`


## ,warnset delthreshold
Delete a specific warning count threshold by its UUID.<br/>
 - Usage: `,warnset delthreshold <threshold_id>`
Extended Arg Info
> ### threshold_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,warnset threshold
Set an action for a specific warning count threshold.<br/>
 - Usage: `,warnset threshold <warning_count> <action>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### warning_count: int
> ```
> A number without decimal places.
> ```
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>warnset show
Show the current warning channel and thresholds.<br/>
 - Usage: `<@1275521742961508432>warnset show`


## <@1275521742961508432>warnset timeoutduration
Set the duration (in minutes) for timeouts.<br/>
 - Usage: `<@1275521742961508432>warnset timeoutduration <minutes>`
=======
## ,warnset timeoutduration
Set the duration (in minutes) for timeouts.<br/>
 - Usage: `,warnset timeoutduration <minutes>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>warnset channel
Set the default channel for warnings.<br/>
 - Usage: `<@1275521742961508432>warnset channel <channel>`
=======
## ,warnset softbanduration
Set the duration (in days) for message deletion during a softban.<br/>
 - Usage: `,warnset softbanduration <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```


## ,warnset show
Show the current warning channel and thresholds.<br/>
 - Usage: `,warnset show`


## ,warnset channel
Set the default channel for warnings.<br/>
 - Usage: `,warnset channel <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>warnset softbanduration
Set the duration (in days) for message deletion during a softban.<br/>
 - Usage: `<@1275521742961508432>warnset softbanduration <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>warnset delthreshold
Delete a specific warning count threshold by its UUID.<br/>
 - Usage: `<@1275521742961508432>warnset delthreshold <threshold_id>`
Extended Arg Info
> ### threshold_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>adrace
Start an adwarn race that lasts for a configurable amount of time.<br/>
 - Usage: `<@1275521742961508432>adrace <duration>`
=======
# ,adrace
Start an adwarn race that lasts for a configurable amount of time.<br/>
 - Usage: `,adrace <duration>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### duration: int
> ```
> A number without decimal places.
> ```


