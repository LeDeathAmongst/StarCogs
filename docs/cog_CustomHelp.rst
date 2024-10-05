CustomHelp
==========

A custom customisable help for fun and profit

# <@1275521742961508432>chelp
Configure your custom help<br/>
 - Usage: `<@1275521742961508432>chelp`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>chelp refresh
Force refresh the list of categories, This would reset all the uninstalled/unloaded cogs and will put them into uncategorised.<br/>
 - Usage: `<@1275521742961508432>chelp refresh`


## <@1275521742961508432>chelp list
Show the list of categories and the cogs in them<br/>
 - Usage: `<@1275521742961508432>chelp list`


## <@1275521742961508432>chelp dev
Add categories to dev, only displayed to the bot owner(s)<br/>
 - Usage: `<@1275521742961508432>chelp dev`


### <@1275521742961508432>chelp dev remove
Remove categories from the dev list<br/>
 - Usage: `<@1275521742961508432>chelp dev remove <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>chelp dev add
Add categories to the dev list<br/>
 - Usage: `<@1275521742961508432>chelp dev add <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp info
Short info about various themes<br/>
 - Usage: `<@1275521742961508432>chelp info`


## <@1275521742961508432>chelp remove
Remove categories/cogs or everything<br/>
 - Usage: `<@1275521742961508432>chelp remove`


### <@1275521742961508432>chelp remove all
This will delete all the categories<br/>
 - Usage: `<@1275521742961508432>chelp remove all`


### <@1275521742961508432>chelp remove cog
Remove a cog(s) from across categories<br/>
 - Usage: `<@1275521742961508432>chelp remove cog <cog_raw_names>`
 - Aliases: `cogs`
Extended Arg Info
> ### *cog_raw_names: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>chelp remove category
Remove a multiple categories<br/>
 - Usage: `<@1275521742961508432>chelp remove category <categories>`
 - Aliases: `categories and cat`
Extended Arg Info
> ### *categories: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp create
Create a new category to add cogs to it using yaml<br/>
 - Usage: `<@1275521742961508432>chelp create [yaml_txt]`
 - Aliases: `add`
Extended Arg Info
> ### yaml_txt=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp reorder
This can be used to reorder the categories.<br/>

The categories you type are pushed forward while the rest are pushed back.<br/>
 - Usage: `<@1275521742961508432>chelp reorder [categories]`
Extended Arg Info
> ### categories: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp edit
Add reactions and descriptions to the category<br/>
 - Usage: `<@1275521742961508432>chelp edit [yaml_txt]`
Extended Arg Info
> ### yaml_txt=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp load
Load another preset theme.<br/>
Use `<@1275521742961508432>chelp load <theme> all` to load everything from that theme<br/>
 - Usage: `<@1275521742961508432>chelp load <theme> <feature>`
Extended Arg Info
> ### theme: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp reset
Resets all settings to default **custom** help <br/>
use `<@1275521742961508432>chelp set 0` to revert back to the old help<br/>
 - Usage: `<@1275521742961508432>chelp reset`


### <@1275521742961508432>chelp reset hard
Hard reset, clear everything<br/>
 - Usage: `<@1275521742961508432>chelp reset hard`


## <@1275521742961508432>chelp unload
Unloads the given feature, this will reset to default<br/>
 - Usage: `<@1275521742961508432>chelp unload <feature>`
Extended Arg Info
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp set
Change various help settings<br/>
 - Usage: `<@1275521742961508432>chelp set`
 - Aliases: `settings and setting`


### <@1275521742961508432>chelp set arrows
Add custom arrows for fun and profit<br/>
 - Usage: `<@1275521742961508432>chelp set arrows [correct_txt]`
 - Aliases: `arrow`
Extended Arg Info
> ### correct_txt=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>chelp set thumbnail
Set your main thumbnail image here.<br/>
use `<@1275521742961508432>chelp settings thumbnail` to reset this<br/>
 - Usage: `<@1275521742961508432>chelp set thumbnail [url=None]`
 - Aliases: `setthumbnail`
Extended Arg Info
> ### url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>chelp set timeout
Set how long the help menu must stay active<br/>
 - Usage: `<@1275521742961508432>chelp set timeout <wait>`
Extended Arg Info
> ### wait: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>chelp set nav
Enable/Disable navigation arrows<br/>
Disabling this removes every trace of arrows and you can't move to the next page<br/>
People wanted this for some reason lol<br/>
 - Usage: `<@1275521742961508432>chelp set nav <option>`
Extended Arg Info
> ### option: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>chelp set type
Toggles between various menus and arrow types<br/>
 - Usage: `<@1275521742961508432>chelp set type`


### <@1275521742961508432>chelp set deletemessage
Delete the user message that started the help menu.<br/>
Note: This only works if the bot has permissions to delete the user message, otherwise it's supressed<br/>
 - Usage: `<@1275521742961508432>chelp set deletemessage <toggle>`
 - Aliases: `deleteusermessage`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>chelp set usereply
Enable/Disable replies<br/>
 - Usage: `<@1275521742961508432>chelp set usereply <option>`
 - Aliases: `usereplies and reply`
Extended Arg Info
> ### option: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>chelp nsfw
Add categories to nsfw, only displayed in nsfw channels<br/>
 - Usage: `<@1275521742961508432>chelp nsfw`


### <@1275521742961508432>chelp nsfw add
Add categories to the nsfw list<br/>
 - Usage: `<@1275521742961508432>chelp nsfw add <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>chelp nsfw remove
Remove categories from the nsfw list<br/>
 - Usage: `<@1275521742961508432>chelp nsfw remove <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>chelp listthemes
List the themes and available features<br/>
 - Usage: `<@1275521742961508432>chelp listthemes`
 - Aliases: `getthemes`


## <@1275521742961508432>chelp show
Show the current help settings<br/>
 - Usage: `<@1275521742961508432>chelp show`


## <@1275521742961508432>chelp toggle
Set to toggle custom formatter or the default help formatter<br/>
`<@1275521742961508432>chelp toggle 0` to turn custom off <br/>
`<@1275521742961508432>chelp toggle 1` to turn it on<br/>
 - Usage: `<@1275521742961508432>chelp toggle <setval>`
Extended Arg Info
> ### setval: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>chelp auto
Auto categorise cogs based on it's tags and display them<br/>
 - Usage: `<@1275521742961508432>chelp auto`


# <@1275521742961508432>findcategory
Get the category where the command is present<br/>
 - Usage: `<@1275521742961508432>findcategory <command>`
 - Aliases: `findcat`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


