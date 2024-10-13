A complex cog for managing global ban lists across multiple Discord servers.

# ,globalbanlistowner
Group command for Global Ban List owner settings.<br/>
 - Usage: `,globalbanlistowner`
 - Restricted to: `BOT_OWNER`
 - Aliases: `gblo`
## ,globalbanlistowner setownerlog
Set the channel for owner logging.<br/>
 - Usage: `,globalbanlistowner setownerlog <channel>`
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
## ,globalbanlistowner refreshlists
Manually refresh the embeds for a specific list or all lists.<br/>
 - Usage: `,globalbanlistowner refreshlists [list_name=None]`
Extended Arg Info
> ### list_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,globalbanlistowner remauth
Remove a user from the authorized users list.<br/>
 - Usage: `,globalbanlistowner remauth <user>`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## ,globalbanlistowner setappealchannel
Set the channel for ban appeals.<br/>
 - Usage: `,globalbanlistowner setappealchannel [channel=None]`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,globalbanlistowner setbanlistchannel
Set the channel for displaying ban lists in this server.<br/>
 - Usage: `,globalbanlistowner setbanlistchannel <channel>`
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
## ,globalbanlistowner addauth
Add a user to the authorized users list.<br/>
 - Usage: `,globalbanlistowner addauth <user>`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
# ,globalbanlist (Hybrid Command)
Manage the global ban list.<br/>
 - Usage: `,globalbanlist`
 - Slash Usage: `/globalbanlist`
 - Aliases: `gbl`
## ,globalbanlist unsubscribe (Hybrid Command)
Unsubscribe from a specific ban list.<br/>
 - Usage: `,globalbanlist unsubscribe <list_name>`
 - Slash Usage: `/globalbanlist unsubscribe <list_name>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,globalbanlist appeal (Hybrid Command)
Submit an appeal for a global ban.<br/>
 - Usage: `,globalbanlist appeal`
 - Slash Usage: `/globalbanlist appeal`
## ,globalbanlist subscribe (Hybrid Command)
Subscribe to a specific ban list.<br/>
 - Usage: `,globalbanlist subscribe <list_name>`
 - Slash Usage: `/globalbanlist subscribe <list_name>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,globalbanlist list (Hybrid Command)
List all users in a specific ban list or show available lists.<br/>
 - Usage: `,globalbanlist list [list_name=None]`
 - Slash Usage: `/globalbanlist list [list_name=None]`
Extended Arg Info
> ### list_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,globalbanlist history (Hybrid Command)
Display the history of a specific ban list.<br/>
 - Usage: `,globalbanlist history <list_name>`
 - Slash Usage: `/globalbanlist history <list_name>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,globalbanlist setgenerallog (Hybrid Command)
Set the channel for general logging in this server.<br/>
 - Usage: `,globalbanlist setgenerallog <channel>`
 - Slash Usage: `/globalbanlist setgenerallog <channel>`
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
## ,globalbanlist add (Hybrid Command)
Add a user to a specific ban list.<br/>
 - Usage: `,globalbanlist add <list_name> <user> <reason_and_proof>`
 - Slash Usage: `/globalbanlist add <list_name> <user> <reason_and_proof>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason_and_proof: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,globalbanlist remove (Hybrid Command)
Remove a user from a specific ban list.<br/>
 - Usage: `,globalbanlist remove <list_name> <user>`
 - Slash Usage: `/globalbanlist remove <list_name> <user>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### user: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
