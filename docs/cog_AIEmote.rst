AIEmote
=======

Human-like Discord reacts to messages powered by OpenAI.

<<<<<<< HEAD
# <@1275521742961508432>aiemote
=======
# ,aiemote
>>>>>>> 9e308722 (Revamped and Fixed)
Totally not glorified sentiment analysis™<br/>

Picks a reaction for a message using gpt-3.5-turbo<br/>

To get started, please add a channel to the whitelist with:<br/>
<<<<<<< HEAD
`<@1275521742961508432>aiemote allow <#channel>`<br/>
 - Usage: `<@1275521742961508432>aiemote`
 - Restricted to: `ADMIN`


## <@1275521742961508432>aiemote optout
Opt out of sending your message to OpenAI (bot-wide)<br/>

The bot will no longer react to your messages<br/>
 - Usage: `<@1275521742961508432>aiemote optout`


## <@1275521742961508432>aiemote allow
=======
`,aiemote allow <#channel>`<br/>
 - Usage: `,aiemote`
 - Restricted to: `ADMIN`


## ,aiemote allow
>>>>>>> 9e308722 (Revamped and Fixed)
Add a channel to the whitelist<br/>

*Arguments*<br/>
- `<channel>` The mention of channel<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiemote allow <channel>`
=======
 - Usage: `,aiemote allow <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `add`
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


<<<<<<< HEAD
## <@1275521742961508432>aiemote whitelist
List all channels in the whitelist <br/>
 - Usage: `<@1275521742961508432>aiemote whitelist`
 - Restricted to: `ADMIN`


## <@1275521742961508432>aiemote remove
=======
## ,aiemote optinbydefault
Toggles whether users are opted in by default in this server<br/>

This command is disabled for servers with more than 150 members.<br/>
 - Usage: `,aiemote optinbydefault`
 - Restricted to: `ADMIN`


## ,aiemote whitelist
List all channels in the whitelist <br/>
 - Usage: `,aiemote whitelist`
 - Restricted to: `ADMIN`


## ,aiemote remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove a channel from the whitelist<br/>

*Arguments*<br/>
- `<channel>` The mention of channel<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiemote remove <channel>`
=======
 - Usage: `,aiemote remove <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `rm`
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


<<<<<<< HEAD
## <@1275521742961508432>aiemote optin
Opt in of sending your message to OpenAI (bot-wide)<br/>

This will allow the bot to react to your messages<br/>
 - Usage: `<@1275521742961508432>aiemote optin`


## <@1275521742961508432>aiemote optinbydefault
Toggles whether users are opted in by default in this server<br/>

This command is disabled for servers with more than 150 members.<br/>
 - Usage: `<@1275521742961508432>aiemote optinbydefault`
 - Restricted to: `ADMIN`


# <@1275521742961508432>aiemoteowner
Owner only commands for aiemote<br/>
        <br/>
 - Usage: `<@1275521742961508432>aiemoteowner`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>aiemoteowner config
List all emojis in the global list (and current server list)<br/>
        <br/>
 - Usage: `<@1275521742961508432>aiemoteowner config`
 - Restricted to: `BOT_OWNER`
 - Aliases: `settings, list, and conf`


## <@1275521742961508432>aiemoteowner remove
=======
## ,aiemote optout
Opt out of sending your message to OpenAI (bot-wide)<br/>

The bot will no longer react to your messages<br/>
 - Usage: `,aiemote optout`


## ,aiemote optin
Opt in of sending your message to OpenAI (bot-wide)<br/>

This will allow the bot to react to your messages<br/>
 - Usage: `,aiemote optin`


# ,aiemoteowner
Owner only commands for aiemote<br/>
        <br/>
 - Usage: `,aiemoteowner`
 - Restricted to: `BOT_OWNER`


## ,aiemoteowner add
Add an emoji to the global list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to add<br/>
- `<description>` A description of the emoji to be used by OpenAI<br/>
 - Usage: `,aiemoteowner add <emoji> <description>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### emoji
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,aiemoteowner reset
Reset *all* settings<br/>
 - Usage: `,aiemoteowner reset`
 - Restricted to: `BOT_OWNER`


## ,aiemoteowner remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove an emoji from the global list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to remove<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiemoteowner remove <emoji>`
=======
 - Usage: `,aiemoteowner remove <emoji>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `rm`
Extended Arg Info
> ### emoji
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiemoteowner sremove
Remove an emoji from this current server list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to remove<br/>
 - Usage: `<@1275521742961508432>aiemoteowner sremove <emoji>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `srm`
Extended Arg Info
> ### emoji
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aiemoteowner percent
=======
## ,aiemoteowner percent
>>>>>>> 9e308722 (Revamped and Fixed)
Set the chance that the bot will react to a message (for all servers bot is in)<br/>

*Arguments*<br/>
- `<percent>` The percent chance that the bot will react to a message<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiemoteowner percent <percent>`
=======
 - Usage: `,aiemoteowner percent <percent>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### percent: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiemoteowner instruction
=======
## ,aiemoteowner config
List all emojis in the global list (and current server list)<br/>
        <br/>
 - Usage: `,aiemoteowner config`
 - Restricted to: `BOT_OWNER`
 - Aliases: `settings, list, and conf`


## ,aiemoteowner instruction
>>>>>>> 9e308722 (Revamped and Fixed)
Add additonal (prompting) instruction for the langauge model when picking an emoji<br/>

*Arguments*<br/>
- `<instruction>` The extra instruction to use<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiemoteowner instruction <instruction>`
=======
 - Usage: `,aiemoteowner instruction <instruction>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `extra_instruction and extra`
Extended Arg Info
> ### instruction: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiemoteowner add
Add an emoji to the global list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to add<br/>
- `<description>` A description of the emoji to be used by OpenAI<br/>
 - Usage: `<@1275521742961508432>aiemoteowner add <emoji> <description>`
 - Restricted to: `BOT_OWNER`
=======
## ,aiemoteowner sremove
Remove an emoji from this current server list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to remove<br/>
 - Usage: `,aiemoteowner sremove <emoji>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `srm`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### emoji
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
<<<<<<< HEAD
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aiemoteowner sadd
=======


## ,aiemoteowner sadd
>>>>>>> 9e308722 (Revamped and Fixed)
Add an emoji to this current server list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to add<br/>
- `<description>` A description of the emoji to be used by OpenAI<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiemoteowner sadd <emoji> <description>`
=======
 - Usage: `,aiemoteowner sadd <emoji> <description>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### emoji
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiemoteowner reset
Reset *all* settings<br/>
 - Usage: `<@1275521742961508432>aiemoteowner reset`
 - Restricted to: `BOT_OWNER`


=======
>>>>>>> 9e308722 (Revamped and Fixed)
