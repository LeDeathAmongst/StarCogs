# EmbedUtils Help

### embed

**Description:** Post a simple embed with a color, a title and a description.

Put the title in quotes if it contains spaces.
If you provide a message, it will be edited.

**Usage:** `<@1275521742961508432>embed`

### embed json

**Description:** Post embeds from valid JSON.

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).
You can use an [**embeds creator**](https://embedutils.com/) to get a JSON payload.

If you provide a message, it will be edited.
You can use an attachment and the command `[p]embed yamlfile` will be invoked automatically.

**Usage:** `<@1275521742961508432>embed json`

### embed yaml

**Description:** Post embeds from valid YAML.

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).

If you provide a message, it will be edited.
You can use an attachment and the command `[p]embed yamlfile` will be invoked automatically.

**Usage:** `<@1275521742961508432>embed yaml`

### embed fromfile

**Description:** Post an embed from a valid JSON file (upload it).

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).
You can use an [**embeds creator**](https://embedutils.com/) to get a JSON payload.

If you provide a message, it will be edited.

**Usage:** `<@1275521742961508432>embed fromfile`

### embed download

**Description:** Download a JSON file for a message's embed(s).

The message must have at least one embed.
You can specify an index (starting by 0) if you want to include only one of the embeds.
The content of the message already sent is included if no index is specified.

**Usage:** `<@1275521742961508432>embed download`

### embed postwebhook

**Description:** Post stored embeds with a webhook.

**Usage:** `<@1275521742961508432>embed postwebhook`

### embed edit

**Description:** Edit a message sent by [botname].

It would be better to use the `message` parameter of all the other commands.

**Usage:** `<@1275521742961508432>embed edit`

### embed list

**Description:** Get info about a stored embed.

**Usage:** `<@1275521742961508432>embed list`

### embed poststored

**Description:** Post stored embeds.

**Usage:** `<@1275521742961508432>embed poststored`

### embed unstore

**Description:** Remove a stored embed.

**Usage:** `<@1275521742961508432>embed unstore`

### embed downloadstored

**Description:** Download a JSON file for a stored embed.

**Usage:** `<@1275521742961508432>embed downloadstored`

### embed yamlfile

**Description:** Post an embed from a valid YAML file (upload it).

If you provide a message, it will be edited.

**Usage:** `<@1275521742961508432>embed yamlfile`

### embed store

**Description:** Store an embed.

Put the name in quotes if it is multiple words.
The `locked` argument specifies whether the embed should be locked to mod and superior only (guild level) or bot owners only (global level).

**Usage:** `<@1275521742961508432>embed store`

### embed dashboard

**Description:** Get the link to the Dashboard.

**Usage:** `<@1275521742961508432>embed dashboard`

### embed migratefromphen

**Description:** Migrate stored embeds from EmbedUtils by Phen.

**Usage:** `<@1275521742961508432>embed migratefromphen`

### embed info

**Description:** Get info about a stored embed.

**Usage:** `<@1275521742961508432>embed info`

### embed message

**Description:** Post embed(s) from an existing message.

The message must have at least one embed.
You can specify an index (starting by 0) if you want to send only one of the embeds.
The content of the message already sent is included if no index is specified.

If you provide a message, it will be edited.

**Usage:** `<@1275521742961508432>embed message`

### embed pastebin

**Description:** Post embeds from a GitHub/Gist/Pastebin/Hastebin link containing valid JSON.

This must be in the format expected by [**this Discord documentation**](https://discord.com/developers/docs/resources/channel#embed-object).
Here's an example: [**this example**](https://gist.github.com/AAA3A-AAA3A/3c9772b34a8ebc09b3b10018185f4cd4).

If you provide a message, it will be edited.

**Usage:** `<@1275521742961508432>embed pastebin`

