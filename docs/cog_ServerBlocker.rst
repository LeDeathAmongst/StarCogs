ServerBlocker
=============

# ,serverblock
Manage blocked servers.<br/>
 - Usage: `,serverblock`
 - Restricted to: `BOT_OWNER`


## ,serverblock add
Add a server to the blocklist with a reason.<br/>
 - Usage: `,serverblock add <server_id> <reason>`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,serverblock remove
Remove a server from the blocklist.<br/>
 - Usage: `,serverblock remove <server_id>`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```


## ,serverblock list
List all blocked servers.<br/>
 - Usage: `,serverblock list`


