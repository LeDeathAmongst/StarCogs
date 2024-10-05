LevelUp
=======

Your friendly neighborhood leveling system

Earn experience by chatting in text and voice channels, compare levels with your friends, customize your profile and view various leaderboards!

# <@1275521742961508432>weekly
View Weekly Leaderboard<br/>
 - Usage: `<@1275521742961508432>weekly [stat=exp] [displayname=True]`
 - Aliases: `week`
 - Checks: `server_only`
Extended Arg Info
> ### stat: str = 'exp'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### displayname: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>lastweekly
View Last Week's Leaderboard<br/>
 - Usage: `<@1275521742961508432>lastweekly`
 - Checks: `server_only`


# <@1275521742961508432>weeklyset
Configure Weekly LevelUp Settings<br/>
 - Usage: `<@1275521742961508432>weeklyset`
 - Restricted to: `ADMIN`
 - Aliases: `wset`
 - Checks: `server_only`


## <@1275521742961508432>weeklyset bonus
Set bonus exp for top weekly winners<br/>
 - Usage: `<@1275521742961508432>weeklyset bonus <bonus>`
Extended Arg Info
> ### bonus: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>weeklyset toggle
Toggle weekly stat tracking<br/>
 - Usage: `<@1275521742961508432>weeklyset toggle`


## <@1275521742961508432>weeklyset autoreset
Toggle auto reset of weekly stats<br/>
 - Usage: `<@1275521742961508432>weeklyset autoreset`


## <@1275521742961508432>weeklyset ping
Toggle whether to ping winners in announcement<br/>
 - Usage: `<@1275521742961508432>weeklyset ping`


## <@1275521742961508432>weeklyset role
Set role to award top weekly winners<br/>
 - Usage: `<@1275521742961508432>weeklyset role <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>weeklyset roleall
Toggle whether all winners get the role<br/>
 - Usage: `<@1275521742961508432>weeklyset roleall`


## <@1275521742961508432>weeklyset channel
Set channel to announce weekly winners<br/>
 - Usage: `<@1275521742961508432>weeklyset channel <channel>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>weeklyset day
Set day for weekly stats reset<br/>
0 = Monday<br/>
1 = Tuesday<br/>
2 = Wednesday<br/>
3 = Thursday<br/>
4 = Friday<br/>
5 = Saturday<br/>
6 = Sunday<br/>
 - Usage: `<@1275521742961508432>weeklyset day <day>`
Extended Arg Info
> ### day: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>weeklyset hour
Set hour for weekly stats reset<br/>
 - Usage: `<@1275521742961508432>weeklyset hour <hour>`
Extended Arg Info
> ### hour: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>weeklyset reset
Reset the weekly leaderboard manually and announce winners<br/>
 - Usage: `<@1275521742961508432>weeklyset reset <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>weeklyset winners
Set number of winners to display<br/>

Due to Discord limitations with max embed field count, the maximum number of winners is 25<br/>
 - Usage: `<@1275521742961508432>weeklyset winners <count>`
Extended Arg Info
> ### count: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>weeklyset view
View the current weekly settings<br/>
 - Usage: `<@1275521742961508432>weeklyset view`


## <@1275521742961508432>weeklyset autoremove
Remove role from previous winner when new one is announced<br/>
 - Usage: `<@1275521742961508432>weeklyset autoremove`


# <@1275521742961508432>leveltop (Hybrid Command)
View the LevelUp leaderboard<br/>
 - Usage: `<@1275521742961508432>leveltop [stat=exp] [globalstats=False] [displayname=True]`
 - Slash Usage: `/leveltop [stat=exp] [globalstats=False] [displayname=True]`
 - Aliases: `lvltop, topstats, membertop, and topranks`
 - Checks: `server_only`
Extended Arg Info
> ### stat: str = 'exp'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### globalstats: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### displayname: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>roletop
View the leaderboard for roles<br/>
 - Usage: `<@1275521742961508432>roletop`
 - Checks: `server_only`


# <@1275521742961508432>profile (Hybrid Command)
View User Profile<br/>
 - Usage: `<@1275521742961508432>profile [user]`
 - Slash Usage: `/profile [user]`
 - Aliases: `pf`
 - Cooldown: `3 per 10.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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


# <@1275521742961508432>prestige (Hybrid Command)
Prestige your rank!<br/>
Once you have reached this servers prestige level requirement, you can<br/>
reset your level and experience to gain a prestige level and any perks associated with it<br/>

If you are over level and xp when you prestige, your xp and levels will carry over<br/>
 - Usage: `<@1275521742961508432>prestige`
 - Slash Usage: `/prestige`
 - Checks: `server_only`


