Status
======

Automatically check for status updates.

When there is one, it will send the update to all channels that
have registered to recieve updates from that service.

There's also the `status` command which anyone can use to check
updates wherever they want.

If there's a service that you want added, contact @vexingvexed or
make an issue on the GitHub repo (or even better a PR!).

# ,statusset
Get automatic status updates in a channel, eg Discord.<br/>

Get started with `,statusset preview` to see what they look like,<br/>
then `,statusset add` to set up automatic updates.<br/>
 - Usage: `,statusset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,statusset preview
Preview what status updates will look like.<br/>

You can also see this at https://go.vexcodes.com/c/statusref<br/>

**<service>**<br/>

    The service you want to preview. There's a list of available services in the<br/>
    `,help statusset` command.<br/>

**<mode>**<br/>

    **all**: Every time the service posts an update on an incident, I will send<br/>
    a new message containing the previous updates as well as the new update. Best<br/>
    used in a fast-moving channel with other users.<br/>

    **latest**: Every time the service posts an update on an incident, I will send<br/>
    a new message containing only the latest update. Best used in a dedicated status<br/>
    channel.<br/>

    **edit**: Naturally, edit mode can't have a preview so won't work with this command.<br/>
    The message content is the same as the `all` mode.<br/>
    When a new incident is created, I will sent a new message. When this<br/>
    incident is updated, I will then add the update to the original message. Best<br/>
    used in a dedicated status channel.<br/>

**<webhook>**<br/>

    Using a webhook means that the status updates will be sent with the avatar<br/>
    as the service's logo and the name will be `[service] Status Update`, instead<br/>
    of my avatar and name.<br/>

**Examples:**<br/>
- `,statusset preview discord all true`<br/>
- `,statusset preview discord latest false`<br/>
 - Usage: `,statusset preview <service> <mode> <webhook>`
Extended Arg Info
> ### webhook: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,statusset clear
Remove all feeds from a channel.<br/>

If you don't specify a channel, I will use the current channel<br/>

**Examples:**<br/>
- `,statusset clear #testing`<br/>
- `,statusset clear` (for using current channel)<br/>
 - Usage: `,statusset clear <chan>`
 - Aliases: `erase`
Extended Arg Info
> ### chan: Union[discord.channel.TextChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,statusset edit
Edit services you've already set up.<br/>
 - Usage: `,statusset edit`


### ,statusset edit mode
Change what mode to use for status updates.<br/>

**All**: Every time the service posts an update on an incident, I will send a new message<br/>
containing the previous updates as well as the new update. Best used in a fast-moving<br/>
channel with other users.<br/>

**Latest**: Every time the service posts an update on an incident, I will send a new<br/>
message containing only the latest update. Best used in a dedicated status channel.<br/>

**Edit**: When a new incident is created, I will sent a new message. When this incident is<br/>
updated, I will then add the update to the original message. Best used in a dedicated<br/>
status channel.<br/>

If you don't specify a channel, I will use the current channel.<br/>

**Examples:**<br/>
- `,statusset edit mode #testing discord latest`<br/>
- `,statusset edit mode discord edit` (for current channel)<br/>
 - Usage: `,statusset edit mode <chan> <service> <mode>`
Extended Arg Info
> ### chan: Union[discord.channel.TextChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### ,statusset edit restrict
Restrict access to the service in the `status` command.<br/>

