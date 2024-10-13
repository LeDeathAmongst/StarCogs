LinkWarner
==========

Remove messages containing links and warn users for it.

<<<<<<< HEAD
# <@1275521742961508432>linkwarner
Settings for LinkWarner cog.<br/>
 - Usage: `<@1275521742961508432>linkwarner`
=======
# ,linkwarner
Settings for LinkWarner cog.<br/>
 - Usage: `,linkwarner`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>linkwarner channel
Channel-specific settings for LinkWarner.<br/>
 - Usage: `<@1275521742961508432>linkwarner channel`


### <@1275521742961508432>linkwarner channel unsetmessage
Unset link warning message for provided channel.<br/>
 - Usage: `<@1275521742961508432>linkwarner channel unsetmessage <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### <@1275521742961508432>linkwarner channel setmessage
Set link warning message for provided channel.<br/>

Those fields will get replaced automatically:<br/>
$mention - Mention the user who sent the message with a link<br/>
$username - The user's display name<br/>
$server - The name of the server<br/>
 - Usage: `<@1275521742961508432>linkwarner channel setmessage <channel> <message>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>linkwarner channel domains
Configuration for allowed/disallowed domains in the specific channel.<br/>
 - Usage: `<@1275521742961508432>linkwarner channel domains`


#### <@1275521742961508432>linkwarner channel domains clear
Clear domains from the domains list of the provided channel.<br/>
 - Usage: `<@1275521742961508432>linkwarner channel domains clear <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
=======
## ,linkwarner deletedelay
Set the delete delay (in seconds) for the warning message.<br/>

Use `,linkwarner deletedelay disable` to disable auto-deletion.<br/>

Note: This does not work when the warning messages are sent through DMs.<br/>
 - Usage: `,linkwarner deletedelay <new_value>`
Extended Arg Info
> ### new_value: int
> ```
> A number without decimal places.
> ```


### ,linkwarner deletedelay disable
Disable auto-deletion of the warning messages.<br/>
 - Usage: `,linkwarner deletedelay disable`


## ,linkwarner excludedroles
Settings for roles that are excluded from getting filtered.<br/>
 - Usage: `,linkwarner excludedroles`


### ,linkwarner excludedroles add
Add roles that will be excluded from getting filtered.<br/>
 - Usage: `,linkwarner excludedroles add <roles>`
Extended Arg Info
> ### *roles: discord.role.Role
>>>>>>> 9e308722 (Revamped and Fixed)
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
<<<<<<< HEAD
>     3. Lookup by channel URL.
>     4. Lookup by name
=======
>     3. Lookup by name
>>>>>>> 9e308722 (Revamped and Fixed)
> 
>     


<<<<<<< HEAD
#### <@1275521742961508432>linkwarner channel domains setmode
Change current domains list mode.<br/>

Available modes:<br/>
`0` - Inherit the server setting and use domains<br/>
      from both server's and channel's domain list.<br/>
`1` - Only domains on the channel's domains list can be sent.<br/>
`2` - All domains can be sent except the ones on the channel's domains list.<br/>
 - Usage: `<@1275521742961508432>linkwarner channel domains setmode <channel> <new_mode>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


#### <@1275521742961508432>linkwarner channel domains remove
Remove domains from the domains list of the provided channel.<br/>

Example:<br/>
`<@1275521742961508432>linkwarner channel domains remove #channel youtube.com discord.com`<br/>
 - Usage: `<@1275521742961508432>linkwarner channel domains remove <channel> <domains>`
 - Aliases: `delete`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
=======
### ,linkwarner excludedroles remove
Remove roles that will be excluded from getting filtered.<br/>
 - Usage: `,linkwarner excludedroles remove <roles>`
 - Aliases: `delete`
Extended Arg Info
> ### *roles: discord.role.Role
>>>>>>> 9e308722 (Revamped and Fixed)
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
<<<<<<< HEAD
>     3. Lookup by channel URL.
>     4. Lookup by name
=======
>     3. Lookup by name
>>>>>>> 9e308722 (Revamped and Fixed)
> 
>     


<<<<<<< HEAD
#### <@1275521742961508432>linkwarner channel domains add
Add domains to the domains list of the provided channel.<br/>

Note: The cog is using exact matching for domain names<br/>
which means that domain names like youtube.com and www.youtube.com<br/>
are treated as 2 different domains.<br/>

