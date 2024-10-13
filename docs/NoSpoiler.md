No spoiler in this server.

# ,nospoiler
Manage the spoiler filter settings.<br/>
 - Usage: `,nospoiler`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## ,nospoiler toggle
Toggle NoSpoiler filter on/off.<br/>
 - Usage: `,nospoiler toggle`
## ,nospoiler deleteafter
Set when the warn message should delete.<br/>

Default timeout is 10 seconds.<br/>
Timeout must be between 10 and 120 seconds.<br/>
 - Usage: `,nospoiler deleteafter <seconds>`
## ,nospoiler version
Shows the version of the cog.<br/>
 - Usage: `,nospoiler version`
## ,nospoiler settings
Show the settings.<br/>
 - Usage: `,nospoiler settings`
 - Aliases: `view and views`
## ,nospoiler logchannel
Set the channel where the bot will log the deleted spoiler messages.<br/>

If the channel is not set, the bot will not log the deleted spoiler messages.<br/>
 - Usage: `,nospoiler logchannel [channel=None]`
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
## ,nospoiler message
Set the spoiler warning message.<br/>

If the message is not set, the bot will use the default message.<br/>
 - Usage: `,nospoiler message [message]`
Extended Arg Info
> ### message: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,nospoiler togglewarnmsg
Toggle the spoiler warning message on or off.<br/>
 - Usage: `,nospoiler togglewarnmsg [toggle=None]`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,nospoiler useembed
Toggle the spoiler warning message to use embed or not.<br/>
 - Usage: `,nospoiler useembed [toggle=None]`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
