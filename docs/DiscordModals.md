# DiscordModals Help

### discordmodals

**Description:** Group of commands to use DiscordModals.

**Usage:** `<@1275521742961508432>discordmodals`

### discordmodals list

**Description:** List all Modals of this server or display the settings for a specific one.

**Usage:** `<@1275521742961508432>discordmodals list`

### discordmodals add

**Description:** Add a Modal for a message.

Use YAML syntax to set up everything.

**Example:**
```
[p]discordmodals add <message>
title: Report a bug
button:
  label: Report
  emoji: ⚠️
  style: 4 # blurple = 1, grey = 2, green = 3, red = 4
modal:
  - label: What is the problem?
    style: 2 # short = 1, paragraph = 2
    required: True
    default: None
    placeholder: None
    min_length: None
    max_length: None
channel: general # id, mention, name
anonymous: False
unique_answer: False
messages:
  error: Error!
  submit: Form submitted.
pings: user1, user2, role1, role2
whitelist_roles: role1, role2
blacklist_roles: role3, role4
assign_roles: role5, role6
```
The `emoji`, `style`, `required`, `default`, `placeholder`, `min_length`, `max_length`, `channel`, `anonymous`, `unique_answer`, `messages`, `pings`, `whitelist_roles`, `blacklist_roles` and `assign_roles` are not required.

**Usage:** `<@1275521742961508432>discordmodals add`

### discordmodals remove

**Description:** Remove a Modal for a message.

**Usage:** `<@1275521742961508432>discordmodals remove`