# <@1275521742961508432>setprofile (Hybrid Command)
Customize your profile<br/>
 - Usage: `<@1275521742961508432>setprofile`
 - Slash Usage: `/setprofile`
 - Aliases: `myprofile, mypf, and pfset`
 - Checks: `server_only`


## <@1275521742961508432>setprofile remfont (Hybrid Command)
Remove a default font from the cog's fonts folder<br/>
 - Usage: `<@1275521742961508432>setprofile remfont <filename>`
 - Slash Usage: `/setprofile remfont <filename>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### filename: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile blur (Hybrid Command)
Toggle a slight blur effect on the background image where the text is displayed.<br/>
 - Usage: `<@1275521742961508432>setprofile blur`
 - Slash Usage: `/setprofile blur`


## <@1275521742961508432>setprofile view (Hybrid Command)
View your profile settings<br/>
 - Usage: `<@1275521742961508432>setprofile view`
 - Slash Usage: `/setprofile view`


## <@1275521742961508432>setprofile bgpath (Hybrid Command)
Get the folder paths for this cog's backgrounds<br/>
 - Usage: `<@1275521742961508432>setprofile bgpath`
 - Slash Usage: `/setprofile bgpath`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>setprofile fonts (Hybrid Command)
View the available fonts you can use<br/>
 - Usage: `<@1275521742961508432>setprofile fonts`
 - Slash Usage: `/setprofile fonts`
 - Cooldown: `1 per 5.0 seconds`


## <@1275521742961508432>setprofile shownick (Hybrid Command)
Toggle whether your nickname or username is shown in your profile<br/>
 - Usage: `<@1275521742961508432>setprofile shownick`
 - Slash Usage: `/setprofile shownick`


## <@1275521742961508432>setprofile rembackground (Hybrid Command)
Remove a default background from the cog's backgrounds folder<br/>
 - Usage: `<@1275521742961508432>setprofile rembackground <filename>`
 - Slash Usage: `/setprofile rembackground <filename>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### filename: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile addfont (Hybrid Command)
Add a custom font to the cog from discord<br/>

