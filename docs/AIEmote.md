Human-like Discord reacts to messages powered by OpenAI.

# ,aiemote
Totally not glorified sentiment analysis™<br/>

Picks a reaction for a message using gpt-3.5-turbo<br/>

To get started, please add a channel to the whitelist with:<br/>
`,aiemote allow <#channel>`<br/>
 - Usage: `,aiemote`
 - Restricted to: `ADMIN`
## ,aiemote allow
Add a channel to the whitelist<br/>

*Arguments*<br/>
- `<channel>` The mention of channel<br/>
 - Usage: `,aiemote allow <channel>`
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
Remove a channel from the whitelist<br/>

*Arguments*<br/>
- `<channel>` The mention of channel<br/>
 - Usage: `,aiemote remove <channel>`
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
Remove an emoji from the global list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to remove<br/>
 - Usage: `,aiemoteowner remove <emoji>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `rm`
Extended Arg Info
> ### emoji
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,aiemoteowner percent
Set the chance that the bot will react to a message (for all servers bot is in)<br/>

*Arguments*<br/>
- `<percent>` The percent chance that the bot will react to a message<br/>
 - Usage: `,aiemoteowner percent <percent>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### percent: int
> ```
> A number without decimal places.
> ```
## ,aiemoteowner config
List all emojis in the global list (and current server list)<br/>
        <br/>
 - Usage: `,aiemoteowner config`
 - Restricted to: `BOT_OWNER`
 - Aliases: `settings, list, and conf`
## ,aiemoteowner instruction
Add additonal (prompting) instruction for the langauge model when picking an emoji<br/>

*Arguments*<br/>
- `<instruction>` The extra instruction to use<br/>
 - Usage: `,aiemoteowner instruction <instruction>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `extra_instruction and extra`
Extended Arg Info
> ### instruction: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,aiemoteowner sremove
Remove an emoji from this current server list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to remove<br/>
 - Usage: `,aiemoteowner sremove <emoji>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `srm`
Extended Arg Info
> ### emoji
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,aiemoteowner sadd
Add an emoji to this current server list<br/>

*Arguments*<br/>
- `<emoji>` The emoji to add<br/>
- `<description>` A description of the emoji to be used by OpenAI<br/>
 - Usage: `,aiemoteowner sadd <emoji> <description>`
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
