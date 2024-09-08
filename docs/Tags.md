# Tags Help

### tagsettings

**Description:** Manage Tags cog settings.

**Usage:** `<@1275521742961508432>tagsettings`

### tagsettings limit

**Description:** Change the global and guild limit for tags.

**Usage:** `<@1275521742961508432>tagsettings limit`

### tagsettings limit global

**Description:** Change the global limit for tags.

**Usage:** `<@1275521742961508432>tagsettings limit global`

### tagsettings limit guild

**Description:** Change the guild limit for tags.

**Usage:** `<@1275521742961508432>tagsettings limit guild`

### tagsettings block

**Description:** Manage custom TagScript blocks.

**Usage:** `<@1275521742961508432>tagsettings block`

### tagsettings block remove

**Description:** Remove a custom block from the TagScript interpreter.

**Usage:** `<@1275521742961508432>tagsettings block remove`

### tagsettings block add

**Description:** Add a custom block to the TagScript interpreter.

The passed code must return a block class that inherits from `TagScriptEngine.Block`.

**Usage:** `<@1275521742961508432>tagsettings block add`

### tagsettings block list

**Description:** List all custom blocks in the TagScript interpreter.

**Usage:** `<@1275521742961508432>tagsettings block list`

### tagsettings block show

**Description:** Show the code of a custom block.

**Usage:** `<@1275521742961508432>tagsettings block show`

### tagsettings settings

**Description:** View Tags settings.

**Usage:** `<@1275521742961508432>tagsettings settings`

### tagsettings dotparam

**Description:** Toggle the TagScript parsing style.

If `dot_parameter` is enabled, TagScript blocks will parse like this:
`{declaration.parameter:payload}`
instead of:
`{declaration(parameter):payload}`

**Usage:** `<@1275521742961508432>tagsettings dotparam`

### tagsettings async

**Description:** Toggle using the asynchronous TagScript interpreter.

If you aren't a developer or don't know what this is, there's no reason for you to change it.

**Usage:** `<@1275521742961508432>tagsettings async`

### migratealias

**Description:** Migrate the Alias cog's global and server aliases into tags.

This converts all aliases created with the Alias cog into tags with command blocks.
This action cannot be undone.

**Example:**
`[p]migratealias`

**Usage:** `<@1275521742961508432>migratealias`

### migratecustomcom

**Description:** Migrate the CustomCommand cog's server commands into tags.

This converts all custom commands created into tags with the command text as TagScript.
Randomized commands are converted into random blocks.
Commands with converters are converted into indexed args blocks.
This action cannot be undone.

**Example:**
`[p]migratecustomcom`

**Usage:** `<@1275521742961508432>migratecustomcom`

### invoketag

**Description:** Manually invoke a tag with its name and arguments.

Restricting this command with permissions in servers will restrict all members from invoking tags.

**Examples:**
`[p]invoketag searchitem trophy`
`[p]invoketag donate`

**Usage:** `<@1275521742961508432>invoketag`

### tags

**Description:** View all tags and aliases.

This command will show global tags if run in DMs.

**Example:**
`[p]tags`

**Usage:** `<@1275521742961508432>tags`

### tag

**Description:** Tag management with TagScript.

These commands use TagScriptEngine.
Read the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/) to learn how to use TagScript blocks.

**Usage:** `<@1275521742961508432>tag`

### tag edit

**Description:** Edit a tag's TagScript.

