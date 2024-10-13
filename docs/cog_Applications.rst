Applications
============

A complex application system for Discord servers.

# ,appset
Configure the application system.<br/>
 - Usage: `,appset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,appset setlogchannel
Set the channel for application logs.<br/>
 - Usage: `,appset setlogchannel <channel>`
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


## ,appset setmessage
Set the message for the application embed.<br/>
 - Usage: `,appset setmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,appset setchannel
Set the channel where applications will be sent.<br/>
 - Usage: `,appset setchannel <channel>`
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


# ,createapplyembed
Create an embed with a dropdown for users to start applications.<br/>
 - Usage: `,createapplyembed`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


# ,apps
Manage application types and questions.<br/>
 - Usage: `,apps`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


# ,apply
Start a new application.<br/>
 - Usage: `,apply`
 - Checks: `server_only`


# ,appstats
View application statistics.<br/>
 - Usage: `,appstats`
 - Checks: `server_only`


# ,appsearch
Search for applications by user or type.<br/>
 - Usage: `,appsearch <search_term>`
 - Checks: `server_only`
Extended Arg Info
> ### search_term: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


