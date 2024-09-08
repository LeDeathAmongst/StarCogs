# AIEmote Help

### aiemote

**Description:** Totally not glorified sentiment analysis™

Picks a reaction for a message using gpt-3.5-turbo

To get started, please add a channel to the whitelist with:
`[p]aiemote allow <#channel>`

**Usage:** `<@1275521742961508432>aiemote`

### aiemote optin

**Description:** Opt in of sending your message to OpenAI (bot-wide)

This will allow the bot to react to your messages

**Usage:** `<@1275521742961508432>aiemote optin`

### aiemote remove

**Description:** Remove a channel from the whitelist

*Arguments*
- `<channel>` The mention of channel

**Usage:** `<@1275521742961508432>aiemote remove`

### aiemote allow

**Description:** Add a channel to the whitelist

*Arguments*
- `<channel>` The mention of channel

**Usage:** `<@1275521742961508432>aiemote allow`

### aiemote optout

**Description:** Opt out of sending your message to OpenAI (bot-wide)

The bot will no longer react to your messages

**Usage:** `<@1275521742961508432>aiemote optout`

### aiemote whitelist

**Description:** List all channels in the whitelist 

**Usage:** `<@1275521742961508432>aiemote whitelist`

### aiemote optinbydefault

**Description:** Toggles whether users are opted in by default in this server

This command is disabled for servers with more than 150 members.

**Usage:** `<@1275521742961508432>aiemote optinbydefault`

### aiemoteowner

**Description:** Owner only commands for aiemote
        

**Usage:** `<@1275521742961508432>aiemoteowner`

### aiemoteowner instruction

**Description:** Add additonal (prompting) instruction for the langauge model when picking an emoji

*Arguments*
- `<instruction>` The extra instruction to use

**Usage:** `<@1275521742961508432>aiemoteowner instruction`

### aiemoteowner sremove

**Description:** Remove an emoji from this current server list

*Arguments*
- `<emoji>` The emoji to remove

**Usage:** `<@1275521742961508432>aiemoteowner sremove`

### aiemoteowner reset

**Description:** Reset *all* settings

**Usage:** `<@1275521742961508432>aiemoteowner reset`

### aiemoteowner sadd

**Description:** Add an emoji to this current server list

*Arguments*
- `<emoji>` The emoji to add
- `<description>` A description of the emoji to be used by OpenAI

**Usage:** `<@1275521742961508432>aiemoteowner sadd`

### aiemoteowner config

**Description:** List all emojis in the global list (and current server list)
        

**Usage:** `<@1275521742961508432>aiemoteowner config`

### aiemoteowner add

**Description:** Add an emoji to the global list

*Arguments*
- `<emoji>` The emoji to add
- `<description>` A description of the emoji to be used by OpenAI

**Usage:** `<@1275521742961508432>aiemoteowner add`

### aiemoteowner percent

**Description:** Set the chance that the bot will react to a message (for all servers bot is in)

*Arguments*
- `<percent>` The percent chance that the bot will react to a message

**Usage:** `<@1275521742961508432>aiemoteowner percent`

### aiemoteowner remove

**Description:** Remove an emoji from the global list

*Arguments*
- `<emoji>` The emoji to remove

**Usage:** `<@1275521742961508432>aiemoteowner remove`

