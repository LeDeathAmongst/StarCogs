# AutoMod Help

### automod

**Description:** Commnads for interacting with automod

**Usage:** `<@1275521742961508432>automod`

### automod create

**Description:** Create automod rules, triggers, and actions

**Usage:** `<@1275521742961508432>automod create`

### automod create trigger

**Description:** Create a saved trigger for use in automod Rules.

- `<name>` The name of this trigger for reference later.
Usage: `<trigger>`
- `allows:` A space separated list of words to allow.
- `keywords:` A space separated list of words to filter.
- `mentions:` The number of user/role mentions that would trigger this rule (0-50).
- `presets:` Any combination of discord presets. e.g. `profanity`, `sexual_content`, or `slurs`.
- `regex:` A space separated list of regex patterns to include.
Note: If you want to use `mentions` you cannot also use `presets`, `keywords` or
`regex` in the same trigger. Likewise if you use any `presets` you cannot
use `keywords`, `regex`, or `mentions`.
Examples:
    `[p]automod create trigger mytrigger regex: ^b(a|@)dw(o|0)rd(s|5)$`

**Usage:** `<@1275521742961508432>automod create trigger`

### automod create action

**Description:** Create a saved action for use in automod Rules.

- `<name>` The name of this action for reference later.
Usage: `<action>`
- `message:` The message to send to a user when triggered.
- `channel:` The channel to send a notification to.
- `duration:` How long to timeout the user for. Max 28 days.
Only one of these options can be applied at a time.
Examples:
    `[p]automod create action grumpyuser message: You're being too grumpy`
    `[p]automod create action notifymods channel: #modlog`
    `[p]automod create action 2hrtimeout duration: 2 hours`

**Usage:** `<@1275521742961508432>automod create action`

### automod create rule

**Description:** Create an automod rule in the server

Usage:
- `trigger:` The name of a saved trigger.
- `actions:` The name(s) of saved actions.
- `enabled:` yes/true/t to enable this rule right away.
- `roles:` The roles that are exempt from this rule.
- `channels:` The channels that are exempt from this rule.
- `reason:` An optional reason for creating this rule.

Example:
    `[p]automod create rule trigger: mytrigger actions: timeoutuser notifymods enabled: true roles: @mods`
    Will create an automod rule with the saved trigger `mytrigger` and
    the saved actions `timeoutuser` and `notifymods`.

**Usage:** `<@1275521742961508432>automod create rule`

### automod actions

**Description:** View the servers saved automod actions

**Usage:** `<@1275521742961508432>automod actions`

### automod triggers

**Description:** View the servers saved automod triggers

**Usage:** `<@1275521742961508432>automod triggers`

### automod rules

**Description:** View the servers current automod rules

**Usage:** `<@1275521742961508432>automod rules`

