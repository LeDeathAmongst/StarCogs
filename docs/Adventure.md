Adventure, derived from the Goblins Adventure cog by locastan.

## /adventure rebirth (Slash Command)
Resets your character level and increases your rebirths by 1.<br/>
 - Usage: `/adventure rebirth`
 - Checks: `Server Only`
## /adventure negaverse (Slash Command)
This will send you to fight a nega-member!<br/>
 - Usage: `/adventure negaverse <offering>`
 - `offering:` (Required) …

 - Checks: `Server Only`
Extended Arg Info
> ### offering: int
> - Autocomplete: False
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /adventure loot (Slash Command)
This opens one of your precious treasure chests.<br/>
 - Usage: `/adventure loot [box_type] [number]`
 - `box_type:` (Optional) …
 - `number:` (Optional) …

Extended Arg Info
> ### box_type: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### number: int
> - Autocomplete: False
> - Default: 1
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /adventure convert (Slash Command)
Convert normal, rare or epic chests.<br/>
 - Usage: `/adventure convert <box_rarity> [amount]`
 - `box_rarity:` (Required) …
 - `amount:` (Optional) …

Extended Arg Info
> ### box_rarity: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### amount: int
> - Autocomplete: False
> - Default: 1
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /adventure aleaderboard (Slash Command)
Print the leaderboard.<br/>
 - Usage: `/adventure aleaderboard [show_global]`
 - `show_global:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### show_global: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /adventure scoreboard (Slash Command)
Print the scoreboard.<br/>
 - Usage: `/adventure scoreboard [show_global]`
 - `show_global:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### show_global: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /adventure nvsb (Slash Command)
Print the negaverse scoreboard.<br/>
 - Usage: `/adventure nvsb [show_global]`
 - `show_global:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### show_global: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /adventure wscoreboard (Slash Command)
Print the weekly scoreboard.<br/>
 - Usage: `/adventure wscoreboard [show_global]`
 - `show_global:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### show_global: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /adventure heroclass (Slash Command)
Allows you to select a class if you are level 10 or above.<br/>
 - Usage: `/adventure heroclass [class] [action]`
 - `class:` (Optional) …
 - `action:` (Optional) …

Extended Arg Info
> ### clz: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### action: str
> - Autocomplete: False
> - Default: None
> - Choices: ['info']
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventure pet
[Ranger Class Only]<br/>
 - Usage: `,adventure pet`
### /adventure pet find (Slash Command)
[Ranger Class Only]<br/>
 - Usage: `/adventure pet find`
### /adventure pet forage (Slash Command)
Use your pet to forage for items!<br/>
 - Usage: `/adventure pet forage`
### /adventure pet free (Slash Command)
Free your pet :cry:<br/>
 - Usage: `/adventure pet free`
## /adventure bless (Slash Command)
[Cleric Class Only]<br/>
 - Usage: `/adventure bless`
## /adventure insight (Slash Command)
[Psychic Class Only]<br/>
 - Usage: `/adventure insight`
 - Checks: `Server Only`
## /adventure rage (Slash Command)
[Berserker Class Only]<br/>
 - Usage: `/adventure rage`
## /adventure focus (Slash Command)
[Wizard Class Only]<br/>
 - Usage: `/adventure focus`
## /adventure music (Slash Command)
[Bard Class Only]<br/>
 - Usage: `/adventure music`
## /adventure forge (Slash Command)
[Tinkerer Class Only]<br/>
 - Usage: `/adventure forge`
## /adventure skill (Slash Command)
This allows you to spend skillpoints.<br/>
 - Usage: `/adventure skill [skill] [amount]`
 - `skill:` (Optional) …
 - `amount:` (Optional) …

Extended Arg Info
> ### skill: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### amount: int
> - Autocomplete: False
> - Default: 1
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /adventure setinfo (Slash Command)
Show set bonuses for the specified set.<br/>
 - Usage: `/adventure setinfo [set_name]`
 - `set_name:` (Optional) …

