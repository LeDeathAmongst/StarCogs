Make the bot react to messages with your mention, reply, your user ID or a custom trigger, based on roles perks!

# ,personalreact (Hybrid Command)
Make the bot react to messages with your mention, reply, your user ID or a custom trigger!<br/>
 - Usage: `,personalreact`
 - Slash Usage: `/personalreact`
 - Aliases: `pr`
 - Checks: `server_only`
## ,personalreact view (Hybrid Command)
View your PersonalReact settings.<br/>
 - Usage: `,personalreact view`
 - Slash Usage: `/personalreact view`
 - Checks: `server_only`
## ,personalreact customtrigger (Hybrid Command)
Set a custom trigger.<br/>
 - Usage: `,personalreact customtrigger <custom_trigger>`
 - Slash Usage: `/personalreact customtrigger <custom_trigger>`
 - Checks: `server_only`
Extended Arg Info
> ### custom_trigger: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,personalreact ignorebots (Hybrid Command)
Ignore bots.<br/>
 - Usage: `,personalreact ignorebots <toggle>`
 - Slash Usage: `/personalreact ignorebots <toggle>`
 - Checks: `server_only`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,personalreact addreactions (Hybrid Command)
Add reaction(s).<br/>
 - Usage: `,personalreact addreactions <reactions>`
 - Slash Usage: `/personalreact addreactions <reactions>`
 - Aliases: `addreaction, addreacts, and addreact`
 - Checks: `server_only`
## ,personalreact disable (Hybrid Command)
Disable PersonalReact for you.<br/>
 - Usage: `,personalreact disable`
 - Slash Usage: `/personalreact disable`
 - Checks: `server_only`
## ,personalreact enable (Hybrid Command)
Enable PersonalReact for you.<br/>
 - Usage: `,personalreact enable`
 - Slash Usage: `/personalreact enable`
 - Checks: `server_only`
## ,personalreact reactions (Hybrid Command)
Set your reactions.<br/>
 - Usage: `,personalreact reactions <reactions>`
 - Slash Usage: `/personalreact reactions <reactions>`
 - Aliases: `reacts`
 - Checks: `server_only`
## ,personalreact ignoremyself (Hybrid Command)
Ignore yourself.<br/>
 - Usage: `,personalreact ignoremyself <toggle>`
 - Slash Usage: `/personalreact ignoremyself <toggle>`
 - Checks: `server_only`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,personalreact userid (Hybrid Command)
Allow the bot to react on the messages which contain your user ID.<br/>
 - Usage: `,personalreact userid <toggle>`
 - Slash Usage: `/personalreact userid <toggle>`
 - Checks: `server_only`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,personalreact replies (Hybrid Command)
Allow the bot to react on the messages which ping you in replies.<br/>
 - Usage: `,personalreact replies <toggle>`
 - Slash Usage: `/personalreact replies <toggle>`
 - Checks: `server_only`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,personalreact removereactions (Hybrid Command)
Remove reaction(s).<br/>
 - Usage: `,personalreact removereactions <reactions>`
 - Slash Usage: `/personalreact removereactions <reactions>`
 - Aliases: `removereaction, removereacts, and removereact`
 - Checks: `server_only`
# ,setpersonalreact (Hybrid Command)
Set PersonalReact settings.<br/>
 - Usage: `,setpersonalreact`
 - Slash Usage: `/setpersonalreact`
 - Restricted to: `ADMIN`
 - Aliases: `setpr`
 - Checks: `server_only`
## ,setpersonalreact clearmember (Hybrid Command)
Clear a member's PersonalReact settings.<br/>
 - Usage: `,setpersonalreact clearmember <member>`
 - Slash Usage: `/setpersonalreact clearmember <member>`
 - Checks: `server_only`
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
## ,setpersonalreact resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setpersonalreact resetsetting <setting>`
 - Slash Usage: `/setpersonalreact resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,setpersonalreact blacklistedchannels (Hybrid Command)
The channels where the bot won't react.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Union]`<br/>
 - Usage: `,setpersonalreact blacklistedchannels <value>`
 - Slash Usage: `/setpersonalreact blacklistedchannels <value>`
 - Checks: `server_only`
