A cog to get and display some documentations in Discord! Use `[p]listsources` to get a list of all the available sources.

# ,docs (Hybrid Command)
View rich documentation for a specific node/query.<br/>

The name must be exact, or else rtfm is invoked instead.<br/>

Arguments:<br/>
- `source`: The name of the documentation to use. Defaults to the one configured with `,setgetdocs defaultsource`.<br/>
- `query`: The documentation node/query. (`random` to get a random documentation)<br/>
 - Usage: `,docs [source=None] [query]`
 - Slash Usage: `/docs [source=None] [query]`
 - Aliases: `getdocs, getdoc, and doc`
Extended Arg Info
> ### query: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,rtfm (Hybrid Command)
Show all items matching your search.<br/>

Arguments:<br/>
- `source`: The name of the documentation to use. Defaults to the one configured with `,setgetdocs defaultsource`.<br/>
- `limit`: The limit of objects to be sent.<br/>
- `with_std`: Also display links to non-API documentation.<br/>
- `query`: Your search. (`events` to get all dpy events, for `discord.py`, `redbot` and `pylav` source only)<br/>
 - Usage: `,rtfm [source=None] [limit=10] [with_std=False] [query]`
 - Slash Usage: `/rtfm [source=None] [limit=10] [with_std=False] [query]`
 - Aliases: `rtfd`
Extended Arg Info
> ### limit: Optional[int] = 10
> ```
> A number without decimal places.
> ```
> ### with_std: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### query: Optional[str] = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,listsources (Hybrid Command)
Shows a list of all sources, those that are available or those that are disabled.<br/>
 - Usage: `,listsources [_sorted=False] [status=available]`
 - Slash Usage: `/listsources [_sorted=False] [status=available]`
 - Aliases: `listdocsources, listrtfmsources, and listsource`
Extended Arg Info
> ### _sorted: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,setgetdocs (Hybrid Command)
Commands to configure GetDocs.<br/>
 - Usage: `,setgetdocs`
 - Slash Usage: `/setgetdocs`
 - Restricted to: `BOT_OWNER`
## ,setgetdocs caching (Hybrid Command)
Enable or disable Documentations caching when loading the cog.<br/>

If the option is disabled, a web request will be executed when the command `,getdocs` is run only for the searched item.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setgetdocs caching <value>`
 - Slash Usage: `/setgetdocs caching <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setgetdocs getdebugloopsstatus (Hybrid Command)
Get an embed to check loops status.<br/>
 - Usage: `,setgetdocs getdebugloopsstatus`
 - Slash Usage: `/setgetdocs getdebugloopsstatus`
## ,setgetdocs stats (Hybrid Command)
Show stats about all documentations sources.<br/>
 - Usage: `,setgetdocs stats`
 - Slash Usage: `/setgetdocs stats`
## ,setgetdocs showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setgetdocs showsettings [with_dev=False]`
 - Slash Usage: `/setgetdocs showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setgetdocs resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setgetdocs resetsetting <setting>`
 - Slash Usage: `/setgetdocs resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setgetdocs modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setgetdocs modalconfig [confirmation=False]`
 - Slash Usage: `/setgetdocs modalconfig [confirmation=False]`
 - Aliases: `configmodal`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setgetdocs defaultsource (Hybrid Command)
Set the documentations source.<br/>

Default value: `discord.py`<br/>
Dev: `<class 'getdocs.getdocs.SourceConverter'>`<br/>
 - Usage: `,setgetdocs defaultsource <value>`
 - Slash Usage: `/setgetdocs defaultsource <value>`
## ,setgetdocs disablesources (Hybrid Command)
Disable Documentations source(s).<br/>
 - Usage: `,setgetdocs disablesources <sources>`
 - Slash Usage: `/setgetdocs disablesources <sources>`
 - Aliases: `disablesource`
## ,setgetdocs enablesources (Hybrid Command)
Enable Documentations source(s).<br/>
 - Usage: `,setgetdocs enablesources <sources>`
 - Slash Usage: `/setgetdocs enablesources <sources>`
 - Aliases: `enablesource`
