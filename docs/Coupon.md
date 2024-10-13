Creates redeemable coupons for credits.<br/><br/>The bank must be in guild mode and not global mode for this cog to work.

# ,coupon
Coupon commands.<br/>
 - Usage: `,coupon`
 - Checks: `server_only and pred`
## ,coupon redeem
Redeems a coupon code.<br/>
 - Usage: `,coupon redeem <coupon>`
 - Checks: `pred`
Extended Arg Info
> ### coupon: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,coupon clearall
Clears all unclaimed coupons.<br/>
 - Usage: `,coupon clearall`
 - Restricted to: `MOD`
 - Checks: `pred`
## ,coupon list
Shows active coupon codes.<br/>
 - Usage: `,coupon list`
 - Restricted to: `ADMIN`
 - Checks: `pred`
## ,coupon create
Generates a unique coupon code.<br/>
 - Usage: `,coupon create <credits>`
 - Restricted to: `ADMIN`
 - Checks: `pred`
Extended Arg Info
> ### credits: int
> ```
> A number without decimal places.
> ```
