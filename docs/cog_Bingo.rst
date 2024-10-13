Bingo
=====

<<<<<<< HEAD
# <@1275521742961508432>bingoset
Commands for setting bingo settings<br/>
 - Usage: `<@1275521742961508432>bingoset`
=======
# ,bingoset
Commands for setting bingo settings<br/>
 - Usage: `,bingoset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>bingoset name
Set the name of the current bingo card.<br/>

`name` - the name you want to use for the current bingo card.<br/>
 - Usage: `<@1275521742961508432>bingoset name <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>bingoset icon
Add an icon image to the bingo card<br/>

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.<br/>
 - Usage: `<@1275521742961508432>bingoset icon [image_url=None]`
=======
## ,bingoset stamp
Set the colour of the "stamp" that fills the box.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `,bingoset stamp <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## ,bingoset watermark
Add a watermark image to the bingo card<br/>

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.<br/>
 - Usage: `,bingoset watermark [image_url=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### image_url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>bingoset reset
Reset a users bingo card or reset the whole servers bingo card.<br/>
 - Usage: `<@1275521742961508432>bingoset reset [member=None]`
=======
## ,bingoset box
Set the colour of the Bingo card boxes border.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `,bingoset box <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## ,bingoset background
Set the colour of the Bingo card background.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `,bingoset background <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## ,bingoset text
Set the colour of the text.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `,bingoset text <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## ,bingoset tiles
Set the tiles for the servers bingo cards.<br/>

`tiles` - Separate each tile with `;`<br/>
 - Usage: `,bingoset tiles <tiles>`
Extended Arg Info
> ### tiles: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,bingoset reset
Reset a users bingo card or reset the whole servers bingo card.<br/>
 - Usage: `,bingoset reset [member=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### member: Optional[discord.member.Member] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>bingoset clear
Clear out the current bingo cards tiles.<br/>
 - Usage: `<@1275521742961508432>bingoset clear`


## <@1275521742961508432>bingoset text
Set the colour of the text.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `<@1275521742961508432>bingoset text <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## <@1275521742961508432>bingoset box
Set the colour of the Bingo card boxes border.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `<@1275521742961508432>bingoset box <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## <@1275521742961508432>bingoset tiles
Set the tiles for the servers bingo cards.<br/>

`tiles` - Separate each tile with `;`<br/>
 - Usage: `<@1275521742961508432>bingoset tiles <tiles>`
Extended Arg Info
> ### tiles: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>bingoset background
Set the colour of the Bingo card background.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `<@1275521742961508432>bingoset background <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## <@1275521742961508432>bingoset stamp
Set the colour of the "stamp" that fills the box.<br/>

`colour` - must be a hex colour code<br/>
 - Usage: `<@1275521742961508432>bingoset stamp <colour>`
Extended Arg Info
> ### colour: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## <@1275521742961508432>bingoset watermark
Add a watermark image to the bingo card<br/>

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.<br/>
 - Usage: `<@1275521742961508432>bingoset watermark [image_url=None]`
Extended Arg Info
> ### image_url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>bingoset seed
=======
## ,bingoset clear
Clear out the current bingo cards tiles.<br/>
 - Usage: `,bingoset clear`


## ,bingoset seed
>>>>>>> 9e308722 (Revamped and Fixed)
Set an additional seed to the randomness of players cards.<br/>

`seed` - A number that is added to the player ID used to<br/>
seed their card.<br/>

Use this to shuffle everyone's card while keeping the exact<br/>
same tiles for a game of bingo. Default is 0.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>bingoset seed <seed>`
=======
 - Usage: `,bingoset seed <seed>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### seed: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>bingoset settings
Show the current bingo card settings<br/>
 - Usage: `<@1275521742961508432>bingoset settings`


## <@1275521742961508432>bingoset bingo
Set the "BINGO" of the board.<br/>

`bingo` - The word to use for bingo. Must be exactly 5 characters.<br/>
 - Usage: `<@1275521742961508432>bingoset bingo <bingo>`
Extended Arg Info
> ### bingo: str
=======
## ,bingoset name
Set the name of the current bingo card.<br/>

`name` - the name you want to use for the current bingo card.<br/>
 - Usage: `,bingoset name <name>`
Extended Arg Info
> ### name: str
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>bingoset bgtile
=======
## ,bingoset bgtile
>>>>>>> 9e308722 (Revamped and Fixed)
Set the background image (tiled).<br/>

This will override the background colour if set as it will attempt<br/>
to tile the image over the entire background.<br/>

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>bingoset bgtile [image_url=None]`
=======
 - Usage: `,bingoset bgtile [image_url=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### image_url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>bingo
=======
## ,bingoset settings
Show the current bingo card settings<br/>
 - Usage: `,bingoset settings`


## ,bingoset icon
Add an icon image to the bingo card<br/>

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.<br/>
 - Usage: `,bingoset icon [image_url=None]`
Extended Arg Info
> ### image_url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,bingoset bingo
Set the "BINGO" of the board.<br/>

`bingo` - The word to use for bingo. Must be exactly 5 characters.<br/>
 - Usage: `,bingoset bingo <bingo>`
Extended Arg Info
> ### bingo: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,bingo
>>>>>>> 9e308722 (Revamped and Fixed)
Generate a Bingo Card<br/>

`stamp` - Select the tile that you would like to stamp. If not<br/>
provided will just show your current bingo card.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>bingo [stamp=None]`
=======
 - Usage: `,bingo [stamp=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`


