Roomer
======

<<<<<<< HEAD
# <@1275521742961508432>roomer
Roomer settings<br/>
 - Usage: `<@1275521742961508432>roomer`
=======
# ,roomer
Roomer settings<br/>
 - Usage: `,roomer`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>roomer private
Change settings for private rooms<br/>
 - Usage: `<@1275521742961508432>roomer private`


### <@1275521742961508432>roomer private disable
Disable private rooms<br/>
 - Usage: `<@1275521742961508432>roomer private disable`


### <@1275521742961508432>roomer private startchannel
Set a channel that users will join to start using private rooms.<br/>
I recommend not allowing talking permissions here.<br/>
 - Usage: `<@1275521742961508432>roomer private startchannel <vc>`
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
### <@1275521742961508432>roomer private enable
Enable private rooms<br/>
 - Usage: `<@1275521742961508432>roomer private enable`


## <@1275521742961508432>roomer auto
Automation settings.<br/>
 - Usage: `<@1275521742961508432>roomer auto`


### <@1275521742961508432>roomer auto userlimit
Set the user limit for automatically created voicechannels.<br/>
 - Usage: `<@1275521742961508432>roomer auto userlimit <limit>`
=======
### ,roomer private disable
Disable private rooms<br/>
 - Usage: `,roomer private disable`


## ,roomer auto
Automation settings.<br/>
 - Usage: `,roomer auto`


### ,roomer auto userlimit
Set the user limit for automatically created voicechannels.<br/>
 - Usage: `,roomer auto userlimit <limit>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### limit: Optional[int]
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
### <@1275521742961508432>roomer auto channel
Manage channels related to automated voicechannels.<br/>
 - Usage: `<@1275521742961508432>roomer auto channel`


#### <@1275521742961508432>roomer auto channel add
Add a start channel used for automatic voicechannels.<br/>
 - Usage: `<@1275521742961508432>roomer auto channel add <channel>`
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


#### <@1275521742961508432>roomer auto channel remove
Remove a start channel used for automatic voicechannels.<br/>
 - Usage: `<@1275521742961508432>roomer auto channel remove <channel>`
=======
### ,roomer auto channel
Manage channels related to automated voicechannels.<br/>
 - Usage: `,roomer auto channel`


#### ,roomer auto channel remove
Remove a start channel used for automatic voicechannels.<br/>
 - Usage: `,roomer auto channel remove <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
### <@1275521742961508432>roomer auto disable
Disable automatic voicechannel creation.<br/>
 - Usage: `<@1275521742961508432>roomer auto disable`


### <@1275521742961508432>roomer auto name
Set the name that is used for automatically created voicechannels.<br/>
 - Usage: `<@1275521742961508432>roomer auto name <name>`
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
### <@1275521742961508432>roomer auto enable
Enable automatic voicechannel creation.<br/>
 - Usage: `<@1275521742961508432>roomer auto enable`


## <@1275521742961508432>roomer text
Change settings for private text channels.<br/>
 - Usage: `<@1275521742961508432>roomer text`


### <@1275521742961508432>roomer text disable
Enable private text channels.<br/>
 - Usage: `<@1275521742961508432>roomer text disable`


### <@1275521742961508432>roomer text enable
Enable private text channels.<br/>
 - Usage: `<@1275521742961508432>roomer text enable`


# <@1275521742961508432>vc
Voicechannel commands.<br/>
 - Usage: `<@1275521742961508432>vc`
 - Checks: `server_only`


## <@1275521742961508432>vc join
Join a private room.<br/>
 - Usage: `<@1275521742961508432>vc join <key>`
 - Checks: `server_only`
Extended Arg Info
> ### key: str
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>vc hidden
Hide or unhide a voicechannel you own.<br/>
 - Usage: `<@1275521742961508432>vc hidden [true_or_false=True]`
=======
## ,vc hidden
Hide or unhide a voicechannel you own.<br/>
 - Usage: `,vc hidden [true_or_false=True]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### true_or_false: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>vc create
Create a private voicechannel.<br/>
 - Usage: `<@1275521742961508432>vc create [public=False] <name>`
Extended Arg Info
> ### public: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>tc
Textchannel commands.<br/>
 - Usage: `<@1275521742961508432>tc`
 - Checks: `server_only`


## <@1275521742961508432>tc join
Join a private text channel.<br/>
 - Usage: `<@1275521742961508432>tc join <key>`
=======
## ,vc join
Join a private room.<br/>
 - Usage: `,vc join <key>`
 - Checks: `server_only`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### key: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>tc close
Close the current private text cannel.<br/>
 - Usage: `<@1275521742961508432>tc close`


## <@1275521742961508432>tc create
Create a private text channel.<br/>
 - Usage: `<@1275521742961508432>tc create [public=False] <name>`
=======
# ,tc
Textchannel commands.<br/>
 - Usage: `,tc`
 - Checks: `server_only`


## ,tc create
Create a private text channel.<br/>
 - Usage: `,tc create [public=False] <name>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### public: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
=======
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


>>>>>>> 9e308722 (Revamped and Fixed)
