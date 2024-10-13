Auto-upload files with configured extension sent by users to gist.github.com.

# ,autogistset
AutoGist settings.<br/>
 - Usage: `,autogistset`
 - Restricted to: `ADMIN`
## ,autogistset allowchannels
Allow the bot to listen to the given channels.<br/>
 - Usage: `,autogistset allowchannels <channels>`
 - Aliases: `allowchannel`
 - Checks: `server_only`
Extended Arg Info
> ### *channels: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,autogistset listoverridden
List server channels that don't use the default setting.<br/>
 - Usage: `,autogistset listoverridden`
 - Checks: `server_only`
## ,autogistset extensions
Settings for file extensions<br/>
that are required for AutoGist to upload file to Gist.<br/>

By default AutoGist will look for files with `.txt` and `.log` extensions.<br/>
 - Usage: `,autogistset extensions`
 - Aliases: `ext and exts`
 - Checks: `server_only`
### ,autogistset extensions list
List file extensions that are required for AutoGist to upload file to Gist.<br/>
 - Usage: `,autogistset extensions list`
### ,autogistset extensions remove
Remove file extensions from the list.<br/>

Example:<br/>
`,autogist extensions remove txt .log` - removes `.txt` and `.log` extensions.<br/>
 - Usage: `,autogistset extensions remove <extensions>`
 - Aliases: `delete`
Extended Arg Info
> ### *extensions: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,autogistset extensions add
Add file extensions to the list.<br/>

Example:<br/>
`,autogist extensions add txt .log` - adds `.txt` and `.log` extensions.<br/>
 - Usage: `,autogistset extensions add <extensions>`
Extended Arg Info
> ### *extensions: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,autogistset token
Instructions to set the GitHub API token.<br/>
 - Usage: `,autogistset token`
 - Restricted to: `BOT_OWNER`
## ,autogistset channeldefault
Set whether AutoGist should by default listen to channels.<br/>

If default is set to True, bot will only listen to channels it was explicitly<br/>
allowed to listen to with `,autogistset allowchannels` command.<br/>

If default is set to False, bot will listen to all channels except the ones<br/>
it was explicitly blocked from listening to<br/>
with `,autogistset denychannels` command.<br/>

By default, servers will not listen to any channel.<br/>
Use `,autogist channeldefault` without a setting to see current mode.<br/>
 - Usage: `,autogistset channeldefault [allow=None]`
 - Checks: `server_only`
Extended Arg Info
> ### allow: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,autogistset listentohumans
Make AutoGist listen to messages from humans in this server.<br/>
 - Usage: `,autogistset listentohumans [state=None]`
 - Checks: `server_only`
Extended Arg Info
> ### state: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,autogistset listentoself
Make the bot listen to messages from itself in this server.<br/>

See also: `,autogistset listentobots` command,<br/>
that makes the bot listen to other bots.<br/>
 - Usage: `,autogistset listentoself [state=None]`
 - Checks: `server_only`
Extended Arg Info
> ### state: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,autogistset listentobots
Make AutoGist listen to messages from other bots in this server.<br/>

NOTE: To make bot listen to messages from itself,<br/>
you need to use `,autogistset listentoself` command.<br/>
 - Usage: `,autogistset listentobots [state=None]`
 - Checks: `server_only`
Extended Arg Info
> ### state: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,autogistset blockchannels
Block the bot from listening to the given channels.<br/>
 - Usage: `,autogistset blockchannels <channels>`
 - Aliases: `blockchannel`
 - Checks: `server_only`
Extended Arg Info
> ### *channels: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
