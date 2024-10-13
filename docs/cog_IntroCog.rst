IntroCog
========

# ,intro
Manage your introduction.<br/>
 - Usage: `,intro`
 - Checks: `server_only`


## ,intro removefield
Remove a field from the introduction form.<br/>
 - Usage: `,intro removefield <field_name>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,intro setfooter
Set the footer for the introduction embed.<br/>
 - Usage: `,intro setfooter <footer>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### footer: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,intro setbreakfield
Set the title for the break field.<br/>
 - Usage: `,intro setbreakfield <break_field_title>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### break_field_title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,intro addvalue
Add a field value to your introduction.<br/>

Example: ,intro addvalue name John Doe<br/>
 - Usage: `,intro addvalue <field_name> <field_value>`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### field_value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,intro preview
Preview your introduction.<br/>
 - Usage: `,intro preview`


## ,intro addfield
Add a field to the introduction form.<br/>
 - Usage: `,intro addfield <field_name>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,intro viewfooter
View the current footer for the introduction embed.<br/>
 - Usage: `,intro viewfooter`


## ,intro viewbreakfield
View the current break field title.<br/>
 - Usage: `,intro viewbreakfield`


## ,intro setcolor
Set the color for your introduction embed.<br/>
 - Usage: `,intro setcolor <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     


## ,intro send
Send your introduction to the configured channel.<br/>
 - Usage: `,intro send`


## ,intro example
Set an example introduction with predefined fields and values.<br/>
 - Usage: `,intro example`


## ,intro viewfields
View the fields available for your introduction in this server.<br/>
 - Usage: `,intro viewfields`


## ,intro settitle
Set the title for the introduction embed.<br/>
 - Usage: `,intro settitle <title>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,intro viewtitle
View the current title for the introduction embed.<br/>
 - Usage: `,intro viewtitle`


## ,intro editvalue
Edit a field value in your introduction.<br/>

Example: ,intro editvalue name Jane Doe<br/>
 - Usage: `,intro editvalue <field_name> <field_value>`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### field_value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,intro setchannel
Set the channel where introductions will be sent.<br/>
 - Usage: `,intro setchannel <channel>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
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


## ,intro removevalue
Remove a field value from your introduction.<br/>
 - Usage: `,intro removevalue <field_name>`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


