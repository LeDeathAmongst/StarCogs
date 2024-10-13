Away
====

Le away cog

<<<<<<< HEAD
# <@1275521742961508432>away
=======
# ,away
>>>>>>> 9e308722 (Revamped and Fixed)
Tell the bot you're away or back.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>away [delete_after=None] [message]`
=======
 - Usage: `,away [delete_after=None] [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>idle
=======
# ,idle
>>>>>>> 9e308722 (Revamped and Fixed)
Set an automatic reply when you're idle.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>idle [delete_after=None] [message]`
=======
 - Usage: `,idle [delete_after=None] [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>offline
=======
# ,offline
>>>>>>> 9e308722 (Revamped and Fixed)
Set an automatic reply when you're offline.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>offline [delete_after=None] [message]`
=======
 - Usage: `,offline [delete_after=None] [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>dnd
=======
# ,dnd
>>>>>>> 9e308722 (Revamped and Fixed)
Set an automatic reply when you're dnd.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>dnd [delete_after=None] [message]`
=======
 - Usage: `,dnd [delete_after=None] [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `donotdisturb`
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>streaming
=======
# ,streaming
>>>>>>> 9e308722 (Revamped and Fixed)
Set an automatic reply when you're streaming.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>streaming [delete_after=None] [message]`
=======
 - Usage: `,streaming [delete_after=None] [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>listening
=======
# ,listening
>>>>>>> 9e308722 (Revamped and Fixed)
Set an automatic reply when you're listening to Spotify.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>listening [delete_after=None] [message]`
=======
 - Usage: `,listening [delete_after=None] [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = ' '
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>gaming
=======
# ,gaming
>>>>>>> 9e308722 (Revamped and Fixed)
Set an automatic reply when you're playing a specified game.<br/>

`game` The game you would like automatic responses for<br/>
`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>

Use "double quotes" around a game's name if it is more than one word.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>gaming <game> [delete_after=None] [message]`
=======
 - Usage: `,gaming <game> [delete_after=None] [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>toggleaway
Toggle away messages on the whole server or a specific server member.<br/>

Mods, Admins and Bot Owner are immune to this.<br/>
 - Usage: `<@1275521742961508432>toggleaway [member=None]`
=======
# ,toggleaway
Toggle away messages on the whole server or a specific server member.<br/>

Mods, Admins and Bot Owner are immune to this.<br/>
 - Usage: `,toggleaway [member=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member = None
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


<<<<<<< HEAD
# <@1275521742961508432>awaytextonly
Toggle forcing the server's away messages to be text only.<br/>

This overrides the embed_links check this cog uses for message sending.<br/>
 - Usage: `<@1275521742961508432>awaytextonly`
=======
# ,awaytextonly
Toggle forcing the server's away messages to be text only.<br/>

This overrides the embed_links check this cog uses for message sending.<br/>
 - Usage: `,awaytextonly`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>awaysettings
View your current away settings<br/>
 - Usage: `<@1275521742961508432>awaysettings`
=======
# ,awaysettings
View your current away settings<br/>
 - Usage: `,awaysettings`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `awayset`


