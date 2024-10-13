AltMarker
=========

Mark alt accounts

# ,alt
Mark or unmark an alt acount<br/>
 - Usage: `,alt`
 - Aliases: `alts`


## ,alt mark
Mark an alt account<br/>
 - Usage: `,alt mark <member> <alt>`
 - Aliases: `add`
Extended Arg Info
> ### member: discord.member.Member
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
> ### alt: discord.member.Member
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


## ,alt unmark
Unmark an alt account<br/>
 - Usage: `,alt unmark <member> <alt>`
 - Restricted to: `MOD`
 - Aliases: `remove and delete`
Extended Arg Info
> ### member: discord.member.Member
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
> ### alt: discord.member.Member
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


## ,alt get
Get alts of a member<br/>
 - Usage: `,alt get <member>`
 - Restricted to: `MOD`
Extended Arg Info
> ### member: discord.member.Member
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


# ,amset
Set altmarker settings<br/>
 - Usage: `,amset`
 - Restricted to: `ADMIN`


## ,amset notify
Toggle notification on moderation actions<br/>
 - Usage: `,amset notify [channel=None]`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


