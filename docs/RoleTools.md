# RoleTools Help

### roletools

**Description:** Commands for creating custom role settings

**Usage:** `<@1275521742961508432>roletools`

### roletools message

**Description:** Commands for sending/editing messages for roletools

**Usage:** `<@1275521742961508432>roletools message`

### roletools message sendselect

**Description:** Send a select menu to a specified channel for role assignment

`<channel>` - the channel to send the button role buttons to.
`[menus]...` - The names of the select menus you want included in the
message up to a maximum of 5.
`<message>` - The message to be included with the select menu.

**Usage:** `<@1275521742961508432>roletools message sendselect`

### roletools message editbutton

**Description:** Edit a bots message to include Role Buttons

`<message>` - The existing message to add role buttons to. Must be a bots message.
`[buttons]...` - The names of the buttons you want to include up to a maximum of 25.

**Usage:** `<@1275521742961508432>roletools message editbutton`

### roletools message sendbutton

**Description:** Send buttons to a specified channel with optional message.

`<channel>` - the channel to send the button role buttons to.
`[buttons]...` - The names of the buttons you want included in the
message up to a maximum of 25.
`<message>` - The message to be included with the buttons.

**Usage:** `<@1275521742961508432>roletools message sendbutton`

### roletools message editselect

**Description:** Edit a bots message to include Role Buttons

`<message>` - The existing message to add role buttons to. Must be a bots message.
`[menus]...` - The names of the select menus you want to include up to a maximum of 5.

**Usage:** `<@1275521742961508432>roletools message editselect`

### roletools message edit

**Description:** Edit a bots message to include Role Buttons

`<message>` - The existing message to add role buttons to. Must be a bots message.
`[buttons]...` - The names of the buttons you want to include up to a maximum of 25.
`[menus]...` - The names of the select menus you want to include up to a maximum of 5.

Note: There is a maximum of 25 slots available on one message. Each menu
uses up 5 slots while each button uses up 1 slot.

**Usage:** `<@1275521742961508432>roletools message edit`

### roletools message send

**Description:** Send a select menu to a specified channel for role assignment

`<channel>` - the channel to send the button role buttons to.
`[buttons]...` - The names of the buttons you want included in the
`[menus]...` - The names of the select menus you want included in the
message up to a maximum of 5.
`<message>` - The message to be included with the select menu.

Note: There is a maximum of 25 slots available on one message. Each menu
uses up 5 slots while each button uses up 1 slot.

**Usage:** `<@1275521742961508432>roletools message send`

### roletools buttons

**Description:** Setup role buttons

**Usage:** `<@1275521742961508432>roletools buttons`

### roletools buttons view

**Description:** View current buttons setup for role assign in this server.

**Usage:** `<@1275521742961508432>roletools buttons view`

### roletools buttons cleanup

**Description:** Check each button that has registered a message still exists and remove buttons with
missing messages.

# Note: This will also potentially cause problems if the button exists in a thread
it will not be found if the thread is archived and subsequently removed.

**Usage:** `<@1275521742961508432>roletools buttons cleanup`

### roletools buttons create

**Description:** Create a role button

- `<name>` - The name of the button for use later in setup.
- `<role>` - The role this button will assign or remove.
- `[extras]`
 - `label:` - The optional label for the button.
 - `emoji:` - The optional emoji used in the button.
 - `style:` - The background button style. Must be one of the following:
   - `primary`
   - `secondary`
   - `success`
   - `danger`
   - `blurple`
   - `grey`
   - `green`
   - `red`

Note: If no label and no emoji are provided the roles name will be used instead.
This name will not update if the role name is changed.

Example:
    `[p]roletools button create role1 @role label: Super fun role style: blurple emoji: 😀`

**Usage:** `<@1275521742961508432>roletools buttons create`

### roletools buttons delete

**Description:** Delete a saved button.

`<name>` - the name of the button you want to delete.

**Usage:** `<@1275521742961508432>roletools buttons delete`

### roletools selfadd

**Description:** Set whether or not a user can apply the role to themselves.

`[true_or_false]` optional boolean of what to set the setting to.
If not provided the current setting will be shown instead.
`<role>` The role you want to set.

