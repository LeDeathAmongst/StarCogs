Designates a channel that will send automated messages mimicking your friends using Markov chains. They will have your friends' avatars and nicknames too!<br/>Please use the `[p]simulator info` command for more information.

# ,simulator
Main simulator command. Use me!<br/>
 - Usage: `,simulator`
 - Aliases: `sim`
## ,simulator feed
Feed past messages into the simulator from the configured channels from scratch.<br/>
 - Usage: `,simulator feed [days=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### days: Optional[int] = None
> ```
> A number without decimal places.
> ```
## ,simulator stats
Statistics about the simulator, globally or for a user<br/>
 - Usage: `,simulator stats [user=None]`
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
## ,simulator info
How this works<br/>
 - Usage: `,simulator info`
 - Aliases: `help`
## ,simulator set
Set up your simulator.<br/>
 - Usage: `,simulator set`
### ,simulator set conversationdelay
Simulated conversations will occur randomly according to this value in minutes.<br/>
 - Usage: `,simulator set conversationdelay <minutes>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```
### ,simulator set inputrole
Members must have this role to participate in the simulator.<br/>
 - Usage: `,simulator set inputrole <role>`
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
### ,simulator set showsettings
Show the current simulator settings<br/>
 - Usage: `,simulator set showsettings`
### ,simulator set outputchannel
Set the channel the simulator will run in.<br/>
 - Usage: `,simulator set outputchannel <channel>`
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
### ,simulator set inputchannels
Set a series of channels that will feed the simulator.<br/>
 - Usage: `,simulator set inputchannels <channels>`
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
### ,simulator set commentdelay
Messages will be sent randomly during simulated conversations according to this value in seconds.<br/>
 - Usage: `,simulator set commentdelay <chance>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### chance: int
> ```
> A number without decimal places.
> ```
## ,simulator start
Start the simulator in the configured channel.<br/>
 - Usage: `,simulator start`
 - Restricted to: `BOT_OWNER`
## ,simulator stop
Stop the simulator.<br/>
 - Usage: `,simulator stop`
 - Restricted to: `BOT_OWNER`
## ,simulator count
Count instances of a word, globally or for a user<br/>
 - Usage: `,simulator count <word> [user=None]`
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
# ,dontsimulateme
Excludes you from your messages being read and analyzed by the simulator.<br/>
 - Usage: `,dontsimulateme`
