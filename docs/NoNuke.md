# NoNuke Help

### nonuke

**Description:** Anti-Nuke System for lazy guild owners!

Monitors the following events:
Kicks & Bans
Channel Creation/Edit/Deletion
Role Creation/Edit/Deletion

Set a cooldown(in seconds)
Set an overload count(X events in X seconds)
Set an action(kick, ban, strip, notify)

If a user or bot exceeds X mod events within X seconds, the set action will be performed

**Usage:** `<@1275521742961508432>nonuke`

### nonuke whitelist

**Description:** Add/Remove users from the whitelist

**Usage:** `<@1275521742961508432>nonuke whitelist`

### nonuke logchannel

**Description:** Set the log channel for Anti-Nuke kicks

**Usage:** `<@1275521742961508432>nonuke logchannel`

### nonuke enable

**Description:** Enable/Disable the NoNuke system

**Usage:** `<@1275521742961508432>nonuke enable`

### nonuke cooldown

**Description:** Cooldown (in seconds) for NoNuke to trigger

**Usage:** `<@1275521742961508432>nonuke cooldown`

### nonuke ignorebots

**Description:** Toggle whether other bots are ignored

**NOTE:** Bot specific roles (the role created when the bot joins) cannot be removed.
If NoNuke is set to strip roles, and a bot triggers it while having an integrated role, NoNuke will fail
to remove the role from it.

**Usage:** `<@1275521742961508432>nonuke ignorebots`

### nonuke action

**Description:** Set the action for the bot to take when NoNuke is triggered

**Actions**
`kick` - kick the user
`ban` - ban the user
`strip` - strip all roles with permissions from user
`notify` - just sends a report to the log channel

**Usage:** `<@1275521742961508432>nonuke action`

### nonuke dm

**Description:** Toggle whether the bot sends the user a DM when a kick or ban action is performed

**Usage:** `<@1275521742961508432>nonuke dm`

### nonuke view

**Description:** View the NoNuke settings

**Usage:** `<@1275521742961508432>nonuke view`

### nonuke overload

**Description:** How many mod actions can be done within the set cooldown

**Mod actions include:**
Kicks & Bans
Channel Creation/Edit/Deletion
Role Creation/Edit/Deletion

**Usage:** `<@1275521742961508432>nonuke overload`

