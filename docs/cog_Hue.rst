Hue
===

Control philips hue light on the same network as the bot

<<<<<<< HEAD
# <@1275521742961508432>hue
Commands for interacting with Hue lights<br/>
 - Usage: `<@1275521742961508432>hue`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>hue colour
Sets the colour for lights<br/>
 - Usage: `<@1275521742961508432>hue colour`
 - Aliases: `color`


### <@1275521742961508432>hue colour hex
Attempt to set the colour based on hex values<br/>
Not 100% accurate<br/>

`hex` the hex code colour to try to change to<br/>
`name` the name of the light to adjust<br/>
 - Usage: `<@1275521742961508432>hue colour hex <hex_code> [name]`
Extended Arg Info
> ### hex_code
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>hue colour xy
Sets the colour using xyz colour values<br/>

`x` must be a number the x value to set<br/>
`y` must be a number the y value to set<br/>
`name` the name of the light to adjust<br/>
Note: The z value is determined from two other values<br/>
 - Usage: `<@1275521742961508432>hue colour xy <x> <y> [name]`
 - Aliases: `xyz`
Extended Arg Info
> ### x: float
> ```
> A number with or without decimal places.
> ```
> ### y: float
> ```
> A number with or without decimal places.
=======
# ,hue
Commands for interacting with Hue lights<br/>
 - Usage: `,hue`
 - Restricted to: `BOT_OWNER`


## ,hue brightness
Sets the brightness for lights<br/>

`brightness` the level of brightness to set<br/>
`name` the name of the light to adjust<br/>
 - Usage: `,hue brightness [brightness=254] [name]`
Extended Arg Info
> ### brightness: int = 254
> ```
> A number without decimal places.
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
### <@1275521742961508432>hue colour rgb
=======
## ,hue test
Testing<br/>
 - Usage: `,hue test`


## ,hue random
Sets the light to a random colour<br/>

`name` the name of the light to adjust<br/>
 - Usage: `,hue random [name]`
Extended Arg Info
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,hue on
Turns on Light<br/>

`name` the name of the light to adjust<br/>
 - Usage: `,hue on [name=None]`
Extended Arg Info
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,hue colour
Sets the colour for lights<br/>
 - Usage: `,hue colour`
 - Aliases: `color`


### ,hue colour rgb
>>>>>>> 9e308722 (Revamped and Fixed)
Sets the colour using RGB colour coordinates<br/>

`red` must be a number the red value to set<br/>
`green` must be a number the green value to set<br/>
`blue` must be a number the blue value to set<br/>
`name` the name of the light to adjust<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hue colour rgb <red> <green> <blue> [name]`
=======
 - Usage: `,hue colour rgb <red> <green> <blue> [name]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### red: float
> ```
> A number with or without decimal places.
> ```
> ### green: float
> ```
> A number with or without decimal places.
> ```
> ### blue: float
> ```
> A number with or without decimal places.
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>hue temp
=======
### ,hue colour xy
Sets the colour using xyz colour values<br/>

`x` must be a number the x value to set<br/>
`y` must be a number the y value to set<br/>
`name` the name of the light to adjust<br/>
Note: The z value is determined from two other values<br/>
 - Usage: `,hue colour xy <x> <y> [name]`
 - Aliases: `xyz`
Extended Arg Info
> ### x: float
> ```
> A number with or without decimal places.
> ```
> ### y: float
> ```
> A number with or without decimal places.
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,hue colour hex
Attempt to set the colour based on hex values<br/>
Not 100% accurate<br/>

`hex` the hex code colour to try to change to<br/>
`name` the name of the light to adjust<br/>
 - Usage: `,hue colour hex <hex_code> [name]`
Extended Arg Info
> ### hex_code
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,hue temp
>>>>>>> 9e308722 (Revamped and Fixed)
Sets the colour temperature for lights<br/>

`ct` must be a number the colour temperature to set<br/>
`name` the name of the light to adjust<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hue temp [ct=500] [name]`
=======
 - Usage: `,hue temp [ct=500] [name]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `ct, colourtemp, colortemp, and temperature`
Extended Arg Info
> ### ct: int = 500
> ```
> A number without decimal places.
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>hue off
Turns off light<br/>

`name` the name of the light to adjust<br/>
 - Usage: `<@1275521742961508432>hue off [name]`
=======
## ,hue off
Turns off light<br/>

`name` the name of the light to adjust<br/>
 - Usage: `,hue off [name]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>hue set
Commands for setting hue settings<br/>
 - Usage: `<@1275521742961508432>hue set`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>hue set connect
Setup command if bridge cannot connect<br/>
 - Usage: `<@1275521742961508432>hue set connect [ip=None]`
=======
## ,hue switch
Toggles lights on or off<br/>

`name` the name of the light to adjust<br/>
 - Usage: `,hue switch [name]`
Extended Arg Info
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,hue set
Commands for setting hue settings<br/>
 - Usage: `,hue set`
 - Restricted to: `BOT_OWNER`


### ,hue set connect
Setup command if bridge cannot connect<br/>
 - Usage: `,hue set connect [ip=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### ip: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>hue switch
Toggles lights on or off<br/>

`name` the name of the light to adjust<br/>
 - Usage: `<@1275521742961508432>hue switch [name]`
Extended Arg Info
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>hue test
Testing<br/>
 - Usage: `<@1275521742961508432>hue test`


## <@1275521742961508432>hue brightness
Sets the brightness for lights<br/>

`brightness` the level of brightness to set<br/>
`name` the name of the light to adjust<br/>
 - Usage: `<@1275521742961508432>hue brightness [brightness=254] [name]`
Extended Arg Info
> ### brightness: int = 254
> ```
> A number without decimal places.
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>hue random
Sets the light to a random colour<br/>

`name` the name of the light to adjust<br/>
 - Usage: `<@1275521742961508432>hue random [name]`
Extended Arg Info
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>hue on
Turns on Light<br/>

`name` the name of the light to adjust<br/>
 - Usage: `<@1275521742961508432>hue on [name=None]`
Extended Arg Info
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


=======
>>>>>>> 9e308722 (Revamped and Fixed)
