ModLog
======

Browse and manage modlog cases. To manage modlog settings, use `[p]modlogset`.

<<<<<<< HEAD
# <@1275521742961508432>case
Show the specified case.<br/>
 - Usage: `<@1275521742961508432>case <number>`
=======
# ,case
Show the specified case.<br/>
 - Usage: `,case <number>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>casesfor
Display cases for the specified member.<br/>
 - Usage: `<@1275521742961508432>casesfor <member>`
=======
# ,casesfor
Display cases for the specified member.<br/>
 - Usage: `,casesfor <member>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### member: Union[discord.member.Member, int]
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
# <@1275521742961508432>listcases
List cases for the specified member.<br/>
 - Usage: `<@1275521742961508432>listcases <member>`
=======
# ,listcases
List cases for the specified member.<br/>
 - Usage: `,listcases <member>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### member: Union[discord.member.Member, int]
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
# <@1275521742961508432>reason
=======
# ,reason
>>>>>>> 9e308722 (Revamped and Fixed)
Specify a reason for a modlog case.<br/>

Please note that you can only edit cases you are<br/>
the owner of unless you are a mod, admin or server owner.<br/>

If no case number is specified, the latest case will be used.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>reason <case> <reason>`
=======
 - Usage: `,reason <case> <reason>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### case: Optional[int]
> ```
> A number without decimal places.
> ```
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


