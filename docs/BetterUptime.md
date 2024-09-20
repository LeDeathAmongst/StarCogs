# BetterUptime Help

### uptime

**Description:** No description provided.

**Usage:** `<@1275521742961508432>uptime`

### uptime data

**Description:** No description provided.

**Usage:** `<@1275521742961508432>uptime data`

### uptime graph

**Description:** No description provided.

**Usage:** `<@1275521742961508432>uptime graph`

### uptime downtime

**Description:** No description provided.

**Usage:** `<@1275521742961508432>uptime downtime`

### uptime

**Description:** Get [botname]'s uptime percent over the last 30 days, and when I was last restarted.

The default value for `num_days` is `30`. You can put `0` days for all-time data.
Otherwise, it needs to be `5` or more.

Note: embeds must be enabled for this rich data to show

**Examples:**
- `[p]uptime`
- `[p]uptime 0` (for all-time data)
- `[p]uptime 7`

**Usage:** `<@1275521742961508432>uptime`

### downtime

**Description:** Check [botname] downtime over the last 30 days.

The default value for `num_days` is `30`. You can put `0` days for all-time data.
Otherwise, it needs to be `5` or more.

**Examples:**
- `[p]uptime`
- `[p]uptime 0` (for all-time data)
- `[p]uptime 7`

**Usage:** `<@1275521742961508432>downtime`

### uptimegraph

**Description:** Check [botname] uptime with a graph over the last 30 days.

The default value for `num_days` is `30`. You can put `0` days for all-time data.
Otherwise, it needs to be `5` or more.

**Examples:**
- `[p]uptime` - for the default of 30 days
- `[p]uptime 0` - for all-time data
-]uptime 7` - 7 days

**Usage:** `<@1275521742961508432>uptimegraph`

### uptimeexport

**Description:** Export my uptime data to CSV

The numbers represent uptime, so 86400 means 100% for that day (86400 seconds in 1 day).

Everything is in UTC.

Connected is the bot being connected to Discord.

Cog loaded is the cog being loaded but not necessarily connected to Discord.

Therefore, connected should always be equal to or lower than cog loaded.

**Usage:** `<@1275521742961508432>uptimeexport`

### resetbu

**Description:** Reset the cog's data.

**Usage:** `<@1275521742961508432>resetbu`

