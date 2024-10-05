Bumper
======

A cog for bumping your server to other servers.

# <@1275521742961508432>bumpset
Group command to set bump configuration.<br/>
 - Usage: `<@1275521742961508432>bumpset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## <@1275521742961508432>bumpset channel
Set the bump channel.<br/>
 - Usage: `<@1275521742961508432>bumpset channel <channel>`
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


## <@1275521742961508432>bumpset invite
Set the invite link.<br/>
 - Usage: `<@1275521742961508432>bumpset invite <invite>`
Extended Arg Info
> ### invite: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>bumpset embed_color
Set the embed color.<br/>
 - Usage: `<@1275521742961508432>bumpset embed_color <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## <@1275521742961508432>bumpset thumbnail
Set the thumbnail URL for the bump embed.<br/>
 - Usage: `<@1275521742961508432>bumpset thumbnail <thumbnail_url>`
Extended Arg Info
> ### thumbnail_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>bumpset image
Set the image URL for the bump embed.<br/>
 - Usage: `<@1275521742961508432>bumpset image <image_url>`
Extended Arg Info
> ### image_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>bumpset description
Set the server description (max 1024 characters).<br/>
 - Usage: `<@1275521742961508432>bumpset description <description>`
Extended Arg Info
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>bumpowner
Owner-only bump configuration.<br/>
 - Usage: `<@1275521742961508432>bumpowner`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>bumpowner listprem
List all premium codes and who they are assigned to.<br/>
 - Usage: `<@1275521742961508432>bumpowner listprem`


## <@1275521742961508432>bumpowner support_server_invite
Set the support server invite link.<br/>
 - Usage: `<@1275521742961508432>bumpowner support_server_invite <invite>`
Extended Arg Info
> ### invite: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>bumpowner config_log_channel
Set the channel where configuration logs are sent.<br/>
 - Usage: `<@1275521742961508432>bumpowner config_log_channel <channel>`
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


## <@1275521742961508432>bumpowner bump_log_channel
Set the channel where bump logs are sent.<br/>
 - Usage: `<@1275521742961508432>bumpowner bump_log_channel <channel>`
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


## <@1275521742961508432>bumpowner report_channel
Set the channel where bump reports are sent.<br/>
 - Usage: `<@1275521742961508432>bumpowner report_channel <channel>`
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


# <@1275521742961508432>mycodes
List all premium codes assigned to the user.<br/>
 - Usage: `<@1275521742961508432>mycodes`


# <@1275521742961508432>codegen
Generate premium codes. Use -1 for permanent, or specify time and unit (e.g., 1d for 1 day, 1m for 1 month).<br/>
 - Usage: `<@1275521742961508432>codegen <user_id> <duration> [quantity=1]`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
> ### duration: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### quantity: int = 1
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>revokeprem
Revoke a premium code.<br/>
 - Usage: `<@1275521742961508432>revokeprem <code>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>revokepremserver
Revoke premium status from a server.<br/>
 - Usage: `<@1275521742961508432>revokepremserver <server_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>redeem
Redeem a premium code.<br/>
 - Usage: `<@1275521742961508432>redeem <code>`
 - Checks: `server_only`
Extended Arg Info
> ### code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>bumper
Send the bump message to all servers with a configured bump channel.<br/>
 - Usage: `<@1275521742961508432>bumper`
 - Checks: `server_only`


# <@1275521742961508432>bumprep
Group command for handling bump reports.<br/>
 - Usage: `<@1275521742961508432>bumprep`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>bumprep accept
Accept a reported bump.<br/>
 - Usage: `<@1275521742961508432>bumprep accept <report_message_id>`
Extended Arg Info
> ### report_message_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>bumprep deny
Deny a reported bump.<br/>
 - Usage: `<@1275521742961508432>bumprep deny <report_message_id>`
Extended Arg Info
> ### report_message_id: int
> ```
> A number without decimal places.
> ```


