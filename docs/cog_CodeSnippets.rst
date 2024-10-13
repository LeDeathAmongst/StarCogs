CodeSnippets
============

A cog to send code content from a GitHub/Gist/GitLab/BitBucket/Pastebin/Hastebin URL!

<<<<<<< HEAD
# <@1275521742961508432>codesnippets (Hybrid Command)
Send code content from a GitHub/Gist/GitLab/BitBucket/Pastebin/Hastebin URL.<br/>
 - Usage: `<@1275521742961508432>codesnippets [limit=3] <urls>`
=======
# ,codesnippets (Hybrid Command)
Send code content from a GitHub/Gist/GitLab/BitBucket/Pastebin/Hastebin URL.<br/>
 - Usage: `,codesnippets [limit=3] <urls>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/codesnippets [limit=3] <urls>`
 - Aliases: `codesnippet`
Extended Arg Info
> ### urls: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>setcodesnippets (Hybrid Command)
Configure CodeSnippets.<br/>
 - Usage: `<@1275521742961508432>setcodesnippets`
=======
# ,setcodesnippets (Hybrid Command)
Configure CodeSnippets.<br/>
 - Usage: `,setcodesnippets`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setcodesnippets`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>setcodesnippets showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>setcodesnippets showsettings [with_dev=False]`
 - Slash Usage: `/setcodesnippets showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setcodesnippets addchannel (Hybrid Command)
Add a channel where the cog have to send automatically code snippets from URLs.<br/>
 - Usage: `<@1275521742961508432>setcodesnippets addchannel <channel>`
 - Slash Usage: `/setcodesnippets addchannel <channel>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>setcodesnippets removechannel (Hybrid Command)
Remove a channel where the cog have to send automatically code snippets from URLs.<br/>
 - Usage: `<@1275521742961508432>setcodesnippets removechannel <channel>`
=======
## ,setcodesnippets removechannel (Hybrid Command)
Remove a channel where the cog have to send automatically code snippets from URLs.<br/>
 - Usage: `,setcodesnippets removechannel <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setcodesnippets removechannel <channel>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


<<<<<<< HEAD
=======
## ,setcodesnippets showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setcodesnippets showsettings [with_dev=False]`
 - Slash Usage: `/setcodesnippets showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcodesnippets addchannel (Hybrid Command)
Add a channel where the cog have to send automatically code snippets from URLs.<br/>
 - Usage: `,setcodesnippets addchannel <channel>`
 - Slash Usage: `/setcodesnippets addchannel <channel>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


>>>>>>> 9e308722 (Revamped and Fixed)