## ,setpersonalreact roles (Hybrid Command)
Set the roles requirements.<br/>
 - Usage: `,setpersonalreact roles`
 - Slash Usage: `/setpersonalreact roles`
 - Aliases: `view`
 - Checks: `server_only`
## ,setpersonalreact removectrolesrequirements (Hybrid Command)
Remove custom trigger roles requirements.<br/>
 - Usage: `,setpersonalreact removectrolesrequirements <roles>`
 - Slash Usage: `/setpersonalreact removectrolesrequirements <roles>`
 - Aliases: `removectrolerequirement, removectrolesreq, and removectrolereq`
 - Checks: `server_only`
## ,setpersonalreact mincustomtriggerlength (Hybrid Command)
The minimum length of a custom trigger.<br/>

Default value: `3`<br/>
Dev: `Range[int, 3, 8]`<br/>
 - Usage: `,setpersonalreact mincustomtriggerlength <value>`
 - Slash Usage: `/setpersonalreact mincustomtriggerlength <value>`
 - Checks: `server_only`
## ,setpersonalreact maxreactionspermember (Hybrid Command)
The maximum number of reactions a member can set for them.<br/>

Default value: `5`<br/>
Dev: `Range[int, 1, 8]`<br/>
 - Usage: `,setpersonalreact maxreactionspermember <value>`
 - Slash Usage: `/setpersonalreact maxreactionspermember <value>`
 - Checks: `server_only`
## ,setpersonalreact alwaysallowcustomtrigger (Hybrid Command)
Whether to always allow the custom trigger feature.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setpersonalreact alwaysallowcustomtrigger <value>`
 - Slash Usage: `/setpersonalreact alwaysallowcustomtrigger <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setpersonalreact showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setpersonalreact showsettings [with_dev=False]`
 - Slash Usage: `/setpersonalreact showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setpersonalreact useamountssum (Hybrid Command)
Whether to use the sum of the roles requirements or the maximum amount.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setpersonalreact useamountssum <value>`
 - Slash Usage: `/setpersonalreact useamountssum <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setpersonalreact addctrolesrequirements (Hybrid Command)
Add custom trigger roles requirements.<br/>
 - Usage: `,setpersonalreact addctrolesrequirements <roles> <amount>`
 - Slash Usage: `/setpersonalreact addctrolesrequirements <roles> <amount>`
 - Aliases: `addctrolerequirement, addctrolesreq, and addctrolereq`
 - Checks: `server_only`
## ,setpersonalreact removebaserolesrequirements (Hybrid Command)
Remove base roles requirements.<br/>
 - Usage: `,setpersonalreact removebaserolesrequirements <roles>`
 - Slash Usage: `/setpersonalreact removebaserolesrequirements <roles>`
 - Aliases: `removebaserolerequirement, removebaserolesreq, and removebaserolereq`
 - Checks: `server_only`
## ,setpersonalreact modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setpersonalreact modalconfig [confirmation=False]`
 - Slash Usage: `/setpersonalreact modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setpersonalreact addbaserolesrequirements (Hybrid Command)
Add base roles requirements.<br/>
 - Usage: `,setpersonalreact addbaserolesrequirements <roles> <amount>`
 - Slash Usage: `/setpersonalreact addbaserolesrequirements <roles> <amount>`
 - Aliases: `addbaserolerequirement, addbaserolesreq, and addbaserolereq`
 - Checks: `server_only`
## ,setpersonalreact purge (Hybrid Command)

 - Usage: `,setpersonalreact purge [confirmation=False]`
 - Slash Usage: `/setpersonalreact purge [confirmation=False]`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,setpersonalreact allowrepliestrigger (Hybrid Command)
Whether to allow the replies trigger.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setpersonalreact allowrepliestrigger <value>`
 - Slash Usage: `/setpersonalreact allowrepliestrigger <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```