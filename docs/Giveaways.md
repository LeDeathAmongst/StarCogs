Giveaway Commands

# <@1275521742961508432>giveaway (Hybrid Command)
Manage the giveaway system<br/>
 - Usage: `<@1275521742961508432>giveaway`
 - Slash Usage: `/giveaway`
 - Aliases: `gw`
## <@1275521742961508432>giveaway list (Hybrid Command)
List all giveaways in the server.<br/>
 - Usage: `<@1275521742961508432>giveaway list`
 - Slash Usage: `/giveaway list`
## <@1275521742961508432>giveaway end (Hybrid Command)
End a giveaway.<br/>
 - Usage: `<@1275521742961508432>giveaway end <msgid>`
 - Slash Usage: `/giveaway end <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>giveaway advanced (Hybrid Command)
Advanced creation of Giveaways.<br/>


`<@1275521742961508432>gw explain` for a further full listing of the arguments.<br/>
 - Usage: `<@1275521742961508432>giveaway advanced <arguments>`
 - Slash Usage: `/giveaway advanced <arguments>`
 - Aliases: `adv`
## <@1275521742961508432>giveaway info (Hybrid Command)
Information about a giveaway.<br/>
 - Usage: `<@1275521742961508432>giveaway info <msgid>`
 - Slash Usage: `/giveaway info <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>giveaway integrations (Hybrid Command)
Various 3rd party integrations for giveaways.<br/>
 - Usage: `<@1275521742961508432>giveaway integrations`
 - Slash Usage: `/giveaway integrations`
## <@1275521742961508432>giveaway start (Hybrid Command)
Start a giveaway.<br/>

This by default will DM the winner and also DM a user if they cannot enter the giveaway.<br/>
 - Usage: `<@1275521742961508432>giveaway start <channel> <time> <prize>`
 - Slash Usage: `/giveaway start <channel> <time> <prize>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### prize: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>giveaway reroll (Hybrid Command)
Reroll a giveaway.<br/>
 - Usage: `<@1275521742961508432>giveaway reroll <msgid>`
 - Slash Usage: `/giveaway reroll <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>giveaway explain (Hybrid Command)
Explanation of giveaway advanced and the arguements it supports.<br/>
 - Usage: `<@1275521742961508432>giveaway explain`
 - Slash Usage: `/giveaway explain`
## <@1275521742961508432>giveaway edit (Hybrid Command)
Edit a giveaway.<br/>

See `<@1275521742961508432>gw explain` for more info on the flags.<br/>
 - Usage: `<@1275521742961508432>giveaway edit <msgid> <flags>`
 - Slash Usage: `/giveaway edit <msgid> <flags>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>giveaway entrants (Hybrid Command)
List all entrants for a giveaway.<br/>
 - Usage: `<@1275521742961508432>giveaway entrants <msgid>`
 - Slash Usage: `/giveaway entrants <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```
