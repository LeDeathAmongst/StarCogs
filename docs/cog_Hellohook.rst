Hellohook
=========

Custom welcome message bots

<<<<<<< HEAD
# <@1275521742961508432>hellohook
Hellohook settings<br/>

**`<@1275521742961508432>hellohook settings`** View current settings<br/>

**`<@1275521742961508432>hellohook setgreet`** Set a Greet/welcome message<br/>
**`<@1275521742961508432>hellohook setgreethook`**  Set #channel for Greet message<br/>

**`<@1275521742961508432>hellohook setleave`** Set a Leave message<br/>
**`<@1275521742961508432>hellohook setleavehook`**  Set #channel for Leave message<br/>

Due to Discord limitations, you will have to create a webhook yourself in the channel you want the welcome message in. See **`<@1275521742961508432>hellohook setgreethook`** for more details.<br/>

[See Documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)<br/>
 - Usage: `<@1275521742961508432>hellohook`
=======
# ,hellohook
Hellohook settings<br/>

**`,hellohook settings`** View current settings<br/>

**`,hellohook setgreet`** Set a Greet/welcome message<br/>
**`,hellohook setgreethook`**  Set #channel for Greet message<br/>

**`,hellohook setleave`** Set a Leave message<br/>
**`,hellohook setleavehook`**  Set #channel for Leave message<br/>

Due to Discord limitations, you will have to create a webhook yourself in the channel you want the welcome message in. See **`,hellohook setgreethook`** for more details.<br/>

[See Documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)<br/>
 - Usage: `,hellohook`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>hellohook test
Send a test welcome message to the hellohook<br/>
 - Usage: `<@1275521742961508432>hellohook test`


## <@1275521742961508432>hellohook reset
⚠️ Reset all settings<br/>
 - Usage: `<@1275521742961508432>hellohook reset <TypeTrueToConfirm>`
Extended Arg Info
> ### TypeTrueToConfirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>hellohook setgreet
=======
## ,hellohook settings
List current Hellohook settings<br/>
 - Usage: `,hellohook settings`
 - Aliases: `list`


## ,hellohook setgreethook
Set the webhook URL/channel for Greet messages<br/>

Must be webhook URL. Due to Discord limitations, you will have to make the webhook yourself. You can create a webhook in your desired channel by:<br/>

#channel ⚙ settings > Integrations > Webhooks > New Webhook<br/>

