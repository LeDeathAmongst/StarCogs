Prefix
======

Prefix management.

# ,prefix
Manage server prefixes.<br/>

Running this command without subcommands will show this server's prefixes.<br/>

**Example:**<br/>
`,prefix`<br/>
 - Usage: `,prefix`
 - Checks: `server_only`


## ,prefix set
Set the prefixes for this server.<br/>

Multiple prefixes can be set at once.<br/>
To add a prefix with spaces, use quotes.<br/>
This will overwrite any current prefixes.<br/>

**Examples:**<br/>
`,prefix set ! n!`<br/>
`,prefix set .. & "Hey siri, "`<br/>
 - Usage: `,prefix set <prefixes>`
 - Restricted to: `ADMIN`
 - Aliases: `=`


## ,prefix clear
Reset this server's prefixes to the default list.<br/>

This cannot be undone.<br/>

**Example:**<br/>
`,prefix clear`<br/>
 - Usage: `,prefix clear`
 - Restricted to: `ADMIN`
 - Aliases: `reset`


## ,prefix remove
Remove a prefix from this server's prefix list.<br/>

Use quotes to remove a prefix with spaces.<br/>

**Examples:**<br/>
`,prefix remove ~`<br/>
`,prefix - "Alexa, "`<br/>
 - Usage: `,prefix remove <prefix>`
 - Restricted to: `ADMIN`
 - Aliases: `-`
Extended Arg Info
> ### prefix: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,prefix add
Add a prefix to this server's prefix list.<br/>

Use quotes to add a prefix with spaces.<br/>

**Examples:**<br/>
`,prefix add ?`<br/>
`,prefix + "Starfire, can you please "`<br/>
 - Usage: `,prefix add <prefix>`
 - Restricted to: `ADMIN`
 - Aliases: `+`


