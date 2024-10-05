Index
=====

Browse and install repos / cogs from a Red-Index

# <@1275521742961508432>index
Red-Index cog discoverability commands<br/>
 - Usage: `<@1275521742961508432>index`


## <@1275521742961508432>index search
Search for cogs<br/>
 - Usage: `<@1275521742961508432>index search <search_term>`
Extended Arg Info
> ### search_term: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>index browse
Browses repos / cogs<br/>
 - Usage: `<@1275521742961508432>index browse [repo_name=]`
Extended Arg Info
> ### repo_name=''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>indexset
Red-Index configuration<br/>
 - Usage: `<@1275521742961508432>indexset`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>indexset refresh
Manually refresh the Red-Index cache.<br/>
 - Usage: `<@1275521742961508432>indexset refresh`


## <@1275521742961508432>indexset showunapproved
Toggle unapproved cogs display<br/>
 - Usage: `<@1275521742961508432>indexset showunapproved <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>indexset maxminutes
Minutes elapsed before the cache is considered stale<br/>

Set 0 if you want the cache refresh to be manual only<br/>
 - Usage: `<@1275521742961508432>indexset maxminutes <minutes>`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>indexset link
Set a custom Red-Index link<br/>
 - Usage: `<@1275521742961508432>indexset link [link=]`
Extended Arg Info
> ### link: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


