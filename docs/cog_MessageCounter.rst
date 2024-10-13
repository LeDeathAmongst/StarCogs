MessageCounter
==============

# ,messagestats
Commands for tracking how many messages matched patterns.<br/>
 - Usage: `,messagestats`
 - Restricted to: `ADMIN`


## ,messagestats info
Checks the complete info of a tracked word.<br/>
 - Usage: `,messagestats info <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats dontnotifychannel
Turn off the notifychannel trigger.<br/>
 - Usage: `,messagestats dontnotifychannel <channel> <word>`
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
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats addcounter
Adds a counter for how many times a message with this word has been sent in this server.<br/>
 - Usage: `,messagestats addcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats notifyme
Whenever the word appears in a message on this server you will receive a DM from this bot.<br/>
 - Usage: `,messagestats notifyme <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats checkcounter
Checks how many messages containing this word have been sent since we started counting.<br/>
 - Usage: `,messagestats checkcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats resetcounter
Resets the counter of the word to 0 and the started-counting date to now.<br/>
 - Usage: `,messagestats resetcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats dontnotifyme
Turn off the notifyme trigger.<br/>
 - Usage: `,messagestats dontnotifyme <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats list
Lists all words we are looking for in this server with their stored info.<br/>
 - Usage: `,messagestats list`


## ,messagestats notifychannel
Whenever a message containing this word appears in this server a message is sent to the set channel.<br/>
 - Usage: `,messagestats notifychannel <channel> <word>`
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
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,messagestats delcounter
Deletes the counter for this word.<br/>
 - Usage: `,messagestats delcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


