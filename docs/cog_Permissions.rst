Permissions
===========

Customize permissions for commands and cogs.

# <@1275521742961508432>permissions (Hybrid Command)
Command permission management tools.<br/>
 - Usage: `<@1275521742961508432>permissions`
 - Slash Usage: `/permissions`


## <@1275521742961508432>permissions addserverrule (Hybrid Command)
Add a rule to a command in this server.<br/>

`<allow_or_deny>` should be one of "allow" or "deny".<br/>

`<cog_or_command>` is the cog or command to add the rule to.<br/>
This is case sensitive.<br/>

`<who_or_what>` is a comma-separated list of users, channels, or roles the rule is for.<br/>
 - Usage: `<@1275521742961508432>permissions addserverrule <allow_or_deny> <cog_or_command> <who_or_what>`
 - Slash Usage: `/permissions addserverrule <allow_or_deny> <cog_or_command> <who_or_what>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `addserverrule`
 - Checks: `server_only`


## <@1275521742961508432>permissions setdefaultglobalrule (Hybrid Command)
Set the default global rule for a command.<br/>

This is the rule a command will default to when no other rule<br/>
is found.<br/>

`<allow_or_deny>` should be one of "allow", "deny" or "clear".<br/>
"clear" will reset the default rule.<br/>

`<cog_or_command>` is the cog or command to set the default<br/>
rule for. This is case sensitive.<br/>
 - Usage: `<@1275521742961508432>permissions setdefaultglobalrule <allow_or_deny> <cog_or_command>`
 - Slash Usage: `/permissions setdefaultglobalrule <allow_or_deny> <cog_or_command>`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>permissions clearserverrules (Hybrid Command)
Reset all rules in this server.<br/>
 - Usage: `<@1275521742961508432>permissions clearserverrules`
 - Slash Usage: `/permissions clearserverrules`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `clearserverrules`
 - Checks: `server_only`


## <@1275521742961508432>permissions setdefaultserverrule (Hybrid Command)
Set the default rule for a command in this server.<br/>

This is the rule a command will default to when no other rule<br/>
is found.<br/>

`<allow_or_deny>` should be one of "allow", "deny" or "clear".<br/>
"clear" will reset the default rule.<br/>

`<cog_or_command>` is the cog or command to set the default<br/>
rule for. This is case sensitive.<br/>
 - Usage: `<@1275521742961508432>permissions setdefaultserverrule <allow_or_deny> <cog_or_command>`
 - Slash Usage: `/permissions setdefaultserverrule <allow_or_deny> <cog_or_command>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `setdefaultserverrule`
 - Checks: `server_only`


## <@1275521742961508432>permissions addglobalrule (Hybrid Command)
Add a global rule to a command.<br/>

`<allow_or_deny>` should be one of "allow" or "deny".<br/>

`<cog_or_command>` is the cog or command to add the rule to.<br/>
This is case sensitive.<br/>

`<who_or_what>` is a comma-separated list of users, channels, or roles the rule is for.<br/>
 - Usage: `<@1275521742961508432>permissions addglobalrule <allow_or_deny> <cog_or_command> <who_or_what>`
 - Slash Usage: `/permissions addglobalrule <allow_or_deny> <cog_or_command> <who_or_what>`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>permissions canrun (Hybrid Command)
Check if a user can run a command.<br/>

This will take the current context into account, such as the<br/>
server and text channel.<br/>
 - Usage: `<@1275521742961508432>permissions canrun <user> <command>`
 - Slash Usage: `/permissions canrun <user> <command>`
Extended Arg Info
> ### user: discord.member.Member
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
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>permissions removeglobalrule (Hybrid Command)
Remove a global rule from a command.<br/>

`<cog_or_command>` is the cog or command to remove the rule<br/>
from. This is case sensitive.<br/>

`<who_or_what>` is a comma-separated list of users, channels, or roles the rule is for.<br/>
 - Usage: `<@1275521742961508432>permissions removeglobalrule <cog_or_command> <who_or_what>`
 - Slash Usage: `/permissions removeglobalrule <cog_or_command> <who_or_what>`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>permissions clearglobalrules (Hybrid Command)
Reset all global rules.<br/>
 - Usage: `<@1275521742961508432>permissions clearglobalrules`
 - Slash Usage: `/permissions clearglobalrules`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>permissions removeserverrule (Hybrid Command)
Remove a server rule from a command.<br/>

`<cog_or_command>` is the cog or command to remove the rule<br/>
from. This is case sensitive.<br/>

`<who_or_what>` is a comma-separated list of users, channels, or roles the rule is for.<br/>
 - Usage: `<@1275521742961508432>permissions removeserverrule <cog_or_command> <who_or_what>`
 - Slash Usage: `/permissions removeserverrule <cog_or_command> <who_or_what>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `removeserverrule`
 - Checks: `server_only`


## <@1275521742961508432>permissions explain (Hybrid Command)
Explain how permissions work.<br/>
 - Usage: `<@1275521742961508432>permissions explain`
 - Slash Usage: `/permissions explain`


# <@1275521742961508432>acl (Hybrid Command)
Manage permissions with YAML files.<br/>
 - Usage: `<@1275521742961508432>acl`
 - Slash Usage: `/acl`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `yaml`


## <@1275521742961508432>acl yamlexample (Hybrid Command)
Sends an example of the yaml layout for permissions<br/>
 - Usage: `<@1275521742961508432>acl yamlexample`
 - Slash Usage: `/acl yamlexample`


## <@1275521742961508432>acl updateserver (Hybrid Command)
Update rules for this server with a YAML file.<br/>

This won't touch any rules not specified in the YAML<br/>
file.<br/>
 - Usage: `<@1275521742961508432>acl updateserver`
 - Slash Usage: `/acl updateserver`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `updateserver`
 - Checks: `server_only`


## <@1275521742961508432>acl getglobal (Hybrid Command)
Get a YAML file detailing all global rules.<br/>
 - Usage: `<@1275521742961508432>acl getglobal`
 - Slash Usage: `/acl getglobal`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>acl setglobal (Hybrid Command)
Set global rules with a YAML file.<br/>

**WARNING**: This will override reset *all* global rules<br/>
to the rules specified in the uploaded file.<br/>

This does not validate the names of commands and cogs before<br/>
setting the new rules.<br/>
 - Usage: `<@1275521742961508432>acl setglobal`
 - Slash Usage: `/acl setglobal`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>acl updateglobal (Hybrid Command)
Update global rules with a YAML file.<br/>

This won't touch any rules not specified in the YAML<br/>
file.<br/>
 - Usage: `<@1275521742961508432>acl updateglobal`
 - Slash Usage: `/acl updateglobal`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>acl getserver (Hybrid Command)
Get a YAML file detailing all rules in this server.<br/>
 - Usage: `<@1275521742961508432>acl getserver`
 - Slash Usage: `/acl getserver`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `getserver`
 - Checks: `server_only`


## <@1275521742961508432>acl setserver (Hybrid Command)
Set rules for this server with a YAML file.<br/>

**WARNING**: This will override reset *all* rules in this<br/>
server to the rules specified in the uploaded file.<br/>
 - Usage: `<@1275521742961508432>acl setserver`
 - Slash Usage: `/acl setserver`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `setserver`
 - Checks: `server_only`


