Fluent
======

Seamless translation between two languages in one channel. Or manual translation to various languages.

Fluent uses google translate by default, with [Flowery](https://flowery.pw/) as a fallback.

Fluent also supports the [Deepl](https://www.deepl.com/pro#developer) tranlsation api.
1. Register your free Deepl account **[Here](https://www.deepl.com/pro#developer)**.
2. Obtain your API key **[Here](https://www.deepl.com/account/summary)**.
3. Set your API key with:
`[p]set api deepl key YOUR_KEY_HERE`

If a deepl key is set, it will use that before falling back to google translate and then flowery.

# <@1275521742961508432>serverlocale
Check the current server's locale<br/>
 - Usage: `<@1275521742961508432>serverlocale`


# <@1275521742961508432>translate (Hybrid Command)
Translate a message<br/>
 - Usage: `<@1275521742961508432>translate <to_language> [message]`
 - Slash Usage: `/translate <to_language> [message]`
Extended Arg Info
> ### to_language: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>fluent
Base command<br/>
 - Usage: `<@1275521742961508432>fluent`
 - Restricted to: `MOD`


## <@1275521742961508432>fluent remove
Remove a channel from Fluent<br/>
 - Usage: `<@1275521742961508432>fluent remove [channel=None]`
 - Aliases: `delete, del, and rem`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.ForumChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>fluent add
Add a channel and languages to translate between<br/>

Tip: Language 1 is the first to be converted. For example, if you expect most of the conversation to be<br/>
in english, then make english language 2 to use less api calls.<br/>
 - Usage: `<@1275521742961508432>fluent add <language1> <language2> [channel=None]`
Extended Arg Info
> ### language1: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### language2: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.ForumChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>fluent view
View all fluent channels<br/>
 - Usage: `<@1275521742961508432>fluent view`


