# Bingo Help

### bingoset

**Description:** Commands for setting bingo settings

**Usage:** `<@1275521742961508432>bingoset`

### bingoset tiles

**Description:** Set the tiles for the servers bingo cards.

`tiles` - Separate each tile with `;`

**Usage:** `<@1275521742961508432>bingoset tiles`

### bingoset background

**Description:** Set the colour of the Bingo card background.

`colour` - must be a hex colour code

**Usage:** `<@1275521742961508432>bingoset background`

### bingoset watermark

**Description:** Add a watermark image to the bingo card

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.

**Usage:** `<@1275521742961508432>bingoset watermark`

### bingoset reset

**Description:** Reset a users bingo card or reset the whole servers bingo card.

**Usage:** `<@1275521742961508432>bingoset reset`

### bingoset clear

**Description:** Clear out the current bingo cards tiles.

**Usage:** `<@1275521742961508432>bingoset clear`

### bingoset text

**Description:** Set the colour of the text.

`colour` - must be a hex colour code

**Usage:** `<@1275521742961508432>bingoset text`

### bingoset box

**Description:** Set the colour of the Bingo card boxes border.

`colour` - must be a hex colour code

**Usage:** `<@1275521742961508432>bingoset box`

### bingoset bgtile

**Description:** Set the background image (tiled).

This will override the background colour if set as it will attempt
to tile the image over the entire background.

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.

**Usage:** `<@1275521742961508432>bingoset bgtile`

### bingoset settings

**Description:** Show the current bingo card settings

**Usage:** `<@1275521742961508432>bingoset settings`

### bingoset name

**Description:** Set the name of the current bingo card.

`name` - the name you want to use for the current bingo card.

**Usage:** `<@1275521742961508432>bingoset name`

### bingoset stamp

**Description:** Set the colour of the "stamp" that fills the box.

`colour` - must be a hex colour code

**Usage:** `<@1275521742961508432>bingoset stamp`

### bingoset icon

**Description:** Add an icon image to the bingo card

`[image_url]` - Must be an image url with `.jpg` or `.png` extension.

**Usage:** `<@1275521742961508432>bingoset icon`

### bingoset bingo

**Description:** Set the "BINGO" of the board.

`bingo` - The word to use for bingo. Must be exactly 5 characters.

**Usage:** `<@1275521742961508432>bingoset bingo`

### bingoset seed

**Description:** Set an additional seed to the randomness of players cards.

`seed` - A number that is added to the player ID used to
seed their card.

Use this to shuffle everyone's card while keeping the exact
same tiles for a game of bingo. Default is 0.

**Usage:** `<@1275521742961508432>bingoset seed`

### bingo

**Description:** Generate a Bingo Card

`stamp` - Select the tile that you would like to stamp. If not
provided will just show your current bingo card.

**Usage:** `<@1275521742961508432>bingo`

