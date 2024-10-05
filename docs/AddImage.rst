AddImage
========

Add images the bot can upload

# <@1275521742961508432>addimage
Add an image for the bot to directly upload<br/>
 - Usage: `<@1275521742961508432>addimage`
 - Checks: `server_only`


## <@1275521742961508432>addimage deleteallbyuser
Delete all triggers created by a specified user ID.<br/>
 - Usage: `<@1275521742961508432>addimage deleteallbyuser <user_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>addimage delete
Remove a selected images<br/>

`name` the command name used to post the image<br/>
 - Usage: `<@1275521742961508432>addimage delete <name>`
 - Restricted to: `MOD`
 - Aliases: `remove, rem, and del`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>addimage clear_global
Clears the full set of images stored globally<br/>
 - Usage: `<@1275521742961508432>addimage clear_global`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>addimage addglobal
Add an image to direct upload globally<br/>

`name` the command name used to post the image<br/>
 - Usage: `<@1275521742961508432>addimage addglobal <name>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>addimage ignoreglobal
Toggle usage of bot owner set global images on this server<br/>
 - Usage: `<@1275521742961508432>addimage ignoreglobal`
 - Restricted to: `MOD`


## <@1275521742961508432>addimage list
List images added to bot<br/>
 - Usage: `<@1275521742961508432>addimage list [image_loc=server] [server_id=None]`
Extended Arg Info
> ### image_loc='server'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### server_id: discord.server.Guild = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     


## <@1275521742961508432>addimage clean_deleted_images
Cleanup deleted images that are not supposed to be saved anymore<br/>
 - Usage: `<@1275521742961508432>addimage clean_deleted_images`
 - Restricted to: `MOD`


## <@1275521742961508432>addimage add
Add an image to direct upload on this server<br/>

`name` the command name used to post the image<br/>
 - Usage: `<@1275521742961508432>addimage add <name>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>addimage deleteglobal
Remove a selected images<br/>

`name` the command name used to post the image<br/>
 - Usage: `<@1275521742961508432>addimage deleteglobal <name>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `dg and delglobal`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>addimage clear_images
Clear all the images stored for the current server<br/>
 - Usage: `<@1275521742961508432>addimage clear_images`
 - Restricted to: `MOD`


