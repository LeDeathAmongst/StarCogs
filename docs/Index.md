Browse and install repos / cogs from a Red-Index

# ,index
Red-Index cog discoverability commands<br/>
 - Usage: `,index`
## ,index search
Search for cogs<br/>
 - Usage: `,index search <search_term>`
Extended Arg Info
> ### search_term: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,index browse
Browses repos / cogs<br/>
 - Usage: `,index browse [repo_name=]`
Extended Arg Info
> ### repo_name=''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,indexset
Red-Index configuration<br/>
 - Usage: `,indexset`
 - Restricted to: `BOT_OWNER`
## ,indexset link
Set a custom Red-Index link<br/>
 - Usage: `,indexset link [link=]`
Extended Arg Info
> ### link: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,indexset maxminutes
Minutes elapsed before the cache is considered stale<br/>

Set 0 if you want the cache refresh to be manual only<br/>
 - Usage: `,indexset maxminutes <minutes>`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```
## ,indexset showunapproved
Toggle unapproved cogs display<br/>
 - Usage: `,indexset showunapproved <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,indexset refresh
Manually refresh the Red-Index cache.<br/>
 - Usage: `,indexset refresh`
