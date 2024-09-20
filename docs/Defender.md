# Defender Help

### dset

**Description:** Defender system settings

**Usage:** `<@1275521742961508432>dset`

### dset joinmonitor

**Description:** Join monitor auto module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset joinmonitor`

### dset joinmonitor wdchecks

**Description:** Implement advanced Warden based checks

Issuing this command with no arguments will show the current checks
Passing 'remove' will remove existing checks

**Usage:** `<@1275521742961508432>dset joinmonitor wdchecks`

### dset joinmonitor verificationlevel

**Description:** Raises the server's verification level on raids

You can find a full description of Discord's verification levels in
the server's settings "Moderation" tab.

Verification levels:
0 - No action
1 - Low: verified email
2 - Medium: must be registered for longer than 5 minutes
3 - High: must be a member of this server for longer than 10 minutes
4 - Highest: must have a verified phone on their Discord account

**Usage:** `<@1275521742961508432>dset joinmonitor verificationlevel`

### dset joinmonitor notifynew

**Description:** Enables notifications for users younger than X hours

Use 0 hours to disable notifications

**Usage:** `<@1275521742961508432>dset joinmonitor notifynew`

### dset joinmonitor users

**Description:** Sets users (X users joined in Y minutes)

**Usage:** `<@1275521742961508432>dset joinmonitor users`

### dset joinmonitor enable

**Description:** Toggles join monitor

**Usage:** `<@1275521742961508432>dset joinmonitor enable`

### dset joinmonitor minutes

**Description:** Sets minutes (X users joined in Y minutes)

**Usage:** `<@1275521742961508432>dset joinmonitor minutes`

### dset voteout

**Description:** Voteout manual module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset voteout`

### dset voteout action

**Description:** Sets action (ban, kick, softban, punish)

**Usage:** `<@1275521742961508432>dset voteout action`

### dset voteout rank

**Description:** Sets target rank

**Usage:** `<@1275521742961508432>dset voteout rank`

### dset voteout wipe

**Description:** Sets how many days worth of messages to delete if the action is ban

Setting 0 will not delete any message

**Usage:** `<@1275521742961508432>dset voteout wipe`

### dset voteout enable

**Description:** Toggles voteout

**Usage:** `<@1275521742961508432>dset voteout enable`

### dset voteout votes

**Description:** Sets required votes number for it to pass

**Usage:** `<@1275521742961508432>dset voteout votes`

### dset emergency

**Description:** Emergency mode configuration

See [p]defender status for more information about emergency mode

**Usage:** `<@1275521742961508432>dset emergency`

### dset emergency modules

**Description:** Sets emergency modules

Emergency modules will be rendered available to helper roles
during emergency mode. Selecting no modules to this command will
disable emergency mode.
Available emergency modules: voteout, vaporize, silence

**Usage:** `<@1275521742961508432>dset emergency modules`

### dset emergency minutes

**Description:** Sets max inactivity minutes for staff

After X minutes of inactivity following an alert emergency
mode will be engaged and helper roles will be able to use
the emergency modules.

**Usage:** `<@1275521742961508432>dset emergency minutes`

### dset rank3

**Description:** Rank 3 configuration

See [p]defender status for more information about this rank

**Usage:** `<@1275521742961508432>dset rank3`

### dset rank3 minmessages

**Description:** Minimum messages required to reach Rank 3

**Usage:** `<@1275521742961508432>dset rank3 minmessages`

### dset rank3 joineddays

**Description:** Days since join required to be considered Rank 3

**Usage:** `<@1275521742961508432>dset rank3 joineddays`

### dset silence

**Description:** Silence manual module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset silence`

### dset silence enable

**Description:** Toggle silence manual module

**Usage:** `<@1275521742961508432>dset silence enable`

### dset vaporize

**Description:** Vaporize manual module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset vaporize`

### dset vaporize enable

**Description:** Toggle vaporize manual module

**Usage:** `<@1275521742961508432>dset vaporize enable`

### dset vaporize maxtargets

**Description:** Sets the maximum amount of targets (1-999)

By default only a maximum of 15 users can be vaporized at once

**Usage:** `<@1275521742961508432>dset vaporize maxtargets`

### dset raiderdetection

