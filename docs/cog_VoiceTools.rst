VoiceTools
==========

Various tools to make voice channels better!

# ,voicetools
Settings for voice tools.<br/>
 - Usage: `,voicetools`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,voicetools forcelimit
Settings for ForceLimit module.<br/>

Force user limit to all members of the server including admins<br/>
(Kicking is done the same way as in `,voicekick`)<br/>

When combined with VIP module, this won't kick VIPs going over limit<br/>
You can also add user or role to this module's ignore list,<br/>
if you want to ignore going over limit while not raising user limit for channel<br/>
or you can ignore chosen channels to stop bot from kicking users from it.<br/>
 - Usage: `,voicetools forcelimit`


### ,voicetools forcelimit unignore
Adds members, roles or voice channels to ignorelist of ForceLimit module<br/>

Members and roles on ignorelist will bypass forcelimit<br/>
(meaning - not getting kicked)<br/>

Voice channels on ignorelist won't be checked<br/>
(as if ForceLimit module was disabled for them)<br/>
 - Usage: `,voicetools forcelimit unignore <ignores>`


### ,voicetools forcelimit ignore
Adds members, roles or voice channels to ignorelist of ForceLimit module.<br/>

Members and roles on ignorelist will bypass forcelimit<br/>
(meaning - not getting kicked)<br/>

Voice channels on ignorelist won't be checked<br/>
(as if ForceLimit module was disabled for them)<br/>
 - Usage: `,voicetools forcelimit ignore <ignores>`


### ,voicetools forcelimit enable
Enables ForceLimit module.<br/>
 - Usage: `,voicetools forcelimit enable`


### ,voicetools forcelimit ignorelist
Shows ignorelist of ForceLimit module.<br/>

This can include members and roles which bypass forcelimit<br/>
and voice channels which won't be checked.<br/>
 - Usage: `,voicetools forcelimit ignorelist`


### ,voicetools forcelimit disable
Disables ForceLimit module.<br/>
 - Usage: `,voicetools forcelimit disable`


## ,voicetools vip
Settings for VIP module.<br/>

Set members and roles to not count to user limit in voice channel<br/>
(limit will be raised accordingly after they join to make it possible)<br/>
 - Usage: `,voicetools vip`


### ,voicetools vip disable
Disables VIP module.<br/>
 - Usage: `,voicetools vip disable`


### ,voicetools vip remove
Removes members and roles to vip list of VIP module.<br/>

VIP members and roles will not count to user limit in voice channel.<br/>
 - Usage: `,voicetools vip remove <vips>`


### ,voicetools vip enable
Enables VIP module.<br/>
 - Usage: `,voicetools vip enable`


### ,voicetools vip add
Adds members and roles to vip list of VIP module.<br/>

VIP members and roles will not count to user limit in voice channel.<br/>
 - Usage: `,voicetools vip add <vips>`


### ,voicetools vip list
Shows vip list of VIP module.<br/>

Members and roles specified here will not count to user limit in voice channel.<br/>
 - Usage: `,voicetools vip list`


