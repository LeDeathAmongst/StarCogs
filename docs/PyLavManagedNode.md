Configure the managed Lavalink node used by PyLav

# ,plmanaged
Configure the managed Lavalink node used by PyLav<br/>
 - Usage: `,plmanaged`
 - Restricted to: `BOT_OWNER`
## ,plmanaged toggle
Toggle the managed node on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `,plmanaged toggle`
## ,plmanaged update
Update the managed Lavalink node<br/>
 - Usage: `,plmanaged update [update=0]`
Extended Arg Info
> ### update: int = 0
> ```
> A number without decimal places.
> ```
## ,plmanaged heapsize
Set the managed Lavalink node maximum heap-size.<br/>

By default, this value is 2G of available RAM in the host machine represented by (65-1023M|1+G) (256M,<br/>
256G for example)<br/>

This value only represents the maximum amount of RAM allowed to be used at any given point, and does not mean<br/>
that the managed Lavalink node will always use this amount of RAM.<br/>
 - Usage: `,plmanaged heapsize <size>`
 - Aliases: `hs, ram, and memory`
Extended Arg Info
> ### size: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,plmanaged updates
Toggle the managed node auto updates on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `,plmanaged updates`
## ,plmanaged Settings
Change the managed node start up configs<br/>
 - Usage: `,plmanaged Settings`
 - Aliases: `config and set`
### ,plmanaged Settings source
Toggle the managed node sources<br/>
 - Usage: `,plmanaged Settings source <source> <state>`
Extended Arg Info
> ### source: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,plmanaged Settings host
Set the managed node host<br/>
 - Usage: `,plmanaged Settings host <host>`
Extended Arg Info
> ### host: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,plmanaged Settings filter
Toggle the managed node filters<br/>
 - Usage: `,plmanaged Settings filter <filter_name> <state>`
Extended Arg Info
> ### filter_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,plmanaged Settings iprotation
Configure Lavalink IP Rotation for rate limits.<br/>

Run `,plmanaged settings iprotation 1` to remove the ip rotation<br/>
 - Usage: `,plmanaged Settings iprotation [reset]`
 - Aliases: `ir`
Extended Arg Info
> ### reset: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,plmanaged Settings plugins
Change the managed node plugins<br/>
 - Usage: `,plmanaged Settings plugins`
#### ,plmanaged Settings plugins enable
Enable one of the available plugins<br/>
 - Usage: `,plmanaged Settings plugins enable <plugin>`
Extended Arg Info
> ### plugin: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### ,plmanaged Settings plugins update
Update the managed node plugins<br/>
 - Usage: `,plmanaged Settings plugins update`
#### ,plmanaged Settings plugins disable
Disabled one of the available plugins<br/>
 - Usage: `,plmanaged Settings plugins disable <plugin>`
Extended Arg Info
> ### plugin: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,plmanaged Settings server
Configure multiple settings for the managed node.<br/>

Run `,plmanaged settings server <setting> info` to show info about the settings and what they do.<br/>

**Setting names**:<br/>
`bufferDurationMs` : Integer i.e 400 (Default 400) - Set to 0 to disable JDA-NAS<br/>
`frameBufferDurationMs` : Integer i.e 1000 (Default 1000)<br/>
`trackStuckThresholdMs` : Integer i.e 1000 (Default 1000)<br/>
`youtubePlaylistLoadLimit` : Integer i.e 1000 (Default 1000)<br/>
`opusEncodingQuality` : Integer i.e 10 (Default 10)<br/>
`resamplingQuality` : String i.e LOW (Default HIGH)<br/>
`useSeekGhosting` : Boolean i.e True (Default True)<br/>
`playerUpdateInterval` : Integer i.e 30 (Default 30)<br/>
`youtubeSearchEnabled` : Boolean i.e True (Default True)<br/>
`soundcloudSearchEnabled` : Boolean i.e True (Default True)<br/>
 - Usage: `,plmanaged Settings server <setting> <value>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,plmanaged Settings httpproxy
Configure a HTTP proxy for Lavalink<br/>

Run `,plmanaged settings httpproxy 1` to remove the proxy.<br/>
 - Usage: `,plmanaged Settings httpproxy [reset]`
 - Aliases: `hp`
Extended Arg Info
> ### reset: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,plmanaged Settings port
`Dangerous command` Set the managed Lavalink node connection port.<br/>

This port is the port the managed Lavalink node binds to, you should only change this if there is a<br/>
conflict with the default port because you already have an application using port 2154 on this device.<br/>

The value by default is `2154`.<br/>
 - Usage: `,plmanaged Settings port <port>`
Extended Arg Info
> ### port: int
> ```
> A number without decimal places.
> ```
## ,plmanaged version
Show the version of the Cog and PyLav<br/>
 - Usage: `,plmanaged version`
