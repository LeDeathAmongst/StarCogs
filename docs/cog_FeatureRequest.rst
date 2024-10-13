FeatureRequest
==============

Cog to handle feature requests.

# ,frequest
Base command for feature requests.<br/>
 - Usage: `,frequest`
 - Aliases: `fr`


## ,frequest status
Check the status of a feature request.<br/>
 - Usage: `,frequest status <request_id>`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,frequest submit
Request a new feature for the bot.<br/>
 - Usage: `,frequest submit <feature>`
Extended Arg Info
> ### feature: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,frequest consider
Consider a feature request.<br/>
 - Usage: `,frequest consider <request_id> [reason]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,frequest deny
Deny a feature request.<br/>
 - Usage: `,frequest deny <request_id> [reason]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,frequest channel
Set the channel for feature requests.<br/>
 - Usage: `,frequest channel <channel>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,frequest accept
Accept a feature request.<br/>
 - Usage: `,frequest accept <request_id> [reason]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### request_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


