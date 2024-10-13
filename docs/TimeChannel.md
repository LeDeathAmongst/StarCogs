Allocate a Discord voice channel to show the time in specific timezones. Updates every hour.<br/><br/>A list of timezones can be found here, though you should be able to enter any<br/>major city: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List<br/><br/>There is a fuzzy search so you don't need to put the region in, only the city.<br/><br/>The `[p]timezones` command (runnable by anyone) will show the full location name.

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
 - Restricted to: `ADMIN`
 - Aliases: `tcset`
## ,timechannelset remove
Delete and stop updating a channel.<br/>

For the <channel> argument, you can use its ID or mention (type #!channelname)<br/>

**Example:**<br/>
- `,tcset remove #!channelname` (the ! is how to mention voice channels)<br/>
- `,tcset remove 834146070094282843`<br/>
 - Usage: `,timechannelset remove <channel>`
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
## ,timechannelset short
Get the short identifier for the main `create` command.<br/>

The list of acceptable timezones is here (the "TZ database name" column):<br/>
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List<br/>

There is a fuzzy search, so you shouldn't need to enter the region.<br/>

Please look at `,help tcset create` for more information.<br/>

**Examples:**<br/>
- `,tcset short New York`<br/>
- `,tcset short UTC`<br/>
- `,tcset short London`<br/>
- `,tcset short Europe/London`<br/>
 - Usage: `,timechannelset short <timezone>`
Extended Arg Info
> ### timezone: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
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