Extended Arg Info
> ### set_name: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /adventure stats (Slash Command)
This draws up a character sheet of you or an optionally specified member.<br/>
 - Usage: `/adventure stats [user]`
 - `user:` (Optional) …

Extended Arg Info
> ### user: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> …
> 
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
## /adventure unequip (Slash Command)
This stashes a specified equipped item into your backpack.<br/>
 - Usage: `/adventure unequip <item>`
 - `item:` (Required) …

Extended Arg Info
> ### item: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /adventure equip (Slash Command)
This equips an item from your backpack.<br/>
 - Usage: `/adventure equip <item>`
 - `item:` (Required) …

Extended Arg Info
> ### item: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventure backpack
This shows the contents of your backpack.<br/>
 - Usage: `,adventure backpack`
### /adventure backpack show (Slash Command)
This shows the contents of your backpack.<br/>
 - Usage: `/adventure backpack show [show_diff] [rarity] [slot]`
 - `show_diff:` (Optional) …
 - `rarity:` (Optional) …
 - `slot:` (Optional) …

Extended Arg Info
> ### show_diff: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### rarity: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### slot: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /adventure backpack equip (Slash Command)
Equip an item from your backpack.<br/>
 - Usage: `/adventure backpack equip <equip_item>`
 - `equip_item:` (Required) …

Extended Arg Info
> ### equip_item: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /adventure backpack eset (Slash Command)
Equip all parts of a set that you own.<br/>
 - Usage: `/adventure backpack eset <set_name>`
 - `set_name:` (Required) …

Extended Arg Info
> ### set_name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /adventure backpack disassemble (Slash Command)
Disassemble items from your backpack.<br/>
 - Usage: `/adventure backpack disassemble <backpack_items>`
 - `backpack_items:` (Required) …

Extended Arg Info
> ### backpack_items: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /adventure backpack sellall (Slash Command)
Sell all items in your backpack. Optionally specify rarity or slot.<br/>
 - Usage: `/adventure backpack sellall [rarity] [slot]`
 - `rarity:` (Optional) …
 - `slot:` (Optional) …

Extended Arg Info
> ### rarity: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### slot: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /adventure backpack sell (Slash Command)
Sell an item from your backpack.<br/>
 - Usage: `/adventure backpack sell <item>`
 - `item:` (Required) …

Extended Arg Info
> ### item: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /adventure backpack trade (Slash Command)
Trade an item from your backpack to another user.<br/>
 - Usage: `/adventure backpack trade <buyer> <item> [asking]`
 - `buyer:` (Required) …
 - `item:` (Required) …
 - `asking:` (Optional) …

Extended Arg Info
> ### buyer: discord.member.Member
> - Autocomplete: False
> 
> …
> 
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
> ### item: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### asking: int
> - Autocomplete: False
> - Default: 1000
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /adventure start (Slash Command)
This will send you on an adventure!<br/>
 - Usage: `/adventure start [challenge]`
 - `challenge:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### challenge: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,themeset
[Admin] Modify themes.<br/>
 - Usage: `,themeset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## ,themeset add
[Owner] Add/Update objects in the specified theme.<br/>
 - Usage: `,themeset add`
 - Restricted to: `BOT_OWNER`
### ,themeset add pet
[Owner] Add/Update a pet object in the specified theme.<br/>

Usage: `,themeset add pet theme++name++bonus_multiplier++required_cha++crit_chance++always_crit`<br/>

`theme` is the one-word theme folder name. The default is `default`.<br/>
`name` is the name of the pet.<br/>
`bonus_multiplier` is a number between `1.00` and `2.00` for the reward bonus percentage on a successful adventure.<br/>
`required_cha` is the required charisma/diplomacy level that the ranger must overcome to catch the pet - usually between `1` and `500`.<br/>
`crit_chance` is the chance to have a critical strike, between `1` and `100` percent.<br/>
`always_crit` is `True` or `False` for whether the pet will always have a critical strike when attacking.<br/>
 - Usage: `,themeset add pet <pet_data>`
