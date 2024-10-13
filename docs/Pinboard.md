Make pinned messages communal! Users can add and remove their contributions to a pinned message at any time.

# ,pinboard
Change the list of active pinned messages<br/>
 - Usage: `,pinboard`
 - Checks: `server_only`
## ,pinboard remove
Remove your own content to a pinned message<br/>
 - Usage: `,pinboard remove <pinnedMsgName>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,pinboard add
Add or edit your own content to a pinned message<br/>
 - Usage: `,pinboard add <pinnedMsgName> <content>`
 - Aliases: `edit`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### content
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,setpinboard
Change the list of active pinned messages<br/>
 - Usage: `,setpinboard`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## ,setpinboard reset
⚠️ Reset all pinned messages<br/>

Type **`,setpinboard reset True`** if you're really sure.<br/>
 - Usage: `,setpinboard reset [areYouSure=False]`
Extended Arg Info
> ### areYouSure=False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setpinboard add
Create a new pinned message<br/>

pinnedMsgName is a label for the pinned message, so that you/others can easily refer back to it later. It should be a single word and short/easy to remember.<br/>
 - Usage: `,setpinboard add <pinnedMsgName> <channel> <messageDescription>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### messageDescription
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setpinboard list
List all pinned messages<br/>
 - Usage: `,setpinboard list`
## ,setpinboard edit
Edit description of a pinned message<br/>
 - Usage: `,setpinboard edit <pinnedMsgName> <description>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setpinboard update
Update one or all pinned messages<br/>
 - Usage: `,setpinboard update [pinnedMsgName=None] [repin=False]`
Extended Arg Info
> ### pinnedMsgName=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### repin=False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setpinboard import
Import data<br/>
 - Usage: `,setpinboard import <data>`
Extended Arg Info
> ### data
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setpinboard remove
Remove a pinned message<br/>

The message stays behind, but it will be removed from the tracking system, so you can't update it anymore.<br/>
 - Usage: `,setpinboard remove <pinnedMsgName>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
