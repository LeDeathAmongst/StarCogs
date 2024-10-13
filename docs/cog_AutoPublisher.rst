AutoPublisher
=============

Automatically push news channel messages.

# ,autopublisher
Manage AutoPublisher setting.<br/>
 - Usage: `,autopublisher`
 - Restricted to: `ADMIN`
 - Aliases: `aph and autopub`
 - Checks: `server_only`


## ,autopublisher resetcount
Reset the published messages count.<br/>
 - Usage: `,autopublisher resetcount`
 - Restricted to: `BOT_OWNER`


## ,autopublisher version
Shows the version of the cog.<br/>
 - Usage: `,autopublisher version`


## ,autopublisher ignorechannel
Ignore/Unignore a news channel to prevent AutoPublisher from publishing messages in it.<br/>

You can provide multiple channels to ignore or unignore at once.<br/>
You decide if you wanna use the select menu or provide the channel(s) manually in the command.<br/>
 - Usage: `,autopublisher ignorechannel <channels>`


## ,autopublisher toggle
Toggle AutoPublisher enable or disable.<br/>

- It's disabled by default.<br/>
    - Please ensure that the bot has access to `view_channel` in your news channels. it also need `manage_messages` to be able to publish.<br/>

**Note:**<br/>
- This cog requires News Channel. If you don't have it, you can't use this cog.<br/>
    - Learn more [here on how to enable](https://support.discord.com/hc/en-us/articles/360047132851-Enabling-Your-Community-Server) community server. (which is a part of news channel feature.)<br/>
 - Usage: `,autopublisher toggle`


## ,autopublisher settings
Show AutoPublisher setting.<br/>
 - Usage: `,autopublisher settings`
 - Aliases: `view`


## ,autopublisher stats
Show the number of published messages.<br/>
 - Usage: `,autopublisher stats`
 - Restricted to: `BOT_OWNER`


## ,autopublisher reset
Reset AutoPublisher setting.<br/>
 - Usage: `,autopublisher reset`


