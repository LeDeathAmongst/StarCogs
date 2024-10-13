TimeChannel
===========

Allocate a Discord voice channel to show the time in specific timezones. Updates every hour.

A list of timezones can be found here, though you should be able to enter any
major city: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List

There is a fuzzy search so you don't need to put the region in, only the city.

The `[p]timezones` command (runnable by anyone) will show the full location name.

<<<<<<< HEAD
# <@1275521742961508432>timechannelinfo

 - Usage: `<@1275521742961508432>timechannelinfo`
 - Aliases: `tcinfo`


# <@1275521742961508432>timezones
See the time in all the configured timezones for this server.<br/>
 - Usage: `<@1275521742961508432>timezones`
 - Checks: `server_only`


# <@1275521742961508432>timechannelset
Manage channels which will show the time for a timezone.<br/>
 - Usage: `<@1275521742961508432>timechannelset`
=======
# ,timechannelinfo

 - Usage: `,timechannelinfo`
 - Aliases: `tcinfo`


# ,timezones
See the time in all the configured timezones for this server.<br/>
 - Usage: `,timezones`
 - Checks: `server_only`


# ,timechannelset
Manage channels which will show the time for a timezone.<br/>
 - Usage: `,timechannelset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `tcset`


<<<<<<< HEAD
## <@1275521742961508432>timechannelset create
Set up a time channel in this server.<br/>

If you move the channel into a category, **click 'Keep Current Permissions' in the sync<br/>
permissions dialogue.**<br/>

**How to use this command:**<br/>

First, use the `<@1275521742961508432>tcset short <long_tz>` to get the short identifier for the<br/>
timezone of your choice.<br/>

Once you've got a short identifier from `tcset short`, you can use it in this command.<br/>
Simply put curly brackets, `{` and `}` around it, and it will be replaced with the time.<br/>

**For example**, running `<@1275521742961508432>tcset short new york` gives a short identifier of `fv`.<br/>
This can then be used like so:<br/>
`<@1275521742961508432>tcset create 🕑️ New York: {fv}`.<br/>

You could also use two in one, for example<br/>
`<@1275521742961508432>tcset create UK: {ni} FR: {nr}`<br/>

The default is 12 hour time, but you can use `{shortid-24h}` for 24 hour time,<br/>
eg `{ni-24h}`<br/>

**More Examples:**<br/>
- `<@1275521742961508432>tcset create 🕑️ New York: {fv}`<br/>
- `<@1275521742961508432>tcset create 🌐 UTC: {qw}`<br/>
- `<@1275521742961508432>tcset create {ni-24h} in London`<br/>
- `<@1275521742961508432>tcset create US Pacific: {qv-24h}`<br/>
 - Usage: `<@1275521742961508432>timechannelset create <string>`
Extended Arg Info
> ### string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>timechannelset remove
=======
## ,timechannelset remove
>>>>>>> 9e308722 (Revamped and Fixed)
Delete and stop updating a channel.<br/>

For the <channel> argument, you can use its ID or mention (type #!channelname)<br/>

**Example:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>tcset remove #!channelname` (the ! is how to mention voice channels)<br/>
- `<@1275521742961508432>tcset remove 834146070094282843`<br/>
 - Usage: `<@1275521742961508432>timechannelset remove <channel>`
=======
- `,tcset remove #!channelname` (the ! is how to mention voice channels)<br/>
- `,tcset remove 834146070094282843`<br/>
 - Usage: `,timechannelset remove <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>timechannelset short
=======
## ,timechannelset short
>>>>>>> 9e308722 (Revamped and Fixed)
Get the short identifier for the main `create` command.<br/>

The list of acceptable timezones is here (the "TZ database name" column):<br/>
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List<br/>

There is a fuzzy search, so you shouldn't need to enter the region.<br/>

<<<<<<< HEAD
Please look at `<@1275521742961508432>help tcset create` for more information.<br/>

**Examples:**<br/>
- `<@1275521742961508432>tcset short New York`<br/>
- `<@1275521742961508432>tcset short UTC`<br/>
- `<@1275521742961508432>tcset short London`<br/>
- `<@1275521742961508432>tcset short Europe/London`<br/>
 - Usage: `<@1275521742961508432>timechannelset short <timezone>`
=======
Please look at `,help tcset create` for more information.<br/>

**Examples:**<br/>
- `,tcset short New York`<br/>
- `,tcset short UTC`<br/>
- `,tcset short London`<br/>
- `,tcset short Europe/London`<br/>
 - Usage: `,timechannelset short <timezone>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### timezone: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>timechannelset loopstatus

 - Usage: `<@1275521742961508432>timechannelset loopstatus`
 - Restricted to: `BOT_OWNER`


=======
## ,timechannelset loopstatus

 - Usage: `,timechannelset loopstatus`
 - Restricted to: `BOT_OWNER`


## ,timechannelset create
Set up a time channel in this server.<br/>

If you move the channel into a category, **click 'Keep Current Permissions' in the sync<br/>
permissions dialogue.**<br/>

**How to use this command:**<br/>

First, use the `,tcset short <long_tz>` to get the short identifier for the<br/>
timezone of your choice.<br/>

Once you've got a short identifier from `tcset short`, you can use it in this command.<br/>
Simply put curly brackets, `{` and `}` around it, and it will be replaced with the time.<br/>

**For example**, running `,tcset short new york` gives a short identifier of `fv`.<br/>
This can then be used like so:<br/>
`,tcset create 🕑️ New York: {fv}`.<br/>

You could also use two in one, for example<br/>
`,tcset create UK: {ni} FR: {nr}`<br/>

The default is 12 hour time, but you can use `{shortid-24h}` for 24 hour time,<br/>
eg `{ni-24h}`<br/>

**More Examples:**<br/>
- `,tcset create 🕑️ New York: {fv}`<br/>
- `,tcset create 🌐 UTC: {qw}`<br/>
- `,tcset create {ni-24h} in London`<br/>
- `,tcset create US Pacific: {qv-24h}`<br/>
 - Usage: `,timechannelset create <string>`
Extended Arg Info
> ### string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


>>>>>>> 9e308722 (Revamped and Fixed)
