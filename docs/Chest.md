# Chest Help

### chestset

**Description:** Configure the chest game

**Usage:** `<@1275521742961508432>chestset`

### chestset version

**Description:** Shows the version of the cog.

**Usage:** `<@1275521742961508432>chestset version`

### chestset channel

**Description:** Set the channel for the chest game.

Use the command again to disable chest from spawning.

**Usage:** `<@1275521742961508432>chestset channel`

### chestset owner

**Description:** Group owner commands.

**Usage:** `<@1275521742961508432>chestset owner`

### chestset owner toggle

**Description:** Toggle whether you want to use image(s) in spawn/claim embed or not.

Default is Disabled.

**Usage:** `<@1275521742961508432>chestset owner toggle`

### chestset owner emoji

**Description:** Change the default emoji on the button.

Leave blank to reset back to default.
Note that your bot must share the same server as the emoji for the custom emoji to work.

**Usage:** `<@1275521742961508432>chestset owner emoji`

### chestset owner image

**Description:** Set a new default image.

Args:
    ctx (discord.Context): The command context.
    image_type (str): The type of image to update (spawn, claim or fail).
    image (str, optional): The URL of the image or None if an attachment is provided. Defaults to None.

**Usage:** `<@1275521742961508432>chestset owner image`

### chestset owner rate

**Description:** Change the fail rate to a different.

Default is 30% fail rate.

**Example**:
- `[p]chestset rate 40` This will make you fail 40% of time to get coins.

**Arguments**:
- `<fail_rate>` The number of whichever % you want users to fail.
    - Cannot be longer than 100 and less than 1.

**Usage:** `<@1275521742961508432>chestset owner rate`

### chestset owner reset

**Description:** Manage the chest game resets.

**Usage:** `<@1275521742961508432>chestset owner reset`

### chestset owner reset resetsetting

**Description:** Reset back to default setting

**Usage:** `<@1275521742961508432>chestset owner reset resetsetting`

### chestset owner reset resetdb

**Description:** Reset the database.

**Usage:** `<@1275521742961508432>chestset owner reset resetdb`

### chestset owner reset resetguilddb

**Description:** Reset the database for a specific guild.

**Usage:** `<@1275521742961508432>chestset owner reset resetguilddb`

### chestset owner credit

**Description:** Change how much credits users can get from claiming.

Default is 5,000. (it random select between 1 and 5,000)

**Usage:** `<@1275521742961508432>chestset owner credit`

### chestset owner debug

**Description:** Debug the database.

This will show all the records in the database table for debugging purposes.
It will show the guild_id and the next_chest_time for each record.

**Usage:** `<@1275521742961508432>chestset owner debug`

### chestset role

**Description:** Set the role for the chest game.

Use the command again to disable chest from spawning.

**Usage:** `<@1275521742961508432>chestset role`

### chestset settings

**Description:** Show current settings

**Usage:** `<@1275521742961508432>chestset settings`

