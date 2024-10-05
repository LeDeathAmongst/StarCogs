RoleRequests
============

Adds or removes a role on users by request.

# <@1275521742961508432>request
Requests access to a role.<br/>
 - Usage: `<@1275521742961508432>request <role_name>`
 - Aliases: `iam and req`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>request addrole
Adds a role to be requestable.<br/>
 - Usage: `<@1275521742961508432>request addrole <role_name>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>request rem
Takes a requestable role.<br/>
 - Usage: `<@1275521742961508432>request rem <role_name>`
 - Aliases: `remove`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>request list
Lists the roles that can be requested.<br/>
 - Usage: `<@1275521742961508432>request list`
 - Checks: `server_only`


## <@1275521742961508432>request remrole
Removes a role from being requestable.<br/>
 - Usage: `<@1275521742961508432>request remrole <role_name>`
 - Restricted to: `MOD`
 - Aliases: `removerole`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>request clear
Clears all requestable roles.<br/>
 - Usage: `<@1275521742961508432>request clear`
 - Aliases: `clr`
 - Checks: `server_only`


## <@1275521742961508432>request postlist
Lists the roles that can be requested and posts them permanently to the specified channel.<br/>
 - Usage: `<@1275521742961508432>request postlist <channel>`
 - Restricted to: `MOD`
 - Aliases: `post_list`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>request massadd
Adds roles to all users who have participated in a channel within the last X messages.<br/>
 - Usage: `<@1275521742961508432>request massadd [limit=1000] [channel=None] <role_name>`
 - Restricted to: `MOD`
 - Aliases: `massapplyrole and massapply`
 - Checks: `server_only`
Extended Arg Info
> ### limit: int = 1000
> ```
> A number without decimal places.
> ```
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>request add
Gives you a requestable role.<br/>
 - Usage: `<@1275521742961508432>request add <role_name>`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>reqset
Adjust <@1275521742961508432>request command settings.<br/>
 - Usage: `<@1275521742961508432>reqset`
 - Restricted to: `MOD`
 - Checks: `server_only`


## <@1275521742961508432>reqset auto_post_list
Whether to automatically update existing post_list posts when roles or counts change.<br/>

For value, pass in "true" or "false".<br/>
Omit the value to toggle.<br/>
 - Usage: `<@1275521742961508432>reqset auto_post_list [value=None]`
 - Restricted to: `MOD`
 - Aliases: `auto_postlist`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>reqset max_requestable
Maximum number of roles that users can request.<br/>

If set to -1, there is no limit.<br/>
 - Usage: `<@1275521742961508432>reqset max_requestable <count>`
 - Restricted to: `MOD`
 - Aliases: `max_req and max`
 - Checks: `server_only`
Extended Arg Info
> ### count: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>reqset show_member_count
Whether to show or hide the number of users who currently have the role in successful <@1275521742961508432>request commands and the role list.<br/>

For value, pass in "true" or "false".<br/>
Omit the value to toggle.<br/>
Using the aliases with "hide" at the start inverts the value passed in.<br/>
 - Usage: `<@1275521742961508432>reqset show_member_count [value=None]`
 - Restricted to: `MOD`
 - Aliases: `hide_member_count, show_stats, and hide_stats`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>reqset request_channel
Where `<@1275521742961508432>request list` commands say to use the `<@1275521742961508432>request` command. Use the command without a channel argument to set to no channel.<br/>
 - Usage: `<@1275521742961508432>reqset request_channel [channel=None]`
 - Restricted to: `MOD`
 - Aliases: `req_channel and channel`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


