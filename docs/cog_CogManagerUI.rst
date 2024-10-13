CogManagerUI
============

Commands to interface with Red's cog manager.

<<<<<<< HEAD
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
=======
# ,paths
Lists current cog paths in order of priority.<br/>
 - Usage: `,paths`
 - Restricted to: `BOT_OWNER`


# ,addpath
Add a path to the list of available cog paths.<br/>
 - Usage: `,addpath <path>`
 - Restricted to: `BOT_OWNER`


# ,removepath
Removes one or more paths from the available cog paths given the `path_numbers` from `,paths`.<br/>
 - Usage: `,removepath <path_numbers>`
 - Restricted to: `BOT_OWNER`


# ,reorderpath
Reorders paths internally to allow discovery of different cogs.<br/>
 - Usage: `,reorderpath <from_> <to>`
 - Restricted to: `BOT_OWNER`


# ,installpath
>>>>>>> 9e308722 (Revamped and Fixed)
Returns the current install path or sets it if one is provided.<br/>

The provided path must be absolute or relative to the bot's<br/>
directory and it must already exist.<br/>

No installed cogs will be transferred in the process.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>installpath [path=None]`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>cogs
Lists all loaded and available cogs.<br/>
 - Usage: `<@1275521742961508432>cogs`
=======
 - Usage: `,installpath [path=None]`
 - Restricted to: `BOT_OWNER`


# ,cogs
Lists all loaded and available cogs.<br/>
 - Usage: `,cogs`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`


