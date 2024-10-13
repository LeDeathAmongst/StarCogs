ReviewsCog
==========

A cog for managing product or service reviews.

# ,review
Review commands.<br/>
 - Usage: `,review`
 - Checks: `server_only`


## ,review export
Export reviews to a CSV or PDF file.<br/>
 - Usage: `,review export <file_format>`
Extended Arg Info
> ### file_format: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,review approve
Approve a review.<br/>
 - Usage: `,review approve <review_id>`
Extended Arg Info
> ### review_id: int
> ```
> A number without decimal places.
> ```


## ,review list
List all reviews.<br/>
 - Usage: `,review list`


## ,review setchannel
Set the channel where approved reviews will be posted.<br/>
 - Usage: `,review setchannel <channel>`
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


## ,review submit
Submit a review for approval.<br/>
 - Usage: `,review submit`


## ,review remove
Remove a review.<br/>
 - Usage: `,review remove <review_id>`
Extended Arg Info
> ### review_id: int
> ```
> A number without decimal places.
> ```


