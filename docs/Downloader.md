Install community cogs made by Cog Creators.<br/><br/>Community cogs, also called third party cogs, are not included<br/>in the default Red install.<br/><br/>Community cogs come in repositories. Repos are a group of cogs<br/>you can install. You always need to add the creator's repository<br/>using the `[p]repo` command before you can install one or more<br/>cogs from the creator.

# <@1275521742961508432>pipinstall
Install a group of dependencies using pip.<br/>

Examples:<br/>
- `<@1275521742961508432>pipinstall bs4`<br/>
- `<@1275521742961508432>pipinstall py-cpuinfo psutil`<br/>

Improper usage of this command can break your bot, be careful.<br/>

**Arguments**<br/>

- `<deps...>` The package or packages you wish to install.<br/>
 - Usage: `<@1275521742961508432>pipinstall <deps>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### *deps: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>repo
Base command for repository management.<br/>
 - Usage: `<@1275521742961508432>repo`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>repo list
List all installed repos.<br/>
 - Usage: `<@1275521742961508432>repo list`
## <@1275521742961508432>repo info
Show information about a repo.<br/>

Example:<br/>
- `<@1275521742961508432>repo info 26-Cogs`<br/>

**Arguments**<br/>

- `<repo>` The name of the repo to show info about.<br/>
 - Usage: `<@1275521742961508432>repo info <repo>`
## <@1275521742961508432>repo delete
Remove repos and their files.<br/>

Examples:<br/>
- `<@1275521742961508432>repo delete 26-Cogs`<br/>
- `<@1275521742961508432>repo delete 26-Cogs Laggrons-Dumb-Cogs`<br/>

**Arguments**<br/>

- `<repos...>` The repo or repos to remove.<br/>
 - Usage: `<@1275521742961508432>repo delete <repos>`
 - Aliases: `remove and del`
## <@1275521742961508432>repo update
Update all repos, or ones of your choosing.<br/>

This will *not* update the cogs installed from those repos.<br/>

Examples:<br/>
- `<@1275521742961508432>repo update`<br/>
- `<@1275521742961508432>repo update 26-Cogs`<br/>
- `<@1275521742961508432>repo update 26-Cogs Laggrons-Dumb-Cogs`<br/>

**Arguments**<br/>

- `[repos...]` The name or names of repos to update. If omitted, all repos are updated.<br/>
 - Usage: `<@1275521742961508432>repo update <repos>`
## <@1275521742961508432>repo add
Add a new repo.<br/>

Examples:<br/>
- `<@1275521742961508432>repo add 26-Cogs https://github.com/Twentysix26/x26-Cogs`<br/>
- `<@1275521742961508432>repo add Laggrons-Dumb-Cogs https://github.com/retke/Laggrons-Dumb-Cogs v3`<br/>

Repo names can only contain characters A-z, numbers, underscores, hyphens, and dots (but they cannot start or end with a dot).<br/>

The branch will be the default branch if not specified.<br/>

**Arguments**<br/>

- `<name>` The name given to the repo.<br/>
- `<repo_url>` URL to the cog branch. Usually GitHub or GitLab.<br/>
- `[branch]` Optional branch to install cogs from.<br/>
 - Usage: `<@1275521742961508432>repo add <name> <repo_url> [branch=None]`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### repo_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### branch: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>cog
Base command for cog installation management commands.<br/>
 - Usage: `<@1275521742961508432>cog`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>cog checkforupdates
Check for available cog updates (including pinned cogs).<br/>

This command doesn't update cogs, it only checks for updates.<br/>
Use `<@1275521742961508432>cog update` to update cogs.<br/>
 - Usage: `<@1275521742961508432>cog checkforupdates`
## <@1275521742961508432>cog listpinned
List currently pinned cogs.<br/>
 - Usage: `<@1275521742961508432>cog listpinned`
## <@1275521742961508432>cog info
List information about a single cog.<br/>

Example:<br/>
- `<@1275521742961508432>cog info 26-Cogs defender`<br/>

**Arguments**<br/>

- `<repo>` The repo to get cog info from.<br/>
- `<cog>` The cog to get info on.<br/>
 - Usage: `<@1275521742961508432>cog info <repo> <cog_name>`
Extended Arg Info
> ### cog_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>cog unpin
Unpin cogs - this will remove the update lock from those cogs.<br/>

Examples:<br/>
- `<@1275521742961508432>cog unpin defender`<br/>
- `<@1275521742961508432>cog unpin updated_cog1 updated_cog2`<br/>

**Arguments**<br/>

- `<cogs...>` The cog or cogs to unpin. Must already be installed and pinned.<br/>
 - Usage: `<@1275521742961508432>cog unpin <cogs>`
## <@1275521742961508432>cog updateallfromrepos
Update all cogs from repos of your choosing.<br/>

Examples:<br/>
- `<@1275521742961508432>cog updateallfromrepos 26-Cogs`<br/>
- `<@1275521742961508432>cog updateallfromrepos True 26-Cogs`<br/>
- `<@1275521742961508432>cog updateallfromrepos Laggrons-Dumb-Cogs 26-Cogs`<br/>

**Arguments**<br/>

- `[reload]` Whether to reload cogs immediately after update or not.<br/>
- `<repos...>` The repo or repos to update all cogs from.<br/>
 - Usage: `<@1275521742961508432>cog updateallfromrepos <reload> <repos>`
Extended Arg Info
> ### reload: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>cog updatetoversion
Update all cogs, or ones of your choosing to chosen revision of one repo.<br/>

Note that update doesn't mean downgrade and therefore `revision`<br/>
has to be newer than the version that cog currently has installed. If you want to<br/>
downgrade the cog, uninstall and install it again.<br/>

See `<@1275521742961508432>cog installversion` for an explanation of `revision`.<br/>

