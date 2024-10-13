Pupper
======

Pet the doggo!

# ,pets
Manage your pet.<br/>
 - Usage: `,pets`
 - Restricted to: `MOD`
 - Aliases: `pupper`
 - Checks: `server_only`


## ,pets thanks
Set the pet thanks message.<br/>
 - Usage: `,pets thanks [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,pets credits
Set the pet credits range on successful petting.<br/>
 - Usage: `,pets credits <min_amt> <max_amt>`
Extended Arg Info
> ### min_amt: int
> ```
> A number without decimal places.
> ```
> ### max_amt: int
> ```
> A number without decimal places.
> ```


## ,pets cooldown
Set the pet appearance cooldown in seconds.<br/>

300s/5 minute minimum. Default is 3600s/1 hour.<br/>
 - Usage: `,pets cooldown [seconds=None]`
Extended Arg Info
> ### seconds: int = None
> ```
> A number without decimal places.
> ```


## ,pets toggle
Toggle pets on the server.<br/>
 - Usage: `,pets toggle`


## ,pets delete
Set how long to wait before deleting the thanks message.<br/>
To leave the thanks message with no deletion, use 0 as the amount.<br/>
10 is the default.<br/>
Max is 5 minutes (300).<br/>
 - Usage: `,pets delete [amount=0]`
Extended Arg Info
> ### amount: int = 0
> ```
> A number without decimal places.
> ```


## ,pets channel
Channel management for pet appearance.<br/>
 - Usage: `,pets channel`
 - Restricted to: `MOD`
 - Checks: `server_only`


### ,pets channel removeall
Remove all petting channels from the list.<br/>
 - Usage: `,pets channel removeall`


### ,pets channel add
Add a text channel for pets.<br/>
 - Usage: `,pets channel add <channel>`
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


### ,pets channel addall
Add all valid channels for the server that the bot can speak in.<br/>
 - Usage: `,pets channel addall`


### ,pets channel remove
Remove a text channel from petting.<br/>
 - Usage: `,pets channel remove <channel>`
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


## ,pets hello
Set the pet greeting message.<br/>
 - Usage: `,pets hello [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


