Automatically change the status of your bot every minute

# ,cyclestatusversion
Get the version of Cycle Status that Starfire is running<br/>
 - Usage: `,cyclestatusversion`
 - Aliases: `csversion`
# ,cyclestatus
Commands working with the status<br/>
 - Usage: `,cyclestatus`
 - Restricted to: `BOT_OWNER`
 - Aliases: `cstatus`
## ,cyclestatus clear
Clear all of the statuses<br/>
 - Usage: `,cyclestatus clear`
## ,cyclestatus add
Add a status to the list<br/>

Put `{bot_server_count}` or `{bot_member_count}` in your message to have the user count and server count of your bot!<br/>
You can also put `{bot_prefix}` in your message to have the bot's prefix be displayed (eg. `{bot_prefix}ping`)<br/>

**Arguments**<br/>
    - `status` The status to add to the cycle.<br/>
 - Usage: `,cyclestatus add <status>`
Extended Arg Info
> ### status: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
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
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,cyclestatus remove
Remove a status from the list<br/>

**Arguments**<br/>
    - `num` The index of the status you want to remove.<br/>
 - Usage: `,cyclestatus remove [num=None]`
 - Aliases: `del, rm, and delete`
## ,cyclestatus toggle
Toggle whether the status should be cycled.<br/>

This is handy for if you want to keep your statuses but don't want them displayed at the moment<br/>

**Arguments**<br/>
    - `value` Whether to toggle cycling statues<br/>
 - Usage: `,cyclestatus toggle <value>`
Extended Arg Info
> ### value: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,cyclestatus list
List the available statuses<br/>
 - Usage: `,cyclestatus list`
## ,cyclestatus settings
Show your current settings for the cycle status cog<br/>
 - Usage: `,cyclestatus settings`
## ,cyclestatus type
Change the type of Starfire's status<br/>

**Arguments**<br/>
    - `status` The status type. Valid types are<br/>
    `playing, listening, watching, custom, and competing`<br/>
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