**Usage:** `<@1275521742961508432>roletools selfadd`

### roletools select

**Description:** Setup role select menus

**Usage:** `<@1275521742961508432>roletools select`

### roletools select delete

**Description:** Delete a saved select menu.

`<name>` - the name of the select menu you want to delete.

**Usage:** `<@1275521742961508432>roletools select delete`

### roletools select view

**Description:** View current select menus setup for role assign in this server.

**Usage:** `<@1275521742961508432>roletools select view`

### roletools select deleteoption

**Description:** Delete a saved option.

`<name>` - the name of the select option you want to delete.

**Usage:** `<@1275521742961508432>roletools select deleteoption`

### roletools select cleanup

**Description:** Check each select menu that has registered a message still exists and remove buttons with
missing messages.

# Note: This will also potentially cause problems if the button exists in a thread
it will not be found if the thread is archived and subsequently removed.

**Usage:** `<@1275521742961508432>roletools select cleanup`

### roletools select create

**Description:** Create a select menu

- `<name>` - The name for you to use when you send a message with this menu.
- `[options]...` - The select menu options you designated previously.
- `[extras]`
 - `min:` - The minimum number of items from this menu to be selected.
 - `max:` - The maximum number of items from this menu that can be selected.
 (If not provided this will default to the number of options provided.)
 - `placeholder:` - This is the default text on the menu when no option has been
chosen yet.
Example:
    `[p]roletools select create myrolemenu role1 role2 role3 placeholder: Pick your role!`

**Usage:** `<@1275521742961508432>roletools select create`

### roletools select createoption

**Description:** Create a select menu option

- `<name>` - The name of the select option for use later in setup.
- `<role>` - The role this select option will assign or remove.
- `[extras]`
 - `label:` - The optional label for the option, max of 25 characters.
 - `description:` - The description for the option, max of 50 characters.
 - `emoji:` - The optional emoji used in the select option.

Note: If no label and no emoji are provided the roles name will be used instead.
This name will not update if the role name is changed.

Example:
    `[p]roletools select createoption role1 @role label: Super Fun Role emoji: 😀`

**Usage:** `<@1275521742961508432>roletools select createoption`

### roletools select viewoptions

**Description:** View current select menus setup for role assign in this server.

**Usage:** `<@1275521742961508432>roletools select viewoptions`

### roletools atomic

**Description:** Set the atomicity of role assignment.
What this means is that when this is `True` roles will be
applied inidvidually and not cause any errors. When this
is set to `False` roles will be grouped together into one call.

This can cause race conditions if you have other methods of applying
roles setup when set to `False`.

`[true_or_false]` optional boolean of what to set the setting to.
To reset back to the default global rules use `clear`.
If not provided the current setting will be shown instead.

**Usage:** `<@1275521742961508432>roletools atomic`

### roletools autorole

**Description:** Set a role to be automatically applied when a user joins the server.

`[true_or_false]` optional boolean of what to set the setting to.
If not provided the current setting will be shown instead.
`<role>` The role you want to set.

**Usage:** `<@1275521742961508432>roletools autorole`

### roletools include

**Description:** Set role inclusion

**Usage:** `<@1275521742961508432>roletools include`

### roletools include remove

**Description:** Remove role inclusion

`<role>` This is the role a user may acquire you want to set exclusions for.
`<include>` The role(s) currently inclusive you no longer wish to have included

**Usage:** `<@1275521742961508432>roletools include remove`

### roletools include add

**Description:** Add role inclusion (This will add roles if the designated role is acquired
if the designated role is removed the included roles will also be removed
if the included roles are set to selfremovable)

`<role>` This is the role a user may acquire you want to set exclusions for.
`<include>` The role(s) you wish to have added when a user gains the `<role>`

Note: This will only work for roles assigned by this cog.

**Usage:** `<@1275521742961508432>roletools include add`

### roletools include mutual

**Description:** Allow setting roles mutually inclusive to eachother

This is equivalent to individually setting each roles inclusive roles to another
set of roles.

`[role...]` The roles you want to set as mutually inclusive.

**Usage:** `<@1275521742961508432>roletools include mutual`

### roletools forceroleremove

