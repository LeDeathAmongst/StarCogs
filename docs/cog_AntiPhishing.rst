AntiPhishing
============

Guard users from malicious links and phishing attempts with customizable protection options.

<<<<<<< HEAD
# <@1275521742961508432>antiphishing
Configurable options to help keep known malicious links out of your community's conversations.<br/>
 - Usage: `<@1275521742961508432>antiphishing`
 - Checks: `server_only`


## <@1275521742961508432>antiphishing logchannel
Set the logging channel where link detections will be sent.<br/>
 - Usage: `<@1275521742961508432>antiphishing logchannel <channel>`
=======
# ,antiphishing
Configurable options to help keep known malicious links out of your community's conversations.<br/>
 - Usage: `,antiphishing`
 - Checks: `server_only`


## ,antiphishing enroll
Enroll your server into remote URL monitoring by providing a webhook URL.<br/>

The webhook will be used to send detected URLs to a security provider for monitoring.<br/>
 - Usage: `,antiphishing enroll <webhook>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### webhook: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,antiphishing logchannel
Set the logging channel where link detections will be sent.<br/>
 - Usage: `,antiphishing logchannel <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
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


<<<<<<< HEAD
## <@1275521742961508432>antiphishing settings
Show the current antiphishing settings.<br/>
 - Usage: `<@1275521742961508432>antiphishing settings`
 - Restricted to: `ADMIN`


## <@1275521742961508432>antiphishing action
=======
## ,antiphishing settings
Show the current antiphishing settings.<br/>
 - Usage: `,antiphishing settings`
 - Restricted to: `ADMIN`


## ,antiphishing stats
Check protection statistics for this server<br/>
 - Usage: `,antiphishing stats`


## ,antiphishing action
>>>>>>> 9e308722 (Revamped and Fixed)
Choose the action that occurs when a user sends a phishing scam.<br/>

Options:<br/>
**`ignore`** - Disables phishing protection<br/>
**`notify`** - Alerts in channel when malicious links detected (default)<br/>
**`delete`** - Deletes the message<br/>
**`kick`** - Delete message and kick sender<br/>
**`ban`** - Delete message and ban sender (recommended)<br/>
**`timeout`** - Temporarily mute the user<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>antiphishing action <action>`
=======
 - Usage: `,antiphishing action <action>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>antiphishing autoban
Set the number of malicious links a user can share before being banned. Set to 0 to disable autoban.<br/>
 - Usage: `<@1275521742961508432>antiphishing autoban <autoban>`
=======
## ,antiphishing autoban
Set the number of malicious links a user can share before being banned. Set to 0 to disable autoban.<br/>
 - Usage: `,antiphishing autoban <autoban>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
Extended Arg Info
> ### autoban: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>antiphishing stats
Check protection statistics for this server<br/>
 - Usage: `<@1275521742961508432>antiphishing stats`


## <@1275521742961508432>antiphishing enroll
Enroll your server into remote URL monitoring by providing a webhook URL.<br/>

The webhook will be used to send detected URLs to a security provider for monitoring.<br/>
 - Usage: `<@1275521742961508432>antiphishing enroll <webhook>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### webhook: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


=======
>>>>>>> 9e308722 (Revamped and Fixed)
