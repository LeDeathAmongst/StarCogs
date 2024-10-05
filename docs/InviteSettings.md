Manage invites.

# <@1275521742961508432>invite
Show all set invites or manage invite links.<br/>
 - Usage: `<@1275521742961508432>invite`
## <@1275521742961508432>invite set
Set invite links, names, and embed color.<br/>
 - Usage: `<@1275521742961508432>invite set`
 - Restricted to: `BOT_OWNER`
### <@1275521742961508432>invite set invite
Set an invite link.<br/>

**Arguments**<br/>
    - `invite_type`: The type of invite (e.g., main, admin, support).<br/>
    - `name`: The display name for the invite.<br/>
    - `invite_link`: The invite link.<br/>
 - Usage: `<@1275521742961508432>invite set invite <invite_type> <name> <invite_link>`
Extended Arg Info
> ### invite_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### invite_link: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>invite set fieldname
Set the field name for an invite type.<br/>

**Arguments**<br/>
    - `invite_type`: The type of invite (e.g., main, admin, support).<br/>
    - `field_name`: The field name to display in the embed.<br/>
 - Usage: `<@1275521742961508432>invite set fieldname <invite_type> <field_name>`
Extended Arg Info
> ### invite_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>invite set color
Set the embed color.<br/>

**Arguments**<br/>
    - `color`: The color for the embed.<br/>
 - Usage: `<@1275521742961508432>invite set color <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
# <@1275521742961508432>support
Send an embed with a support server invite link button.<br/>
 - Usage: `<@1275521742961508432>support`
