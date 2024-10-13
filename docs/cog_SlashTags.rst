SlashTags
=========

Create custom slash commands.

The TagScript documentation can be found [here](https://phen-cogs.readthedocs.io/en/latest/index.html).

<<<<<<< HEAD
# <@1275521742961508432>slashtag
=======
# ,slashtag
>>>>>>> 9e308722 (Revamped and Fixed)
Slash Tag management with TagScript.<br/>

These commands use TagScriptEngine.<br/>
[This site](https://phen-cogs.readthedocs.io/en/latest/index.html) has documentation on how to use TagScript blocks.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>slashtag`
=======
 - Usage: `,slashtag`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `st`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>slashtag edit
Edit a slash tag.<br/>
 - Usage: `<@1275521742961508432>slashtag edit <tag> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `e`


### <@1275521742961508432>slashtag edit argument
Edit a single slash tag's argument by name.<br/>
 - Usage: `<@1275521742961508432>slashtag edit argument <tag> <argument>`
 - Aliases: `option`
Extended Arg Info
> ### argument: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>slashtag edit arguments
Edit a slash tag's arguments.<br/>

See [this documentation page](https://phen-cogs.readthedocs.io/en/latest/slashtags/slash_arguments.html) for more information on slash tag arguments.<br/>
 - Usage: `<@1275521742961508432>slashtag edit arguments <tag>`
 - Aliases: `options`


### <@1275521742961508432>slashtag edit name
Edit a slash tag's name.<br/>
 - Usage: `<@1275521742961508432>slashtag edit name <tag> <name>`


### <@1275521742961508432>slashtag edit tagscript
Edit a slash tag's TagScript.<br/>
 - Usage: `<@1275521742961508432>slashtag edit tagscript <tag> <tagscript>`


### <@1275521742961508432>slashtag edit description
Edit a slash tag's description.<br/>
 - Usage: `<@1275521742961508432>slashtag edit description <tag> <description>`
Extended Arg Info
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>slashtag user
Add a user command tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `<@1275521742961508432>slashtag user <tag_name> <tagscript>`
 - Restricted to: `MOD`


## <@1275521742961508432>slashtag pastebin
Add a slash tag with a Pastebin link.<br/>
 - Usage: `<@1275521742961508432>slashtag pastebin <tag_name> <link>`
 - Restricted to: `MOD`
 - Aliases: `++`


## <@1275521742961508432>slashtag remove
Delete a slash tag.<br/>
 - Usage: `<@1275521742961508432>slashtag remove <tag>`
=======
## ,slashtag remove
Delete a slash tag.<br/>
 - Usage: `,slashtag remove <tag>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `delete and -`


<<<<<<< HEAD
## <@1275521742961508432>slashtag add
Add a slash tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `<@1275521742961508432>slashtag add <tag_name> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `create and +`


## <@1275521742961508432>slashtag info
Get info about a slash tag that is stored on this server.<br/>
 - Usage: `<@1275521742961508432>slashtag info <tag>`


## <@1275521742961508432>slashtag raw
Get a slash tag's raw content.<br/>
 - Usage: `<@1275521742961508432>slashtag raw <tag>`


## <@1275521742961508432>slashtag list
View stored slash tags.<br/>
 - Usage: `<@1275521742961508432>slashtag list`


## <@1275521742961508432>slashtag global
=======
## ,slashtag list
View stored slash tags.<br/>
 - Usage: `,slashtag list`


## ,slashtag message
Add a message command tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `,slashtag message <tag_name> <tagscript>`
 - Restricted to: `MOD`


## ,slashtag global
>>>>>>> 9e308722 (Revamped and Fixed)
Global Slash Tag management with TagScript.<br/>

These commands use TagScriptEngine.<br/>
[This site](https://phen-cogs.readthedocs.io/en/latest/index.html) has documentation on how to use TagScript blocks.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>slashtag global`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>slashtag global message
Add a message command global tag with TagScript.<br/>

[global Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/global slashtags/global slashtags.html)<br/>
 - Usage: `<@1275521742961508432>slashtag global message <tag_name> <tagscript>`
 - Restricted to: `MOD`


### <@1275521742961508432>slashtag global info
Get info about a global slash tag that is stored on this server.<br/>
 - Usage: `<@1275521742961508432>slashtag global info <tag>`


### <@1275521742961508432>slashtag global pastebin
Add a global slash tag with a Pastebin link.<br/>
 - Usage: `<@1275521742961508432>slashtag global pastebin <tag_name> <link>`
 - Aliases: `++`


### <@1275521742961508432>slashtag global user
Add a user command global tag with TagScript.<br/>

[global Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/global slashtags/global slashtags.html)<br/>
 - Usage: `<@1275521742961508432>slashtag global user <tag_name> <tagscript>`
 - Restricted to: `MOD`


### <@1275521742961508432>slashtag global raw
Get a global slash tag's raw content.<br/>
 - Usage: `<@1275521742961508432>slashtag global raw <tag>`


### <@1275521742961508432>slashtag global add
Add a global slash tag with TagScript.<br/>

[global Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/global slashtags/global slashtags.html)<br/>
 - Usage: `<@1275521742961508432>slashtag global add <tag_name> <tagscript>`


### <@1275521742961508432>slashtag global list
View stored global slash tags.<br/>
 - Usage: `<@1275521742961508432>slashtag global list`


### <@1275521742961508432>slashtag global remove
Delete a global slash tag.<br/>
 - Usage: `<@1275521742961508432>slashtag global remove <tag>`
 - Aliases: `delete and -`


### <@1275521742961508432>slashtag global restore
Restore all global slash tags from the database.<br/>
 - Usage: `<@1275521742961508432>slashtag global restore [tag=None]`


### <@1275521742961508432>slashtag global usage
See global slash tag usage stats.<br/>

**Example:**<br/>
`<@1275521742961508432>slashtag global usage`<br/>
 - Usage: `<@1275521742961508432>slashtag global usage`
 - Aliases: `stats`


### <@1275521742961508432>slashtag global edit
Edit a global slash tag.<br/>
 - Usage: `<@1275521742961508432>slashtag global edit <tag> <tagscript>`
 - Aliases: `e`


#### <@1275521742961508432>slashtag global edit argument
Edit a single global slash tag's argument by name.<br/>
 - Usage: `<@1275521742961508432>slashtag global edit argument <tag> <argument>`
=======
 - Usage: `,slashtag global`
 - Restricted to: `BOT_OWNER`


### ,slashtag global info
Get info about a global slash tag that is stored on this server.<br/>
 - Usage: `,slashtag global info <tag>`


### ,slashtag global pastebin
Add a global slash tag with a Pastebin link.<br/>
 - Usage: `,slashtag global pastebin <tag_name> <link>`
 - Aliases: `++`


### ,slashtag global raw
Get a global slash tag's raw content.<br/>
 - Usage: `,slashtag global raw <tag>`


### ,slashtag global message
Add a message command global tag with TagScript.<br/>

[global Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/global slashtags/global slashtags.html)<br/>
 - Usage: `,slashtag global message <tag_name> <tagscript>`
 - Restricted to: `MOD`


### ,slashtag global list
View stored global slash tags.<br/>
 - Usage: `,slashtag global list`


### ,slashtag global add
Add a global slash tag with TagScript.<br/>

[global Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/global slashtags/global slashtags.html)<br/>
 - Usage: `,slashtag global add <tag_name> <tagscript>`


### ,slashtag global remove
Delete a global slash tag.<br/>
 - Usage: `,slashtag global remove <tag>`
 - Aliases: `delete and -`


### ,slashtag global usage
See global slash tag usage stats.<br/>

**Example:**<br/>
`,slashtag global usage`<br/>
 - Usage: `,slashtag global usage`
 - Aliases: `stats`


### ,slashtag global restore
Restore all global slash tags from the database.<br/>
 - Usage: `,slashtag global restore [tag=None]`


### ,slashtag global user
Add a user command global tag with TagScript.<br/>

[global Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/global slashtags/global slashtags.html)<br/>
 - Usage: `,slashtag global user <tag_name> <tagscript>`
 - Restricted to: `MOD`


### ,slashtag global edit
Edit a global slash tag.<br/>
 - Usage: `,slashtag global edit <tag> <tagscript>`
 - Aliases: `e`


#### ,slashtag global edit name
Edit a global slash tag's name.<br/>
 - Usage: `,slashtag global edit name <tag> <name>`


#### ,slashtag global edit argument
Edit a single global slash tag's argument by name.<br/>
 - Usage: `,slashtag global edit argument <tag> <argument>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `option`
Extended Arg Info
> ### argument: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
#### <@1275521742961508432>slashtag global edit name
Edit a global slash tag's name.<br/>
 - Usage: `<@1275521742961508432>slashtag global edit name <tag> <name>`


#### <@1275521742961508432>slashtag global edit tagscript
Edit a global slash tag's TagScript.<br/>
 - Usage: `<@1275521742961508432>slashtag global edit tagscript <tag> <tagscript>`


#### <@1275521742961508432>slashtag global edit description
Edit a global slash tag's description.<br/>
 - Usage: `<@1275521742961508432>slashtag global edit description <tag> <description>`
=======
#### ,slashtag global edit description
Edit a global slash tag's description.<br/>
 - Usage: `,slashtag global edit description <tag> <description>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
#### <@1275521742961508432>slashtag global edit arguments
Edit a global slash tag's arguments.<br/>

See [this documentation page](https://phen-cogs.readthedocs.io/en/latest/global slashtags/slash_arguments.html) for more information on global slash tag arguments.<br/>
 - Usage: `<@1275521742961508432>slashtag global edit arguments <tag>`
 - Aliases: `options`


## <@1275521742961508432>slashtag clear
Clear all slash tags for this server.<br/>
 - Usage: `<@1275521742961508432>slashtag clear`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>slashtag usage
See slash tag usage stats.<br/>

**Example:**<br/>
`<@1275521742961508432>slashtag usage`<br/>
 - Usage: `<@1275521742961508432>slashtag usage`
 - Aliases: `stats`


## <@1275521742961508432>slashtag message
Add a message command tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `<@1275521742961508432>slashtag message <tag_name> <tagscript>`
 - Restricted to: `MOD`


## <@1275521742961508432>slashtag restore
Restore all slash tags from the database.<br/>
 - Usage: `<@1275521742961508432>slashtag restore [tag=None]`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>slashtagset
Manage SlashTags settings.<br/>
 - Usage: `<@1275521742961508432>slashtagset`
=======
#### ,slashtag global edit arguments
Edit a global slash tag's arguments.<br/>

See [this documentation page](https://phen-cogs.readthedocs.io/en/latest/global slashtags/slash_arguments.html) for more information on global slash tag arguments.<br/>
 - Usage: `,slashtag global edit arguments <tag>`
 - Aliases: `options`


#### ,slashtag global edit tagscript
Edit a global slash tag's TagScript.<br/>
 - Usage: `,slashtag global edit tagscript <tag> <tagscript>`


## ,slashtag restore
Restore all slash tags from the database.<br/>
 - Usage: `,slashtag restore [tag=None]`
 - Restricted to: `BOT_OWNER`


## ,slashtag clear
Clear all slash tags for this server.<br/>
 - Usage: `,slashtag clear`
 - Restricted to: `BOT_OWNER`


## ,slashtag add
Add a slash tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `,slashtag add <tag_name> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `create and +`


## ,slashtag usage
See slash tag usage stats.<br/>

**Example:**<br/>
`,slashtag usage`<br/>
 - Usage: `,slashtag usage`
 - Aliases: `stats`


## ,slashtag raw
Get a slash tag's raw content.<br/>
 - Usage: `,slashtag raw <tag>`


## ,slashtag edit
Edit a slash tag.<br/>
 - Usage: `,slashtag edit <tag> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `e`


### ,slashtag edit description
Edit a slash tag's description.<br/>
 - Usage: `,slashtag edit description <tag> <description>`
Extended Arg Info
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,slashtag edit name
Edit a slash tag's name.<br/>
 - Usage: `,slashtag edit name <tag> <name>`


### ,slashtag edit arguments
Edit a slash tag's arguments.<br/>

See [this documentation page](https://phen-cogs.readthedocs.io/en/latest/slashtags/slash_arguments.html) for more information on slash tag arguments.<br/>
 - Usage: `,slashtag edit arguments <tag>`
 - Aliases: `options`


### ,slashtag edit tagscript
Edit a slash tag's TagScript.<br/>
 - Usage: `,slashtag edit tagscript <tag> <tagscript>`


### ,slashtag edit argument
Edit a single slash tag's argument by name.<br/>
 - Usage: `,slashtag edit argument <tag> <argument>`
 - Aliases: `option`
Extended Arg Info
> ### argument: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,slashtag info
Get info about a slash tag that is stored on this server.<br/>
 - Usage: `,slashtag info <tag>`


## ,slashtag user
Add a user command tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `,slashtag user <tag_name> <tagscript>`
 - Restricted to: `MOD`


## ,slashtag pastebin
Add a slash tag with a Pastebin link.<br/>
 - Usage: `,slashtag pastebin <tag_name> <link>`
 - Restricted to: `MOD`
 - Aliases: `++`


# ,slashtagset
Manage SlashTags settings.<br/>
 - Usage: `,slashtagset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `slashset`


<<<<<<< HEAD
## <@1275521742961508432>slashtagset testing
Load or unload the SlashTag interaction development test cog.<br/>
 - Usage: `<@1275521742961508432>slashtagset testing [true_or_false=None]`
Extended Arg Info
> ### true_or_false: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>slashtagset rmeval
Remove the slash eval command.<br/>
 - Usage: `<@1275521742961508432>slashtagset rmeval`
 - Checks: `dev_check`


## <@1275521742961508432>slashtagset settings
View SlashTags settings.<br/>
 - Usage: `<@1275521742961508432>slashtagset settings`


## <@1275521742961508432>slashtagset addeval
Add a slash eval command for debugging.<br/>
 - Usage: `<@1275521742961508432>slashtagset addeval`
 - Checks: `dev_check`


## <@1275521742961508432>slashtagset appid
Manually set the application ID for Starfire slash commands if it differs from the bot user ID.<br/>

This only applies to legacy bots. If you don't know what this means, you don't need to worry about it.<br/>
 - Usage: `<@1275521742961508432>slashtagset appid [id=None]`
=======
## ,slashtagset settings
View SlashTags settings.<br/>
 - Usage: `,slashtagset settings`


## ,slashtagset appid
Manually set the application ID for Starfire slash commands if it differs from the bot user ID.<br/>

This only applies to legacy bots. If you don't know what this means, you don't need to worry about it.<br/>
 - Usage: `,slashtagset appid [id=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### id: int = None
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
=======
## ,slashtagset testing
Load or unload the SlashTag interaction development test cog.<br/>
 - Usage: `,slashtagset testing [true_or_false=None]`
Extended Arg Info
> ### true_or_false: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,slashtagset rmeval
Remove the slash eval command.<br/>
 - Usage: `,slashtagset rmeval`
 - Checks: `dev_check`


## ,slashtagset addeval
Add a slash eval command for debugging.<br/>
 - Usage: `,slashtagset addeval`
 - Checks: `dev_check`


>>>>>>> 9e308722 (Revamped and Fixed)
