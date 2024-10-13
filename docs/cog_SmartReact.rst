SmartReact
==========

Create automatic reactions when trigger words are typed in chat

<<<<<<< HEAD
# <@1275521742961508432>react
Smart Reacts, modified.<br/>
 - Usage: `<@1275521742961508432>react`
 - Checks: `server_only`


## <@1275521742961508432>react del
=======
# ,react
Smart Reacts, modified.<br/>
 - Usage: `,react`
 - Checks: `server_only`


## ,react add
Add an auto reaction to a word.<br/>

Parameters:<br/>
-----------<br/>
word: str<br/>
    The word you wish to react to.<br/>
emoji: Union[str, discord.Emoji]<br/>
    The emoji you wish to react with, interpreted as the string representation<br/>
    with <:name:id> if it is a custom emoji.<br/>
 - Usage: `,react add <word> <emoji>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### emoji: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,react list
List the auto reaction emojis and triggers.<br/>
 - Usage: `,react list`


## ,react del
>>>>>>> 9e308722 (Revamped and Fixed)
Delete an auto reaction to a word.<br/>

Parameters:<br/>
-----------<br/>
word: str<br/>
    The word you wish to react to.<br/>
emoji: Union[str, discord.Emoji]<br/>
    The emoji you wish to react with, interpreted as the string representation<br/>
    with <:name:id> if it is a custom emoji.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>react del <word> <emoji>`
=======
 - Usage: `,react del <word> <emoji>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `delete, remove, and rm`
 - Checks: `server_only`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### emoji: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>react add
Add an auto reaction to a word.<br/>

Parameters:<br/>
-----------<br/>
word: str<br/>
    The word you wish to react to.<br/>
emoji: Union[str, discord.Emoji]<br/>
    The emoji you wish to react with, interpreted as the string representation<br/>
    with <:name:id> if it is a custom emoji.<br/>
 - Usage: `<@1275521742961508432>react add <word> <emoji>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### emoji: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>react reload
Reloads auto reactions with new emojis by name<br/>
 - Usage: `<@1275521742961508432>react reload`
=======
## ,react reload
Reloads auto reactions with new emojis by name<br/>
 - Usage: `,react reload`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>react list
List the auto reaction emojis and triggers.<br/>
 - Usage: `<@1275521742961508432>react list`


=======
>>>>>>> 9e308722 (Revamped and Fixed)
