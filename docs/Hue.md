Control philips hue light on the same network as the bot

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
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
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
Sets the colour using RGB colour coordinates<br/>

`red` must be a number the red value to set<br/>
`green` must be a number the green value to set<br/>
`blue` must be a number the blue value to set<br/>
`name` the name of the light to adjust<br/>
 - Usage: `,hue colour rgb <red> <green> <blue> [name]`
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
Sets the colour temperature for lights<br/>

`ct` must be a number the colour temperature to set<br/>
`name` the name of the light to adjust<br/>
 - Usage: `,hue temp [ct=500] [name]`
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
## ,hue off
Turns off light<br/>

`name` the name of the light to adjust<br/>
 - Usage: `,hue off [name]`
Extended Arg Info
> ### name=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
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
Extended Arg Info
> ### ip: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
