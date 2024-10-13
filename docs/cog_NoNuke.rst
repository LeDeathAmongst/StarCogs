NoNuke
======

Anti-Nuke System for lazy server owners!

Monitors the following events:
Kicks/Bans/Unbans/Prunes
Channel Creation/Edit/Deletion
Role Creation/Edit/Deletion
Emoji Creation/Edit/Deletion
Sticker Creation/Edit/Deletion
Webhook Creation/Edit/Deletion
Member role/nickname updates

Set a cooldown(in seconds)
Set an overload count(X events in X seconds)
Set an action(kick, ban, strip, notify)

If a user or bot exceeds X mod events within X seconds, the set action will be performed.

- Any dangerous permissions added to a role will be logged.
- If the vanity URL is changed, it will be logged.

# ,nonuke
Anti-Nuke System for lazy server owners!<br/>

Monitors the following events:<br/>
Kicks & Bans<br/>
Channel Creation/Edit/Deletion<br/>
Role Creation/Edit/Deletion<br/>

Set a cooldown(in seconds)<br/>
Set an overload count(X events in X seconds)<br/>
Set an action(kick, ban, strip, notify)<br/>

If a user or bot exceeds X mod events within X seconds, the set action will be performed<br/>
 - Usage: `,nonuke`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


## ,nonuke overload
How many mod actions can be done within the set cooldown<br/>

**Mod actions include:**<br/>
Kicks & Bans<br/>
Channel Creation/Edit/Deletion<br/>
Role Creation/Edit/Deletion<br/>
 - Usage: `,nonuke overload <overload>`
Extended Arg Info
> ### overload: int
> ```
> A number without decimal places.
> ```


## ,nonuke logchannel
Set the log channel for Anti-Nuke kicks<br/>
 - Usage: `,nonuke logchannel <channel>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,nonuke dm
Toggle whether the bot sends the user a DM when a kick or ban action is performed<br/>
 - Usage: `,nonuke dm`


## ,nonuke ignorebots
Toggle whether other bots are ignored<br/>

**NOTE:** Bot specific roles (the role created when the bot joins) cannot be removed.<br/>
If NoNuke is set to strip roles, and a bot triggers it while having an integrated role, NoNuke will fail<br/>
to remove the role from it.<br/>
 - Usage: `,nonuke ignorebots`


## ,nonuke enable
Enable/Disable the NoNuke system<br/>
 - Usage: `,nonuke enable`


## ,nonuke view
View the NoNuke settings<br/>
 - Usage: `,nonuke view`


## ,nonuke action
Set the action for the bot to take when NoNuke is triggered<br/>

**Actions**<br/>
`kick` - kick the user<br/>
`ban` - ban the user<br/>
`strip` - strip all roles with permissions from user<br/>
`notify` - just sends a report to the log channel<br/>
 - Usage: `,nonuke action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,nonuke whitelist
Add/Remove users from the whitelist<br/>
 - Usage: `,nonuke whitelist <user>`
Extended Arg Info
> ### user: discord.member.Member
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     


## ,nonuke cooldown
Cooldown (in seconds) for NoNuke to trigger<br/>
 - Usage: `,nonuke cooldown <cooldown>`
Extended Arg Info
> ### cooldown: int
> ```
> A number without decimal places.
> ```


