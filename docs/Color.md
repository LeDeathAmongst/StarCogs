View embeds showcasing the supplied color and information about it

# ,color
Group command for color commands<br/>
 - Usage: `,color`
 - Aliases: `colour`
## ,color hsl
Provides the hexadecimal value and the RGB value of the hsl value given.  Each value must have a space between them.<br/>
 - Usage: `,color hsl <h> <s> <l>`
Extended Arg Info
> ### h: float
> ```
> A number with or without decimal places.
> ```
> ### s: float
> ```
> A number with or without decimal places.
> ```
> ### l: float
> ```
> A number with or without decimal places.
> ```
## ,color name
Provides the hexadecimal value, RGB value and HSL value of a passed color.  For example, pass `red` or `blue` as the name argument.<br/>
 - Usage: `,color name <name>`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,color rgb
Provides the hexadecimal value and HSL value of the rgb value given.  Each value must have a space between them.  Highest argument must be 1 or 255, indicating the highest value of a single value (r, g, or b).<br/>
 - Usage: `,color rgb <highest> <r> <g> <b>`
Extended Arg Info
> ### highest: int
> ```
> A number without decimal places.
> ```
> ### r: float
> ```
> A number with or without decimal places.
> ```
> ### g: float
> ```
> A number with or without decimal places.
> ```
> ### b: float
> ```
> A number with or without decimal places.
> ```
## ,color hex
Provides the RGB value and HSL value of a passed hexadecimal value.  Hexadecimal value must in the format of something like `#ffffff` or `0xffffff` to be used.<br/>
 - Usage: `,color hex <hexa>`
Extended Arg Info
> ### hexa: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,color msgshort
Enable or disable the in-message shortcut.<br/>

In-message shortcuts can be used by using the hex, rgb or name after a `#` in the middle of a message, as follows:<br/>

`#000000` (hex)<br/>
`#1,1,1` (rgb)<br/>
`#black` (named)<br/>
 - Usage: `,color msgshort <enable>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### enable: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,color decimal
Provides the RGB value of the decimal value given.<br/>
 - Usage: `,color decimal <decimal>`
Extended Arg Info
> ### decimal: int
> ```
> A number without decimal places.
> ```
