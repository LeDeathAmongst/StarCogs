Tools for Managing Custom Emojis

# <@1275521742961508432>emojitools
Various tools for managing custom emojis in servers.<br/>

`<@1275521742961508432>emojitools add` has various tools to add emojis to the current server.<br/>
`<@1275521742961508432>emojitools delete` lets you remove emojis from the server.<br/>
`<@1275521742961508432>emojitools tozip` returns an instant `.zip` archive of emojis (w/o saving a folder permanently).<br/>
`<@1275521742961508432>emojitools save` allows you to save emojis to folders **in the cog data path**: this requires storage!<br/>
 - Usage: `<@1275521742961508432>emojitools`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## <@1275521742961508432>emojitools save
Save Custom Emojis to Folders<br/>

**IMPORTANT**: this **will** save folders to the cog data path, requiring storage in the machine the bot is hosted on.<br/>
The folders will be accessible to admin across all servers with access to this cog.<br/>
The other `EmojiTools` features that do **NOT** require storage, so disable this command group if you wish.<br/>
For large public bots, it is highly recommended to restrict usage of or disable this command group.<br/>
 - Usage: `<@1275521742961508432>emojitools save`
 - Restricted to: `ADMIN`
### <@1275521742961508432>emojitools save emojis
Save to a folder the specified custom emojis (can be from any server).<br/>
 - Usage: `<@1275521742961508432>emojitools save emojis <folder_name> <emojis>`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### folder_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *emojis: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>emojitools save getzip
Zip and upload an EmojiTools folder.<br/>
 - Usage: `<@1275521742961508432>emojitools save getzip <folder_number>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### folder_number: int
> ```
> A number without decimal places.
> ```
### <@1275521742961508432>emojitools save remove
Remove an EmojiTools folder.<br/>
 - Usage: `<@1275521742961508432>emojitools save remove <folder_number>`
 - Cooldown: `1 per 60.0 seconds`
Extended Arg Info
> ### folder_number: int
> ```
> A number without decimal places.
> ```
### <@1275521742961508432>emojitools save folders
List all your saved EmojiTools folders.<br/>
 - Usage: `<@1275521742961508432>emojitools save folders`
### <@1275521742961508432>emojitools save server
Save to a folder all custom emojis from this server (folder name defaults to server name).<br/>
 - Usage: `<@1275521742961508432>emojitools save server [folder_name=None]`
 - Cooldown: `1 per 60.0 seconds`
Extended Arg Info
> ### folder_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>emojitools add
Add Custom Emojis to Server<br/>
 - Usage: `<@1275521742961508432>emojitools add`
### <@1275521742961508432>emojitools add fromreaction
Add an emoji to this server from a specific reaction on a message.<br/>
 - Usage: `<@1275521742961508432>emojitools add fromreaction <specific_reaction> <message> [new_name=None]`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### specific_reaction: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
> ### new_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>emojitools add emojis
Add some emojis to this server.<br/>
 - Usage: `<@1275521742961508432>emojitools add emojis <emojis>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### *emojis: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>emojitools add fromzip
Add some emojis to this server from a provided .zip archive.<br/>

The `.zip` archive should extract to a folder, which contains files in the formats `.png`, `.jpg`, or `.gif`.<br/>
You can also use the `<@1275521742961508432>emojitools tozip` command to get a zip archive, extract it, remove unnecessary emojis, then re-zip and upload.<br/>
 - Usage: `<@1275521742961508432>emojitools add fromzip`
 - Restricted to: `ADMIN`
 - Cooldown: `1 per 60.0 seconds`
### <@1275521742961508432>emojitools add fromimage
Add an emoji to this server from a provided image.<br/>

The attached image should be in one of the following formats: `.png`, `.jpg`, or `.gif`.<br/>
 - Usage: `<@1275521742961508432>emojitools add fromimage [name=None]`
 - Restricted to: `ADMIN`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>emojitools add allreactionsfrom
Add emojis to this server from all reactions in a message.<br/>
 - Usage: `<@1275521742961508432>emojitools add allreactionsfrom <message>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
### <@1275521742961508432>emojitools add emoji
Add an emoji to this server (leave `name` blank to use the emoji's original name).<br/>
 - Usage: `<@1275521742961508432>emojitools add emoji <emoji> [name=None]`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### emoji: discord.partial_emoji.PartialEmoji
> Converts to a :class:`~discord.PartialEmoji`.
> 
>     This is done by extracting the animated flag, name and ID from the emoji.
> 
>     
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>emojitools delete
Delete Server Custom Emojis<br/>
 - Usage: `<@1275521742961508432>emojitools delete`
 - Aliases: `remove`
### <@1275521742961508432>emojitools delete all
Delete all specific custom emojis from the server.<br/>
 - Usage: `<@1275521742961508432>emojitools delete all <enter_true_to_confirm>`
 - Cooldown: `1 per 60.0 seconds`
Extended Arg Info
> ### enter_true_to_confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### <@1275521742961508432>emojitools delete emojis
Delete custom emojis from the server.<br/>
 - Usage: `<@1275521742961508432>emojitools delete emojis <emoji_names>`
 - Aliases: `emoji`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### *emoji_names: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
## <@1275521742961508432>emojitools info
Get info about a custom emoji from this server.<br/>
 - Usage: `<@1275521742961508432>emojitools info <emoji>`
Extended Arg Info
> ### emoji: discord.emoji.Emoji
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
## <@1275521742961508432>emojitools tozip
Get a `.zip` Archive of Emojis<br/>
 - Usage: `<@1275521742961508432>emojitools tozip`
### <@1275521742961508432>emojitools tozip server
Get a `.zip` archive of all custom emojis in the server.<br/>

The returned `.zip` archive can be used for the `<@1275521742961508432>emojitools add fromzip` command.<br/>
 - Usage: `<@1275521742961508432>emojitools tozip server`
 - Cooldown: `1 per 60.0 seconds`
### <@1275521742961508432>emojitools tozip emojis
Get a `.zip` archive of the provided emojis.<br/>

The returned `.zip` archive can be used for the `<@1275521742961508432>emojitools add fromzip` command.<br/>
 - Usage: `<@1275521742961508432>emojitools tozip emojis <emojis>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### *emojis: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>emojitools edit
Edit Custom Emojis in the Server<br/>
 - Usage: `<@1275521742961508432>emojitools edit`
### <@1275521742961508432>emojitools edit name
Edit the name of a custom emoji from this server.<br/>
 - Usage: `<@1275521742961508432>emojitools edit name <emoji> <name>`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### emoji: discord.emoji.Emoji
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>emojitools edit roles
Edit the roles to which the usage of a custom emoji from this server is restricted.<br/>
 - Usage: `<@1275521742961508432>emojitools edit roles <emoji> <roles>`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### emoji: discord.emoji.Emoji
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