Example:<br/>
`<@1275521742961508432>linkwarner channel domains add #channel youtube.com discord.com`<br/>
 - Usage: `<@1275521742961508432>linkwarner channel domains add <channel> <domains>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### <@1275521742961508432>linkwarner channel ignore
Set if LinkWarner should ignore links in provided channel.<br/>
 - Usage: `<@1275521742961508432>linkwarner channel ignore <channel> <new_state>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>linkwarner channel showsettings
Show settings for the given channel.<br/>
 - Usage: `<@1275521742961508432>linkwarner channel showsettings <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>linkwarner state
Set if LinkWarner should be enabled for this server.<br/>

If used without a setting, this will show the current state.<br/>
 - Usage: `<@1275521742961508432>linkwarner state <new_state>`
=======
## ,linkwarner state
Set if LinkWarner should be enabled for this server.<br/>

If used without a setting, this will show the current state.<br/>
 - Usage: `,linkwarner state <new_state>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>linkwarner unsetmessage
Unset link warning message.<br/>
 - Usage: `<@1275521742961508432>linkwarner unsetmessage`


## <@1275521742961508432>linkwarner domains
Configuration for allowed/disallowed domains in the server.<br/>
 - Usage: `<@1275521742961508432>linkwarner domains`


### <@1275521742961508432>linkwarner domains setmode
Change current domains list mode.<br/>

Available modes:<br/>
`1` - Only domains on the domains list can be sent.<br/>
`2` - All domains can be sent except the ones on the domains list.<br/>
 - Usage: `<@1275521742961508432>linkwarner domains setmode <new_mode>`


### <@1275521742961508432>linkwarner domains remove
Remove domains from the domains list.<br/>

Example:<br/>
`<@1275521742961508432>linkwarner domains remove youtube.com discord.com`<br/>
 - Usage: `<@1275521742961508432>linkwarner domains remove <domains>`
 - Aliases: `delete`


### <@1275521742961508432>linkwarner domains add
=======
## ,linkwarner unsetmessage
Unset link warning message.<br/>
 - Usage: `,linkwarner unsetmessage`


## ,linkwarner domains
Configuration for allowed/disallowed domains in the server.<br/>
 - Usage: `,linkwarner domains`


### ,linkwarner domains add
>>>>>>> 9e308722 (Revamped and Fixed)
Add domains to the domains list.<br/>

Note: The cog is using exact matching for domain names<br/>
which means that domain names like youtube.com and www.youtube.com<br/>
are treated as 2 different domains.<br/>

Example:<br/>
<<<<<<< HEAD
`<@1275521742961508432>linkwarner domains add google.com youtube.com`<br/>
 - Usage: `<@1275521742961508432>linkwarner domains add <domains>`


### <@1275521742961508432>linkwarner domains clear
Clear domains from the domains list.<br/>
 - Usage: `<@1275521742961508432>linkwarner domains clear`


## <@1275521742961508432>linkwarner setmessage
Set link warning message.<br/>

Those fields will get replaced automatically:<br/>
$mention - Mention the user who sent the message with a link<br/>
$username - The user's display name<br/>
$server - The name of the server<br/>
 - Usage: `<@1275521742961508432>linkwarner setmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>linkwarner usedms
=======
`,linkwarner domains add google.com youtube.com`<br/>
 - Usage: `,linkwarner domains add <domains>`


### ,linkwarner domains clear
Clear domains from the domains list.<br/>
 - Usage: `,linkwarner domains clear`


### ,linkwarner domains remove
Remove domains from the domains list.<br/>

Example:<br/>
`,linkwarner domains remove youtube.com discord.com`<br/>
 - Usage: `,linkwarner domains remove <domains>`
 - Aliases: `delete`


### ,linkwarner domains setmode
Change current domains list mode.<br/>

Available modes:<br/>
`1` - Only domains on the domains list can be sent.<br/>
`2` - All domains can be sent except the ones on the domains list.<br/>
 - Usage: `,linkwarner domains setmode <new_mode>`


## ,linkwarner usedms
>>>>>>> 9e308722 (Revamped and Fixed)
Set if LinkWarner should use DMs for warning messages.<br/>

Note: This is NOT recommended as the user might block the bot or all DMs<br/>
from the server and the warning might not get sent to the offender at all.<br/>
This also means that the bot is more likely to get ratelimited for repeatedly<br/>
trying to DM the user when they spam links.<br/>

If you're trying to minimize spam that the warning messages cause,<br/>
you should consider enabling delete delay instead.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>linkwarner usedms <new_state>`
=======
 - Usage: `,linkwarner usedms <new_state>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>linkwarner deletedelay
Set the delete delay (in seconds) for the warning message.<br/>

Use `<@1275521742961508432>linkwarner deletedelay disable` to disable auto-deletion.<br/>

Note: This does not work when the warning messages are sent through DMs.<br/>
 - Usage: `<@1275521742961508432>linkwarner deletedelay <new_value>`
Extended Arg Info
> ### new_value: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>linkwarner deletedelay disable
Disable auto-deletion of the warning messages.<br/>
 - Usage: `<@1275521742961508432>linkwarner deletedelay disable`


## <@1275521742961508432>linkwarner excludedroles
Settings for roles that are excluded from getting filtered.<br/>
 - Usage: `<@1275521742961508432>linkwarner excludedroles`


### <@1275521742961508432>linkwarner excludedroles add
Add roles that will be excluded from getting filtered.<br/>
 - Usage: `<@1275521742961508432>linkwarner excludedroles add <roles>`
Extended Arg Info
> ### *roles: discord.role.Role
=======
## ,linkwarner setmessage
Set link warning message.<br/>

Those fields will get replaced automatically:<br/>
$mention - Mention the user who sent the message with a link<br/>
$username - The user's display name<br/>
$server - The name of the server<br/>
 - Usage: `,linkwarner setmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,linkwarner showsettings
