VrtUtils
========

A collection of stateless utility commands for getting info about various things.

# /latency (Slash Command)
Return the bot's latency.<br/>
 - Usage: `/latency`


# <@1275521742961508432>zip
zip a file or files<br/>
 - Usage: `<@1275521742961508432>zip [archive_name]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### archive_name: str = 'archive.zip'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>unzip
Unzips a zip file and sends the extracted files in the channel<br/>
 - Usage: `<@1275521742961508432>unzip`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>pull
Auto update & reload cogs<br/>
 - Usage: `<@1275521742961508432>pull <cogs>`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>quickpull
Auto update & reload cogs WITHOUT updating dependencies<br/>
 - Usage: `<@1275521742961508432>quickpull <cogs>`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>todorefresh
Refresh a todo list channel.<br/>

Bring all messages without a ✅ or ❌ to the front of the channel.<br/>

**WARNING**: DO NOT USE THIS COMMAND IN A BUSY CHANNEL.<br/>
 - Usage: `<@1275521742961508432>todorefresh <confirm>`
 - Restricted to: `MOD`
 - Aliases: `refreshtodo`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>throwerror (Hybrid Command)
Throw an unhandled exception<br/>

A zero division error will be raised<br/>
 - Usage: `<@1275521742961508432>throwerror`
 - Slash Usage: `/throwerror`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>getsource
Get the source code of a command<br/>
 - Usage: `<@1275521742961508432>getsource <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>text2binary
Convert text to binary<br/>
 - Usage: `<@1275521742961508432>text2binary <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>binary2text
Convert a binary string to text<br/>
 - Usage: `<@1275521742961508432>binary2text <binary_string>`
Extended Arg Info
> ### binary_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>randomnum
Generate a random number between the numbers specified<br/>
 - Usage: `<@1275521742961508432>randomnum [minimum=1] [maximum=100]`
 - Aliases: `rnum`
Extended Arg Info
> ### minimum: int = 1
> ```
> A number without decimal places.
> ```
> ### maximum: int = 100
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>reactmsg
Add a reaction to a message<br/>
 - Usage: `<@1275521742961508432>reactmsg <emoji> [message=None]`
 - Restricted to: `MOD`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### message: discord.message.Message = None
> Converts to a :class:`discord.Message`.
> 
>     


# <@1275521742961508432>logs
View the bot's logs.<br/>
 - Usage: `<@1275521742961508432>logs [max_pages=50]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### max_pages: int = 50
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>diskspeed
Get disk R/W performance for the server your bot is on<br/>

The results of this test may vary, Python isn't fast enough for this kind of byte-by-byte writing,<br/>
and the file buffering and similar adds too much overhead.<br/>
Still this can give a good idea of where the bot is at I/O wise.<br/>
 - Usage: `<@1275521742961508432>diskspeed`
 - Restricted to: `BOT_OWNER`
 - Aliases: `diskbench`


# <@1275521742961508432>isownerof
Get a list of servers the specified user is the owner of<br/>
 - Usage: `<@1275521742961508432>isownerof <user_id>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `ownerof`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>closestuser
Find the closest fuzzy match for a user<br/>
 - Usage: `<@1275521742961508432>closestuser <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>getserverid
Find a server by name or ID<br/>
 - Usage: `<@1275521742961508432>getserverid <query>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `findserver`
Extended Arg Info
> ### query: Union[int, str]
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>getchannel
Find a channel by ID<br/>
 - Usage: `<@1275521742961508432>getchannel <channel_id>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `findchannel`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### channel_id: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>getmessage
Fetch a channelID-MessageID combo and display the message<br/>
 - Usage: `<@1275521742961508432>getmessage <channel_message>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `findmessage`
 - Checks: `bot_has_server_permissions`


# <@1275521742961508432>getuser
Find a user by ID<br/>
 - Usage: `<@1275521742961508432>getuser <user_id>`
 - Aliases: `finduser`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>getbanner
Get a user's banner<br/>
 - Usage: `<@1275521742961508432>getbanner [user=None]`
Extended Arg Info
> ### user: Union[discord.member.Member, int, NoneType] = None
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


# <@1275521742961508432>getwebhook
Find a webhook by ID<br/>
 - Usage: `<@1275521742961508432>getwebhook <webhook_id>`
Extended Arg Info
> ### webhook_id: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>usersjson
Get a json file containing all non-bot usernames/ID's in this server<br/>
 - Usage: `<@1275521742961508432>usersjson`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>oldestchannels
See which channel is the oldest<br/>
 - Usage: `<@1275521742961508432>oldestchannels [amount=10]`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int = 10
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>oldestmembers
See which users have been in the server the longest<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
 - Usage: `<@1275521742961508432>oldestmembers [amount=10] [include_bots=False]`
 - Aliases: `oldestusers`
 - Checks: `server_only`
Extended Arg Info
> ### amount: Optional[int] = 10
> ```
> A number without decimal places.
> ```
> ### include_bots: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>oldestaccounts
See which users have the oldest Discord accounts<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
 - Usage: `<@1275521742961508432>oldestaccounts [amount=10] [include_bots=False]`
 - Checks: `server_only`
Extended Arg Info
> ### amount: Optional[int] = 10
> ```
> A number without decimal places.
> ```
> ### include_bots: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>rolemembers
View all members that have a specific role<br/>
 - Usage: `<@1275521742961508432>rolemembers <role>`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


# <@1275521742961508432>wipevcs
Clear all voice channels from a server<br/>
 - Usage: `<@1275521742961508432>wipevcs`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


# <@1275521742961508432>wipethreads
Clear all threads from a server<br/>
 - Usage: `<@1275521742961508432>wipethreads`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


# <@1275521742961508432>emojidata
Get info about an emoji<br/>
 - Usage: `<@1275521742961508432>emojidata <emoji>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


