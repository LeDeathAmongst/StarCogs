IdeaBoard
=========

Share Ideas and Suggestions

# ,idea (Hybrid Command)
Share an idea/make a suggestion.<br/>
 - Usage: `,idea <content>`
 - Slash Usage: `/idea <content>`
 - Aliases: `suggest`
 - Checks: `bot_has_server_permissions and server_only`
Extended Arg Info
> ### content: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,ideastats (Hybrid Command)
Display your current profile stats for suggestions and votes.<br/>
 - Usage: `,ideastats [member]`
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


# ,approve (Hybrid Command)
Approve an idea/suggestion.<br/>
 - Usage: `,approve <number> [reason]`
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


# ,reject (Hybrid Command)
Reject an idea/suggestion.<br/>
 - Usage: `,reject <number> [reason]`
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


# ,viewvotes (Hybrid Command)
View the list of who has upvoted and who has downvoted a suggestion.<br/>
 - Usage: `,viewvotes <number>`
 - Slash Usage: `/viewvotes <number>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


# ,refresh (Hybrid Command)
Refresh the buttons on a suggestion if it gets stuck.<br/>
 - Usage: `,refresh <number>`
 - Slash Usage: `/refresh <number>`
 - Checks: `server_only`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


# ,ideaset
Manage IdeaBoard settings<br/>
 - Usage: `,ideaset`
 - Restricted to: `ADMIN`
 - Aliases: `ideaboard`


## ,ideaset insights
View insights about the server's suggestions.<br/>

**Arguments**<br/>
- `amount` The number of top users to display for each section.<br/>
 - Usage: `,ideaset insights [amount=3]`
Extended Arg Info
> ### amount: int = 3
> ```
> A number without decimal places.
> ```


## ,ideaset rolecooldown
Set the suggestion cooldown for a specific role<br/>

To remove a role cooldown, specify 0 as the cooldown.<br/>
 - Usage: `,ideaset rolecooldown <role> <cooldown>`
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


## ,ideaset jointime
Set the minimum time a user must be in the server to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum time in hours required to vote.<br/>
    to_suggest: Minimum time in hours required to suggest.<br/>
 - Usage: `,ideaset jointime <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


## ,ideaset discussions
Toggle opening a discussion thread for each suggestion<br/>
 - Usage: `,ideaset discussions`
 - Aliases: `threads and discussion`


## ,ideaset resetuser
Reset a user's stats<br/>
 - Usage: `,ideaset resetuser <member>`
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


## ,ideaset userblacklist
Add/remove a user to/from the user blacklist<br/>
 - Usage: `,ideaset userblacklist <member>`
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


## ,ideaset deletethreads
Toggle deleting discussion threads when a suggestion is approved/denied<br/>
 - Usage: `,ideaset deletethreads`
 - Aliases: `delete and delthreads`


## ,ideaset toggleanonymous
Toggle allowing anonymous suggestions<br/>
 - Usage: `,ideaset toggleanonymous`
 - Aliases: `toggleanon, anonymous, and anon`


## ,ideaset accountage
Set the minimum account age required to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum age in hours required to vote.<br/>
    to_suggest: Minimum age in hours required to suggest.<br/>
 - Usage: `,ideaset accountage <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


## ,ideaset resetall
Reset all user stats<br/>
 - Usage: `,ideaset resetall`


## ,ideaset suggestrole
Add/remove a role to the suggest role whitelist<br/>
 - Usage: `,ideaset suggestrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## ,ideaset upvoteemoji
Set the upvote emoji<br/>
 - Usage: `,ideaset upvoteemoji <emoji>`
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


## ,ideaset togglereveal
Toggle reveal suggestion author on approval<br/>

Approved suggestions are ALWAYS revealed regardless of this setting.<br/>
 - Usage: `,ideaset togglereveal`
 - Aliases: `reveal`


## ,ideaset showstale
View the numbers of suggestions who's message no longer exists.<br/>
 - Usage: `,ideaset showstale`


## ,ideaset approverole
Add/remove a role to the approver role list<br/>
 - Usage: `,ideaset approverole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## ,ideaset minlevel
Set the LevelUp integration minimum level required to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum level required to vote.<br/>
    to_suggest: Minimum level required to suggest.<br/>
 - Usage: `,ideaset minlevel <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


## ,ideaset downvoteemoji
Set the downvote emoji<br/>
 - Usage: `,ideaset downvoteemoji <emoji>`
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


## ,ideaset view
View IdeaBoard settings<br/>
 - Usage: `,ideaset view`


## ,ideaset togglevotecount
Toggle showing vote counts on suggestions<br/>
 - Usage: `,ideaset togglevotecount`
 - Aliases: `votecount`


## ,ideaset cleanup
Cleanup the config.<br/>
- Remove suggestions who's message no longer exists.<br/>
- Remove profiles of users who have left the server.<br/>
- Remove votes from users who have left the server.<br/>
 - Usage: `,ideaset cleanup`


## ,ideaset voterole
Add/remove a role to the voting role whitelist<br/>
 - Usage: `,ideaset voterole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


## ,ideaset roleblacklist
Add/remove a role to/from the role blacklist<br/>
 - Usage: `,ideaset roleblacklist <role>`
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


## ,ideaset channel
Set the approved, rejected, or pending channels for IdeaBoard<br/>
 - Usage: `,ideaset channel <channel> <channel_type>`
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


## ,ideaset toggledm
Toggle DMing users the results of suggestions they made<br/>
 - Usage: `,ideaset toggledm`
 - Aliases: `dm`


## ,ideaset minplaytime
Set the ArkTools integration minimum playtime required to vote and suggest.<br/>

Args:<br/>
    to_vote: Minimum playtime in hours required to vote.<br/>
    to_suggest: Minimum playtime in hours required to suggest.<br/>
 - Usage: `,ideaset minplaytime <to_vote> <to_suggest>`
Extended Arg Info
> ### to_vote: int
> ```
> A number without decimal places.
> ```
> ### to_suggest: int
> ```
> A number without decimal places.
> ```


## ,ideaset cooldown
Set the base cooldown for making suggestions<br/>
 - Usage: `,ideaset cooldown <cooldown>`
 - Aliases: `cd`
Extended Arg Info
> ### cooldown: int
> ```
> A number without decimal places.
> ```


