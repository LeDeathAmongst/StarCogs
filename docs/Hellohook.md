# Hellohook Help

### hellohook

**Description:** Hellohook settings

**`[p]hellohook settings`** View current settings

**`[p]hellohook setgreet`** Set a Greet/welcome message
**`[p]hellohook setgreethook`**  Set #channel for Greet message

**`[p]hellohook setleave`** Set a Leave message
**`[p]hellohook setleavehook`**  Set #channel for Leave message

Due to Discord limitations, you will have to create a webhook yourself in the channel you want the welcome message in. See **`[p]hellohook setgreethook`** for more details.

[See Documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)

**Usage:** `<@1275521742961508432>hellohook`

### hellohook toggle

**Description:** Enable/Disable Hellohook Greet/Leave messages

[p]hellohook toggle greet true -> enable Greet messages
[p]hellohook toggle greet false -> disable Greet messages

[p]hellohook toggle leave true -> enable Leave messages
[p]hellohook toggle leave false -> disable Leave messages

**Usage:** `<@1275521742961508432>hellohook toggle`

### hellohook setleave

**Description:** Set the Leave message

        The message must be a `{ "content": …, "embeds": [{}] }` object.

        You can use variables to put the info of users into the message automatically.

        [Create a webhook message here >
See Hellohook help documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)

        When you are done on Discohook:
        - Scroll to the bottom
        - Click "JSON Data Editor"
        - Click "Copy to Clipboard"
        - Paste it into this bot command
        

**Usage:** `<@1275521742961508432>hellohook setleave`

### hellohook settings

**Description:** List current Hellohook settings

**Usage:** `<@1275521742961508432>hellohook settings`

### hellohook test

**Description:** Send a test welcome message to the hellohook

**Usage:** `<@1275521742961508432>hellohook test`

### hellohook invite

**Description:** Send custom Hellohook welcomes based on invite URLs (beta)

-
⚠️ **Warning: This feature is still in testing.
Data loss is possible. Use at your own risk.
[See Documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)**

**Usage:** `<@1275521742961508432>hellohook invite`

### hellohook invite sync

**Description:** Re-sync the invite tracker if bot's been offline

If the bot has gone offline before, run this command to ensure the bot is tracking the right invites.

Will also remove all server invites that have expired or disappeared.

**Usage:** `<@1275521742961508432>hellohook invite sync`

### hellohook invite remove

**Description:** Remove a custom invite-based welcome

Please input only the ##### part of your <https://discord.gg/#####> invite.

**Usage:** `<@1275521742961508432>hellohook invite remove`

### hellohook invite settings

**Description:** List all invite-based welcomes

**Usage:** `<@1275521742961508432>hellohook invite settings`

### hellohook invite test

**Description:** Test all invite-based welcomes

**Usage:** `<@1275521742961508432>hellohook invite test`

### hellohook invite add

**Description:** Add a custom invite-based welcome

**Usage:** `<@1275521742961508432>hellohook invite add`

### hellohook invite edit

**Description:** Edit a custom invite-based welcome

Please input only the ##### part of your <https://discord.gg/#####> invite.

Fields:
  channel - for webhook URL
  message - for Discohook JSON

**Usage:** `<@1275521742961508432>hellohook invite edit`

### hellohook setleavehook

**Description:** Set the webhook URL/channel for Leave messages

Must be webhook URL. Due to Discord limitations, you will have to make the webhook yourself. You can create a webhook in your desired channel by:

#channel ⚙ settings > Integrations > Webhooks > New Webhook

[How to create a webhook (image) >](https://support.discord.com/hc/article_attachments/1500000463501/Screen_Shot_2020-12-15_at_4.41.53_PM.png)

After you create the webhook, you can customize the profile picture and name of the "bot", which will be used when Hellohook sends a message.

**Usage:** `<@1275521742961508432>hellohook setleavehook`

### hellohook reset

**Description:** ⚠️ Reset all settings

**Usage:** `<@1275521742961508432>hellohook reset`

### hellohook setgreet

**Description:** Set the Greet message

        The message must be a `{ "content": …, "embeds": [{}] }` object.

        You can use variables to put the info of new users into the welcome message automatically.

        [Create a webhook message here >
See Hellohook help documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)

        When you are done on Discohook:
        - Scroll to the bottom
        - Click "JSON Data Editor"
        - Click "Copy to Clipboard"
        - Paste it into this bot command
        

**Usage:** `<@1275521742961508432>hellohook setgreet`

### hellohook setgreethook

**Description:** Set the webhook URL/channel for Greet messages

Must be webhook URL. Due to Discord limitations, you will have to make the webhook yourself. You can create a webhook in your desired channel by:

#channel ⚙ settings > Integrations > Webhooks > New Webhook

[How to create a webhook (image) >](https://support.discord.com/hc/article_attachments/1500000463501/Screen_Shot_2020-12-15_at_4.41.53_PM.png)

After you create the webhook, you can customize the profile picture and name of the "bot", which will be used when Hellohook sends a message.

**Usage:** `<@1275521742961508432>hellohook setgreethook`

