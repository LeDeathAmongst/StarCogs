Play to Memory game, with buttons, leaderboard and Red bank!

# ,memorygame (Hybrid Command)
Play to Memory game. Choose between `3x3`, `4x4` and `5x5` versions.<br/>
 - Usage: `,memorygame [difficulty=5x5]`
 - Slash Usage: `/memorygame [difficulty=5x5]`
# ,memorygameleaderboard (Hybrid Command)
Show MemoryGame leaderboard.<br/>
 - Usage: `,memorygameleaderboard`
 - Slash Usage: `/memorygameleaderboard`
 - Aliases: `memorygamelb`
# ,setmemorygame (Hybrid Command)
Group of commands to set MemoryGame.<br/>
 - Usage: `,setmemorygame`
 - Slash Usage: `/setmemorygame`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## ,setmemorygame maxprize (Hybrid Command)
Set the max prize for Red bank system and cog leaderboard. Default is 5000.<br/>

Default value: `5000`<br/>
Dev: `Range[int, 1000, 50000]`<br/>
 - Usage: `,setmemorygame maxprize <value>`
 - Slash Usage: `/setmemorygame maxprize <value>`
 - Checks: `server_only`
## ,setmemorygame reductionperwrongmatch (Hybrid Command)
Set the reduction per wrong match of prize for Red bank system and cog leaderboard. Default is 15.<br/>

Default value: `15`<br/>
Dev: `Range[int, 0, 30]`<br/>
 - Usage: `,setmemorygame reductionperwrongmatch <value>`
 - Slash Usage: `/setmemorygame reductionperwrongmatch <value>`
 - Checks: `server_only`
## ,setmemorygame modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setmemorygame modalconfig [confirmation=False]`
 - Slash Usage: `/setmemorygame modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setmemorygame resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setmemorygame resetsetting <setting>`
 - Slash Usage: `/setmemorygame resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setmemorygame redeconomy (Hybrid Command)
If this option is enabled, the cog will give credits to the user each time the game is won.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setmemorygame redeconomy <value>`
 - Slash Usage: `/setmemorygame redeconomy <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setmemorygame maxwrongmatches (Hybrid Command)
Set the maximum tries for each game. Use `0` for no limit.<br/>

Default value: `None`<br/>
Dev: `Range[int, 0, 50]`<br/>
 - Usage: `,setmemorygame maxwrongmatches <value>`
 - Slash Usage: `/setmemorygame maxwrongmatches <value>`
 - Checks: `server_only`
## ,setmemorygame resetleaderboard (Hybrid Command)
Reset leaderboard in the server.<br/>
 - Usage: `,setmemorygame resetleaderboard`
 - Slash Usage: `/setmemorygame resetleaderboard`
 - Checks: `server_only`
## ,setmemorygame reductionpersecond (Hybrid Command)
Set the reduction per second of prize for Red bank system and cog leaderboard. Default is 5.<br/>

Default value: `5`<br/>
Dev: `Range[int, 0, 30]`<br/>
 - Usage: `,setmemorygame reductionpersecond <value>`
 - Slash Usage: `/setmemorygame reductionpersecond <value>`
 - Checks: `server_only`
## ,setmemorygame showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setmemorygame showsettings [with_dev=False]`
 - Slash Usage: `/setmemorygame showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
