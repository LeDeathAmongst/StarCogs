# RolesButtons Help

### rolesbuttons

**Description:** Group of commands to use RolesButtons.

**Usage:** `<@1275521742961508432>rolesbuttons`

### rolesbuttons list

**Description:** List all roles-buttons of this server or display the settings for a specific one.

**Usage:** `<@1275521742961508432>rolesbuttons list`

### rolesbuttons add

**Description:** Add a role-button for a message.

(Use the number for the color.)
• `primary`: 1
• `secondary`: 2
• `success`: 3
• `danger`: 4
# Aliases
• `blurple`: 1
• `grey`: 2
• `gray`: 2
• `green`: 3
• `red`: 4

**Usage:** `<@1275521742961508432>rolesbuttons add`

### rolesbuttons remove

**Description:** Remove a role-button for a message.

Use `[p]rolesbuttons list <message>` to find the config identifier.

**Usage:** `<@1275521742961508432>rolesbuttons remove`

### rolesbuttons clear

**Description:** Clear all roles-buttons for a message.

**Usage:** `<@1275521742961508432>rolesbuttons clear`

### rolesbuttons bulk

**Description:** Add roles-buttons for a message.

```[p]rolesbuttons bulk <message> :reaction1:|@role1 :reaction2:|@role2 :reaction3:|@role3```

**Usage:** `<@1275521742961508432>rolesbuttons bulk`

### rolesbuttons mode

**Description:** Choose a mode for the roles-buttons of a message.

Type `add_or_remove`:
- Users get the role if they do not already have it, or lose it.
Type `add_only`:
- Users can only get the role, but only manual action will remove it.
Type `remove_only`:
- Users can only lose a role, and will not be able to get it again without a manual action.
Type `replace`:
- Same as add_or_remove, but the roles from this message will be mutually exclusive, and getting one will remove the previous.

**Usage:** `<@1275521742961508432>rolesbuttons mode`