[How to create a webhook (image) >](https://support.discord.com/hc/article_attachments/1500000463501/Screen_Shot_2020-12-15_at_4.41.53_PM.png)<br/>

After you create the webhook, you can customize the profile picture and name of the "bot", which will be used when Hellohook sends a message.<br/>
 - Usage: `,hellohook setgreethook <webhookUrl>`
 - Aliases: `set, setchannel, and setwebhook`
Extended Arg Info
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,hellohook setgreet
>>>>>>> 9e308722 (Revamped and Fixed)
Set the Greet message<br/>

        The message must be a `{ "content": …, "embeds": [{}] }` object.<br/>

        You can use variables to put the info of new users into the welcome message automatically.<br/>

        [Create a webhook message here ><br/>
See Hellohook help documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)<br/>

        When you are done on Discohook:<br/>
        - Scroll to the bottom<br/>
        - Click "JSON Data Editor"<br/>
        - Click "Copy to Clipboard"<br/>
        - Paste it into this bot command<br/>
        <br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hellohook setgreet <DiscohookJSON>`
=======
 - Usage: `,hellohook setgreet <DiscohookJSON>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `setwelcome`
Extended Arg Info
> ### DiscohookJSON: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>hellohook invite
=======
## ,hellohook test
Send a test welcome message to the hellohook<br/>
 - Usage: `,hellohook test`


## ,hellohook invite
>>>>>>> 9e308722 (Revamped and Fixed)
Send custom Hellohook welcomes based on invite URLs (beta)<br/>

-<br/>
⚠️ **Warning: This feature is still in testing.<br/>
Data loss is possible. Use at your own risk.<br/>
[See Documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)**<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hellohook invite`
=======
 - Usage: `,hellohook invite`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
 - Aliases: `inv and invites`


<<<<<<< HEAD
### <@1275521742961508432>hellohook invite add
Add a custom invite-based welcome<br/>
 - Usage: `<@1275521742961508432>hellohook invite add`


### <@1275521742961508432>hellohook invite edit
=======
### ,hellohook invite edit
>>>>>>> 9e308722 (Revamped and Fixed)
Edit a custom invite-based welcome<br/>

Please input only the ##### part of your <https://discord.gg/#####> invite.<br/>

Fields:<br/>
  channel - for webhook URL<br/>
  message - for Discohook JSON<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hellohook invite edit <inviteLink> <field> <updatedContentHere>`
=======
 - Usage: `,hellohook invite edit <inviteLink> <field> <updatedContentHere>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### inviteLink: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### field: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### updatedContentHere: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
### <@1275521742961508432>hellohook invite remove
Remove a custom invite-based welcome<br/>

Please input only the ##### part of your <https://discord.gg/#####> invite.<br/>
 - Usage: `<@1275521742961508432>hellohook invite remove <inviteLink>`
=======
### ,hellohook invite sync
Re-sync the invite tracker if bot's been offline<br/>

If the bot has gone offline before, run this command to ensure the bot is tracking the right invites.<br/>

Will also remove all server invites that have expired or disappeared.<br/>
 - Usage: `,hellohook invite sync`


### ,hellohook invite remove
Remove a custom invite-based welcome<br/>

Please input only the ##### part of your <https://discord.gg/#####> invite.<br/>
 - Usage: `,hellohook invite remove <inviteLink>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### inviteLink: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
### <@1275521742961508432>hellohook invite sync
Re-sync the invite tracker if bot's been offline<br/>

If the bot has gone offline before, run this command to ensure the bot is tracking the right invites.<br/>

Will also remove all server invites that have expired or disappeared.<br/>
 - Usage: `<@1275521742961508432>hellohook invite sync`


### <@1275521742961508432>hellohook invite settings
List all invite-based welcomes<br/>
 - Usage: `<@1275521742961508432>hellohook invite settings`
 - Aliases: `list`


### <@1275521742961508432>hellohook invite test
Test all invite-based welcomes<br/>
 - Usage: `<@1275521742961508432>hellohook invite test`


## <@1275521742961508432>hellohook setgreethook
Set the webhook URL/channel for Greet messages<br/>

Must be webhook URL. Due to Discord limitations, you will have to make the webhook yourself. You can create a webhook in your desired channel by:<br/>

#channel ⚙ settings > Integrations > Webhooks > New Webhook<br/>

[How to create a webhook (image) >](https://support.discord.com/hc/article_attachments/1500000463501/Screen_Shot_2020-12-15_at_4.41.53_PM.png)<br/>

After you create the webhook, you can customize the profile picture and name of the "bot", which will be used when Hellohook sends a message.<br/>
 - Usage: `<@1275521742961508432>hellohook setgreethook <webhookUrl>`
 - Aliases: `set, setchannel, and setwebhook`
Extended Arg Info
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>hellohook setleavehook
Set the webhook URL/channel for Leave messages<br/>

Must be webhook URL. Due to Discord limitations, you will have to make the webhook yourself. You can create a webhook in your desired channel by:<br/>

#channel ⚙ settings > Integrations > Webhooks > New Webhook<br/>

[How to create a webhook (image) >](https://support.discord.com/hc/article_attachments/1500000463501/Screen_Shot_2020-12-15_at_4.41.53_PM.png)<br/>

After you create the webhook, you can customize the profile picture and name of the "bot", which will be used when Hellohook sends a message.<br/>
 - Usage: `<@1275521742961508432>hellohook setleavehook <webhookUrl>`
Extended Arg Info
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>hellohook toggle
Enable/Disable Hellohook Greet/Leave messages<br/>

<@1275521742961508432>hellohook toggle greet true -> enable Greet messages<br/>
<@1275521742961508432>hellohook toggle greet false -> disable Greet messages<br/>

<@1275521742961508432>hellohook toggle leave true -> enable Leave messages<br/>
<@1275521742961508432>hellohook toggle leave false -> disable Leave messages<br/>
 - Usage: `<@1275521742961508432>hellohook toggle <GreetOrLeave> <TrueOrFalse>`
=======
### ,hellohook invite settings
List all invite-based welcomes<br/>
 - Usage: `,hellohook invite settings`
 - Aliases: `list`


### ,hellohook invite test
Test all invite-based welcomes<br/>
 - Usage: `,hellohook invite test`


### ,hellohook invite add
Add a custom invite-based welcome<br/>
 - Usage: `,hellohook invite add`


## ,hellohook toggle
Enable/Disable Hellohook Greet/Leave messages<br/>

,hellohook toggle greet true -> enable Greet messages<br/>
,hellohook toggle greet false -> disable Greet messages<br/>

,hellohook toggle leave true -> enable Leave messages<br/>
,hellohook toggle leave false -> disable Leave messages<br/>
 - Usage: `,hellohook toggle <GreetOrLeave> <TrueOrFalse>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### GreetOrLeave: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### TrueOrFalse: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>hellohook settings
List current Hellohook settings<br/>
 - Usage: `<@1275521742961508432>hellohook settings`
 - Aliases: `list`


## <@1275521742961508432>hellohook setleave
=======
## ,hellohook setleavehook
Set the webhook URL/channel for Leave messages<br/>

Must be webhook URL. Due to Discord limitations, you will have to make the webhook yourself. You can create a webhook in your desired channel by:<br/>

#channel ⚙ settings > Integrations > Webhooks > New Webhook<br/>

[How to create a webhook (image) >](https://support.discord.com/hc/article_attachments/1500000463501/Screen_Shot_2020-12-15_at_4.41.53_PM.png)<br/>

After you create the webhook, you can customize the profile picture and name of the "bot", which will be used when Hellohook sends a message.<br/>
 - Usage: `,hellohook setleavehook <webhookUrl>`
Extended Arg Info
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,hellohook setleave
>>>>>>> 9e308722 (Revamped and Fixed)
Set the Leave message<br/>

        The message must be a `{ "content": …, "embeds": [{}] }` object.<br/>

        You can use variables to put the info of users into the message automatically.<br/>

        [Create a webhook message here ><br/>
See Hellohook help documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)<br/>

        When you are done on Discohook:<br/>
        - Scroll to the bottom<br/>
        - Click "JSON Data Editor"<br/>
        - Click "Copy to Clipboard"<br/>
        - Paste it into this bot command<br/>
        <br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>hellohook setleave <DiscohookJSON>`
=======
 - Usage: `,hellohook setleave <DiscohookJSON>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### DiscohookJSON: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
=======
## ,hellohook reset
⚠️ Reset all settings<br/>
 - Usage: `,hellohook reset <TypeTrueToConfirm>`
Extended Arg Info
> ### TypeTrueToConfirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


>>>>>>> 9e308722 (Revamped and Fixed)
