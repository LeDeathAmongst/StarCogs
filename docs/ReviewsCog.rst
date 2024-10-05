ReviewsCog
==========

A cog for managing product or service reviews.

# <@1275521742961508432>review
Review commands.<br/>
 - Usage: `<@1275521742961508432>review`
 - Checks: `server_only`


## <@1275521742961508432>review remove
Remove a review.<br/>
 - Usage: `<@1275521742961508432>review remove <review_id>`
Extended Arg Info
> ### review_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>review submit
Submit a review for approval.<br/>
 - Usage: `<@1275521742961508432>review submit`


## <@1275521742961508432>review setchannel
Set the channel where approved reviews will be posted.<br/>
 - Usage: `<@1275521742961508432>review setchannel <channel>`
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


## <@1275521742961508432>review export
Export reviews to a CSV or PDF file.<br/>
 - Usage: `<@1275521742961508432>review export <file_format>`
Extended Arg Info
> ### file_format: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>review list
List all reviews.<br/>
 - Usage: `<@1275521742961508432>review list`


## <@1275521742961508432>review approve
Approve a review.<br/>
 - Usage: `<@1275521742961508432>review approve <review_id>`
Extended Arg Info
> ### review_id: int
> ```
> A number without decimal places.
> ```


