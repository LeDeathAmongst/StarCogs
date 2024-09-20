# MadTranslate Help

### madtranslate

**Description:** Translate something into lots of languages, then back to English!

**Examples:**
- `[p]mtrans This is a sentence.`
- `[p]mtrans 25 Here's another one.`

At the bottom of the output embed is a count-seed pair. You can use this with
the `mtransseed` command to use the same language set.

**Usage:** `<@1275521742961508432>madtranslate`

### mtransseed

**Description:** Use a count-seed pair to (hopefully) get reproducible results.

They may be unreproducible if Google Translate changes its translations.

The count-seed pair is obtained from the main command, `mtrans`, in the embed footer.

**Examples:**
- `[p]mtrans 15-111111 This is a sentence.`
- `[p]mtrans 25-000000 Here's another one.`

**Usage:** `<@1275521742961508432>mtransseed`

