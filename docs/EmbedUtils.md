Create, send, and store rich embeds, from Red-Dashboard too!

# <@1275521742961508432>embed (Hybrid Command)
Post a simple embed with a color, a title and a description.<br/>

Put the title in quotes if it contains spaces.<br/>
If you provide a message, it will be edited.<br/>
 - Usage: `<@1275521742961508432>embed <channel_or_message> <color> <title> <description>`
 - Slash Usage: `/embed <channel_or_message> <color> <title> <description>`
 - Restricted to: `MOD`
 - Aliases: `embedutils`
 - Checks: `server_only`
Extended Arg Info
> ### color: Optional[discord.colour.Colour]
> Converts to a :class:`~discord.Colour`.
> 
>     
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>embed yamlfile (Hybrid Command)
Post an embed from a valid YAML file (upload it).<br/>

If you provide a message, it will be edited.<br/>
 - Usage: `<@1275521742961508432>embed yamlfile [channel_or_message=None]`
 - Slash Usage: `/embed yamlfile [channel_or_message=None]`
 - Aliases: `fromyamlfile`
## <@1275521742961508432>embed message (Hybrid Command)
Post embed(s) from an existing message.<br/>

The message must have at least one embed.<br/>
You can specify an index (starting by 0) if you want to send only one of the embeds.<br/>
The content of the message already sent is included if no index is specified.<br/>

If you provide a message, it will be edited.<br/>
 - Usage: `<@1275521742961508432>embed message <channel_or_message> [message=None] [index=None] [include_content=None]`
 - Slash Usage: `/embed message <channel_or_message> [message=None] [index=None] [include_content=None]`
 - Aliases: `frommessage, msg, and frommsg`
Extended Arg Info
> ### message: discord.message.Message = None
> Converts to a :class:`discord.Message`.
> 
>     
> ### index: int = None
> ```
> A number without decimal places.
> ```
> ### include_content: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>embed json (Hybrid Command)
Post embeds from valid JSON.<br/>

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).<br/>
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).<br/>
You can use an [**embeds creator**](https://embedutils.com/) to get a JSON payload.<br/>

If you provide a message, it will be edited.<br/>
You can use an attachment and the command `<@1275521742961508432>embed yamlfile` will be invoked automatically.<br/>
 - Usage: `<@1275521742961508432>embed json [channel_or_message=None] [data]`
 - Slash Usage: `/embed json [channel_or_message=None] [data]`
 - Aliases: `fromjson and fromdata`
## <@1275521742961508432>embed download (Hybrid Command)
Download a JSON file for a message's embed(s).<br/>

The message must have at least one embed.<br/>
You can specify an index (starting by 0) if you want to include only one of the embeds.<br/>
The content of the message already sent is included if no index is specified.<br/>
 - Usage: `<@1275521742961508432>embed download [message=None] [index=None] [include_content=None]`
 - Slash Usage: `/embed download [message=None] [index=None] [include_content=None]`
Extended Arg Info
> ### message: discord.message.Message = None
> Converts to a :class:`discord.Message`.
> 
>     
> ### index: int = None
> ```
> A number without decimal places.
> ```
> ### include_content: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>embed edit (Hybrid Command)
Edit a message sent by Starfire.<br/>

It would be better to use the `message` parameter of all the other commands.<br/>
 - Usage: `<@1275521742961508432>embed edit <message> <conversion_type> [data]`
 - Slash Usage: `/embed edit <message> <conversion_type> [data]`
 - Restricted to: `MOD`
Extended Arg Info
> ### data: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>embed list (Hybrid Command)
Get info about a stored embed.<br/>
 - Usage: `<@1275521742961508432>embed list [global_level=False]`
 - Slash Usage: `/embed list [global_level=False]`
 - Restricted to: `MOD`
 - Aliases: `liststored and liststoredembeds`
Extended Arg Info
> ### global_level: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>embed pastebin (Hybrid Command)
Post embeds from a GitHub/Gist/Pastebin/Hastebin link containing valid JSON.<br/>

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).<br/>
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).<br/>

If you provide a message, it will be edited.<br/>
 - Usage: `<@1275521742961508432>embed pastebin [channel_or_message=None] <data>`
 - Slash Usage: `/embed pastebin [channel_or_message=None] <data>`
 - Aliases: `frompastebin, gist, fromgist, hastebin, and fromhastebin`
