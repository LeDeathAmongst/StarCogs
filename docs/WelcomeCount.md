A special welcome cog which keeps a daily count of new users.<br/><br/>Idea came from Twentysix's version of Red on the official Red-DiscordBot<br/>server.

# ,welcomecount
Manage settings for WelcomeCount.<br/>
 - Usage: `,welcomecount`
 - Restricted to: `ADMIN`
 - Aliases: `wcount`
 - Checks: `server_only`
## ,welcomecount message
Set the bot's welcome message.<br/>

This message can be formatted using these parameters:<br/>
    mention - Mention the user who joined<br/>
    username - The user's display name<br/>
    server - The name of the server<br/>
    count - The number of users who joined today.<br/>
    plural - Empty if `count` is 1. 's' otherwise.<br/>
    total - The total number of users in the server.<br/>
To format the welcome message with the above parameters, include them<br/>
in your message surrounded by curly braces {}.<br/>
 - Usage: `,welcomecount message <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,welcomecount toggle
Toggle welcome messages in this channel.<br/>
 - Usage: `,welcomecount toggle`
## ,welcomecount deletelast
Toggle deleting the previous welcome message in this channel.<br/>

When enabled, the last message is deleted *only* if it was sent on<br/>
the same day as the new welcome message.<br/>
 - Usage: `,welcomecount deletelast`
## ,welcomecount joinrole
Set a role which a user must receive before they're welcomed.<br/>

This means that, instead of the welcome message being sent when<br/>
the user joins the server, the welcome message will be sent when<br/>
they receive a particular role.<br/>

Use `,welcomecount joinrole disable` to revert to the default<br/>
behaviour.<br/>
 - Usage: `,welcomecount joinrole <role>`
Extended Arg Info
> ### role: Union[discord.role.Role, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
