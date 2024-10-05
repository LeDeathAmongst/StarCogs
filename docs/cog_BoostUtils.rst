BoostUtils
==========

Nitro Boost Utilities.

# <@1275521742961508432>boostmessage
Configuration commands for boost messages.<br/>
 - Usage: `<@1275521742961508432>boostmessage`
 - Aliases: `boostmsg and bmsg`
 - Checks: `server_only`


## <@1275521742961508432>boostmessage message
Configure boost and unboost messages.<br/>
 - Usage: `<@1275521742961508432>boostmessage message`
 - Restricted to: `ADMIN`


### <@1275521742961508432>boostmessage message boosted
Configure the boost message.<br/>

- Running the command with no arguments will reset the boost message.<br/>
 - Usage: `<@1275521742961508432>boostmessage message boosted [message]`
 - Aliases: `boost`


### <@1275521742961508432>boostmessage message unboosted
Configure the unboost message.<br/>

- Running the command with no arguments will reset the unboost message.<br/>
 - Usage: `<@1275521742961508432>boostmessage message unboosted [message]`
 - Aliases: `unboost`


## <@1275521742961508432>boostmessage settings
See the boost messages settings configured for your server.<br/>
 - Usage: `<@1275521742961508432>boostmessage settings`
 - Aliases: `show, showsettings, and ss`


## <@1275521742961508432>boostmessage toggle
Enable or disable boost messages.<br/>

- Running the command with no arguments will disable the boost messages.<br/>
 - Usage: `<@1275521742961508432>boostmessage toggle [true_or_false=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### true_or_false: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>boostmessage channels
Add or remove the channels for boost messages.<br/>
 - Usage: `<@1275521742961508432>boostmessage channels <add_or_remove> <channels>`
 - Restricted to: `ADMIN`


