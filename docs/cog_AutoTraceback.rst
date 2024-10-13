AutoTraceback
=============

A cog to display the error traceback of a command automatically after the error!

<<<<<<< HEAD
# <@1275521742961508432>traceback (Hybrid Command)
=======
# ,traceback (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Sends to the owner the last command exception that has occurred.<br/>

If public (yes is specified), it will be sent to the chat instead.<br/>

Warning: Sending the traceback publicly can accidentally reveal sensitive information about your computer or configuration.<br/>

**Examples:**<br/>
<<<<<<< HEAD
    - `<@1275521742961508432>traceback` - Sends the traceback to your DMs.<br/>
    - `<@1275521742961508432>traceback True` - Sends the last traceback in the current context.<br/>
=======
    - `,traceback` - Sends the traceback to your DMs.<br/>
    - `,traceback True` - Sends the last traceback in the current context.<br/>
>>>>>>> 9e308722 (Revamped and Fixed)

**Arguments:**<br/>
    - `[public]` - Whether to send the traceback to the current context. Default is `True`.<br/>
    - `[index]`  - The error index. `0` is the last one.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>traceback [public=True] [index=0]`
=======
 - Usage: `,traceback [public=True] [index=0]`
>>>>>>> 9e308722 (Revamped and Fixed)
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


