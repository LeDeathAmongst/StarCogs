VrtUtils
========

A collection of stateless utility commands for getting info about various things.

# /latency (Slash Command)
Return the bot's latency.<br/>
 - Usage: `/latency`


<<<<<<< HEAD
# <@1275521742961508432>zip
zip a file or files<br/>
 - Usage: `<@1275521742961508432>zip [archive_name]`
=======
# ,zip
zip a file or files<br/>
 - Usage: `,zip [archive_name]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### archive_name: str = 'archive.zip'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
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
=======
# ,unzip
Unzips a zip file and sends the extracted files in the channel<br/>
 - Usage: `,unzip`
 - Restricted to: `BOT_OWNER`


# ,pull
Auto update & reload cogs<br/>
 - Usage: `,pull <cogs>`
 - Restricted to: `BOT_OWNER`


# ,quickpull
Auto update & reload cogs WITHOUT updating dependencies<br/>
 - Usage: `,quickpull <cogs>`
 - Restricted to: `BOT_OWNER`


# ,todorefresh
>>>>>>> 9e308722 (Revamped and Fixed)
Refresh a todo list channel.<br/>

Bring all messages without a ✅ or ❌ to the front of the channel.<br/>

**WARNING**: DO NOT USE THIS COMMAND IN A BUSY CHANNEL.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>todorefresh <confirm>`
=======
 - Usage: `,todorefresh <confirm>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `refreshtodo`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
# <@1275521742961508432>throwerror (Hybrid Command)
Throw an unhandled exception<br/>

A zero division error will be raised<br/>
 - Usage: `<@1275521742961508432>throwerror`
=======
# ,throwerror (Hybrid Command)
Throw an unhandled exception<br/>

A zero division error will be raised<br/>
 - Usage: `,throwerror`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/throwerror`
 - Restricted to: `BOT_OWNER`


<<<<<<< HEAD
# <@1275521742961508432>getsource
Get the source code of a command<br/>
 - Usage: `<@1275521742961508432>getsource <command>`
=======
# ,getsource
Get the source code of a command<br/>
 - Usage: `,getsource <command>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>text2binary
Convert text to binary<br/>
 - Usage: `<@1275521742961508432>text2binary <text>`
=======
# ,text2binary
Convert text to binary<br/>
 - Usage: `,text2binary <text>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>binary2text
Convert a binary string to text<br/>
 - Usage: `<@1275521742961508432>binary2text <binary_string>`
=======
# ,binary2text
Convert a binary string to text<br/>
 - Usage: `,binary2text <binary_string>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### binary_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>randomnum
Generate a random number between the numbers specified<br/>
 - Usage: `<@1275521742961508432>randomnum [minimum=1] [maximum=100]`
=======
# ,randomnum
Generate a random number between the numbers specified<br/>
 - Usage: `,randomnum [minimum=1] [maximum=100]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>reactmsg
Add a reaction to a message<br/>
 - Usage: `<@1275521742961508432>reactmsg <emoji> [message=None]`
=======
# ,reactmsg
Add a reaction to a message<br/>
 - Usage: `,reactmsg <emoji> [message=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>logs
View the bot's logs.<br/>
 - Usage: `<@1275521742961508432>logs [max_pages=50]`
=======
# ,logs
View the bot's logs.<br/>
 - Usage: `,logs [max_pages=50]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### max_pages: int = 50
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>diskspeed
=======
# ,diskspeed
>>>>>>> 9e308722 (Revamped and Fixed)
Get disk R/W performance for the server your bot is on<br/>

The results of this test may vary, Python isn't fast enough for this kind of byte-by-byte writing,<br/>
and the file buffering and similar adds too much overhead.<br/>
Still this can give a good idea of where the bot is at I/O wise.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>diskspeed`
=======
 - Usage: `,diskspeed`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `diskbench`


<<<<<<< HEAD
# <@1275521742961508432>isownerof
Get a list of servers the specified user is the owner of<br/>
 - Usage: `<@1275521742961508432>isownerof <user_id>`
=======
# ,isownerof
Get a list of servers the specified user is the owner of<br/>
 - Usage: `,isownerof <user_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `ownerof`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>closestuser
Find the closest fuzzy match for a user<br/>
 - Usage: `<@1275521742961508432>closestuser <query>`
