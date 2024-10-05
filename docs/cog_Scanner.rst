Scanner
=======

Scan images as they are sent through according to the set models.

# <@1275521742961508432>scanner
Group command for changing scanner's settings.<br/>
 - Usage: `<@1275521742961508432>scanner`
 - Restricted to: `ADMIN`


## <@1275521742961508432>scanner settings
View registered settings<br/>
 - Usage: `<@1275521742961508432>scanner settings`


## <@1275521742961508432>scanner lists
Manage whitelist and blacklists for Scanner cog.<br/>
 - Usage: `<@1275521742961508432>scanner lists`


### <@1275521742961508432>scanner lists blacklist
Blacklist channels from the scanner.<br/>

Blacklisted channels will NOT be checked for rule-violating pictures.<br/>
 - Usage: `<@1275521742961508432>scanner lists blacklist`


#### <@1275521742961508432>scanner lists blacklist add
Add channels to the blacklist<br/>
 - Usage: `<@1275521742961508432>scanner lists blacklist add <channels>`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


#### <@1275521742961508432>scanner lists blacklist clear
Removes all channels from the blacklist<br/>
 - Usage: `<@1275521742961508432>scanner lists blacklist clear`


#### <@1275521742961508432>scanner lists blacklist remove
Remove channels from the blacklist<br/>
 - Usage: `<@1275521742961508432>scanner lists blacklist remove <channels>`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### <@1275521742961508432>scanner lists whitelist
Whitelist channels from the scanner.<br/>

Whitelisted channels will be the ONLY channels checked for rule violating pictures<br/>
 - Usage: `<@1275521742961508432>scanner lists whitelist`


#### <@1275521742961508432>scanner lists whitelist remove
Remove channels from the whitelist<br/>
 - Usage: `<@1275521742961508432>scanner lists whitelist remove <channels>`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


#### <@1275521742961508432>scanner lists whitelist clear
Removes all channels from the whitelist<br/>
 - Usage: `<@1275521742961508432>scanner lists whitelist clear`


#### <@1275521742961508432>scanner lists whitelist add
Add channels to the whitelist<br/>
 - Usage: `<@1275521742961508432>scanner lists whitelist add <channels>`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>scanner detect
Group command for changing what the scanner cog detects.<br/>
 - Usage: `<@1275521742961508432>scanner detect`


### <@1275521742961508432>scanner detect wad
Set whether or not to check for WAD content in images.<br/>

WAD stands for Weapons, Alcohol and Drugs<br/>
 - Usage: `<@1275521742961508432>scanner detect wad <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>scanner detect nude
Set whether or not to check for nude content in images.<br/>
 - Usage: `<@1275521742961508432>scanner detect nude <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>scanner detect tm
Manage settings for Text Moderation in pictures.<br/>
 - Usage: `<@1275521742961508432>scanner detect tm`
 - Aliases: `textmoderation`


#### <@1275521742961508432>scanner detect tm checks
Manage the various profanities to check for in Text Moderation in images.<br/>
 - Usage: `<@1275521742961508432>scanner detect tm checks`


##### <@1275521742961508432>scanner detect tm checks remove
Removes checks from the Text Moderation check<br/>
 - Usage: `<@1275521742961508432>scanner detect tm checks remove <checks>`
Extended Arg Info
> ### *checks: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


##### <@1275521742961508432>scanner detect tm checks add
Adds checks to the Text Moderation check.<br/>

Must be `sexual`, `insult`, `disciminatory`, `innapropriate`, `other_profanity`, `email`, `ipv4`, `ipv6`, `phone_number_us`, `phone_number_uk`, `phone_number_fr` or `ssn`.<br/>
 - Usage: `<@1275521742961508432>scanner detect tm checks add <checks>`
Extended Arg Info
> ### *checks: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


##### <@1275521742961508432>scanner detect tm checks clear
Removes all channels from the whitelist<br/>
 - Usage: `<@1275521742961508432>scanner detect tm checks clear`


#### <@1275521742961508432>scanner detect tm enable
Set whether or not to check for Text Mderation in images.<br/>
 - Usage: `<@1275521742961508432>scanner detect tm enable <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>scanner detect mm
Manage settings for Message Moderation.<br/>
 - Usage: `<@1275521742961508432>scanner detect mm`
 - Aliases: `messagemoderation`


#### <@1275521742961508432>scanner detect mm enable
Set whether or not to check for Message Mderation.<br/>
 - Usage: `<@1275521742961508432>scanner detect mm enable <yes_or_no>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


#### <@1275521742961508432>scanner detect mm checks
Manage the various types to check for in Message Moderation.<br/>
 - Usage: `<@1275521742961508432>scanner detect mm checks`


##### <@1275521742961508432>scanner detect mm checks clear
Removes all checks from Message Moderation<br/>
 - Usage: `<@1275521742961508432>scanner detect mm checks clear`


##### <@1275521742961508432>scanner detect mm checks remove
Removes checks from the Message Moderation check<br/>
 - Usage: `<@1275521742961508432>scanner detect mm checks remove <checks>`
Extended Arg Info
> ### *checks: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


##### <@1275521742961508432>scanner detect mm checks add
Adds checks to the Message Moderation check.<br/>

Must be `sexual`, `insult`, `disciminatory`, `innapropriate`, `other_profanity`, `email`, `ipv4`, `ipv6`, `phone_number_us`, `phone_number_uk`, `phone_number_fr` or `ssn`.<br/>
 - Usage: `<@1275521742961508432>scanner detect mm checks add <checks>`
Extended Arg Info
> ### *checks: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>scanner detect offensive
Set whether or not to check for offensive content in images.<br/>

Offensive content includes content such as middle fingers, offensive flags or offensive groups of people.<br/>
 - Usage: `<@1275521742961508432>scanner detect offensive <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>scanner detect partial
Set whether or not messages will be reported be they contain partial nudity.<br/>

Note that the nude toggle must be turned on for this to work.<br/>
 - Usage: `<@1275521742961508432>scanner detect partial <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>scanner detect scammer
Set whether or not to check for scammer content in images.<br/>

By scammer content it checks for verified scammers in the picture.<br/>
 - Usage: `<@1275521742961508432>scanner detect scammer <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>scanner report
Manage how reports are handled, and base reasons for deletion for messages being deleted.<br/>
 - Usage: `<@1275521742961508432>scanner report`


### <@1275521742961508432>scanner report channel
Set the channel for reports to go to.<br/>
 - Usage: `<@1275521742961508432>scanner report channel <channel>`
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


### <@1275521742961508432>scanner report mentionuser
Add or remove users from being mentioned when a report is sent.<br/>
 - Usage: `<@1275521742961508432>scanner report mentionuser [user]`
Extended Arg Info
> ### user: discord.member.Member = None
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


### <@1275521742961508432>scanner report percent
Set the percent a picture must have in order to be violating.  100 means full violation, 0 is no violation<br/>
 - Usage: `<@1275521742961508432>scanner report percent <percent>`
Extended Arg Info
> ### percent: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>scanner report autodelete
Set whether the messages should be auto deleted and reported or just reported.<br/>
 - Usage: `<@1275521742961508432>scanner report autodelete <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>scanner report mentionrole
Add or remove roles from being mentioned when a report is sent.<br/>
 - Usage: `<@1275521742961508432>scanner report mentionrole [role]`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>scanner report showpic
Set whether or not to show the violating picture in the report.<br/>
 - Usage: `<@1275521742961508432>scanner report showpic <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>scanner creds
Set the API user and API secret to use with requests from sightengine.com.<br/>
 - Usage: `<@1275521742961508432>scanner creds <user> <secret>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### secret
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


