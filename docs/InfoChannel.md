# InfoChannel Help

### infochannel

**Description:** Toggle info channel for this server

**Usage:** `<@1275521742961508432>infochannel`

### infochannelset

**Description:** Toggle different types of infochannels

**Usage:** `<@1275521742961508432>infochannelset`

### infochannelset togglerole

**Description:** Toggle an infochannel that shows the count of users with the specified role

**Usage:** `<@1275521742961508432>infochannelset togglerole`

### infochannelset togglechannel

**Description:** Toggles the infochannel for the specified channel type.

Valid Types are:
- `members`: Total members on the server
- `humans`: Total members that aren't bots
- `boosters`: Total amount of boosters
- `bots`: Total bots
- `roles`: Total number of roles
- `channels`: Total number of channels excluding infochannels,
- `online`: Total online members,
- `offline`: Total offline members,

**Usage:** `<@1275521742961508432>infochannelset togglechannel`

### infochannelset rolename

**Description:** Change the name of the infochannel for specific roles.

{count} must be used to display number members with the given role.
{role} can be used for the roles name.
Leave blank to set back to default.

Default is set to: `{role}: {count}`

Examples:
- `[p]infochannelset rolename @Patrons {role}: {count}`
- `[p]infochannelset rolename Elite {count} members with {role} role`
- `[p]infochannelset rolename "Space Role" Total boosters: {count}`

Warning: This command counts against the channel update rate limit and may be queued.

**Usage:** `<@1275521742961508432>infochannelset rolename`

### infochannelset name

**Description:** Change the name of the infochannel for the specified channel type.

{count} must be used to display number of total members in the server.
Leave blank to set back to default.

Examples:
- `[p]infochannelset name members Cool Cats: {count}`
- `[p]infochannelset name bots {count} Robot Overlords`

Valid Types are:
- `members`: Total members on the server
- `humans`: Total members that aren't bots
- `boosters`: Total amount of boosters
- `bots`: Total bots
- `roles`: Total number of roles
- `channels`: Total number of channels excluding infochannels
- `online`: Total online members
- `offline`: Total offline members

Warning: This command counts against the channel update rate limit and may be queued.

**Usage:** `<@1275521742961508432>infochannelset name`

