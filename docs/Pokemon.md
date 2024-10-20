This is pokemon related stuff cog.<br/>- Can you guess Who's That Pokémon?<br/>- Fetch Pokémon cards based on Pokémon Trading Card Game (a.k.a Pokémon TCG).<br/>- Get information about a Pokémon.

# ,whosthatpokemon (Hybrid Command)
Guess Who's that Pokémon in 30 seconds!<br/>

You can optionally specify generation from `gen1` to `gen8` only.<br/>

**Example:**<br/>
- `,whosthatpokemon` - This will start a new Generation.<br/>
- `,whosthatpokemon gen1` - This will pick any pokemon from generation 1 for you to guess.<br/>

**Arguments:**<br/>
- `[generation]` - Where you choose any generation from gen 1 to gen 9.<br/>
 - Usage: `,whosthatpokemon [generation=None]`
 - Slash Usage: `/whosthatpokemon [generation=None]`
 - Aliases: `wtp`
 - Cooldown: `1 per 30.0 seconds`
# ,tcgcard (Hybrid Command)
Fetch Pokémon cards based on Pokémon Trading Card Game (a.k.a Pokémon TCG).<br/>

**Example:**<br/>
- `,tcgcard pikachu` - returns information about pikachu's cards.<br/>

**Arguments:**<br/>
- `<query>` - The pokemon you want to search for.<br/>
 - Usage: `,tcgcard <query>`
 - Slash Usage: `/tcgcard <query>`
 - Cooldown: `1 per 5.0 seconds`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,pokeinfo (Hybrid Command)
Get information about a Pokémon.<br/>

**Example:**<br/>
- `,pokeinfo pikachu` - returns information about Pikachu.<br/>

**Arguments:**<br/>
- `<pokemon>` - The Pokémon you want to search for.<br/>
    - If you dont know names, you can check the list from the [national pokedex](https://pokemondb.net/pokedex/national).<br/>
 - Usage: `,pokeinfo <pokemon>`
 - Slash Usage: `/pokeinfo <pokemon>`
 - Cooldown: `1 per 5.0 seconds`
Extended Arg Info
> ### pokemon: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```