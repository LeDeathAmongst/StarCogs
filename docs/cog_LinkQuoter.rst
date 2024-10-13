LinkQuoter
==========

Quote any Discord message from its link!

<<<<<<< HEAD
# <@1275521742961508432>linkquote (Hybrid Command)
Quote a message from a link.<br/>
 - Usage: `<@1275521742961508432>linkquote [message]`
=======
# ,linkquote (Hybrid Command)
Quote a message from a link.<br/>
 - Usage: `,linkquote [message]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/linkquote [message]`
 - Aliases: `linquoter and lq`
 - Cooldown: `3 per 10.0 seconds`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>setlinkquoter (Hybrid Command)
Commands to configure LinkQuoter.<br/>
 - Usage: `<@1275521742961508432>setlinkquoter`
=======
# ,setlinkquoter (Hybrid Command)
Commands to configure LinkQuoter.<br/>
 - Usage: `,setlinkquoter`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setlinkquoter`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>setlinkquoter resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `<@1275521742961508432>setlinkquoter resetsetting <setting>`
=======
## ,setlinkquoter resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setlinkquoter resetsetting <setting>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setlinkquoter resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setlinkquoter deleteafter (Hybrid Command)
Set the time in seconds to delete the message after.<br/>

Default value: `0`<br/>
Dev: `<class 'int'>`<br/>
 - Usage: `<@1275521742961508432>setlinkquoter deleteafter <value>`
 - Slash Usage: `/setlinkquoter deleteafter <value>`
 - Aliases: `delete_time`
 - Checks: `server_only`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>setlinkquoter blacklistchannels (Hybrid Command)
Set the channels in which auto-quoting will be disabled.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
 - Usage: `<@1275521742961508432>setlinkquoter blacklistchannels <value>`
 - Slash Usage: `/setlinkquoter blacklistchannels <value>`
 - Aliases: `blacklist`
 - Checks: `server_only`


## <@1275521742961508432>setlinkquoter enabled (Hybrid Command)
=======
## ,setlinkquoter enabled (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Toggle automatic link-quoting.<br/>

Enabling this will make Starfire attempt to quote any message link that is sent in this server.<br/>
Starfire will ignore any message that has `no quote` in it.<br/>
If the user doesn't have permission to view the channel that they link, it will not quote.<br/>

<<<<<<< HEAD
To enable quoting from other servers, run `<@1275521742961508432>linkquoteset global`.<br/>
=======
To enable quoting from other servers, run `,linkquoteset global`.<br/>
>>>>>>> 9e308722 (Revamped and Fixed)

To prevent spam, links can be automatically quoted 3 times every 10 seconds.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setlinkquoter enabled <value>`
=======
 - Usage: `,setlinkquoter enabled <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setlinkquoter enabled <value>`
 - Aliases: `auto`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setlinkquoter whitelistchannels (Hybrid Command)
Set the channels in which auto-quoting will be enabled.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
 - Usage: `<@1275521742961508432>setlinkquoter whitelistchannels <value>`
 - Slash Usage: `/setlinkquoter whitelistchannels <value>`
 - Aliases: `whitelist`
 - Checks: `server_only`


## <@1275521742961508432>setlinkquoter showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>setlinkquoter showsettings [with_dev=False]`
 - Slash Usage: `/setlinkquoter showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setlinkquoter webhooks (Hybrid Command)
Toggle sending message with the name and avatar of the Author of the quote (with webhooks)<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setlinkquoter webhooks <value>`
 - Slash Usage: `/setlinkquoter webhooks <value>`
 - Aliases: `webhook`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setlinkquoter migratefromphen (Hybrid Command)
Migrate config from LinkQuoter by Phen.<br/>
 - Usage: `<@1275521742961508432>setlinkquoter migratefromphen`
 - Slash Usage: `/setlinkquoter migratefromphen`
 - Restricted to: `BOT_OWNER`
 - Aliases: `migratefromlinkquoter`
 - Checks: `server_only`


## <@1275521742961508432>setlinkquoter crossserver (Hybrid Command)
=======
## ,setlinkquoter crossserver (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Toggle cross-server quoting.<br/>

Turning this setting on will allow this server to quote other servers, and other servers to quote this one.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setlinkquoter crossserver <value>`
=======
 - Usage: `,setlinkquoter crossserver <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setlinkquoter crossserver <value>`
 - Aliases: `global`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setlinkquoter deletemessagebutton (Hybrid Command)
Toggle the delete message button on the quote messages.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setlinkquoter deletemessagebutton <value>`
 - Slash Usage: `/setlinkquoter deletemessagebutton <value>`
 - Aliases: `delete_button`
=======
## ,setlinkquoter blacklistchannels (Hybrid Command)
Set the channels in which auto-quoting will be disabled.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
 - Usage: `,setlinkquoter blacklistchannels <value>`
 - Slash Usage: `/setlinkquoter blacklistchannels <value>`
 - Aliases: `blacklist`
 - Checks: `server_only`


## ,setlinkquoter webhooks (Hybrid Command)
Toggle sending message with the name and avatar of the Author of the quote (with webhooks)<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setlinkquoter webhooks <value>`
 - Slash Usage: `/setlinkquoter webhooks <value>`
 - Aliases: `webhook`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setlinkquoter deletemessage (Hybrid Command)
=======
## ,setlinkquoter deletemessage (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Toggle deleting of messages for automatic quoting.<br/>

If automatic quoting is enabled, then Starfire will also delete messages that contain links in them.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setlinkquoter deletemessage <value>`
=======
 - Usage: `,setlinkquoter deletemessage <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setlinkquoter deletemessage <value>`
 - Aliases: `delete`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setlinkquoter modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `<@1275521742961508432>setlinkquoter modalconfig [confirmation=False]`
=======
## ,setlinkquoter showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setlinkquoter showsettings [with_dev=False]`
 - Slash Usage: `/setlinkquoter showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setlinkquoter deleteafter (Hybrid Command)
Set the time in seconds to delete the message after.<br/>

Default value: `0`<br/>
Dev: `<class 'int'>`<br/>
 - Usage: `,setlinkquoter deleteafter <value>`
 - Slash Usage: `/setlinkquoter deleteafter <value>`
 - Aliases: `delete_time`
 - Checks: `server_only`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```


## ,setlinkquoter whitelistchannels (Hybrid Command)
Set the channels in which auto-quoting will be enabled.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
 - Usage: `,setlinkquoter whitelistchannels <value>`
 - Slash Usage: `/setlinkquoter whitelistchannels <value>`
 - Aliases: `whitelist`
 - Checks: `server_only`


## ,setlinkquoter migratefromphen (Hybrid Command)
Migrate config from LinkQuoter by Phen.<br/>
 - Usage: `,setlinkquoter migratefromphen`
 - Slash Usage: `/setlinkquoter migratefromphen`
 - Restricted to: `BOT_OWNER`
 - Aliases: `migratefromlinkquoter`
 - Checks: `server_only`


## ,setlinkquoter deletemessagebutton (Hybrid Command)
Toggle the delete message button on the quote messages.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setlinkquoter deletemessagebutton <value>`
 - Slash Usage: `/setlinkquoter deletemessagebutton <value>`
 - Aliases: `delete_button`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setlinkquoter modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setlinkquoter modalconfig [confirmation=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setlinkquoter modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


