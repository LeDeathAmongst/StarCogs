Economy
=======

Get rich and have fun with imaginary currency!

# <@1275521742961508432>bank
Base command to manage the bank.<br/>
 - Usage: `<@1275521742961508432>bank`
 - Checks: `server_only_check`


## <@1275521742961508432>bank transfer
Transfer currency to other users.<br/>

This will come out of your balance, so make sure you have enough.<br/>

Example:<br/>
- `<@1275521742961508432>bank transfer @Twentysix 500`<br/>

**Arguments**<br/>

- `<to>` The user to give currency to.<br/>
- `<amount>` The amount of currency to give.<br/>
 - Usage: `<@1275521742961508432>bank transfer <to> <amount>`
Extended Arg Info
> ### to: discord.member.Member
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
> ### amount: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>bank balance
Show the user's account balance.<br/>

Example:<br/>
- `<@1275521742961508432>bank balance`<br/>
- `<@1275521742961508432>bank balance @Twentysix`<br/>

**Arguments**<br/>

- `<user>` The user to check the balance of. If omitted, defaults to your own balance.<br/>
 - Usage: `<@1275521742961508432>bank balance [user=operator.attrgetter('author')]`
Extended Arg Info
> ### user: discord.member.Member = operator.attrgetter('author')
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


## <@1275521742961508432>bank set
Set the balance of a user's bank account.<br/>

Putting + or - signs before the amount will add/remove currency on the user's bank account instead.<br/>

Examples:<br/>
- `<@1275521742961508432>bank set @Twentysix 26` - Sets balance to 26<br/>
- `<@1275521742961508432>bank set @Twentysix +2` - Increases balance by 2<br/>
- `<@1275521742961508432>bank set @Twentysix -6` - Decreases balance by 6<br/>

**Arguments**<br/>

- `<to>` The user to set the currency of.<br/>
- `<creds>` The amount of currency to set their balance to.<br/>
 - Usage: `<@1275521742961508432>bank set <to> <creds>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### to: discord.member.Member
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


# <@1275521742961508432>payday

 - Usage: `<@1275521742961508432>payday`
 - Checks: `server_only_check`


# <@1275521742961508432>leaderboard
Print the leaderboard.<br/>

Defaults to top 10.<br/>

Examples:<br/>
- `<@1275521742961508432>leaderboard`<br/>
- `<@1275521742961508432>leaderboard 50` - Shows the top 50 instead of top 10.<br/>
- `<@1275521742961508432>leaderboard 100 yes` - Shows the top 100 from all servers.<br/>

**Arguments**<br/>

- `<top>` How many positions on the leaderboard to show. Defaults to 10 if omitted.<br/>
- `<show_global>` Whether to include results from all servers. This will default to false unless specified.<br/>
 - Usage: `<@1275521742961508432>leaderboard [top=10] [show_global=False]`
 - Checks: `server_only_check`
Extended Arg Info
> ### top: int = 10
> ```
> A number without decimal places.
> ```
> ### show_global: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>payouts
Show the payouts for the slot machine.<br/>
 - Usage: `<@1275521742961508432>payouts`
 - Checks: `server_only_check`


# <@1275521742961508432>slot
Use the slot machine.<br/>

Example:<br/>
- `<@1275521742961508432>slot 50`<br/>

**Arguments**<br/>

- `<bid>` The amount to bet on the slot machine. Winning payouts are higher when you bet more.<br/>
 - Usage: `<@1275521742961508432>slot <bid>`
 - Checks: `server_only_check`
Extended Arg Info
> ### bid: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>economyset
Base command to manage Economy settings.<br/>
 - Usage: `<@1275521742961508432>economyset`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global and server_only_check`


## <@1275521742961508432>economyset showsettings
Shows the current economy settings<br/>
 - Usage: `<@1275521742961508432>economyset showsettings`


## <@1275521742961508432>economyset paydayamount
Set the amount earned each payday.<br/>

Example:<br/>
- `<@1275521742961508432>economyset paydayamount 400`<br/>

**Arguments**<br/>

- `<creds>` The new amount to give when using the payday command. Default is 120.<br/>
 - Usage: `<@1275521742961508432>economyset paydayamount <creds>`
Extended Arg Info
> ### creds: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>economyset paydaytime
Set the cooldown for the payday command.<br/>

Examples:<br/>
- `<@1275521742961508432>economyset paydaytime 86400`<br/>
- `<@1275521742961508432>economyset paydaytime 1d`<br/>

**Arguments**<br/>

- `<duration>` The new duration to wait in between uses of payday. Default is 5 minutes.<br/>
Accepts: seconds, minutes, hours, days, weeks (if no unit is specified, the duration is assumed to be given in seconds)<br/>
 - Usage: `<@1275521742961508432>economyset paydaytime <duration>`


## <@1275521742961508432>economyset slotmax
Set the maximum slot machine bid.<br/>

Example:<br/>
- `<@1275521742961508432>economyset slotmax 50`<br/>

**Arguments**<br/>

- `<bid>` The new maximum bid for using the slot machine. Default is 100.<br/>
 - Usage: `<@1275521742961508432>economyset slotmax <bid>`


## <@1275521742961508432>economyset rolepaydayamount
Set the amount earned each payday for a role.<br/>

Set to `0` to remove the payday amount you set for that role.<br/>

Only available when not using a global bank.<br/>

Example:<br/>
- `<@1275521742961508432>economyset rolepaydayamount @Members 400`<br/>

**Arguments**<br/>

- `<role>` The role to assign a custom payday amount to.<br/>
- `<creds>` The new amount to give when using the payday command.<br/>
 - Usage: `<@1275521742961508432>economyset rolepaydayamount <role> <creds>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### creds: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>economyset slottime
Set the cooldown for the slot machine.<br/>

Examples:<br/>
- `<@1275521742961508432>economyset slottime 10`<br/>
- `<@1275521742961508432>economyset slottime 10m`<br/>

**Arguments**<br/>

- `<duration>` The new duration to wait in between uses of the slot machine. Default is 5 seconds.<br/>
Accepts: seconds, minutes, hours, days, weeks (if no unit is specified, the duration is assumed to be given in seconds)<br/>
 - Usage: `<@1275521742961508432>economyset slottime <duration>`


## <@1275521742961508432>economyset slotmin
Set the minimum slot machine bid.<br/>

Example:<br/>
- `<@1275521742961508432>economyset slotmin 10`<br/>

**Arguments**<br/>

- `<bid>` The new minimum bid for using the slot machine. Default is 5.<br/>
 - Usage: `<@1275521742961508432>economyset slotmin <bid>`


