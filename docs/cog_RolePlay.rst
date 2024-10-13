RolePlay
========

Set up a role play, where the author of messages are secret - the bot reposts all messages.

Admins can get started with `[p]roleplay channel`, as well as some other configuration options.

<<<<<<< HEAD
# <@1275521742961508432>roleplayinfo

 - Usage: `<@1275521742961508432>roleplayinfo`


# <@1275521742961508432>roleplay
=======
# ,roleplayinfo

 - Usage: `,roleplayinfo`


# ,roleplay
>>>>>>> 9e308722 (Revamped and Fixed)
Role play configuration.<br/>

This is a group command, so you can use it to configure the roleplay for a channel.<br/>

<<<<<<< HEAD
Get started with `<@1275521742961508432>roleplay channel`.<br/>
 - Usage: `<@1275521742961508432>roleplay`
=======
Get started with `,roleplay channel`.<br/>
 - Usage: `,roleplay`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>roleplay log
Set a channel to log role play messages to.<br/>

If you do not specify a channel logging will be disabled.<br/>

**Examples:**<br/>
- `<@1275521742961508432>roleplay log #logs` - set to a channel called logs<br/>
- `<@1275521742961508432>roleplay log` - disable logging<br/>
 - Usage: `<@1275521742961508432>roleplay log <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>roleplay radio
Enable or disable radio.<br/>

The default is disabled.<br/>

**Examples:**<br/>
- `<@1275521742961508432>roleplay radio true` - enable radio mode<br/>
- `<@1275521742961508432>roleplay radio false` - disable radio mode<br/>
 - Usage: `<@1275521742961508432>roleplay radio <radio>`
Extended Arg Info
> ### radio: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>roleplay radiotitle
Set a title for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `<@1275521742961508432>roleplay radiotitle New radio transmission detected` - the default<br/>
 - Usage: `<@1275521742961508432>roleplay radiotitle <title>`
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>roleplay radiofooter
Set a footer for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `<@1275521742961508432>roleplay radiofooter Transmission over`<br/>
- `<@1275521742961508432>roleplay radiofooter` - reset to none<br/>
 - Usage: `<@1275521742961508432>roleplay radiofooter <footer>`
Extended Arg Info
> ### footer: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>roleplay radioimage
Set an image for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `<@1275521742961508432>roleplay radioimage https://i.imgur.com/example.png`<br/>
- `<@1275521742961508432>roleplay radioimage` - reset to none<br/>
 - Usage: `<@1275521742961508432>roleplay radioimage <image_url>`
Extended Arg Info
> ### image_url: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>roleplay channel
Set the channel for the roleplay.<br/>

Leave blank to disable.<br/>

**Examples:**<br/>
- `<@1275521742961508432>roleplay channel` - disable roleplay<br/>
- `<@1275521742961508432>roleplay channel #roleplay` - set the channel to #roleplay<br/>
 - Usage: `<@1275521742961508432>roleplay channel <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## <@1275521742961508432>roleplay embed
Enable or disable embeds.<br/>

The default is disabled.<br/>

**Examples:**<br/>
- `<@1275521742961508432>roleplay embed true` - enable<br/>
- `<@1275521742961508432>roleplay embed false` - disable<br/>
 - Usage: `<@1275521742961508432>roleplay embed <embed>`
Extended Arg Info
> ### embed: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>roleplay settings
View the current settings for the roleplay.<br/>
 - Usage: `<@1275521742961508432>roleplay settings`


## <@1275521742961508432>roleplay delete
=======
## ,roleplay delete
>>>>>>> 9e308722 (Revamped and Fixed)
Automatically delete messages in the role play channel after time has passed.<br/>

The time is in minutes.<br/>

The default is disabled.<br/>

**Examples:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>roleplay delete 5` - delete after 5 mins<br/>
- `<@1275521742961508432>roleplay delete 30` - delete after 30 mins<br/>
- `<@1275521742961508432>roleplay delete` - disable deletion<br/>
 - Usage: `<@1275521742961508432>roleplay delete <delete_after>`
=======
- `,roleplay delete 5` - delete after 5 mins<br/>
- `,roleplay delete 30` - delete after 30 mins<br/>
- `,roleplay delete` - disable deletion<br/>
 - Usage: `,roleplay delete <delete_after>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### delete_after: Optional[int]
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
=======
## ,roleplay radiotitle
Set a title for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `,roleplay radiotitle New radio transmission detected` - the default<br/>
 - Usage: `,roleplay radiotitle <title>`
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,roleplay radioimage
Set an image for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `,roleplay radioimage https://i.imgur.com/example.png`<br/>
- `,roleplay radioimage` - reset to none<br/>
 - Usage: `,roleplay radioimage <image_url>`
Extended Arg Info
> ### image_url: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,roleplay radiofooter
Set a footer for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `,roleplay radiofooter Transmission over`<br/>
- `,roleplay radiofooter` - reset to none<br/>
 - Usage: `,roleplay radiofooter <footer>`
Extended Arg Info
> ### footer: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,roleplay radio
Enable or disable radio.<br/>

The default is disabled.<br/>

**Examples:**<br/>
- `,roleplay radio true` - enable radio mode<br/>
- `,roleplay radio false` - disable radio mode<br/>
 - Usage: `,roleplay radio <radio>`
Extended Arg Info
> ### radio: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,roleplay embed
Enable or disable embeds.<br/>

The default is disabled.<br/>

**Examples:**<br/>
- `,roleplay embed true` - enable<br/>
- `,roleplay embed false` - disable<br/>
 - Usage: `,roleplay embed <embed>`
Extended Arg Info
> ### embed: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,roleplay log
Set a channel to log role play messages to.<br/>

If you do not specify a channel logging will be disabled.<br/>

**Examples:**<br/>
- `,roleplay log #logs` - set to a channel called logs<br/>
- `,roleplay log` - disable logging<br/>
 - Usage: `,roleplay log <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,roleplay settings
View the current settings for the roleplay.<br/>
 - Usage: `,roleplay settings`


## ,roleplay channel
Set the channel for the roleplay.<br/>

Leave blank to disable.<br/>

**Examples:**<br/>
- `,roleplay channel` - disable roleplay<br/>
- `,roleplay channel #roleplay` - set the channel to #roleplay<br/>
 - Usage: `,roleplay channel <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


>>>>>>> 9e308722 (Revamped and Fixed)
