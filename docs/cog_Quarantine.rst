Quarantine
==========

Quarantine a user

<<<<<<< HEAD
# <@1275521742961508432>setquar
Change the configurations for <@1275521742961508432>quar<br/>
 - Usage: `<@1275521742961508432>setquar`
 - Checks: `server_only`


## <@1275521742961508432>setquar role
Set the quarantine role<br/>
 - Usage: `<@1275521742961508432>setquar role [role=None]`
=======
# ,setquar
Change the configurations for ,quar<br/>
 - Usage: `,setquar`
 - Checks: `server_only`


## ,setquar role
Set the quarantine role<br/>
 - Usage: `,setquar role [role=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>setquar list
List current settings<br/>
 - Usage: `<@1275521742961508432>setquar list`
 - Restricted to: `MOD`


## <@1275521742961508432>setquar report
Send an embed with quarantine reason to a specified channel<br/>
 - Usage: `<@1275521742961508432>setquar report [channel=]`
=======
## ,setquar list
List current settings<br/>
 - Usage: `,setquar list`
 - Restricted to: `MOD`


## ,setquar report
Send an embed with quarantine reason to a specified channel<br/>
 - Usage: `,setquar report [channel=]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: discord.channel.TextChannel = ''
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>quar
Quarantines a user (config in `<@1275521742961508432>setquar`)<br/>
 - Usage: `<@1275521742961508432>quar [user=None] [reason]`
=======
# ,quar
Quarantines a user (config in `,setquar`)<br/>
 - Usage: `,quar [user=None] [reason]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
Extended Arg Info
> ### user: discord.member.Member = None
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
> ### reason=''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>quarall
=======
# ,quarall
>>>>>>> 9e308722 (Revamped and Fixed)
Search for all usernames (not nicknames) that match a string and quarantine them<br/>

Types:<br/>
1 - Normal quarantine<br/>
2 - Kick the users<br/>
3 - Ban the users<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>quarall [quarType=1] <userSearchText>`
=======
 - Usage: `,quarall [quarType=1] <userSearchText>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
Extended Arg Info
> ### quarType: int = 1
> ```
> A number without decimal places.
> ```
> ### userSearchText: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


