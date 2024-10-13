Unbelievaboat Commands.

# ,unbset
Manage various settings for Unbelievaboat.<br/>
 - Usage: `,unbset`
 - Aliases: `unb-set`
 - Checks: `server_only and check_global_setting_admin`
## ,unbset fine-rate
Set the min or max fine rate for crimes.<br/>
 - Usage: `,unbset fine-rate <min_or_max> <amount>`
 - Aliases: `finerate`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### min_or_max: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,unbset add-reply
Add a custom reply for working or crime.<br/>

Put {amount} in place of where you want the amount earned to be.<br/>
 - Usage: `,unbset add-reply <job> <reply>`
 - Checks: `check_global_setting_admin and server_only`
Extended Arg Info
> ### job
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reply: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,unbset failure-rate
Set the failure rate for crimes and robbing.<br/>
 - Usage: `,unbset failure-rate <job> <amount>`
 - Aliases: `failurerate`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### job: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,unbset interest-rate
Set the interest rate if unable to pay a fine from wallet.<br/>
 - Usage: `,unbset interest-rate <amount>`
 - Aliases: `interestrate`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,unbset default-replies
Whether to use the default replies to work and crime.<br/>
 - Usage: `,unbset default-replies <enable>`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### enable: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,unbset del-reply
Delete a custom reply.<br/>
 - Usage: `,unbset del-reply <job> <id>`
 - Checks: `check_global_setting_admin and server_only`
Extended Arg Info
> ### job
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### id: int
> ```
> A number without decimal places.
> ```
## ,unbset betting
Set the min or max betting amounts.<br/>
 - Usage: `,unbset betting <min_or_max> <amount>`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### min_or_max: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,unbset wallet
Wallet Settings.<br/>
 - Usage: `,unbset wallet`
 - Checks: `server_only and check_global_setting_admin`
### ,unbset wallet toggle
Toggle the wallet system.<br/>
 - Usage: `,unbset wallet toggle <on_or_off>`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,unbset wallet max
Set the max a wallet can have.<br/>
 - Usage: `,unbset wallet max <amount>`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,unbset list-replies
List custom replies.<br/>
 - Usage: `,unbset list-replies <job>`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### job
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,unbset settings
Current unbelievaboat settings.<br/>
 - Usage: `,unbset settings`
 - Checks: `check_global_setting_admin and server_only`
## ,unbset payout
Set the min or max payout for working or crimes.<br/>
 - Usage: `,unbset payout <job> <min_or_max> <amount>`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### job: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### min_or_max: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,unbset cooldown
Set the cooldown for the work, crime or rob commands. Minimum cooldown is 30 seconds.<br/>

The time can be formatted as so `1h30m` etc. Valid times are hours, minutes and seconds.<br/>
 - Usage: `,unbset cooldown <job> <time>`
 - Checks: `server_only`
Extended Arg Info
> ### job
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,cooldowns
List your remaining cooldowns..<br/>
 - Usage: `,cooldowns`
 - Checks: `server_only`
# ,roulette
Bet on the roulette wheel.<br/>

**Current supported bets**:<br/>
Single   - Any single number.<br/>
Colors   - Red/Black<br/>
Halfs    - 1st/2nd half<br/>
Even Odd - Even or Odd<br/>
Dozens   - 1st/2nd/3rd Dozen (Groups of 12)<br/>
Colums   - 1st/2nd/3rd Column.<br/>
- This is based on the English version of the roulette wheel.<br/>
 - Usage: `,roulette <amount> <bet>`
 - Checks: `roulette_disabled_check and server_only`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
> ### bet
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,roulette start
Start a game of roulette.<br/>
 - Usage: `,roulette start`
 - Checks: `roulette_disabled_check`
# ,rouletteset
Manage settings for roulette.<br/>
 - Usage: `,rouletteset`
 - Restricted to: `ADMIN`
 - Checks: `server_only and check_global_setting_admin`
## ,rouletteset toggle
Toggle roulette on and off.<br/>
 - Usage: `,rouletteset toggle`
 - Checks: `server_only and check_global_setting_admin`
## ,rouletteset time
Set the time for roulette wheel to start spinning.<br/>
 - Usage: `,rouletteset time <time>`
 - Checks: `server_only, check_global_setting_admin, and roulette_disabled_check`
## ,rouletteset settings
Roulette Settings.<br/>
 - Usage: `,rouletteset settings`
## ,rouletteset payouts
Set payouts for roulette winnings.<br/>

Note: payout is what your prize is multiplied by.<br/>
Valid types:<br/>
zero<br/>
single<br/>
color<br/>
dozen<br/>
odd_or_even<br/>
halfs<br/>
column<br/>
 - Usage: `,rouletteset payouts <type> <payout>`
 - Checks: `server_only, check_global_setting_admin, and roulette_disabled_check`
Extended Arg Info
> ### type
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### payout: int
> ```
> A number without decimal places.
> ```
# ,wallet
Wallet commands.<br/>
 - Usage: `,wallet`
 - Checks: `server_only and wallet_disabled_check`
## ,wallet balance
Show the user's wallet balance.<br/>

Defaults to yours.<br/>
 - Usage: `,wallet balance [user=None]`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member = None
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
## ,wallet set
Set a users wallet balance.<br/>
 - Usage: `,wallet set <user> <amount>`
 - Checks: `server_only, check_global_setting_admin, and wallet_disabled_check`
Extended Arg Info
> ### user: discord.member.Member
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
## ,wallet leaderboard
Print the wallet leaderboard.<br/>
 - Usage: `,wallet leaderboard [top=10]`
 - Checks: `server_only`
Extended Arg Info
> ### top: int = 10
> ```
> A number without decimal places.
> ```
# ,deposit
Deposit cash from your wallet to your bank.<br/>
 - Usage: `,deposit <amount>`
 - Cooldown: `1 per 5.0 seconds`
 - Checks: `server_only and wallet_disabled_check`
Extended Arg Info
> ### amount: Union[int, str]
> ```
> A number without decimal places.
> ```
# ,withdraw
Withdraw cash from your bank to your wallet.<br/>
 - Usage: `,withdraw <amount>`
 - Cooldown: `1 per 5.0 seconds`
 - Checks: `server_only and wallet_disabled_check`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
# ,addmoneyrole
Add money to the balance of all users within a role.<br/>

Valid arguements are 'banks' or 'wallet'.<br/>
 - Usage: `,addmoneyrole <amount> <role> [destination=wallet]`
 - Restricted to: `ADMIN`
 - Aliases: `addcashrole`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### destination: Optional[str] = 'wallet'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,removemoneyrole
Remove money from the bank balance of all users within a role.<br/>

Valid arguements are 'banks' or 'wallet'.<br/>
 - Usage: `,removemoneyrole <amount> <role> [destination=wallet]`
 - Restricted to: `ADMIN`
 - Aliases: `removecashrole`
 - Checks: `server_only and check_global_setting_admin`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### destination: Optional[str] = 'wallet'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,work
Work for some cash.<br/>
 - Usage: `,work`
 - Checks: `server_only`
# ,crime
Commit a crime, more risk but higher payout.<br/>
 - Usage: `,crime`
 - Checks: `server_only`
# ,rob
Rob another user.<br/>
 - Usage: `,rob <user>`
 - Checks: `wallet_disabled_check and server_only`
Extended Arg Info
> ### user: discord.member.Member
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
