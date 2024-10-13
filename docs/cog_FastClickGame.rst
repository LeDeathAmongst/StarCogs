FastClickGame
=============

Play to click on the right button as fast as you can!

<<<<<<< HEAD
# <@1275521742961508432>fastclickgame (Hybrid Command)
Play to click on the right button as fast as you can!<br/>
 - Usage: `<@1275521742961508432>fastclickgame`
=======
# ,fastclickgame (Hybrid Command)
Play to click on the right button as fast as you can!<br/>
 - Usage: `,fastclickgame`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/fastclickgame`
 - Aliases: `fastclick and fcg`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>fastclickgame multi (Hybrid Command)
Play Fast Click Game with multiple rounds.<br/>
 - Usage: `<@1275521742961508432>fastclickgame multi [rounds=3] [buttons=25]`
=======
## ,fastclickgame multi (Hybrid Command)
Play Fast Click Game with multiple rounds.<br/>
 - Usage: `,fastclickgame multi [rounds=3] [buttons=25]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/fastclickgame multi [rounds=3] [buttons=25]`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>fastclickgame duel (Hybrid Command)
Play Fast Click Game with another player.<br/>
 - Usage: `<@1275521742961508432>fastclickgame duel <player>`
=======
## ,fastclickgame leaderboard (Hybrid Command)
Show Fast Click Game leaderboard.<br/>
 - Usage: `,fastclickgame leaderboard`
 - Slash Usage: `/fastclickgame leaderboard`
 - Aliases: `lb`
 - Checks: `server_only`


## ,fastclickgame duel (Hybrid Command)
Play Fast Click Game with another player.<br/>
 - Usage: `,fastclickgame duel <player>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/fastclickgame duel <player>`
 - Aliases: `single`
 - Checks: `server_only`
Extended Arg Info
> ### player: discord.member.Member
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
## <@1275521742961508432>fastclickgame leaderboard (Hybrid Command)
Show Fast Click Game leaderboard.<br/>
 - Usage: `<@1275521742961508432>fastclickgame leaderboard`
 - Slash Usage: `/fastclickgame leaderboard`
 - Aliases: `lb`
 - Checks: `server_only`


# <@1275521742961508432>setfastclickgame (Hybrid Command)
Group of commands to set FastClickGame.<br/>
 - Usage: `<@1275521742961508432>setfastclickgame`
=======
# ,setfastclickgame (Hybrid Command)
Group of commands to set FastClickGame.<br/>
 - Usage: `,setfastclickgame`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setfastclickgame`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>setfastclickgame redeconomy (Hybrid Command)
=======
## ,setfastclickgame resetleaderboard (Hybrid Command)
Reset leaderboard in the server.<br/>
 - Usage: `,setfastclickgame resetleaderboard`
 - Slash Usage: `/setfastclickgame resetleaderboard`
 - Checks: `server_only`


## ,setfastclickgame prize (Hybrid Command)
Set the prize for Red bank system and cog leaderboard. Default is 5000.<br/>

Default value: `2500`<br/>
Dev: `Range[int, 1000, 50000]`<br/>
 - Usage: `,setfastclickgame prize <value>`
 - Slash Usage: `/setfastclickgame prize <value>`
 - Checks: `server_only`


## ,setfastclickgame showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setfastclickgame showsettings [with_dev=False]`
 - Slash Usage: `/setfastclickgame showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setfastclickgame redeconomy (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
If this option is enabled, the cog will give credits to the user each time the game is won.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setfastclickgame redeconomy <value>`
=======
 - Usage: `,setfastclickgame redeconomy <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setfastclickgame redeconomy <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setfastclickgame modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `<@1275521742961508432>setfastclickgame modalconfig [confirmation=False]`
=======
## ,setfastclickgame resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setfastclickgame resetsetting <setting>`
 - Slash Usage: `/setfastclickgame resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,setfastclickgame modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setfastclickgame modalconfig [confirmation=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setfastclickgame modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setfastclickgame showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>setfastclickgame showsettings [with_dev=False]`
 - Slash Usage: `/setfastclickgame showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setfastclickgame prize (Hybrid Command)
Set the prize for Red bank system and cog leaderboard. Default is 5000.<br/>

Default value: `2500`<br/>
Dev: `Range[int, 1000, 50000]`<br/>
 - Usage: `<@1275521742961508432>setfastclickgame prize <value>`
 - Slash Usage: `/setfastclickgame prize <value>`
 - Checks: `server_only`


## <@1275521742961508432>setfastclickgame resetleaderboard (Hybrid Command)
Reset leaderboard in the server.<br/>
 - Usage: `<@1275521742961508432>setfastclickgame resetleaderboard`
 - Slash Usage: `/setfastclickgame resetleaderboard`
 - Checks: `server_only`


## <@1275521742961508432>setfastclickgame resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `<@1275521742961508432>setfastclickgame resetsetting <setting>`
 - Slash Usage: `/setfastclickgame resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


=======
>>>>>>> 9e308722 (Revamped and Fixed)
