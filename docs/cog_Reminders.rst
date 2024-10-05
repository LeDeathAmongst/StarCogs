Reminders
=========

Don't forget anything anymore! Reminders in DMs, channels, FIFO commands scheduler, say scheduler... With 'Me Too', snooze and buttons.

# <@1275521742961508432>remindme (Hybrid Command)
Create a reminder with optional reminder text or message.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `<@1275521742961508432>reminder timetips` to display tips for time parsing.<br/>

**Examples:**<br/>
- `<@1275521742961508432>remindme in 8min45sec to do that thing`<br/>
- `<@1275521742961508432>remindme to water my plants in 2 hours`<br/>
- `<@1275521742961508432>remindme in 3 days`<br/>
- `<@1275521742961508432>remindme 8h`<br/>
- `<@1275521742961508432>remindme every 1 week to take out the trash`<br/>
- `<@1275521742961508432>remindme in 1 hour <message_link>`<br/>
- `<@1275521742961508432>remindme at 10h to add some feature to my codes`<br/>
 - Usage: `<@1275521742961508432>remindme <time> [message_or_text]`
 - Slash Usage: `/remindme <time> [message_or_text]`
Extended Arg Info
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message_or_text: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>remind (Hybrid Command)
Create a reminder with optional reminder text or message, in a channel with an user/role ping.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `<@1275521742961508432>reminder timetips` to display tips for time parsing.<br/>

Examples:<br/>
- `<@1275521742961508432>remind #destination @user1 @user2 @user2 in 2 hours to buy a gift`<br/>
 - Usage: `<@1275521742961508432>remind <destination> <targets> <time> [message_or_text]`
 - Slash Usage: `/remind <destination> <targets> <time> [message_or_text]`
 - Checks: `server_only`
Extended Arg Info
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message_or_text: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>reminder (Hybrid Command)
List, edit and delete existing reminders, or create FIFO/commands or Say reminders.<br/>
 - Usage: `<@1275521742961508432>reminder`
 - Slash Usage: `/reminder`
 - Aliases: `reminders`


## <@1275521742961508432>reminder remove (Hybrid Command)
Remove existing Reminder(s) from their IDs.<br/>

- Use `last` to remove your last created reminder.<br/>
- Use `next` to remove your next triggered reminder.<br/>
 - Usage: `<@1275521742961508432>reminder remove <reminders>`
 - Slash Usage: `/reminder remove <reminders>`
 - Aliases: `delete and -`


## <@1275521742961508432>reminder timetips (Hybrid Command)
Show time parsing tips.<br/>
 - Usage: `<@1275521742961508432>reminder timetips`
 - Slash Usage: `/reminder timetips`
 - Aliases: `parsingtips`


## <@1275521742961508432>reminder expires (Hybrid Command)
Edit the expires time of an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>
It's the same converter as for creation, but without the option of repetition.<br/>
 - Usage: `<@1275521742961508432>reminder expires <reminder> <time>`
 - Slash Usage: `/reminder expires <reminder> <time>`
 - Aliases: `expiresat`
Extended Arg Info
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>reminder fifo (Hybrid Command)
Create a FIFO/command reminder. The chosen command will be executed with you as invoker. Don't provide the prefix.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `<@1275521742961508432>reminder timetips` to display tips for time parsing.<br/>

Examples:<br/>
- `<@1275521742961508432>reminder fifo #destination "at 10h every day" ping<br/>
 - Usage: `<@1275521742961508432>reminder fifo <destination> <time> <command>`
 - Slash Usage: `/reminder fifo <destination> <time> <command>`
 - Restricted to: `ADMIN`
 - Aliases: `command`
 - Checks: `server_only`
Extended Arg Info
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>reminder timezone (Hybrid Command)
Set your timezone for the time converter.<br/>

Timezone should be specified in the format: `Continent/City`.<br/>
Example: `Europe/Paris`, `America/New_York`...<br/>
You can find a list of valid timezones at: https://timezonedb.com/time-zones.<br/>
 - Usage: `<@1275521742961508432>reminder timezone <timezone>`
 - Slash Usage: `/reminder timezone <timezone>`


## <@1275521742961508432>reminder repeat (Hybrid Command)
Edit the repeat of an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>

Allowed **intervals** are:<br/>
• `years`/`year`/`y`<br/>
• `months`/`month`/`mo`<br/>
• `weeks`/`week`/`w`<br/>
• `days`/`day`/`d`<br/>
• `hours`/`hour`/`hrs`/`hr`/`h`<br/>
• `minutes`/`minute`/`mins`/`min`/`m`<br/>

You can combine **relative intervals** like this:<br/>
• `1y 1mo 2 days -5h`<br/>
 - Usage: `<@1275521742961508432>reminder repeat <reminder> <repeat>`
 - Slash Usage: `/reminder repeat <reminder> <repeat>`
Extended Arg Info
> ### repeat: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>reminder list (Hybrid Command)
List your existing reminders.<br/>

Sort options:<br/>
- `expire`: Display them in order of next triggering.<br/>
- `created`: Display them in order of creating.<br/>
- `id`: Display them in order of their ID.<br/>
 - Usage: `<@1275521742961508432>reminder list [card=False] [content_type=None] [sort=expire]`
 - Slash Usage: `/reminder list [card=False] [content_type=None] [sort=expire]`
Extended Arg Info
> ### card: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>reminder clear (Hybrid Command)
Clear all your existing reminders.<br/>
 - Usage: `<@1275521742961508432>reminder clear [confirmation=False]`
 - Slash Usage: `/reminder clear [confirmation=False]`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>reminder edit (Hybrid Command)
Edit an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>
 - Usage: `<@1275521742961508432>reminder edit <reminder>`
 - Slash Usage: `/reminder edit <reminder>`
 - Aliases: `info and show`


## <@1275521742961508432>reminder say (Hybrid Command)
Create a reminder who will say/send text.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `<@1275521742961508432>reminder timetips` to display tips for time parsing.<br/>

Examples:<br/>
- `<@1275521742961508432>reminder say #destination "at 9h every day" Hello everyone!<br/>
 - Usage: `<@1275521742961508432>reminder say <destination> <time> <text>`
 - Slash Usage: `/reminder say <destination> <time> <text>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>reminder text (Hybrid Command)
Edit the text of an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>
 - Usage: `<@1275521742961508432>reminder text <reminder> <text>`
 - Slash Usage: `/reminder text <reminder> <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>reminder timestamps (Hybrid Command)
