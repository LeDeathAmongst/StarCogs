# Permissions Help

### permissions

**Description:** Command permission management tools.

**Usage:** `<@1275521742961508432>permissions`

### permissions explain

**Description:** Explain how permissions works.

**Usage:** `<@1275521742961508432>permissions explain`

### permissions setdefaultglobalrule

**Description:** Set the default global rule for a command.

This is the rule a command will default to when no other rule
is found.

`<allow_or_deny>` should be one of "allow", "deny" or "clear".
"clear" will reset the default rule.

`<cog_or_command>` is the cog or command to set the default
rule for. This is case sensitive.

**Usage:** `<@1275521742961508432>permissions setdefaultglobalrule`

### permissions clearglobalrules

**Description:** Reset all global rules.

**Usage:** `<@1275521742961508432>permissions clearglobalrules`

### permissions clearserverrules

**Description:** Reset all rules in this server.

**Usage:** `<@1275521742961508432>permissions clearserverrules`

### permissions addserverrule

**Description:** Add a rule to a command in this server.

`<allow_or_deny>` should be one of "allow" or "deny".

`<cog_or_command>` is the cog or command to add the rule to.
This is case sensitive.

`<who_or_what...>` is one or more users, channels or roles the rule is for.

**Usage:** `<@1275521742961508432>permissions addserverrule`

### permissions removeserverrule

**Description:** Remove a server rule from a command.

`<cog_or_command>` is the cog or command to remove the rule
from. This is case sensitive.

`<who_or_what...>` is one or more users, channels or roles the rule is for.

**Usage:** `<@1275521742961508432>permissions removeserverrule`

### permissions addglobalrule

**Description:** Add a global rule to a command.

`<allow_or_deny>` should be one of "allow" or "deny".

`<cog_or_command>` is the cog or command to add the rule to.
This is case sensitive.

`<who_or_what...>` is one or more users, channels or roles the rule is for.

**Usage:** `<@1275521742961508432>permissions addglobalrule`

### permissions canrun

**Description:** Check if a user can run a command.

This will take the current context into account, such as the
server and text channel.

**Usage:** `<@1275521742961508432>permissions canrun`

### permissions setdefaultserverrule

**Description:** Set the default rule for a command in this server.

This is the rule a command will default to when no other rule
is found.

`<allow_or_deny>` should be one of "allow", "deny" or "clear".
"clear" will reset the default rule.

`<cog_or_command>` is the cog or command to set the default
rule for. This is case sensitive.

**Usage:** `<@1275521742961508432>permissions setdefaultserverrule`

### permissions removeglobalrule

**Description:** Remove a global rule from a command.

`<cog_or_command>` is the cog or command to remove the rule
from. This is case sensitive.

`<who_or_what...>` is one or more users, channels or roles the rule is for.

**Usage:** `<@1275521742961508432>permissions removeglobalrule`

### permissions acl

**Description:** Manage permissions with YAML files.

**Usage:** `<@1275521742961508432>permissions acl`

### permissions acl yamlexample

**Description:** Sends an example of the yaml layout for permissions

**Usage:** `<@1275521742961508432>permissions acl yamlexample`

### permissions acl setglobal

**Description:** Set global rules with a YAML file.

**WARNING**: This will override reset *all* global rules
to the rules specified in the uploaded file.

This does not validate the names of commands and cogs before
setting the new rules.

**Usage:** `<@1275521742961508432>permissions acl setglobal`

### permissions acl setserver

**Description:** Set rules for this server with a YAML file.

**WARNING**: This will override reset *all* rules in this
server to the rules specified in the uploaded file.

**Usage:** `<@1275521742961508432>permissions acl setserver`

### permissions acl updateserver

**Description:** Update rules for this server with a YAML file.

This won't touch any rules not specified in the YAML
file.

**Usage:** `<@1275521742961508432>permissions acl updateserver`

### permissions acl getglobal

**Description:** Get a YAML file detailing all global rules.

**Usage:** `<@1275521742961508432>permissions acl getglobal`

### permissions acl updateglobal

**Description:** Update global rules with a YAML file.

This won't touch any rules not specified in the YAML
file.

**Usage:** `<@1275521742961508432>permissions acl updateglobal`

### permissions acl getserver

**Description:** Get a YAML file detailing all rules in this server.

**Usage:** `<@1275521742961508432>permissions acl getserver`

