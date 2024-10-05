SecureInv
=========

# <@1275521742961508432>inv
Create one or several invites with the specified parameters.<br/>

For specifying unlimited days or uses, use 0.<br/>

Defaults can be set with `<@1275521742961508432>inv set`.<br/>
If no defaults are found, channel defaults to the current channel,<br/>
days defaults to 1, and uses defaults to 0 (infinite).<br/>

Uses will always be finite if days is infinite.<br/>
 - Usage: `<@1275521742961508432>inv [channel=None] [days=None] [uses=None] [amount=None] [reason]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>inv set
Configure or view the server's default inv settings.<br/>
 - Usage: `<@1275521742961508432>inv set`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


### <@1275521742961508432>inv set days
Set or clear the default amount of days an `<@1275521742961508432>inv` lasts for.<br/>

Set to 0 for unlimited days.<br/>
 - Usage: `<@1275521742961508432>inv set days [days]`


### <@1275521742961508432>inv set channel
Set or clear the default channel an `<@1275521742961508432>inv` directs to.<br/>
 - Usage: `<@1275521742961508432>inv set channel [channel]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### <@1275521742961508432>inv set uses
Set or clear the default amount of times an `<@1275521742961508432>inv` can be used.<br/>

Set to 0 for unlimited uses.<br/>
 - Usage: `<@1275521742961508432>inv set uses [uses]`


