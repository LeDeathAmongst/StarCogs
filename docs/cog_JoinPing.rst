JoinPing
========

Ghost ping users when they join.

# ,jpset
Adjust the settings for the cog.<br/>
 - Usage: `,jpset`
 - Restricted to: `ADMIN`
 - Aliases: `joinpingset`
 - Checks: `server_only`


## ,jpset channel
Set the channels where the pings will be sent on member join.<br/>
 - Usage: `,jpset channel`
 - Aliases: `c and channels`


### ,jpset channel add
Remove the channels from the list of channels where the pings will be sent on member join.<br/>
 - Usage: `,jpset channel add <channels>`
 - Aliases: `a`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


### ,jpset channel remove
Add the channels to the list of channels where the pings will be sent on member join.<br/>
 - Usage: `,jpset channel remove <channels>`
 - Aliases: `r`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,jpset deleteafter
Set the time in seconds after which the ping message will be deleted.<br/>
 - Usage: `,jpset deleteafter <seconds>`
 - Aliases: `da`
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```


## ,jpset show
Show the current joinping settings.<br/>
 - Usage: `,jpset show`
 - Aliases: `showsettings, settings, and setting`


## ,jpset test
Test whether the pings and message you set up work correctly.<br/>

This is hidden as to not abuse the pings.<br/>
 - Usage: `,jpset test`
 - Aliases: `testping`


## ,jpset message
Set the message that will be sent when a user joins.<br/>

Usable placeholders include:<br/>
- {member} (the member that joined)<br/>
    - {member(mention)} (the mention)<br/>
    - {member(id)} (the id)<br/>
    - {member(name)} (the name)<br/>
    - {member(discriminator)} (the discriminator)<br/>

- {server} (the server the member joined)<br/>

This messsage uses tagscript and allows embed<br/>
 - Usage: `,jpset message <message>`
 - Aliases: `m`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


