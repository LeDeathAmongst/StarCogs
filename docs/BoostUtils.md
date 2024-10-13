Nitro Boost Utilities.

# ,boostmessage
Configuration commands for boost messages.<br/>
 - Usage: `,boostmessage`
 - Aliases: `boostmsg and bmsg`
 - Checks: `server_only`
## ,boostmessage settings
See the boost messages settings configured for your server.<br/>
 - Usage: `,boostmessage settings`
 - Aliases: `show, showsettings, and ss`
## ,boostmessage toggle
Enable or disable boost messages.<br/>

- Running the command with no arguments will disable the boost messages.<br/>
 - Usage: `,boostmessage toggle [true_or_false=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### true_or_false: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,boostmessage message
Configure boost and unboost messages.<br/>
 - Usage: `,boostmessage message`
 - Restricted to: `ADMIN`
### ,boostmessage message unboosted
Configure the unboost message.<br/>

- Running the command with no arguments will reset the unboost message.<br/>
 - Usage: `,boostmessage message unboosted [message]`
 - Aliases: `unboost`
### ,boostmessage message boosted
Configure the boost message.<br/>

- Running the command with no arguments will reset the boost message.<br/>
 - Usage: `,boostmessage message boosted [message]`
 - Aliases: `boost`
## ,boostmessage channels
Add or remove the channels for boost messages.<br/>
 - Usage: `,boostmessage channels <add_or_remove> <channels>`
 - Restricted to: `ADMIN`
