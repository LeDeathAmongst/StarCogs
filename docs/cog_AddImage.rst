AddImage
========

Add images the bot can upload

# ,addimage
Add an image for the bot to directly upload<br/>
 - Usage: `,addimage`
 - Checks: `server_only`


## ,addimage clear_images
Clear all the images stored for the current server<br/>
 - Usage: `,addimage clear_images`
 - Restricted to: `MOD`


## ,addimage deleteallbyuser
Delete all triggers created by a specified user ID.<br/>
 - Usage: `,addimage deleteallbyuser <user_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


## ,addimage clear_global
Clears the full set of images stored globally<br/>
 - Usage: `,addimage clear_global`
 - Restricted to: `BOT_OWNER`


## ,addimage clean_deleted_images
Cleanup deleted images that are not supposed to be saved anymore<br/>
 - Usage: `,addimage clean_deleted_images`
 - Restricted to: `MOD`


## ,addimage addglobal
Add an image to direct upload globally<br/>

`name` the command name used to post the image<br/>
 - Usage: `,addimage addglobal <name>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,addimage ignoreglobal
Toggle usage of bot owner set global images on this server<br/>
 - Usage: `,addimage ignoreglobal`
 - Restricted to: `MOD`


## ,addimage deleteglobal
Remove a selected images<br/>

`name` the command name used to post the image<br/>
 - Usage: `,addimage deleteglobal <name>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `dg and delglobal`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,addimage add
Add an image to direct upload on this server<br/>

`name` the command name used to post the image<br/>
 - Usage: `,addimage add <name>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,addimage list
List images added to bot<br/>
 - Usage: `,addimage list [image_loc=server] [server_id=None]`
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


## ,addimage delete
Remove a selected images<br/>

`name` the command name used to post the image<br/>
 - Usage: `,addimage delete <name>`
 - Restricted to: `MOD`
 - Aliases: `remove, rem, and del`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