The passed tagscript will replace the tag's current tagscript.
View the [TagScript docs](https://seina-cogs.readthedocs.io/en/latest/blocks.html) to find information on how to write valid tagscript.

**Example:**
`[p]tag edit rickroll Never gonna give you up!`

**Usage:** `<@1275521742961508432>tag edit`

### tag usage

**Description:** See tag usage stats.

**Example:**
`[p]tag usage`

**Usage:** `<@1275521742961508432>tag usage`

### tag process

**Description:** Process a temporary Tag without storing.

This differs from `[p]tag run` as it creates a fake tag and properly handles actions for all blocks.
The `{args}` block is not supported.

**Example:**
`[p]tag run {require(Admin):You must be admin to use this tag.} Congrats on being an admin!`

**Usage:** `<@1275521742961508432>tag process`

### tag alias

**Description:**         Add an alias for a tag.

        Adding an alias to the tag will make the tag invokable using the alias or the tag name.
        In the example below, running `[p]donation` will invoke the `donate` tag.
​
        **Example:**
        `[p]tag alias donate donation`

**Usage:** `<@1275521742961508432>tag alias`

### tag info

**Description:** Show information about a tag.

You can view meta information for a tag on this server or a global tag.
If a tag on this server has the same name as a global tag, it will show the server tag.

**Example:**
`[p]tag info notsupport`

**Usage:** `<@1275521742961508432>tag info`

### tag pastebin

**Description:** Add a tag with a Pastebin link.

**Example:**
`[p]tag pastebin starwarsopeningcrawl https://pastebin.com/CKjn6uYv`

**Usage:** `<@1275521742961508432>tag pastebin`

### tag add

**Description:** Add a tag with TagScript.

[Tag usage guide](https://seina-cogs.readthedocs.io/en/latest/tags/blocks.html#usage)

**Example:**
`[p]tag add lawsofmotion {embed(title):Newton's Laws of motion}
{embed(description): According to all known laws of aviation, there is no way a bee should be able to fly.}`

**Usage:** `<@1275521742961508432>tag add`

### tag remove

**Description:** Permanently delete a tag.

If you want to remove a tag's alias, use `[p]tag unalias`.

**Example:**
`[p]tag remove RickRoll`

**Usage:** `<@1275521742961508432>tag remove`

### tag docs

**Description:** Search the TagScript documentation for a block.

https://seina-cogs.readthedocs.io/en/latest/

**Example:**
`[p]tag docs embed`

**Usage:** `<@1275521742961508432>tag docs`

### tag run

**Description:** Execute TagScript without storing.

The variables and actions fields display debugging information.

**Example:**
`[p]tag run {#:yes,no}`

**Usage:** `<@1275521742961508432>tag run`

### tag append

**Description:** Add text to a tag's TagScript.

**Example:**
`[p]tag append rickroll Never gonna let you down!`

**Usage:** `<@1275521742961508432>tag append`

### tag raw

**Description:** Get a tag's raw content.

The sent TagScript will be escaped from Discord style formatting characters.

**Example:**
`[p]tag raw noping`

**Usage:** `<@1275521742961508432>tag raw`

### tag list

**Description:** View all stored tags on this server.

To view info on a specific tag, use `[p]tag info`.

**Example:**
`[p]tag list`

**Usage:** `<@1275521742961508432>tag list`

### tag backup

**Description:** Backup all the tag data for your server.

**Usage:** `<@1275521742961508432>tag backup`

### tag search

**Description:** Search for tags by name.

**Example:**
`[p]tag search notsupport`

**Usage:** `<@1275521742961508432>tag search`

### tag restore

**Description:** Restore all tag data for your server.

This command will restore all data from the backup file.
This command will also delete all the previously made tags if
not present in the backup file.

You can pass a message ID, a ChannelID-MessageID pair, or a message link
to the `message` argument.
Alternatively, if you want to reply to a message, pass anything to the
message argument while replying to a message.

**Usage:** `<@1275521742961508432>tag restore`

### tag global

**Description:** Global Tag management with TagScript.

These commands use TagScriptEngine.
Read the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/) to learn how to use TagScript blocks.

**Usage:** `<@1275521742961508432>tag global`

### tag global edit

**Description:** Edit a global tag's TagScript.

The passed tagscript will replace the global tag's current tagscript.
View the [TagScript docs](https://seina-cogs.readthedocs.io/en/latest/blocks.html) to find information on how to write valid tagscript.

**Example:**
`[p]tag global edit rickroll Never gonna give you up!`

**Usage:** `<@1275521742961508432>tag global edit`

### tag global list

**Description:** View all stored global tags on this server.

To view info on a specific global tag, use `[p]tag global info`.

**Example:**
`[p]tag global list`

**Usage:** `<@1275521742961508432>tag global list`

### tag global usage

**Description:** See global tag usage stats.

**Example:**
`[p]tag global usage`

**Usage:** `<@1275521742961508432>tag global usage`

### tag global append

**Description:** Add text to a global tag's TagScript.

**Example:**
`[p]tag global append rickroll Never gonna let you down!`

**Usage:** `<@1275521742961508432>tag global append`

### tag global raw

**Description:** Get a global tag's raw content.

The sent TagScript will be escaped from Discord style formatting characters.

**Example:**
`[p]tag global raw noping`

**Usage:** `<@1275521742961508432>tag global raw`

### tag global pastebin

**Description:** Add a global tag with a Pastebin link.

**Example:**
`[p]tag global pastebin starwarsopeningcrawl https://pastebin.com/CKjn6uYv`

**Usage:** `<@1275521742961508432>tag global pastebin`

### tag global alias

**Description:** Add an alias for a global tag.

        Adding an alias to the global tag will make the global tag invokable using the alias or the global tag name.
        In the example below, running `[p]donation` will invoke the `donate` global tag.
​
        **Example:**
        `[p]tag global alias donate donation`

**Usage:** `<@1275521742961508432>tag global alias`

### tag global remove

**Description:** Permanently delete a global tag.

If you want to remove a global tag's alias, use `[p]tag global unalias`.

**Example:**
`[p]tag global remove RickRoll`

**Usage:** `<@1275521742961508432>tag global remove`

### tag global search

**Description:** Search for global tags by name.

**Example:**
`[p]tag global search notsupport`

**Usage:** `<@1275521742961508432>tag global search`

### tag global backup

**Description:** Backup all the global tag data.

**Usage:** `<@1275521742961508432>tag global backup`

### tag global restore

**Description:** No description provided.

**Usage:** `<@1275521742961508432>tag global restore`

### tag global unalias

**Description:** Remove an alias for a global tag.

​The global tag will still be able to be used under its original name.
You can delete the original global tag with the `[p]tag global remove` command.

**Example:**
`global tag unalias donate donation`

**Usage:** `<@1275521742961508432>tag global unalias`

### tag global add

**Description:** Add a global tag with TagScript.

[Global Tag usage guide](https://seina-cogs.readthedocs.io/en/latest/global tags/blocks.html#usage)

**Example:**
`[p]tag global add lawsofmotion {embed(title):Newton's Laws of motion}
{embed(description): According to all known laws of aviation, there is no way a bee should be able to fly.}`

**Usage:** `<@1275521742961508432>tag global add`

### tag unalias

**Description:** Remove an alias for a tag.

​The tag will still be able to be used under its original name.
You can delete the original tag with the `[p]tag remove` command.

**Example:**
`tag unalias donate donation`

**Usage:** `<@1275521742961508432>tag unalias`

