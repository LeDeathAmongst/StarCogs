SelfAssign
==========

Allows users to self-assign roles from a designated list

# ,selfassign

 - Usage: `,selfassign`


## ,selfassign unset
Removes a role from the allowed self-assign list. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `,selfassign unset <role>`
 - Restricted to: `MOD`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,selfassign list
Lists roles that can be self-assigned, sorted alphabetically<br/>
 - Usage: `,selfassign list`
 - Restricted to: `MOD`


## ,selfassign take
Allows a user to have a role removed from them by request. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `,selfassign take <role>`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,selfassign set
Flags a given role as self-assignable<br/>
 - Usage: `,selfassign set <role>`
 - Restricted to: `MOD`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,selfassign give
Allows a user to have a role assigned to them by request. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `,selfassign give <role>`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


