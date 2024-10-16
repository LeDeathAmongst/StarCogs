Create and use tags.<br/><br/>The TagScript documentation can be found [here](https://seina-cogs.readthedocs.io/en/latest/).

# ,tagsettings
Manage Tags cog settings.<br/>
 - Usage: `,tagsettings`
 - Restricted to: `BOT_OWNER`
 - Aliases: `tagset`
## ,tagsettings dotparam
Toggle the TagScript parsing style.<br/>

If `dot_parameter` is enabled, TagScript blocks will parse like this:<br/>
`{declaration.parameter:payload}`<br/>
instead of:<br/>
`{declaration(parameter):payload}`<br/>
 - Usage: `,tagsettings dotparam [true_or_false=None]`
Extended Arg Info
> ### true_or_false: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,tagsettings settings
View Tags settings.<br/>
 - Usage: `,tagsettings settings`
 - Checks: `server_only`
## ,tagsettings async
Toggle using the asynchronous TagScript interpreter.<br/>

If you aren't a developer or don't know what this is, there's no reason for you to change it.<br/>
 - Usage: `,tagsettings async [true_or_false=None]`
Extended Arg Info
> ### true_or_false: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,tagsettings limit
Change the global and server limit for tags.<br/>
 - Usage: `,tagsettings limit`
### ,tagsettings limit global
Change the global limit for tags.<br/>
 - Usage: `,tagsettings limit global <amount>`
### ,tagsettings limit server
Change the server limit for tags.<br/>
 - Usage: `,tagsettings limit server <amount> [server=None]`
 - Checks: `server_only`
Extended Arg Info
> ### server: Optional[discord.server.Guild] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## ,tagsettings block
Manage custom TagScript blocks.<br/>
 - Usage: `,tagsettings block`
### ,tagsettings block show
Show the code of a custom block.<br/>
 - Usage: `,tagsettings block show <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,tagsettings block add
Add a custom block to the TagScript interpreter.<br/>

The passed code must return a block class that inherits from `TagScriptEngine.Block`.<br/>
 - Usage: `,tagsettings block add <name> <code>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,tagsettings block list
List all custom blocks in the TagScript interpreter.<br/>
 - Usage: `,tagsettings block list`
### ,tagsettings block remove
Remove a custom block from the TagScript interpreter.<br/>
 - Usage: `,tagsettings block remove <name>`
 - Aliases: `delete`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,migratealias
Migrate the Alias cog's global and server aliases into tags.<br/>

This converts all aliases created with the Alias cog into tags with command blocks.<br/>
This action cannot be undone.<br/>

**Example:**<br/>
`,migratealias`<br/>
 - Usage: `,migratealias`
 - Restricted to: `BOT_OWNER`
# ,migratecustomcom
Migrate the CustomCommand cog's server commands into tags.<br/>

This converts all custom commands created into tags with the command text as TagScript.<br/>
Randomized commands are converted into random blocks.<br/>
Commands with converters are converted into indexed args blocks.<br/>
This action cannot be undone.<br/>

**Example:**<br/>
`,migratecustomcom`<br/>
 - Usage: `,migratecustomcom`
 - Restricted to: `BOT_OWNER`
 - Aliases: `migratecustomcommands`
# ,invoketag
Manually invoke a tag with its name and arguments.<br/>

Restricting this command with permissions in servers will restrict all members from invoking tags.<br/>

**Examples:**<br/>
`,invoketag searchitem trophy`<br/>
`,invoketag donate`<br/>
 - Usage: `,invoketag <response> <tag_name> [args]`
Extended Arg Info
> ### response: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### tag_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### args: Optional[str] = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,tags
View all tags and aliases.<br/>

This command will show global tags if run in DMs.<br/>

**Example:**<br/>
`,tags`<br/>
 - Usage: `,tags`
# ,tag
Tag management with TagScript.<br/>

These commands use TagScriptEngine.<br/>
Read the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/) to learn how to use TagScript blocks.<br/>
 - Usage: `,tag`
 - Aliases: `customcom, cc, and alias`
 - Checks: `server_only`
## ,tag alias
Add an alias for a tag.<br/>

        Adding an alias to the tag will make the tag invokable using the alias or the tag name.<br/>
        In the example below, running `,donation` will invoke the `donate` tag.<br/>
