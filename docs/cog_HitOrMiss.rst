HitOrMiss
=========

A snowball bot based (but hugely different) cog.

And no it doesn't use slash commands.
*Yet*.

<<<<<<< HEAD
# <@1275521742961508432>throw
=======
# ,throw
>>>>>>> 9e308722 (Revamped and Fixed)
Throw an item you own at a user<br/>

`item` is the name of the item you want to throw<br/>
`target` is the user you want to throw the item at<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>throw <target> <item>`
 - Cooldown: `1 per 5.0 seconds`


# <@1275521742961508432>heal
Heal yourself.<br/>

Use a medkit if you own one, to increase your hp from anywhere near 1 to 40.<br/>
 - Usage: `<@1275521742961508432>heal`
 - Cooldown: `1 per 60.0 seconds`


# <@1275521742961508432>hitormiss
Hit or Miss<br/>
 - Usage: `<@1275521742961508432>hitormiss`
=======
 - Usage: `,throw <target> <item>`
 - Cooldown: `1 per 5.0 seconds`


# ,heal
Heal yourself.<br/>

Use a medkit if you own one, to increase your hp from anywhere near 1 to 40.<br/>
 - Usage: `,heal`
 - Cooldown: `1 per 60.0 seconds`


# ,hitormiss
Hit or Miss<br/>
 - Usage: `,hitormiss`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `hom`
 - Cooldown: `2 per 5.0 seconds`


<<<<<<< HEAD
## <@1275521742961508432>hitormiss buy
Buy a Hit Or Miss item for your inventory.<br/>

`<@1275521742961508432>buy <item>` to buy 1 of the item.<br/>
`<@1275521742961508432>buy <amount> <item>` to buy a specific amount of the item.<br/>

where,<br/>
`<item>` is the name of the item you want to buy.<br/>
 - Usage: `<@1275521742961508432>hitormiss buy [amount=None] <item>`
 - Aliases: `purchase`
Extended Arg Info
> ### amount: Optional[int] = None
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>hitormiss inventory
See all the items that you currently own in Hit Or Miss.<br/>
 - Usage: `<@1275521742961508432>hitormiss inventory`
 - Aliases: `inv`


## <@1275521742961508432>hitormiss stats
See yours or others Hit Or Miss stats.<br/>
 - Usage: `<@1275521742961508432>hitormiss stats [user=None]`
 - Aliases: `profile`


## <@1275521742961508432>hitormiss deleteitem
Delete an item from the Hit Or Miss shop that you created.<br/>

Owner only command.<br/>
 - Usage: `<@1275521742961508432>hitormiss deleteitem <item>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `remove, delete, and di`


## <@1275521742961508432>hitormiss leaderboard
=======
## ,hitormiss inventory
See all the items that you currently own in Hit Or Miss.<br/>
 - Usage: `,hitormiss inventory`
 - Aliases: `inv`


## ,hitormiss leaderboard
>>>>>>> 9e308722 (Revamped and Fixed)
Show the top players in the Hit Or Miss leaderboard.<br/>

There are 6 ways learderboards can be sorted:<br/>
- **Throws**: The leaderboard shows the top players who threw the most items.<br/>
- **Kills**: The amount of kills users have. (default)<br/>
- **Deaths**: The amount of times users have died.<br/>
- **Hits**: The amount of times users have hit others.<br/>
- **Misses**: The amount of times users have missed a throw.<br/>
- **KDR**: The K/D ratio of user's kills to their deaths.<br/>
- **All**: TO see all of the above at once. (This type won't be sorted and randomly placed.)<br/>

Pass any of the above exactly to the `type` parameter.<br/>

The leaderboard is `local` by default (only for the current server).<br/>
To show the global leaderboard, pass `true` to the `global_or_local` argument.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hitormiss leaderboard [_type=kills] [global_or_local=False]`
 - Aliases: `lb and top`


## <@1275521742961508432>hitormiss createitem
=======
 - Usage: `,hitormiss leaderboard [_type=kills] [global_or_local=False]`
 - Aliases: `lb and top`


## ,hitormiss buy
Buy a Hit Or Miss item for your inventory.<br/>

`,buy <item>` to buy 1 of the item.<br/>
`,buy <amount> <item>` to buy a specific amount of the item.<br/>

where,<br/>
`<item>` is the name of the item you want to buy.<br/>
 - Usage: `,hitormiss buy [amount=None] <item>`
 - Aliases: `purchase`
Extended Arg Info
> ### amount: Optional[int] = None
> ```
> A number without decimal places.
> ```


## ,hitormiss stats
See yours or others Hit Or Miss stats.<br/>
 - Usage: `,hitormiss stats [user=None]`
 - Aliases: `profile`


## ,hitormiss createitem
>>>>>>> 9e308722 (Revamped and Fixed)
Create a new Hit Or Miss item.<br/>

Owner only command.<br/>
This is an interactive questionaire asking you details about the item You want to create.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hitormiss createitem`
=======
 - Usage: `,hitormiss createitem`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `make, create, newitem, and ci`


<<<<<<< HEAD
## <@1275521742961508432>hitormiss shop
See items available to buy for Hit Or Miss.<br/>

User `<@1275521742961508432>buy <item>` to buy an item.<br/>
 - Usage: `<@1275521742961508432>hitormiss shop`
=======
## ,hitormiss deleteitem
Delete an item from the Hit Or Miss shop that you created.<br/>

Owner only command.<br/>
 - Usage: `,hitormiss deleteitem <item>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `remove, delete, and di`


## ,hitormiss shop
See items available to buy for Hit Or Miss.<br/>

User `,buy <item>` to buy an item.<br/>
 - Usage: `,hitormiss shop`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `items`


