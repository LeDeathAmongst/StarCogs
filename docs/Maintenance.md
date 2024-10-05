Put the bot on maintenance, and allow a customizable message to the people not whitelisted

# <@1275521742961508432>maintenance
Control the bot's maintenance.<br/>
 - Usage: `<@1275521742961508432>maintenance`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>maintenance on
Puts the bot on maintenance, preventing everyone but you and people whitelisted from running commands.  Other people will just be told the bot is currently on maintenance.<br/>

You can use the following arguments to specify things:<br/>
    --start-in: Makes the maintenace start in that long.<br/>
    --end-in: Schedules the maintenance to end in that long from the current second.<br/>
    --end-after: Schedules the maintenance to end in that long after the maitenance has started.<br/>
    --whitelist: Provide user IDs after this to whitelist people from the maintenance.<br/>

Examples:<br/>
`<@1275521742961508432>maintenance on --start-in 5 seconds`; starts a maintenance in 5 seconds<br/>
`<@1275521742961508432>maintenance on --start-in 5 seconds --end-in 10 seconds`; starts a maintenance in 5 seconds, then scheduled to end in 10 seconds, so it will only be on maintenance for 5 seconds.<br/>
`<@1275521742961508432>maintenance on --start-in 10 seconds --end-after 10 seconds --whitelist 473541068378341376 473541068378341377`; starts a maintenance in 10 seconds, that lasts for 10 seconds after, and has the two user IDs who are exempted from the maintenance.<br/>
 - Usage: `<@1275521742961508432>maintenance on [args]`
## <@1275521742961508432>maintenance deleteafter
Set the amount of seconds before the maintenance message is deleted.  Pass 0 to make it not delete the message.<br/>
 - Usage: `<@1275521742961508432>maintenance deleteafter <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>maintenance message
Set the message sent when the bot is down for maintenance<br/>
 - Usage: `<@1275521742961508432>maintenance message <message>`
Extended Arg Info
> ### message
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>maintenance off
Clears the bot from maintenance<br/>
 - Usage: `<@1275521742961508432>maintenance off`
## <@1275521742961508432>maintenance settings
Tells the current settings of the cog.<br/>
 - Usage: `<@1275521742961508432>maintenance settings`
## <@1275521742961508432>maintenance whitelist
Remove or add a person from or to the whitelist for the current maintenance.  Note that this is only for the current maintenance, subsequent ones must have them set again.<br/>
 - Usage: `<@1275521742961508432>maintenance whitelist <user>`
Extended Arg Info
> ### user: discord.user.User
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