### ,themeset add monster
[Owner] Add/Update a monster object in the specified theme.<br/>

Usage: `,themeset add monster theme++name++hp++dipl++pdef++mdef++cdef++boss++image`<br/>

`theme` is the one-word theme folder name. The default is `default`.<br/>
`name` is the name of the monster.<br/>
`hp` is the base amount of hp the monster has.<br/>
`dipl` is the base amount of charisma/diplomacy the monster has.<br/>
`pdef` is the percentage of physical resistance, `0.0` to `100.0`.<br/>
`mdef` is the percentage of magic resistance, `0.0` to `100.0`.<br/>
`cdef` is the percentage of charisma/diplomacy resistance, `0.0` to `100.0`.<br/>
`boss` is whether the monster is a boss, determined with `True` or `False`.<br/>
`image` is a URL for an image of the monster.<br/>
 - Usage: `,themeset add monster <theme_data>`
## ,themeset delete
[Owner] Remove objects in the specified theme.<br/>
 - Usage: `,themeset delete`
 - Restricted to: `BOT_OWNER`
 - Aliases: `del, rem, and remove`
### ,themeset delete monster
[Owner] Remove a monster object in the specified theme.<br/>

The default theme is `default`.<br/>
 - Usage: `,themeset delete monster <theme> <monster>`
Extended Arg Info
> ### theme: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### monster: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,themeset delete pet
[Owner] Remove a pet object in the specified theme.<br/>

The default theme is `default`.<br/>
 - Usage: `,themeset delete pet <theme> <pet>`
Extended Arg Info
> ### theme: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### pet: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,themeset list
[Admin] Show custom objects in the specified theme.<br/>
 - Usage: `,themeset list`
 - Aliases: `show`
### ,themeset list monster
[Admin] Show monster objects in the specified theme.<br/>

The default theme is `default`.<br/>
This will only display custom monsters added through the `themeset` command.<br/>
 - Usage: `,themeset list monster <theme>`
Extended Arg Info
> ### theme: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### ,themeset list pet
[Admin] Show pet objects in the specified theme.<br/>

The default theme is `default`.<br/>
This will only display custom pets added through the `themeset` command.<br/>
 - Usage: `,themeset list pet <theme>`
Extended Arg Info
> ### theme: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,rebirth (Hybrid Command)
Resets your character level and increases your rebirths by 1.<br/>
 - Usage: `,rebirth`
 - Slash Usage: `/rebirth`
 - Checks: `server_only`
