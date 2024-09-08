# Economy Help

### bank

**Description:** Base command to manage the bank.

**Usage:** `<@1275521742961508432>bank`

### bank balance

**Description:** Show the user's account balance.

Example:
- `[p]bank balance`
- `[p]bank balance @Twentysix`

**Arguments**

- `<user>` The user to check the balance of. If omitted, defaults to your own balance.

**Usage:** `<@1275521742961508432>bank balance`

### bank transfer

**Description:** Transfer currency to other users.

This will come out of your balance, so make sure you have enough.

Example:
- `[p]bank transfer @Twentysix 500`

**Arguments**

- `<to>` The user to give currency to.
- `<amount>` The amount of currency to give.

**Usage:** `<@1275521742961508432>bank transfer`

### bank set

**Description:** Set the balance of a user's bank account.

Putting + or - signs before the amount will add/remove currency on the user's bank account instead.

Examples:
- `[p]bank set @Twentysix 26` - Sets balance to 26
- `[p]bank set @Twentysix +2` - Increases balance by 2
- `[p]bank set @Twentysix -6` - Decreases balance by 6

**Arguments**

- `<to>` The user to set the currency of.
- `<creds>` The amount of currency to set their balance to.

**Usage:** `<@1275521742961508432>bank set`

### payday

**Description:** No description provided.

**Usage:** `<@1275521742961508432>payday`

### leaderboard

**Description:** Print the leaderboard.

Defaults to top 10.

Examples:
- `[p]leaderboard`
- `[p]leaderboard 50` - Shows the top 50 instead of top 10.
- `[p]leaderboard 100 yes` - Shows the top 100 from all servers.

**Arguments**

- `<top>` How many positions on the leaderboard to show. Defaults to 10 if omitted.
- `<show_global>` Whether to include results from all servers. This will default to false unless specified.

**Usage:** `<@1275521742961508432>leaderboard`

### payouts

**Description:** Show the payouts for the slot machine.

**Usage:** `<@1275521742961508432>payouts`

### slot

**Description:** Use the slot machine.

Example:
- `[p]slot 50`

**Arguments**

- `<bid>` The amount to bet on the slot machine. Winning payouts are higher when you bet more.

**Usage:** `<@1275521742961508432>slot`

### economyset

**Description:** Base command to manage Economy settings.

**Usage:** `<@1275521742961508432>economyset`

### economyset paydayamount

**Description:** Set the amount earned each payday.

Example:
- `[p]economyset paydayamount 400`

**Arguments**

- `<creds>` The new amount to give when using the payday command. Default is 120.

**Usage:** `<@1275521742961508432>economyset paydayamount`

### economyset paydaytime

**Description:** Set the cooldown for the payday command.

Examples:
- `[p]economyset paydaytime 86400`
- `[p]economyset paydaytime 1d`

**Arguments**

- `<duration>` The new duration to wait in between uses of payday. Default is 5 minutes.
Accepts: seconds, minutes, hours, days, weeks (if no unit is specified, the duration is assumed to be given in seconds)

**Usage:** `<@1275521742961508432>economyset paydaytime`

### economyset slotmin

**Description:** Set the minimum slot machine bid.

Example:
- `[p]economyset slotmin 10`

**Arguments**

- `<bid>` The new minimum bid for using the slot machine. Default is 5.

**Usage:** `<@1275521742961508432>economyset slotmin`

### economyset slotmax

**Description:** Set the maximum slot machine bid.

Example:
- `[p]economyset slotmax 50`

**Arguments**

- `<bid>` The new maximum bid for using the slot machine. Default is 100.

**Usage:** `<@1275521742961508432>economyset slotmax`

### economyset showsettings

**Description:** Shows the current economy settings

**Usage:** `<@1275521742961508432>economyset showsettings`

### economyset slottime

**Description:** Set the cooldown for the slot machine.

Examples:
- `[p]economyset slottime 10`
- `[p]economyset slottime 10m`

**Arguments**

- `<duration>` The new duration to wait in between uses of the slot machine. Default is 5 seconds.
Accepts: seconds, minutes, hours, days, weeks (if no unit is specified, the duration is assumed to be given in seconds)

**Usage:** `<@1275521742961508432>economyset slottime`

### economyset rolepaydayamount

**Description:** Set the amount earned each payday for a role.

Set to `0` to remove the payday amount you set for that role.

Only available when not using a global bank.

Example:
- `[p]economyset rolepaydayamount @Members 400`

**Arguments**

- `<role>` The role to assign a custom payday amount to.
- `<creds>` The new amount to give when using the payday command.

**Usage:** `<@1275521742961508432>economyset rolepaydayamount`

