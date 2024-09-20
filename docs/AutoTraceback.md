# AutoTraceback Help

### traceback

**Description:** Sends to the owner the last command exception that has occurred.

If public (yes is specified), it will be sent to the chat instead.

Warning: Sending the traceback publicly can accidentally reveal sensitive information about your computer or configuration.

**Examples:**
    - `[p]traceback` - Sends the traceback to your DMs.
    - `[p]traceback True` - Sends the last traceback in the current context.

**Arguments:**
    - `[public]` - Whether to send the traceback to the current context. Default is `True`.
    - `[index]`  - The error index. `0` is the last one.

**Usage:** `<@1275521742961508432>traceback`

