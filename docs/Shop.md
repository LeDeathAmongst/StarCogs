# <@1275521742961508432>shop
Shop commands.<br/>
 - Usage: `<@1275521742961508432>shop`
 - Checks: `server_only`
## <@1275521742961508432>shop selling

 - Usage: `<@1275521742961508432>shop selling <user>`
Extended Arg Info
> ### user: Optional[discord.user.User]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## <@1275521742961508432>shop createitem
Create an item for sale in the shop.<br/>
 - Usage: `<@1275521742961508432>shop createitem <name>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `ci`
## <@1275521742961508432>shop deleteitem
Delete an item from the shop.<br/>
 - Usage: `<@1275521742961508432>shop deleteitem <name>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `di`
## <@1275521742961508432>shop offer
Offer an item for sale in the shop.<br/>
`item`: The item to sell.<br/>
`price`: The price of the item.<br/>
`amount`: The amount of the item you want to offer.<br/>

Once you offer an item up for sell, it will show up in the `<@1275521742961508432>shop selling` command for people to buy it.<br/>
 - Usage: `<@1275521742961508432>shop offer <item> <price> <amount>`
Extended Arg Info
> ### item: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### price: int
> ```
> A number without decimal places.
> ```
> ### amount: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>shop listitems
List items for sale in the shop.<br/>
 - Usage: `<@1275521742961508432>shop listitems`
 - Aliases: `li`
