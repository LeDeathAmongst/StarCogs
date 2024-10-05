Set a channel to listens and control the music player.

# <@1275521742961508432>plcontrollerset
Configure the PyLav Controller.<br/>
 - Usage: `<@1275521742961508432>plcontrollerset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## <@1275521742961508432>plcontrollerset greedy
Toggles whether I should listen to any message I see or only messages starting without a command prefix.<br/>
 - Usage: `<@1275521742961508432>plcontrollerset greedy`
 - Restricted to: `BOT_OWNER`
 - Aliases: `g`
## <@1275521742961508432>plcontrollerset channel
Set the channel to create the controller in.<br/>
 - Usage: `<@1275521742961508432>plcontrollerset channel <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.VoiceChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## <@1275521742961508432>plcontrollerset slowmode
Toggle whether the controller should use slowmode.<br/>
 - Usage: `<@1275521742961508432>plcontrollerset slowmode`
 - Aliases: `sm`
## <@1275521742961508432>plcontrollerset acceptrequests
Toggle whether the controller should listen for requests.<br/>
 - Usage: `<@1275521742961508432>plcontrollerset acceptrequests`
 - Aliases: `ar and listen`
## <@1275521742961508432>plcontrollerset antispam
Toggle whether the controller enable the antispam check.<br/>
 - Usage: `<@1275521742961508432>plcontrollerset antispam`
 - Aliases: `spam`
## <@1275521742961508432>plcontrollerset acceptsearches
Toggle whether the controller should listen for searches.<br/>
 - Usage: `<@1275521742961508432>plcontrollerset acceptsearches`
 - Aliases: `as and search`