**Description:** Raider detection auto module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset raiderdetection`

### dset raiderdetection minutes

**Description:** Sets minutes (User posted X messages in Y minutes)

**Usage:** `<@1275521742961508432>dset raiderdetection minutes`

### dset raiderdetection messages

**Description:** Sets messages (User posted X messages in Y minutes)

**Usage:** `<@1275521742961508432>dset raiderdetection messages`

### dset raiderdetection enable

**Description:** Toggles raider detection

**Usage:** `<@1275521742961508432>dset raiderdetection enable`

### dset raiderdetection wdchecks

**Description:** Implement advanced Warden based checks

Issuing this command with no arguments will show the current checks
Passing 'remove' will remove existing checks

**Usage:** `<@1275521742961508432>dset raiderdetection wdchecks`

### dset raiderdetection wipe

**Description:** Sets how many days worth of messages to delete if the action is ban

Setting 0 will not delete any message

**Usage:** `<@1275521742961508432>dset raiderdetection wipe`

### dset raiderdetection action

**Description:** Sets action (ban, kick, softban, punish or none (notify only))

**Usage:** `<@1275521742961508432>dset raiderdetection action`

### dset raiderdetection rank

**Description:** Sets target rank

**Usage:** `<@1275521742961508432>dset raiderdetection rank`

### dset commentanalysis

**Description:** Comment analysis configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset commentanalysis`

### dset commentanalysis deletemessage

**Description:** Toggles whether to delete the offending message

**Usage:** `<@1275521742961508432>dset commentanalysis deletemessage`

### dset commentanalysis token

**Description:** Sets Perspective API token

https://developers.perspectiveapi.com/s/docs

**Usage:** `<@1275521742961508432>dset commentanalysis token`

### dset commentanalysis enable

**Description:** Toggles comment analysis

**Usage:** `<@1275521742961508432>dset commentanalysis enable`

### dset commentanalysis wipe

**Description:** Sets how many days worth of messages to delete if the action is ban

Setting 0 will not delete any message

**Usage:** `<@1275521742961508432>dset commentanalysis wipe`

### dset commentanalysis reason

**Description:** Sets a reason for the action (modlog use)

**Usage:** `<@1275521742961508432>dset commentanalysis reason`

### dset commentanalysis action

**Description:** Sets action (ban, kick, softban, punish or none (notification only))

**Usage:** `<@1275521742961508432>dset commentanalysis action`

### dset commentanalysis rank

**Description:** Sets target rank

**Usage:** `<@1275521742961508432>dset commentanalysis rank`

### dset commentanalysis threshold

**Description:** Sets the threshold that will trigger CA's action (20-100)

**Usage:** `<@1275521742961508432>dset commentanalysis threshold`

### dset commentanalysis attributes

**Description:** Setup the attributes that CA will check

**Usage:** `<@1275521742961508432>dset commentanalysis attributes`

### dset commentanalysis wdchecks

**Description:** Implement advanced Warden based checks

Issuing this command with no arguments will show the current checks
Passing 'remove' will remove existing checks

**Usage:** `<@1275521742961508432>dset commentanalysis wdchecks`

### dset alert