**Arguments**<br/>
`preferred_filename` - If a name is given, it will be saved as this name instead of the filename<br/>
**Note:** do not include the file extension in the preferred name, it will be added automatically<br/>
 - Usage: `<@1275521742961508432>setprofile addfont [preferred_filename=None]`
 - Slash Usage: `/setprofile addfont [preferred_filename=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### preferred_filename: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile namecolor (Hybrid Command)
Set a color for your username<br/>

For a specific color, try **[Google's hex color picker](https://htmlcolorcodes.com/)**<br/>

Set to `default` to randomize the color each time your profile is generated<br/>
 - Usage: `<@1275521742961508432>setprofile namecolor <color>`
 - Slash Usage: `/setprofile namecolor <color>`
 - Aliases: `name`
Extended Arg Info
> ### color: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile style (Hybrid Command)
Set your profile image style<br/>

- `default` is the default profile style, very customizable<br/>
- `runescape` is a runescape style profile, less customizable but more nostalgic<br/>
- (WIP) - more to come<br/>
 - Usage: `<@1275521742961508432>setprofile style <style>`
 - Slash Usage: `/setprofile style <style>`


## <@1275521742961508432>setprofile barcolor (Hybrid Command)
Set a color for your level bar<br/>

For a specific color, try **[Google's hex color picker](https://htmlcolorcodes.com/)**<br/>

Set to `default` to randomize the color each time your profile is generated<br/>
 - Usage: `<@1275521742961508432>setprofile barcolor <color>`
 - Slash Usage: `/setprofile barcolor <color>`
 - Aliases: `levelbar, lvlbar, and bar`
Extended Arg Info
> ### color: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile statcolor (Hybrid Command)
Set a color for your server stats<br/>

For a specific color, try **[Google's hex color picker](https://htmlcolorcodes.com/)**<br/>

Set to `default` to randomize the color each time your profile is generated<br/>
 - Usage: `<@1275521742961508432>setprofile statcolor <color>`
 - Slash Usage: `/setprofile statcolor <color>`
 - Aliases: `stat`
Extended Arg Info
> ### color: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile fontpath (Hybrid Command)
Get folder paths for this cog's fonts<br/>
 - Usage: `<@1275521742961508432>setprofile fontpath`
 - Slash Usage: `/setprofile fontpath`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>setprofile addbackground (Hybrid Command)
Add a custom background to the cog from discord<br/>

**Arguments**<br/>
`preferred_filename` - If a name is given, it will be saved as this name instead of the filename<br/>

**DISCLAIMER**<br/>
- Do not replace any existing file names with custom images<br/>
- If you add broken or corrupt images it can break the cog<br/>
- Do not include the file extension in the preferred name, it will be added automatically<br/>
 - Usage: `<@1275521742961508432>setprofile addbackground [preferred_filename=None]`
 - Slash Usage: `/setprofile addbackground [preferred_filename=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### preferred_filename: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile background (Hybrid Command)
Set a background for your profile<br/>

This will override your profile banner as the background<br/>

**WARNING**<br/>
The default profile style is wide (1050 by 450 pixels) with an aspect ratio of 21:9.<br/>
Portrait images will be cropped.<br/>

Tip: Googling "dual monitor backgrounds" gives good results for the right images<br/>

Here are some good places to look.<br/>
[dualmonitorbackgrounds](https://www.dualmonitorbackgrounds.com/)<br/>
[setaswall](https://www.setaswall.com/dual-monitor-wallpapers/)<br/>
[pexels](https://www.pexels.com/photo/panoramic-photography-of-trees-and-lake-358482/)<br/>
[teahub](https://www.teahub.io/searchw/dual-monitor/)<br/>

**Additional Options**<br/>
 - Leave `url` blank or specify `default` to reset back to using your profile banner (or random if you don't have one)<br/>
 - `random` will randomly select from a pool of default backgrounds each time<br/>
 - `filename` run `<@1275521742961508432>mypf backgrounds` to view default options you can use by including their filename<br/>
 - Usage: `<@1275521742961508432>setprofile background [url=None]`
 - Slash Usage: `/setprofile background [url=None]`
 - Aliases: `bg`
Extended Arg Info
> ### url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile font (Hybrid Command)
Set a font for your profile<br/>

To view available fonts, type `<@1275521742961508432>myprofile fonts`<br/>
To revert to the default font, use `default` for the `font_name` argument<br/>
 - Usage: `<@1275521742961508432>setprofile font <font_name>`
 - Slash Usage: `/setprofile font <font_name>`
Extended Arg Info
> ### font_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setprofile backgrounds (Hybrid Command)
View the all available backgrounds<br/>
 - Usage: `<@1275521742961508432>setprofile backgrounds`
 - Slash Usage: `/setprofile backgrounds`
 - Cooldown: `1 per 5.0 seconds`


# <@1275521742961508432>stars (Hybrid Command)
Reward a good noodle<br/>
 - Usage: `<@1275521742961508432>stars [user]`
 - Slash Usage: `/stars [user]`
 - Aliases: `givestar, addstar, and thanks`
 - Checks: `server_only`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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


# <@1275521742961508432>startop
View the Star Leaderboard<br/>
 - Usage: `<@1275521742961508432>startop [globalstats=False] [displayname=True]`
 - Aliases: `topstars, starleaderboard, and starlb`
 - Checks: `server_only`
Extended Arg Info
> ### globalstats: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### displayname: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>starset
Configure LevelUp Star Settings<br/>
 - Usage: `<@1275521742961508432>starset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## <@1275521742961508432>starset mentiondelete
Toggle whether the bot auto-deletes the star mentions<br/>

Set to 0 to disable auto-delete<br/>
 - Usage: `<@1275521742961508432>starset mentiondelete <delete_after>`
Extended Arg Info
> ### delete_after: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>starset view
View Star Settings<br/>
 - Usage: `<@1275521742961508432>starset view`


## <@1275521742961508432>starset cooldown
Set the star cooldown<br/>
 - Usage: `<@1275521742961508432>starset cooldown <cooldown>`
Extended Arg Info
> ### cooldown: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>starset mention
Toggle star reaction mentions<br/>
 - Usage: `<@1275521742961508432>starset mention`


# <@1275521742961508432>levelowner
Owner Only LevelUp Settings<br/>
 - Usage: `<@1275521742961508432>levelowner`
 - Restricted to: `BOT_OWNER`
 - Aliases: `lvlowner`
 - Checks: `server_only`


## <@1275521742961508432>levelowner ignore
Add/Remove a server from the ignore list<br/>
 - Usage: `<@1275521742961508432>levelowner ignore <server_id>`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelowner internalapi
Enable internal API for parallel image generation<br/>

Setting a port will spin up a detatched but cog-managed FastAPI server to handle image generation.<br/>
The process ID will be attached to the bot object and persist through reloads.<br/>

**USE AT YOUR OWN RISK!!!**<br/>
Using the internal API will spin up multiple subprocesses to handle bulk image generation.<br/>
If your bot crashes, the API subprocess will not be killed and will need to be manually terminated!<br/>
It is HIGHLY reccommended to host the api separately!<br/>

Set to 0 to disable the internal API<br/>

**Notes**<br/>
- This will spin up a 1 worker per core on the bot's cpu.<br/>
- If the API fails, the cog will fall back to the default image generation method.<br/>
 - Usage: `<@1275521742961508432>levelowner internalapi <port>`
Extended Arg Info
> ### port: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelowner cache
Set the cache time for user profiles<br/>
 - Usage: `<@1275521742961508432>levelowner cache <seconds>`
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelowner backupinterval
Set the interval for backups<br/>
 - Usage: `<@1275521742961508432>levelowner backupinterval <interval>`
Extended Arg Info
> ### interval: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelowner autoclean
Toggle purging of config data for servers the bot is no longer in<br/>
 - Usage: `<@1275521742961508432>levelowner autoclean`


## <@1275521742961508432>levelowner rendergifs
Toggle rendering of GIFs for animated profiles<br/>
 - Usage: `<@1275521742961508432>levelowner rendergifs`
 - Aliases: `rendergif and gif`


## <@1275521742961508432>levelowner forceembeds
Toggle enforcing profile embeds<br/>

If enabled, profiles will only use embeds on all servers.<br/>
This disables image generation globally.<br/>
 - Usage: `<@1275521742961508432>levelowner forceembeds`
 - Aliases: `forceembed`


## <@1275521742961508432>levelowner ignorebots
Toggle ignoring bots for XP and profiles<br/>

**USE AT YOUR OWN RISK**<br/>
Allowing your bot to listen to other bots is a BAD IDEA and should NEVER be enabled on public bots.<br/>
 - Usage: `<@1275521742961508432>levelowner ignorebots`


## <@1275521742961508432>levelowner view
View Global LevelUp Settings<br/>
 - Usage: `<@1275521742961508432>levelowner view`


## <@1275521742961508432>levelowner maxbackups
Set the maximum number of backups to keep<br/>
 - Usage: `<@1275521742961508432>levelowner maxbackups <backups>`
Extended Arg Info
> ### backups: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelowner externalapi
Set the external API URL for image generation<br/>

Set to an `none` to disable the external API<br/>

**Notes**<br/>
- If the API fails, the cog will fall back to the default image generation method.<br/>
 - Usage: `<@1275521742961508432>levelowner externalapi <url>`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>mocklvl
Test LevelUp Image Generation<br/>
 - Usage: `<@1275521742961508432>mocklvl`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>leveldata
Admin Only Data Commands<br/>
 - Usage: `<@1275521742961508432>leveldata`
 - Restricted to: `ADMIN`
 - Aliases: `lvldata and ldata`
 - Checks: `server_only`


## <@1275521742961508432>leveldata reset
Reset all user data in this server<br/>
 - Usage: `<@1275521742961508432>leveldata reset`


## <@1275521742961508432>leveldata backupcog
Backup the cog's data<br/>
 - Usage: `<@1275521742961508432>leveldata backupcog`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>leveldata restore
Restore this server's data<br/>
 - Usage: `<@1275521742961508432>leveldata restore`


## <@1275521742961508432>leveldata importfixator
Import data from Fixator's Leveler cog<br/>

This will overwrite existing LevelUp level data and stars<br/>
It will also import XP range level roles, and ignored channels<br/>

*Obviously you will need MongoDB running while you run this command*<br/>
 - Usage: `<@1275521742961508432>leveldata importfixator`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>leveldata restorecog
Restore the cog's data<br/>
 - Usage: `<@1275521742961508432>leveldata restorecog`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>leveldata importmalarne
Import levels and exp from Malarne's Leveler cog<br/>

**Arguments**<br/>
➣ `import_by` - Import by level or exp<br/>
• If `level`, it will import their level and calculate exp from that.<br/>
• If `exp`, it will import their exp directly and calculate level from that.<br/>
➣ `replace` - Replace existing data (True/False)<br/>
• If True, it will replace existing data.<br/>
➣ `all_users` - Import all users regardless of if they're in the server (True/False)<br/>
 - Usage: `<@1275521742961508432>leveldata importmalarne <import_by> <replace> <all_users>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### replace: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### all_users: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>leveldata importmee6
Import levels and exp from MEE6<br/>

**Arguments**<br/>
➣ `import_by` - Import by level or exp<br/>
• If `level`, it will import their level and calculate exp from that.<br/>
• If `exp`, it will import their exp directly and calculate level from that.<br/>
➣ `replace` - Replace existing data (True/False)<br/>
➣ `include_settings` - Include MEE6 settings (True/False)<br/>
➣ `all_users` - Import all users regardless of if they're in the server (True/False)<br/>
 - Usage: `<@1275521742961508432>leveldata importmee6 <import_by> <replace> <include_settings> <all_users>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### replace: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### include_settings: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### all_users: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>leveldata resetcog
Reset the ENTIRE cog's data<br/>
 - Usage: `<@1275521742961508432>leveldata resetcog`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>leveldata importamari
Import levels and exp from AmariBot<br/>
**Arguments**<br/>
➣ `import_by` - Import by level or exp<br/>
• If `level`, it will import their level and calculate exp from that.<br/>
• If `exp`, it will import their exp directly and calculate level from that.<br/>
➣ `replace` - Replace existing data (True/False)<br/>
• If True, it will replace existing data.<br/>
➣ `api_key` - Your [AmariBot API key](https://docs.google.com/forms/d/e/1FAIpQLScQDCsIqaTb1QR9BfzbeohlUJYA3Etwr-iSb0CRKbgjA-fq7Q/viewform?usp=send_form)<br/>
➣ `all_users` - Import all users regardless of if they're in the server (True/False)<br/>
 - Usage: `<@1275521742961508432>leveldata importamari <import_by> <replace> <api_key> <all_users>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### replace: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### api_key: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### all_users: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>leveldata resetglobal
Reset user data for all servers<br/>
 - Usage: `<@1275521742961508432>leveldata resetglobal`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>leveldata importpolaris
Import levels and exp from Polaris<br/>

**Make sure your server's leaderboard is public!**<br/>

**Arguments**<br/>
➣ `replace` - Replace existing data (True/False)<br/>
➣ `include_settings` - Include Polaris settings (True/False)<br/>
➣ `all_users` - Import all users regardless of if they're in the server (True/False)<br/>

[Polaris](https://gdcolon.com/polaris/)<br/>
 - Usage: `<@1275521742961508432>leveldata importpolaris <replace> <include_settings> <all_users>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### replace: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### include_settings: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### all_users: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>leveldata backup
Backup this server's data<br/>
 - Usage: `<@1275521742961508432>leveldata backup`


## <@1275521742961508432>leveldata cleanup
Cleanup the database<br/>

Performs the following actions:<br/>
- Delete data for users no longer in the server<br/>
- Removes channels and roles that no longer exist<br/>
 - Usage: `<@1275521742961508432>leveldata cleanup`


# <@1275521742961508432>levelset
Configure LevelUp Settings<br/>
 - Usage: `<@1275521742961508432>levelset`
 - Restricted to: `ADMIN`
 - Aliases: `lvlset and lset`
 - Checks: `server_only`


## <@1275521742961508432>levelset addxp
Add XP to a user or role<br/>
 - Usage: `<@1275521742961508432>levelset addxp <user_or_role> <xp>`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
> ### xp: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelset voice
Voice settings<br/>
 - Usage: `<@1275521742961508432>levelset voice`


### <@1275521742961508432>levelset voice invisible
Ignore invisible voice users<br/>
Toggle whether invisible users in a voice channel can gain voice XP<br/>
 - Usage: `<@1275521742961508432>levelset voice invisible`


### <@1275521742961508432>levelset voice deafened
Ignore deafened voice users<br/>
Toggle whether deafened users in a voice channel can gain voice XP<br/>
 - Usage: `<@1275521742961508432>levelset voice deafened`


### <@1275521742961508432>levelset voice channelbonus
Add a range of bonus XP to apply to certain channels<br/>

This bonus applies to voice time xp<br/>

Set both min and max to 0 to remove the role bonus<br/>
 - Usage: `<@1275521742961508432>levelset voice channelbonus <channel> <min_xp> <max_xp>`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### min_xp: int
> ```
> A number without decimal places.
> ```
> ### max_xp: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset voice rolebonus
Add a range of bonus XP to apply to certain roles<br/>

This bonus applies to voice time xp<br/>

Set both min and max to 0 to remove the role bonus<br/>
 - Usage: `<@1275521742961508432>levelset voice rolebonus <role> <min_xp> <max_xp>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### min_xp: int
> ```
> A number without decimal places.
> ```
> ### max_xp: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset voice muted
Ignore muted voice users<br/>
Toggle whether self-muted users in a voice channel can gain voice XP<br/>
 - Usage: `<@1275521742961508432>levelset voice muted`


### <@1275521742961508432>levelset voice xp
Set voice XP gain<br/>
Sets the amount of XP gained per minute in a voice channel (default is 2)<br/>
 - Usage: `<@1275521742961508432>levelset voice xp <voice_xp>`
Extended Arg Info
> ### voice_xp: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset voice streambonus
Add a range of bonus XP to users who are Discord streaming<br/>

This bonus applies to voice time xp<br/>

Set both min and max to 0 to remove the bonus<br/>
 - Usage: `<@1275521742961508432>levelset voice streambonus <min_xp> <max_xp>`
Extended Arg Info
> ### min_xp: int
> ```
> A number without decimal places.
> ```
> ### max_xp: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset voice solo
Ignore solo voice users<br/>
Toggle whether solo users in a voice channel can gain voice XP<br/>
 - Usage: `<@1275521742961508432>levelset voice solo`


## <@1275521742961508432>levelset dm
Toggle DM notifications<br/>

Determines whether LevelUp messages are DM'd to the user<br/>
 - Usage: `<@1275521742961508432>levelset dm`


## <@1275521742961508432>levelset setlevel
Set a user's level<br/>

**Arguments**<br/>
• `user` - The user to set the level for<br/>
• `level` - The level to set the user to<br/>
 - Usage: `<@1275521742961508432>levelset setlevel <user> <level>`
Extended Arg Info
> ### user: discord.member.Member
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
> ### level: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelset starmentiondelete
Toggle whether the bot auto-deletes the star mentions<br/>
Set to 0 to disable auto-delete<br/>
 - Usage: `<@1275521742961508432>levelset starmentiondelete <deleted_after>`
Extended Arg Info
> ### deleted_after: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelset forcestyle
Force a profile style for all users<br/>

Specify `none` to disable the forced style<br/>
 - Usage: `<@1275521742961508432>levelset forcestyle <style>`


## <@1275521742961508432>levelset levelupmessages
Level up alert messages<br/>

**Arguments**<br/>
The following placeholders can be used:<br/>
• `{username}`: The user's name<br/>
• `{mention}`: Mentions the user<br/>
• `{displayname}`: The user's display name<br/>
• `{level}`: The level the user just reached<br/>
• `{server}`: The server the user is in<br/>

**If using dmrole or msgrole**<br/>
• `{role}`: The role the user just recieved<br/>
 - Usage: `<@1275521742961508432>levelset levelupmessages`
 - Aliases: `lvlalerts, levelalerts, lvlmessages, and lvlmsg`


### <@1275521742961508432>levelset levelupmessages dm
Set the DM a user gets when they level up (Without recieving a role).<br/>

**Arguments**<br/>
The following placeholders can be used:<br/>
• `{username}`: The user's name<br/>
• `{mention}`: Mentions the user<br/>
• `{displayname}`: The user's display name<br/>
• `{level}`: The level the user just reached<br/>
• `{server}`: The server the user is in<br/>
 - Usage: `<@1275521742961508432>levelset levelupmessages dm [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>levelset levelupmessages msgrole
Set the message sent when a user levels up and recieves a role.<br/>

**Arguments**<br/>
The following placeholders can be used:<br/>
• `{username}`: The user's name<br/>
• `{mention}`: Mentions the user<br/>
• `{displayname}`: The user's display name<br/>
• `{level}`: The level the user just reached<br/>
• `{server}`: The server the user is in<br/>
• `{role}`: The role the user just recieved<br/>
 - Usage: `<@1275521742961508432>levelset levelupmessages msgrole [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>levelset levelupmessages msg
Set the message sent when a user levels up.<br/>

**Arguments**<br/>
The following placeholders can be used:<br/>
• `{username}`: The user's name<br/>
• `{mention}`: Mentions the user<br/>
• `{displayname}`: The user's display name<br/>
• `{level}`: The level the user just reached<br/>
• `{server}`: The server the user is in<br/>
 - Usage: `<@1275521742961508432>levelset levelupmessages msg [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>levelset levelupmessages dmrole
Set the DM a user gets when they level up and recieve a role.<br/>

**Arguments**<br/>
The following placeholders can be used:<br/>
• `{username}`: The user's name<br/>
• `{mention}`: Mentions the user<br/>
• `{displayname}`: The user's display name<br/>
• `{level}`: The level the user just reached<br/>
• `{server}`: The server the user is in<br/>
• `{role}`: The role the user just recieved<br/>
 - Usage: `<@1275521742961508432>levelset levelupmessages dmrole [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>levelset levelupmessages view
View the current level up alert messages<br/>
 - Usage: `<@1275521742961508432>levelset levelupmessages view`


## <@1275521742961508432>levelset roles
Level role assignment<br/>
 - Usage: `<@1275521742961508432>levelset roles`


### <@1275521742961508432>levelset roles remove
Unassign a role from a level<br/>
 - Usage: `<@1275521742961508432>levelset roles remove <level>`
 - Aliases: `rem and del`
Extended Arg Info
> ### level: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset roles autoremove
Automatic removal of previous level roles<br/>
 - Usage: `<@1275521742961508432>levelset roles autoremove`


### <@1275521742961508432>levelset roles initialize
Initialize level roles<br/>

This command is for if you added level roles after users have achieved that level,<br/>
it will apply all necessary roles to a user according to their level and prestige<br/>
 - Usage: `<@1275521742961508432>levelset roles initialize`
 - Aliases: `init`
 - Cooldown: `1 per 240.0 seconds`


### <@1275521742961508432>levelset roles add
Assign a role to a level<br/>
 - Usage: `<@1275521742961508432>levelset roles add <level> <role>`
Extended Arg Info
> ### level: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>levelset removexp
Remove XP from a user or role<br/>
 - Usage: `<@1275521742961508432>levelset removexp <user_or_role> <xp>`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
> ### xp: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelset levelchannel
Set LevelUp log channel<br/>

Set a channel for all level up messages to send to.<br/>

If level notify is off and mention is on, the bot will mention the user in the channel<br/>
 - Usage: `<@1275521742961508432>levelset levelchannel [channel=None]`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>levelset resetemojis
Reset the emojis to default<br/>
 - Usage: `<@1275521742961508432>levelset resetemojis`


## <@1275521742961508432>levelset setprestige
Set a user to a specific prestige level<br/>

Prestige roles will need to be manually added/removed when using this command<br/>
 - Usage: `<@1275521742961508432>levelset setprestige <user> <prestige>`
Extended Arg Info
> ### user: discord.member.Member
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
> ### prestige: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelset levelnotify
Send levelup message in the channel the user is typing in<br/>

Send a message in the channel a user is typing in when they level up<br/>
 - Usage: `<@1275521742961508432>levelset levelnotify`


## <@1275521742961508432>levelset toggle
Toggle the LevelUp system<br/>
 - Usage: `<@1275521742961508432>levelset toggle`


## <@1275521742961508432>levelset allowed
Base command for all allowed lists<br/>
 - Usage: `<@1275521742961508432>levelset allowed`


### <@1275521742961508432>levelset allowed role
Add/Remove a role in the allowed list<br/>
If the allow list is not empty, only roles in the list will gain XP<br/>

Use the command with a role already in the allowed list to remove it<br/>
 - Usage: `<@1275521742961508432>levelset allowed role <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>levelset allowed channel
Add/Remove a channel in the allowed list<br/>
If the allow list is not empty, only channels in the list will gain XP<br/>

Use the command with a channel already in the allowed list to remove it<br/>
 - Usage: `<@1275521742961508432>levelset allowed channel <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.CategoryChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>levelset starmention
Toggle star reaction mentions<br/>
Toggle whether the bot mentions that a user reacted to a message with a star<br/>
 - Usage: `<@1275521742961508432>levelset starmention`


## <@1275521742961508432>levelset emojis
Set the emojis used to represent each stat type<br/>
 - Usage: `<@1275521742961508432>levelset emojis <level> <prestige> <star> <chat> <voicetime> <experience> <balance>`
Extended Arg Info
> ### level: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### prestige: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### star: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### chat: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### voicetime: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### experience: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### balance: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>levelset ignore
Base command for all ignore lists<br/>
 - Usage: `<@1275521742961508432>levelset ignore`


### <@1275521742961508432>levelset ignore channel
Add/Remove a channel in the ignore list<br/>
Channels in the ignore list don't gain XP<br/>

Use the command with a channel already in the ignore list to remove it<br/>
 - Usage: `<@1275521742961508432>levelset ignore channel <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.CategoryChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### <@1275521742961508432>levelset ignore user
Add/Remove a user in the ignore list<br/>
Members in the ignore list don't gain XP<br/>

Use the command with a user already in the ignore list to remove them<br/>
 - Usage: `<@1275521742961508432>levelset ignore user <user>`
Extended Arg Info
> ### user: discord.member.Member
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


### <@1275521742961508432>levelset ignore role
Add/Remove a role in the ignore list<br/>
Members with roles in the ignore list don't gain XP<br/>

Use the command with a role already in the ignore list to remove it<br/>
 - Usage: `<@1275521742961508432>levelset ignore role <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>levelset algorithm
Customize the leveling algorithm for your server<br/>
• Default base is 100<br/>
• Default exp is 2<br/>

**Equation**<br/>
➣ Getting required XP for a level<br/>
• `base * (level ^ exp) = XP`<br/>
➣ Getting required level for an XP value<br/>
• `level = (XP / base) ^ (1 / exp)`<br/>

**Arguments**<br/>
➣ `part` - The part of the algorithm to change<br/>
➣ `value` - The value to set it to<br/>
 - Usage: `<@1275521742961508432>levelset algorithm <part> <value>`
 - Aliases: `algo`
Extended Arg Info
> ### value: Union[float, int]
> ```
> A number with or without decimal places.
> ```


## <@1275521742961508432>levelset showbalance
Toggle whether to show user's economy credit balance in their profile<br/>
 - Usage: `<@1275521742961508432>levelset showbalance`
 - Aliases: `showbal`


## <@1275521742961508432>levelset mention
Toggle whether to mention the user in the level up message<br/>

If level notify is on AND a log channel is set, the user will only be mentioned in the channel they are in.<br/>
 - Usage: `<@1275521742961508432>levelset mention`


## <@1275521742961508432>levelset prestige
Prestige settings<br/>
 - Usage: `<@1275521742961508432>levelset prestige`


### <@1275521742961508432>levelset prestige level
Set the level required to prestige<br/>
 - Usage: `<@1275521742961508432>levelset prestige level <level>`
Extended Arg Info
> ### level: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset prestige remove
Remove a prestige level<br/>
 - Usage: `<@1275521742961508432>levelset prestige remove <prestige>`
 - Aliases: `rem and del`
Extended Arg Info
> ### prestige: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset prestige keeproles
Keep level roles after prestiging<br/>
 - Usage: `<@1275521742961508432>levelset prestige keeproles`


### <@1275521742961508432>levelset prestige add
Add a role to a prestige level<br/>
 - Usage: `<@1275521742961508432>levelset prestige add <prestige> <role> <emoji>`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### prestige: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>levelset prestige stack
Toggle stacking roles on prestige<br/>

For example each time you prestige, you keep the previous prestige roles<br/>
 - Usage: `<@1275521742961508432>levelset prestige stack`


## <@1275521742961508432>levelset messages
Message settings<br/>
 - Usage: `<@1275521742961508432>levelset messages`
 - Aliases: `message and msg`


### <@1275521742961508432>levelset messages cooldown
Cooldown threshold for message XP<br/>

When a user sends a message they will have to wait X seconds before their message<br/>
counts as XP gained<br/>
 - Usage: `<@1275521742961508432>levelset messages cooldown <cooldown>`
Extended Arg Info
> ### cooldown: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset messages channelbonus
Add a range of bonus XP to apply to certain channels<br/>

This bonus applies to message xp<br/>

Set both min and max to 0 to remove the role bonus<br/>
 - Usage: `<@1275521742961508432>levelset messages channelbonus <channel> <min_xp> <max_xp>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.CategoryChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### min_xp: int
> ```
> A number without decimal places.
> ```
> ### max_xp: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset messages xp
Set message XP range<br/>

Set the Min and Max amount of XP that a message can gain<br/>
Default is 3 min and 6 max<br/>
 - Usage: `<@1275521742961508432>levelset messages xp <min_xp> <max_xp>`
Extended Arg Info
> ### min_xp: int
> ```
> A number without decimal places.
> ```
> ### max_xp: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset messages rolebonus
Add a range of bonus XP to apply to certain roles<br/>

This bonus applies to message xp<br/>

Set both min and max to 0 to remove the role bonus<br/>
 - Usage: `<@1275521742961508432>levelset messages rolebonus <role> <min_xp> <max_xp>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### min_xp: int
> ```
> A number without decimal places.
> ```
> ### max_xp: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>levelset messages length
Set minimum message length for XP<br/>
Minimum length a message must be to count towards XP gained<br/>

Set to 0 to disable<br/>
 - Usage: `<@1275521742961508432>levelset messages length <length>`
Extended Arg Info
> ### length: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelset embeds
Toggle using embeds or generated pics<br/>
 - Usage: `<@1275521742961508432>levelset embeds`


## <@1275521742961508432>levelset rolegroup
Add or remove a role to the role group<br/>

These roles gain their own experience points as a group<br/>
When a member gains xp while having this role, the xp they earn is also added to the role group<br/>
 - Usage: `<@1275521742961508432>levelset rolegroup <role>`
Extended Arg Info
> ### role: Union[discord.role.Role, int]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>levelset commandxp
Toggle whether users can gain Exp from running commands<br/>
 - Usage: `<@1275521742961508432>levelset commandxp`


## <@1275521742961508432>levelset starcooldown
Set the star cooldown<br/>

Users can give another user a star every X seconds<br/>
 - Usage: `<@1275521742961508432>levelset starcooldown <seconds>`
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>levelset view
View all LevelUP settings<br/>
 - Usage: `<@1275521742961508432>levelset view`


## <@1275521742961508432>levelset seelevels
Test the level algorithm<br/>
View the first 20 levels using the current algorithm to test experience curve<br/>
 - Usage: `<@1275521742961508432>levelset seelevels`


