MadTranslate
============

Translate things into lots of languages then back to English!

This will defiantly have some funny moments... Take everything with a pinch of salt!

# <@1275521742961508432>madtranslateinfo

 - Usage: `<@1275521742961508432>madtranslateinfo`


# <@1275521742961508432>madtranslate
Translate something into lots of languages, then back to English!<br/>

**Examples:**<br/>
- `<@1275521742961508432>mtrans This is a sentence.`<br/>
- `<@1275521742961508432>mtrans 25 Here's another one.`<br/>

At the bottom of the output embed is a count-seed pair. You can use this with<br/>
the `mtransseed` command to use the same language set.<br/>
 - Usage: `<@1275521742961508432>madtranslate [count=15] <text_to_translate>`
 - Aliases: `mtranslate and mtrans`
Extended Arg Info
> ### count: Optional[int] = 15
> ```
> A number without decimal places.
> ```
> ### text_to_translate: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


# <@1275521742961508432>mtransseed
Use a count-seed pair to (hopefully) get reproducible results.<br/>

They may be unreproducible if Google Translate changes its translations.<br/>

The count-seed pair is obtained from the main command, `mtrans`, in the embed footer.<br/>

**Examples:**<br/>
- `<@1275521742961508432>mtrans 15-111111 This is a sentence.`<br/>
- `<@1275521742961508432>mtrans 25-000000 Here's another one.`<br/>
 - Usage: `<@1275521742961508432>mtransseed <count_seed> <text_to_translate>`
Extended Arg Info
> ### count_seed: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text_to_translate: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


