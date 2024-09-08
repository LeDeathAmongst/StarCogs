# Filter Help

### filterset

**Description:** Base command to manage filter settings.

**Usage:** `<@1275521742961508432>filterset`

### filterset ban

**Description:** Set the filter's autoban conditions.

Users will be banned if they send `<count>` filtered words in
`<timeframe>` seconds.

Set both to zero to disable autoban.

Examples:
- `[p]filterset ban 5 5` - Ban users who say 5 filtered words in 5 seconds.
- `[p]filterset ban 2 20` - Ban users who say 2 filtered words in 20 seconds.

**Arguments:**

- `<count>` The amount of filtered words required to trigger a ban.
- `<timeframe>` The period of time in which too many filtered words will trigger a ban.

**Usage:** `<@1275521742961508432>filterset ban`

### filterset defaultname

**Description:** Set the nickname for users with a filtered name.

Note that this has no effect if filtering names is disabled
(to toggle, run `[p]filter names`).

The default name used is *John Doe*.

Example:
- `[p]filterset defaultname Missingno`

**Arguments:**

- `<name>` The new nickname to assign.

**Usage:** `<@1275521742961508432>filterset defaultname`

### filter

**Description:** Base command to add or remove words from the server filter.

Use double quotes to add or remove sentences.

**Usage:** `<@1275521742961508432>filter`

### filter clear

**Description:** Clears this server's filter list.

**Usage:** `<@1275521742961508432>filter clear`

### filter names

**Description:** Toggle name and nickname filtering.

This is disabled by default.

**Usage:** `<@1275521742961508432>filter names`

### filter delete

**Description:** Remove words from the filter.

Use double quotes to remove sentences.

Examples:
- `[p]filter remove word1 word2 word3`
- `[p]filter remove "This is a sentence"`

**Arguments:**

- `[words...]` The words or sentences to no longer filter.

**Usage:** `<@1275521742961508432>filter delete`

### filter channel

**Description:** Base command to add or remove words from the channel filter.

Use double quotes to add or remove sentences.

**Usage:** `<@1275521742961508432>filter channel`

### filter channel add

**Description:** Add words to the filter.

Use double quotes to add sentences.

Examples:
- `[p]filter channel add #channel word1 word2 word3`
- `[p]filter channel add #channel "This is a sentence"`

**Arguments:**

- `<channel>` The text, voice, stage, or forum channel to add filtered words to.
- `[words...]` The words or sentences to filter.

**Usage:** `<@1275521742961508432>filter channel add`

### filter channel list

**Description:** Send a list of the channel's filtered words.

**Usage:** `<@1275521742961508432>filter channel list`

### filter channel clear

**Description:** Clears this channel's filter list.

**Usage:** `<@1275521742961508432>filter channel clear`

### filter channel delete

**Description:** Remove words from the filter.

Use double quotes to remove sentences.

Examples:
- `[p]filter channel remove #channel word1 word2 word3`
- `[p]filter channel remove #channel "This is a sentence"`

**Arguments:**

- `<channel>` The text, voice, stage, or forum channel to add filtered words to.
- `[words...]` The words or sentences to no longer filter.

**Usage:** `<@1275521742961508432>filter channel delete`

### filter add

**Description:** Add words to the filter.

Use double quotes to add sentences.

Examples:
- `[p]filter add word1 word2 word3`
- `[p]filter add "This is a sentence"`

**Arguments:**

- `[words...]` The words or sentences to filter.

**Usage:** `<@1275521742961508432>filter add`

### filter list

**Description:** Send a list of this server's filtered words.

**Usage:** `<@1275521742961508432>filter list`

