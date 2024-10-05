Pupper
======

Pet the doggo!

# <@1275521742961508432>pets
Manage your pet.<br/>
 - Usage: `<@1275521742961508432>pets`
 - Restricted to: `MOD`
 - Aliases: `pupper`
 - Checks: `server_only`


## <@1275521742961508432>pets cooldown
Set the pet appearance cooldown in seconds.<br/>

300s/5 minute minimum. Default is 3600s/1 hour.<br/>
 - Usage: `<@1275521742961508432>pets cooldown [seconds=None]`
Extended Arg Info
> ### seconds: int = None
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>pets toggle
Toggle pets on the server.<br/>
 - Usage: `<@1275521742961508432>pets toggle`


## <@1275521742961508432>pets thanks
Set the pet thanks message.<br/>
 - Usage: `<@1275521742961508432>pets thanks [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>pets channel
Channel management for pet appearance.<br/>
 - Usage: `<@1275521742961508432>pets channel`
 - Restricted to: `MOD`
 - Checks: `server_only`


### <@1275521742961508432>pets channel remove
Remove a text channel from petting.<br/>
 - Usage: `<@1275521742961508432>pets channel remove <channel>`
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


### <@1275521742961508432>pets channel add
Add a text channel for pets.<br/>
 - Usage: `<@1275521742961508432>pets channel add <channel>`
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


### <@1275521742961508432>pets channel removeall
Remove all petting channels from the list.<br/>
 - Usage: `<@1275521742961508432>pets channel removeall`


### <@1275521742961508432>pets channel addall
Add all valid channels for the server that the bot can speak in.<br/>
 - Usage: `<@1275521742961508432>pets channel addall`


## <@1275521742961508432>pets delete
Set how long to wait before deleting the thanks message.<br/>
To leave the thanks message with no deletion, use 0 as the amount.<br/>
10 is the default.<br/>
Max is 5 minutes (300).<br/>
 - Usage: `<@1275521742961508432>pets delete [amount=0]`
Extended Arg Info
> ### amount: int = 0
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>pets hello
Set the pet greeting message.<br/>
 - Usage: `<@1275521742961508432>pets hello [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>pets credits
Set the pet credits range on successful petting.<br/>
 - Usage: `<@1275521742961508432>pets credits <min_amt> <max_amt>`
Extended Arg Info
> ### min_amt: int
> ```
> A number without decimal places.
> ```
> ### max_amt: int
> ```
> A number without decimal places.
> ```


