Hunting, it hunts birds and things that fly.

# ,hunting
Hunting, it hunts birds and things that fly.<br/>
 - Usage: `,hunting`
 - Checks: `server_only`
## ,hunting stop
Stop the hunt.<br/>
 - Usage: `,hunting stop [channel=operator.attrgetter('channel')]`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: discord.channel.TextChannel = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,hunting bangtime
Toggle displaying the bang response time from users.<br/>
 - Usage: `,hunting bangtime`
 - Restricted to: `MOD`
## ,hunting eagle
Toggle whether shooting an eagle is bad.<br/>
 - Usage: `,hunting eagle`
 - Restricted to: `MOD`
## ,hunting reward
Set a credit reward range for successfully shooting a bird<br/>

Leave the options blank to disable bang rewards<br/>
 - Usage: `,hunting reward [min_reward=None] [max_reward=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### min_reward: int = None
> ```
> A number without decimal places.
> ```
> ### max_reward: int = None
> ```
> A number without decimal places.
> ```
## ,hunting version
Show the cog version.<br/>
 - Usage: `,hunting version`
## ,hunting mode
Toggle whether the bot listens for 'bang' or a reaction.<br/>
 - Usage: `,hunting mode`
 - Restricted to: `MOD`
## ,hunting start
Start the hunt.<br/>
 - Usage: `,hunting start [channel=operator.attrgetter('channel')]`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: discord.channel.TextChannel = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,hunting clearleaderboard
Clear all the scores from the leaderboard.<br/>
 - Usage: `,hunting clearleaderboard`
 - Restricted to: `BOT_OWNER`
## ,hunting score
This will show the score of a hunter.<br/>
 - Usage: `,hunting score [member=None]`
Extended Arg Info
> ### member: discord.member.Member = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
## ,hunting next
When will the next occurrence happen?<br/>
 - Usage: `,hunting next`
 - Restricted to: `MOD`
## ,hunting leaderboard
This will show the top 50 hunters for the server.<br/>
Use True for the global_leaderboard variable to show the global leaderboard.<br/>
 - Usage: `,hunting leaderboard [global_leaderboard=False]`
Extended Arg Info
> ### global_leaderboard=False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,hunting timing
Change the hunting timing.<br/>

`interval_min` = Minimum time in seconds for a new bird. (60 min)<br/>
`interval_max` = Maximum time in seconds for a new bird. (120 min)<br/>
`bang_timeout` = Time in seconds for users to shoot a bird before it flies away. (10s min)<br/>
 - Usage: `,hunting timing <interval_min> <interval_max> <bang_timeout>`
 - Restricted to: `MOD`
Extended Arg Info
> ### interval_min: int
> ```
> A number without decimal places.
> ```
> ### interval_max: int
> ```
> A number without decimal places.
> ```
> ### bang_timeout: int
> ```
> A number without decimal places.
> ```
