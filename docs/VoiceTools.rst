VoiceTools
==========

Various tools to make voice channels better!

# <@1275521742961508432>voicetools
Settings for voice tools.<br/>
 - Usage: `<@1275521742961508432>voicetools`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## <@1275521742961508432>voicetools forcelimit
Settings for ForceLimit module.<br/>

Force user limit to all members of the server including admins<br/>
(Kicking is done the same way as in `<@1275521742961508432>voicekick`)<br/>

When combined with VIP module, this won't kick VIPs going over limit<br/>
You can also add user or role to this module's ignore list,<br/>
if you want to ignore going over limit while not raising user limit for channel<br/>
or you can ignore chosen channels to stop bot from kicking users from it.<br/>
 - Usage: `<@1275521742961508432>voicetools forcelimit`


### <@1275521742961508432>voicetools forcelimit ignore
Adds members, roles or voice channels to ignorelist of ForceLimit module.<br/>

Members and roles on ignorelist will bypass forcelimit<br/>
(meaning - not getting kicked)<br/>

Voice channels on ignorelist won't be checked<br/>
(as if ForceLimit module was disabled for them)<br/>
 - Usage: `<@1275521742961508432>voicetools forcelimit ignore <ignores>`


### <@1275521742961508432>voicetools forcelimit enable
Enables ForceLimit module.<br/>
 - Usage: `<@1275521742961508432>voicetools forcelimit enable`


### <@1275521742961508432>voicetools forcelimit disable
Disables ForceLimit module.<br/>
 - Usage: `<@1275521742961508432>voicetools forcelimit disable`


### <@1275521742961508432>voicetools forcelimit ignorelist
Shows ignorelist of ForceLimit module.<br/>

This can include members and roles which bypass forcelimit<br/>
and voice channels which won't be checked.<br/>
 - Usage: `<@1275521742961508432>voicetools forcelimit ignorelist`


### <@1275521742961508432>voicetools forcelimit unignore
Adds members, roles or voice channels to ignorelist of ForceLimit module<br/>

Members and roles on ignorelist will bypass forcelimit<br/>
(meaning - not getting kicked)<br/>

Voice channels on ignorelist won't be checked<br/>
(as if ForceLimit module was disabled for them)<br/>
 - Usage: `<@1275521742961508432>voicetools forcelimit unignore <ignores>`


## <@1275521742961508432>voicetools vip
Settings for VIP module.<br/>

Set members and roles to not count to user limit in voice channel<br/>
(limit will be raised accordingly after they join to make it possible)<br/>
 - Usage: `<@1275521742961508432>voicetools vip`


### <@1275521742961508432>voicetools vip disable
Disables VIP module.<br/>
 - Usage: `<@1275521742961508432>voicetools vip disable`


### <@1275521742961508432>voicetools vip remove
Removes members and roles to vip list of VIP module.<br/>

VIP members and roles will not count to user limit in voice channel.<br/>
 - Usage: `<@1275521742961508432>voicetools vip remove <vips>`


### <@1275521742961508432>voicetools vip list
Shows vip list of VIP module.<br/>

Members and roles specified here will not count to user limit in voice channel.<br/>
 - Usage: `<@1275521742961508432>voicetools vip list`


### <@1275521742961508432>voicetools vip enable
Enables VIP module.<br/>
 - Usage: `<@1275521742961508432>voicetools vip enable`


### <@1275521742961508432>voicetools vip add
Adds members and roles to vip list of VIP module.<br/>

VIP members and roles will not count to user limit in voice channel.<br/>
 - Usage: `<@1275521742961508432>voicetools vip add <vips>`


