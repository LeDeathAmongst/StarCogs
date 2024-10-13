Gmail
=====

Send emails using your Gmail account.

Use `[p]gmailhelp` for help getting started.

# /email (Slash Command)
Send an email<br/>
 - Usage: `/email <sender> <recipient> <subject> <message> [attachment1] [attachment2] [attachment3]`
 - `sender:` (Required) …
 - `recipient:` (Required) …
 - `subject:` (Required) …
 - `message:` (Required) …
 - `attachment1:` (Optional) …
 - `attachment2:` (Optional) …
 - `attachment3:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### sender: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### recipient: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### subject: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### attachment1: discord.message.Attachment
> - Autocomplete: False
> - Default: None
> 
> …
> 
> Represents an attachment from Discord.
> 
>     
> ### attachment2: discord.message.Attachment
> - Autocomplete: False
> - Default: None
> 
> …
> 
> Represents an attachment from Discord.
> 
>     
> ### attachment3: discord.message.Attachment
> - Autocomplete: False
> - Default: None
> 
> …
> 
> Represents an attachment from Discord.
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>email
Send an email<br/>

Attach files to the command to send them as attachments<br/>
 - Usage: `<@1275521742961508432>email <sender> <recipient> <subject> <message>`
=======
# ,email
Send an email<br/>

Attach files to the command to send them as attachments<br/>
 - Usage: `,email <sender> <recipient> <subject> <message>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `server_only`
Extended Arg Info
> ### sender: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### recipient: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### subject: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>addemail
Add an email account<br/>
 - Usage: `<@1275521742961508432>addemail`
=======
# ,addemail
Add an email account<br/>
 - Usage: `,addemail`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Aliases: `addgmail`
 - Checks: `server_only`


<<<<<<< HEAD
# <@1275521742961508432>editemail
Edit an email account<br/>
 - Usage: `<@1275521742961508432>editemail <email>`
=======
# ,editemail
Edit an email account<br/>
 - Usage: `,editemail <email>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Aliases: `editgmail`
 - Checks: `server_only`
Extended Arg Info
> ### email: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>deleteemail
Delete an email account<br/>
 - Usage: `<@1275521742961508432>deleteemail <email>`
=======
# ,deleteemail
Delete an email account<br/>
 - Usage: `,deleteemail <email>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### email: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>gmailroles
Set the roles allowed to send emails<br/>
 - Usage: `<@1275521742961508432>gmailroles <roles>`
=======
# ,gmailroles
Set the roles allowed to send emails<br/>
 - Usage: `,gmailroles <roles>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


<<<<<<< HEAD
# <@1275521742961508432>gmailsettings
View the email settings for the server<br/>
 - Usage: `<@1275521742961508432>gmailsettings`
 - Checks: `server_only`


# <@1275521742961508432>gmailhelp
Get instructions for setting up Gmail<br/>
 - Usage: `<@1275521742961508432>gmailhelp`
=======
# ,gmailsettings
View the email settings for the server<br/>
 - Usage: `,gmailsettings`
 - Checks: `server_only`


# ,gmailhelp
Get instructions for setting up Gmail<br/>
 - Usage: `,gmailhelp`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `gmailsetup`
 - Checks: `server_only`


