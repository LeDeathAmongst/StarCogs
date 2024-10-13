OnConnect
=========

This cog is used to send shard events.

# ,connectset
Settings for shard event logging.<br/>
 - Usage: `,connectset`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


## ,connectset emoji
Settings to change default emoji.<br/>

NOTE: If you want to set custom emojis, your bot needs to share the same server<br/>
as the custom emoji.<br/>
 - Usage: `,connectset emoji`
 - Aliases: `emojis`


### ,connectset emoji orange
Change the orange emoji to your own.<br/>

**Example:**<br/>
- `,connectset emoji orange :orange_heart:`<br/>
This will change the orange emoji to :orange_heart:.<br/>

**Arguments:**<br/>
- `[emoji]` - Is where you set the emoji. Leave it blank to reset.<br/>
 - Usage: `,connectset emoji orange [emoji]`


### ,connectset emoji red
Change the red emoji to your own.<br/>

**Example:**<br/>
- `,connectset emoji red :heart:`<br/>
This will change the red emoji to :heart:.<br/>

**Arguments:**<br/>
- `[emoji]` - Is where you set the emoji. Leave it blank to reset.<br/>
 - Usage: `,connectset emoji red [emoji]`


### ,connectset emoji green
Change the green emoji to your own.<br/>

**Example:**<br/>
- `,connectset emoji green :green_heart:`<br/>
This will change the green emoji to :green_heart:.<br/>

**Arguments:**<br/>
- `[emoji]` - Is where you set the emoji. Leave it blank to reset.<br/>
 - Usage: `,connectset emoji green [emoji]`


## ,connectset version
Shows the cog version.<br/>
 - Usage: `,connectset version`


## ,connectset showsettings
Shows the current settings for OnConnect.<br/>
 - Usage: `,connectset showsettings`
 - Aliases: `settings`


## ,connectset channel
Set the channel to log shard events to.<br/>

**Example:**<br/>
- `,connectset channel #general`<br/>
This will set the event channel to general.<br/>

**Arguments:**<br/>
- `[channel]` - Is where you set the event channel. Leave it blank to disable.<br/>
 - Usage: `,connectset channel [channel]`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


