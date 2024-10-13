Chatchart
=========

Show activity.

<<<<<<< HEAD
# <@1275521742961508432>chatchart
Generates a pie chart, representing the last 5000 messages in the specified channel.<br/>
 - Usage: `<@1275521742961508432>chatchart [channel=None] [messages=5000]`
=======
# ,chatchart
Generates a pie chart, representing the last 5000 messages in the specified channel.<br/>
 - Usage: `,chatchart [channel=None] [messages=5000]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>serverchart
=======
# ,serverchart
>>>>>>> 9e308722 (Revamped and Fixed)
Generates a pie chart, representing the last 1000 messages from every allowed channel in the server.<br/>

As example:<br/>
For each channel that the bot is allowed to scan. It will take the last 1000 messages from each channel.<br/>
And proceed to build a chart out of that.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>serverchart [messages=1000]`
=======
 - Usage: `,serverchart [messages=1000]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `serverchart`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### messages: int = 1000
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>ccdeny
Add a channel to deny chatchart use.<br/>
 - Usage: `<@1275521742961508432>ccdeny <channel>`
=======
# ,ccdeny
Add a channel to deny chatchart use.<br/>
 - Usage: `,ccdeny <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>ccdenylist
List the channels that are denied.<br/>
 - Usage: `<@1275521742961508432>ccdenylist`
=======
# ,ccdenylist
List the channels that are denied.<br/>
 - Usage: `,ccdenylist`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>ccallow
Remove a channel from the deny list to allow chatchart use.<br/>
 - Usage: `<@1275521742961508432>ccallow <channel>`
=======
# ,ccallow
Remove a channel from the deny list to allow chatchart use.<br/>
 - Usage: `,ccallow <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>cclimit
Limit the amount of messages someone can request.<br/>

Use `0` for no limit.<br/>
 - Usage: `<@1275521742961508432>cclimit [limit_amount=None]`
=======
# ,cclimit
Limit the amount of messages someone can request.<br/>

Use `0` for no limit.<br/>
 - Usage: `,cclimit [limit_amount=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### limit_amount: int = None
> ```
> A number without decimal places.
> ```


