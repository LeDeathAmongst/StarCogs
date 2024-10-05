A heavy-handed hammer for anything that looks like a link.

# <@1275521742961508432>antilinks
Configuration options.<br/>
 - Usage: `<@1275521742961508432>antilinks`
 - Restricted to: `MOD`
 - Aliases: `nolinks, nolink, antilink, and alset`
 - Checks: `server_only`
## <@1275521742961508432>antilinks channel
Set the message transfer channel.<br/>

Leave the channel blank to turn it off.<br/>
 - Usage: `<@1275521742961508432>antilinks channel [channel=None]`
 - Aliases: `chan`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## <@1275521742961508432>antilinks whitelist
Whitelist options.<br/>
 - Usage: `<@1275521742961508432>antilinks whitelist`
### <@1275521742961508432>antilinks whitelist role
Add or remove roles from the whitelist.<br/>
 - Usage: `<@1275521742961508432>antilinks whitelist role <add_or_remove> [roles=None]`
#### <@1275521742961508432>antilinks whitelist role list
List whitelisted roles.<br/>
 - Usage: `<@1275521742961508432>antilinks whitelist role list`
 - Aliases: `view`
### <@1275521742961508432>antilinks whitelist user
Add or remove users from the whitelist.<br/>
 - Usage: `<@1275521742961508432>antilinks whitelist user <add_or_remove> [members=None]`
#### <@1275521742961508432>antilinks whitelist user list
List whitelisted users.<br/>
 - Usage: `<@1275521742961508432>antilinks whitelist user list`
## <@1275521742961508432>antilinks watch
Add/remove/list channels to watch.<br/>

- If added, links will be removed in these channels.<br/>
 - Usage: `<@1275521742961508432>antilinks watch <add_or_remove> [channels=None]`
### <@1275521742961508432>antilinks watch list
List the channels being watched.<br/>
 - Usage: `<@1275521742961508432>antilinks watch list`
