Play local files and folders from the owner configured location

# /local (Slash Command)
Play a local file or folder, supports partial searching<br/>
 - Usage: `/local <entry> [recursive]`
 - `entry:` (Required) The local file or folder to play
 - `recursive:` (Optional) If entry is a folder, play everything inside of it recursively

 - Checks: `Server Only`
Extended Arg Info
> ### entry: str
> - Autocomplete: True
> 
> The local file or folder to play
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### recursive: bool
> - Autocomplete: False
> - Default: False
> 
> If entry is a folder, play everything inside of it recursively
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,pllocalset
Configure cog settings<br/>
 - Usage: `,pllocalset`
## ,pllocalset version
Show the version of the Cog and PyLav<br/>
 - Usage: `,pllocalset version`
## ,pllocalset update
Update the track list for /local<br/>
 - Usage: `,pllocalset update`
 - Restricted to: `BOT_OWNER`