**Description:** Force remove sticky role on one or more users.

`<users>` The users you want to have a forced stickyrole applied to.
`<roles>` The role you want to set.

Note: This is generally only useful for users who have left the server.

**Usage:** `<@1275521742961508432>roletools forceroleremove`

### roletools removerole

**Description:** Removes a role from the designated members.

`<role>` The role you want to give.
`[who...]` Who you want to give the role to. This can include any of the following:```diff
+ Member
    A specified member of the server.
+ Role
    People who already have a specified role.
+ TextChannel
    People who have access to see the channel provided.
Or one of the following:
+ everyone - everyone in the server.
+ here     - everyone who appears online in the server.
+ bots     - all the bots in the server.
+ humans   - all the humans in the server.
```
**Note:** This runs through exclusive and inclusive role checks
which may cause unintended roles to be removed/applied.

**This command is on a cooldown of 10 seconds per member who receives
a role up to a maximum of 1 hour.**

**Usage:** `<@1275521742961508432>roletools removerole`

### roletools sticky

**Description:** Set whether or not a role will be re-applied when a user leaves and rejoins the server.

`[true_or_false]` optional boolean of what to set the setting to.
If not provided the current setting will be shown instead.
`<role>` The role you want to set.

**Usage:** `<@1275521742961508432>roletools sticky`

### roletools required

**Description:** Set role requirements

**Usage:** `<@1275521742961508432>roletools required`

### roletools required any

**Description:** Set the required roles to require any of the roles instead of all of them

`<role>` This is the role a user may acquire you want to set requirements for.
`<require_any>` Either `True` or `False`. If `True` any of the required roles will allow
the user to acquire the `<role>`.

Note: This will only work for roles assigned by this cog.

**Usage:** `<@1275521742961508432>roletools required any`

### roletools required remove

**Description:** Remove role requirements

`<role>` This is the role a user may acquire you want to set requirements for.
`<requires>` The role(s) you wish to have added when a user gains the `<role>`

Note: This will only work for roles assigned by this cog.

**Usage:** `<@1275521742961508432>roletools required remove`

### roletools required add

**Description:** Add role requirements

`<role>` This is the role a user may acquire you want to set requirements for.
`<requires>` The role(s) the user requires before being allowed to gain this role.

Note: This will only work for roles assigned by this cog.

**Usage:** `<@1275521742961508432>roletools required add`

### roletools viewroles

**Description:** View current roletools setup for each role in the server

`[role]` The role you want to see settings for.

**Usage:** `<@1275521742961508432>roletools viewroles`

### roletools globalatomic

**Description:** Set the atomicity of role assignment.
What this means is that when this is `True` roles will be
applied inidvidually and not cause any errors. When this
is set to `False` roles will be grouped together into one call.

This can cause race conditions if you have other methods of applying
roles setup when set to `False`.

`[true_or_false]` optional boolean of what to set the setting to.
If not provided the current setting will be shown instead.

**Usage:** `<@1275521742961508432>roletools globalatomic`

### roletools cost

**Description:** Set the cost to acquire a role.

`[cost]` The price you want to set the role at in bot credits.
Setting this to 0 or lower will remove the cost.
If not provided the current setting will be shown instead.
`<role>` The role you want to set.

**Usage:** `<@1275521742961508432>roletools cost`

### roletools giverole

**Description:** Gives a role to designated members.

`<role>` The role you want to give.
`[who...]` Who you want to give the role to. This can include any of the following:```diff
+ Member
    A specified member of the server.
+ Role
    People who already have a specified role.
+ TextChannel
    People who have access to see the channel provided.
Or one of the following:
+ everyone - everyone in the server.
+ here     - everyone who appears online in the server.
+ bots     - all the bots in the server.
+ humans   - all the humans in the server.
```
**Note:** This runs through exclusive and inclusive role checks
which may cause unintended roles to be removed/applied.

**This command is on a cooldown of 10 seconds per member who receives
a role up to a maximum of 1 hour.**

**Usage:** `<@1275521742961508432>roletools giverole`

### roletools selfrem

**Description:** Set whether or not a user can remove the role from themselves.

