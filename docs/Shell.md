Run shell commands on bot's system from Discord.

# ,shell
Run shell command.<br/>
 - Usage: `,shell <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,shellq
Run shell command quietly.<br/>

If command's exit code is 0, `,shellq` will only send a tick reaction.<br/>
Otherwise, the result will be shown as with regular `,shell` command.<br/>
 - Usage: `,shellq <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,killshells
Kill all shell processes started by Shell cog.<br/>
 - Usage: `,killshells`
 - Restricted to: `BOT_OWNER`
# ,shellset
Manage settings of the Shell cog.<br/>
 - Usage: `,shellset`
 - Restricted to: `BOT_OWNER`
## ,shellset shell
Set a replacement shell for the default ``/bin/sh``.<br/>

This needs to be a full path to the replacement shell.<br/>
The input is not validated.<br/>

Only works on POSIX systems.<br/>
 - Usage: `,shellset shell <replacement_shell>`
Extended Arg Info
> ### replacement_shell: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,shellset shell reset
Reset the replacement shell back to the default.<br/>
 - Usage: `,shellset shell reset`
