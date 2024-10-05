TellMe
======

Create custom commands with DMs and server messages.

# <@1275521742961508432>tellme
Run a command.<br/>
 - Usage: `<@1275521742961508432>tellme <command_name>`
 - Checks: `server_only`
Extended Arg Info
> ### command_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>tellme create
Create a new command.<br/>
 - Usage: `<@1275521742961508432>tellme create <command_name>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>tellme server
Set the message to be sent in the server.<br/>

If nothing is passed, it will remove the server message.<br/>
 - Usage: `<@1275521742961508432>tellme server <command_name> [text]`
Extended Arg Info
> ### command_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>tellme delete
Delete a command.<br/>
 - Usage: `<@1275521742961508432>tellme delete <command_name>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>tellme dm
Set the message to be sent in dms.<br/>

If nothing is passed, it will remove the dm message.<br/>
 - Usage: `<@1275521742961508432>tellme dm <command_name> [text]`
Extended Arg Info
> ### command_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>tellme list
List commands created with tellme.<br/>
 - Usage: `<@1275521742961508432>tellme list`


