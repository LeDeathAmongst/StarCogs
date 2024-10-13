A collection of stateless utility commands for getting info about various things.

# /latency (Slash Command)
Return the bot's latency.<br/>
 - Usage: `/latency`
# ,zip
zip a file or files<br/>
 - Usage: `,zip [archive_name]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### archive_name: str = 'archive.zip'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
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
Refresh a todo list channel.<br/>

Bring all messages without a ✅ or ❌ to the front of the channel.<br/>

**WARNING**: DO NOT USE THIS COMMAND IN A BUSY CHANNEL.<br/>
 - Usage: `,todorefresh <confirm>`
 - Restricted to: `MOD`
 - Aliases: `refreshtodo`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,throwerror (Hybrid Command)
Throw an unhandled exception<br/>

A zero division error will be raised<br/>
 - Usage: `,throwerror`
 - Slash Usage: `/throwerror`
 - Restricted to: `BOT_OWNER`
# ,getsource
Get the source code of a command<br/>
 - Usage: `,getsource <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,text2binary
Convert text to binary<br/>
 - Usage: `,text2binary <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,binary2text
Convert a binary string to text<br/>
 - Usage: `,binary2text <binary_string>`
Extended Arg Info
> ### binary_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,randomnum
Generate a random number between the numbers specified<br/>
 - Usage: `,randomnum [minimum=1] [maximum=100]`
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
# ,reactmsg
Add a reaction to a message<br/>
 - Usage: `,reactmsg <emoji> [message=None]`
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
# ,logs
View the bot's logs.<br/>
 - Usage: `,logs [max_pages=50]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### max_pages: int = 50
> ```
> A number without decimal places.
> ```
# ,diskspeed
Get disk R/W performance for the server your bot is on<br/>

The results of this test may vary, Python isn't fast enough for this kind of byte-by-byte writing,<br/>
and the file buffering and similar adds too much overhead.<br/>
Still this can give a good idea of where the bot is at I/O wise.<br/>
 - Usage: `,diskspeed`
 - Restricted to: `BOT_OWNER`
 - Aliases: `diskbench`
# ,isownerof
Get a list of servers the specified user is the owner of<br/>
 - Usage: `,isownerof <user_id>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `ownerof`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
# ,closestuser
Find the closest fuzzy match for a user<br/>
 - Usage: `,closestuser <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,getserverid
Find a server by name or ID<br/>
 - Usage: `,getserverid <query>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `findserver`
Extended Arg Info
> ### query: Union[int, str]
> ```
> A number without decimal places.
> ```
# ,getchannel
Find a channel by ID<br/>
 - Usage: `,getchannel <channel_id>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `findchannel`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### channel_id: int
> ```
> A number without decimal places.
> ```
# ,getmessage
Fetch a channelID-MessageID combo and display the message<br/>
 - Usage: `,getmessage <channel_message>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `findmessage`
 - Checks: `bot_has_server_permissions`
# ,getuser
Find a user by ID<br/>
 - Usage: `,getuser <user_id>`
 - Aliases: `finduser`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
# ,getbanner
Get a user's banner<br/>
 - Usage: `,getbanner [user=None]`
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
# ,getwebhook
Find a webhook by ID<br/>
 - Usage: `,getwebhook <webhook_id>`
Extended Arg Info
> ### webhook_id: int
> ```
> A number without decimal places.
> ```
# ,usersjson
Get a json file containing all non-bot usernames/ID's in this server<br/>
 - Usage: `,usersjson`
 - Restricted to: `BOT_OWNER`
# ,oldestchannels
See which channel is the oldest<br/>
 - Usage: `,oldestchannels [amount=10]`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int = 10
> ```
> A number without decimal places.
> ```
# ,oldestmembers
See which users have been in the server the longest<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
 - Usage: `,oldestmembers [amount=10] [include_bots=False]`
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
# ,oldestaccounts
See which users have the oldest Discord accounts<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
 - Usage: `,oldestaccounts [amount=10] [include_bots=False]`
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
# ,rolemembers
View all members that have a specific role<br/>
 - Usage: `,rolemembers <role>`
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
# ,wipevcs
Clear all voice channels from a server<br/>
 - Usage: `,wipevcs`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
# ,wipethreads
Clear all threads from a server<br/>
 - Usage: `,wipethreads`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
# ,emojidata
Get info about an emoji<br/>
 - Usage: `,emojidata <emoji>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
# ,exportchat
Export chat history to an html file<br/>
 - Usage: `,exportchat [channel=operator.attrgetter('channel')] [limit=50] [tz_info=UTC] [military_time=False]`
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
# ,botemojis
Add/Edit/List/Delete bot emojis<br/>
 - Usage: `,botemojis`
 - Restricted to: `BOT_OWNER`
 - Aliases: `botemoji and bmoji`
## ,botemojis fromemoji
Create a new bot emoji from an existing one<br/>
 - Usage: `,botemojis fromemoji <emoji>`
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
## ,botemojis delete
Delete an bot emoji<br/>
 - Usage: `,botemojis delete <emoji_id>`
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```
## ,botemojis list
List all existing bot emojis<br/>
 - Usage: `,botemojis list`
## ,botemojis add
Create a new emoji from an image attachment<br/>

If a name is not specified, the image's filename will be used<br/>
 - Usage: `,botemojis add [name=None]`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,botemojis edit
Edit a bot emoji's name<br/>
 - Usage: `,botemojis edit <emoji_id> <name>`
Extended Arg Info
> ### emoji_id: int
> ```
> A number without decimal places.
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
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
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,runshell
Run a shell command from within your bots venv<br/>
 - Usage: `,runshell <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,servers
View servers your bot is in<br/>
 - Usage: `,servers`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
# ,botinfo
Get info about the bot<br/>
 - Usage: `,botinfo`
 - Cooldown: `1 per 15.0 seconds`
# ,botip
Get the bots public IP address (in DMs)<br/>
 - Usage: `,botip`
 - Restricted to: `BOT_OWNER`
# ,ispeed
Run an internet speed test.<br/>

Keep in mind that this speedtest is single threaded and may not be accurate!<br/>

Based on PhasecoreX's [netspeed](https://github.com/PhasecoreX/PCXCogs/tree/master/netspeed) cog<br/>
 - Usage: `,ispeed`
 - Restricted to: `BOT_OWNER`
# ,shared
View members in a specified server that are also in this server<br/>
 - Usage: `,shared <server>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: Union[discord.server.Guild, int]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
# ,botshared
View servers that the bot and a user are both in together<br/>

Does not include the server this command is run in<br/>
 - Usage: `,botshared <user>`
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
 - Restricted to: `BOT_OWNER`