=======
# ,closestuser
Find the closest fuzzy match for a user<br/>
 - Usage: `,closestuser <query>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>getserverid
Find a server by name or ID<br/>
 - Usage: `<@1275521742961508432>getserverid <query>`
=======
# ,getserverid
Find a server by name or ID<br/>
 - Usage: `,getserverid <query>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `findserver`
Extended Arg Info
> ### query: Union[int, str]
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>getchannel
Find a channel by ID<br/>
 - Usage: `<@1275521742961508432>getchannel <channel_id>`
=======
# ,getchannel
Find a channel by ID<br/>
 - Usage: `,getchannel <channel_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `findchannel`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### channel_id: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>getmessage
Fetch a channelID-MessageID combo and display the message<br/>
 - Usage: `<@1275521742961508432>getmessage <channel_message>`
=======
# ,getmessage
Fetch a channelID-MessageID combo and display the message<br/>
 - Usage: `,getmessage <channel_message>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `findmessage`
 - Checks: `bot_has_server_permissions`


<<<<<<< HEAD
# <@1275521742961508432>getuser
Find a user by ID<br/>
 - Usage: `<@1275521742961508432>getuser <user_id>`
=======
# ,getuser
Find a user by ID<br/>
 - Usage: `,getuser <user_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `finduser`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>getbanner
Get a user's banner<br/>
 - Usage: `<@1275521742961508432>getbanner [user=None]`
=======
# ,getbanner
Get a user's banner<br/>
 - Usage: `,getbanner [user=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>getwebhook
Find a webhook by ID<br/>
 - Usage: `<@1275521742961508432>getwebhook <webhook_id>`
=======
# ,getwebhook
Find a webhook by ID<br/>
 - Usage: `,getwebhook <webhook_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### webhook_id: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>usersjson
Get a json file containing all non-bot usernames/ID's in this server<br/>
 - Usage: `<@1275521742961508432>usersjson`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>oldestchannels
See which channel is the oldest<br/>
 - Usage: `<@1275521742961508432>oldestchannels [amount=10]`
=======
# ,usersjson
Get a json file containing all non-bot usernames/ID's in this server<br/>
 - Usage: `,usersjson`
 - Restricted to: `BOT_OWNER`


# ,oldestchannels
See which channel is the oldest<br/>
 - Usage: `,oldestchannels [amount=10]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### amount: int = 10
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>oldestmembers
=======
# ,oldestmembers
>>>>>>> 9e308722 (Revamped and Fixed)
See which users have been in the server the longest<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>oldestmembers [amount=10] [include_bots=False]`
=======
 - Usage: `,oldestmembers [amount=10] [include_bots=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>oldestaccounts
=======
# ,oldestaccounts
>>>>>>> 9e308722 (Revamped and Fixed)
See which users have the oldest Discord accounts<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>oldestaccounts [amount=10] [include_bots=False]`
=======
 - Usage: `,oldestaccounts [amount=10] [include_bots=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>rolemembers
View all members that have a specific role<br/>
 - Usage: `<@1275521742961508432>rolemembers <role>`
=======
# ,rolemembers
View all members that have a specific role<br/>
 - Usage: `,rolemembers <role>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>wipevcs
Clear all voice channels from a server<br/>
 - Usage: `<@1275521742961508432>wipevcs`
=======
# ,wipevcs
Clear all voice channels from a server<br/>
 - Usage: `,wipevcs`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>wipethreads
Clear all threads from a server<br/>
 - Usage: `<@1275521742961508432>wipethreads`
=======
# ,wipethreads
Clear all threads from a server<br/>
 - Usage: `,wipethreads`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>emojidata
Get info about an emoji<br/>
 - Usage: `<@1275521742961508432>emojidata <emoji>`
=======
# ,emojidata
Get info about an emoji<br/>
 - Usage: `,emojidata <emoji>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>exportchat
Export chat history to an html file<br/>
 - Usage: `<@1275521742961508432>exportchat [channel=operator.attrgetter('channel')] [limit=50] [tz_info=UTC] [military_time=False]`
=======
# ,exportchat
Export chat history to an html file<br/>
 - Usage: `,exportchat [channel=operator.attrgetter('channel')] [limit=50] [tz_info=UTC] [military_time=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>botemojis
Add/Edit/List/Delete bot emojis<br/>
 - Usage: `<@1275521742961508432>botemojis`
=======
# ,botemojis
Add/Edit/List/Delete bot emojis<br/>
 - Usage: `,botemojis`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `botemoji and bmoji`


<<<<<<< HEAD
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
=======
## ,botemojis fromemoji
Create a new bot emoji from an existing one<br/>
 - Usage: `,botemojis fromemoji <emoji>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>botemojis list
List all existing bot emojis<br/>
 - Usage: `<@1275521742961508432>botemojis list`


## <@1275521742961508432>botemojis delete
Delete an bot emoji<br/>
 - Usage: `<@1275521742961508432>botemojis delete <emoji_id>`
=======
## ,botemojis delete
Delete an bot emoji<br/>
 - Usage: `,botemojis delete <emoji_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>botemojis add
Create a new emoji from an image attachment<br/>

If a name is not specified, the image's filename will be used<br/>
 - Usage: `<@1275521742961508432>botemojis add [name=None]`
=======
## ,botemojis list
List all existing bot emojis<br/>
 - Usage: `,botemojis list`


## ,botemojis add
Create a new emoji from an image attachment<br/>

If a name is not specified, the image's filename will be used<br/>
 - Usage: `,botemojis add [name=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>botemojis edit
Edit a bot emoji's name<br/>
 - Usage: `<@1275521742961508432>botemojis edit <emoji_id> <name>`
=======
## ,botemojis edit
Edit a bot emoji's name<br/>
 - Usage: `,botemojis edit <emoji_id> <name>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>pip
Run a pip command from within your bots venv<br/>
 - Usage: `<@1275521742961508432>pip <command>`
=======
## ,botemojis get
Get details about a bot emoji<br/>
 - Usage: `,botemojis get <emoji_id>`
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```


# ,pip
Run a pip command from within your bots venv<br/>
 - Usage: `,pip <command>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>runshell
Run a shell command from within your bots venv<br/>
 - Usage: `<@1275521742961508432>runshell <command>`
=======
# ,runshell
Run a shell command from within your bots venv<br/>
 - Usage: `,runshell <command>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>servers
View servers your bot is in<br/>
 - Usage: `<@1275521742961508432>servers`
=======
# ,servers
View servers your bot is in<br/>
 - Usage: `,servers`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>botinfo
Get info about the bot<br/>
 - Usage: `<@1275521742961508432>botinfo`
 - Cooldown: `1 per 15.0 seconds`


# <@1275521742961508432>botip
Get the bots public IP address (in DMs)<br/>
 - Usage: `<@1275521742961508432>botip`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>ispeed
=======
# ,botinfo
Get info about the bot<br/>
 - Usage: `,botinfo`
 - Cooldown: `1 per 15.0 seconds`


# ,botip
Get the bots public IP address (in DMs)<br/>
 - Usage: `,botip`
 - Restricted to: `BOT_OWNER`


# ,ispeed
>>>>>>> 9e308722 (Revamped and Fixed)
Run an internet speed test.<br/>

Keep in mind that this speedtest is single threaded and may not be accurate!<br/>

Based on PhasecoreX's [netspeed](https://github.com/PhasecoreX/PCXCogs/tree/master/netspeed) cog<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>ispeed`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>shared
View members in a specified server that are also in this server<br/>
 - Usage: `<@1275521742961508432>shared <server>`
=======
 - Usage: `,ispeed`
 - Restricted to: `BOT_OWNER`


# ,shared
View members in a specified server that are also in this server<br/>
 - Usage: `,shared <server>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: Union[discord.server.Guild, int]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>botshared
View servers that the bot and a user are both in together<br/>

Does not include the server this command is run in<br/>
 - Usage: `<@1275521742961508432>botshared <user>`
=======
# ,botshared
View servers that the bot and a user are both in together<br/>

Does not include the server this command is run in<br/>
 - Usage: `,botshared <user>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
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
=======
# ,viewapikeys
DM yourself the bot's API keys<br/>
 - Usage: `,viewapikeys`
 - Restricted to: `BOT_OWNER`


# ,cleantmp
Cleanup all the `.tmp` files left behind by Red's config<br/>
 - Usage: `,cleantmp`
 - Restricted to: `BOT_OWNER`


# ,cogsizes
View the storage space each cog's saved data is taking up<br/>
 - Usage: `,cogsizes`
 - Restricted to: `BOT_OWNER`


# ,codesizes
View the storage space each cog's code is taking up<br/>
 - Usage: `,codesizes`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`


