Trickle credits into your Economy<br/><br/>More detailed docs: <https://cogs.yamikaitou.dev/economytrickle.html>

# <@1275521742961508432>economytrickle
Configure various settings<br/>
 - Usage: `<@1275521742961508432>economytrickle`
 - Restricted to: `ADMIN`
 - Aliases: `trickleset`
 - Checks: `is_owner_if_bank_global`
## <@1275521742961508432>economytrickle showblocks
Provide a list of channels that are on the blocklist for this server<br/>
 - Usage: `<@1275521742961508432>economytrickle showblocks`
 - Restricted to: `ADMIN`
 - Aliases: `showblock`
 - Checks: `server_only`
## <@1275521742961508432>economytrickle voice
Set the number of credits to grant every minute<br/>

Set the number to 0 to disable<br/>
Max value is 1000<br/>
 - Usage: `<@1275521742961508432>economytrickle voice <number>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>economytrickle credits
Set the number of credits to grant<br/>

Set the number to 0 to disable<br/>
Max value is 1000<br/>
 - Usage: `<@1275521742961508432>economytrickle credits <number>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>economytrickle settings
Show the current settings<br/>
 - Usage: `<@1275521742961508432>economytrickle settings`
 - Restricted to: `ADMIN`
 - Aliases: `info and showsettings`
 - Checks: `is_owner_if_bank_global`
## <@1275521742961508432>economytrickle messages
Set the number of messages required to gain credits<br/>

Set the number to 0 to disable<br/>
Max value is 100<br/>
 - Usage: `<@1275521742961508432>economytrickle messages <number>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>economytrickle blocklist
Add/Remove the current channel (or a specific channel) to the blocklist<br/>

Not passing a channel will add/remove the channel you ran the command in to the blocklist<br/>
 - Usage: `<@1275521742961508432>economytrickle blocklist [channel=None]`
 - Restricted to: `ADMIN`
 - Aliases: `blacklist`
 - Checks: `server_only`
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
