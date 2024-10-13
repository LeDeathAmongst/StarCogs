LinkStorage
===========

A cog to store and retrieve links by name.

<<<<<<< HEAD
# <@1275521742961508432>link
Group command for managing links.<br/>
 - Usage: `<@1275521742961508432>link`


## <@1275521742961508432>link disallow
Disallow a user from overriding and deleting any links and groups.<br/>
 - Usage: `<@1275521742961508432>link disallow <user>`
 - Restricted to: `BOT_OWNER`
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


## <@1275521742961508432>link userlist
List all stored links of the user.<br/>
 - Usage: `<@1275521742961508432>link userlist`


## <@1275521742961508432>link allow
Allow a user to override and delete any links and groups.<br/>
 - Usage: `<@1275521742961508432>link allow <user>`
 - Restricted to: `BOT_OWNER`
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


## <@1275521742961508432>link listgroups
List all groups.<br/>
 - Usage: `<@1275521742961508432>link listgroups`


## <@1275521742961508432>link list
List all stored links for the user.<br/>
 - Usage: `<@1275521742961508432>link list`


## <@1275521742961508432>link get
Retrieve a link by name.<br/>
 - Usage: `<@1275521742961508432>link get <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>link deletegroup
Delete a group.<br/>
 - Usage: `<@1275521742961508432>link deletegroup <group>`
=======
# ,link
Group command for managing links.<br/>
 - Usage: `,link`


## ,link userlist
List all stored links of the user.<br/>
 - Usage: `,link userlist`


## ,link creategroup
Create a new group.<br/>
 - Usage: `,link creategroup <group>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### group: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>link adminremove
Remove a link or group by its name (admin only).<br/>
 - Usage: `<@1275521742961508432>link adminremove <name> [group=default]`
=======
## ,link get
Retrieve a link by name.<br/>
 - Usage: `,link get <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,link useradd
Add a link to the user's storage.<br/>
 - Usage: `,link useradd <name_link>`
Extended Arg Info
> ### name_link: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,link allow
Allow a user to override and delete any links and groups.<br/>
 - Usage: `,link allow <user>`
 - Restricted to: `BOT_OWNER`
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


## ,link adminremove
Remove a link or group by its name (admin only).<br/>
 - Usage: `,link adminremove <name> [group=default]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### group: str = 'default'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>link creategroup
Create a new group.<br/>
 - Usage: `<@1275521742961508432>link creategroup <group>`
=======
## ,link remove
Remove a link from the storage.<br/>
 - Usage: `,link remove <name_group>`
Extended Arg Info
> ### name_group: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,link listgroups
List all groups.<br/>
 - Usage: `,link listgroups`


## ,link list
List all stored links for the user.<br/>
 - Usage: `,link list`


## ,link userremove
Remove a link from the user's storage.<br/>
 - Usage: `,link userremove <name_group>`
Extended Arg Info
> ### name_group: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,link deletegroup
Delete a group.<br/>
 - Usage: `,link deletegroup <group>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### group: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>link useradd
Add a link to the user's storage.<br/>
 - Usage: `<@1275521742961508432>link useradd <name_link>`
Extended Arg Info
> ### name_link: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>link remove
Remove a link from the storage.<br/>
 - Usage: `<@1275521742961508432>link remove <name_group>`
Extended Arg Info
> ### name_group: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>link userremove
Remove a link from the user's storage.<br/>
 - Usage: `<@1275521742961508432>link userremove <name_group>`
Extended Arg Info
> ### name_group: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>link add
Add a link to the storage.<br/>
 - Usage: `<@1275521742961508432>link add <name_link>`
=======
## ,link disallow
Disallow a user from overriding and deleting any links and groups.<br/>
 - Usage: `,link disallow <user>`
 - Restricted to: `BOT_OWNER`
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


## ,link add
Add a link to the storage.<br/>
 - Usage: `,link add <name_link>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### name_link: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


