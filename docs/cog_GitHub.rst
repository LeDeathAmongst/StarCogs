GitHub
======

GitHub RSS Commit Feeds

Customizable system for GitHub commit updates similar to the webhook.

# ,ghinterval
Set the global fetch interval for GitHub.<br/>

Depending on the size of your bot, you may want to modify the interval for which the bot fetches all feeds for updates (default is 3 minutes).<br/>
 - Usage: `,ghinterval <interval_in_minutes>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### interval_in_minutes: int
> ```
> A number without decimal places.
> ```


# ,githubset
GitHub Settings<br/>
 - Usage: `,githubset`
 - Restricted to: `ADMIN`
 - Aliases: `ghset`
 - Checks: `server_only`


## ,githubset force
Force a specific GitHub feed to post the last commit.<br/>
 - Usage: `,githubset force <user> <name>`
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


## ,githubset listall
List all GitHub RSS feeds in the server.<br/>
 - Usage: `,githubset listall`


## ,githubset short
Set whether the GitHub message content should just include the title.<br/>
 - Usage: `,githubset short <short>`
Extended Arg Info
> ### short: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,githubset limit
Set the GitHub RSS feed limit per user.<br/>
 - Usage: `,githubset limit [num=5]`
Extended Arg Info
> ### num: int = 5
> ```
> A number without decimal places.
> ```


## ,githubset view
View the server settings for GitHub.<br/>
 - Usage: `,githubset view`


## ,githubset rename
Rename a user's GitHub RSS feed.<br/>
 - Usage: `,githubset rename <user> <old_name> <new_name>`
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


## ,githubset color
Set the GitHub RSS feed embed color for the server (enter "None" to reset).<br/>
 - Usage: `,githubset color <hex_color>`
Extended Arg Info
> ### hex_color: Union[discord.colour.Colour, github.converters.ExplicitNone]
> Converts to a :class:`~discord.Colour`.
> 
>     


## ,githubset notify
Set whether to send repo addition/removal notices to the channel.<br/>
 - Usage: `,githubset notify <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,githubset channeloverride
Set a channel override for a feed (leave empty to reset).<br/>
 - Usage: `,githubset channeloverride <user> <feed_name> [channel=None]`
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


## ,githubset timestamp
Set whether GitHub RSS feed embeds should include a timestamp.<br/>
 - Usage: `,githubset timestamp <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,githubset channel
Set the default GitHub RSS feed channel.<br/>
 - Usage: `,githubset channel <channel>`
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


## ,githubset forceall
Force a run of the GitHub feed fetching coroutine.<br/>
 - Usage: `,githubset forceall`


## ,githubset role
Set the GitHub role requirement.<br/>

Note: Only those who are a mod or has permissions `manage_channels` can add / remove.<br/>
This is for you to lock to a speficially role to those with the permission to add / remove.<br/>
Only those who have the role can add / remove feeds, if they dont have the role, they will not be able to use this command.<br/>
 - Usage: `,githubset role [role=None]`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


# ,github
GitHub RSS Commit Feeds<br/>
 - Usage: `,github`
 - Restricted to: `MOD`
 - Aliases: `gh`
 - Checks: `server_only`


## ,github add
Add a GitHub RSS feed to the server.<br/>

For the accepted link formats, see `,github whatlinks`.<br/>
 - Usage: `,github add <name> <url> [branch=]`
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


## ,github whatlinks
What links can you submit to `,github add`?<br/>
 - Usage: `,github whatlinks`


## ,github remove
Remove a GitHub RSS feed from the server.<br/>
 - Usage: `,github remove <name>`
 - Aliases: `delete`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,github get
Test out fetching a GitHub repository url.<br/>
 - Usage: `,github get <entries> <url> [branch=None]`
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


## ,github list
List your GitHub RSS feeds in the server.<br/>
 - Usage: `,github list`


