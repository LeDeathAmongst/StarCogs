PyLavNotifier
=============

Listen to events from the PyLav player and send them as messages to the specified channel

# <@1275521742961508432>plnotifier
Configure the PyLavNotifier cog<br/>
 - Usage: `<@1275521742961508432>plnotifier`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


## <@1275521742961508432>plnotifier version
Show the version of the Cog and PyLav<br/>
 - Usage: `<@1275521742961508432>plnotifier version`


## <@1275521742961508432>plnotifier event
Set whether or not to notify for the specified event.<br/>

Arguments:<br/>
    event -- The event to set.<br/>
    toggle -- Whether or not to notify upon receiving this event.<br/>
    use_mention -- Whether or not to use a mention instead of the name for the action requested.<br/>
 - Usage: `<@1275521742961508432>plnotifier event <event> <toggle> [use_mention=False]`
Extended Arg Info
> ### event: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### use_mention: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>plnotifier webhook
Set the notify channel for the player<br/>
 - Usage: `<@1275521742961508432>plnotifier webhook <channel> [use_thread=True]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### use_thread: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```


