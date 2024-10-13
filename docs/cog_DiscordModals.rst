DiscordModals
=============

A cog to use Discord Modals, forms with graphic interface!

<<<<<<< HEAD
# <@1275521742961508432>discordmodals (Hybrid Command)
Group of commands to use DiscordModals.<br/>
 - Usage: `<@1275521742961508432>discordmodals`
=======
# ,discordmodals (Hybrid Command)
Group of commands to use DiscordModals.<br/>
 - Usage: `,discordmodals`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/discordmodals`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>discordmodals purge (Hybrid Command)
Clear all Modals for a server.<br/>
 - Usage: `<@1275521742961508432>discordmodals purge`
=======
## ,discordmodals remove (Hybrid Command)
Remove a Modal for a message.<br/>
 - Usage: `,discordmodals remove <message>`
 - Slash Usage: `/discordmodals remove <message>`
 - Aliases: `-`
 - Checks: `server_only`


## ,discordmodals purge (Hybrid Command)
Clear all Modals for a server.<br/>
 - Usage: `,discordmodals purge`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/discordmodals purge`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>discordmodals add (Hybrid Command)
=======
## ,discordmodals add (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Add a Modal for a message.<br/>

Use YAML syntax to set up everything.<br/>

**Example:**<br/>
```
<<<<<<< HEAD
<@1275521742961508432>discordmodals add <message>
=======
,discordmodals add <message>
>>>>>>> 9e308722 (Revamped and Fixed)
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
The `emoji`, `style`, `required`, `default`, `placeholder`, `min_length`, `max_length`, `channel`, `anonymous`, `unique_answer`, `messages`, `pings`, `whitelist_roles`, `blacklist_roles` and `assign_roles` are not required.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>discordmodals add <message> <argument>`
=======
 - Usage: `,discordmodals add <message> <argument>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/discordmodals add <message> <argument>`
 - Aliases: `+`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>discordmodals remove (Hybrid Command)
Remove a Modal for a message.<br/>
 - Usage: `<@1275521742961508432>discordmodals remove <message>`
 - Slash Usage: `/discordmodals remove <message>`
 - Aliases: `-`
 - Checks: `server_only`


## <@1275521742961508432>discordmodals list (Hybrid Command)
List all Modals of this server or display the settings for a specific one.<br/>
 - Usage: `<@1275521742961508432>discordmodals list [message=None]`
=======
## ,discordmodals list (Hybrid Command)
List all Modals of this server or display the settings for a specific one.<br/>
 - Usage: `,discordmodals list [message=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/discordmodals list [message=None]`
 - Checks: `server_only`


