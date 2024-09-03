# Strikes Help

### strike

**Description:** Strike a user.

**Usage:** `<@1275521742961508432>strike`

### delstrike

**Description:** Remove a single strike by its ID.

**Usage:** `<@1275521742961508432>delstrike`

### delstrikes

**Description:** Remove all strikes from a member.

**Usage:** `<@1275521742961508432>delstrikes`

### strikes

**Description:** Show all previous strikes for a user.

**Usage:** `<@1275521742961508432>strikes`

### allstrikes

**Description:** Show all recent individual strikes.

`[num_days]` is the number of past days of strikes to display.
Defaults to 30. When 0, all strikes from the beginning of time
will be counted shown.

**Usage:** `<@1275521742961508432>allstrikes`

### strikecounts

**Description:** Show the strike count for multiple users.

`[num_days]` is the number of past days of strikes to count.
Defaults to 0, which means all strikes from the beginning of
time will be counted.

`[limit]` is the maximum amount of members to show the
strike count for. Defaults to 100.

`[sort_by]` is the column to sort the table by. May be one of
either *count* or *date*. Defaults to *count*.

`[sort_order]` is the order to sort in. It may be one of either
*desc* for descending or *asc* for ascending. Defaults to
*desc*.

**Usage:** `<@1275521742961508432>strikecounts`