Show settings for the current server.<br/>
 - Usage: `,linkwarner showsettings`


## ,linkwarner channel
Channel-specific settings for LinkWarner.<br/>
 - Usage: `,linkwarner channel`


### ,linkwarner channel showsettings
Show settings for the given channel.<br/>
 - Usage: `,linkwarner channel showsettings <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
>>>>>>> 9e308722 (Revamped and Fixed)
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
<<<<<<< HEAD
>     3. Lookup by name
=======
>     3. Lookup by channel URL.
>     4. Lookup by name
>>>>>>> 9e308722 (Revamped and Fixed)
> 
>     


<<<<<<< HEAD
### <@1275521742961508432>linkwarner excludedroles remove
Remove roles that will be excluded from getting filtered.<br/>
 - Usage: `<@1275521742961508432>linkwarner excludedroles remove <roles>`
 - Aliases: `delete`
Extended Arg Info
> ### *roles: discord.role.Role
=======
### ,linkwarner channel unsetmessage
Unset link warning message for provided channel.<br/>
 - Usage: `,linkwarner channel unsetmessage <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### ,linkwarner channel setmessage
Set link warning message for provided channel.<br/>

Those fields will get replaced automatically:<br/>
$mention - Mention the user who sent the message with a link<br/>
$username - The user's display name<br/>
$server - The name of the server<br/>
 - Usage: `,linkwarner channel setmessage <channel> <message>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,linkwarner channel domains
Configuration for allowed/disallowed domains in the specific channel.<br/>
 - Usage: `,linkwarner channel domains`


#### ,linkwarner channel domains clear
Clear domains from the domains list of the provided channel.<br/>
 - Usage: `,linkwarner channel domains clear <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


#### ,linkwarner channel domains setmode
Change current domains list mode.<br/>

Available modes:<br/>
`0` - Inherit the server setting and use domains<br/>
      from both server's and channel's domain list.<br/>
`1` - Only domains on the channel's domains list can be sent.<br/>
`2` - All domains can be sent except the ones on the channel's domains list.<br/>
 - Usage: `,linkwarner channel domains setmode <channel> <new_mode>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


#### ,linkwarner channel domains add
Add domains to the domains list of the provided channel.<br/>

Note: The cog is using exact matching for domain names<br/>
which means that domain names like youtube.com and www.youtube.com<br/>
are treated as 2 different domains.<br/>

Example:<br/>
`,linkwarner channel domains add #channel youtube.com discord.com`<br/>
 - Usage: `,linkwarner channel domains add <channel> <domains>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


#### ,linkwarner channel domains remove
Remove domains from the domains list of the provided channel.<br/>

Example:<br/>
`,linkwarner channel domains remove #channel youtube.com discord.com`<br/>
 - Usage: `,linkwarner channel domains remove <channel> <domains>`
 - Aliases: `delete`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
>>>>>>> 9e308722 (Revamped and Fixed)
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
<<<<<<< HEAD
>     3. Lookup by name
=======
>     3. Lookup by channel URL.
>     4. Lookup by name
>>>>>>> 9e308722 (Revamped and Fixed)
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>linkwarner showsettings
Show settings for the current server.<br/>
 - Usage: `<@1275521742961508432>linkwarner showsettings`
=======
### ,linkwarner channel ignore
Set if LinkWarner should ignore links in provided channel.<br/>
 - Usage: `,linkwarner channel ignore <channel> <new_state>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
>>>>>>> 9e308722 (Revamped and Fixed)


