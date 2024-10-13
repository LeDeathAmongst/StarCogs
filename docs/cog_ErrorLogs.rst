ErrorLogs
=========

Log tracebacks of command errors in discord channels.

# ,errorlogs
Manage error logs.<br/>
 - Usage: `,errorlogs`
 - Restricted to: `BOT_OWNER`


## ,errorlogs enabled
Enable or disable error logging.<br/>
 - Usage: `,errorlogs enabled <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,errorlogs global
Enable or disable errors from all servers.<br/>
 - Usage: `,errorlogs global <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,errorlogs scroll
Scroll through the console's history.<br/>

__**Arguments**__<br/>
`page_size`: (integer) The initial number of lines in each<br/>
page.<br/>
`num_pages`: (integer) The number of pages to read into the<br/>
buffer.<br/>
 - Usage: `,errorlogs scroll [page_size=25] [num_pages=15]`
 - Aliases: `history`
Extended Arg Info
> ### page_size: int = 25
> ```
> A number without decimal places.
> ```
> ### num_pages: int = 15
> ```
> A number without decimal places.
> ```