Examples:<br/>
- `<@1275521742961508432>cog updatetoversion Broken-Repo e798cc268e199612b1316a3d1f193da0770c7016 cog_name`<br/>
- `<@1275521742961508432>cog updatetoversion True Broken-Repo 6107c0770ad391f1d3a6131b216991e862cc897e cog_name`<br/>

**Arguments**<br/>

- `[reload]` Whether to reload cogs immediately after update or not.<br/>
- `<repo>` The repo or repos to update all cogs from.<br/>
- `<revision>` The revision to update to.<br/>
- `[cogs...]` The cog or cogs to update.<br/>
 - Usage: `<@1275521742961508432>cog updatetoversion <reload> <repo> <revision> <cogs>`
Extended Arg Info
> ### reload: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### revision: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>cog list
List all available cogs from a single repo.<br/>

Example:<br/>
- `<@1275521742961508432>cog list 26-Cogs`<br/>

**Arguments**<br/>

- `<repo>` The repo to list cogs from.<br/>
 - Usage: `<@1275521742961508432>cog list <repo>`
## <@1275521742961508432>cog pin
Pin cogs - this will lock cogs on their current version.<br/>

Examples:<br/>
- `<@1275521742961508432>cog pin defender`<br/>
- `<@1275521742961508432>cog pin outdated_cog1 outdated_cog2`<br/>

**Arguments**<br/>

- `<cogs...>` The cog or cogs to pin. Must already be installed.<br/>
 - Usage: `<@1275521742961508432>cog pin <cogs>`
## <@1275521742961508432>cog install
Install a cog from the given repo.<br/>

Examples:<br/>
- `<@1275521742961508432>cog install 26-Cogs defender`<br/>
- `<@1275521742961508432>cog install Laggrons-Dumb-Cogs say roleinvite`<br/>

**Arguments**<br/>

- `<repo>` The name of the repo to install cogs from.<br/>
- `<cogs...>` The cog or cogs to install.<br/>
 - Usage: `<@1275521742961508432>cog install <repo> <cog_names>`
Extended Arg Info
> ### *cog_names: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## <@1275521742961508432>cog reinstallreqs
This command should not be used unless Red specifically asks for it.<br/>

This command will reinstall cog requirements and shared libraries for all installed cogs.<br/>

Red might ask the owner to use this when it clears contents of the lib folder<br/>
because of change in minor version of Python.<br/>
 - Usage: `<@1275521742961508432>cog reinstallreqs`
## <@1275521742961508432>cog update
Update all cogs, or ones of your choosing.<br/>

Examples:<br/>
- `<@1275521742961508432>cog update`<br/>
- `<@1275521742961508432>cog update True`<br/>
- `<@1275521742961508432>cog update defender`<br/>
- `<@1275521742961508432>cog update True defender`<br/>

**Arguments**<br/>

- `[reload]` Whether to reload cogs immediately after update or not.<br/>
- `[cogs...]` The cog or cogs to update. If omitted, all cogs are updated.<br/>
 - Usage: `<@1275521742961508432>cog update <reload> <cogs>`
Extended Arg Info
> ### reload: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## <@1275521742961508432>cog uninstall
Uninstall cogs.<br/>

You may only uninstall cogs which were previously installed<br/>
by Downloader.<br/>

Examples:<br/>
- `<@1275521742961508432>cog uninstall defender`<br/>
- `<@1275521742961508432>cog uninstall say roleinvite`<br/>

**Arguments**<br/>

- `<cogs...>` The cog or cogs to uninstall.<br/>
 - Usage: `<@1275521742961508432>cog uninstall <cogs>`
## <@1275521742961508432>cog installversion
Install a cog from the specified revision of given repo.<br/>

Revisions are "commit ids" that point to the point in the code when a specific change was made.<br/>
The latest revision can be found in the URL bar for any GitHub repo by [pressing "y" on that repo](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/getting-permanent-links-to-files#press-y-to-permalink-to-a-file-in-a-specific-commit).<br/>

Older revisions can be found in the URL bar by [viewing the commit history of any repo](https://cdn.discordapp.com/attachments/133251234164375552/775760247787749406/unknown.png)<br/>

Example:<br/>
- `<@1275521742961508432>cog installversion Broken-Repo e798cc268e199612b1316a3d1f193da0770c7016 cog_name`<br/>

**Arguments**<br/>

- `<repo>` The name of the repo to install cogs from.<br/>
- `<revision>` The revision to install from.<br/>
- `<cogs...>` The cog or cogs to install.<br/>
 - Usage: `<@1275521742961508432>cog installversion <repo> <revision> <cog_names>`
Extended Arg Info
> ### revision: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *cog_names: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>updr
Update cogs and reload immediately.<br/>

Examples:<br/>
- `<@1275521742961508432>updr`<br/>
- `<@1275521742961508432>updr defender`<br/>

**Arguments**<br/>

- `[cogs...]` The cog or cogs to update. If omitted, all cogs are updated.<br/>
 - Usage: `<@1275521742961508432>updr <cogs>`
 - Restricted to: `BOT_OWNER`
 - Aliases: `cur`
# <@1275521742961508432>updrall
Update all repositories and their cogs if updates are available.<br/>
 - Usage: `<@1275521742961508432>updrall`
 - Restricted to: `BOT_OWNER`
 - Aliases: `rur`
# <@1275521742961508432>findcog (Hybrid Command)
Find which cog a command comes from.<br/>

This will only work with loaded cogs.<br/>

Example:<br/>
- `<@1275521742961508432>findcog ping`<br/>

**Arguments**<br/>

- `<command_name>` The command to search for.<br/>
 - Usage: `<@1275521742961508432>findcog <command_name>`
 - Slash Usage: `/findcog <command_name>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
