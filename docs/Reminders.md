# Reminders Help

### remindme

**Description:** Create a reminder with optional reminder text or message.

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.
Use `[p]reminder timetips` to display tips for time parsing.

**Examples:**
- `[p]remindme in 8min45sec to do that thing`
- `[p]remindme to water my plants in 2 hours`
- `[p]remindme in 3 days`
- `[p]remindme 8h`
- `[p]remindme every 1 week to take out the trash`
- `[p]remindme in 1 hour <message_link>`
- `[p]remindme at 10h to add some feature to my codes`

**Usage:** `<@1275521742961508432>remindme`

### remind

**Description:** Create a reminder with optional reminder text or message, in a channel with an user/role ping.

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.
Use `[p]reminder timetips` to display tips for time parsing.

Examples:
- `[p]remind #destination @user1 @user2 @user2 in 2 hours to buy a gift`

**Usage:** `<@1275521742961508432>remind`

### reminder

**Description:** List, edit and delete existing reminders, or create FIFO/commands or Say reminders.

**Usage:** `<@1275521742961508432>reminder`

### reminder fifo

**Description:** Create a FIFO/command reminder. The chosen command will be executed with you as invoker. Don't provide the prefix.

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.
Use `[p]reminder timetips` to display tips for time parsing.

Examples:
- `[p]reminder fifo #destination "at 10h every day" ping

**Usage:** `<@1275521742961508432>reminder fifo`

### reminder list

**Description:** List your existing reminders.

Sort options:
- `expire`: Display them in order of next triggering.
- `created`: Display them in order of creating.
- `id`: Display them in order of their ID.

**Usage:** `<@1275521742961508432>reminder list`

### reminder text

**Description:** Edit the text of an existing Reminder from its ID.

- Use `last` to edit your last created reminder.
- Use `next` to edit your next triggered reminder.

**Usage:** `<@1275521742961508432>reminder text`

### reminder expires

**Description:** Edit the expires time of an existing Reminder from its ID.

- Use `last` to edit your last created reminder.
- Use `next` to edit your next triggered reminder.
It's the same converter as for creation, but without the option of repetition.

**Usage:** `<@1275521742961508432>reminder expires`

### reminder clear

**Description:** Clear all your existing reminders.

**Usage:** `<@1275521742961508432>reminder clear`

### reminder repeat

**Description:** Edit the repeat of an existing Reminder from its ID.

- Use `last` to edit your last created reminder.
- Use `next` to edit your next triggered reminder.

Allowed **intervals** are:
• `years`/`year`/`y`
• `months`/`month`/`mo`
• `weeks`/`week`/`w`
• `days`/`day`/`d`
• `hours`/`hour`/`hrs`/`hr`/`h`
• `minutes`/`minute`/`mins`/`min`/`m`

You can combine **relative intervals** like this:
• `1y 1mo 2 days -5h`

**Usage:** `<@1275521742961508432>reminder repeat`

### reminder timestamps

**Description:** Get a list of Discord timestamps for a given time. You can provide a repeat.

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule.
You don't have to put quotes around the `time` argument.
Use `[p]reminder timetips` to display tips for time parsing.

**Usage:** `<@1275521742961508432>reminder timestamps`

### reminder say

**Description:** Create a reminder who will say/send text.

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.
Use `[p]reminder timetips` to display tips for time parsing.

Examples:
- `[p]reminder say #destination "at 9h every day" Hello everyone!

**Usage:** `<@1275521742961508432>reminder say`

### reminder timetips

**Description:** Show time parsing tips.

**Usage:** `<@1275521742961508432>reminder timetips`

### reminder edit

**Description:** Edit an existing Reminder from its ID.

- Use `last` to edit your last created reminder.
- Use `next` to edit your next triggered reminder.

**Usage:** `<@1275521742961508432>reminder edit`

### reminder timezone

**Description:** Set your timezone for the time converter.

Timezone should be specified in the format: `Continent/City`.
Example: `Europe/Paris`, `America/New_York`...
You can find a list of valid timezones at: https://timezonedb.com/time-zones.

**Usage:** `<@1275521742961508432>reminder timezone`

### reminder remove

**Description:** Remove existing Reminder(s) from their IDs.

- Use `last` to remove your last created reminder.
- Use `next` to remove your next triggered reminder.

**Usage:** `<@1275521742961508432>reminder remove`

### setreminders

**Description:** Configure Reminders.

**Usage:** `<@1275521742961508432>setreminders`

### setreminders secondsallowed

**Description:** Check reminders every 30 seconds instead of every 1 minute, to allow reminders with precise duration.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setreminders secondsallowed`

### setreminders maximumuserreminders

**Description:** Change the reminders limit for each user (except bot owners).

Default value: `20`
Dev: `Range[int, 1, 125]`

**Usage:** `<@1275521742961508432>setreminders maximumuserreminders`

### setreminders metoo

**Description:** Show a `Me too` button in reminders.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setreminders metoo`

### setreminders clearuserreminders

**Description:** Clear all existing reminders for a user.

**Usage:** `<@1275521742961508432>setreminders clearuserreminders`

### setreminders showsettings

**Description:** Show all settings for the cog with defaults and values.

**Usage:** `<@1275521742961508432>setreminders showsettings`

### setreminders minimumrepeat

**Description:** Change the minimum minutes number for a repeat time.

Default value: `60`
Dev: `Range[int, 10, None]`

**Usage:** `<@1275521742961508432>setreminders minimumrepeat`

### setreminders snoozeview

**Description:** Send Snooze view/buttons when reminders sending.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setreminders snoozeview`

### setreminders migratefromremindme

**Description:** Migrate Reminders from RemindMe by PhasecoreX.

**Usage:** `<@1275521742961508432>setreminders migratefromremindme`

### setreminders migratefromfifo

**Description:** Migrate Reminders from FIFO by Fox.

**Usage:** `<@1275521742961508432>setreminders migratefromfifo`

### setreminders modalconfig

**Description:** Set all settings for the cog with a Discord Modal.

**Usage:** `<@1275521742961508432>setreminders modalconfig`

### setreminders repeatallowed

**Description:** Enable or disabled repeat option for users (except bot owners).

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setreminders repeatallowed`

### setreminders resetsetting

**Description:** Reset a setting.

**Usage:** `<@1275521742961508432>setreminders resetsetting`

### setreminders fifoallowed

**Description:** Allow or deny commands reminders for users (except bot owners).

Default value: `False`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setreminders fifoallowed`

### setreminders creationview

**Description:** Send Creation view/buttons when reminders creation.

Default value: `True`
Dev: `<class 'bool'>`

**Usage:** `<@1275521742961508432>setreminders creationview`

