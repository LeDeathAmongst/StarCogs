Sticky
======

Sticky messages to your channels.

<<<<<<< HEAD
# <@1275521742961508432>sticky
Sticky a message to this channel.<br/>
 - Usage: `<@1275521742961508432>sticky <content>`
=======
# ,sticky
Sticky a message to this channel.<br/>
 - Usage: `,sticky <content>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### content: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>sticky existing
Sticky an existing message to this channel.<br/>

This will try to sticky the content and embed of the message.<br/>
Attachments will not be added to the stickied message.<br/>

Stickying messages with multiple embeds may result in unexpected<br/>
behaviour, as the bot cannot send multiple rich embeds in a<br/>
single message.<br/>
 - Usage: `<@1275521742961508432>sticky existing <message_id_or_url>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### message_id_or_url: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     


## <@1275521742961508432>sticky toggleheader
Toggle the header for stickied messages in this channel.<br/>

The header is enabled by default.<br/>
 - Usage: `<@1275521742961508432>sticky toggleheader <true_or_false>`
=======
## ,sticky toggleheader
Toggle the header for stickied messages in this channel.<br/>

The header is enabled by default.<br/>
 - Usage: `,sticky toggleheader <true_or_false>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
# <@1275521742961508432>unsticky
=======
## ,sticky existing
Sticky an existing message to this channel.<br/>

This will try to sticky the content and embed of the message.<br/>
Attachments will not be added to the stickied message.<br/>

Stickying messages with multiple embeds may result in unexpected<br/>
behaviour, as the bot cannot send multiple rich embeds in a<br/>
single message.<br/>
 - Usage: `,sticky existing <message_id_or_url>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### message_id_or_url: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     


# ,unsticky
>>>>>>> 9e308722 (Revamped and Fixed)
Remove the sticky message from this channel.<br/>

Deleting the sticky message will also unsticky it.<br/>

<<<<<<< HEAD
Do `<@1275521742961508432>unsticky yes` to skip the confirmation prompt.<br/>
 - Usage: `<@1275521742961508432>unsticky [force=False]`
=======
Do `,unsticky yes` to skip the confirmation prompt.<br/>
 - Usage: `,unsticky [force=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### force: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