# ,negaverse (Hybrid Command)
This will send you to fight a nega-member!<br/>
 - Usage: `,negaverse <offering>`
 - Slash Usage: `/negaverse <offering>`
 - Aliases: `nv`
 - Cooldown: `1 per 3600.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### offering: int
> ```
> A number without decimal places.
> ```
# ,loot (Hybrid Command)
This opens one of your precious treasure chests.<br/>

Use the box rarity type with the command: normal, rare, epic, legendary, ascended or set.<br/>
 - Usage: `,loot [box_type=None] [number=1]`
 - Slash Usage: `/loot [box_type=None] [number=1]`
 - Cooldown: `1 per 4.0 seconds`
Extended Arg Info
> ### number: int = 1
> ```
> A number without decimal places.
> ```
# ,convert (Hybrid Command)
Convert normal, rare or epic chests.<br/>

Trade 25 normal chests for 1 rare chest.<br/>
Trade 25 rare chests for 1 epic chest.<br/>
Trade 25 epic chests for 1 legendary chest.<br/>
 - Usage: `,convert <box_rarity> [amount=1]`
 - Slash Usage: `/convert <box_rarity> [amount=1]`
 - Cooldown: `1 per 4.0 seconds`
Extended Arg Info
> ### amount: int = 1
> ```
> A number without decimal places.
> ```
# ,loadout
Set up gear sets or loadouts.<br/>
 - Usage: `,loadout`
 - Aliases: `loadouts`
## ,loadout delete
Delete a saved loadout.<br/>
 - Usage: `,loadout delete <name>`
 - Aliases: `del, rem, and remove`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,loadout save
Save your current equipment as a loadout.<br/>
 - Usage: `,loadout save <name>`
 - Aliases: `update`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,loadout show
Show saved loadouts.<br/>
 - Usage: `,loadout show [name=None]`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,loadout equip
Equip a saved loadout.<br/>
 - Usage: `,loadout equip <name>`
 - Aliases: `load`
 - Cooldown: `1 per 600.0 seconds`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,aleaderboard (Hybrid Command)
Print the leaderboard.<br/>
 - Usage: `,aleaderboard [show_global=False]`
 - Slash Usage: `/aleaderboard [show_global=False]`
 - Checks: `server_only`
Extended Arg Info
> ### show_global: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,scoreboard (Hybrid Command)
Print the scoreboard.<br/>
 - Usage: `,scoreboard [show_global=False]`
 - Slash Usage: `/scoreboard [show_global=False]`
 - Checks: `server_only`
Extended Arg Info
> ### show_global: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,nvsb (Hybrid Command)
Print the negaverse scoreboard.<br/>
 - Usage: `,nvsb [show_global=False]`
 - Slash Usage: `/nvsb [show_global=False]`
 - Checks: `server_only`
Extended Arg Info
> ### show_global: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,wscoreboard (Hybrid Command)
Print the weekly scoreboard.<br/>
 - Usage: `,wscoreboard [show_global=False]`
 - Slash Usage: `/wscoreboard [show_global=False]`
 - Checks: `server_only`
Extended Arg Info
> ### show_global: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,atransfer
Transfer currency between players/economies.<br/>
 - Usage: `,atransfer`
 - Checks: `has_separated_economy`
## ,atransfer withdraw
Convert gold to bank currency.<br/>
 - Usage: `,atransfer withdraw <amount>`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,atransfer player
Transfer gold to another player.<br/>
 - Usage: `,atransfer player <amount> <player>`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
> ### player: discord.member.Member
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
## ,atransfer give
[Owner] Give gold to adventurers.<br/>
 - Usage: `,atransfer give <amount> <players>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
> ### *players: discord.member.Member
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
## ,atransfer deposit
Convert bank currency to gold.<br/>
 - Usage: `,atransfer deposit <amount>`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
# ,mysets
Show your sets.<br/>
 - Usage: `,mysets`
# ,apayday
Get some free gold.<br/>
 - Usage: `,apayday`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `has_separated_economy`
