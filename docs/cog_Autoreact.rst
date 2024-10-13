Autoreact
=========

Lets you configure emojis that will be added to any message containing text matching a regex.

<<<<<<< HEAD
# <@1275521742961508432>autoreact
Reacts to specific text with an emoji.<br/>
 - Usage: `<@1275521742961508432>autoreact`
 - Checks: `server_only`


## <@1275521742961508432>autoreact add
Add a new autoreact using regex. Tip: (?i) in a regex makes it case-insensitive.<br/>
 - Usage: `<@1275521742961508432>autoreact add <emoji> <pattern>`
=======
# ,autoreact
Reacts to specific text with an emoji.<br/>
 - Usage: `,autoreact`
 - Checks: `server_only`


## ,autoreact remove
Remove an existing autoreact for an emoji.<br/>
 - Usage: `,autoreact remove <emoji>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


## ,autoreact add
Add a new autoreact using regex. Tip: (?i) in a regex makes it case-insensitive.<br/>
 - Usage: `,autoreact add <emoji> <pattern>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### pattern: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>autoreact list
Shows all autoreacts.<br/>
 - Usage: `<@1275521742961508432>autoreact list`


## <@1275521742961508432>autoreact remove
Remove an existing autoreact for an emoji.<br/>
 - Usage: `<@1275521742961508432>autoreact remove <emoji>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


# <@1275521742961508432>coreact
Copies other people's reactions to recent messages.<br/>
 - Usage: `<@1275521742961508432>coreact`


## <@1275521742961508432>coreact chance
The percent chance that the bot will add its own reaction when anyone else reacts.<br/>
 - Usage: `<@1275521742961508432>coreact chance <chance>`
=======
## ,autoreact list
Shows all autoreacts.<br/>
 - Usage: `,autoreact list`


# ,coreact
Copies other people's reactions to recent messages.<br/>
 - Usage: `,coreact`


## ,coreact chance
The percent chance that the bot will add its own reaction when anyone else reacts.<br/>
 - Usage: `,coreact chance <chance>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### chance: Optional[float]
> ```
> A number with or without decimal places.
> ```


