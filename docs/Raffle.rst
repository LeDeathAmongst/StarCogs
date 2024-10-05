Raffle
======

Run simple Raffles for your server.

# <@1275521742961508432>raffle
Raffle group command<br/>
 - Usage: `<@1275521742961508432>raffle`
 - Checks: `server_only`


## <@1275521742961508432>raffle end
Ends a raffle early. A winner will still be chosen.<br/>
 - Usage: `<@1275521742961508432>raffle end [message_id=None]`
Extended Arg Info
> ### message_id: int = None
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>raffle start
Starts a raffle.<br/>

Timer accepts a integer input that represents seconds or it will<br/>
take the format of HH:MM:SS.<br/>

Example timer inputs:<br/>
`80`       = 1 minute and 20 seconds or 80 seconds<br/>
`30:10`    = 30 minutes and 10 seconds<br/>
`24:00:00` = 1 day or 24 hours<br/>

Title should not be longer than 35 characters.<br/>
 - Usage: `<@1275521742961508432>raffle start <timer> <title>`
Extended Arg Info
> ### timer
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>raffle version
Displays the currently installed version of raffle.<br/>
 - Usage: `<@1275521742961508432>raffle version`


## <@1275521742961508432>raffle cancel
Cancels an on-going raffle. No winner is chosen.<br/>
 - Usage: `<@1275521742961508432>raffle cancel [message_id=None]`
Extended Arg Info
> ### message_id: int = None
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>raffle reroll
Reroll the winner for a raffle. Requires the channel and message id.<br/>
 - Usage: `<@1275521742961508432>raffle reroll <channel> <messageid>`
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
> ### messageid: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>raffle clear

 - Usage: `<@1275521742961508432>raffle clear`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>setraffle
Set Raffle group command<br/>
 - Usage: `<@1275521742961508432>setraffle`
 - Checks: `server_only`


## <@1275521742961508432>setraffle channel
Set the output channel for raffles.<br/>
 - Usage: `<@1275521742961508432>setraffle channel [channel=None]`
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


