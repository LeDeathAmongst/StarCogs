EmojiTools
==========

Tools for Managing Custom Emojis

# ,emojitools
Various tools for managing custom emojis in servers.<br/>

`,emojitools add` has various tools to add emojis to the current server.<br/>
`,emojitools delete` lets you remove emojis from the server.<br/>
`,emojitools tozip` returns an instant `.zip` archive of emojis (w/o saving a folder permanently).<br/>
`,emojitools save` allows you to save emojis to folders **in the cog data path**: this requires storage!<br/>
 - Usage: `,emojitools`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,emojitools save
Save Custom Emojis to Folders<br/>

**IMPORTANT**: this **will** save folders to the cog data path, requiring storage in the machine the bot is hosted on.<br/>
The folders will be accessible to admin across all servers with access to this cog.<br/>
The other `EmojiTools` features that do **NOT** require storage, so disable this command group if you wish.<br/>
For large public bots, it is highly recommended to restrict usage of or disable this command group.<br/>
 - Usage: `,emojitools save`
 - Restricted to: `ADMIN`


### ,emojitools save server
Save to a folder all custom emojis from this server (folder name defaults to server name).<br/>
 - Usage: `,emojitools save server [folder_name=None]`
 - Cooldown: `1 per 60.0 seconds`
Extended Arg Info
> ### folder_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,emojitools save emojis
Save to a folder the specified custom emojis (can be from any server).<br/>
 - Usage: `,emojitools save emojis <folder_name> <emojis>`
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


### ,emojitools save folders
List all your saved EmojiTools folders.<br/>
 - Usage: `,emojitools save folders`


### ,emojitools save getzip
Zip and upload an EmojiTools folder.<br/>
 - Usage: `,emojitools save getzip <folder_number>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### folder_number: int
> ```
> A number without decimal places.
> ```


### ,emojitools save remove
Remove an EmojiTools folder.<br/>
 - Usage: `,emojitools save remove <folder_number>`
 - Cooldown: `1 per 60.0 seconds`
Extended Arg Info
> ### folder_number: int
> ```
> A number without decimal places.
> ```


## ,emojitools tozip
Get a `.zip` Archive of Emojis<br/>
 - Usage: `,emojitools tozip`


### ,emojitools tozip emojis
Get a `.zip` archive of the provided emojis.<br/>

The returned `.zip` archive can be used for the `,emojitools add fromzip` command.<br/>
 - Usage: `,emojitools tozip emojis <emojis>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### *emojis: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,emojitools tozip server
Get a `.zip` archive of all custom emojis in the server.<br/>

The returned `.zip` archive can be used for the `,emojitools add fromzip` command.<br/>
 - Usage: `,emojitools tozip server`
 - Cooldown: `1 per 60.0 seconds`


## ,emojitools edit
Edit Custom Emojis in the Server<br/>
 - Usage: `,emojitools edit`


### ,emojitools edit roles
Edit the roles to which the usage of a custom emoji from this server is restricted.<br/>
 - Usage: `,emojitools edit roles <emoji> <roles>`
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


### ,emojitools edit name
Edit the name of a custom emoji from this server.<br/>
 - Usage: `,emojitools edit name <emoji> <name>`
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


## ,emojitools add
Add Custom Emojis to Server<br/>
 - Usage: `,emojitools add`


### ,emojitools add fromimage
Add an emoji to this server from a provided image.<br/>

The attached image should be in one of the following formats: `.png`, `.jpg`, or `.gif`.<br/>
 - Usage: `,emojitools add fromimage [name=None]`
 - Restricted to: `ADMIN`
 - Cooldown: `1 per 15.0 seconds`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,emojitools add allreactionsfrom
Add emojis to this server from all reactions in a message.<br/>
 - Usage: `,emojitools add allreactionsfrom <message>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     


### ,emojitools add emoji
Add an emoji to this server (leave `name` blank to use the emoji's original name).<br/>
 - Usage: `,emojitools add emoji <emoji> [name=None]`
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


### ,emojitools add fromzip
Add some emojis to this server from a provided .zip archive.<br/>

The `.zip` archive should extract to a folder, which contains files in the formats `.png`, `.jpg`, or `.gif`.<br/>
You can also use the `,emojitools tozip` command to get a zip archive, extract it, remove unnecessary emojis, then re-zip and upload.<br/>
 - Usage: `,emojitools add fromzip`
 - Restricted to: `ADMIN`
 - Cooldown: `1 per 60.0 seconds`


### ,emojitools add fromreaction
Add an emoji to this server from a specific reaction on a message.<br/>
 - Usage: `,emojitools add fromreaction <specific_reaction> <message> [new_name=None]`
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


### ,emojitools add emojis
Add some emojis to this server.<br/>
 - Usage: `,emojitools add emojis <emojis>`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### *emojis: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,emojitools info
Get info about a custom emoji from this server.<br/>
 - Usage: `,emojitools info <emoji>`
Extended Arg Info
> ### emoji: discord.emoji.Emoji
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     


## ,emojitools delete
Delete Server Custom Emojis<br/>
 - Usage: `,emojitools delete`
 - Aliases: `remove`


### ,emojitools delete all
Delete all specific custom emojis from the server.<br/>
 - Usage: `,emojitools delete all <enter_true_to_confirm>`
 - Cooldown: `1 per 60.0 seconds`
Extended Arg Info
> ### enter_true_to_confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


### ,emojitools delete emojis
Delete custom emojis from the server.<br/>
 - Usage: `,emojitools delete emojis <emoji_names>`
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


