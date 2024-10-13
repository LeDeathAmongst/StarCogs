Calculator
==========

A cog to do calculations from Discord with buttons!

# ,calculate (Hybrid Command)
Calculate a simple expression.<br/>
 - Usage: `,calculate [calculation]`
 - Slash Usage: `/calculate [calculation]`
 - Aliases: `calc`
Extended Arg Info
> ### calculation: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,setcalculator (Hybrid Command)
Commands to configure Calculator.<br/>
 - Usage: `,setcalculator`
 - Slash Usage: `/setcalculator`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,setcalculator defaultsimpleembed (Hybrid Command)
Set the default state of the simple embed mode.<br/>
 - Usage: `,setcalculator defaultsimpleembed <default_simple_embed>`
 - Slash Usage: `/setcalculator defaultsimpleembed <default_simple_embed>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### default_simple_embed: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator defaultreactcalculations (Hybrid Command)
Set the default state of the react calculations.<br/>
 - Usage: `,setcalculator defaultreactcalculations <default_react_calculations>`
 - Slash Usage: `/setcalculator defaultreactcalculations <default_react_calculations>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### default_react_calculations: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setcalculator modalconfig [confirmation=False]`
 - Slash Usage: `/setcalculator modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator resultcodeblock (Hybrid Command)
Toggle the codeblock mode.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setcalculator resultcodeblock <value>`
 - Slash Usage: `/setcalculator resultcodeblock <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setcalculator resetsetting <setting>`
 - Slash Usage: `/setcalculator resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,setcalculator autocalculations (Hybrid Command)
Toggle the auto calculations.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setcalculator autocalculations <value>`
 - Slash Usage: `/setcalculator autocalculations <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator reactcalculations (Hybrid Command)
Toggle the reaction calculations.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setcalculator reactcalculations <value>`
 - Slash Usage: `/setcalculator reactcalculations <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator reactcalculationsignoredchannels (Hybrid Command)
The channels to ignore for the reaction calculations.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Union]`<br/>
 - Usage: `,setcalculator reactcalculationsignoredchannels <value>`
 - Slash Usage: `/setcalculator reactcalculationsignoredchannels <value>`
 - Checks: `server_only`


## ,setcalculator showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setcalculator showsettings [with_dev=False]`
 - Slash Usage: `/setcalculator showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator simpleembed (Hybrid Command)
Toggle the simple embed mode.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setcalculator simpleembed <value>`
 - Slash Usage: `/setcalculator simpleembed <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator defaultautocalculations (Hybrid Command)
Set the default state of the auto calculations.<br/>
 - Usage: `,setcalculator defaultautocalculations <default_auto_calculations>`
 - Slash Usage: `/setcalculator defaultautocalculations <default_auto_calculations>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### default_auto_calculations: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator defaultresultcodeblock (Hybrid Command)
Set the default state of the result codeblock mode.<br/>
 - Usage: `,setcalculator defaultresultcodeblock <default_result_codeblock>`
 - Slash Usage: `/setcalculator defaultresultcodeblock <default_result_codeblock>`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### default_result_codeblock: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setcalculator autocalculationsignoredchannels (Hybrid Command)
The channels to ignore for the auto calculations.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Union]`<br/>
 - Usage: `,setcalculator autocalculationsignoredchannels <value>`
 - Slash Usage: `/setcalculator autocalculationsignoredchannels <value>`
 - Checks: `server_only`


