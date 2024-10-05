Counting
========

Count from 1 to infinity!

# <@1275521742961508432>counting (Hybrid Command)
Counting commands<br/>
 - Usage: `<@1275521742961508432>counting`
 - Slash Usage: `/counting`
 - Checks: `server_only`


## <@1275521742961508432>counting resetme (Hybrid Command)
Reset your counting stats.<br/>
 - Usage: `<@1275521742961508432>counting resetme`
 - Slash Usage: `/counting resetme`


## <@1275521742961508432>counting countstats (Hybrid Command)
Get your current counting statistics.<br/>
 - Usage: `<@1275521742961508432>counting countstats [user=None]`
 - Slash Usage: `/counting countstats [user=None]`
 - Aliases: `stats`
 - Cooldown: `1 per 10.0 seconds`
Extended Arg Info
> ### user: Optional[discord.user.User] = None
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


# <@1275521742961508432>countingset
Counting settings commands.<br/>
 - Usage: `<@1275521742961508432>countingset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## <@1275521742961508432>countingset togglereact
Toggle the reactions for correct numbers.<br/>
 - Usage: `<@1275521742961508432>countingset togglereact`


## <@1275521742961508432>countingset toggle
Toggle counting in the channel<br/>
 - Usage: `<@1275521742961508432>countingset toggle`


## <@1275521742961508432>countingset togglesilent
Toggle silent mode for counting messages.<br/>

Silent is discords new feature.<br/>
 - Usage: `<@1275521742961508432>countingset togglesilent`


## <@1275521742961508432>countingset setmessage
Set the default message for a specific type.<br/>

Available message types: edit, count<br/>

`edit` - The message to show when a user edits their message in the counting channel.<br/>
`count` - The message to show when a user sends an incorrect number in the counting channel.<br/>

**Examples:**<br/>
- `<@1275521742961508432>countingset setmessage edit You can't edit your messages here.`<br/>
- `<@1275521742961508432>countingset setmessage count Next number should be {next_count}`<br/>

**Arguments:**<br/>
- `<message_type>` The type of message to set (edit or count).<br/>
- `<message>` The message to set.<br/>
 - Usage: `<@1275521742961508432>countingset setmessage <message_type> <message>`
Extended Arg Info
> ### message_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>countingset channel
Set the counting channel<br/>
 - Usage: `<@1275521742961508432>countingset channel <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>countingset togglesameuser
Toggle whether the same user can count more than once consecutively.<br/>

Users cannot count consecutively if this is enabled meaning they have to wait for someone else to count.<br/>
 - Usage: `<@1275521742961508432>countingset togglesameuser`


## <@1275521742961508432>countingset reset
Reset the settings for the counting.<br/>
 - Usage: `<@1275521742961508432>countingset reset`


## <@1275521742961508432>countingset setreaction
Set the reaction for correct numbers.<br/>
 - Usage: `<@1275521742961508432>countingset setreaction <emoji_input>`
Extended Arg Info
> ### emoji_input: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>countingset togglemessage
Toggle to show a message for a specific setting.<br/>

Available settings: edit, count<br/>

`count` - Show the next number message when a user sends an incorrect number. Default is disabled<br/>
`edit` - Shows a message when a user edits their message in the counting channel. Default is disabled<br/>
 - Usage: `<@1275521742961508432>countingset togglemessage <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>countingset deleteafter
Set the number of seconds to delete the incorrect message<br/>

Default is 5 seconds<br/>
 - Usage: `<@1275521742961508432>countingset deleteafter <seconds>`


## <@1275521742961508432>countingset settings
Show the current counting settings.<br/>
 - Usage: `<@1275521742961508432>countingset settings`


