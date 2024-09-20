# WelcomeCount Help

### welcomecount

**Description:** Manage settings for WelcomeCount.

**Usage:** `<@1275521742961508432>welcomecount`

### welcomecount toggle

**Description:** Toggle welcome messages in this channel.

**Usage:** `<@1275521742961508432>welcomecount toggle`

### welcomecount joinrole

**Description:** Set a role which a user must receive before they're welcomed.

This means that, instead of the welcome message being sent when
the user joins the server, the welcome message will be sent when
they receive a particular role.

Use `[p]welcomecount joinrole disable` to revert to the default
behaviour.

**Usage:** `<@1275521742961508432>welcomecount joinrole`

### welcomecount deletelast

**Description:** Toggle deleting the previous welcome message in this channel.

When enabled, the last message is deleted *only* if it was sent on
the same day as the new welcome message.

**Usage:** `<@1275521742961508432>welcomecount deletelast`

### welcomecount message

**Description:** Set the bot's welcome message.

This message can be formatted using these parameters:
    mention - Mention the user who joined
    username - The user's display name
    server - The name of the server
    count - The number of users who joined today.
    plural - Empty if `count` is 1. 's' otherwise.
    total - The total number of users in the server.
To format the welcome message with the above parameters, include them
in your message surrounded by curly braces {}.

**Usage:** `<@1275521742961508432>welcomecount message`

