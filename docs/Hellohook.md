Custom welcome message bots

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
 - Restricted to: `ADMIN`
 - Checks: `server_only`
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
 - Usage: `,hellohook setgreet <DiscohookJSON>`
 - Aliases: `setwelcome`
Extended Arg Info
> ### DiscohookJSON: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,hellohook test
Send a test welcome message to the hellohook<br/>
 - Usage: `,hellohook test`
## ,hellohook invite
Send custom Hellohook welcomes based on invite URLs (beta)<br/>

-<br/>
⚠️ **Warning: This feature is still in testing.<br/>
Data loss is possible. Use at your own risk.<br/>
[See Documentation >](https://coffeebank.github.io/coffee-cogs/hellohook)**<br/>
 - Usage: `,hellohook invite`
 - Restricted to: `ADMIN`
 - Aliases: `inv and invites`
### ,hellohook invite edit
Edit a custom invite-based welcome<br/>

Please input only the ##### part of your <https://discord.gg/#####> invite.<br/>

Fields:<br/>
  channel - for webhook URL<br/>
  message - for Discohook JSON<br/>
 - Usage: `,hellohook invite edit <inviteLink> <field> <updatedContentHere>`
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
### ,hellohook invite sync
Re-sync the invite tracker if bot's been offline<br/>

If the bot has gone offline before, run this command to ensure the bot is tracking the right invites.<br/>

Will also remove all server invites that have expired or disappeared.<br/>
 - Usage: `,hellohook invite sync`
### ,hellohook invite remove
Remove a custom invite-based welcome<br/>

Please input only the ##### part of your <https://discord.gg/#####> invite.<br/>
 - Usage: `,hellohook invite remove <inviteLink>`
Extended Arg Info
> ### inviteLink: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
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
Extended Arg Info
> ### GreetOrLeave: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### TrueOrFalse: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
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
 - Usage: `,hellohook setleave <DiscohookJSON>`
Extended Arg Info
> ### DiscohookJSON: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,hellohook reset
⚠️ Reset all settings<br/>
 - Usage: `,hellohook reset <TypeTrueToConfirm>`
Extended Arg Info
> ### TypeTrueToConfirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```