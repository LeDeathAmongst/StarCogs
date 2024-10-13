Automatically deletes server configurations 15 minutes after the bot leaves the server.

# ,canceldeletion
Cancels the scheduled deletion for a specific server.<br/>
 - Usage: `,canceldeletion <server_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server_id: int
> ```
> A number without decimal places.
> ```
# ,setdellog
Sets the log channel for purge notifications.<br/>
 - Usage: `,setdellog <channel>`
 - Restricted to: `BOT_OWNER`
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
