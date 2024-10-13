Trick or treating for your server.

# ,eatcandy
Eat some candy.<br/>

Valid types: candy/candie(s), chocolate(s), lollipop(s), cookie(s), star(s)<br/>
Examples:<br/>
    `,eatcandy 3 lollipops`<br/>
    `,eatcandy star`<br/>

🍬<br/>
The star of this competition. You should try to eat all of these, but don't get too sick.<br/>

🍫<br/>
Reduces sickness by 10.<br/>

🍭<br/>
Reduces sickness by 20.<br/>

🥠<br/>
Sets sickness to a random amount - fortune favours the brave.<br/>

⭐<br/>
Resets sickness to 0.<br/>
 - Usage: `,eatcandy [number=1] [candy_type=None]`
 - Cooldown: `1 per 1.0 second`
 - Checks: `server_only`
Extended Arg Info
> ### number: Optional[int] = 1
> ```
> A number without decimal places.
> ```
> ### candy_type=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,totbalance
[Admin] Check how many candies are 'on the ground' in the server.<br/>
 - Usage: `,totbalance`
 - Restricted to: `MOD`
 - Checks: `server_only`
# ,buycandy
Buy some candy. Prices could vary at any time.<br/>
 - Usage: `,buycandy <pieces>`
 - Checks: `server_only`
Extended Arg Info
> ### pieces: int
> ```
> A number without decimal places.
> ```
# ,cboard
Show the candy eating leaderboard.<br/>
 - Usage: `,cboard`
 - Checks: `server_only`
# ,cinventory
Check your inventory.<br/>
 - Usage: `,cinventory`
 - Checks: `server_only`
# ,totclearall
[Owner] Clear all saved game data.<br/>
 - Usage: `,totclearall [are_you_sure=False]`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### are_you_sure=False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,totcooldown
Set the cooldown time for trick or treating on the server.<br/>
 - Usage: `,totcooldown [cooldown_time=0]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### cooldown_time: int = 0
> ```
> A number without decimal places.
> ```
# ,pickup
Pick up some candy, if there is any.<br/>
 - Usage: `,pickup`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `server_only`
# ,stealcandy
Steal some candy.<br/>
 - Usage: `,stealcandy [user=None]`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member = None
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
# ,totchannel
Channel management for Trick or Treat.<br/>
 - Usage: `,totchannel`
 - Restricted to: `MOD`
 - Checks: `server_only`
## ,totchannel add
Add a text channel for Trick or Treating.<br/>
 - Usage: `,totchannel add <channel>`
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
## ,totchannel remove
Remove a text channel from Trick or Treating.<br/>
 - Usage: `,totchannel remove <channel>`
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
# ,tottoggle
Toggle trick or treating on the whole server.<br/>
 - Usage: `,tottoggle`
 - Restricted to: `MOD`
 - Checks: `server_only`
# ,totversion
Trick or Treat version.<br/>
 - Usage: `,totversion`
 - Checks: `server_only`
