PyLavManagedNode
================

Configure the managed Lavalink node used by PyLav

# <@1275521742961508432>plmanaged
Configure the managed Lavalink node used by PyLav<br/>
 - Usage: `<@1275521742961508432>plmanaged`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>plmanaged toggle
Toggle the managed node on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `<@1275521742961508432>plmanaged toggle`


## <@1275521742961508432>plmanaged updates
Toggle the managed node auto updates on/off.<br/>

Changes will be applied after I restart.<br/>
 - Usage: `<@1275521742961508432>plmanaged updates`


## <@1275521742961508432>plmanaged heapsize
Set the managed Lavalink node maximum heap-size.<br/>

By default, this value is 2G of available RAM in the host machine represented by (65-1023M|1+G) (256M,<br/>
256G for example)<br/>

This value only represents the maximum amount of RAM allowed to be used at any given point, and does not mean<br/>
that the managed Lavalink node will always use this amount of RAM.<br/>
 - Usage: `<@1275521742961508432>plmanaged heapsize <size>`
 - Aliases: `hs, ram, and memory`
Extended Arg Info
> ### size: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>plmanaged Settings
Change the managed node start up configs<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings`
 - Aliases: `config and set`


### <@1275521742961508432>plmanaged Settings port
`Dangerous command` Set the managed Lavalink node connection port.<br/>

This port is the port the managed Lavalink node binds to, you should only change this if there is a<br/>
conflict with the default port because you already have an application using port 2154 on this device.<br/>

The value by default is `2154`.<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings port <port>`
Extended Arg Info
> ### port: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>plmanaged Settings source
Toggle the managed node sources<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings source <source> <state>`
Extended Arg Info
> ### source: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>plmanaged Settings host
Set the managed node host<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings host <host>`
Extended Arg Info
> ### host: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>plmanaged Settings filter
Toggle the managed node filters<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings filter <filter_name> <state>`
Extended Arg Info
> ### filter_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>plmanaged Settings iprotation
Configure Lavalink IP Rotation for rate limits.<br/>

Run `<@1275521742961508432>plmanaged settings iprotation 1` to remove the ip rotation<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings iprotation [reset]`
 - Aliases: `ir`
Extended Arg Info
> ### reset: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


### <@1275521742961508432>plmanaged Settings plugins
Change the managed node plugins<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings plugins`


#### <@1275521742961508432>plmanaged Settings plugins disable
Disabled one of the available plugins<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings plugins disable <plugin>`
Extended Arg Info
> ### plugin: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>plmanaged Settings plugins update
Update the managed node plugins<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings plugins update`


#### <@1275521742961508432>plmanaged Settings plugins enable
Enable one of the available plugins<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings plugins enable <plugin>`
Extended Arg Info
> ### plugin: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>plmanaged Settings server
Configure multiple settings for the managed node.<br/>

Run `<@1275521742961508432>plmanaged settings server <setting> info` to show info about the settings and what they do.<br/>

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
 - Usage: `<@1275521742961508432>plmanaged Settings server <setting> <value>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>plmanaged Settings httpproxy
Configure a HTTP proxy for Lavalink<br/>

Run `<@1275521742961508432>plmanaged settings httpproxy 1` to remove the proxy.<br/>
 - Usage: `<@1275521742961508432>plmanaged Settings httpproxy [reset]`
 - Aliases: `hp`
Extended Arg Info
> ### reset: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>plmanaged version
Show the version of the Cog and PyLav<br/>
 - Usage: `<@1275521742961508432>plmanaged version`


## <@1275521742961508432>plmanaged update
Update the managed Lavalink node<br/>
 - Usage: `<@1275521742961508432>plmanaged update [update=0]`
Extended Arg Info
> ### update: int = 0
> ```
> A number without decimal places.
> ```


