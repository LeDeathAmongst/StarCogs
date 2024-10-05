OwnerProtection
===============

A cog to protect the bot owner/trusted owners from being muted, timed out, kicked, or banned.

# <@1275521742961508432>owner
Group command for owner protection settings.<br/>
 - Usage: `<@1275521742961508432>owner`
 - Checks: `server_only`


## <@1275521742961508432>owner remove
Remove a user from the protected owners list.<br/>
 - Usage: `<@1275521742961508432>owner remove <owner>`
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


## <@1275521742961508432>owner give
Give the support role to the command invoker if it exists.<br/>
 - Usage: `<@1275521742961508432>owner give`
 - Checks: `OwnerProtection`


## <@1275521742961508432>owner setrole
Set the name of the support role.<br/>
 - Usage: `<@1275521742961508432>owner setrole <name>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>owner modalconfig
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `<@1275521742961508432>owner modalconfig [confirmation=False]`
 - Aliases: `configmodal`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>owner admin
Toggle admin permissions for the support role.<br/>
 - Usage: `<@1275521742961508432>owner admin`
 - Checks: `OwnerProtection`


## <@1275521742961508432>owner ownerrolename
The name of the owner role.<br/>

Default value: `...`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `<@1275521742961508432>owner ownerrolename <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>owner supportrolemessage
Message sent when the support role is created.<br/>

Default value: `Support role created successfully.`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `<@1275521742961508432>owner supportrolemessage <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>owner add
Add a user to the protected owners list.<br/>
 - Usage: `<@1275521742961508432>owner add <owner>`
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


## <@1275521742961508432>owner showsettings
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>owner showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>owner ownermessage
Message sent to the server owner when the support role is created.<br/>

Default value: `Hello {owner_name},<br/>

I have created a role called '{role_name}' in {server_name} for bot support purposes. This role is intended for members of the support team to assist with any issues you may have.`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `<@1275521742961508432>owner ownermessage <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>owner create
Create the support role with specified permissions.<br/>
 - Usage: `<@1275521742961508432>owner create [name=None] [message=None]`
 - Checks: `OwnerProtection`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>owner setmessage
Set the message to be sent when the support role is created.<br/>
 - Usage: `<@1275521742961508432>owner setmessage <message>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>owner resetsetting
Reset a setting.<br/>
 - Usage: `<@1275521742961508432>owner resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>owner list
List all protected owners.<br/>
 - Usage: `<@1275521742961508432>owner list`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>owner delete
Delete the support role.<br/>
 - Usage: `<@1275521742961508432>owner delete`
 - Checks: `OwnerProtection`


