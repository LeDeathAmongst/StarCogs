NoSpoiler
=========

No spoiler in this server.

# <@1275521742961508432>nospoiler
Manage the spoiler filter settings.<br/>
 - Usage: `<@1275521742961508432>nospoiler`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## <@1275521742961508432>nospoiler useembed
Toggle the spoiler warning message to use embed or not.<br/>
 - Usage: `<@1275521742961508432>nospoiler useembed [toggle=None]`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>nospoiler togglewarnmsg
Toggle the spoiler warning message on or off.<br/>
 - Usage: `<@1275521742961508432>nospoiler togglewarnmsg [toggle=None]`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>nospoiler message
Set the spoiler warning message.<br/>

If the message is not set, the bot will use the default message.<br/>
 - Usage: `<@1275521742961508432>nospoiler message [message]`
Extended Arg Info
> ### message: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>nospoiler version
Shows the version of the cog.<br/>
 - Usage: `<@1275521742961508432>nospoiler version`


## <@1275521742961508432>nospoiler settings
Show the settings.<br/>
 - Usage: `<@1275521742961508432>nospoiler settings`
 - Aliases: `view and views`


## <@1275521742961508432>nospoiler toggle
Toggle NoSpoiler filter on/off.<br/>
 - Usage: `<@1275521742961508432>nospoiler toggle`


## <@1275521742961508432>nospoiler logchannel
Set the channel where the bot will log the deleted spoiler messages.<br/>

If the channel is not set, the bot will not log the deleted spoiler messages.<br/>
 - Usage: `<@1275521742961508432>nospoiler logchannel [channel=None]`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>nospoiler deleteafter
Set when the warn message should delete.<br/>

Default timeout is 10 seconds.<br/>
Timeout must be between 10 and 120 seconds.<br/>
 - Usage: `<@1275521742961508432>nospoiler deleteafter <seconds>`