# ,give
[Owner] Commands to add things to players' inventories.<br/>
 - Usage: `,give`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`
## ,give item
[Owner] Adds a custom item to a specified member.<br/>

Item names containing spaces must be enclosed in double quotes.<br/>
available stats are:<br/>
- `attack:` or `att:` defaults to 0.<br/>
- `charisma:` or `diplo:` or `cha:` defaults to 0.<br/>
- `intelligence:` or `int:` defaults to 0.<br/>
- `dexterity:` or `dex:` defaults to 0.<br/>
- `luck:` defaults to 0.<br/>
- `rarity:` (one of `normal`, `rare`, `epic`, `legendary`, `set`, `forged`, or `event`) defaults to normal.<br/>
- `degrade:` (Set to -1 to never degrade on rebirths) defaults to 3.<br/>
- `level:` or `lvl:` defaults to the calculated level required based on stats.<br/>
- `slot:` (one of `head`, `neck`, `chest`, `gloves`, `belt`, `legs`, `boots`, `left`, `right`<br/>
  `ring`, `charm`, `two handed`) defaults to left.<br/>
Example:<br/>
```
,give item @locastan "fine dagger" att: 1 charisma: 1 degrade: -1 level: 100 rarity: rare slot: twohanded
```
Will give locastan a 1 attack 1 charisma `.fine_dagger`.<br/>
 - Usage: `,give item <user> <item_name> <stats>`
Extended Arg Info
> ### user: Union[discord.member.Member, discord.user.User]
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
> ### item_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,give loot
[Owner] Give treasure chest(s) to all specified users.<br/>
 - Usage: `,give loot <loot_type> [users=None] [number=1]`
Extended Arg Info
> ### number: int = 1
> ```
> A number without decimal places.
> ```
# ,devcooldown
[Dev] Resets the after-adventure cooldown in this server.<br/>
 - Usage: `,devcooldown`
 - Restricted to: `BOT_OWNER`
# ,makecart
[Dev] Force a cart to appear.<br/>
 - Usage: `,makecart [stockcount=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### stockcount: Optional[int] = None
> ```
> A number without decimal places.
> ```
# ,genitems
[Dev] Generate random items.<br/>
 - Usage: `,genitems <rarity> <slot> [num=1]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### num: int = 1
> ```
> A number without decimal places.
> ```
# ,copyuser
[Owner] Copy another members data to yourself.<br/>

Note this overrides your current data.<br/>
 - Usage: `,copyuser <user_id>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
# ,devrebirth
[Dev] Set multiple users rebirths and level.<br/>
 - Usage: `,devrebirth [rebirth_level=1] [character_level=1] [users=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### rebirth_level: int = 1
> ```
> A number without decimal places.
> ```
> ### character_level: int = 1
> ```
> A number without decimal places.
> ```
# ,devreset
[Dev] Reset the skill cooldown for multiple users.<br/>
 - Usage: `,devreset <users>`
 - Restricted to: `BOT_OWNER`
# ,adventureseed
[Owner] Shows information about an adventure seed<br/>
 - Usage: `,adventureseed <seed>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### seed: Union[str, int]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,adventurestats
[Owner] Show all current adventures.<br/>
 - Usage: `,adventurestats [server=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### server: Optional[discord.server.Guild] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
# ,heroclass (Hybrid Command)
Allows you to select a class if you are level 10 or above.<br/>

For information on class use: `,heroclass classname info`.<br/>
 - Usage: `,heroclass [clz=None] [action=None]`
 - Slash Usage: `/heroclass [clz=None] [action=None]`
 - Cooldown: `1 per 7200.0 seconds`
# ,pet (Hybrid Command)
[Ranger Class Only]<br/>

This allows a Ranger to tame or set free a pet or send it foraging.<br/>
 - Usage: `,pet`
 - Slash Usage: `/pet`
 - Cooldown: `1 per 5.0 seconds`
## ,pet free (Hybrid Command)
Free your pet :cry:<br/>
 - Usage: `,pet free`
 - Slash Usage: `/pet free`
## ,pet forage (Hybrid Command)
Use your pet to forage for items!<br/>
 - Usage: `,pet forage`
 - Slash Usage: `/pet forage`
# ,bless (Hybrid Command)
[Cleric Class Only]<br/>

This allows a praying Cleric to add substantial bonuses for heroes fighting the battle.<br/>
 - Usage: `,bless`
 - Slash Usage: `/bless`
# ,insight (Hybrid Command)
[Psychic Class Only]<br/>
This allows a Psychic to expose the current enemy's weakeness to the party.<br/>
 - Usage: `,insight`
 - Slash Usage: `/insight`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `server_only`
# ,rage (Hybrid Command)
[Berserker Class Only]<br/>

This allows a Berserker to add substantial attack bonuses for one battle.<br/>
 - Usage: `,rage`
 - Slash Usage: `/rage`
# ,focus (Hybrid Command)
[Wizard Class Only]<br/>

This allows a Wizard to add substantial magic bonuses for one battle.<br/>
 - Usage: `,focus`
 - Slash Usage: `/focus`
# ,music (Hybrid Command)
[Bard Class Only]<br/>

This allows a Bard to add substantial diplomacy bonuses for one battle.<br/>
 - Usage: `,music`
 - Slash Usage: `/music`
# ,forge (Hybrid Command)
[Tinkerer Class Only]<br/>

This allows a Tinkerer to forge two items into a device. (1h cooldown)<br/>
 - Usage: `,forge`
 - Slash Usage: `/forge`
# ,skill (Hybrid Command)
This allows you to spend skillpoints.<br/>

`,skill attack/charisma/intelligence`<br/>
`,skill reset` Will allow you to reset your skill points for a cost.<br/>
 - Usage: `,skill [skill=None] [amount=1]`
 - Slash Usage: `/skill [skill=None] [amount=1]`
 - Cooldown: `1 per 2.0 seconds`
Extended Arg Info
> ### amount: int = 1
> ```
> A number without decimal places.
> ```
# ,setinfo (Hybrid Command)
Show set bonuses for the specified set.<br/>
 - Usage: `,setinfo [set_name]`
 - Slash Usage: `/setinfo [set_name]`
Extended Arg Info
> ### set_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,stats (Hybrid Command)
This draws up a character sheet of you or an optionally specified member.<br/>
 - Usage: `,stats [user]`
 - Slash Usage: `/stats [user]`
Extended Arg Info
> ### user: Union[discord.member.Member, discord.user.User] = None
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
# ,unequip (Hybrid Command)
This stashes a specified equipped item into your backpack.<br/>

Use `,unequip name of item` or `,unequip slot`<br/>
 - Usage: `,unequip <item>`
 - Slash Usage: `/unequip <item>`
# ,equip (Hybrid Command)
This equips an item from your backpack.<br/>
 - Usage: `,equip <item>`
 - Slash Usage: `/equip <item>`
# ,backpack (Hybrid Command)
This shows the contents of your backpack.<br/>

Give it a rarity and/or slot to filter what backpack items to show.<br/>

Selling:     `,backpack sell item_name`<br/>
Trading:     `,backpack trade @user price item_name`<br/>
Equip:       `,backpack equip item_name`<br/>
Sell All:    `,backpack sellall rarity slot`<br/>
Disassemble: `,backpack disassemble item_name`<br/>

Note: An item **degrade** level is how many rebirths it will last, before it is broken down.<br/>
 - Usage: `,backpack [show_diff=False] [rarity=None] [slot]`
 - Slash Usage: `/backpack [show_diff=False] [rarity=None] [slot]`
Extended Arg Info
> ### show_diff: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,backpack eset (Hybrid Command)
Equip all parts of a set that you own.<br/>
 - Usage: `,backpack eset <set_name>`
 - Slash Usage: `/backpack eset <set_name>`
 - Cooldown: `1 per 600.0 seconds`
Extended Arg Info
> ### set_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,backpack sellall (Hybrid Command)
Sell all items in your backpack. Optionally specify rarity or slot.<br/>
 - Usage: `,backpack sellall [rarity=None] [slot]`
 - Slash Usage: `/backpack sellall [rarity=None] [slot]`
## ,backpack equip (Hybrid Command)
Equip an item from your backpack.<br/>
 - Usage: `,backpack equip <equip_item>`
 - Slash Usage: `/backpack equip <equip_item>`
## ,backpack trade (Hybrid Command)
Trade an item from your backpack to another user.<br/>
 - Usage: `,backpack trade <buyer> [asking=1000] <item>`
 - Slash Usage: `/backpack trade <buyer> [asking=1000] <item>`
Extended Arg Info
> ### buyer: discord.member.Member
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
> ### asking: Optional[int] = 1000
> ```
> A number without decimal places.
> ```
## ,backpack sell (Hybrid Command)
Sell an item from your backpack.<br/>
 - Usage: `,backpack sell <item>`
 - Slash Usage: `/backpack sell <item>`
 - Cooldown: `3 per 60.0 seconds`
## ,backpack disassemble (Hybrid Command)
Disassemble items from your backpack.<br/>

This will provide a chance for a chest,<br/>
or the item might break while you are handling it...<br/>
 - Usage: `,backpack disassemble <backpack_items>`
 - Slash Usage: `/backpack disassemble <backpack_items>`
# ,ebackpack
This shows the contents of your backpack that can be equipped.<br/>

Give it a rarity and/or slot to filter what backpack items to show.<br/>

Note: An item **degrade** level is how many rebirths it will last, before it is broken down.<br/>
 - Usage: `,ebackpack [show_diff=False] [rarity=None] [slot]`
Extended Arg Info
> ### show_diff: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,cbackpack
Complex backpack management tools.<br/>

Please read the usage instructions [here](https://github.com/aikaterna/gobcog/blob/master/docs/cbackpack.md)<br/>
 - Usage: `,cbackpack`
## ,cbackpack show
This shows the contents of your backpack.<br/>

Please read the usage instructions [here](https://github.com/aikaterna/gobcog/blob/master/docs/cbackpack.md)<br/>
 - Usage: `,cbackpack show <query>`
## ,cbackpack disassemble
Disassemble items from your backpack.<br/>

This will provide a chance for a chest,<br/>
or the item might break while you are handling it...<br/>

Please read the usage instructions [here](https://github.com/aikaterna/gobcog/blob/master/docs/cbackpack.md)<br/>
 - Usage: `,cbackpack disassemble <query>`
## ,cbackpack sell
Sell items from your backpack.<br/>

Forged items cannot be sold using this command.<br/>

Please read the usage instructions [here](https://github.com/aikaterna/gobcog/blob/master/docs/cbackpack.md)<br/>
 - Usage: `,cbackpack sell <query>`
 - Cooldown: `3 per 60.0 seconds`
# ,adventureset
Setup various adventure settings.<br/>
 - Usage: `,adventureset`
 - Checks: `server_only`
## ,adventureset sepcurrency
[Owner] Toggle whether the currency should be separated from main bot currency.<br/>
 - Usage: `,adventureset sepcurrency`
 - Restricted to: `BOT_OWNER`
## ,adventureset showsettings
Display current settings.<br/>
 - Usage: `,adventureset showsettings`
 - Cooldown: `1 per 4.0 seconds`
 - Checks: `server_only`
## ,adventureset cartroom
[Admin] Lock carts to a specific text channel.<br/>
 - Usage: `,adventureset cartroom [room=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### room: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,adventureset remove
[Owner] Lets you remove an item from a user.<br/>

Use the full name of the item including the rarity characters like . or []  or {}.<br/>
 - Usage: `,adventureset remove <user> <full_item_name>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### user: Union[discord.member.Member, discord.user.User]
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
> ### full_item_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventureset dailybonus
[Owner] Set the daily xp and currency bonus.<br/>

**percentage** must be between 0% and 100%.<br/>
 - Usage: `,adventureset dailybonus <day> <percentage>`
 - Restricted to: `BOT_OWNER`
## ,adventureset embeds
[Admin] Set whether or not to use embeds for the adventure game.<br/>
 - Usage: `,adventureset embeds`
 - Restricted to: `ADMIN`
 - Aliases: `embed`
## ,adventureset locks
[Admin] Reset Adventure locks.<br/>
 - Usage: `,adventureset locks`
 - Restricted to: `ADMIN`
### ,adventureset locks user
[Owner] Reset a multiple adventurers lock.<br/>
 - Usage: `,adventureset locks user <users>`
 - Restricted to: `BOT_OWNER`
### ,adventureset locks adventure
[Admin] Reset the adventure game lock for the server.<br/>
 - Usage: `,adventureset locks adventure`
 - Checks: `server_only`
## ,adventureset economy
[Admin] Manages the adventure economy.<br/>
 - Usage: `,adventureset economy`
 - Checks: `check_global_setting_admin, server_only, and has_separated_economy`
### ,adventureset economy tax
[Owner] Set the tax thresholds.<br/>

**gold** must be positive<br/>
**tax** must be between 0 and 1.<br/>

Example: `,adventureset economy tax 10000,0.1 20000,0.2 ...`<br/>
 - Usage: `,adventureset economy tax <taxes>`
 - Restricted to: `BOT_OWNER`
### ,adventureset economy rate
[Owner] Set how much 1 bank credit is worth in adventure.<br/>

**rate_in**: Is how much gold you will get for 1 bank credit. Default is 10<br/>
**rate_out**: Is how much gold is needed to convert to 1 bank credit. Default is 11<br/>
 - Usage: `,adventureset economy rate <rate_in> <rate_out>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### rate_in: int
> ```
> A number without decimal places.
> ```
> ### rate_out: int
> ```
> A number without decimal places.
> ```
### ,adventureset economy withdraw
[Admin] Toggle whether users are allowed to withdraw from adventure currency to main currency.<br/>
 - Usage: `,adventureset economy withdraw`
### ,adventureset economy maxwithdraw
[Admin] Set how much players are allowed to withdraw.<br/>
 - Usage: `,adventureset economy maxwithdraw <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## ,adventureset globalcartname
[Owner] Set the default name of the cart.<br/>
 - Usage: `,adventureset globalcartname <name>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventureset advcooldown
[Admin] Changes the cooldown/gather time after an adventure.<br/>

Default is 120 seconds.<br/>
 - Usage: `,adventureset advcooldown <time_in_seconds>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### time_in_seconds: int
> ```
> A number without decimal places.
> ```
## ,adventureset cartchests
[Admin] Set whether or not to sell chests in the cart.<br/>
 - Usage: `,adventureset cartchests`
 - Restricted to: `BOT_OWNER`
 - Aliases: `chests`
## ,adventureset carttime
[Admin] Set the cooldown of the cart.<br/>
Time can be in seconds, minutes, hours, or days.<br/>
Examples: `1h 30m`, `2 days`, `300 seconds`<br/>
 - Usage: `,adventureset carttime <time>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventureset version
Display the version of adventure being used.<br/>
 - Usage: `,adventureset version`
## ,adventureset cartname
[Admin] Set the server's name of the cart.<br/>
 - Usage: `,adventureset cartname <name>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventureset theme
[Owner] Change the theme for adventure.<br/>

The default theme is `default`.<br/>
More info can be found at: <https://github.com/aikaterna/gobcog#make-your-own-adventure-theme><br/>
 - Usage: `,adventureset theme <theme>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### theme
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventureset restrict
[Owner] Set whether or not adventurers are restricted to one adventure at a time.<br/>
 - Usage: `,adventureset restrict`
 - Restricted to: `BOT_OWNER`
## ,adventureset rebirthcost
[Admin] Set what percentage of the user balance to charge for rebirths.<br/>

Unless the user's balance is under 1k, users that rebirth will be left with the base of 1k credits plus the remaining credit percentage after the rebirth charge.<br/>
 - Usage: `,adventureset rebirthcost <percentage>`
 - Checks: `check_global_setting_admin`
Extended Arg Info
> ### percentage: float
> ```
> A number with or without decimal places.
> ```
## ,adventureset god
[Admin] Set the server's name of the god.<br/>
 - Usage: `,adventureset god <name>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventureset easymode
[Owner] Set whether or not Adventure will be in easy mode.<br/>

Easy mode gives less rewards, but monster information is shown.<br/>
 - Usage: `,adventureset easymode`
 - Restricted to: `BOT_OWNER`
## ,adventureset cart
[Admin] Add or remove a text channel that the Trader cart can appear in.<br/>

If the channel is already in the list, it will be removed.<br/>
Use `,adventureset cart` with no arguments to show the channel list.<br/>
 - Usage: `,adventureset cart [channel]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## ,adventureset globalgod
[Owner] Set the default name of the god.<br/>
 - Usage: `,adventureset globalgod <name>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,adventureset clear
[Owner] Lets you clear multiple users character sheets.<br/>
 - Usage: `,adventureset clear <users>`
 - Restricted to: `BOT_OWNER`
# ,adventure (Hybrid Command)
This will send you on an adventure!<br/>

You play by reacting with the offered emojis.<br/>
 - Usage: `,adventure [challenge]`
 - Slash Usage: `/adventure [challenge]`
 - Aliases: `a`
 - Cooldown: `1 per 5.0 seconds`
 - Checks: `server_only`
