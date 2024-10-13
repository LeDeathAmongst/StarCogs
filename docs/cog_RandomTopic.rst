RandomTopic
===========

A cog to send random topics at configurable intervals.

<<<<<<< HEAD
# <@1275521742961508432>rt
Commands to configure Random Topic.<br/>
 - Usage: `<@1275521742961508432>rt`
=======
# ,rt
Commands to configure Random Topic.<br/>
 - Usage: `,rt`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>rt setinterval
Set the interval for sending random topics (in minutes).<br/>

Use this command to set the interval at which the bot will send random topics.<br/>
 - Usage: `<@1275521742961508432>rt setinterval <interval>`
Extended Arg Info
> ### interval: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>rt setchannel
Set the channel where random topics will be sent.<br/>

Use this command to specify which text channel the bot should use to send the random topics. Make sure to mention the channel.<br/>
 - Usage: `<@1275521742961508432>rt setchannel <channel>`
=======
## ,rt setchannel
Set the channel where random topics will be sent.<br/>

Use this command to specify which text channel the bot should use to send the random topics. Make sure to mention the channel.<br/>
 - Usage: `,rt setchannel <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>rt setrole
Set the role to be pinged when a new topic is posted.<br/>

Use this command to specify which role should be mentioned whenever a new random topic is generated and sent to the channel.<br/>
 - Usage: `<@1275521742961508432>rt setrole <role>`
=======
## ,rt setinterval
Set the interval for sending random topics (in minutes).<br/>

Use this command to set the interval at which the bot will send random topics.<br/>
 - Usage: `,rt setinterval <interval>`
Extended Arg Info
> ### interval: int
> ```
> A number without decimal places.
> ```


## ,rt setrole
Set the role to be pinged when a new topic is posted.<br/>

Use this command to specify which role should be mentioned whenever a new random topic is generated and sent to the channel.<br/>
 - Usage: `,rt setrole <role>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>rt settitle
Set the title for the Random Topic embed.<br/>

Use this command to customize the title that will appear in the random topic embeds.<br/>
 - Usage: `<@1275521742961508432>rt settitle <title>`
=======
## ,rt settitle
Set the title for the Random Topic embed.<br/>

Use this command to customize the title that will appear in the random topic embeds.<br/>
 - Usage: `,rt settitle <title>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


