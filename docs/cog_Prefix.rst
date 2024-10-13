Prefix
======

Prefix management.

<<<<<<< HEAD
# <@1275521742961508432>prefix
=======
# ,prefix
>>>>>>> 9e308722 (Revamped and Fixed)
Manage server prefixes.<br/>

Running this command without subcommands will show this server's prefixes.<br/>

**Example:**<br/>
<<<<<<< HEAD
`<@1275521742961508432>prefix`<br/>
 - Usage: `<@1275521742961508432>prefix`
 - Checks: `server_only`


## <@1275521742961508432>prefix set
=======
`,prefix`<br/>
 - Usage: `,prefix`
 - Checks: `server_only`


## ,prefix set
>>>>>>> 9e308722 (Revamped and Fixed)
Set the prefixes for this server.<br/>

Multiple prefixes can be set at once.<br/>
To add a prefix with spaces, use quotes.<br/>
This will overwrite any current prefixes.<br/>

**Examples:**<br/>
<<<<<<< HEAD
`<@1275521742961508432>prefix set ! n!`<br/>
`<@1275521742961508432>prefix set .. & "Hey siri, "`<br/>
 - Usage: `<@1275521742961508432>prefix set <prefixes>`
=======
`,prefix set ! n!`<br/>
`,prefix set .. & "Hey siri, "`<br/>
 - Usage: `,prefix set <prefixes>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `=`


<<<<<<< HEAD
## <@1275521742961508432>prefix remove
=======
## ,prefix clear
Reset this server's prefixes to the default list.<br/>

This cannot be undone.<br/>

**Example:**<br/>
`,prefix clear`<br/>
 - Usage: `,prefix clear`
 - Restricted to: `ADMIN`
 - Aliases: `reset`


## ,prefix remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove a prefix from this server's prefix list.<br/>

Use quotes to remove a prefix with spaces.<br/>

**Examples:**<br/>
<<<<<<< HEAD
`<@1275521742961508432>prefix remove ~`<br/>
`<@1275521742961508432>prefix - "Alexa, "`<br/>
 - Usage: `<@1275521742961508432>prefix remove <prefix>`
=======
`,prefix remove ~`<br/>
`,prefix - "Alexa, "`<br/>
 - Usage: `,prefix remove <prefix>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `-`
Extended Arg Info
> ### prefix: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>prefix clear
Reset this server's prefixes to the default list.<br/>

This cannot be undone.<br/>

**Example:**<br/>
`<@1275521742961508432>prefix clear`<br/>
 - Usage: `<@1275521742961508432>prefix clear`
 - Restricted to: `ADMIN`
 - Aliases: `reset`


## <@1275521742961508432>prefix add
=======
## ,prefix add
>>>>>>> 9e308722 (Revamped and Fixed)
Add a prefix to this server's prefix list.<br/>

Use quotes to add a prefix with spaces.<br/>

**Examples:**<br/>
<<<<<<< HEAD
`<@1275521742961508432>prefix add ?`<br/>
`<@1275521742961508432>prefix + "Starfire, can you please "`<br/>
 - Usage: `<@1275521742961508432>prefix add <prefix>`
=======
`,prefix add ?`<br/>
`,prefix + "Starfire, can you please "`<br/>
 - Usage: `,prefix add <prefix>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `+`


