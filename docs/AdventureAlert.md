Alert when a dragon appears in adventure

# ,adventurealert (Hybrid Command)
Set notifications for all adventures<br/>
 - Usage: `,adventurealert`
 - Slash Usage: `/adventurealert`
## ,adventurealert settings (Hybrid Command)
Shows a list of servers you have alerts<br/>
 - Usage: `,adventurealert settings`
 - Slash Usage: `/adventurealert settings`
 - Aliases: `setting`
## ,adventurealert toggle (Hybrid Command)
Toggle adventure notifications in this server<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `,adventurealert toggle [alert_style=None]`
 - Slash Usage: `/adventurealert toggle [alert_style=None]`
 - Aliases: `user, users, remove, rem, and add`
 - Checks: `server_only`
## ,adventurealert removealluser (Hybrid Command)
Remove A specified user from adventurealert across the bot<br/>
 - Usage: `,adventurealert removealluser <user_id>`
 - Slash Usage: `/adventurealert removealluser <user_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
## ,adventurealert global (Hybrid Command)
Toggle adventure notifications in all shared servers<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `,adventurealert global [alert_style=None]`
 - Slash Usage: `/adventurealert global [alert_style=None]`
## ,adventurealert removeuser (Hybrid Command)
Remove a specific user ID from adventure alerts<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `,adventurealert removeuser <user_id> [alert_style=None]`
 - Slash Usage: `/adventurealert removeuser <user_id> [alert_style=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
## ,adventurealert role (Hybrid Command)
Add or remove a role to be pinged when a dragon appears<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `,adventurealert role [alert_style=None] <role>`
 - Slash Usage: `/adventurealert role [alert_style=None] <role>`
 - Restricted to: `MOD`
 - Aliases: `roles`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## ,adventurealert removeall (Hybrid Command)
Remove all adventurealert settings in all servers<br/>
 - Usage: `,adventurealert removeall`
 - Slash Usage: `/adventurealert removeall`
