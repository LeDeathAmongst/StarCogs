Simulator
=========

Designates a channel that will send automated messages mimicking your friends using Markov chains. They will have your friends' avatars and nicknames too!
Please use the `[p]simulator info` command for more information.

# <@1275521742961508432>simulator
Main simulator command. Use me!<br/>
 - Usage: `<@1275521742961508432>simulator`
 - Aliases: `sim`


## <@1275521742961508432>simulator set
Set up your simulator.<br/>
 - Usage: `<@1275521742961508432>simulator set`


### <@1275521742961508432>simulator set showsettings
Show the current simulator settings<br/>
 - Usage: `<@1275521742961508432>simulator set showsettings`


### <@1275521742961508432>simulator set outputchannel
Set the channel the simulator will run in.<br/>
 - Usage: `<@1275521742961508432>simulator set outputchannel <channel>`
 - Restricted to: `BOT_OWNER`
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


### <@1275521742961508432>simulator set inputchannels
Set a series of channels that will feed the simulator.<br/>
 - Usage: `<@1275521742961508432>simulator set inputchannels <channels>`
 - Restricted to: `BOT_OWNER`
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


### <@1275521742961508432>simulator set inputrole
Members must have this role to participate in the simulator.<br/>
 - Usage: `<@1275521742961508432>simulator set inputrole <role>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>simulator set conversationdelay
Simulated conversations will occur randomly according to this value in minutes.<br/>
 - Usage: `<@1275521742961508432>simulator set conversationdelay <minutes>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>simulator set commentdelay
Messages will be sent randomly during simulated conversations according to this value in seconds.<br/>
 - Usage: `<@1275521742961508432>simulator set commentdelay <chance>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### chance: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>simulator stats
Statistics about the simulator, globally or for a user<br/>
 - Usage: `<@1275521742961508432>simulator stats [user=None]`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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


## <@1275521742961508432>simulator feed
Feed past messages into the simulator from the configured channels from scratch.<br/>
 - Usage: `<@1275521742961508432>simulator feed [days=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### days: Optional[int] = None
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>simulator count
Count instances of a word, globally or for a user<br/>
 - Usage: `<@1275521742961508432>simulator count <word> [user=None]`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### user: Optional[discord.member.Member] = None
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


## <@1275521742961508432>simulator info
How this works<br/>
 - Usage: `<@1275521742961508432>simulator info`
 - Aliases: `help`


## <@1275521742961508432>simulator stop
Stop the simulator.<br/>
 - Usage: `<@1275521742961508432>simulator stop`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>simulator start
Start the simulator in the configured channel.<br/>
 - Usage: `<@1275521742961508432>simulator start`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>dontsimulateme
Excludes you from your messages being read and analyzed by the simulator.<br/>
 - Usage: `<@1275521742961508432>dontsimulateme`


