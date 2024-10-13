CycleStatus
===========

Automatically change the status of your bot every minute

<<<<<<< HEAD
# <@1275521742961508432>cyclestatusversion
Get the version of Cycle Status that Starfire is running<br/>
 - Usage: `<@1275521742961508432>cyclestatusversion`
 - Aliases: `csversion`


# <@1275521742961508432>cyclestatus
Commands working with the status<br/>
 - Usage: `<@1275521742961508432>cyclestatus`
=======
# ,cyclestatusversion
Get the version of Cycle Status that Starfire is running<br/>
 - Usage: `,cyclestatusversion`
 - Aliases: `csversion`


# ,cyclestatus
Commands working with the status<br/>
 - Usage: `,cyclestatus`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `cstatus`


<<<<<<< HEAD
## <@1275521742961508432>cyclestatus mode
Change Starfire's status mode<br/>

**Arguments**<br/>
    - `mode` The mode type. Valid types are:<br/>
    `online, idle, dnd, and do not disturb`<br/>
 - Usage: `<@1275521742961508432>cyclestatus mode <mode>`


## <@1275521742961508432>cyclestatus usehelp
Change whether the status should have ` | <@1275521742961508432>help`<br/>

**Arguments**<br/>
    - `toggle` Whether help should be used or not.<br/>
 - Usage: `<@1275521742961508432>cyclestatus usehelp [toggle=None]`
Extended Arg Info
> ### toggle: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>cyclestatus clear
Clear all of the statuses<br/>
 - Usage: `<@1275521742961508432>cyclestatus clear`


## <@1275521742961508432>cyclestatus forcenext
Force the next status to display on the bot<br/>
 - Usage: `<@1275521742961508432>cyclestatus forcenext`
 - Checks: `CycleStatus`


## <@1275521742961508432>cyclestatus add
=======
## ,cyclestatus clear
Clear all of the statuses<br/>
 - Usage: `,cyclestatus clear`


## ,cyclestatus add
>>>>>>> 9e308722 (Revamped and Fixed)
Add a status to the list<br/>

Put `{bot_server_count}` or `{bot_member_count}` in your message to have the user count and server count of your bot!<br/>
You can also put `{bot_prefix}` in your message to have the bot's prefix be displayed (eg. `{bot_prefix}ping`)<br/>

**Arguments**<br/>
    - `status` The status to add to the cycle.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>cyclestatus add <status>`
=======
 - Usage: `,cyclestatus add <status>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### status: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>cyclestatus random
Have the bot cycle to a random status<br/>

**Arguments**<br/>
    - `value` Whether to have random statuses be enabled or not<br/>
 - Usage: `<@1275521742961508432>cyclestatus random <value>`
Extended Arg Info
> ### value: bool
=======
## ,cyclestatus forcenext
Force the next status to display on the bot<br/>
 - Usage: `,cyclestatus forcenext`
 - Checks: `CycleStatus`


## ,cyclestatus usehelp
Change whether the status should have ` | ,help`<br/>

**Arguments**<br/>
    - `toggle` Whether help should be used or not.<br/>
 - Usage: `,cyclestatus usehelp [toggle=None]`
Extended Arg Info
> ### toggle: Optional[bool] = None
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>cyclestatus remove
=======
## ,cyclestatus remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove a status from the list<br/>

**Arguments**<br/>
    - `num` The index of the status you want to remove.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>cyclestatus remove [num=None]`
 - Aliases: `del, rm, and delete`


## <@1275521742961508432>cyclestatus toggle
=======
 - Usage: `,cyclestatus remove [num=None]`
 - Aliases: `del, rm, and delete`


## ,cyclestatus toggle
>>>>>>> 9e308722 (Revamped and Fixed)
Toggle whether the status should be cycled.<br/>

This is handy for if you want to keep your statuses but don't want them displayed at the moment<br/>

**Arguments**<br/>
    - `value` Whether to toggle cycling statues<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>cyclestatus toggle <value>`
=======
 - Usage: `,cyclestatus toggle <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### value: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>cyclestatus type
=======
## ,cyclestatus list
List the available statuses<br/>
 - Usage: `,cyclestatus list`


## ,cyclestatus settings
Show your current settings for the cycle status cog<br/>
 - Usage: `,cyclestatus settings`


## ,cyclestatus type
>>>>>>> 9e308722 (Revamped and Fixed)
Change the type of Starfire's status<br/>

**Arguments**<br/>
    - `status` The status type. Valid types are<br/>
    `playing, listening, watching, custom, and competing`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>cyclestatus type <status>`


## <@1275521742961508432>cyclestatus list
List the available statuses<br/>
 - Usage: `<@1275521742961508432>cyclestatus list`


## <@1275521742961508432>cyclestatus settings
Show your current settings for the cycle status cog<br/>
 - Usage: `<@1275521742961508432>cyclestatus settings`
=======
 - Usage: `,cyclestatus type <status>`


## ,cyclestatus random
Have the bot cycle to a random status<br/>

**Arguments**<br/>
    - `value` Whether to have random statuses be enabled or not<br/>
 - Usage: `,cyclestatus random <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,cyclestatus mode
Change Starfire's status mode<br/>

**Arguments**<br/>
    - `mode` The mode type. Valid types are:<br/>
    `online, idle, dnd, and do not disturb`<br/>
 - Usage: `,cyclestatus mode <mode>`
>>>>>>> 9e308722 (Revamped and Fixed)


