PyLavController
===============

Set a channel to listens and control the music player.

# ,plcontrollerset
Configure the PyLav Controller.<br/>
 - Usage: `,plcontrollerset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,plcontrollerset greedy
Toggles whether I should listen to any message I see or only messages starting without a command prefix.<br/>
 - Usage: `,plcontrollerset greedy`
 - Restricted to: `BOT_OWNER`
 - Aliases: `g`


## ,plcontrollerset antispam
Toggle whether the controller enable the antispam check.<br/>
 - Usage: `,plcontrollerset antispam`
 - Aliases: `spam`


## ,plcontrollerset acceptrequests
Toggle whether the controller should listen for requests.<br/>
 - Usage: `,plcontrollerset acceptrequests`
 - Aliases: `ar and listen`


## ,plcontrollerset acceptsearches
Toggle whether the controller should listen for searches.<br/>
 - Usage: `,plcontrollerset acceptsearches`
 - Aliases: `as and search`


## ,plcontrollerset slowmode
Toggle whether the controller should use slowmode.<br/>
 - Usage: `,plcontrollerset slowmode`
 - Aliases: `sm`


## ,plcontrollerset channel
Set the channel to create the controller in.<br/>
 - Usage: `,plcontrollerset channel <channel>`
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


