Battle in a Pokemon Duel with another member of your server.

# ,pokemonduel
Battle in a Pokemon Duel with another member of your server.<br/>
 - Usage: `,pokemonduel <opponent>`
 - Aliases: `pokeduel`
Extended Arg Info
> ### opponent: discord.member.Member
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
## ,pokemonduel party
Manage your party of pokemon.<br/>
 - Usage: `,pokemonduel party`
### ,pokemonduel party pokecord
Create a party of pokemon imported from Pokecord.<br/>
 - Usage: `,pokemonduel party pokecord <ids>`
Extended Arg Info
> ### *ids: int
> ```
> A number without decimal places.
> ```
### ,pokemonduel party list
View the pokemon currently in your party.<br/>
 - Usage: `,pokemonduel party list`
 - Aliases: `view`
### ,pokemonduel party set
Set your party of pokemon.<br/>

In order to set your party, you will need to create a team on Pokemon Showdown Team Builder.<br/>
1. Go to the [Team Builder site](https://play.pokemonshowdown.com/teambuilder).<br/>
2. Click the "New Team" button.<br/>
3. Select the format "Anything Goes".<br/>
4. Use the "Add Pokemon" button to create a new pokemon.<br/>
5. Pick its moves, ability, gender, level, etc.<br/>
6. Repeat steps 4 and 5 for up to 6 total pokemon<br/>
7. On the team view, select the "Import/Export" button at the TOP.<br/>
8. Copy the text provided, and pass that to this command.<br/>
 - Usage: `,pokemonduel party set <pokemon_data>`
Extended Arg Info
> ### pokemon_data
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,pokemonduel inverse
Battle in an Inverse Duel with another member of your server.<br/>
 - Usage: `,pokemonduel inverse <opponent>`
Extended Arg Info
> ### opponent: discord.member.Member
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
# ,pokemonduelset
Config options for pokemon duels.<br/>
 - Usage: `,pokemonduelset`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## ,pokemonduelset thread
Set if a thread should be created per-game to contain game messages.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `,pokemonduelset thread [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```