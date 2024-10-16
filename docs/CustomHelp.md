A custom customisable help for fun and profit

# ,chelp
Configure your custom help<br/>
 - Usage: `,chelp`
 - Restricted to: `BOT_OWNER`
## ,chelp show
Show the current help settings<br/>
 - Usage: `,chelp show`
## ,chelp auto
Auto categorise cogs based on it's tags and display them<br/>
 - Usage: `,chelp auto`
## ,chelp set
Change various help settings<br/>
 - Usage: `,chelp set`
 - Aliases: `settings and setting`
### ,chelp set timeout
Set how long the help menu must stay active<br/>
 - Usage: `,chelp set timeout <wait>`
Extended Arg Info
> ### wait: int
> ```
> A number without decimal places.
> ```
### ,chelp set type
Toggles between various menus and arrow types<br/>
 - Usage: `,chelp set type`
### ,chelp set usereply
Enable/Disable replies<br/>
 - Usage: `,chelp set usereply <option>`
 - Aliases: `usereplies and reply`
Extended Arg Info
> ### option: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,chelp set thumbnail
Set your main thumbnail image here.<br/>
use `,chelp settings thumbnail` to reset this<br/>
 - Usage: `,chelp set thumbnail [url=None]`
 - Aliases: `setthumbnail`
Extended Arg Info
> ### url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,chelp set arrows
Add custom arrows for fun and profit<br/>
 - Usage: `,chelp set arrows [correct_txt]`
 - Aliases: `arrow`
Extended Arg Info
> ### correct_txt=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,chelp set deletemessage
Delete the user message that started the help menu.<br/>
Note: This only works if the bot has permissions to delete the user message, otherwise it's supressed<br/>
 - Usage: `,chelp set deletemessage <toggle>`
 - Aliases: `deleteusermessage`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,chelp set nav
Enable/Disable navigation arrows<br/>
Disabling this removes every trace of arrows and you can't move to the next page<br/>
People wanted this for some reason lol<br/>
 - Usage: `,chelp set nav <option>`
Extended Arg Info
> ### option: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,chelp list
Show the list of categories and the cogs in them<br/>
 - Usage: `,chelp list`
## ,chelp nsfw
Add categories to nsfw, only displayed in nsfw channels<br/>
 - Usage: `,chelp nsfw`
### ,chelp nsfw add
Add categories to the nsfw list<br/>
 - Usage: `,chelp nsfw add <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,chelp nsfw remove
Remove categories from the nsfw list<br/>
 - Usage: `,chelp nsfw remove <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp edit
Add reactions and descriptions to the category<br/>
 - Usage: `,chelp edit [yaml_txt]`
Extended Arg Info
> ### yaml_txt=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp load
Load another preset theme.<br/>
Use `,chelp load <theme> all` to load everything from that theme<br/>
 - Usage: `,chelp load <theme> <feature>`
Extended Arg Info
> ### theme: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp reset
Resets all settings to default **custom** help <br/>
use `,chelp set 0` to revert back to the old help<br/>
 - Usage: `,chelp reset`
### ,chelp reset hard
Hard reset, clear everything<br/>
 - Usage: `,chelp reset hard`
## ,chelp unload
Unloads the given feature, this will reset to default<br/>
 - Usage: `,chelp unload <feature>`
Extended Arg Info
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp info
Short info about various themes<br/>
 - Usage: `,chelp info`
## ,chelp remove
Remove categories/cogs or everything<br/>
 - Usage: `,chelp remove`
### ,chelp remove cog
Remove a cog(s) from across categories<br/>
 - Usage: `,chelp remove cog <cog_raw_names>`
 - Aliases: `cogs`
Extended Arg Info
> ### *cog_raw_names: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,chelp remove all
This will delete all the categories<br/>
 - Usage: `,chelp remove all`
### ,chelp remove category
Remove a multiple categories<br/>
 - Usage: `,chelp remove category <categories>`
 - Aliases: `categories and cat`
Extended Arg Info
> ### *categories: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp listthemes
List the themes and available features<br/>
 - Usage: `,chelp listthemes`
 - Aliases: `getthemes`
## ,chelp reorder
This can be used to reorder the categories.<br/>

The categories you type are pushed forward while the rest are pushed back.<br/>
 - Usage: `,chelp reorder [categories]`
Extended Arg Info
> ### categories: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp dev
Add categories to dev, only displayed to the bot owner(s)<br/>
 - Usage: `,chelp dev`
### ,chelp dev remove
Remove categories from the dev list<br/>
 - Usage: `,chelp dev remove <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,chelp dev add
Add categories to the dev list<br/>
 - Usage: `,chelp dev add <category>`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp create
Create a new category to add cogs to it using yaml<br/>
 - Usage: `,chelp create [yaml_txt]`
 - Aliases: `add`
Extended Arg Info
> ### yaml_txt=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,chelp toggle
Set to toggle custom formatter or the default help formatter<br/>
`,chelp toggle 0` to turn custom off <br/>
`,chelp toggle 1` to turn it on<br/>
 - Usage: `,chelp toggle <setval>`
Extended Arg Info
> ### setval: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,chelp refresh
Force refresh the list of categories, This would reset all the uninstalled/unloaded cogs and will put them into uncategorised.<br/>
 - Usage: `,chelp refresh`
# ,findcategory
Get the category where the command is present<br/>
 - Usage: `,findcategory <command>`
 - Aliases: `findcat`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
