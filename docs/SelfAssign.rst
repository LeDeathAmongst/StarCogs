SelfAssign
==========

Allows users to self-assign roles from a designated list

# <@1275521742961508432>selfassign

 - Usage: `<@1275521742961508432>selfassign`


## <@1275521742961508432>selfassign set
Flags a given role as self-assignable<br/>
 - Usage: `<@1275521742961508432>selfassign set <role>`
 - Restricted to: `MOD`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>selfassign list
Lists roles that can be self-assigned, sorted alphabetically<br/>
 - Usage: `<@1275521742961508432>selfassign list`
 - Restricted to: `MOD`


## <@1275521742961508432>selfassign unset
Removes a role from the allowed self-assign list. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `<@1275521742961508432>selfassign unset <role>`
 - Restricted to: `MOD`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>selfassign take
Allows a user to have a role removed from them by request. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `<@1275521742961508432>selfassign take <role>`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>selfassign give
Allows a user to have a role assigned to them by request. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `<@1275521742961508432>selfassign give <role>`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


