TrickOrTreat
============

Trick or treating for your server.

# <@1275521742961508432>eatcandy
Eat some candy.<br/>

Valid types: candy/candie(s), chocolate(s), lollipop(s), cookie(s), star(s)<br/>
Examples:<br/>
    `<@1275521742961508432>eatcandy 3 lollipops`<br/>
    `<@1275521742961508432>eatcandy star`<br/>

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
 - Usage: `<@1275521742961508432>eatcandy [number=1] [candy_type=None]`
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


# <@1275521742961508432>totbalance
[Admin] Check how many candies are 'on the ground' in the server.<br/>
 - Usage: `<@1275521742961508432>totbalance`
 - Restricted to: `MOD`
 - Checks: `server_only`


# <@1275521742961508432>buycandy
Buy some candy. Prices could vary at any time.<br/>
 - Usage: `<@1275521742961508432>buycandy <pieces>`
 - Checks: `server_only`
Extended Arg Info
> ### pieces: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>cboard
Show the candy eating leaderboard.<br/>
 - Usage: `<@1275521742961508432>cboard`
 - Checks: `server_only`


# <@1275521742961508432>cinventory
Check your inventory.<br/>
 - Usage: `<@1275521742961508432>cinventory`
 - Checks: `server_only`


# <@1275521742961508432>totclearall
[Owner] Clear all saved game data.<br/>
 - Usage: `<@1275521742961508432>totclearall [are_you_sure=False]`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### are_you_sure=False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>totcooldown
Set the cooldown time for trick or treating on the server.<br/>
 - Usage: `<@1275521742961508432>totcooldown [cooldown_time=0]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### cooldown_time: int = 0
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>pickup
Pick up some candy, if there is any.<br/>
 - Usage: `<@1275521742961508432>pickup`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `server_only`


# <@1275521742961508432>stealcandy
Steal some candy.<br/>
 - Usage: `<@1275521742961508432>stealcandy [user=None]`
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


# <@1275521742961508432>totchannel
Channel management for Trick or Treat.<br/>
 - Usage: `<@1275521742961508432>totchannel`
 - Restricted to: `MOD`
 - Checks: `server_only`


## <@1275521742961508432>totchannel add
Add a text channel for Trick or Treating.<br/>
 - Usage: `<@1275521742961508432>totchannel add <channel>`
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


## <@1275521742961508432>totchannel remove
Remove a text channel from Trick or Treating.<br/>
 - Usage: `<@1275521742961508432>totchannel remove <channel>`
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


# <@1275521742961508432>tottoggle
Toggle trick or treating on the whole server.<br/>
 - Usage: `<@1275521742961508432>tottoggle`
 - Restricted to: `MOD`
 - Checks: `server_only`


# <@1275521742961508432>totversion
Trick or Treat version.<br/>
 - Usage: `<@1275521742961508432>totversion`
 - Checks: `server_only`


