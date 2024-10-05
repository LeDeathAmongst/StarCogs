GitHub RSS Commit Feeds<br/><br/>Customizable system for GitHub commit updates similar to the webhook.

# <@1275521742961508432>ghinterval
Set the global fetch interval for GitHub.<br/>

Depending on the size of your bot, you may want to modify the interval for which the bot fetches all feeds for updates (default is 3 minutes).<br/>
 - Usage: `<@1275521742961508432>ghinterval <interval_in_minutes>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### interval_in_minutes: int
> ```
> A number without decimal places.
> ```
# <@1275521742961508432>githubset
GitHub Settings<br/>
 - Usage: `<@1275521742961508432>githubset`
 - Restricted to: `ADMIN`
 - Aliases: `ghset`
 - Checks: `server_only`
## <@1275521742961508432>githubset notify
Set whether to send repo addition/removal notices to the channel.<br/>
 - Usage: `<@1275521742961508432>githubset notify <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>githubset channel
Set the default GitHub RSS feed channel.<br/>
 - Usage: `<@1275521742961508432>githubset channel <channel>`
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
## <@1275521742961508432>githubset channeloverride
Set a channel override for a feed (leave empty to reset).<br/>
 - Usage: `<@1275521742961508432>githubset channeloverride <user> <feed_name> [channel=None]`
Extended Arg Info
> ### user: discord.member.Member
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
> ### feed_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## <@1275521742961508432>githubset color
Set the GitHub RSS feed embed color for the server (enter "None" to reset).<br/>
 - Usage: `<@1275521742961508432>githubset color <hex_color>`
Extended Arg Info
> ### hex_color: Union[discord.colour.Colour, github.converters.ExplicitNone]
> Converts to a :class:`~discord.Colour`.
> 
>     
## <@1275521742961508432>githubset listall
List all GitHub RSS feeds in the server.<br/>
 - Usage: `<@1275521742961508432>githubset listall`
## <@1275521742961508432>githubset forceall
Force a run of the GitHub feed fetching coroutine.<br/>
 - Usage: `<@1275521742961508432>githubset forceall`
## <@1275521742961508432>githubset rename
Rename a user's GitHub RSS feed.<br/>
 - Usage: `<@1275521742961508432>githubset rename <user> <old_name> <new_name>`
Extended Arg Info
> ### user: discord.member.Member
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
> ### old_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### new_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>githubset force
Force a specific GitHub feed to post the last commit.<br/>
 - Usage: `<@1275521742961508432>githubset force <user> <name>`
Extended Arg Info
> ### user: discord.member.Member
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
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>githubset view
View the server settings for GitHub.<br/>
 - Usage: `<@1275521742961508432>githubset view`
## <@1275521742961508432>githubset limit
Set the GitHub RSS feed limit per user.<br/>
 - Usage: `<@1275521742961508432>githubset limit [num=5]`
Extended Arg Info
> ### num: int = 5
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>githubset timestamp
Set whether GitHub RSS feed embeds should include a timestamp.<br/>
 - Usage: `<@1275521742961508432>githubset timestamp <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>githubset role
Set the GitHub role requirement.<br/>

Note: Only those who are a mod or has permissions `manage_channels` can add / remove.<br/>
This is for you to lock to a speficially role to those with the permission to add / remove.<br/>
Only those who have the role can add / remove feeds, if they dont have the role, they will not be able to use this command.<br/>
 - Usage: `<@1275521742961508432>githubset role [role=None]`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## <@1275521742961508432>githubset short
Set whether the GitHub message content should just include the title.<br/>
 - Usage: `<@1275521742961508432>githubset short <short>`
Extended Arg Info
> ### short: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# <@1275521742961508432>github
GitHub RSS Commit Feeds<br/>
 - Usage: `<@1275521742961508432>github`
 - Restricted to: `MOD`
 - Aliases: `gh`
 - Checks: `server_only`
## <@1275521742961508432>github get
Test out fetching a GitHub repository url.<br/>
 - Usage: `<@1275521742961508432>github get <entries> <url> [branch=None]`
 - Aliases: `fetch and test`
Extended Arg Info
> ### entries: Optional[int]
> ```
> A number without decimal places.
> ```
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### branch: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>github list
List your GitHub RSS feeds in the server.<br/>
 - Usage: `<@1275521742961508432>github list`
## <@1275521742961508432>github add
Add a GitHub RSS feed to the server.<br/>

For the accepted link formats, see `<@1275521742961508432>github whatlinks`.<br/>
 - Usage: `<@1275521742961508432>github add <name> <url> [branch=]`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### branch: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>github whatlinks
What links can you submit to `<@1275521742961508432>github add`?<br/>
 - Usage: `<@1275521742961508432>github whatlinks`
## <@1275521742961508432>github remove
Remove a GitHub RSS feed from the server.<br/>
 - Usage: `<@1275521742961508432>github remove <name>`
 - Aliases: `delete`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
