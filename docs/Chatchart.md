Show activity.

# <@1275521742961508432>chatchart
Generates a pie chart, representing the last 5000 messages in the specified channel.<br/>
 - Usage: `<@1275521742961508432>chatchart [channel=None] [messages=5000]`
 - Cooldown: `1 per 10.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### messages: int = 5000
> ```
> A number without decimal places.
> ```
# <@1275521742961508432>serverchart
Generates a pie chart, representing the last 1000 messages from every allowed channel in the server.<br/>

As example:<br/>
For each channel that the bot is allowed to scan. It will take the last 1000 messages from each channel.<br/>
And proceed to build a chart out of that.<br/>
 - Usage: `<@1275521742961508432>serverchart [messages=1000]`
 - Restricted to: `MOD`
 - Aliases: `serverchart`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### messages: int = 1000
> ```
> A number without decimal places.
> ```
# <@1275521742961508432>ccdeny
Add a channel to deny chatchart use.<br/>
 - Usage: `<@1275521742961508432>ccdeny <channel>`
 - Restricted to: `MOD`
 - Checks: `server_only`
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
# <@1275521742961508432>ccdenylist
List the channels that are denied.<br/>
 - Usage: `<@1275521742961508432>ccdenylist`
 - Restricted to: `MOD`
 - Checks: `server_only`
# <@1275521742961508432>ccallow
Remove a channel from the deny list to allow chatchart use.<br/>
 - Usage: `<@1275521742961508432>ccallow <channel>`
 - Restricted to: `MOD`
 - Checks: `server_only`
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
# <@1275521742961508432>cclimit
Limit the amount of messages someone can request.<br/>

Use `0` for no limit.<br/>
 - Usage: `<@1275521742961508432>cclimit [limit_amount=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### limit_amount: int = None
> ```
> A number without decimal places.
> ```
