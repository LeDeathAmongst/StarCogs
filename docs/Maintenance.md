# Maintenance Help

### maintenance

**Description:** Control the bot's maintenance.

**Usage:** `<@1275521742961508432>maintenance`

### maintenance message

**Description:** Set the message sent when the bot is down for maintenance

**Usage:** `<@1275521742961508432>maintenance message`

### maintenance deleteafter

**Description:** Set the amount of seconds before the maintenance message is deleted.  Pass 0 to make it not delete the message.

**Usage:** `<@1275521742961508432>maintenance deleteafter`

### maintenance off

**Description:** Clears the bot from maintenance

**Usage:** `<@1275521742961508432>maintenance off`

### maintenance whitelist

**Description:** Remove or add a person from or to the whitelist for the current maintenance.  Note that this is only for the current maintenance, subsequent ones must have them set again.

**Usage:** `<@1275521742961508432>maintenance whitelist`

### maintenance settings

**Description:** Tells the current settings of the cog.

**Usage:** `<@1275521742961508432>maintenance settings`

### maintenance on

**Description:** Puts the bot on maintenance, preventing everyone but you and people whitelisted from running commands.  Other people will just be told the bot is currently on maintenance.

You can use the following arguments to specify things:
    --start-in: Makes the maintenace start in that long.
    --end-in: Schedules the maintenance to end in that long from the current second.
    --end-after: Schedules the maintenance to end in that long after the maitenance has started.
    --whitelist: Provide user IDs after this to whitelist people from the maintenance.

Examples:
`[p]maintenance on --start-in 5 seconds`; starts a maintenance in 5 seconds
`[p]maintenance on --start-in 5 seconds --end-in 10 seconds`; starts a maintenance in 5 seconds, then scheduled to end in 10 seconds, so it will only be on maintenance for 5 seconds.
`[p]maintenance on --start-in 10 seconds --end-after 10 seconds --whitelist 473541068378341376 473541068378341377`; starts a maintenance in 10 seconds, that lasts for 10 seconds after, and has the two user IDs who are exempted from the maintenance.

**Usage:** `<@1275521742961508432>maintenance on`

