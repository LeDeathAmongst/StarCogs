# ,roomer
Roomer settings<br/>
 - Usage: `,roomer`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## ,roomer private
Change settings for private rooms<br/>
 - Usage: `,roomer private`
### ,roomer private enable
Enable private rooms<br/>
 - Usage: `,roomer private enable`
### ,roomer private startchannel
Set a channel that users will join to start using private rooms.<br/>
I recommend not allowing talking permissions here.<br/>
 - Usage: `,roomer private startchannel <vc>`
Extended Arg Info
> ### vc: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### ,roomer private disable
Disable private rooms<br/>
 - Usage: `,roomer private disable`
## ,roomer auto
Automation settings.<br/>
 - Usage: `,roomer auto`
### ,roomer auto userlimit
Set the user limit for automatically created voicechannels.<br/>
 - Usage: `,roomer auto userlimit <limit>`
Extended Arg Info
> ### limit: Optional[int]
> ```
> A number without decimal places.
> ```
### ,roomer auto channel
Manage channels related to automated voicechannels.<br/>
 - Usage: `,roomer auto channel`
#### ,roomer auto channel remove
Remove a start channel used for automatic voicechannels.<br/>
 - Usage: `,roomer auto channel remove <channel>`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### ,roomer auto channel add
Add a start channel used for automatic voicechannels.<br/>
 - Usage: `,roomer auto channel add <channel>`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### ,roomer auto disable
Disable automatic voicechannel creation.<br/>
 - Usage: `,roomer auto disable`
### ,roomer auto name
Set the name that is used for automatically created voicechannels.<br/>
 - Usage: `,roomer auto name <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,roomer auto enable
Enable automatic voicechannel creation.<br/>
 - Usage: `,roomer auto enable`
## ,roomer text
Change settings for private text channels.<br/>
 - Usage: `,roomer text`
### ,roomer text enable
Enable private text channels.<br/>
 - Usage: `,roomer text enable`
### ,roomer text disable
Enable private text channels.<br/>
 - Usage: `,roomer text disable`
# ,vc
Voicechannel commands.<br/>
 - Usage: `,vc`
 - Checks: `server_only`
## ,vc create
Create a private voicechannel.<br/>
 - Usage: `,vc create [public=False] <name>`
Extended Arg Info
> ### public: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,vc hidden
Hide or unhide a voicechannel you own.<br/>
 - Usage: `,vc hidden [true_or_false=True]`
 - Checks: `server_only`
Extended Arg Info
> ### true_or_false: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,vc join
Join a private room.<br/>
 - Usage: `,vc join <key>`
 - Checks: `server_only`
Extended Arg Info
> ### key: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,tc
Textchannel commands.<br/>
 - Usage: `,tc`
 - Checks: `server_only`
## ,tc create
Create a private text channel.<br/>
 - Usage: `,tc create [public=False] <name>`
Extended Arg Info
> ### public: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,tc close
Close the current private text cannel.<br/>
 - Usage: `,tc close`
## ,tc join
Join a private text channel.<br/>
 - Usage: `,tc join <key>`
Extended Arg Info
> ### key: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
