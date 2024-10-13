A heavy-handed hammer for anything that looks like a link.

# ,antilinks
Configuration options.<br/>
 - Usage: `,antilinks`
 - Restricted to: `MOD`
 - Aliases: `nolinks, nolink, antilink, and alset`
 - Checks: `server_only`
## ,antilinks watch
Add/remove/list channels to watch.<br/>

- If added, links will be removed in these channels.<br/>
 - Usage: `,antilinks watch <add_or_remove> [channels=None]`
### ,antilinks watch list
List the channels being watched.<br/>
 - Usage: `,antilinks watch list`
## ,antilinks whitelist
Whitelist options.<br/>
 - Usage: `,antilinks whitelist`
### ,antilinks whitelist user
Add or remove users from the whitelist.<br/>
 - Usage: `,antilinks whitelist user <add_or_remove> [members=None]`
#### ,antilinks whitelist user list
List whitelisted users.<br/>
 - Usage: `,antilinks whitelist user list`
### ,antilinks whitelist role
Add or remove roles from the whitelist.<br/>
 - Usage: `,antilinks whitelist role <add_or_remove> [roles=None]`
#### ,antilinks whitelist role list
List whitelisted roles.<br/>
 - Usage: `,antilinks whitelist role list`
 - Aliases: `view`
## ,antilinks channel
Set the message transfer channel.<br/>

Leave the channel blank to turn it off.<br/>
 - Usage: `,antilinks channel [channel=None]`
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