**Description:** Alert manual module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset alert`

### dset alert enable

**Description:** Toggle alert manual module

**Usage:** `<@1275521742961508432>dset alert enable`

### dset importfrom

**Description:** Import the configuration from another server

This is permitted only if the command issuer is admin in both servers

**Usage:** `<@1275521742961508432>dset importfrom`

### dset general

**Description:** Defender general settings

**Usage:** `<@1275521742961508432>dset general`

### dset general messagecachecap

**Description:** Sets the maximum # of messages to cache for each user / channel

**Usage:** `<@1275521742961508432>dset general messagecachecap`

### dset general helperroles

**Description:** Sets the helper roles

See [p]defender status for more information about these roles

**Usage:** `<@1275521742961508432>dset general helperroles`

### dset general trustedroles

**Description:** Sets the trusted roles

Users belonging to this role will be classified as Rank 1

**Usage:** `<@1275521742961508432>dset general trustedroles`

### dset general messagecacheexpire

**Description:** Sets how long a message should be cached before being discarded

**Usage:** `<@1275521742961508432>dset general messagecacheexpire`

### dset general reset

**Description:** Resets Defender configuration for this server

**Usage:** `<@1275521742961508432>dset general reset`

### dset general countmessages

**Description:** Toggles message count (and rank 4)

**Usage:** `<@1275521742961508432>dset general countmessages`

### dset general notifyrole

**Description:** Sets the role that will be pinged in case of alerts

**Usage:** `<@1275521742961508432>dset general notifyrole`

### dset general punishmessage

**Description:** Sets the messages that I will send after assigning the punish role

Supports context variables. You can add the following to your message:
$user -> User's name + tag
$user_name -> User's name
$user_display -> User's nickname if set or user's name
$user_id -> User's id
$user_mention -> User's mention
$user_nickname -> User's nickname if set or 'None'

**Usage:** `<@1275521742961508432>dset general punishmessage`

### dset general punishrole

**Description:** Sets the role that will be assigned to misbehaving users

Note: this will only be assigned if the 'action' of a module
is set to 'punish'.

**Usage:** `<@1275521742961508432>dset general punishrole`

### dset general enable

**Description:** Toggle defender system

**Usage:** `<@1275521742961508432>dset general enable`

### dset general notifychannel

**Description:** Sets the channel where notifications will be sent

This channel should preferably be staff readable only as it could
potentially contain sensitive info

**Usage:** `<@1275521742961508432>dset general notifychannel`

### dset invitefilter

**Description:** Invite filter auto module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset invitefilter`

### dset invitefilter rank

**Description:** Sets target rank

**Usage:** `<@1275521742961508432>dset invitefilter rank`

### dset invitefilter wdchecks

**Description:** Implement advanced Warden based checks

Issuing this command with no arguments will show the current checks
Passing 'remove' will remove existing checks

**Usage:** `<@1275521742961508432>dset invitefilter wdchecks`

### dset invitefilter deletemessage

**Description:** Toggles whether to delete the invite's message

**Usage:** `<@1275521742961508432>dset invitefilter deletemessage`

### dset invitefilter excludeowninvites

**Description:** Excludes this server's invites from the filter

**Usage:** `<@1275521742961508432>dset invitefilter excludeowninvites`

### dset invitefilter enable

**Description:** Toggle invite filter

**Usage:** `<@1275521742961508432>dset invitefilter enable`

### dset invitefilter action

**Description:** Sets action (ban, kick, softban, punish or none (deletion only))

**Usage:** `<@1275521742961508432>dset invitefilter action`

### dset warden

**Description:** Warden auto module configuration

See [p]defender status for more information about this module

**Usage:** `<@1275521742961508432>dset warden`

### dset warden uploadmaxsize

**Description:** Sets the maximum allowed size for Warden rules upload

Reccommended size is 3KB

**Usage:** `<@1275521742961508432>dset warden uploadmaxsize`

### dset warden periodicallowed

**Description:** Toggles the ability to globally create periodic rules

Periodic rules are rules that can be scheduled to run against
an entire server userbase on an interval between 5 minutes and 24 hours

**Usage:** `<@1275521742961508432>dset warden periodicallowed`

### dset warden enable

**Description:** Toggles warden

**Usage:** `<@1275521742961508432>dset warden enable`

### dset warden regexsafetychecks

**Description:** Globally toggles the safety checks for user defined regex

These checks disable Warden rules with regex that takes too long to be evaluated. It is
recommended to keep this feature enabled.

**Usage:** `<@1275521742961508432>dset warden regexsafetychecks`

### dset warden regexallowed

**Description:** Toggles the ability to globally create rules with user defined regex

**Usage:** `<@1275521742961508432>dset warden regexallowed`

### defender

**Description:** Defender commands reserved to staff

**Usage:** `<@1275521742961508432>defender`

### defender messages

**Description:** Access recorded messages of users / channels

**Usage:** `<@1275521742961508432>defender messages`

### defender messages user

**Description:** Shows recent messages of a user

**Usage:** `<@1275521742961508432>defender messages user`

### defender messages channel

**Description:** Shows recent messages of a channel

**Usage:** `<@1275521742961508432>defender messages channel`

### defender messages exportuser

**Description:** Exports recent messages of a user to a file

**Usage:** `<@1275521742961508432>defender messages exportuser`

### defender messages exportchannel

**Description:** Exports recent messages of a channel to a file

**Usage:** `<@1275521742961508432>defender messages exportchannel`

### defender warden