​<br/>
        **Example:**<br/>
        `,tag alias donate donation`<br/>
 - Usage: `,tag alias <tag> <alias>`
 - Restricted to: `MOD`
## ,tag info
Show information about a tag.<br/>

You can view meta information for a tag on this server or a global tag.<br/>
If a tag on this server has the same name as a global tag, it will show the server tag.<br/>

**Example:**<br/>
`,tag info notsupport`<br/>
 - Usage: `,tag info <tag>`
## ,tag pastebin
Add a tag with a Pastebin link.<br/>

**Example:**<br/>
`,tag pastebin starwarsopeningcrawl https://pastebin.com/CKjn6uYv`<br/>
 - Usage: `,tag pastebin <tag_name> <link>`
 - Restricted to: `MOD`
 - Aliases: `++`
## ,tag remove
Permanently delete a tag.<br/>

If you want to remove a tag's alias, use `,tag unalias`.<br/>

**Example:**<br/>
`,tag remove RickRoll`<br/>
 - Usage: `,tag remove <tag>`
 - Restricted to: `MOD`
 - Aliases: `delete and -`
## ,tag docs
Search the TagScript documentation for a block.<br/>

https://seina-cogs.readthedocs.io/en/latest/<br/>

**Example:**<br/>
`,tag docs embed`<br/>
 - Usage: `,tag docs [keyword=None]`
Extended Arg Info
> ### keyword: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,tag backup
Backup all the tag data for your server.<br/>
 - Usage: `,tag backup`
 - Restricted to: `ADMIN`
## ,tag append
Add text to a tag's TagScript.<br/>

**Example:**<br/>
`,tag append rickroll Never gonna let you down!`<br/>
 - Usage: `,tag append <tag> <tagscript>`
 - Restricted to: `MOD`
## ,tag raw
Get a tag's raw content.<br/>

The sent TagScript will be escaped from Discord style formatting characters.<br/>

**Example:**<br/>
`,tag raw noping`<br/>
 - Usage: `,tag raw <tag>`
## ,tag list
View all stored tags on this server.<br/>

To view info on a specific tag, use `,tag info`.<br/>

**Example:**<br/>
`,tag list`<br/>
 - Usage: `,tag list`
## ,tag restore
Restore all tag data for your server.<br/>

This command will restore all data from the backup file.<br/>
This command will also delete all the previously made tags if<br/>
not present in the backup file.<br/>

You can pass a message ID, a ChannelID-MessageID pair, or a message link<br/>
to the `message` argument.<br/>
Alternatively, if you want to reply to a message, pass anything to the<br/>
message argument while replying to a message.<br/>
 - Usage: `,tag restore <message>`
 - Restricted to: `ADMIN`
## ,tag add
Add a tag with TagScript.<br/>

