# LinkWarner Help

### linkwarner

**Description:** Settings for LinkWarner cog.

**Usage:** `<@1275521742961508432>linkwarner`

### linkwarner domains

**Description:** Configuration for allowed/disallowed domains in the guild.

**Usage:** `<@1275521742961508432>linkwarner domains`

### linkwarner domains add

**Description:** Add domains to the domains list.

Note: The cog is using exact matching for domain names
which means that domain names like youtube.com and www.youtube.com
are treated as 2 different domains.

Example:
`[p]linkwarner domains add google.com youtube.com`

**Usage:** `<@1275521742961508432>linkwarner domains add`

### linkwarner domains clear

**Description:** Clear domains from the domains list.

**Usage:** `<@1275521742961508432>linkwarner domains clear`

### linkwarner domains remove

**Description:** Remove domains from the domains list.

Example:
`[p]linkwarner domains remove youtube.com discord.com`

**Usage:** `<@1275521742961508432>linkwarner domains remove`

### linkwarner domains setmode

**Description:** Change current domains list mode.

Available modes:
`1` - Only domains on the domains list can be sent.
`2` - All domains can be sent except the ones on the domains list.

**Usage:** `<@1275521742961508432>linkwarner domains setmode`

### linkwarner unsetmessage

**Description:** Unset link warning message.

**Usage:** `<@1275521742961508432>linkwarner unsetmessage`

### linkwarner usedms

**Description:** Set if LinkWarner should use DMs for warning messages.

Note: This is NOT recommended as the user might block the bot or all DMs
from the server and the warning might not get sent to the offender at all.
This also means that the bot is more likely to get ratelimited for repeatedly
trying to DM the user when they spam links.

If you're trying to minimize spam that the warning messages cause,
you should consider enabling delete delay instead.

**Usage:** `<@1275521742961508432>linkwarner usedms`

### linkwarner deletedelay

**Description:** Set the delete delay (in seconds) for the warning message.

Use `[p]linkwarner deletedelay disable` to disable auto-deletion.

Note: This does not work when the warning messages are sent through DMs.

**Usage:** `<@1275521742961508432>linkwarner deletedelay`

### linkwarner deletedelay disable

**Description:** Disable auto-deletion of the warning messages.

**Usage:** `<@1275521742961508432>linkwarner deletedelay disable`

### linkwarner setmessage

**Description:** Set link warning message.

Those fields will get replaced automatically:
$mention - Mention the user who sent the message with a link
$username - The user's display name
$server - The name of the server

**Usage:** `<@1275521742961508432>linkwarner setmessage`

### linkwarner channel

**Description:** Channel-specific settings for LinkWarner.

**Usage:** `<@1275521742961508432>linkwarner channel`

### linkwarner channel setmessage

**Description:** Set link warning message for provided channel.

Those fields will get replaced automatically:
$mention - Mention the user who sent the message with a link
$username - The user's display name
$server - The name of the server

**Usage:** `<@1275521742961508432>linkwarner channel setmessage`

### linkwarner channel domains

**Description:** Configuration for allowed/disallowed domains in the specific channel.

**Usage:** `<@1275521742961508432>linkwarner channel domains`

### linkwarner channel domains setmode

**Description:** Change current domains list mode.

Available modes:
`0` - Inherit the guild setting and use domains
      from both guild's and channel's domain list.
`1` - Only domains on the channel's domains list can be sent.
`2` - All domains can be sent except the ones on the channel's domains list.

**Usage:** `<@1275521742961508432>linkwarner channel domains setmode`

### linkwarner channel domains remove

**Description:** Remove domains from the domains list of the provided channel.

Example:
`[p]linkwarner channel domains remove #channel youtube.com discord.com`

**Usage:** `<@1275521742961508432>linkwarner channel domains remove`

### linkwarner channel domains add

**Description:** Add domains to the domains list of the provided channel.

Note: The cog is using exact matching for domain names
which means that domain names like youtube.com and www.youtube.com
are treated as 2 different domains.

Example:
`[p]linkwarner channel domains add #channel youtube.com discord.com`

**Usage:** `<@1275521742961508432>linkwarner channel domains add`

### linkwarner channel domains clear

**Description:** Clear domains from the domains list of the provided channel.

**Usage:** `<@1275521742961508432>linkwarner channel domains clear`

### linkwarner channel ignore

**Description:** Set if LinkWarner should ignore links in provided channel.

**Usage:** `<@1275521742961508432>linkwarner channel ignore`

### linkwarner channel showsettings

**Description:** Show settings for the given channel.

**Usage:** `<@1275521742961508432>linkwarner channel showsettings`

### linkwarner channel unsetmessage

**Description:** Unset link warning message for provided channel.

**Usage:** `<@1275521742961508432>linkwarner channel unsetmessage`

### linkwarner excludedroles

**Description:** Settings for roles that are excluded from getting filtered.

**Usage:** `<@1275521742961508432>linkwarner excludedroles`

### linkwarner excludedroles add

**Description:** Add roles that will be excluded from getting filtered.

**Usage:** `<@1275521742961508432>linkwarner excludedroles add`

### linkwarner excludedroles remove

**Description:** Remove roles that will be excluded from getting filtered.

**Usage:** `<@1275521742961508432>linkwarner excludedroles remove`

### linkwarner showsettings

**Description:** Show settings for the current guild.

**Usage:** `<@1275521742961508432>linkwarner showsettings`

### linkwarner state

**Description:** Set if LinkWarner should be enabled for this guild.

If used without a setting, this will show the current state.

**Usage:** `<@1275521742961508432>linkwarner state`

