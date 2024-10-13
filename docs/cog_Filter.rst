Filter
======

This cog is designed for "filtering" unwanted words and phrases from a server.

It provides tools to manage a list of words or sentences, and to customize automatic actions to be taken against users who use those words in channels or in their name/nickname.

This can be used to prevent inappropriate language, off-topic discussions, invite links, and more.

<<<<<<< HEAD
# <@1275521742961508432>filterset
Base command to manage filter settings.<br/>
 - Usage: `<@1275521742961508432>filterset`
=======
# ,filterset
Base command to manage filter settings.<br/>
 - Usage: `,filterset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>filterset ban
=======
## ,filterset ban
>>>>>>> 9e308722 (Revamped and Fixed)
Set the filter's autoban conditions.<br/>

Users will be banned if they send `<count>` filtered words in<br/>
`<timeframe>` seconds.<br/>

Set both to zero to disable autoban.<br/>

Examples:<br/>
<<<<<<< HEAD
- `<@1275521742961508432>filterset ban 5 5` - Ban users who say 5 filtered words in 5 seconds.<br/>
- `<@1275521742961508432>filterset ban 2 20` - Ban users who say 2 filtered words in 20 seconds.<br/>
=======
- `,filterset ban 5 5` - Ban users who say 5 filtered words in 5 seconds.<br/>
- `,filterset ban 2 20` - Ban users who say 2 filtered words in 20 seconds.<br/>
>>>>>>> 9e308722 (Revamped and Fixed)

**Arguments:**<br/>

- `<count>` The amount of filtered words required to trigger a ban.<br/>
- `<timeframe>` The period of time in which too many filtered words will trigger a ban.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>filterset ban <count> <timeframe>`
=======
 - Usage: `,filterset ban <count> <timeframe>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### count: int
> ```
> A number without decimal places.
> ```
> ### timeframe: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>filterset defaultname
Set the nickname for users with a filtered name.<br/>

Note that this has no effect if filtering names is disabled<br/>
(to toggle, run `<@1275521742961508432>filter names`).<br/>
=======
## ,filterset defaultname
Set the nickname for users with a filtered name.<br/>

Note that this has no effect if filtering names is disabled<br/>
(to toggle, run `,filter names`).<br/>
>>>>>>> 9e308722 (Revamped and Fixed)

The default name used is *John Doe*.<br/>

Example:<br/>
<<<<<<< HEAD
- `<@1275521742961508432>filterset defaultname Missingno`<br/>
=======
- `,filterset defaultname Missingno`<br/>
>>>>>>> 9e308722 (Revamped and Fixed)

**Arguments:**<br/>

- `<name>` The new nickname to assign.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>filterset defaultname <name>`
=======
 - Usage: `,filterset defaultname <name>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>filter
Base command to add or remove words from the server filter.<br/>

Use double quotes to add or remove sentences.<br/>
 - Usage: `<@1275521742961508432>filter`
=======
# ,filter
Base command to add or remove words from the server filter.<br/>

Use double quotes to add or remove sentences.<br/>
 - Usage: `,filter`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>filter add
Add words to the filter.<br/>

Use double quotes to add sentences.<br/>

Examples:<br/>
- `<@1275521742961508432>filter add word1 word2 word3`<br/>
- `<@1275521742961508432>filter add "This is a sentence"`<br/>

**Arguments:**<br/>

- `[words...]` The words or sentences to filter.<br/>
 - Usage: `<@1275521742961508432>filter add <words>`
Extended Arg Info
> ### *words: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>filter clear
Clears this server's filter list.<br/>
 - Usage: `<@1275521742961508432>filter clear`


## <@1275521742961508432>filter channel
Base command to add or remove words from the channel filter.<br/>

Use double quotes to add or remove sentences.<br/>
 - Usage: `<@1275521742961508432>filter channel`


### <@1275521742961508432>filter channel clear
Clears this channel's filter list.<br/>
 - Usage: `<@1275521742961508432>filter channel clear`


### <@1275521742961508432>filter channel add
=======
## ,filter channel
Base command to add or remove words from the channel filter.<br/>

Use double quotes to add or remove sentences.<br/>
 - Usage: `,filter channel`


### ,filter channel delete
Remove words from the filter.<br/>

Use double quotes to remove sentences.<br/>

Examples:<br/>
- `,filter channel remove #channel word1 word2 word3`<br/>
- `,filter channel remove #channel "This is a sentence"`<br/>