**Description:** Warden rules management

See [p]defender status for more information about Warden

**Usage:** `<@1275521742961508432>defender warden`

### defender warden show

**Description:** Shows a rule

**Usage:** `<@1275521742961508432>defender warden show`

### defender warden list

**Description:** Lists existing rules

**Usage:** `<@1275521742961508432>defender warden list`

### defender warden add

**Description:** Adds a new rule

**Usage:** `<@1275521742961508432>defender warden add`

### defender warden removeall

**Description:** Removes all rules

**Usage:** `<@1275521742961508432>defender warden removeall`

### defender warden memory

**Description:** Shows or resets the memory of Warden

Can be filtered. Supports wildcards (* and ?)

**Usage:** `<@1275521742961508432>defender warden memory`

### defender warden run

**Description:** Runs a rule against the whole userbase

Confirmation is asked before execution.

**Usage:** `<@1275521742961508432>defender warden run`

### defender warden debug

**Description:** Simulate and give a detailed summary of an event

A Warden event must be passed with the proper target ID (user or local message)

When this command is issued all the rules registered to the event will be
processed in a safe way against the target, if any.
If the target satisfies the conditions, *only* the heatpoint related actions
will be carried on.
The heatpoint actions will be "sandboxed", so the newly added heatpoints won't
have any effect outside this test.
Remember that Warden evaluates each condition in order and stops at the first failed
root condition: the last condition that is listed in a failed rule is where Warden
stopped evaluating them.
If a valid Rank is also passed it will be used in place of the target's real
rank during the test.
See the documentation for a full list of Warden events.

Example:
[p]def warden debug <valid_user_id> on-user-join
[p]def warden debug <valid_message_id> on-message
[p]def warden debug <valid_message_id> on-message-edit 3

**Usage:** `<@1275521742961508432>defender warden debug`

### defender warden find

**Description:** Search for text in existing rules

**Usage:** `<@1275521742961508432>defender warden find`

### defender warden remove

**Description:** Removes a rule by name

**Usage:** `<@1275521742961508432>defender warden remove`

### defender warden exportall

**Description:** Sends all the rules as a tar.gz archive

**Usage:** `<@1275521742961508432>defender warden exportall`

### defender warden export

**Description:** Sends the rule as a YAML file

**Usage:** `<@1275521742961508432>defender warden export`

### defender warden upload

**Description:** Starts a rule upload session

**Usage:** `<@1275521742961508432>defender warden upload`

### defender updates

**Description:** Shows all the past announcements of Defender

**Usage:** `<@1275521742961508432>defender updates`

### defender memberranks

**Description:** Counts how many members are in each rank

**Usage:** `<@1275521742961508432>defender memberranks`

### defender status

**Description:** Shows overall status of the Defender system

**Usage:** `<@1275521742961508432>defender status`

### defender emergency

**Description:** Manually engage or turn off emergency mode

Upon activation, staff will be pinged and any module
that is set to be active in emergency mode will be rendered
available to helpers

**Usage:** `<@1275521742961508432>defender emergency`

### defender freshmeat

**Description:** Returns a list of the new users of the day

Can be filtered. Supports wildcards (* and ?)

**Usage:** `<@1275521742961508432>defender freshmeat`

### defender identify

**Description:** Shows a member's rank + info

**Usage:** `<@1275521742961508432>defender identify`

### defender notifynew

**Description:** Sends you a DM if a user younger than X hours joins

Use 0 hours to disable notifications

**Usage:** `<@1275521742961508432>defender notifynew`

### defender monitor

**Description:** Shows recent events that might require your attention

Can be filtered. Supports wildcards (* and ?)

**Usage:** `<@1275521742961508432>defender monitor`

### alert

**Description:** Alert the staff members

**Usage:** `<@1275521742961508432>alert`

### vaporize

**Description:** Gets rid of bad actors in a quick and silent way

Works only on Rank 3 and under

**Usage:** `<@1275521742961508432>vaporize`

### voteout

**Description:** Initiates a vote to expel a user from the server

Can be used by members with helper roles during emergency mode

**Usage:** `<@1275521742961508432>voteout`

### silence

**Description:** Enables server wide message autodeletion for the specified rank (and below)

Passing 0 will disable this.

**Usage:** `<@1275521742961508432>silence`

