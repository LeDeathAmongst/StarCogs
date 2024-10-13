NoBot
=====

Filter messages from other bots

Some "Free" bots spam ads and links when using their commands, this cog fixes that.
Add a bot to the watchlist and add phrases to look for and if that phrase is found in the other bot's
message, this cog will delete them.

<<<<<<< HEAD
# <@1275521742961508432>nobot
Main setup command for NoBot<br/>
 - Usage: `<@1275521742961508432>nobot`


## <@1275521742961508432>nobot delfilter
Delete a filter<br/>
 - Usage: `<@1275521742961508432>nobot delfilter`


## <@1275521742961508432>nobot view
View NoBot settings<br/>
 - Usage: `<@1275521742961508432>nobot view`


## <@1275521742961508432>nobot delbot
Remove a bot from the filter list<br/>

If bot is no longer in the server, use its ID<br/>
 - Usage: `<@1275521742961508432>nobot delbot <bot>`
Extended Arg Info
> ### bot: Union[discord.member.Member, int]
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


## <@1275521742961508432>nobot addbot
Add a bot to the filter list<br/>
 - Usage: `<@1275521742961508432>nobot addbot <bot>`
=======
# ,nobot
Main setup command for NoBot<br/>
 - Usage: `,nobot`


## ,nobot view
View NoBot settings<br/>
 - Usage: `,nobot view`


## ,nobot addbot
Add a bot to the filter list<br/>
 - Usage: `,nobot addbot <bot>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### bot: discord.member.Member
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


<<<<<<< HEAD
## <@1275521742961508432>nobot addfilter
Add text context to match against the bot filter list, use phrases that match what the bot sends exactly<br/>
 - Usage: `<@1275521742961508432>nobot addfilter <message>`
=======
## ,nobot delfilter
Delete a filter<br/>
 - Usage: `,nobot delfilter`


## ,nobot addfilter
Add text context to match against the bot filter list, use phrases that match what the bot sends exactly<br/>
 - Usage: `,nobot addfilter <message>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### message
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
=======
## ,nobot delbot
Remove a bot from the filter list<br/>

If bot is no longer in the server, use its ID<br/>
 - Usage: `,nobot delbot <bot>`
Extended Arg Info
> ### bot: Union[discord.member.Member, int]
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


>>>>>>> 9e308722 (Revamped and Fixed)
