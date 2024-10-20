Track votes on Disurl, assign roles to voters and remind them to vote!

# ,disurlvotestracker (Hybrid Command)
Commands to interact with DisurlVotesTracker.<br/>
 - Usage: `,disurlvotestracker`
 - Slash Usage: `/disurlvotestracker`
 - Aliases: `dvt`
 - Checks: `server_only`
## ,disurlvotestracker monthlyleaderboard (Hybrid Command)
Show the monthly leaderboard of voters.<br/>
 - Usage: `,disurlvotestracker monthlyleaderboard`
 - Slash Usage: `/disurlvotestracker monthlyleaderboard`
 - Checks: `server_only`
## ,disurlvotestracker leaderboard (Hybrid Command)
Show the lifetime leaderboard of voters.<br/>
 - Usage: `,disurlvotestracker leaderboard`
 - Slash Usage: `/disurlvotestracker leaderboard`
 - Checks: `server_only`
# ,setdisurlvotestracker (Hybrid Command)
Commands to configure DisurlVotesTracker.<br/>
 - Usage: `,setdisurlvotestracker`
 - Slash Usage: `/setdisurlvotestracker`
 - Restricted to: `ADMIN`
 - Aliases: `setdvt`
 - Checks: `server_only`
## ,setdisurlvotestracker customvoteremindermessage (Hybrid Command)
Custom vote reminder message. You can specify the ID or the link of an existing message, or provide an embed payload. Use the variables `{member_name}`, `{member_avatar_url}`, `{member_mention}`, `{member_id}`, `{server_name}`, `{server_icon_url}`, `{server_id}`, `{votes_channel_name}`, `{votes_channel_mention}`, `{votes_channel_id}`, `{voters_role_name}`, `{voters_role_mention}`, `{voters_role_id}`, `{number_member_votes}`, `{number_member_monthly_votes}`, `{s_1}` (`number_member_votes` plural) and `{s_2}` (`number_member_monthly_votes` plural).<br/>

Default value: `None`<br/>
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`<br/>
 - Usage: `,setdisurlvotestracker customvoteremindermessage <value>`
 - Slash Usage: `/setdisurlvotestracker customvoteremindermessage <value>`
 - Checks: `server_only`
## ,setdisurlvotestracker resetleaderboards (Hybrid Command)
Reset the leaderboards.<br/>
 - Usage: `,setdisurlvotestracker resetleaderboards [confirmation=False]`
 - Slash Usage: `/setdisurlvotestracker resetleaderboards [confirmation=False]`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setdisurlvotestracker votereminder (Hybrid Command)
Toggle vote reminders. A reminder will be sent to voters 12 hours after their vote.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setdisurlvotestracker votereminder <value>`
 - Slash Usage: `/setdisurlvotestracker votereminder <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setdisurlvotestracker showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setdisurlvotestracker showsettings [with_dev=False]`
 - Slash Usage: `/setdisurlvotestracker showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setdisurlvotestracker enabled (Hybrid Command)
Toggle the cog. WARNING: Red-Dashboard has to be installed and started for this to work.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setdisurlvotestracker enabled <value>`
 - Slash Usage: `/setdisurlvotestracker enabled <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setdisurlvotestracker getdebugloopsstatus (Hybrid Command)
Get an embed for check loop status.<br/>
 - Usage: `,setdisurlvotestracker getdebugloopsstatus`
 - Slash Usage: `/setdisurlvotestracker getdebugloopsstatus`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
## ,setdisurlvotestracker disurlauthaurizationkey (Hybrid Command)
Your Disurl authorization key, used to secure the Dashboard webhook. That's the key which you set on https://disurl.me/dashboard/server/GUILD_ID/webhooks.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,setdisurlvotestracker disurlauthaurizationkey <value>`
 - Slash Usage: `/setdisurlvotestracker disurlauthaurizationkey <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setdisurlvotestracker votersrole (Hybrid Command)
The role that will be assigned to voters.<br/>

Default value: `None`<br/>
Dev: `<class 'disurlvotestracker.converter.RoleHierarchyConverter'>`<br/>
 - Usage: `,setdisurlvotestracker votersrole <value>`
 - Slash Usage: `/setdisurlvotestracker votersrole <value>`
 - Checks: `server_only`
## ,setdisurlvotestracker customvotemessage (Hybrid Command)
Custom vote message. You can specify the ID or the link of an existing message, or provide an embed payload. Use the variables `{member_name}`, `{member_avatar_url}`, `{member_mention}`, `{member_id}`, `{server_name}`, `{server_icon_url}`, `{server_id}`, `{votes_channel_name}`, `{votes_channel_mention}`, `{votes_channel_id}`, `{voters_role_name}`, `{voters_role_mention}`, `{voters_role_id}`, `{number_member_votes}`, `{number_member_monthly_votes}`, `{s_1}` (`number_member_votes` plural) and `{s_2}` (`number_member_monthly_votes` plural).<br/>

Default value: `None`<br/>
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`<br/>
 - Usage: `,setdisurlvotestracker customvotemessage <value>`
 - Slash Usage: `/setdisurlvotestracker customvotemessage <value>`
 - Checks: `server_only`
## ,setdisurlvotestracker instructions (Hybrid Command)
Instructions on how to set up DisurlVotesTracker.<br/>
 - Usage: `,setdisurlvotestracker instructions`
 - Slash Usage: `/setdisurlvotestracker instructions`
 - Checks: `server_only`
## ,setdisurlvotestracker voteschannel (Hybrid Command)
The channel where votes notifications will be sent.<br/>

Default value: `None`<br/>
Dev: `typing.Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]`<br/>
 - Usage: `,setdisurlvotestracker voteschannel <value>`
 - Slash Usage: `/setdisurlvotestracker voteschannel <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,setdisurlvotestracker resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setdisurlvotestracker resetsetting <setting>`
 - Slash Usage: `/setdisurlvotestracker resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setdisurlvotestracker modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setdisurlvotestracker modalconfig [confirmation=False]`
 - Slash Usage: `/setdisurlvotestracker modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```