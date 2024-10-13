Reports
=======

Create user reports that server staff can respond to.

Users can open reports using `[p]report`. These are then sent
to a channel in the server for staff, and the report creator
gets a DM. Both can be used to communicate.

# ,reportset
Manage Reports.<br/>
 - Usage: `,reportset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,reportset output
Set the channel where reports will be sent.<br/>
 - Usage: `,reportset output <channel>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,reportset toggle
Enable or disable reporting for this server.<br/>
 - Usage: `,reportset toggle`
 - Restricted to: `ADMIN`
 - Aliases: `toggleactive`


# ,report
Send a report.<br/>

Use without arguments for interactive reporting, or do<br/>
`,report [text]` to use it non-interactively.<br/>
 - Usage: `,report [_report]`
Extended Arg Info
> ### _report: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,report interact
Open a message tunnel.<br/>

This tunnel will forward things you say in this channel or thread<br/>
to the ticket opener's direct messages.<br/>

Tunnels do not persist across bot restarts.<br/>
 - Usage: `,report interact <ticket_number>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### ticket_number: int
> ```
> A number without decimal places.
> ```


