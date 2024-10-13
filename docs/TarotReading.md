Post information about tarot cards and readings

# ,tarot (Hybrid Command)
Receive a tarot reading<br/>
 - Usage: `,tarot`
 - Slash Usage: `/tarot`
## ,tarot set (Hybrid Command)
Set commands for tarot<br/>
 - Usage: `,tarot set`
 - Slash Usage: `/tarot set`
### ,tarot set globaldeck (Hybrid Command)
Set which deck to use from https://www.tarot.com/tarot/decks<br/>

This sets it for every server the bot is in by default. Servers<br/>
can specify their own deck to use via `,tarot set deck`<br/>

`deck_name` must be the name in the URL for the deck you want to use.<br/>
If not provided will revert to the default to the Rider–Waite Tarot Deck.<br/>
 - Usage: `,tarot set globaldeck [deck_name=None]`
 - Slash Usage: `/tarot set globaldeck [deck_name=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### deck_name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,tarot set deck (Hybrid Command)
Set which deck to use from https://www.tarot.com/tarot/decks<br/>

`deck_name` must be the name in the URL for the deck you want to use.<br/>
If not provided will revert to the default to the Rider–Waite Tarot Deck.<br/>
 - Usage: `,tarot set deck [deck_name=None]`
 - Slash Usage: `/tarot set deck [deck_name=None]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### deck_name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,tarot life (Hybrid Command)
Unique reading based on your discord user ID. Doesn't change.<br/>

`[user]` Optional user who you want to see a life tarot reading for.<br/>
If no user is provided this will run for the user who is running the command.<br/>
 - Usage: `,tarot life [user=None]`
 - Slash Usage: `/tarot life [user=None]`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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
## ,tarot reading (Hybrid Command)
Unique reading as of this very moment.<br/>

`[user]` Optional user you want to view a tarot reading for.<br/>
If no user is provided this will run for the user who is running the command.<br/>
 - Usage: `,tarot reading [user=None]`
 - Slash Usage: `/tarot reading [user=None]`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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
## ,tarot card (Hybrid Command)
Random card or choose a card based on number or name.<br/>

`[tarot_card]` Is the full name of any tarot card or a number corresponding to specific cards.<br/>
If this doesn't match any cards number or name then a random one will be displayed instead.<br/>
 - Usage: `,tarot card <tarot_card>`
 - Slash Usage: `/tarot card <tarot_card>`
