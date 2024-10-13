PayDay
======

Customizable PayDay system

More detailed docs: <https://cogs.yamikaitou.dev/payday.html>

<<<<<<< HEAD
# <@1275521742961508432>freecredits
More options to get free credits<br/>
 - Usage: `<@1275521742961508432>freecredits`
 - Checks: `server_only_check`


## <@1275521742961508432>freecredits all
Claim all available freecredits<br/>
 - Usage: `<@1275521742961508432>freecredits all`
 - Checks: `cmd_all`


## <@1275521742961508432>freecredits monthly
Get some free currency every month (30 days)<br/>
 - Usage: `<@1275521742961508432>freecredits monthly`
 - Checks: `cmd_check`


## <@1275521742961508432>freecredits yearly
Get some free currency every year (365 days)<br/>
 - Usage: `<@1275521742961508432>freecredits yearly`
 - Checks: `cmd_check`


## <@1275521742961508432>freecredits quarterly
Get some free currency every quarter (122 days)<br/>
 - Usage: `<@1275521742961508432>freecredits quarterly`
 - Checks: `cmd_check`


## <@1275521742961508432>freecredits hourly
Get some free currency every hour<br/>
 - Usage: `<@1275521742961508432>freecredits hourly`
 - Checks: `cmd_check`


## <@1275521742961508432>freecredits daily
Get some free currency every day<br/>
 - Usage: `<@1275521742961508432>freecredits daily`
 - Checks: `cmd_check`


## <@1275521742961508432>freecredits times
Display remaining time for all options<br/>
 - Usage: `<@1275521742961508432>freecredits times`
 - Checks: `cmd_all`


## <@1275521742961508432>freecredits weekly
Get some free currency every week (7 days)<br/>
 - Usage: `<@1275521742961508432>freecredits weekly`
 - Checks: `cmd_check`


# <@1275521742961508432>pdconfig
Configure the `freecredits` options<br/>

More detailed docs: <https://cogs.yamikaitou.dev/payday.html#pdconfig><br/>
 - Usage: `<@1275521742961508432>pdconfig`
=======
# ,freecredits
More options to get free credits<br/>
 - Usage: `,freecredits`
 - Checks: `server_only_check`


## ,freecredits times
Display remaining time for all options<br/>
 - Usage: `,freecredits times`
 - Checks: `cmd_all`


## ,freecredits weekly
Get some free currency every week (7 days)<br/>
 - Usage: `,freecredits weekly`
 - Checks: `cmd_check`


## ,freecredits daily
Get some free currency every day<br/>
 - Usage: `,freecredits daily`
 - Checks: `cmd_check`


## ,freecredits all
Claim all available freecredits<br/>
 - Usage: `,freecredits all`
 - Checks: `cmd_all`


## ,freecredits hourly
Get some free currency every hour<br/>
 - Usage: `,freecredits hourly`
 - Checks: `cmd_check`


## ,freecredits quarterly
Get some free currency every quarter (122 days)<br/>
 - Usage: `,freecredits quarterly`
 - Checks: `cmd_check`


## ,freecredits yearly
Get some free currency every year (365 days)<br/>
 - Usage: `,freecredits yearly`
 - Checks: `cmd_check`


## ,freecredits monthly
Get some free currency every month (30 days)<br/>
 - Usage: `,freecredits monthly`
 - Checks: `cmd_check`


# ,pdconfig
Configure the `freecredits` options<br/>

More detailed docs: <https://cogs.yamikaitou.dev/payday.html#pdconfig><br/>
 - Usage: `,pdconfig`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`


<<<<<<< HEAD
## <@1275521742961508432>pdconfig monthly
Configure the `monthly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `<@1275521742961508432>pdconfig monthly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `month`
=======
## ,pdconfig debug
Pull some config data for a specific user/member, useful for Support questions<br/>
 - Usage: `,pdconfig debug <person>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### person: Union[discord.member.Member, discord.user.User]
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


