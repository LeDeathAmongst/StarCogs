# ExtendedEconomy Help

### bankpie

**Description:** View a pie chart of the top X bank balances.

**Usage:** `<@1275521742961508432>bankpie`

### extendedeconomy

**Description:** Extended Economy settings

**NOTE**
Although setting prices for pure slash commands works, there is no refund mechanism in place for them.

Should a hybrid or text command fail due to an unhandled exception, the user will be refunded.

**Usage:** `<@1275521742961508432>extendedeconomy`

### extendedeconomy stackpaydays

**Description:** Toggle whether payday roles stack or not

**Usage:** `<@1275521742961508432>extendedeconomy stackpaydays`

### extendedeconomy deleteafter

**Description:** Set the delete after time for cost check messages

- Set to 0 to disable (Recommended for public bots)
- Default is 0 (disabled)

**Usage:** `<@1275521742961508432>extendedeconomy deleteafter`

### extendedeconomy rolebonus

**Description:** Add/Remove Payday role bonuses

Example: `[p]ecoset rolebonus @role 0.1` - Adds a 10% bonus to the user's payday if they have the role.

To remove a bonus, set the bonus to 0.

**Usage:** `<@1275521742961508432>extendedeconomy rolebonus`

### extendedeconomy resetcooldown

**Description:** Reset the payday cooldown for a user

**Usage:** `<@1275521742961508432>extendedeconomy resetcooldown`

### extendedeconomy view

**Description:** View the current settings

**Usage:** `<@1275521742961508432>extendedeconomy view`

### extendedeconomy autopayday

**Description:** Toggle whether paydays are claimed automatically (Global bank)

**Usage:** `<@1275521742961508432>extendedeconomy autopayday`

### extendedeconomy mainlog

**Description:** Set the main log channel

**Usage:** `<@1275521742961508432>extendedeconomy mainlog`

### extendedeconomy transfertax

**Description:** Set the transfer tax percentage as a decimal

*Example: `0.05` is for 5% tax*

- Set to 0 to disable
- Default is 0

**Usage:** `<@1275521742961508432>extendedeconomy transfertax`

### extendedeconomy autopaydayrole

**Description:** Add/Remove auto payday roles

**Usage:** `<@1275521742961508432>extendedeconomy autopaydayrole`

### extendedeconomy eventlog

**Description:** Set an event log channel

**Events:**
- set_balance
- transfer_credits
- bank_wipe
- prune
- set_global
- payday_claim

**Usage:** `<@1275521742961508432>extendedeconomy eventlog`

### extendedeconomy autoclaimchannel

**Description:** Set the auto claim channel

**Usage:** `<@1275521742961508432>extendedeconomy autoclaimchannel`

### addcost

**Description:** Add a cost to a command

**Usage:** `<@1275521742961508432>addcost`

### banksetrole

**Description:** Set the balance of all user accounts that have a specific role

Putting + or - signs before the amount will add/remove currency on the user's bank account instead.

Examples:
- `[p]banksetrole @everyone 420` - Sets everyones balance to 420
- `[p]banksetrole @role +69` - Increases balance by 69 for everyone with the role
- `[p]banksetrole @role -42` - Decreases balance by 42 for everyone with the role

**Arguments**

- `<role>` The role to set the currency of for each user that has it.
- `<creds>` The amount of currency to set their balance to.

**Usage:** `<@1275521742961508432>banksetrole`

