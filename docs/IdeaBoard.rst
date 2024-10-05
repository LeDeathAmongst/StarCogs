IdeaBoard
=========

Share Ideas and Suggestions

# <@1275521742961508432>idea (Hybrid Command)
Share an idea/make a suggestion.<br/>
 - Usage: `<@1275521742961508432>idea <content>`
 - Slash Usage: `/idea <content>`
 - Aliases: `suggest`
 - Checks: `bot_has_server_permissions and server_only`
Extended Arg Info
> ### content: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>ideastats (Hybrid Command)
Display your current profile stats for suggestions and votes.<br/>
 - Usage: `<@1275521742961508432>ideastats [member]`
 - Slash Usage: `/ideastats [member]`
 - Checks: `server_only`
Extended Arg Info
> ### member: Optional[discord.member.Member] = None
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


# <@1275521742961508432>approve (Hybrid Command)
Approve an idea/suggestion.<br/>
 - Usage: `<@1275521742961508432>approve <number> [reason]`
 - Slash Usage: `/approve <number> [reason]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>reject (Hybrid Command)
Reject an idea/suggestion.<br/>
 - Usage: `<@1275521742961508432>reject <number> [reason]`
 - Slash Usage: `/reject <number> [reason]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>viewvotes (Hybrid Command)
View the list of who has upvoted and who has downvoted a suggestion.<br/>
 - Usage: `<@1275521742961508432>viewvotes <number>`
 - Slash Usage: `/viewvotes <number>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>refresh (Hybrid Command)
Refresh the buttons on a suggestion if it gets stuck.<br/>
 - Usage: `<@1275521742961508432>refresh <number>`
 - Slash Usage: `/refresh <number>`
 - Checks: `server_only`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


# <@1275521742961508432>ideaset
Manage IdeaBoard settings<br/>
 - Usage: `<@1275521742961508432>ideaset`
 - Restricted to: `ADMIN`
 - Aliases: `ideaboard`


## <@1275521742961508432>ideaset cleanup
Cleanup the config.<br/>
- Remove suggestions who's message no longer exists.<br/>
- Remove profiles of users who have left the server.<br/>
- Remove votes from users who have left the server.<br/>
 - Usage: `<@1275521742961508432>ideaset cleanup`


## <@1275521742961508432>ideaset cooldown
Set the base cooldown for making suggestions<br/>
 - Usage: `<@1275521742961508432>ideaset cooldown <cooldown>`
 - Aliases: `cd`
Extended Arg Info
> ### cooldown: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ideaset toggledm
Toggle DMing users the results of suggestions they made<br/>
 - Usage: `<@1275521742961508432>ideaset toggledm`
 - Aliases: `dm`


## <@1275521742961508432>ideaset roleblacklist
Add/remove a role to/from the role blacklist<br/>
 - Usage: `<@1275521742961508432>ideaset roleblacklist <role>`
 - Aliases: `blacklistrole and rolebl`
Extended Arg Info
> ### role: Union[discord.role.Role, int]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>ideaset channel
Set the approved, rejected, or pending channels for IdeaBoard<br/>
 - Usage: `<@1275521742961508432>ideaset channel <channel> <channel_type>`
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


## <@1275521742961508432>ideaset minplaytime
Set the ArkTools integration minimum playtime required to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum playtime in hours required to vote.<br/>
    to_suggest: Minimum playtime in hours required to suggest.<br/>
 - Usage: `<@1275521742961508432>ideaset minplaytime <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ideaset insights
View insights about the server's suggestions.<br/>

**Arguments**<br/>
- `amount` The number of top users to display for each section.<br/>
 - Usage: `<@1275521742961508432>ideaset insights [amount=3]`
Extended Arg Info
> ### amount: int = 3
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ideaset discussions
Toggle opening a discussion thread for each suggestion<br/>
 - Usage: `<@1275521742961508432>ideaset discussions`
 - Aliases: `threads and discussion`


## <@1275521742961508432>ideaset rolecooldown
Set the suggestion cooldown for a specific role<br/>

To remove a role cooldown, specify 0 as the cooldown.<br/>
 - Usage: `<@1275521742961508432>ideaset rolecooldown <role> <cooldown>`
 - Aliases: `rolecd`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### cooldown: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ideaset jointime
Set the minimum time a user must be in the server to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum time in hours required to vote.<br/>
    to_suggest: Minimum time in hours required to suggest.<br/>
 - Usage: `<@1275521742961508432>ideaset jointime <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ideaset resetuser
Reset a user's stats<br/>
 - Usage: `<@1275521742961508432>ideaset resetuser <member>`
Extended Arg Info
> ### member: discord.member.Member
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


## <@1275521742961508432>ideaset view
View IdeaBoard settings<br/>
 - Usage: `<@1275521742961508432>ideaset view`


## <@1275521742961508432>ideaset userblacklist
Add/remove a user to/from the user blacklist<br/>
 - Usage: `<@1275521742961508432>ideaset userblacklist <member>`
 - Aliases: `blacklistuser and userbl`
Extended Arg Info
> ### member: Union[discord.member.Member, int]
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


## <@1275521742961508432>ideaset deletethreads
Toggle deleting discussion threads when a suggestion is approved/denied<br/>
 - Usage: `<@1275521742961508432>ideaset deletethreads`
 - Aliases: `delete and delthreads`


## <@1275521742961508432>ideaset toggleanonymous
Toggle allowing anonymous suggestions<br/>
 - Usage: `<@1275521742961508432>ideaset toggleanonymous`
 - Aliases: `toggleanon, anonymous, and anon`


## <@1275521742961508432>ideaset accountage
Set the minimum account age required to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum age in hours required to vote.<br/>
    to_suggest: Minimum age in hours required to suggest.<br/>
 - Usage: `<@1275521742961508432>ideaset accountage <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>ideaset resetall
Reset all user stats<br/>
 - Usage: `<@1275521742961508432>ideaset resetall`


## <@1275521742961508432>ideaset suggestrole
Add/remove a role to the suggest role whitelist<br/>
 - Usage: `<@1275521742961508432>ideaset suggestrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>ideaset upvoteemoji
Set the upvote emoji<br/>
 - Usage: `<@1275521742961508432>ideaset upvoteemoji <emoji>`
 - Aliases: `upvote and up`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>ideaset togglevotecount
Toggle showing vote counts on suggestions<br/>
 - Usage: `<@1275521742961508432>ideaset togglevotecount`
 - Aliases: `votecount`


## <@1275521742961508432>ideaset togglereveal
Toggle reveal suggestion author on approval<br/>

Approved suggestions are ALWAYS revealed regardless of this setting.<br/>
 - Usage: `<@1275521742961508432>ideaset togglereveal`
 - Aliases: `reveal`


## <@1275521742961508432>ideaset showstale
View the numbers of suggestions who's message no longer exists.<br/>
 - Usage: `<@1275521742961508432>ideaset showstale`


## <@1275521742961508432>ideaset approverole
Add/remove a role to the approver role list<br/>
 - Usage: `<@1275521742961508432>ideaset approverole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>ideaset downvoteemoji
Set the downvote emoji<br/>
 - Usage: `<@1275521742961508432>ideaset downvoteemoji <emoji>`
 - Aliases: `downvote and down`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>ideaset voterole
Add/remove a role to the voting role whitelist<br/>
 - Usage: `<@1275521742961508432>ideaset voterole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## <@1275521742961508432>ideaset minlevel
Set the LevelUp integration minimum level required to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum level required to vote.<br/>
    to_suggest: Minimum level required to suggest.<br/>
 - Usage: `<@1275521742961508432>ideaset minlevel <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


