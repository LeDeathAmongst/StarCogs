Lets you configure emojis that will be added to any message containing text matching a regex.

# <@1275521742961508432>autoreact
Reacts to specific text with an emoji.<br/>
 - Usage: `<@1275521742961508432>autoreact`
 - Checks: `server_only`
## <@1275521742961508432>autoreact add
Add a new autoreact using regex. Tip: (?i) in a regex makes it case-insensitive.<br/>
 - Usage: `<@1275521742961508432>autoreact add <emoji> <pattern>`
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
## <@1275521742961508432>autoreact list
Shows all autoreacts.<br/>
 - Usage: `<@1275521742961508432>autoreact list`
# <@1275521742961508432>coreact
Copies other people's reactions to recent messages.<br/>
 - Usage: `<@1275521742961508432>coreact`
## <@1275521742961508432>coreact chance
The percent chance that the bot will add its own reaction when anyone else reacts.<br/>
 - Usage: `<@1275521742961508432>coreact chance <chance>`
Extended Arg Info
> ### chance: Optional[float]
> ```
> A number with or without decimal places.
> ```
