# DisurlVotesTracker Help

### disurlvotestracker

**Description:** Commands to interact with DisurlVotesTracker.

**Usage:** `<@1275521742961508432>disurlvotestracker`

### disurlvotestracker monthlyleaderboard

**Description:** Show the monthly leaderboard of voters.

**Usage:** `<@1275521742961508432>disurlvotestracker monthlyleaderboard`

### disurlvotestracker leaderboard

**Description:** Show the lifetime leaderboard of voters.

**Usage:** `<@1275521742961508432>disurlvotestracker leaderboard`

### setdisurlvotestracker

**Description:** Commands to configure DisurlVotesTracker.

**Usage:** `<@1275521742961508432>setdisurlvotestracker`

### setdisurlvotestracker showsettings

**Description:** Show all settings for the cog with defaults and values.

**Usage:** `<@1275521742961508432>setdisurlvotestracker showsettings`

### setdisurlvotestracker customvotemessage

**Description:** Custom vote message. You can specify the ID or the link of an existing message, or provide an embed payload. Use the variables `{member_name}`, `{member_avatar_url}`, `{member_mention}`, `{member_id}`, `{guild_name}`, `{guild_icon_url}`, `{guild_id}`, `{votes_channel_name}`, `{votes_channel_mention}`, `{votes_channel_id}`, `{voters_role_name}`, `{voters_role_mention}`, `{voters_role_id}`, `{number_member_votes}`, `{number_member_monthly_votes}`, `{s_1}` (`number_member_votes` plural) and `{s_2}` (`number_member_monthly_votes` plural).

Default value: `None`
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`

**Usage:** `<@1275521742961508432>setdisurlvotestracker customvotemessage`

### setdisurlvotestracker customvoteremindermessage

**Description:** Custom vote reminder message. You can specify the ID or the link of an existing message, or provide an embed payload. Use the variables `{member_name}`, `{member_avatar_url}`, `{member_mention}`, `{member_id}`, `{guild_name}`, `{guild_icon_url}`, `{guild_id}`, `{votes_channel_name}`, `{votes_channel_mention}`, `{votes_channel_id}`, `{voters_role_name}`, `{voters_role_mention}`, `{voters_role_id}`, `{number_member_votes}`, `{number_member_monthly_votes}`, `{s_1}` (`number_member_votes` plural) and `{s_2}` (`number_member_monthly_votes` plural).

Default value: `None`
Dev: `<class 'AAA3A_utils.settings.CustomMessageConverter'>`

**Usage:** `<@1275521742961508432>setdisurlvotestracker customvoteremindermessage`

### setdisurlvotestracker resetleaderboards

**Description:** Reset the leaderboards.

**Usage:** `<@1275521742961508432>setdisurlvotestracker resetleaderboards`

### setdisurlvotestracker modalconfig

**Description:** Set all settings for the cog with a Discord Modal.

**Usage:** `<@1275521742961508432>setdisurlvotestracker modalconfig`

### setdisurlvotestracker votersrole

**Description:** The role that will be assigned to voters.

Default value: `None`
Dev: `<class 'disurlvotestracker.converter.RoleHierarchyConverter'>`

**Usage:** `<@1275521742961508432>setdisurlvotestracker votersrole`

### setdisurlvotestracker votereminder

**Description:** Toggle vote reminders. A reminder will be sent to voters 12 hours after their vote.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdisurlvotestracker votereminder`

### setdisurlvotestracker resetsetting

**Description:** Reset a setting.

**Usage:** `<@1275521742961508432>setdisurlvotestracker resetsetting`

### setdisurlvotestracker voteschannel

**Description:** The channel where votes notifications will be sent.

Default value: `None`
Dev: `typing.Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]`

**Usage:** `<@1275521742961508432>setdisurlvotestracker voteschannel`

### setdisurlvotestracker instructions

**Description:** Instructions on how to set up DisurlVotesTracker.

**Usage:** `<@1275521742961508432>setdisurlvotestracker instructions`

### setdisurlvotestracker enabled

**Description:** Toggle the cog. WARNING: Red-Dashboard has to be installed and started for this to work.

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setdisurlvotestracker enabled`

### setdisurlvotestracker disurlauthaurizationkey

**Description:** Your Disurl authorization key, used to secure the Dashboard webhook. That's the key which you set on https://disurl.me/dashboard/server/GUILD_ID/webhooks.

Default value: `None`
Dev: `<class 'str'>`

**Usage:** `<@1275521742961508432>setdisurlvotestracker disurlauthaurizationkey`

