KoFiTracker
===========

Track donations, subscriptions and shop orders on KoFi!

<<<<<<< HEAD
# <@1275521742961508432>kofiprofile (Hybrid Command)
Get the details of a KoFi profile.<br/>
 - Usage: `<@1275521742961508432>kofiprofile <kofi_page_url>`
=======
# ,kofiprofile (Hybrid Command)
Get the details of a KoFi profile.<br/>
 - Usage: `,kofiprofile <kofi_page_url>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/kofiprofile <kofi_page_url>`
Extended Arg Info
> ### kofi_page_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>setkofitracker (Hybrid Command)
Commands to configure KoFiTracker.<br/>
 - Usage: `<@1275521742961508432>setkofitracker`
=======
# ,setkofitracker (Hybrid Command)
Commands to configure KoFiTracker.<br/>
 - Usage: `,setkofitracker`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setkofitracker`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>setkofitracker add (Hybrid Command)
Add a KoFi page to track.<br/>

⚠ **Note:** If you choose to show personal details, the user's email and shipping details will be shown to everyone in the channel.<br/>
 - Usage: `<@1275521742961508432>setkofitracker add <channel> <kofi_page_url> <verification_token> [types=['Donation', 'Subscription', 'Shop Order']] [show_private=False] [show_personal_details=False]`
=======
## ,setkofitracker instructions (Hybrid Command)
Instructions on how to set up KoFiTracker.<br/>
 - Usage: `,setkofitracker instructions`
 - Slash Usage: `/setkofitracker instructions`
 - Checks: `server_only`


## ,setkofitracker add (Hybrid Command)
Add a KoFi page to track.<br/>

⚠ **Note:** If you choose to show personal details, the user's email and shipping details will be shown to everyone in the channel.<br/>
 - Usage: `,setkofitracker add <channel> <kofi_page_url> <verification_token> [types=['Donation', 'Subscription', 'Shop Order']] [show_private=False] [show_personal_details=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setkofitracker add <channel> <kofi_page_url> <verification_token> [types=['Donation', 'Subscription', 'Shop Order']] [show_private=False] [show_personal_details=False]`
 - Aliases: `+`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### kofi_page_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### verification_token: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### show_private: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_personal_details: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setkofitracker remove (Hybrid Command)
Remove a KoFi page from tracking.<br/>
 - Usage: `<@1275521742961508432>setkofitracker remove <channel> <kofi_page_url>`
=======
## ,setkofitracker remove (Hybrid Command)
Remove a KoFi page from tracking.<br/>
 - Usage: `,setkofitracker remove <channel> <kofi_page_url>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setkofitracker remove <channel> <kofi_page_url>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### kofi_page_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setkofitracker instructions (Hybrid Command)
Instructions on how to set up KoFiTracker.<br/>
 - Usage: `<@1275521742961508432>setkofitracker instructions`
 - Slash Usage: `/setkofitracker instructions`
 - Checks: `server_only`


## <@1275521742961508432>setkofitracker list (Hybrid Command)
List the KoFi pages being tracked.<br/>
 - Usage: `<@1275521742961508432>setkofitracker list <channel>`
=======
## ,setkofitracker list (Hybrid Command)
List the KoFi pages being tracked.<br/>
 - Usage: `,setkofitracker list <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setkofitracker list <channel>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


