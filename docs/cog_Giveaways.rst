Giveaways
=========

Giveaway Commands

# ,giveaway (Hybrid Command)
Manage the giveaway system<br/>
 - Usage: `,giveaway`
 - Slash Usage: `/giveaway`
 - Aliases: `gw`


## ,giveaway edit (Hybrid Command)
Edit a giveaway.<br/>

See `,gw explain` for more info on the flags.<br/>
 - Usage: `,giveaway edit <msgid> <flags>`
 - Slash Usage: `/giveaway edit <msgid> <flags>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```


## ,giveaway explain (Hybrid Command)
Explanation of giveaway advanced and the arguements it supports.<br/>
 - Usage: `,giveaway explain`
 - Slash Usage: `/giveaway explain`


## ,giveaway advanced (Hybrid Command)
Advanced creation of Giveaways.<br/>


`,gw explain` for a further full listing of the arguments.<br/>
 - Usage: `,giveaway advanced <arguments>`
 - Slash Usage: `/giveaway advanced <arguments>`
 - Aliases: `adv`


## ,giveaway reroll (Hybrid Command)
Reroll a giveaway.<br/>
 - Usage: `,giveaway reroll <msgid>`
 - Slash Usage: `/giveaway reroll <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```


## ,giveaway info (Hybrid Command)
Information about a giveaway.<br/>
 - Usage: `,giveaway info <msgid>`
 - Slash Usage: `/giveaway info <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```


## ,giveaway list (Hybrid Command)
List all giveaways in the server.<br/>
 - Usage: `,giveaway list`
 - Slash Usage: `/giveaway list`


## ,giveaway integrations (Hybrid Command)
Various 3rd party integrations for giveaways.<br/>
 - Usage: `,giveaway integrations`
 - Slash Usage: `/giveaway integrations`


## ,giveaway entrants (Hybrid Command)
List all entrants for a giveaway.<br/>
 - Usage: `,giveaway entrants <msgid>`
 - Slash Usage: `/giveaway entrants <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```


## ,giveaway start (Hybrid Command)
Start a giveaway.<br/>

This by default will DM the winner and also DM a user if they cannot enter the giveaway.<br/>
 - Usage: `,giveaway start <channel> <time> <prize>`
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


## ,giveaway end (Hybrid Command)
End a giveaway.<br/>
 - Usage: `,giveaway end <msgid>`
 - Slash Usage: `/giveaway end <msgid>`
Extended Arg Info
> ### msgid: int
> ```
> A number without decimal places.
> ```