Get a list of Discord timestamps for a given time. You can provide a repeat.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule.<br/>
You don't have to put quotes around the `time` argument.<br/>
Use `<@1275521742961508432>reminder timetips` to display tips for time parsing.<br/>
 - Usage: `<@1275521742961508432>reminder timestamps [repeat_times=100] [time]`
 - Slash Usage: `/reminder timestamps [repeat_times=100] [time]`
 - Aliases: `timestamp`
Extended Arg Info
> ### repeat_times: Optional[int] = 100
> ```
> A number without decimal places.
> ```
> ### time: str = 'now'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>setreminders (Hybrid Command)
Configure Reminders.<br/>
 - Usage: `<@1275521742961508432>setreminders`
 - Slash Usage: `/setreminders`
 - Restricted to: `BOT_OWNER`


## <@1275521742961508432>setreminders creationview (Hybrid Command)
Send Creation view/buttons when reminders creation.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setreminders creationview <value>`
 - Slash Usage: `/setreminders creationview <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders snoozeview (Hybrid Command)
Send Snooze view/buttons when reminders sending.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setreminders snoozeview <value>`
 - Slash Usage: `/setreminders snoozeview <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders clearuserreminders (Hybrid Command)
Clear all existing reminders for a user.<br/>
 - Usage: `<@1275521742961508432>setreminders clearuserreminders <user> [confirmation=False]`
 - Slash Usage: `/setreminders clearuserreminders <user> [confirmation=False]`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders getdebugloopsstatus (Hybrid Command)
Get an embed to check loops status.<br/>
 - Usage: `<@1275521742961508432>setreminders getdebugloopsstatus`
 - Slash Usage: `/setreminders getdebugloopsstatus`


## <@1275521742961508432>setreminders resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `<@1275521742961508432>setreminders resetsetting <setting>`
 - Slash Usage: `/setreminders resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setreminders maximumuserreminders (Hybrid Command)
Change the reminders limit for each user (except bot owners).<br/>

Default value: `20`<br/>
Dev: `Range[int, 1, 125]`<br/>
 - Usage: `<@1275521742961508432>setreminders maximumuserreminders <value>`
 - Slash Usage: `/setreminders maximumuserreminders <value>`
 - Aliases: `maxuserreminders`


## <@1275521742961508432>setreminders migratefromfifo (Hybrid Command)
Migrate Reminders from FIFO by Fox.<br/>
 - Usage: `<@1275521742961508432>setreminders migratefromfifo`
 - Slash Usage: `/setreminders migratefromfifo`
 - Aliases: `migratefromfox`


## <@1275521742961508432>setreminders showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>setreminders showsettings [with_dev=False]`
 - Slash Usage: `/setreminders showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `<@1275521742961508432>setreminders modalconfig [confirmation=False]`
 - Slash Usage: `/setreminders modalconfig [confirmation=False]`
 - Aliases: `configmodal`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders minimumrepeat (Hybrid Command)
Change the minimum minutes number for a repeat time.<br/>

Default value: `60`<br/>
Dev: `Range[int, 10, None]`<br/>
 - Usage: `<@1275521742961508432>setreminders minimumrepeat <value>`
 - Slash Usage: `/setreminders minimumrepeat <value>`


## <@1275521742961508432>setreminders migratefromremindme (Hybrid Command)
Migrate Reminders from RemindMe by PhasecoreX.<br/>
 - Usage: `<@1275521742961508432>setreminders migratefromremindme`
 - Slash Usage: `/setreminders migratefromremindme`
 - Aliases: `migratefrompcx`


## <@1275521742961508432>setreminders repeatallowed (Hybrid Command)
Enable or disabled repeat option for users (except bot owners).<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setreminders repeatallowed <value>`
 - Slash Usage: `/setreminders repeatallowed <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders secondsallowed (Hybrid Command)
Check reminders every 30 seconds instead of every 1 minute, to allow reminders with precise duration.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setreminders secondsallowed <value>`
 - Slash Usage: `/setreminders secondsallowed <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders metoo (Hybrid Command)
Show a `Me too` button in reminders.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setreminders metoo <value>`
 - Slash Usage: `/setreminders metoo <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setreminders fifoallowed (Hybrid Command)
Allow or deny commands reminders for users (except bot owners).<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setreminders fifoallowed <value>`
 - Slash Usage: `/setreminders fifoallowed <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


