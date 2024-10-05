Commands to interface with Red's cog manager.

# <@1275521742961508432>paths
Lists current cog paths in order of priority.<br/>
 - Usage: `<@1275521742961508432>paths`
 - Restricted to: `BOT_OWNER`
# <@1275521742961508432>addpath
Add a path to the list of available cog paths.<br/>
 - Usage: `<@1275521742961508432>addpath <path>`
 - Restricted to: `BOT_OWNER`
# <@1275521742961508432>removepath
Removes one or more paths from the available cog paths given the `path_numbers` from `<@1275521742961508432>paths`.<br/>
 - Usage: `<@1275521742961508432>removepath <path_numbers>`
 - Restricted to: `BOT_OWNER`
# <@1275521742961508432>reorderpath
Reorders paths internally to allow discovery of different cogs.<br/>
 - Usage: `<@1275521742961508432>reorderpath <from_> <to>`
 - Restricted to: `BOT_OWNER`
# <@1275521742961508432>installpath
Returns the current install path or sets it if one is provided.<br/>

The provided path must be absolute or relative to the bot's<br/>
directory and it must already exist.<br/>

No installed cogs will be transferred in the process.<br/>
 - Usage: `<@1275521742961508432>installpath [path=None]`
 - Restricted to: `BOT_OWNER`
# <@1275521742961508432>cogs
Lists all loaded and available cogs.<br/>
 - Usage: `<@1275521742961508432>cogs`
 - Restricted to: `BOT_OWNER`
