# HitOrMiss Help

### throw

**Description:** Throw an item you own at a user

`item` is the name of the item you want to throw
`target` is the user you want to throw the item at

**Usage:** `<@1275521742961508432>throw`

### heal

**Description:** Heal yourself.

Use a medkit if you own one, to increase your hp from anywhere near 1 to 40.

**Usage:** `<@1275521742961508432>heal`

### hitormiss

**Description:** Hit or Miss

**Usage:** `<@1275521742961508432>hitormiss`

### hitormiss createitem

**Description:** Create a new Hit Or Miss item.

Owner only command.
This is an interactive questionaire asking you details about the item You want to create.

**Usage:** `<@1275521742961508432>hitormiss createitem`

### hitormiss shop

**Description:** See items available to buy for Hit Or Miss.

User `[p]buy <item>` to buy an item.

**Usage:** `<@1275521742961508432>hitormiss shop`

### hitormiss inventory

**Description:** See all the items that you currently own in Hit Or Miss.

**Usage:** `<@1275521742961508432>hitormiss inventory`

### hitormiss stats

**Description:** See yours or others Hit Or Miss stats.

**Usage:** `<@1275521742961508432>hitormiss stats`

### hitormiss deleteitem

**Description:** Delete an item from the Hit Or Miss shop that you created.

Owner only command.

**Usage:** `<@1275521742961508432>hitormiss deleteitem`

### hitormiss leaderboard

**Description:** Show the top players in the Hit Or Miss leaderboard.

There are 6 ways learderboards can be sorted:
- **Throws**: The leaderboard shows the top players who threw the most items.
- **Kills**: The amount of kills users have. (default)
- **Deaths**: The amount of times users have died.
- **Hits**: The amount of times users have hit others.
- **Misses**: The amount of times users have missed a throw.
- **KDR**: The K/D ratio of user's kills to their deaths.
- **All**: TO see all of the above at once. (This type won't be sorted and randomly placed.)

Pass any of the above exactly to the `type` parameter.

The leaderboard is `local` by default (only for the current server).
To show the global leaderboard, pass `true` to the `global_or_local` argument.

**Usage:** `<@1275521742961508432>hitormiss leaderboard`

### hitormiss buy

**Description:** Buy a Hit Or Miss item for your inventory.

`[p]buy <item>` to buy 1 of the item.
`[p]buy <amount> <item>` to buy a specific amount of the item.

where,
`<item>` is the name of the item you want to buy.

**Usage:** `<@1275521742961508432>hitormiss buy`

