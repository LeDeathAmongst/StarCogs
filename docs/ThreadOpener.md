A cog to open continuous threads to messages in a channel.

# ,threadopener
Manage ThreadOpener settings.<br/>
 - Usage: `,threadopener`
 - Restricted to: `ADMIN`
 - Cooldown: `1 per 10.0 seconds`
 - Checks: `server_only`
## ,threadopener blacklist
Base command for Thread Opener blacklists.<br/>

**Commands:**<br/>
- `,threadopener blacklist users <add_or_remove> <users>`<br/>
- `,threadopener blacklist roles <add_or_remove> <roles>`<br/>
 - Usage: `,threadopener blacklist`
 - Aliases: `bl`
### ,threadopener blacklist roles
Add or remove roles for your server's blacklist.<br/>

**Arguments:**<br/>
- `<add_or_remove>` should be either `add` to add roles or `remove` to remove roles.<br/>
- `<users>` roles to be added.<br/>

**Example:**<br/>
- `,threadopener blacklist roles add @members`<br/>
- `,threadopener blacklist roles remove @members`<br/>

**Note:**<br/>
- You can add or remove multiple roles at once.<br/>
- You can also use role ID instead of mentioning the role.<br/>
 - Usage: `,threadopener blacklist roles <add_or_remove> <roles>`
 - Aliases: `role`
### ,threadopener blacklist list
View the blacklist.<br/>

**Arguments:**<br/>
` `<users_or_roles>` should be either ``users`` to view the user blacklist<br/>
    or `roles` to view the role blacklist.<br/>
 - Usage: `,threadopener blacklist list [users_or_roles=users]`
### ,threadopener blacklist users
Add or remove users for your server's blacklist.<br/>

**Arguments:**<br/>
- `<add_or_remove>` should be either `add` to add users or `remove` to remove users.<br/>
- `<users>` users to be added.<br/>

**Example:**<br/>
- `,threadopener blacklist users add @inthedark.org`<br/>
- `,threadopener blacklist users remove @inthedark.org`<br/>

**Note:**<br/>
- You can add or remove multiple users at once.<br/>
- You can also use user ID instead of mentioning the user.<br/>
 - Usage: `,threadopener blacklist users <add_or_remove> <users>`
 - Aliases: `user, members, and member`
## ,threadopener slowmode
Change the slowmode of threads.<br/>

- Use `0` to dsiable slowmode delay in threads.<br/>
 - Usage: `,threadopener slowmode <amount>`
 - Aliases: `slow`
## ,threadopener channels
Add or remove channels for your server.<br/>

**Arguments:**<br/>
- `<add_or_remove>` should be either `add` to add channels or `remove` to remove channels.<br/>
- `<channels>` channels to be added.<br/>

**Example:**<br/>
- `,threadopener channels add #channel`<br/>
- `,threadopener channels remove #channel`<br/>

**Note:**<br/>
- You can add or remove multiple channels at once.<br/>
- You can also use channel ID instead of mentioning the channel.<br/>
 - Usage: `,threadopener channels <add_or_remove> <channels>`
 - Aliases: `channel`
## ,threadopener showsettings
Show ThreadOpener settings.<br/>
 - Usage: `,threadopener showsettings`
 - Aliases: `ss and show`
## ,threadopener allowbots
Allow/Disallow bots from auto-creating threads using Thread Opener.<br/>
 - Usage: `,threadopener allowbots <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,threadopener archive
Change the archive duration of threads.<br/>

- Use `0` to disable auto archive duration of threads.<br/>
 - Usage: `,threadopener archive <amount>`
## ,threadopener name
Change the default thread name for ThreadOpener.<br/>

(Supports TagScript)<br/>

**Attributes:**<br/>
- `{server}`: [Your server/server.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)<br/>
- `{author}`: [Author of the thread.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{created}`: Formatted time string of when the thread was created.<br/>
- `{counter}`: Counter of how created thread. (Everytime a thread is created using ThreadOpener the counter goes up by 1.)<br/>

**Example:**<br/>
- `,threadopener name {author(name)}:{created}:{counter}`<br/>
- `,threadopener name {author(name)}-{counter}`<br/>
 - Usage: `,threadopener name [tagscript]`
 - Aliases: `defaultname, default, and dn`
## ,threadopener message
Manage thread opener notifications when they are opened.<br/>
 - Usage: `,threadopener message`
### ,threadopener message buttons
Toggle buttons from the thread opener notification message. (Enabled by default.)<br/>
 - Usage: `,threadopener message buttons <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### ,threadopener message set
Change the thread opener notification message.<br/>

(Supports Tagscript)<br/>

**Blocks:**<br/>
- [Assugnment Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block)<br/>
- [If Block](https://seina-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#if-block)<br/>
- [Embed Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block)<br/>
- [Command Block](https://seina-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#command-block)<br/>

**Variable:**<br/>
- `{server}`: [Your server/server.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block)<br/>
- `{author}`: [Author of the message.](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block)<br/>
- `{color}`: Starfire's default color.<br/>

**Example:**<br/>
```
{embed(description):Welcome to the thread.}
{embed(thumbnail):{member(avatar)}}
{embed(color):{color}}
```
 - Usage: `,threadopener message set [message]`
### ,threadopener message toggle
Toggle the thread opener notification message.<br/>
 - Usage: `,threadopener message toggle <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,threadopener toggle
Toggle ThreadOpener enable or disable.<br/>
 - Usage: `,threadopener toggle <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
