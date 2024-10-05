Events
======

Host and manage events in your server with a variety of customization options.

Create an event, set a channel for submissions and entry requirements/options.
Users can enter the event and make submissions according to the parameters set.

# <@1275521742961508432>enotify
Enable/Disable event notifications for yourself<br/>

You will be notified when events start and end<br/>
 - Usage: `<@1275521742961508432>enotify`
 - Checks: `server_only`


# <@1275521742961508432>enter
Enter an event if one exists<br/>
 - Usage: `<@1275521742961508432>enter`
 - Checks: `server_only`


# <@1275521742961508432>events
Create, manage and view events<br/>
 - Usage: `<@1275521742961508432>events`
 - Checks: `server_only`


## <@1275521742961508432>events staffrole
Add/Remove staff roles<br/>

If ping staff is enabled, these roles will be pinged on event completion<br/>
 - Usage: `<@1275521742961508432>events staffrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>events resultdelete
(Toggle) Include event results in the messages to delete on cleanup<br/>

If this is on when an event is deleted and the user chooses to clean up the messages,<br/>
the results announcement will also be deleted<br/>
 - Usage: `<@1275521742961508432>events resultdelete`


## <@1275521742961508432>events create
Create a new event<br/>
 - Usage: `<@1275521742961508432>events create`


## <@1275521742961508432>events delete
Delete an event outright<br/>
 - Usage: `<@1275521742961508432>events delete`


## <@1275521742961508432>events view
View the current events and settings<br/>
 - Usage: `<@1275521742961508432>events view`


## <@1275521742961508432>events remove
Remove a user from an active event<br/>
 - Usage: `<@1275521742961508432>events remove <user>`
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


## <@1275521742961508432>events autodelete
(Toggle) Auto delete events from config when they complete<br/>

If auto delete is enabled, the messages in the event channel will need to be cleaned up manually<br/>
 - Usage: `<@1275521742961508432>events autodelete`


## <@1275521742961508432>events emoji
Set the default emoji for votes<br/>

Changing the vote emoji only affects events created after this is changed.<br/>
Existing events will still use the previous emoji for votes<br/>
 - Usage: `<@1275521742961508432>events emoji <emoji>`
Extended Arg Info
> ### emoji: Optional[discord.emoji.Emoji]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>events end
End an event early, counting votes/announcing the winner<br/>

This will also delete the event afterwards<br/>
 - Usage: `<@1275521742961508432>events end`


## <@1275521742961508432>events shorten
Shorten the runtime of an event<br/>

**Examples**<br/>
`10d` - 10 days<br/>
`7d4h` - 7 days 4 hours<br/>
 - Usage: `<@1275521742961508432>events shorten <time_string>`
Extended Arg Info
> ### time_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>events pingstaff
(Toggle) Ping staff on event completion<br/>
 - Usage: `<@1275521742961508432>events pingstaff`


## <@1275521742961508432>events blacklistuser
Add/Remove blacklisted users<br/>

These users are not allowed to enter events, but can still vote on them<br/>
 - Usage: `<@1275521742961508432>events blacklistuser <user>`
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


## <@1275521742961508432>events extend
Extend the runtime of an event<br/>

**Examples**<br/>
`10d` - 10 days<br/>
`7d4h` - 7 days 4 hours<br/>
 - Usage: `<@1275521742961508432>events extend <time_string>`
Extended Arg Info
> ### time_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>events blacklistrole
Add/Remove blacklisted roles<br/>

These roles are not allowed to enter events, but can still vote on them<br/>
 - Usage: `<@1275521742961508432>events blacklistrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>events notifyrole
Add/Remove notify roles<br/>

These roles will be pinged on event start and completion<br/>
 - Usage: `<@1275521742961508432>events notifyrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


