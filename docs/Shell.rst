Shell
=====

Run shell commands on bot's system from Discord.

# <@1275521742961508432>shell
Run shell command.<br/>
 - Usage: `<@1275521742961508432>shell <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>shellq
Run shell command quietly.<br/>

If command's exit code is 0, `<@1275521742961508432>shellq` will only send a tick reaction.<br/>
Otherwise, the result will be shown as with regular `<@1275521742961508432>shell` command.<br/>
 - Usage: `<@1275521742961508432>shellq <command>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>killshells
Kill all shell processes started by Shell cog.<br/>
 - Usage: `<@1275521742961508432>killshells`
 - Restricted to: `BOT_OWNER`


# <@1275521742961508432>shellset
Manage settings of the Shell cog.<br/>
 - Usage: `<@1275521742961508432>shellset`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>shellset shell
Set a replacement shell for the default ``/bin/sh``.<br/>

This needs to be a full path to the replacement shell.<br/>
The input is not validated.<br/>

Only works on POSIX systems.<br/>
 - Usage: `<@1275521742961508432>shellset shell <replacement_shell>`
Extended Arg Info
> ### replacement_shell: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>shellset shell reset
Reset the replacement shell back to the default.<br/>
 - Usage: `<@1275521742961508432>shellset shell reset`