**Arguments:**<br/>

- `<channel>` The text, voice, stage, or forum channel to add filtered words to.<br/>
- `[words...]` The words or sentences to no longer filter.<br/>
 - Usage: `,filter channel delete <channel> <words>`
 - Aliases: `remove and del`
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
> ### *words: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,filter channel clear
Clears this channel's filter list.<br/>
 - Usage: `,filter channel clear`


### ,filter channel list
Send a list of the channel's filtered words.<br/>
 - Usage: `,filter channel list`


### ,filter channel add
>>>>>>> 9e308722 (Revamped and Fixed)
Add words to the filter.<br/>

Use double quotes to add sentences.<br/>

Examples:<br/>
<<<<<<< HEAD
- `<@1275521742961508432>filter channel add #channel word1 word2 word3`<br/>
- `<@1275521742961508432>filter channel add #channel "This is a sentence"`<br/>
=======
- `,filter channel add #channel word1 word2 word3`<br/>
- `,filter channel add #channel "This is a sentence"`<br/>
>>>>>>> 9e308722 (Revamped and Fixed)

**Arguments:**<br/>

- `<channel>` The text, voice, stage, or forum channel to add filtered words to.<br/>
- `[words...]` The words or sentences to filter.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>filter channel add <channel> <words>`
=======
 - Usage: `,filter channel add <channel> <words>`
>>>>>>> 9e308722 (Revamped and Fixed)
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
> ### *words: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
### <@1275521742961508432>filter channel list
Send a list of the channel's filtered words.<br/>
 - Usage: `<@1275521742961508432>filter channel list`


### <@1275521742961508432>filter channel delete
=======
## ,filter add
Add words to the filter.<br/>

Use double quotes to add sentences.<br/>

Examples:<br/>
- `,filter add word1 word2 word3`<br/>
- `,filter add "This is a sentence"`<br/>

**Arguments:**<br/>

- `[words...]` The words or sentences to filter.<br/>
 - Usage: `,filter add <words>`
Extended Arg Info
> ### *words: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,filter list
Send a list of this server's filtered words.<br/>
 - Usage: `,filter list`


## ,filter clear
Clears this server's filter list.<br/>
 - Usage: `,filter clear`


## ,filter delete
>>>>>>> 9e308722 (Revamped and Fixed)
Remove words from the filter.<br/>

Use double quotes to remove sentences.<br/>

Examples:<br/>
<<<<<<< HEAD
- `<@1275521742961508432>filter channel remove #channel word1 word2 word3`<br/>
- `<@1275521742961508432>filter channel remove #channel "This is a sentence"`<br/>

**Arguments:**<br/>

- `<channel>` The text, voice, stage, or forum channel to add filtered words to.<br/>
- `[words...]` The words or sentences to no longer filter.<br/>
 - Usage: `<@1275521742961508432>filter channel delete <channel> <words>`
 - Aliases: `remove and del`
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
=======
- `,filter remove word1 word2 word3`<br/>
- `,filter remove "This is a sentence"`<br/>

**Arguments:**<br/>

- `[words...]` The words or sentences to no longer filter.<br/>
 - Usage: `,filter delete <words>`
 - Aliases: `remove and del`
Extended Arg Info
>>>>>>> 9e308722 (Revamped and Fixed)
> ### *words: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>filter names
Toggle name and nickname filtering.<br/>

This is disabled by default.<br/>
 - Usage: `<@1275521742961508432>filter names`


## <@1275521742961508432>filter delete
Remove words from the filter.<br/>

Use double quotes to remove sentences.<br/>

Examples:<br/>
- `<@1275521742961508432>filter remove word1 word2 word3`<br/>
- `<@1275521742961508432>filter remove "This is a sentence"`<br/>

**Arguments:**<br/>

- `[words...]` The words or sentences to no longer filter.<br/>
 - Usage: `<@1275521742961508432>filter delete <words>`
 - Aliases: `remove and del`
Extended Arg Info
> ### *words: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>filter list
Send a list of this server's filtered words.<br/>
 - Usage: `<@1275521742961508432>filter list`
=======
## ,filter names
Toggle name and nickname filtering.<br/>

This is disabled by default.<br/>
 - Usage: `,filter names`
>>>>>>> 9e308722 (Revamped and Fixed)


