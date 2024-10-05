AutoTraceback
=============

A cog to display the error traceback of a command automatically after the error!

# <@1275521742961508432>traceback (Hybrid Command)
Sends to the owner the last command exception that has occurred.<br/>

If public (yes is specified), it will be sent to the chat instead.<br/>

Warning: Sending the traceback publicly can accidentally reveal sensitive information about your computer or configuration.<br/>

**Examples:**<br/>
    - `<@1275521742961508432>traceback` - Sends the traceback to your DMs.<br/>
    - `<@1275521742961508432>traceback True` - Sends the last traceback in the current context.<br/>

**Arguments:**<br/>
    - `[public]` - Whether to send the traceback to the current context. Default is `True`.<br/>
    - `[index]`  - The error index. `0` is the last one.<br/>
 - Usage: `<@1275521742961508432>traceback [public=True] [index=0]`
 - Slash Usage: `/traceback [public=True] [index=0]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### public: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### index: int = 0
> ```
> A number without decimal places.
> ```


