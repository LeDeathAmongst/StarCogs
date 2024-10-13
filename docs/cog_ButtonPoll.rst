ButtonPoll
==========

Create polls with buttons, and get a pie chart afterwards!

# /poll (Slash Command)
Start a button-based poll.<br/>
 - Usage: `/poll <question> <duration> <choice1> <choice2> [channel] [description] [choice3] [choice4] [choice5]`
 - `question:` (Required) Question to ask.
 - `duration:` (Required) Duration of the poll. Examples: 1 day, 1 minute, 4 hours
 - `choice1:` (Required) First choice.
 - `choice2:` (Required) Second choice.
 - `channel:` (Optional) Channel to start the poll in.
 - `description:` (Optional) An optional description.
 - `choice3:` (Optional) Optional third choice.
 - `choice4:` (Optional) Optional fourth choice.
 - `choice5:` (Optional) Optional fifth choice.

 - Checks: `Server Only`
Extended Arg Info
> ### question: str
> - Autocomplete: False
> 
> Question to ask.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### duration: str
> - Autocomplete: False
> 
> Duration of the poll. Examples: 1 day, 1 minute, 4 hours
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### choice1: str
> - Autocomplete: False
> 
> First choice.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### choice2: str
> - Autocomplete: False
> 
> Second choice.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> Channel to start the poll in.
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### description: str
> - Autocomplete: False
> - Default: None
> 
> An optional description.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### choice3: str
> - Autocomplete: False
> - Default: None
> 
> Optional third choice.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### choice4: str
> - Autocomplete: False
> - Default: None
> 
> Optional fourth choice.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### choice5: str
> - Autocomplete: False
> - Default: None
> 
> Optional fifth choice.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>buttonpollinfo

 - Usage: `<@1275521742961508432>buttonpollinfo`


# <@1275521742961508432>buttonpoll
=======
# ,buttonpollinfo

 - Usage: `,buttonpollinfo`


# ,buttonpoll
>>>>>>> 9e308722 (Revamped and Fixed)
Start a button-based poll<br/>

This is an interactive setup. By default the current channel will be used,<br/>
but if you want to start a poll remotely you can send the channel name<br/>
along with the buttonpoll command.<br/>

**Examples:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>buttonpoll` - start a poll in the current channel<br/>
- `<@1275521742961508432>buttonpoll #polls` start a poll somewhere else<br/>
 - Usage: `<@1275521742961508432>buttonpoll [chan=None]`
=======
- `,buttonpoll` - start a poll in the current channel<br/>
- `,buttonpoll #polls` start a poll somewhere else<br/>
 - Usage: `,buttonpoll [chan=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `poll and bpoll`
 - Checks: `server_only`
Extended Arg Info
> ### chan: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>advstartpoll
Advanced users: create a pull using command arguments<br/>

The help text for this command is too long to fit in the help command. Just run<br/>
`<@1275521742961508432>advstartpoll` to see it.<br/>
 - Usage: `<@1275521742961508432>advstartpoll [arguments]`
=======
# ,advstartpoll
Advanced users: create a pull using command arguments<br/>

The help text for this command is too long to fit in the help command. Just run<br/>
`,advstartpoll` to see it.<br/>
 - Usage: `,advstartpoll [arguments]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### arguments: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>getvoters
=======
# ,getvoters
>>>>>>> 9e308722 (Revamped and Fixed)
Fetch the current voters for a running poll<br/>

**Arguments**<br/>
- `message_id`: (integer) The ID of the poll message<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>getvoters <message_id>`
=======
 - Usage: `,getvoters <message_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `voters`
 - Checks: `server_only`
Extended Arg Info
> ### message_id: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>endpoll
=======
# ,endpoll
>>>>>>> 9e308722 (Revamped and Fixed)
End a currently running poll<br/>

**Arguments**<br/>
- `message_id`: (integer) The ID of the poll message<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>endpoll <message_id>`
=======
 - Usage: `,endpoll <message_id>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Aliases: `endp`
 - Checks: `server_only`
Extended Arg Info
> ### message_id: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>listpolls
List all currently running polls<br/>
 - Usage: `<@1275521742961508432>listpolls`
=======
# ,listpolls
List all currently running polls<br/>
 - Usage: `,listpolls`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