# <@1275521742961508432>exportchat
Export chat history to an html file<br/>
 - Usage: `<@1275521742961508432>exportchat [channel=operator.attrgetter('channel')] [limit=50] [tz_info=UTC] [military_time=False]`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### channel: discord.channel.TextChannel = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### limit: int = 50
> ```
> A number without decimal places.
> ```
> ### tz_info: str = 'UTC'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### military_time: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


# <@1275521742961508432>botemojis
Add/Edit/List/Delete bot emojis<br/>
 - Usage: `<@1275521742961508432>botemojis`
 - Restricted to: `BOT_OWNER`
 - Aliases: `botemoji and bmoji`


## <@1275521742961508432>botemojis get
Get details about a bot emoji<br/>
 - Usage: `<@1275521742961508432>botemojis get <emoji_id>`
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>botemojis fromemoji
Create a new bot emoji from an existing one<br/>
 - Usage: `<@1275521742961508432>botemojis fromemoji <emoji>`
 - Aliases: `addfrom and addemoji`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>botemojis list
List all existing bot emojis<br/>
 - Usage: `<@1275521742961508432>botemojis list`


## <@1275521742961508432>botemojis delete
Delete an bot emoji<br/>
 - Usage: `<@1275521742961508432>botemojis delete <emoji_id>`
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>botemojis add
Create a new emoji from an image attachment<br/>

If a name is not specified, the image's filename will be used<br/>
 - Usage: `<@1275521742961508432>botemojis add [name=None]`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>botemojis edit
Edit a bot emoji's name<br/>
 - Usage: `<@1275521742961508432>botemojis edit <emoji_id> <name>`
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>pip
Run a pip command from within your bots venv<br/>
 - Usage: `<@1275521742961508432>pip <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>runshell
Run a shell command from within your bots venv<br/>
 - Usage: `<@1275521742961508432>runshell <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>servers
View servers your bot is in<br/>
 - Usage: `<@1275521742961508432>servers`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


# <@1275521742961508432>botinfo
Get info about the bot<br/>
 - Usage: `<@1275521742961508432>botinfo`
 - Cooldown: `1 per 15.0 seconds`


# <@1275521742961508432>botip
Get the bots public IP address (in DMs)<br/>
 - Usage: `<@1275521742961508432>botip`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>ispeed
Run an internet speed test.<br/>

Keep in mind that this speedtest is single threaded and may not be accurate!<br/>

Based on PhasecoreX's [netspeed](https://github.com/PhasecoreX/PCXCogs/tree/master/netspeed) cog<br/>
 - Usage: `<@1275521742961508432>ispeed`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>shared
View members in a specified server that are also in this server<br/>
 - Usage: `<@1275521742961508432>shared <server>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: Union[discord.server.Guild, int]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     


# <@1275521742961508432>botshared
View servers that the bot and a user are both in together<br/>

Does not include the server this command is run in<br/>
 - Usage: `<@1275521742961508432>botshared <user>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user: Union[discord.member.Member, discord.user.User]
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


# <@1275521742961508432>viewapikeys
DM yourself the bot's API keys<br/>
 - Usage: `<@1275521742961508432>viewapikeys`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>cleantmp
Cleanup all the `.tmp` files left behind by Red's config<br/>
 - Usage: `<@1275521742961508432>cleantmp`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>cogsizes
View the storage space each cog's saved data is taking up<br/>
 - Usage: `<@1275521742961508432>cogsizes`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>codesizes
View the storage space each cog's code is taking up<br/>
 - Usage: `<@1275521742961508432>codesizes`
 - Restricted to: `BOT_OWNER`


