Remove messages containing links and warn users for it.

# ,linkwarner
Settings for LinkWarner cog.<br/>
 - Usage: `,linkwarner`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
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
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### ,linkwarner excludedroles remove
Remove roles that will be excluded from getting filtered.<br/>
 - Usage: `,linkwarner excludedroles remove <roles>`
 - Aliases: `delete`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,linkwarner state
Set if LinkWarner should be enabled for this server.<br/>

If used without a setting, this will show the current state.<br/>
 - Usage: `,linkwarner state <new_state>`
Extended Arg Info
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,linkwarner unsetmessage
Unset link warning message.<br/>
 - Usage: `,linkwarner unsetmessage`
## ,linkwarner domains
Configuration for allowed/disallowed domains in the server.<br/>
 - Usage: `,linkwarner domains`
### ,linkwarner domains add
Add domains to the domains list.<br/>

Note: The cog is using exact matching for domain names<br/>
which means that domain names like youtube.com and www.youtube.com<br/>
are treated as 2 different domains.<br/>

Example:<br/>
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
Set if LinkWarner should use DMs for warning messages.<br/>

Note: This is NOT recommended as the user might block the bot or all DMs<br/>
from the server and the warning might not get sent to the offender at all.<br/>
This also means that the bot is more likely to get ratelimited for repeatedly<br/>
trying to DM the user when they spam links.<br/>

If you're trying to minimize spam that the warning messages cause,<br/>
you should consider enabling delete delay instead.<br/>
 - Usage: `,linkwarner usedms <new_state>`
Extended Arg Info
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
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
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
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
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
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
