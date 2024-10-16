A cog to protect the bot owner/trusted owners from being muted, timed out, kicked, or banned.

# ,owner
Group command for owner protection settings.<br/>
 - Usage: `,owner`
 - Checks: `server_only`
## ,owner resetsetting
Reset a setting.<br/>
 - Usage: `,owner resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,owner supportrolename
The name of the support role.<br/>

Default value: `Support`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,owner supportrolename <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,owner give
Give the support role to the command invoker if it exists.<br/>
 - Usage: `,owner give`
 - Restricted to: `BOT_OWNER`
## ,owner admin
Toggle admin permissions for the support role.<br/>
 - Usage: `,owner admin`
 - Restricted to: `BOT_OWNER`
## ,owner supportrolemessage
Message sent when the support role is created.<br/>

Default value: `Support Role created successfully.`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,owner supportrolemessage <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,owner delete
Delete the support role.<br/>
 - Usage: `,owner delete`
 - Restricted to: `BOT_OWNER`
## ,owner ownermessage
Message sent to the server owner when the support role is created.<br/>

Default value: `Support role made for support.`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,owner ownermessage <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,owner create
Create the support role with specified permissions.<br/>
 - Usage: `,owner create [name=None] [message=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,owner modalconfig
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,owner modalconfig [confirmation=False]`
 - Aliases: `configmodal`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,owner list
List all protected owners.<br/>
 - Usage: `,owner list`
 - Restricted to: `BOT_OWNER`
## ,owner add
Add a user to the protected owners list.<br/>
 - Usage: `,owner add <owner>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### owner: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## ,owner ownerrolename
The name of the owner role.<br/>

Default value: `...`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,owner ownerrolename <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,owner remove
Remove a user from the protected owners list.<br/>
 - Usage: `,owner remove <owner>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### owner: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## ,owner showsettings
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,owner showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