Enabling this will reduce spam. Instead of sending the whole update<br/>
(if there's an incident) members will instead be redirected to channels<br/>
that automatically receive the status updates, that they have permission to to view.<br/>

**Examples:**<br/>
- `,statusset edit restrict #testing discord true`<br/>
- `,statusset edit restrict discord false` (for current channel)<br/>
 - Usage: `,statusset edit restrict <chan> <service> <restrict>`
Extended Arg Info
> ### chan: Union[discord.channel.TextChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### restrict: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### ,statusset edit webhook
Set whether or not to use webhooks for status updates.<br/>

Using a webhook means that the status updates will be sent with the avatar as the service's<br/>
logo and the name will be `[service] Status Update`, instead of my avatar and name.<br/>

If you don't specify a channel, I will use the current channel.<br/>

**Examples:**<br/>
- `,statusset edit webhook #testing discord true`<br/>
- `,statusset edit webhook discord false` (for current channel)<br/>
 - Usage: `,statusset edit webhook <chan> <service> <webhook>`
Extended Arg Info
> ### chan: Union[discord.channel.TextChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### webhook: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,statusset add
Start getting status updates for the chosen service!<br/>

There is a list of services you can use in the `,statusset list` command.<br/>

This is an interactive command. It will ask what mode you want to use and if you<br/>
want to use a webhook. You can use the `,statusset preview` command to see how<br/>
different options look or take a look at<br/>
https://go.vexcodes.com/c/statusref<br/>

If you don't specify a specific channel, I will use the current channel.<br/>
 - Usage: `,statusset add <service> <chan>`
Extended Arg Info
> ### chan: Union[discord.channel.TextChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,statusset remove
Stop status updates for a specific service in this server.<br/>

If you don't specify a channel, I will use the current channel.<br/>

**Examples:**<br/>
- `,statusset remove discord #testing`<br/>
- `,statusset remove discord` (for using current channel)<br/>
 - Usage: `,statusset remove <service> [chan=None]`
 - Aliases: `del and delete`
Extended Arg Info
> ### chan: Union[discord.channel.TextChannel, discord.threads.Thread, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,statusset list
List that available services and ones are used in this server.<br/>

Optionally add a service at the end of the command to view detailed settings for that<br/>
service.<br/>

**Examples:**<br/>
- `,statusset list discord`<br/>
- `,statusset list`<br/>
 - Usage: `,statusset list <service>`
 - Aliases: `show and settings`


# ,statusdev
Don't use this; hidden for a reason; stuff _might_ break.<br/>
 - Usage: `,statusdev`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


## ,statusdev devenvvars
Add some dev env vars<br/>

Adds `status`, `loop`, `statusapi`, `sendupdate`.<br/>

These will be removed on cog unload.<br/>
 - Usage: `,statusdev devenvvars`
 - Aliases: `dev`


## ,statusdev checkfeedraw
Get raw JSON data<br/>
 - Usage: `,statusdev checkfeedraw <service>`
 - Aliases: `cfr`


## ,statusdev forcestatus
Simulate latest incident. SENDS TO ALL CHANNELS IN ALL REGISTERED GUILDS.<br/>
 - Usage: `,statusdev forcestatus <service>`
 - Aliases: `fs`


## ,statusdev refreshincidentids
Regenerate the cache of past incident IDs.<br/>
 - Usage: `,statusdev refreshincidentids`
 - Aliases: `ri`


## ,statusdev checkusedfeedcache
Check what feeds this is checking<br/>
 - Usage: `,statusdev checkusedfeedcache`
 - Aliases: `cfc`


## ,statusdev checkserverrestrictions
Check server restrictins for current server<br/>
 - Usage: `,statusdev checkserverrestrictions`
 - Aliases: `cgr`


## ,statusdev loopstatus
Check status of the loop<br/>
 - Usage: `,statusdev loopstatus`
 - Aliases: `l`


## ,statusdev cooldown
Get custom cooldown info for a user<br/>
 - Usage: `,statusdev cooldown [user_id=None]`
 - Aliases: `cd`
Extended Arg Info
> ### user_id: Optional[int] = None
> ```
> A number without decimal places.
> ```


## ,statusdev clearchannels
Clear channels from Config that no longer exists.<br/>
 - Usage: `,statusdev clearchannels`
 - Aliases: `cl`


## ,statusdev checkfeed
Check the current status of a feed in the current channel<br/>
 - Usage: `,statusdev checkfeed <service> [mode=all] [webhook=False]`
 - Aliases: `cf`
Extended Arg Info
> ### webhook: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,statusdev checkid

 - Usage: `,statusdev checkid <service> <id>`
 - Aliases: `cid`
Extended Arg Info
> ### id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# ,status
Check for the status of a variety of services, eg Discord.<br/>

**Example:**<br/>
- `,status discord`<br/>
 - Usage: `,status <service>`
 - Cooldown: `2 per 10.0 seconds`
 - Checks: `server_only`


# ,statusinfo

 - Usage: `,statusinfo`