[Tag usage guide](https://seina-cogs.readthedocs.io/en/latest/tags/blocks.html#usage)<br/>

**Example:**<br/>
`,tag add lawsofmotion {embed(title):Newton's Laws of motion}<br/>
{embed(description): According to all known laws of aviation, there is no way a bee should be able to fly.}`<br/>
 - Usage: `,tag add <tag_name> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `create and +`
## ,tag search
Search for tags by name.<br/>

**Example:**<br/>
`,tag search notsupport`<br/>
 - Usage: `,tag search <keyword>`
Extended Arg Info
> ### keyword: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,tag run
Execute TagScript without storing.<br/>

The variables and actions fields display debugging information.<br/>

**Example:**<br/>
`,tag run {#:yes,no}`<br/>
 - Usage: `,tag run <tagscript>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `execute`
Extended Arg Info
> ### tagscript: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,tag global
Global Tag management with TagScript.<br/>

These commands use TagScriptEngine.<br/>
Read the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/) to learn how to use TagScript blocks.<br/>
 - Usage: `,tag global`
 - Restricted to: `BOT_OWNER`
### ,tag global remove
Permanently delete a global tag.<br/>

If you want to remove a global tag's alias, use `,tag global unalias`.<br/>

**Example:**<br/>
`,tag global remove RickRoll`<br/>
 - Usage: `,tag global remove <tag>`
 - Aliases: `delete and -`
### ,tag global unalias
Remove an alias for a global tag.<br/>

​The global tag will still be able to be used under its original name.<br/>
You can delete the original global tag with the `,tag global remove` command.<br/>

**Example:**<br/>
`global tag unalias donate donation`<br/>
 - Usage: `,tag global unalias <tag> <alias>`
### ,tag global append
Add text to a global tag's TagScript.<br/>

**Example:**<br/>
`,tag global append rickroll Never gonna let you down!`<br/>
 - Usage: `,tag global append <tag> <tagscript>`
### ,tag global search
Search for global tags by name.<br/>

**Example:**<br/>
`,tag global search notsupport`<br/>
 - Usage: `,tag global search <keyword>`
Extended Arg Info
> ### keyword: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,tag global backup
Backup all the global tag data.<br/>
 - Usage: `,tag global backup`
### ,tag global restore

 - Usage: `,tag global restore <message>`
### ,tag global pastebin
Add a global tag with a Pastebin link.<br/>

**Example:**<br/>
`,tag global pastebin starwarsopeningcrawl https://pastebin.com/CKjn6uYv`<br/>
 - Usage: `,tag global pastebin <tag_name> <link>`
 - Aliases: `++`
### ,tag global add
Add a global tag with TagScript.<br/>

[Global Tag usage guide](https://seina-cogs.readthedocs.io/en/latest/global tags/blocks.html#usage)<br/>

**Example:**<br/>
`,tag global add lawsofmotion {embed(title):Newton's Laws of motion}<br/>
{embed(description): According to all known laws of aviation, there is no way a bee should be able to fly.}`<br/>
 - Usage: `,tag global add <tag_name> <tagscript>`
 - Aliases: `create and +`
### ,tag global alias
Add an alias for a global tag.<br/>

        Adding an alias to the global tag will make the global tag invokable using the alias or the global tag name.<br/>
        In the example below, running `,donation` will invoke the `donate` global tag.<br/>
​<br/>
        **Example:**<br/>
        `,tag global alias donate donation`<br/>
 - Usage: `,tag global alias <tag> <alias>`
### ,tag global edit
Edit a global tag's TagScript.<br/>

The passed tagscript will replace the global tag's current tagscript.<br/>
View the [TagScript docs](https://seina-cogs.readthedocs.io/en/latest/blocks.html) to find information on how to write valid tagscript.<br/>

**Example:**<br/>
`,tag global edit rickroll Never gonna give you up!`<br/>
 - Usage: `,tag global edit <tag> <tagscript>`
 - Aliases: `e`
### ,tag global list
View all stored global tags on this server.<br/>

To view info on a specific global tag, use `,tag global info`.<br/>

**Example:**<br/>
`,tag global list`<br/>
 - Usage: `,tag global list`
### ,tag global usage
See global tag usage stats.<br/>

**Example:**<br/>
`,tag global usage`<br/>
 - Usage: `,tag global usage`
 - Aliases: `stats`
### ,tag global raw
Get a global tag's raw content.<br/>

The sent TagScript will be escaped from Discord style formatting characters.<br/>

**Example:**<br/>
`,tag global raw noping`<br/>
 - Usage: `,tag global raw <tag>`
## ,tag unalias
Remove an alias for a tag.<br/>

​The tag will still be able to be used under its original name.<br/>
You can delete the original tag with the `,tag remove` command.<br/>

**Example:**<br/>
`tag unalias donate donation`<br/>
 - Usage: `,tag unalias <tag> <alias>`
 - Restricted to: `MOD`
## ,tag usage
See tag usage stats.<br/>

**Example:**<br/>
`,tag usage`<br/>
 - Usage: `,tag usage`
 - Aliases: `stats`
## ,tag edit
Edit a tag's TagScript.<br/>

The passed tagscript will replace the tag's current tagscript.<br/>
View the [TagScript docs](https://seina-cogs.readthedocs.io/en/latest/blocks.html) to find information on how to write valid tagscript.<br/>

**Example:**<br/>
`,tag edit rickroll Never gonna give you up!`<br/>
 - Usage: `,tag edit <tag> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `e`
## ,tag process
Process a temporary Tag without storing.<br/>

This differs from `,tag run` as it creates a fake tag and properly handles actions for all blocks.<br/>
The `{args}` block is not supported.<br/>

**Example:**<br/>
`,tag run {require(Admin):You must be admin to use this tag.} Congrats on being an admin!`<br/>
 - Usage: `,tag process <tagscript>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### tagscript: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
