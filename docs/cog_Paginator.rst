Paginator
=========

A cog that paginates content and embed given by you.

JSON example:
    https://pastebin.com/DiuFREBW
    
YAML example:
    https://pastebin.com/e9ZvhYUn

<<<<<<< HEAD
# <@1275521742961508432>paginator
=======
# ,paginator
>>>>>>> 9e308722 (Revamped and Fixed)
Commands to manage paginators.<br/>

JSON example:<br/>
    https://pastebin.com/DiuFREBW<br/>

YAML example:<br/>
    https://pastebin.com/e9ZvhYUn<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>paginator`
=======
 - Usage: `,paginator`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `paginate and page`


<<<<<<< HEAD
## <@1275521742961508432>paginator info
Get information about a paginator group.<br/>
 - Usage: `<@1275521742961508432>paginator info <group_name>`
 - Aliases: `i`
=======
## ,paginator removepage
Remove a page from a paginator group.<br/>
 - Usage: `,paginator removepage <group_name> <page_number>`
 - Aliases: `rp`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
<<<<<<< HEAD


## <@1275521742961508432>paginator raw
Get the raw JSON of a paginator group's page.<br/>
 - Usage: `<@1275521742961508432>paginator raw <group_name> <index>`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int
=======
> ### page_number: int
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>paginator delete
Delete a paginator group.<br/>
 - Usage: `<@1275521742961508432>paginator delete <group_name>`
=======
## ,paginator addpage
Add a page to a paginator group.<br/>
 - Usage: `,paginator addpage`
 - Aliases: `ap`


### ,paginator addpage fromyaml
Add a page to a paginator group.<br/>

The `page` argument should be a pastebin link containing valid yaml.<br/>
If `index` is not provided, the page will be added to the end of the paginator group.<br/>
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.<br/>


Example YAML: https://pastebin.com/e9ZvhYUn<br/>
 - Usage: `,paginator addpage fromyaml <group_name> <page> [index=None]`
 - Aliases: `fy and yaml`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
<<<<<<< HEAD


## <@1275521742961508432>paginator start
Starts a paginator of the given group name<br/>
 - Usage: `<@1275521742961508432>paginator start <group_name> [page_number=1] [timeout=None]`
=======
> ### index: int = None
> ```
> A number without decimal places.
> ```


### ,paginator addpage fromjson
Add a page to a paginator group.<br/>

The `page` argument should be a pastebin link containing valid json.<br/>
If `index` is not provided, the page will be added to the end of the paginator group.<br/>
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.<br/>

Example JSON: https://pastebin.com/DiuFREBW<br/>
 - Usage: `,paginator addpage fromjson <group_name> <page> [index=None]`
 - Aliases: `fj and json`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int = None
> ```
> A number without decimal places.
> ```


## ,paginator start
Starts a paginator of the given group name<br/>
 - Usage: `,paginator start <group_name> [page_number=1] [timeout=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### timeout: Optional[int] = None
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>paginator editpage
Edit a page in a paginator group.<br/>
 - Usage: `<@1275521742961508432>paginator editpage <group_name> <page_number> <page>`
=======
## ,paginator info
Get information about a paginator group.<br/>
 - Usage: `,paginator info <group_name>`
 - Aliases: `i`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,paginator editpage
Edit a page in a paginator group.<br/>
 - Usage: `,paginator editpage <group_name> <page_number> <page>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `ep`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### page_number: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>paginator list
List all paginator groups in the server.<br/>
 - Usage: `<@1275521742961508432>paginator list`
 - Aliases: `l`


## <@1275521742961508432>paginator create
Initiate a new paginator group.<br/>
 - Usage: `<@1275521742961508432>paginator create <group_name> [use_reactions=False] [timeout=60] [delete_on_timeout=False]`
=======
## ,paginator list
List all paginator groups in the server.<br/>
 - Usage: `,paginator list`
 - Aliases: `l`


## ,paginator raw
Get the raw JSON of a paginator group's page.<br/>
 - Usage: `,paginator raw <group_name> <index>`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int
> ```
> A number without decimal places.
> ```


## ,paginator delete
Delete a paginator group.<br/>
 - Usage: `,paginator delete <group_name>`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,paginator create
Initiate a new paginator group.<br/>
 - Usage: `,paginator create <group_name> [use_reactions=False] [timeout=60] [delete_on_timeout=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### use_reactions: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### timeout: int = 60
> ```
> A number without decimal places.
> ```
> ### delete_on_timeout: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>paginator removepage
Remove a page from a paginator group.<br/>
 - Usage: `<@1275521742961508432>paginator removepage <group_name> <page_number>`
 - Aliases: `rp`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### page_number: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>paginator addpage
Add a page to a paginator group.<br/>
 - Usage: `<@1275521742961508432>paginator addpage`
 - Aliases: `ap`


### <@1275521742961508432>paginator addpage fromjson
Add a page to a paginator group.<br/>

The `page` argument should be a pastebin link containing valid json.<br/>
If `index` is not provided, the page will be added to the end of the paginator group.<br/>
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.<br/>

Example JSON: https://pastebin.com/DiuFREBW<br/>
 - Usage: `<@1275521742961508432>paginator addpage fromjson <group_name> <page> [index=None]`
 - Aliases: `fj and json`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int = None
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>paginator addpage fromyaml
Add a page to a paginator group.<br/>

The `page` argument should be a pastebin link containing valid yaml.<br/>
If `index` is not provided, the page will be added to the end of the paginator group.<br/>
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.<br/>


Example YAML: https://pastebin.com/e9ZvhYUn<br/>
 - Usage: `<@1275521742961508432>paginator addpage fromyaml <group_name> <page> [index=None]`
 - Aliases: `fy and yaml`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int = None
> ```
> A number without decimal places.
> ```


=======
>>>>>>> 9e308722 (Revamped and Fixed)