`[true_or_false]` optional boolean of what to set the setting to.
If not provided the current setting will be shown instead.
`<role>` The role you want to set.

**Usage:** `<@1275521742961508432>roletools selfrem`

### roletools selfrole

**Description:** Add or remove a defined selfrole

`<role>` The role you want to add or remove.
If you already have the role it will be removed.

**Usage:** `<@1275521742961508432>roletools selfrole`

### roletools forcerole

**Description:** Force a sticky role on one or more users.

`<users>` The users you want to have a forced stickyrole applied to.
`<roles>` The role you want to set.

Note: The only way to remove this would be to manually remove the role from
the user.

**Usage:** `<@1275521742961508432>roletools forcerole`

### roletools reaction

**Description:** Reaction role settings

**Usage:** `<@1275521742961508432>roletools reaction`

### roletools reaction create

**Description:** Create a reaction role

`<message>` can be the channel_id-message_id pair
from copying message ID while holding SHIFT or a message link
`<emoji>` The emoji you want people to react with to get the role.
`<role>` The role you want people to receive for reacting.

**Usage:** `<@1275521742961508432>roletools reaction create`

### roletools reaction bulk

**Description:** Create multiple roles reactions for a single message

`<message>` can be the channel_id-message_id pair
from copying message ID while holding SHIFT or a message link
`[role_emoji...]` Must be a role-emoji pair separated by either `;`, `,`, `|`, or `-`.

Note: Any spaces will be considered a new set of role-emoji pairs, if you
want to specify a role with a space in it without pinging it enclose
the full role-emoji pair in quotes.

e.g. `[p]roletools bulkreact 461417772115558410-821105109097644052 @member-:smile:`
`[p]roletools bulkreact 461417772115558410-821105109097644052 "Super Member-:frown:"`

**Usage:** `<@1275521742961508432>roletools reaction bulk`

### roletools reaction reactroles

**Description:** View current bound roles in the server

**Usage:** `<@1275521742961508432>roletools reaction reactroles`

### roletools reaction cleanup

**Description:** Cleanup old/missing reaction roles and settings.

Note: This will also clear out reaction roles if the bot is just
missing permissions to see the reactions.

**Usage:** `<@1275521742961508432>roletools reaction cleanup`

### roletools reaction remove

**Description:** Remove a reaction role

`<message>` can be the channel_id-message_id pair
from copying message ID while holding SHIFT or a message link
`<emoji>` The emoji you want people to react with to get the role.
`<role>` The role you want people to receive for reacting.

Note: This will not remove the emoji reactions on the message.

**Usage:** `<@1275521742961508432>roletools reaction remove`

### roletools reaction clearreact

**Description:** Clear the reactions for reaction roles. This will remove
all reactions and then re-apply the bots reaction for you.

`<message>` The message you want to clear reactions on.
`[emojis...]` Optional emojis you want to specifically remove.
If no emojis are provided this will clear all the reaction role
emojis the bot has for the message provided.

Note: This will only clear reactions which have a corresponding
reaction role on it.

**Usage:** `<@1275521742961508432>roletools reaction clearreact`

### roletools exclude

**Description:** Set role exclusions

**Usage:** `<@1275521742961508432>roletools exclude`

### roletools exclude add

**Description:** Add role exclusion (This will remove if the designated role is acquired
if the included roles are not selfremovable they will not be removed
and the designated role will not be given)

`<role>` This is the role a user may acquire you want to set exclusions for.
`<exclude>` The role(s) you wish to have removed when a user gains the `<role>`

Note: This will only work for roles assigned by this cog.

**Usage:** `<@1275521742961508432>roletools exclude add`

### roletools exclude mutual

**Description:** Allow setting roles mutually exclusive to eachother

This is equivalent to individually setting each roles exclusive roles to another
set of roles.

`[role...]` The roles you want to set as mutually exclusive.

**Usage:** `<@1275521742961508432>roletools exclude mutual`

### roletools exclude remove

**Description:** Remove role exclusion

`<role>` This is the role a user may acquire you want to set exclusions for.
`<exclude>` The role(s) currently excluded you no longer wish to have excluded

**Usage:** `<@1275521742961508432>roletools exclude remove`