## ,pdconfig weekly
Configure the `weekly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `,pdconfig weekly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `week`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>pdconfig quarterly
Configure the `quarterly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `<@1275521742961508432>pdconfig quarterly <value>`
=======
## ,pdconfig streaks
Configure the `streaks` options<br/>
 - Usage: `,pdconfig streaks`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`


### ,pdconfig streaks percent
Configure streaks to be a percentage or flat amount<br/>

<state> should be any of these combinations, `on/off`, `yes/no`, `1/0`, `true/false`<br/>
 - Usage: `,pdconfig streaks percent <state>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `percentage`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### ,pdconfig streaks weekly
Configure the `weekly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `,pdconfig streaks weekly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `week`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


### ,pdconfig streaks yearly
Configure the `yearly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `,pdconfig streaks yearly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `year`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


### ,pdconfig streaks hourly
Configure the `hourly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `,pdconfig streaks hourly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `hour`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


### ,pdconfig streaks daily
Configure the `daily` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `,pdconfig streaks daily <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `day`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


### ,pdconfig streaks quarterly
Configure the `quarterly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `,pdconfig streaks quarterly <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Aliases: `quarter`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>pdconfig reset
=======
### ,pdconfig streaks monthly
Configure the `monthly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `,pdconfig streaks monthly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `month`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## ,pdconfig quarterly
Configure the `quarterly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `,pdconfig quarterly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `quarter`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## ,pdconfig daily
Configure the `daily` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `,pdconfig daily <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `day`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## ,pdconfig settings
Print the `freecredits` options<br/>
 - Usage: `,pdconfig settings`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`


## ,pdconfig reset
>>>>>>> 9e308722 (Revamped and Fixed)
Forcibly reset the time for a user. WARNING, this will allow the user to claim the credits right away<br/>

For <options>, you can provide any combination of the following (seperate by a space to include multiple)<br/>
hour<br/>
day<br/>
week<br/>
month<br/>
quarter<br/>
year<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>pdconfig reset <person> <options>`
=======
 - Usage: `,pdconfig reset <person> <options>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### person: Union[discord.member.Member, discord.user.User]
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
> ### options: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>pdconfig debug
Pull some config data for a specific user/member, useful for Support questions<br/>
 - Usage: `<@1275521742961508432>pdconfig debug <person>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### person: Union[discord.member.Member, discord.user.User]
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


## <@1275521742961508432>pdconfig weekly
Configure the `weekly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `<@1275521742961508432>pdconfig weekly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `week`
=======
## ,pdconfig yearly
Configure the `yearly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `,pdconfig yearly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `year`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>pdconfig streaks
Configure the `streaks` options<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`


### <@1275521742961508432>pdconfig streaks quarterly
Configure the `quarterly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks quarterly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `quarter`
=======
## ,pdconfig hourly
Configure the `hourly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `,pdconfig hourly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `hour`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
### <@1275521742961508432>pdconfig streaks monthly
Configure the `monthly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks monthly <value>`
=======
## ,pdconfig monthly
Configure the `monthly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `,pdconfig monthly <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Aliases: `month`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
### <@1275521742961508432>pdconfig streaks daily
Configure the `daily` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks daily <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `day`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>pdconfig streaks yearly
Configure the `yearly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks yearly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `year`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>pdconfig streaks weekly
Configure the `weekly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks weekly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `week`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>pdconfig streaks percent
Configure streaks to be a percentage or flat amount<br/>

<state> should be any of these combinations, `on/off`, `yes/no`, `1/0`, `true/false`<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks percent <state>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `percentage`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>pdconfig streaks hourly
Configure the `hourly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `<@1275521742961508432>pdconfig streaks hourly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `hour`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>pdconfig hourly
Configure the `hourly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `<@1275521742961508432>pdconfig hourly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `hour`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>pdconfig daily
Configure the `daily` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `<@1275521742961508432>pdconfig daily <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `day`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>pdconfig settings
Print the `freecredits` options<br/>
 - Usage: `<@1275521742961508432>pdconfig settings`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`


## <@1275521742961508432>pdconfig yearly
Configure the `yearly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `<@1275521742961508432>pdconfig yearly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `year`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


=======
>>>>>>> 9e308722 (Revamped and Fixed)
