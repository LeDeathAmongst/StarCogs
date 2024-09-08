# Core Help

### info

**Description:** Shows info about [botname].

**Usage:** `<@1275521742961508432>info`

### uptime

**Description:** Shows [botname]'s uptime.

**Usage:** `<@1275521742961508432>uptime`

### mydata

**Description:** Commands which interact with the data [botname] has about you.

More information can be found in the [End User Data Documentation.](https://docs.discord.red/en/stable/red_core_data_statement.html)

**Usage:** `<@1275521742961508432>mydata`

### mydata 3rdparty

**Description:** View the End User Data statements of each 3rd-party module.

This will send an attachment with the End User Data statements of all loaded 3rd party cogs.

**Example:**
- `[p]mydata 3rdparty`

**Usage:** `<@1275521742961508432>mydata 3rdparty`

### mydata getmydata

**Description:** [Coming Soon] Get what data [botname] has about you.

**Usage:** `<@1275521742961508432>mydata getmydata`

### mydata forgetme

**Description:** Have [botname] forget what it knows about you.

This may not remove all data about you, data needed for operation,
such as command cooldowns will be kept until no longer necessary.

Further interactions with [botname] may cause it to learn about you again.

**Example:**
- `[p]mydata forgetme`

**Usage:** `<@1275521742961508432>mydata forgetme`

### mydata ownermanagement

**Description:** Commands for more complete data handling.

**Usage:** `<@1275521742961508432>mydata ownermanagement`

### mydata ownermanagement deleteforuser

**Description:** Delete data [botname] has about a user for a user.

This will cause the bot to get rid of or disassociate a lot of non-operational data from the specified user.
Users have access to a different command for this unless they can't interact with the bot at all.
This is a mostly safe operation, but you should not use it unless processing a request from this user as it may impact their usage of the bot.

**Arguments:**
- `<user_id>` - The id of the user whose data would be deleted.

**Usage:** `<@1275521742961508432>mydata ownermanagement deleteforuser`

### mydata ownermanagement processdiscordrequest

**Description:** Handle a deletion request from Discord.

This will cause the bot to get rid of or disassociate all data from the specified user ID.
You should not use this unless Discord has specifically requested this with regard to a deleted user.
This will remove the user from various anti-abuse measures.
If you are processing a manual request from a user, you may want `[p]mydata ownermanagement deleteforuser` instead.

**Arguments:**
- `<user_id>` - The id of the user whose data would be deleted.

**Usage:** `<@1275521742961508432>mydata ownermanagement processdiscordrequest`

### mydata ownermanagement allowuserdeletions

**Description:** Set the bot to allow users to request a data deletion.

This is on by default.
Opposite of `[p]mydata ownermanagement disallowuserdeletions`

**Example:**
- `[p]mydata ownermanagement allowuserdeletions`

**Usage:** `<@1275521742961508432>mydata ownermanagement allowuserdeletions`

### mydata ownermanagement disallowuserdeletions

**Description:** Set the bot to not allow users to request a data deletion.

Opposite of `[p]mydata ownermanagement allowuserdeletions`

**Example:**
- `[p]mydata ownermanagement disallowuserdeletions`

**Usage:** `<@1275521742961508432>mydata ownermanagement disallowuserdeletions`

### mydata ownermanagement setuserdeletionlevel

**Description:** Sets how user deletions are treated.

**Example:**
- `[p]mydata ownermanagement setuserdeletionlevel 1`

**Arguments:**
- `<level>` - The strictness level for user deletion. See Level guide below.

Level:
- `0`: What users can delete is left entirely up to each cog.
- `1`: Cogs should delete anything the cog doesn't need about the user.

**Usage:** `<@1275521742961508432>mydata ownermanagement setuserdeletionlevel`

### mydata ownermanagement deleteuserasowner

**Description:** Delete data [botname] has about a user.

This will cause the bot to get rid of or disassociate a lot of data about the specified user.
This may include more than just end user data, including anti abuse records.

**Arguments:**
- `<user_id>` - The id of the user whose data would be deleted.

**Usage:** `<@1275521742961508432>mydata ownermanagement deleteuserasowner`

### mydata whatdata

**Description:** Find out what type of data [botname] stores and why.

**Example:**
- `[p]mydata whatdata`

**Usage:** `<@1275521742961508432>mydata whatdata`

### embedset

**Description:** Commands for toggling embeds on or off.

This setting determines whether or not to use embeds as a response to a command (for commands that support it).
The default is to use embeds.

The embed settings are checked until the first True/False in this order:

- In guild context:
  1. Channel override - `[p]embedset channel`
  2. Server command override - `[p]embedset command server`
  3. Server override - `[p]embedset server`
  4. Global command override - `[p]embedset command global`
  5. Global setting  -`[p]embedset global`

- In DM context:
  1. User override - `[p]embedset user`
  2. Global command override - `[p]embedset command global`
  3. Global setting - `[p]embedset global`

**Usage:** `<@1275521742961508432>embedset`

### embedset global

**Description:** Toggle the global embed setting.

This is used as a fallback if the user or guild hasn't set a preference.
The default is to use embeds.

To see full evaluation order of embed settings, run `[p]help embedset`.

**Example:**
- `[p]embedset global`

**Usage:** `<@1275521742961508432>embedset global`

### embedset server

**Description:** Set the server's embed setting.

If set, this is used instead of the global default to determine whether or not to use embeds.
This is used for all commands done in a server.

If enabled is left blank, the setting will be unset and the global default will be used instead.

To see full evaluation order of embed settings, run `[p]help embedset`.

**Examples:**
- `[p]embedset server False` - Disables embeds on this server.
- `[p]embedset server` - Resets value to use global default.

**Arguments:**
- `[enabled]` - Whether to use embeds on this server. Leave blank to reset to default.

**Usage:** `<@1275521742961508432>embedset server`

### embedset user

**Description:** Sets personal embed setting for DMs.

If set, this is used instead of the global default to determine whether or not to use embeds.
This is used for all commands executed in a DM with the bot.

If enabled is left blank, the setting will be unset and the global default will be used instead.

To see full evaluation order of embed settings, run `[p]help embedset`.

**Examples:**
- `[p]embedset user False` - Disables embeds in your DMs.
- `[p]embedset user` - Resets value to use global default.

**Arguments:**
- `[enabled]` - Whether to use embeds in your DMs. Leave blank to reset to default.

**Usage:** `<@1275521742961508432>embedset user`

### embedset showsettings

**Description:** Show the current embed settings.

Provide a command name to check for command specific embed settings.

**Examples:**
- `[p]embedset showsettings` - Shows embed settings.
- `[p]embedset showsettings info` - Also shows embed settings for the 'info' command.
- `[p]embedset showsettings "ignore list"` - Checking subcommands requires quotes.

**Arguments:**
- `[command]` - Checks this command for command specific embed settings.

**Usage:** `<@1275521742961508432>embedset showsettings`

### embedset command

**Description:** Sets a command's embed setting.

If you're the bot owner, this will try to change the command's embed setting globally by default.
Otherwise, this will try to change embed settings on the current server.

If enabled is left blank, the setting will be unset.

To see full evaluation order of embed settings, run `[p]help embedset`.

**Examples:**
- `[p]embedset command info` - Clears command specific embed settings for 'info'.
- `[p]embedset command info False` - Disables embeds for 'info'.
- `[p]embedset command "ignore list" True` - Quotes are needed for subcommands.

**Arguments:**
- `[enabled]` - Whether to use embeds for this command. Leave blank to reset to default.

**Usage:** `<@1275521742961508432>embedset command`

### embedset command global

**Description:** Sets a command's embed setting globally.

If set, this is used instead of the global default to determine whether or not to use embeds.

If enabled is left blank, the setting will be unset.

To see full evaluation order of embed settings, run `[p]help embedset`.

**Examples:**
- `[p]embedset command global info` - Clears command specific embed settings for 'info'.
- `[p]embedset command global info False` - Disables embeds for 'info'.
- `[p]embedset command global "ignore list" True` - Quotes are needed for subcommands.

**Arguments:**
- `[enabled]` - Whether to use embeds for this command. Leave blank to reset to default.

**Usage:** `<@1275521742961508432>embedset command global`

### embedset command server

**Description:** Sets a command's embed setting for the current server.

If set, this is used instead of the server default to determine whether or not to use embeds.

If enabled is left blank, the setting will be unset and the server default will be used instead.

To see full evaluation order of embed settings, run `[p]help embedset`.

**Examples:**
- `[p]embedset command server info` - Clears command specific embed settings for 'info'.
- `[p]embedset command server info False` - Disables embeds for 'info'.
- `[p]embedset command server "ignore list" True` - Quotes are needed for subcommands.

**Arguments:**
- `[enabled]` - Whether to use embeds for this command. Leave blank to reset to default.

**Usage:** `<@1275521742961508432>embedset command server`

### embedset channel

**Description:** Set's a channel's embed setting.

If set, this is used instead of the guild and command defaults to determine whether or not to use embeds.
This is used for all commands done in a channel.

If enabled is left blank, the setting will be unset and the guild default will be used instead.

To see full evaluation order of embed settings, run `[p]help embedset`.

**Examples:**
- `[p]embedset channel #text-channel False` - Disables embeds in the #text-channel.
- `[p]embedset channel #forum-channel disable` - Disables embeds in the #forum-channel.
- `[p]embedset channel #text-channel` - Resets value to use guild default in the #text-channel.

**Arguments:**
    - `<channel>` - The text, voice, stage, or forum channel to set embed setting for.
    - `[enabled]` - Whether to use embeds in this channel. Leave blank to reset to default.

**Usage:** `<@1275521742961508432>embedset channel`

### traceback

**Description:** Sends to the owner the last command exception that has occurred.

If public (yes is specified), it will be sent to the chat instead.

Warning: Sending the traceback publicly can accidentally reveal sensitive information about your computer or configuration.

**Examples:**
- `[p]traceback` - Sends the traceback to your DMs.
- `[p]traceback True` - Sends the last traceback in the current context.

**Arguments:**
- `[public]` - Whether to send the traceback to the current context. Leave blank to send to your DMs.

**Usage:** `<@1275521742961508432>traceback`

### invite

**Description:** Shows [botname]'s invite url.

This will always send the invite to DMs to keep it private.

This command is locked to the owner unless `[p]inviteset public` is set to True.

**Example:**
- `[p]invite`

**Usage:** `<@1275521742961508432>invite`

### inviteset

**Description:** Commands to setup [botname]'s invite settings.

**Usage:** `<@1275521742961508432>inviteset`

### inviteset commandscope

**Description:** Add the `applications.commands` scope to your invite URL.

This allows the usage of slash commands on the servers that invited your bot with that scope.

Note that previous servers that invited the bot without the scope cannot have slash commands, they will have to invite the bot a second time.

**Usage:** `<@1275521742961508432>inviteset commandscope`

### inviteset public

**Description:** Toggles if `[p]invite` should be accessible for the average user.

The bot must be made into a `Public bot` in the developer dashboard for public invites to work.

**Example:**
- `[p]inviteset public yes` - Toggles the public invite setting.

**Arguments:**
- `[confirm]` - Required to set to public. Not required to toggle back to private.

**Usage:** `<@1275521742961508432>inviteset public`

### inviteset perms

**Description:** Make the bot create its own role with permissions on join.

The bot will create its own role with the desired permissions when it joins a new server. This is a special role that can't be deleted or removed from the bot.

For that, you need to provide a valid permissions level.
You can generate one here: https://discordapi.com/permissions.html

Please note that you might need two factor authentication for some permissions.

**Example:**
- `[p]inviteset perms 134217728` - Adds a "Manage Nicknames" permission requirement to the invite.

**Arguments:**
- `<level>` - The permission level to require for the bot in the generated invite.

**Usage:** `<@1275521742961508432>inviteset perms`

### leave

**Description:** Leaves servers.

If no server IDs are passed the local server will be left instead.

Note: This command is interactive.

**Examples:**
- `[p]leave` - Leave the current server.
- `[p]leave "Red - Discord Bot"` - Quotes are necessary when there are spaces in the name.
- `[p]leave 133049272517001216 240154543684321280` - Leaves multiple servers, using IDs.

**Arguments:**
- `[servers...]` - The servers to leave. When blank, attempts to leave the current server.

**Usage:** `<@1275521742961508432>leave`

### servers

**Description:** Lists the servers [botname] is currently in.

Note: This command is interactive.

**Usage:** `<@1275521742961508432>servers`

### load

**Description:** Loads cog packages from the local paths and installed cogs.

See packages available to load with `[p]cogs`.

Additional cogs can be added using Downloader, or from local paths using `[p]addpath`.

**Examples:**
- `[p]load general` - Loads the `general` cog.
- `[p]load admin mod mutes` - Loads multiple cogs.

**Arguments:**
- `<cogs...>` - The cog packages to load.

**Usage:** `<@1275521742961508432>load`

### unload

**Description:** Unloads previously loaded cog packages.

See packages available to unload with `[p]cogs`.

**Examples:**
- `[p]unload general` - Unloads the `general` cog.
- `[p]unload admin mod mutes` - Unloads multiple cogs.

**Arguments:**
- `<cogs...>` - The cog packages to unload.

**Usage:** `<@1275521742961508432>unload`

### reload

**Description:** Reloads cog packages.

This will unload and then load the specified cogs.

Cogs that were not loaded will only be loaded.

**Examples:**
- `[p]reload general` - Unloads then loads the `general` cog.
- `[p]reload admin mod mutes` - Unloads then loads multiple cogs.

**Arguments:**
- `<cogs...>` - The cog packages to reload.

**Usage:** `<@1275521742961508432>reload`

### slash

**Description:** Base command for managing what application commands are able to be used on [botname].

**Usage:** `<@1275521742961508432>slash`

### slash disablecog

**Description:** Marks all application commands in a cog as being disabled, preventing them from being added to the bot.

See a list of cogs with application commands with `[p]slash list`.

This command does NOT sync the enabled commands with Discord, that must be done manually with `[p]slash sync` for commands to appear in users' clients.

**Arguments:**
    - `<cog_name>` - The cog to disable commands from. This argument is case sensitive.

**Usage:** `<@1275521742961508432>slash disablecog`

### slash enable

**Description:** Marks an application command as being enabled, allowing it to be added to the bot.

See commands available to enable with `[p]slash list`.

This command does NOT sync the enabled commands with Discord, that must be done manually with `[p]slash sync` for commands to appear in users' clients.

**Arguments:**
    - `<command_name>` - The command name to enable. Only the top level name of a group command should be used.
    - `[command_type]` - What type of application command to enable. Must be one of `slash`, `message`, or `user`. Defaults to `slash`.

**Usage:** `<@1275521742961508432>slash enable`

### slash disable

**Description:** Marks an application command as being disabled, preventing it from being added to the bot.

See commands available to disable with `[p]slash list`.

This command does NOT sync the enabled commands with Discord, that must be done manually with `[p]slash sync` for commands to appear in users' clients.

**Arguments:**
    - `<command_name>` - The command name to disable. Only the top level name of a group command should be used.
    - `[command_type]` - What type of application command to disable. Must be one of `slash`, `message`, or `user`. Defaults to `slash`.

**Usage:** `<@1275521742961508432>slash disable`

### slash sync

**Description:** Syncs the slash settings to discord.

Settings from `[p]slash list` will be synced with discord, changing what commands appear for users.
This should be run sparingly, make all necessary changes before running this command.

**Arguments:**
    - `[guild]` - If provided, syncs commands for that guild. Otherwise, syncs global commands.

**Usage:** `<@1275521742961508432>slash sync`

### slash enablecog

**Description:** Marks all application commands in a cog as being enabled, allowing them to be added to the bot.

See a list of cogs with application commands with `[p]slash list`.

This command does NOT sync the enabled commands with Discord, that must be done manually with `[p]slash sync` for commands to appear in users' clients.

**Arguments:**
    - `<cog_name>` - The cog to enable commands from. This argument is case sensitive.

**Usage:** `<@1275521742961508432>slash enablecog`

### slash list

**Description:** List the slash commands the bot can see, and whether or not they are enabled.

This command shows the state that will be changed to when `[p]slash sync` is run.
Commands from the same cog are grouped, with the cog name as the header.

The prefix denotes the state of the command:
- Commands starting with `- ` have not yet been enabled.
- Commands starting with `+ ` have been manually enabled.
- Commands starting with `++` have been enabled by the cog author, and cannot be disabled.

**Usage:** `<@1275521742961508432>slash list`

### shutdown

**Description:** Shuts down the bot.

Allows [botname] to shut down gracefully.

This is the recommended method for shutting down the bot.

**Examples:**
- `[p]shutdown`
- `[p]shutdown True` - Shutdowns directly.

**Arguments:**
- `[directly]` - Whether to shutdown directly without confirmation. Defaults to False.

**Usage:** `<@1275521742961508432>shutdown`

### restart

**Description:** Attempts to restart [botname].

Makes [botname] quit with exit code 26.
The restart is not guaranteed: it must be dealt with by the process manager in use.

**Examples:**
- `[p]restart`
- `[p]restart True` - Restarts directly.

**Arguments:**
- `[directly]` - Whether to restart directly without confirmation. Defaults to False.

**Usage:** `<@1275521742961508432>restart`

### bankset

**Description:** Base command for bank settings.

**Usage:** `<@1275521742961508432>bankset`

### bankset creditsname

**Description:** Set the name for the bank's currency.

**Usage:** `<@1275521742961508432>bankset creditsname`

### bankset toggleglobal

**Description:** Toggle whether the bank is global or not.

If the bank is global, it will become per-server.
If the bank is per-server, it will become global.

**Usage:** `<@1275521742961508432>bankset toggleglobal`

### bankset registeramount

**Description:** Set the initial balance for new bank accounts.

Example:
- `[p]bankset registeramount 5000`

**Arguments**

- `<creds>` The new initial balance amount. Default is 0.

**Usage:** `<@1275521742961508432>bankset registeramount`

### bankset reset

**Description:** Delete all bank accounts.

Examples:
- `[p]bankset reset` - Did not confirm. Shows the help message.
- `[p]bankset reset yes`

**Arguments**

- `<confirmation>` This will default to false unless specified.

**Usage:** `<@1275521742961508432>bankset reset`

### bankset prune

**Description:** Base command for pruning bank accounts.

**Usage:** `<@1275521742961508432>bankset prune`

### bankset prune global

**Description:** Prune bank accounts for users who no longer share a server with the bot.

Cannot be used without a global bank. See `[p]bankset prune server`.

Examples:
- `[p]bankset prune global` - Did not confirm. Shows the help message.
- `[p]bankset prune global yes`

**Arguments**

- `<confirmation>` This will default to false unless specified.

**Usage:** `<@1275521742961508432>bankset prune global`

### bankset prune server

**Description:** Prune bank accounts for users no longer in the server.

Cannot be used with a global bank. See `[p]bankset prune global`.

Examples:
- `[p]bankset prune server` - Did not confirm. Shows the help message.
- `[p]bankset prune server yes`

**Arguments**

- `<confirmation>` This will default to false unless specified.

**Usage:** `<@1275521742961508432>bankset prune server`

### bankset prune user

**Description:** Delete the bank account of a specified user.

Examples:
- `[p]bankset prune user @Twentysix` - Did not confirm. Shows the help message.
- `[p]bankset prune user @Twentysix yes`

**Arguments**

- `<user>` The user to delete the bank of. Takes mentions, names, and user ids.
- `<confirmation>` This will default to false unless specified.

**Usage:** `<@1275521742961508432>bankset prune user`

### bankset maxbal

**Description:** Set the maximum balance a user can get.

**Usage:** `<@1275521742961508432>bankset maxbal`

### bankset bankname

**Description:** Set the bank's name.

**Usage:** `<@1275521742961508432>bankset bankname`

### bankset showsettings

**Description:** Show the current bank settings.

**Usage:** `<@1275521742961508432>bankset showsettings`

### modlogset

**Description:** Manage modlog settings.

**Usage:** `<@1275521742961508432>modlogset`

### modlogset resetcases

**Description:** Reset all modlog cases in this server.

**Usage:** `<@1275521742961508432>modlogset resetcases`

### modlogset modlog

**Description:** Set a channel as the modlog.

Omit `[channel]` to disable the modlog.

**Usage:** `<@1275521742961508432>modlogset modlog`

### modlogset cases

**Description:** Enable or disable case creation for a mod action.

An action can be enabling or disabling specific cases. (Ban, kick, mute, etc.)

Example: `[p]modlogset cases kick enabled`

**Usage:** `<@1275521742961508432>modlogset cases`

### set

**Description:** Commands for changing [botname]'s settings.

**Usage:** `<@1275521742961508432>set`

### set roles

**Description:** Set server's admin and mod roles for [botname].

**Usage:** `<@1275521742961508432>set roles`

### set roles addadminrole

**Description:** Adds an admin role for this server.

Admins have the same access as Mods, plus additional admin level commands like:
 - `[p]set serverprefix`
 - `[p]addrole`
 - `[p]ban`
 - `[p]ignore guild`

 And more.

**Examples:**
- `[p]set roles addadminrole @Admins`
- `[p]set roles addadminrole Super Admins`

**Arguments:**
- `<role>` - The role to add as an admin.

**Usage:** `<@1275521742961508432>set roles addadminrole`

### set roles removeadminrole

**Description:** Removes an admin role for this server.

**Examples:**
- `[p]set roles removeadminrole @Admins`
- `[p]set roles removeadminrole Super Admins`

**Arguments:**
- `<role>` - The role to remove from being an admin.

**Usage:** `<@1275521742961508432>set roles removeadminrole`

### set roles addmodrole

**Description:** Adds a moderator role for this server.

This grants access to moderator level commands like:
 - `[p]mute`
 - `[p]cleanup`
 - `[p]customcommand create`

 And more.

**Examples:**
- `[p]set roles addmodrole @Mods`
- `[p]set roles addmodrole Loyal Helpers`

**Arguments:**
- `<role>` - The role to add as a moderator.

**Usage:** `<@1275521742961508432>set roles addmodrole`

### set roles removemodrole

**Description:** Removes a mod role for this server.

**Examples:**
- `[p]set roles removemodrole @Mods`
- `[p]set roles removemodrole Loyal Helpers`

**Arguments:**
- `<role>` - The role to remove from being a moderator.

**Usage:** `<@1275521742961508432>set roles removemodrole`

### set status

**Description:** Commands for setting [botname]'s status.

**Usage:** `<@1275521742961508432>set status`

### set status listening

**Description:** Sets [botname]'s listening status.

This will appear as `Listening to <listening>`.

Maximum length for a listening status is 128 characters.

**Examples:**
- `[p]set status listening` - Clears the activity status.
- `[p]set status listening jams`

**Arguments:**
- `[listening]` - The text to follow `Listening to`. Leave blank to clear the current activity status.

**Usage:** `<@1275521742961508432>set status listening`

### set status dnd

**Description:** Set [botname]'s status to do not disturb.

**Usage:** `<@1275521742961508432>set status dnd`

### set status competing

**Description:** Sets [botname]'s competing status.

This will appear as `Competing in <competing>`.

Maximum length for a competing status is 128 characters.

**Examples:**
- `[p]set status competing` - Clears the activity status.
- `[p]set status competing London 2012 Olympic Games`

**Arguments:**
- `[competing]` - The text to follow `Competing in`. Leave blank to clear the current activity status.

**Usage:** `<@1275521742961508432>set status competing`

### set status idle

**Description:** Set [botname]'s status to idle.

**Usage:** `<@1275521742961508432>set status idle`

### set status watching

**Description:** Sets [botname]'s watching status.

This will appear as `Watching <watching>`.

Maximum length for a watching status is 128 characters.

**Examples:**
- `[p]set status watching` - Clears the activity status.
- `[p]set status watching [p]help`

**Arguments:**
- `[watching]` - The text to follow `Watching`. Leave blank to clear the current activity status.

**Usage:** `<@1275521742961508432>set status watching`

### set status invisible

**Description:** Set [botname]'s status to invisible.

**Usage:** `<@1275521742961508432>set status invisible`

### set status streaming

**Description:** Sets [botname]'s streaming status to a twitch stream.

This will appear as `Streaming <stream_title>` or `LIVE ON TWITCH` depending on the context.
It will also include a `Watch` button with a twitch.tv url for the provided streamer.

Maximum length for a stream title is 128 characters.

Leaving both streamer and stream_title empty will clear it.

**Examples:**
- `[p]set status stream` - Clears the activity status.
- `[p]set status stream 26 Twentysix is streaming` - Sets the stream to `https://www.twitch.tv/26`.
- `[p]set status stream https://twitch.tv/26 Twentysix is streaming` - Sets the URL manually.

**Arguments:**
- `<streamer>` - The twitch streamer to provide a link to. This can be their twitch name or the entire URL.
- `<stream_title>` - The text to follow `Streaming` in the status.

**Usage:** `<@1275521742961508432>set status streaming`

### set status online

**Description:** Set [botname]'s status to online.

**Usage:** `<@1275521742961508432>set status online`

### set status playing

**Description:** Sets [botname]'s playing status.

This will appear as `Playing <game>` or `PLAYING A GAME: <game>` depending on the context.

Maximum length for a playing status is 128 characters.

**Examples:**
- `[p]set status playing` - Clears the activity status.
- `[p]set status playing the keyboard`

**Arguments:**
- `[game]` - The text to follow `Playing`. Leave blank to clear the current activity status.

**Usage:** `<@1275521742961508432>set status playing`

### set status custom

**Description:** Sets [botname]'s custom status.

This will appear as `<text>`.

Maximum length for a custom status is 128 characters.

**Examples:**
- `[p]set status custom` - Clears the activity status.
- `[p]set status custom Running cogs...`

**Arguments:**
- `[text]` - The custom status text. Leave blank to clear the current activity status.

**Usage:** `<@1275521742961508432>set status custom`

### set usebuttons

**Description:** Set a global bot variable for using buttons in menus.

When enabled, all usage of cores menus API will use buttons instead of reactions.

This defaults to False.
Using this without a setting will toggle.

**Examples:**
    - `[p]set usebuttons True` - Enables using buttons.
    - `[p]helpset usebuttons` - Toggles the value.

**Arguments:**
    - `[use_buttons]` - Whether to use buttons. Leave blank to toggle.

**Usage:** `<@1275521742961508432>set usebuttons`

### set showsettings

**Description:** Show the current settings for [botname].

Accepts optional server parameter to allow prefix recovery.

**Usage:** `<@1275521742961508432>set showsettings`

### set usebotcolour

**Description:** Toggle whether to use the bot owner-configured colour for embeds.

Default is to use the bot's configured colour.
Otherwise, the colour used will be the colour of the bot's top role.

**Example:**
- `[p]set usebotcolour`

**Usage:** `<@1275521742961508432>set usebotcolour`

### set colour

**Description:** Sets a default colour to be used for the bot's embeds.

Acceptable values for the colour parameter can be found at:

https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.ColourConverter

**Examples:**
- `[p]set colour dark red`
- `[p]set colour blurple`
- `[p]set colour 0x5DADE2`
- `[p]set color 0x#FDFEFE`
- `[p]set color #7F8C8D`

**Arguments:**
- `[colour]` - The colour to use for embeds. Leave blank to set to the default value (red).

**Usage:** `<@1275521742961508432>set colour`

### set prefix

**Description:** Sets [botname]'s global prefix(es).

Warning: This is not additive. It will replace all current prefixes.

See also the `--mentionable` flag to enable mentioning the bot as the prefix.

**Examples:**
- `[p]set prefix !`
- `[p]set prefix "! "` - Quotes are needed to use spaces in prefixes.
- `[p]set prefix "@[botname] "` - This uses a mention as the prefix. See also the `--mentionable` flag.
- `[p]set prefix ! ? .` - Sets multiple prefixes.

**Arguments:**
- `<prefixes...>` - The prefixes the bot will respond to globally.

**Usage:** `<@1275521742961508432>set prefix`

### set bot

**Description:** Commands for changing [botname]'s metadata.

**Usage:** `<@1275521742961508432>set bot`

### set bot banner

**Description:** Sets [botname]'s banner

Supports either an attachment or an image URL.

**Examples:**
- `[p]set bot banner` - With an image attachment, this will set the banner.
- `[p]set bot banner` - Without an attachment, this will show the command help.
- `[p]set bot banner https://opengraph.githubassets.com` - Sets the banner to the provided url.

**Arguments:**
- `[url]` - An image url to be used as an banner. Leave blank when uploading an attachment.

**Usage:** `<@1275521742961508432>set bot banner`

### set bot banner remove

**Description:** Removes [botname]'s banner.

**Example:**
- `[p]set bot banner remove`

**Usage:** `<@1275521742961508432>set bot banner remove`

### set bot username

**Description:** Sets [botname]'s username.

Maximum length for a username is 32 characters.

Note: The username of a verified bot cannot be manually changed.
    Please contact Discord support to change it.

**Example:**
- `[p]set bot username BaguetteBot`

**Arguments:**
- `<username>` - The username to give the bot.

**Usage:** `<@1275521742961508432>set bot username`

### set bot nickname

**Description:** Sets [botname]'s nickname for the current server.

Maximum length for a nickname is 32 characters.

**Example:**
- `[p]set bot nickname 🎃 SpookyBot 🎃`

**Arguments:**
- `[nickname]` - The nickname to give the bot. Leave blank to clear the current nickname.

**Usage:** `<@1275521742961508432>set bot nickname`

### set bot avatar

**Description:** Sets [botname]'s avatar

Supports either an attachment or an image URL.

**Examples:**
- `[p]set bot avatar` - With an image attachment, this will set the avatar.
- `[p]set bot avatar` - Without an attachment, this will show the command help.
- `[p]set bot avatar https://avatars.githubusercontent.com/u/23690422` - Sets the avatar to the provided url.

**Arguments:**
- `[url]` - An image url to be used as an avatar. Leave blank when uploading an attachment.

**Usage:** `<@1275521742961508432>set bot avatar`

### set bot avatar remove

**Description:** Removes [botname]'s avatar.

**Example:**
- `[p]set bot avatar remove`

**Usage:** `<@1275521742961508432>set bot avatar remove`

### set bot description

**Description:** Sets the bot's description.

Use without a description to reset.
This is shown in a few locations, including the help menu.

The maximum description length is 250 characters to ensure it displays properly.

The default is "Red V3".

**Examples:**
- `[p]set bot description` - Resets the description to the default setting.
- `[p]set bot description MyBot: A Red V3 Bot`

**Arguments:**
- `[description]` - The description to use for this bot. Leave blank to reset to the default.

**Usage:** `<@1275521742961508432>set bot description`

### set bot custominfo

**Description:** Customizes a section of `[p]info`.

The maximum amount of allowed characters is 1024.
Supports markdown, links and "mentions".

Link example: `[My link](https://example.com)`

**Examples:**
- `[p]set bot custominfo >>> I can use **markdown** such as quotes, ||spoilers|| and multiple lines.`
- `[p]set bot custominfo Join my [support server](discord.gg/discord)!`
- `[p]set bot custominfo` - Removes custom info text.

**Arguments:**
- `[text]` - The custom info text.

**Usage:** `<@1275521742961508432>set bot custominfo`

### set errormsg

**Description:** Set the message that will be sent on uncaught bot errors.

To include the command name in the message, use the `{command}` placeholder.

If you omit the `msg` argument, the message will be reset to the default one.

**Examples:**
    - `[p]set errormsg` - Resets the error message back to the default: "Error in command '{command}'.". If the command invoker is one of the bot owners, the message will also include "Check your console or logs for details.".
    - `[p]set errormsg Oops, the command {command} has failed! Please try again later.` - Sets the error message to a custom one.

**Arguments:**
    - `[msg]` - The custom error message. Must be less than 1000 characters. Omit to reset to the default one.

**Usage:** `<@1275521742961508432>set errormsg`

### set regionalformat

**Description:** Changes the bot's regional format in this server. This is used for formatting date, time and numbers.

`language_code` can be any language code with country code included, e.g. `en-US`, `de-DE`, `fr-FR`, `pl-PL`, etc.
Pass "reset" to `language_code` to base regional formatting on bot's locale in this server.

If you want to change bot's global regional format, see `[p]set regionalformat global` command.

**Examples:**
- `[p]set regionalformat en-US`
- `[p]set region de-DE`
- `[p]set regionalformat reset` - Resets to the locale.

**Arguments:**
- `[language_code]` - The region format to use for the bot in this server.

**Usage:** `<@1275521742961508432>set regionalformat`

### set regionalformat global

**Description:** Changes the bot's regional format. This is used for formatting date, time and numbers.

`language_code` can be any language code with country code included, e.g. `en-US`, `de-DE`, `fr-FR`, `pl-PL`, etc.
Pass "reset" to `language_code` to base regional formatting on bot's locale.

**Examples:**
- `[p]set regionalformat global en-US`
- `[p]set region global de-DE`
- `[p]set regionalformat global reset` - Resets to the locale.

**Arguments:**
- `[language_code]` - The default region format to use for the bot.

**Usage:** `<@1275521742961508432>set regionalformat global`

### set regionalformat server

**Description:** Changes the bot's regional format in this server. This is used for formatting date, time and numbers.

`language_code` can be any language code with country code included, e.g. `en-US`, `de-DE`, `fr-FR`, `pl-PL`, etc.
Pass "reset" to `language_code` to base regional formatting on bot's locale in this server.

**Examples:**
- `[p]set regionalformat server en-US`
- `[p]set region local de-DE`
- `[p]set regionalformat server reset` - Resets to the locale.

**Arguments:**
- `[language_code]` - The region format to use for the bot in this server.

**Usage:** `<@1275521742961508432>set regionalformat server`

### set ownernotifications

**Description:** Commands for configuring owner notifications.

Owner notifications include usage of `[p]contact` and available Red updates.

**Usage:** `<@1275521742961508432>set ownernotifications`

### set ownernotifications optin

**Description:** Opt-in on receiving owner notifications.

This is the default state.

Note: This will only resume sending owner notifications to your DMs.
    Additional owners and destinations will not be affected.

**Example:**
- `[p]set ownernotifications optin`

**Usage:** `<@1275521742961508432>set ownernotifications optin`

### set ownernotifications adddestination

**Description:** Adds a destination text channel to receive owner notifications.

**Examples:**
- `[p]set ownernotifications adddestination #owner-notifications`
- `[p]set ownernotifications adddestination 168091848718417920` - Accepts channel IDs.

**Arguments:**
- `<channel>` - The channel to send owner notifications to.

**Usage:** `<@1275521742961508432>set ownernotifications adddestination`

### set ownernotifications listdestinations

**Description:** Lists the configured extra destinations for owner notifications.

**Example:**
- `[p]set ownernotifications listdestinations`

**Usage:** `<@1275521742961508432>set ownernotifications listdestinations`

### set ownernotifications optout

**Description:** Opt-out of receiving owner notifications.

Note: This will only stop sending owner notifications to your DMs.
    Additional owners and destinations will still receive notifications.

**Example:**
- `[p]set ownernotifications optout`

**Usage:** `<@1275521742961508432>set ownernotifications optout`

### set ownernotifications removedestination

**Description:** Removes a destination text channel from receiving owner notifications.

**Examples:**
- `[p]set ownernotifications removedestination #owner-notifications`
- `[p]set ownernotifications deletedestination 168091848718417920` - Accepts channel IDs.

**Arguments:**
- `<channel>` - The channel to stop sending owner notifications to.

**Usage:** `<@1275521742961508432>set ownernotifications removedestination`

### set locale

**Description:** Changes [botname]'s locale in this server.

Go to [Red's Crowdin page](https://translate.discord.red) to see locales that are available with translations.

Use "default" to return to the bot's default set language.

If you want to change bot's global locale, see `[p]set locale global` command.

**Examples:**
- `[p]set locale en-US`
- `[p]set locale de-DE`
- `[p]set locale fr-FR`
- `[p]set locale pl-PL`
- `[p]set locale default` - Resets to the global default locale.

**Arguments:**
- `<language_code>` - The default locale to use for the bot. This can be any language code with country code included.

**Usage:** `<@1275521742961508432>set locale`

### set locale global

**Description:** Changes [botname]'s default locale.

This will be used when a server has not set a locale, or in DMs.

Go to [Red's Crowdin page](https://translate.discord.red) to see locales that are available with translations.

To reset to English, use "en-US".

**Examples:**
- `[p]set locale global en-US`
- `[p]set locale global de-DE`
- `[p]set locale global fr-FR`
- `[p]set locale global pl-PL`

**Arguments:**
- `<language_code>` - The default locale to use for the bot. This can be any language code with country code included.

**Usage:** `<@1275521742961508432>set locale global`

### set locale server

**Description:** Changes [botname]'s locale in this server.

Go to [Red's Crowdin page](https://translate.discord.red) to see locales that are available with translations.

Use "default" to return to the bot's default set language.

**Examples:**
- `[p]set locale server en-US`
- `[p]set locale server de-DE`
- `[p]set locale server fr-FR`
- `[p]set locale server pl-PL`
- `[p]set locale server default` - Resets to the global default locale.

**Arguments:**
- `<language_code>` - The default locale to use for the bot. This can be any language code with country code included.

**Usage:** `<@1275521742961508432>set locale server`

### set serverfuzzy

**Description:** Toggle whether to enable fuzzy command search for the server.

This allows the bot to identify potential misspelled commands and offer corrections.

Note: This can be processor intensive and may be unsuitable for larger servers.

Default is for fuzzy command search to be disabled.

**Example:**
- `[p]set serverfuzzy`

**Usage:** `<@1275521742961508432>set serverfuzzy`

### set fuzzy

**Description:** Toggle whether to enable fuzzy command search in DMs.

This allows the bot to identify potential misspelled commands and offer corrections.

Default is for fuzzy command search to be disabled.

**Example:**
- `[p]set fuzzy`

**Usage:** `<@1275521742961508432>set fuzzy`

### set serverprefix

**Description:** Sets [botname]'s server prefix(es).

Warning: This will override global prefixes, the bot will not respond to any global prefixes in this server.
    This is not additive. It will replace all current server prefixes.
    A prefix cannot have more than 25 characters.

**Examples:**
- `[p]set serverprefix !`
- `[p]set serverprefix "! "` - Quotes are needed to use spaces in prefixes.
- `[p]set serverprefix "@[botname] "` - This uses a mention as the prefix.
- `[p]set serverprefix ! ? .` - Sets multiple prefixes.
- `[p]set serverprefix "Red - Discord Bot" ?` - Sets the prefix for a specific server. Quotes are needed to use spaces in the server name.

**Arguments:**
- `[server]` - The server to set the prefix for. Defaults to current server.
- `[prefixes...]` - The prefixes the bot will respond to on this server. Leave blank to clear server prefixes.

**Usage:** `<@1275521742961508432>set serverprefix`

### set deletedelay

**Description:** Set the delay until the bot removes the command message.

Must be between -1 and 60.

Set to -1 to disable this feature.

This is only applied to the current server and not globally.

**Examples:**
- `[p]set deletedelay` - Shows the current delete delay setting.
- `[p]set deletedelay 60` - Sets the delete delay to the max of 60 seconds.
- `[p]set deletedelay -1` - Disables deleting command messages.

**Arguments:**
- `[time]` - The seconds to wait before deleting the command message. Use -1 to disable.

**Usage:** `<@1275521742961508432>set deletedelay`

### set api

**Description:** Commands to set, list or remove various external API tokens.

This setting will be asked for by some 3rd party cogs and some core cogs.

If passed without the `<service>` or `<tokens>` arguments it will allow you to open a modal to set your API keys securely.

To add the keys provide the service name and the tokens as a comma separated
list of key,values as described by the cog requesting this command.

Note: API tokens are sensitive, so this command should only be used in a private channel or in DM with the bot.

**Examples:**
- `[p]set api`
- `[p]set api spotify`
- `[p]set api spotify redirect_uri localhost`
- `[p]set api github client_id,whoops client_secret,whoops`

**Arguments:**
- `<service>` - The service you're adding tokens to.
- `<tokens>` - Pairs of token keys and values. The key and value should be separated by one of ` `, `,`, or `;`.

**Usage:** `<@1275521742961508432>set api`

### set api list

**Description:** Show all external API services along with their keys that have been set.

Secrets are not shown.

**Example:**
- `[p]set api list`

**Usage:** `<@1275521742961508432>set api list`

### set api remove

**Description:** Remove the given services with all their keys and tokens.

**Examples:**
- `[p]set api remove spotify`
- `[p]set api remove github youtube`

**Arguments:**
- `<services...>` - The services to remove.

**Usage:** `<@1275521742961508432>set api remove`

### helpset

**Description:** Commands to manage settings for the help command.

All help settings are applied globally.

**Usage:** `<@1275521742961508432>helpset`

### helpset showhidden

**Description:** This allows the help command to show hidden commands.

This defaults to False.
Using this without a setting will toggle.

**Examples:**
- `[p]helpset showhidden True` - Enables showing hidden commands.
- `[p]helpset showhidden` - Toggles the value.

**Arguments:**
- `[show_hidden]` - Whether to use show hidden commands in help. Leave blank to toggle.

**Usage:** `<@1275521742961508432>helpset showhidden`

### helpset showaliases

**Description:** This allows the help command to show existing commands aliases if there is any.

This defaults to True.
Using this without a setting will toggle.

**Examples:**
- `[p]helpset showaliases False` - Disables showing aliases on this server.
- `[p]helpset showaliases` - Toggles the value.

**Arguments:**
- `[show_aliases]` - Whether to include aliases in help. Leave blank to toggle.

**Usage:** `<@1275521742961508432>helpset showaliases`

### helpset usemenus

**Description:** Allows the help command to be sent as a paginated menu instead of separate
messages.

When "reactions", "buttons", "select", or "selectonly" is passed,
 `[p]help` will only show one page at a time
and will use the associated control scheme to navigate between pages.

 **Examples:**
- `[p]helpset usemenus reactions` - Enables using reaction menus.
- `[p]helpset usemenus buttons` - Enables using button menus.
- `[p]helpset usemenus select` - Enables buttons with a select menu.
- `[p]helpset usemenus selectonly` - Enables a select menu only on help.
- `[p]helpset usemenus disable` - Disables help menus.

**Arguments:**
    - `<"buttons"|"reactions"|"select"|"selectonly"|"disable">` - Whether to use `buttons`,
    `reactions`, `select`, `selectonly`, or no menus.

**Usage:** `<@1275521742961508432>helpset usemenus`

### helpset reacttimeout

**Description:** Set the timeout for reactions, if menus are enabled.

The default is 30 seconds.
The timeout has to be between 15 and 300 seconds.

**Examples:**
- `[p]helpset reacttimeout 30` - The default timeout.
- `[p]helpset reacttimeout 60` - Timeout of 1 minute.
- `[p]helpset reacttimeout 15` - Minimum allowed timeout.
- `[p]helpset reacttimeout 300` - Max allowed timeout (5 mins).

**Arguments:**
- `<seconds>` - The timeout, in seconds, of the reactions.

**Usage:** `<@1275521742961508432>helpset reacttimeout`

### helpset resetsettings

**Description:** This resets [botname]'s help settings to their defaults.

This may not have an impact when using custom formatters from 3rd party cogs

**Example:**
- `[p]helpset resetsettings`

**Usage:** `<@1275521742961508432>helpset resetsettings`

### helpset deletedelay

**Description:** Set the delay after which help pages will be deleted.

The setting is disabled by default, and only applies to non-menu help,
sent in server text channels.
Setting the delay to 0 disables this feature.

The bot has to have MANAGE_MESSAGES permission for this to work.

**Examples:**
- `[p]helpset deletedelay 60` - Delete the help pages after a minute.
- `[p]helpset deletedelay 1` - Delete the help pages as quickly as possible.
- `[p]helpset deletedelay 1209600` - Max time to wait before deleting (14 days).
- `[p]helpset deletedelay 0` - Disable deleting help pages.

**Arguments:**
- `<seconds>` - The seconds to wait before deleting help pages.

**Usage:** `<@1275521742961508432>helpset deletedelay`

### helpset verifyexists

**Description:** Sets whether the bot should respond to help commands for nonexistent topics.

When enabled, this will indicate the existence of help topics, even if the user can't use it.

Note: This setting on its own does not fully prevent command enumeration.

Defaults to False.
Using this without a setting will toggle.

**Examples:**
- `[p]helpset verifyexists True` - Enables sending help for nonexistent topics.
- `[p]helpset verifyexists` - Toggles the value.

**Arguments:**
- `[verify]` - Whether to respond to help for nonexistent topics. Leave blank to toggle.

**Usage:** `<@1275521742961508432>helpset verifyexists`

### helpset maxpages

**Description:** Set the maximum number of help pages sent in a server channel.

If a help message contains more pages than this value, the help message will
be sent to the command author via DM. This is to help reduce spam in server
text channels.

The default value is 2 pages.

**Examples:**
- `[p]helpset maxpages 50` - Basically never send help to DMs.
- `[p]helpset maxpages 0` - Always send help to DMs.

**Arguments:**
- `<limit>` - The max pages allowed to send per help in a server.

**Usage:** `<@1275521742961508432>helpset maxpages`

### helpset tagline

**Description:** Set the tagline to be used.

The maximum tagline length is 2048 characters.
This setting only applies to embedded help. If no tagline is specified, the default will be used instead.

You can use `[​p]` in your tagline, which will be replaced by the bot's prefix.

**Examples:**
- `[p]helpset tagline Thanks for using the bot!`
- `[p]helpset tagline Use [​p]invite to add me to your server.`
- `[p]helpset tagline` - Resets the tagline to the default.

**Arguments:**
- `[tagline]` - The tagline to appear at the bottom of help embeds. Leave blank to reset.

**Usage:** `<@1275521742961508432>helpset tagline`

### helpset pagecharlimit

**Description:** Set the character limit for each page in the help message.

Note: This setting only applies to embedded help.

The default value is 1000 characters. The minimum value is 500.
The maximum is based on the lower of what you provide and what discord allows.

Please note that setting a relatively small character limit may
mean some pages will exceed this limit.

**Example:**
- `[p]helpset pagecharlimit 1500`

**Arguments:**
- `<limit>` - The max amount of characters to show per page in the help message.

**Usage:** `<@1275521742961508432>helpset pagecharlimit`

### helpset resetformatter

**Description:** This resets [botname]'s help formatter to the default formatter.

**Example:**
- `[p]helpset resetformatter`

**Usage:** `<@1275521742961508432>helpset resetformatter`

### helpset verifychecks

**Description:** Sets if commands which can't be run in the current context should be filtered from help.

Defaults to True.
Using this without a setting will toggle.

**Examples:**
- `[p]helpset verifychecks False` - Enables showing unusable commands in help.
- `[p]helpset verifychecks` - Toggles the value.

**Arguments:**
- `[verify]` - Whether to hide unusable commands in help. Leave blank to toggle.

**Usage:** `<@1275521742961508432>helpset verifychecks`

### helpset showsettings

**Description:** Show the current help settings.

Warning: These settings may not be accurate if the default formatter is not in use.

**Example:**
- `[p]helpset showsettings`

**Usage:** `<@1275521742961508432>helpset showsettings`

### helpset usetick

**Description:** This allows the help command message to be ticked if help is sent to a DM.

Ticking is reacting to the help message with a ✅.

Defaults to False.
Using this without a setting will toggle.

Note: This is only used when the bot is not using menus.

**Examples:**
- `[p]helpset usetick False` - Disables ticking when help is sent to DMs.
- `[p]helpset usetick` - Toggles the value.

**Arguments:**
- `[use_tick]` - Whether to tick the help command when help is sent to DMs. Leave blank to toggle.

**Usage:** `<@1275521742961508432>helpset usetick`

### contact

**Description:** Sends a message to the owner.

This is limited to one message every 60 seconds per person.

**Example:**
- `[p]contact Help! The bot has become sentient!`

**Arguments:**
- `[message]` - The message to send to the owner.

**Usage:** `<@1275521742961508432>contact`

### dm

**Description:** Sends a DM to a user.

This command needs a user ID to work.

To get a user ID, go to Discord's settings and open the 'Appearance' tab.
Enable 'Developer Mode', then right click a user and click on 'Copy ID'.

**Example:**
- `[p]dm 262626262626262626 Do you like me? Yes / No`

**Arguments:**
- `[message]` - The message to dm to the user.

**Usage:** `<@1275521742961508432>dm`

### diagnoseissues

**Description:** Diagnose issues with the command checks with ease!

If you want to diagnose the command from a text channel in a different server,
you can do so by using the command in DMs.

**Example:**
- `[p]diagnoseissues #general @Slime ban` - Diagnose why @Slime can't use `[p]ban` in #general channel.

**Arguments:**
- `[channel]` - The text channel that the command should be tested for. Defaults to the current channel.
- `<member>` - The member that should be considered as the command caller.
- `<command_name>` - The name of the command to test.

**Usage:** `<@1275521742961508432>diagnoseissues`

### allowlist

**Description:** Commands to manage the allowlist.

Warning: When the allowlist is in use, the bot will ignore commands from everyone not on the list.

Use `[p]allowlist clear` to disable the allowlist

**Usage:** `<@1275521742961508432>allowlist`

### allowlist add

**Description:** Adds users to the allowlist.

**Examples:**
- `[p]allowlist add @26 @Will` - Adds two users to the allowlist.
- `[p]allowlist add 262626262626262626` - Adds a user by ID.

**Arguments:**
- `<users...>` - The user or users to add to the allowlist.

**Usage:** `<@1275521742961508432>allowlist add`

### allowlist list

**Description:** Lists users on the allowlist.

**Example:**
- `[p]allowlist list`

**Usage:** `<@1275521742961508432>allowlist list`

### allowlist remove

**Description:** Removes users from the allowlist.

The allowlist will be disabled if all users are removed.

**Examples:**
- `[p]allowlist remove @26 @Will` - Removes two users from the allowlist.
- `[p]allowlist remove 262626262626262626` - Removes a user by ID.

**Arguments:**
- `<users...>` - The user or users to remove from the allowlist.

**Usage:** `<@1275521742961508432>allowlist remove`

### allowlist clear

**Description:** Clears the allowlist.

This disables the allowlist.

**Example:**
- `[p]allowlist clear`

**Usage:** `<@1275521742961508432>allowlist clear`

### blocklist

**Description:** Commands to manage the blocklist.

Use `[p]blocklist clear` to disable the blocklist

**Usage:** `<@1275521742961508432>blocklist`

### blocklist list

**Description:** Lists users on the blocklist.

**Example:**
- `[p]blocklist list`

**Usage:** `<@1275521742961508432>blocklist list`

### blocklist remove

**Description:** Removes users from the blocklist.

**Examples:**
- `[p]blocklist remove @26 @Will` - Removes two users from the blocklist.
- `[p]blocklist remove 262626262626262626` - Removes a user by ID.

**Arguments:**
- `<users...>` - The user or users to remove from the blocklist.

**Usage:** `<@1275521742961508432>blocklist remove`

### blocklist clear

**Description:** Clears the blocklist.

**Example:**
- `[p]blocklist clear`

**Usage:** `<@1275521742961508432>blocklist clear`

### blocklist add

**Description:** Adds users to the blocklist.

**Examples:**
- `[p]blocklist add @26 @Will` - Adds two users to the blocklist.
- `[p]blocklist add 262626262626262626` - Blocks a user by ID.

**Arguments:**
- `<users...>` - The user or users to add to the blocklist.

**Usage:** `<@1275521742961508432>blocklist add`

### localallowlist

**Description:** Commands to manage the server specific allowlist.

Warning: When the allowlist is in use, the bot will ignore commands from everyone not on the list in the server.

Use `[p]localallowlist clear` to disable the allowlist

**Usage:** `<@1275521742961508432>localallowlist`

### localallowlist list

**Description:** Lists users and roles on the server allowlist.

**Example:**
- `[p]localallowlist list`

**Usage:** `<@1275521742961508432>localallowlist list`

### localallowlist clear

**Description:** Clears the allowlist.

This disables the local allowlist and clears all entries.

**Example:**
- `[p]localallowlist clear`

**Usage:** `<@1275521742961508432>localallowlist clear`

### localallowlist add

**Description:** Adds a user or role to the server allowlist.

**Examples:**
- `[p]localallowlist add @26 @Will` - Adds two users to the local allowlist.
- `[p]localallowlist add 262626262626262626` - Allows a user by ID.
- `[p]localallowlist add "Super Admins"` - Allows a role with a space in the name without mentioning.

**Arguments:**
- `<users_or_roles...>` - The users or roles to remove from the local allowlist.

**Usage:** `<@1275521742961508432>localallowlist add`

### localallowlist remove

**Description:** Removes user or role from the allowlist.

The local allowlist will be disabled if all users are removed.

**Examples:**
- `[p]localallowlist remove @26 @Will` - Removes two users from the local allowlist.
- `[p]localallowlist remove 262626262626262626` - Removes a user by ID.
- `[p]localallowlist remove "Super Admins"` - Removes a role with a space in the name without mentioning.

**Arguments:**
- `<users_or_roles...>` - The users or roles to remove from the local allowlist.

**Usage:** `<@1275521742961508432>localallowlist remove`

### localblocklist

**Description:** Commands to manage the server specific blocklist.

Use `[p]localblocklist clear` to disable the blocklist

**Usage:** `<@1275521742961508432>localblocklist`

### localblocklist clear

**Description:** Clears the server blocklist.

This disables the server blocklist and clears all entries.

**Example:**
- `[p]blocklist clear`

**Usage:** `<@1275521742961508432>localblocklist clear`

### localblocklist add

**Description:** Adds a user or role to the local blocklist.

**Examples:**
- `[p]localblocklist add @26 @Will` - Adds two users to the local blocklist.
- `[p]localblocklist add 262626262626262626` - Blocks a user by ID.
- `[p]localblocklist add "Bad Apples"` - Blocks a role with a space in the name without mentioning.

**Arguments:**
- `<users_or_roles...>` - The users or roles to add to the local blocklist.

**Usage:** `<@1275521742961508432>localblocklist add`

### localblocklist list

**Description:** Lists users and roles on the server blocklist.

**Example:**
- `[p]localblocklist list`

**Usage:** `<@1275521742961508432>localblocklist list`

### localblocklist remove

**Description:** Removes user or role from local blocklist.

**Examples:**
- `[p]localblocklist remove @26 @Will` - Removes two users from the local blocklist.
- `[p]localblocklist remove 262626262626262626` - Unblocks a user by ID.
- `[p]localblocklist remove "Bad Apples"` - Unblocks a role with a space in the name without mentioning.

**Arguments:**
- `<users_or_roles...>` - The users or roles to remove from the local blocklist.

**Usage:** `<@1275521742961508432>localblocklist remove`

### command

**Description:** Commands to enable and disable commands and cogs.

**Usage:** `<@1275521742961508432>command`

### command listdisabled

**Description:** List disabled commands.

If you're the bot owner, this will show global disabled commands by default.
Otherwise, this will show disabled commands on the current server.

**Example:**
- `[p]command listdisabled`

**Usage:** `<@1275521742961508432>command listdisabled`

### command listdisabled guild

**Description:** List disabled commands in this server.

**Example:**
- `[p]command listdisabled guild`

**Usage:** `<@1275521742961508432>command listdisabled guild`

### command listdisabled global

**Description:** List disabled commands globally.

**Example:**
- `[p]command listdisabled global`

**Usage:** `<@1275521742961508432>command listdisabled global`

### command defaultenablecog

**Description:** Set the default state for a cog as enabled.

This will re-enable the cog for all servers by default.
To override it, use `[p]command disablecog` on the servers you want to disallow usage.

Note: This will only work on loaded cogs, and must reference the title-case cog name.

**Examples:**
- `[p]command defaultenablecog Economy`
- `[p]command defaultenablecog ModLog`

**Arguments:**
- `<cog>` - The name of the cog to make enabled by default. Must be title-case.

**Usage:** `<@1275521742961508432>command defaultenablecog`

### command enablecog

**Description:** Enable a cog in this server.

Note: This will only work on loaded cogs, and must reference the title-case cog name.

**Examples:**
- `[p]command enablecog Economy`
- `[p]command enablecog ModLog`

**Arguments:**
- `<cog>` - The name of the cog to enable on this server. Must be title-case.

**Usage:** `<@1275521742961508432>command enablecog`

### command enable

**Description:** Enable a command.

If you're the bot owner, this will try to enable a globally disabled command by default.
Otherwise, this will try to enable a command disabled on the current server.

**Examples:**
- `[p]command enable userinfo` - Enables the `userinfo` command in the Mod cog.
- `[p]command enable urban` - Enables the `urban` command in the General cog.

**Arguments:**
- `<command>` - The command to enable.

**Usage:** `<@1275521742961508432>command enable`

### command enable server

**Description:**     Enable a command in this server.

**Examples:**
- `[p]command enable server userinfo` - Enables the `userinfo` command in the Mod cog.
- `[p]command enable server urban` - Enables the `urban` command in the General cog.

**Arguments:**
- `<command>` - The command to enable for the current server.

**Usage:** `<@1275521742961508432>command enable server`

### command enable global

**Description:** Enable a command globally.

**Examples:**
- `[p]command enable global userinfo` - Enables the `userinfo` command in the Mod cog.
- `[p]command enable global urban` - Enables the `urban` command in the General cog.

**Arguments:**
- `<command>` - The command to enable globally.

**Usage:** `<@1275521742961508432>command enable global`

### command disabledmsg

**Description:** Set the bot's response to disabled commands.

Leave blank to send nothing.

To include the command name in the message, include the `{command}` placeholder.

**Examples:**
- `[p]command disabledmsg This command is disabled`
- `[p]command disabledmsg {command} is disabled`
- `[p]command disabledmsg` - Sends nothing when a disabled command is attempted.

**Arguments:**
- `[message]` - The message to send when a disabled command is attempted.

**Usage:** `<@1275521742961508432>command disabledmsg`

### command defaultdisablecog

**Description:** Set the default state for a cog as disabled.

This will disable the cog for all servers by default.
To override it, use `[p]command enablecog` on the servers you want to allow usage.

Note: This will only work on loaded cogs, and must reference the title-case cog name.

**Examples:**
- `[p]command defaultdisablecog Economy`
- `[p]command defaultdisablecog ModLog`

**Arguments:**
- `<cog>` - The name of the cog to make disabled by default. Must be title-case.

**Usage:** `<@1275521742961508432>command defaultdisablecog`

### command disable

**Description:** Disable a command.

If you're the bot owner, this will disable commands globally by default.
Otherwise, this will disable commands on the current server.

**Examples:**
- `[p]command disable userinfo` - Disables the `userinfo` command in the Mod cog.
- `[p]command disable urban` - Disables the `urban` command in the General cog.

**Arguments:**
- `<command>` - The command to disable.

**Usage:** `<@1275521742961508432>command disable`

### command disable global

**Description:** Disable a command globally.

**Examples:**
- `[p]command disable global userinfo` - Disables the `userinfo` command in the Mod cog.
- `[p]command disable global urban` - Disables the `urban` command in the General cog.

**Arguments:**
- `<command>` - The command to disable globally.

**Usage:** `<@1275521742961508432>command disable global`

### command disable server

**Description:** Disable a command in this server only.

**Examples:**
- `[p]command disable server userinfo` - Disables the `userinfo` command in the Mod cog.
- `[p]command disable server urban` - Disables the `urban` command in the General cog.

**Arguments:**
- `<command>` - The command to disable for the current server.

**Usage:** `<@1275521742961508432>command disable server`

### command disablecog

**Description:** Disable a cog in this server.

Note: This will only work on loaded cogs, and must reference the title-case cog name.

**Examples:**
- `[p]command disablecog Economy`
- `[p]command disablecog ModLog`

**Arguments:**
- `<cog>` - The name of the cog to disable on this server. Must be title-case.

**Usage:** `<@1275521742961508432>command disablecog`

### command listdisabledcogs

**Description:** List the cogs which are disabled in this server.

**Example:**
- `[p]command listdisabledcogs`

**Usage:** `<@1275521742961508432>command listdisabledcogs`

### autoimmune

**Description:** Commands to manage server settings for immunity from automated actions.

This includes duplicate message deletion and mention spam from the Mod cog, and filters from the Filter cog.

**Usage:** `<@1275521742961508432>autoimmune`

### autoimmune add

**Description:** Makes a user or role immune from automated moderation actions.

**Examples:**
- `[p]autoimmune add @Twentysix` - Adds a user.
- `[p]autoimmune add @Mods` - Adds a role.

**Arguments:**
- `<user_or_role>` - The user or role to add immunity to.

**Usage:** `<@1275521742961508432>autoimmune add`

### autoimmune list

**Description:** Gets the current members and roles configured for automatic moderation action immunity.

**Example:**
- `[p]autoimmune list`

**Usage:** `<@1275521742961508432>autoimmune list`

### autoimmune remove

**Description:** Remove a user or role from being immune to automated moderation actions.

**Examples:**
- `[p]autoimmune remove @Twentysix` - Removes a user.
- `[p]autoimmune remove @Mods` - Removes a role.

**Arguments:**
- `<user_or_role>` - The user or role to remove immunity from.

**Usage:** `<@1275521742961508432>autoimmune remove`

### autoimmune isimmune

**Description:** Checks if a user or role would be considered immune from automated actions.

**Examples:**
- `[p]autoimmune isimmune @Twentysix`
- `[p]autoimmune isimmune @Mods`

**Arguments:**
- `<user_or_role>` - The user or role to check the immunity of.

**Usage:** `<@1275521742961508432>autoimmune isimmune`

### ignore

**Description:** Commands to add servers or channels to the ignore list.

The ignore list will prevent the bot from responding to commands in the configured locations.

Note: Owners and Admins override the ignore list.

**Usage:** `<@1275521742961508432>ignore`

### ignore channel

**Description:** Ignore commands in the channel, thread, or category.

Defaults to the current thread or channel.

Note: Owners, Admins, and those with Manage Channel permissions override ignored channels.

**Examples:**
- `[p]ignore channel #general` - Ignores commands in the #general channel.
- `[p]ignore channel` - Ignores commands in the current channel.
- `[p]ignore channel "General Channels"` - Use quotes for categories with spaces.
- `[p]ignore channel 356236713347252226` - Also accepts IDs.

**Arguments:**
- `<channel>` - The channel to ignore. This can also be a thread or category channel.

**Usage:** `<@1275521742961508432>ignore channel`

### ignore list

**Description:** List the currently ignored servers and channels.

**Example:**
- `[p]ignore list`

**Usage:** `<@1275521742961508432>ignore list`

### ignore server

**Description:** Ignore commands in this server.

Note: Owners, Admins, and those with Manage Server permissions override ignored servers.

**Example:**
- `[p]ignore server` - Ignores the current server

**Usage:** `<@1275521742961508432>ignore server`

### unignore

**Description:** Commands to remove servers or channels from the ignore list.

**Usage:** `<@1275521742961508432>unignore`

### unignore server

**Description:** Remove this server from the ignore list.

**Example:**
- `[p]unignore server` - Stops ignoring the current server

**Usage:** `<@1275521742961508432>unignore server`

### unignore channel

**Description:** Remove a channel, thread, or category from the ignore list.

Defaults to the current thread or channel.

**Examples:**
- `[p]unignore channel #general` - Unignores commands in the #general channel.
- `[p]unignore channel` - Unignores commands in the current channel.
- `[p]unignore channel "General Channels"` - Use quotes for categories with spaces.
- `[p]unignore channel 356236713347252226` - Also accepts IDs. Use this method to unignore categories.

**Arguments:**
- `<channel>` - The channel to unignore. This can also be a thread or category channel.

**Usage:** `<@1275521742961508432>unignore channel`

### licenseinfo

**Description:** Get info about Red's licenses.

**Usage:** `<@1275521742961508432>licenseinfo`

