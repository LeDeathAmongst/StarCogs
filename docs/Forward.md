Forward messages sent to the bot to the bot owner or in a specified channel.

# ,forwardset
Forwarding commands.<br/>
 - Usage: `,forwardset`
 - Restricted to: `BOT_OWNER`
## ,forwardset channel
Set if you want to receive notifications in a channel instead of your DMs.<br/>

Leave blank if you want to set back to your DMs.<br/>
 - Usage: `,forwardset channel [channel=None]`
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
## ,forwardset botmsg
Set whether to send notifications when the bot sends a message.<br/>

Type must be a valid bool.<br/>
 - Usage: `,forwardset botmsg [type=None]`
 - Aliases: `botmessage`
Extended Arg Info
> ### type: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,forwardset blacklist
Blacklist receiving messages from a user.<br/>
 - Usage: `,forwardset blacklist [user_id=None]`
 - Aliases: `bl`
Extended Arg Info
> ### user_id: int = None
> ```
> A number without decimal places.
> ```
## ,forwardset unblacklist
Remove a user from the blacklist.<br/>
 - Usage: `,forwardset unblacklist <user_id>`
 - Aliases: `unbl`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
# ,pm
PMs a person.<br/>

Separate version of ,dm but allows for server owners. This only works for users in the<br/>
server.<br/>
 - Usage: `,pm <user> <message>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
