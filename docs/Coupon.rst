Coupon
======

Creates redeemable coupons for credits.

The bank must be in guild mode and not global mode for this cog to work.

# <@1275521742961508432>coupon
Coupon commands.<br/>
 - Usage: `<@1275521742961508432>coupon`
 - Checks: `server_only and pred`


## <@1275521742961508432>coupon clearall
Clears all unclaimed coupons.<br/>
 - Usage: `<@1275521742961508432>coupon clearall`
 - Restricted to: `MOD`
 - Checks: `pred`


## <@1275521742961508432>coupon create
Generates a unique coupon code.<br/>
 - Usage: `<@1275521742961508432>coupon create <credits>`
 - Restricted to: `ADMIN`
 - Checks: `pred`
Extended Arg Info
> ### credits: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>coupon list
Shows active coupon codes.<br/>
 - Usage: `<@1275521742961508432>coupon list`
 - Restricted to: `ADMIN`
 - Checks: `pred`


## <@1275521742961508432>coupon redeem
Redeems a coupon code.<br/>
 - Usage: `<@1275521742961508432>coupon redeem <coupon>`
 - Checks: `pred`
Extended Arg Info
> ### coupon: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