## <@1275521742961508432>embed fromfile (Hybrid Command)
Post an embed from a valid JSON file (upload it).<br/>

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).<br/>
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).<br/>
You can use an [**embeds creator**](https://embedutils.com/) to get a JSON payload.<br/>

If you provide a message, it will be edited.<br/>
 - Usage: `<@1275521742961508432>embed fromfile [channel_or_message=None]`
 - Slash Usage: `/embed fromfile [channel_or_message=None]`
 - Aliases: `jsonfile, fromjsonfile, and fromdatafile`
## <@1275521742961508432>embed yaml (Hybrid Command)
Post embeds from valid YAML.<br/>

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).<br/>
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).<br/>

If you provide a message, it will be edited.<br/>
You can use an attachment and the command `<@1275521742961508432>embed yamlfile` will be invoked automatically.<br/>
 - Usage: `<@1275521742961508432>embed yaml [channel_or_message=None] [data]`
 - Slash Usage: `/embed yaml [channel_or_message=None] [data]`
 - Aliases: `fromyaml`
## <@1275521742961508432>embed poststored (Hybrid Command)
Post stored embeds.<br/>
 - Usage: `<@1275521742961508432>embed poststored <channel_or_message> <global_level> <names>`
 - Slash Usage: `/embed poststored <channel_or_message> <global_level> <names>`
 - Aliases: `poststoredembed and post`
Extended Arg Info
> ### global_level: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>embed downloadstored (Hybrid Command)
Download a JSON file for a stored embed.<br/>
 - Usage: `<@1275521742961508432>embed downloadstored <global_level> <name>`
 - Slash Usage: `/embed downloadstored <global_level> <name>`
 - Restricted to: `MOD`
 - Aliases: `downloadstoredembed`
Extended Arg Info
> ### global_level: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>embed postwebhook (Hybrid Command)
Post stored embeds with a webhook.<br/>
 - Usage: `<@1275521742961508432>embed postwebhook <channel> <username> <avatar_url> <global_level> <names>`
 - Slash Usage: `/embed postwebhook <channel> <username> <avatar_url> <global_level> <names>`
 - Restricted to: `MOD`
 - Aliases: `webhook`
Extended Arg Info
> ### avatar_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### global_level: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>embed dashboard (Hybrid Command)
Get the link to the Dashboard.<br/>
 - Usage: `<@1275521742961508432>embed dashboard [conversion_type=None] [data]`
 - Slash Usage: `/embed dashboard [conversion_type=None] [data]`
Extended Arg Info
> ### data: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>embed migratefromphen (Hybrid Command)
Migrate stored embeds from EmbedUtils by Phen.<br/>
 - Usage: `<@1275521742961508432>embed migratefromphen`
 - Slash Usage: `/embed migratefromphen`
 - Restricted to: `BOT_OWNER`
 - Aliases: `migratefromembedutils`
## <@1275521742961508432>embed store (Hybrid Command)
Store an embed.<br/>

Put the name in quotes if it is multiple words.<br/>
The `locked` argument specifies whether the embed should be locked to mod and superior only (server level) or bot owners only (global level).<br/>
 - Usage: `<@1275521742961508432>embed store <global_level> <locked> <name> <conversion_type> [data]`
 - Slash Usage: `/embed store <global_level> <locked> <name> <conversion_type> [data]`
 - Restricted to: `MOD`
 - Aliases: `storeembed`
Extended Arg Info
> ### global_level: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### locked: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### data: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>embed unstore (Hybrid Command)
Remove a stored embed.<br/>
 - Usage: `<@1275521742961508432>embed unstore <global_level> <name>`
 - Slash Usage: `/embed unstore <global_level> <name>`
 - Restricted to: `MOD`
 - Aliases: `unstoreembed`
Extended Arg Info
> ### global_level: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>embed info (Hybrid Command)
Get info about a stored embed.<br/>
 - Usage: `<@1275521742961508432>embed info <global_level> <name>`
 - Slash Usage: `/embed info <global_level> <name>`
 - Restricted to: `MOD`
 - Aliases: `infostored and infostoredembed`
Extended Arg Info
> ### global_level: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
