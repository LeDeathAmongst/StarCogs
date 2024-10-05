NickNamer

# <@1275521742961508432>nick
Forcibly change a user's nickname to a predefined string.<br/>
 - Usage: `<@1275521742961508432>nick <user> <reason>`
 - Restricted to: `MOD`
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
> ### reason: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>cnick
Forcibly change a user's nickname.<br/>
 - Usage: `<@1275521742961508432>cnick <user> <nickname> <reason>`
 - Restricted to: `MOD`
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
> ### nickname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>freezenick
Freeze a users nickname.<br/>
 - Usage: `<@1275521742961508432>freezenick <user> <nickname> [reason]`
 - Restricted to: `MOD`
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
> ### nickname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: Optional[str] = 'Nickname frozen.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>unfreezenick
Unfreeze a user's nickname.<br/>
 - Usage: `<@1275521742961508432>unfreezenick <user>`
 - Restricted to: `MOD`
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
# <@1275521742961508432>tempnick
Temporarily rename a user.<br/>
**IMPORTANT**: For better performance, temporary nicknames are checked in a 10 minute intervall.<br/>
 - Usage: `<@1275521742961508432>tempnick <user> <duration> <nickname> [reason]`
 - Restricted to: `MOD`
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
> ### nickname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: Optional[str] = 'User has been temporarily renamed.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>nickset
Nicknamer settings<br/>
 - Usage: `<@1275521742961508432>nickset`
 - Restricted to: `ADMIN`
## <@1275521742961508432>nickset name
Set the default name that will be applied when using ``<@1275521742961508432>nick``<br/>
 - Usage: `<@1275521742961508432>nickset name <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>nickset modlog
Set if you would like to create a modlog entry everytime a nickname is being changed.<br/>
 - Usage: `<@1275521742961508432>nickset modlog <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>nickset dm
Set if you would like the bot to DM the user who's nickname was changed.<br/>
 - Usage: `<@1275521742961508432>nickset dm <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# <@1275521742961508432>nickpurge
Remove all nicknames in the server.<br/>
 - Usage: `<@1275521742961508432>nickpurge <are_you_sure>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### are_you_sure: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
