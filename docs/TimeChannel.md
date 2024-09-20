# TimeChannel Help

### timezones

**Description:** See the time in all the configured timezones for this server.

**Usage:** `<@1275521742961508432>timezones`

### timechannelset

**Description:** Manage channels which will show the time for a timezone.

**Usage:** `<@1275521742961508432>timechannelset`

### timechannelset remove

**Description:** Delete and stop updating a channel.

For the <channel> argument, you can use its ID or mention (type #!channelname)

**Example:**
- `[p]tcset remove #!channelname` (the ! is how to mention voice channels)
- `[p]tcset remove 834146070094282843`

**Usage:** `<@1275521742961508432>timechannelset remove`

### timechannelset create

**Description:** Set up a time channel in this server.

If you move the channel into a category, **click 'Keep Current Permissions' in the sync
permissions dialogue.**

**How to use this command:**

First, use the `[p]tcset short <long_tz>` to get the short identifier for the
timezone of your choice.

Once you've got a short identifier from `tcset short`, you can use it in this command.
Simply put curly brackets, `{` and `}` around it, and it will be replaced with the time.

**For example**, running `[p]tcset short new york` gives a short identifier of `fv`.
This can then be used like so:
`[p]tcset create 🕑️ New York: {fv}`.

You could also use two in one, for example
`[p]tcset create UK: {ni} FR: {nr}`

The default is 12 hour time, but you can use `{shortid-24h}` for 24 hour time,
eg `{ni-24h}`

**More Examples:**
- `[p]tcset create 🕑️ New York: {fv}`
- `[p]tcset create 🌐 UTC: {qw}`
- `[p]tcset create {ni-24h} in London`
- `[p]tcset create US Pacific: {qv-24h}`

**Usage:** `<@1275521742961508432>timechannelset create`

### timechannelset short

**Description:** Get the short identifier for the main `create` command.

The list of acceptable timezones is here (the "TZ database name" column):
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List

There is a fuzzy search, so you shouldn't need to enter the region.

Please look at `[p]help tcset create` for more information.

**Examples:**
- `[p]tcset short New York`
- `[p]tcset short UTC`
- `[p]tcset short London`
- `[p]tcset short Europe/London`

**Usage:** `<@1275521742961508432>timechannelset short`

