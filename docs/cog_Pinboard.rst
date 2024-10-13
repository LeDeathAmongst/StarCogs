Pinboard
========

Make pinned messages communal! Users can add and remove their contributions to a pinned message at any time.

<<<<<<< HEAD
# <@1275521742961508432>pinboard
Change the list of active pinned messages<br/>
 - Usage: `<@1275521742961508432>pinboard`
 - Checks: `server_only`


## <@1275521742961508432>pinboard remove
Remove your own content to a pinned message<br/>
 - Usage: `<@1275521742961508432>pinboard remove <pinnedMsgName>`
=======
# ,pinboard
Change the list of active pinned messages<br/>
 - Usage: `,pinboard`
 - Checks: `server_only`


## ,pinboard remove
Remove your own content to a pinned message<br/>
 - Usage: `,pinboard remove <pinnedMsgName>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>pinboard add
Add or edit your own content to a pinned message<br/>
 - Usage: `<@1275521742961508432>pinboard add <pinnedMsgName> <content>`
=======
## ,pinboard add
Add or edit your own content to a pinned message<br/>
 - Usage: `,pinboard add <pinnedMsgName> <content>`
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
# <@1275521742961508432>setpinboard
Change the list of active pinned messages<br/>
 - Usage: `<@1275521742961508432>setpinboard`
=======
# ,setpinboard
Change the list of active pinned messages<br/>
 - Usage: `,setpinboard`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>setpinboard add
Create a new pinned message<br/>

pinnedMsgName is a label for the pinned message, so that you/others can easily refer back to it later. It should be a single word and short/easy to remember.<br/>
 - Usage: `<@1275521742961508432>setpinboard add <pinnedMsgName> <channel> <messageDescription>`
=======
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
>>>>>>> 9e308722 (Revamped and Fixed)
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


<<<<<<< HEAD
## <@1275521742961508432>setpinboard remove
Remove a pinned message<br/>

The message stays behind, but it will be removed from the tracking system, so you can't update it anymore.<br/>
 - Usage: `<@1275521742961508432>setpinboard remove <pinnedMsgName>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setpinboard reset
⚠️ Reset all pinned messages<br/>

Type **`<@1275521742961508432>setpinboard reset True`** if you're really sure.<br/>
 - Usage: `<@1275521742961508432>setpinboard reset [areYouSure=False]`
Extended Arg Info
> ### areYouSure=False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setpinboard edit
Edit description of a pinned message<br/>
 - Usage: `<@1275521742961508432>setpinboard edit <pinnedMsgName> <description>`
=======
## ,setpinboard list
List all pinned messages<br/>
 - Usage: `,setpinboard list`


## ,setpinboard edit
Edit description of a pinned message<br/>
 - Usage: `,setpinboard edit <pinnedMsgName> <description>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setpinboard update
Update one or all pinned messages<br/>
 - Usage: `<@1275521742961508432>setpinboard update [pinnedMsgName=None] [repin=False]`
=======
## ,setpinboard update
Update one or all pinned messages<br/>
 - Usage: `,setpinboard update [pinnedMsgName=None] [repin=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### pinnedMsgName=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### repin=False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setpinboard import
Import data<br/>
 - Usage: `<@1275521742961508432>setpinboard import <data>`
=======
## ,setpinboard import
Import data<br/>
 - Usage: `,setpinboard import <data>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### data
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setpinboard list
List all pinned messages<br/>
 - Usage: `<@1275521742961508432>setpinboard list`
=======
## ,setpinboard remove
Remove a pinned message<br/>

The message stays behind, but it will be removed from the tracking system, so you can't update it anymore.<br/>
 - Usage: `,setpinboard remove <pinnedMsgName>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
>>>>>>> 9e308722 (Revamped and Fixed)


