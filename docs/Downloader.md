# Downloader Help

### pipinstall

**Description:** Install a group of dependencies using pip.

Examples:
- `[p]pipinstall bs4`
- `[p]pipinstall py-cpuinfo psutil`

Improper usage of this command can break your bot, be careful.

**Arguments**

- `<deps...>` The package or packages you wish to install.

**Usage:** `<@1275521742961508432>pipinstall`

### repo

**Description:** Base command for repository management.

**Usage:** `<@1275521742961508432>repo`

### repo list

**Description:** List all installed repos.

**Usage:** `<@1275521742961508432>repo list`

### repo info

**Description:** Show information about a repo.

Example:
- `[p]repo info 26-Cogs`

**Arguments**

- `<repo>` The name of the repo to show info about.

**Usage:** `<@1275521742961508432>repo info`

### repo delete

**Description:** Remove repos and their files.

Examples:
- `[p]repo delete 26-Cogs`
- `[p]repo delete 26-Cogs Laggrons-Dumb-Cogs`

**Arguments**

- `<repos...>` The repo or repos to remove.

**Usage:** `<@1275521742961508432>repo delete`

### repo update

**Description:** Update all repos, or ones of your choosing.

This will *not* update the cogs installed from those repos.

Examples:
- `[p]repo update`
- `[p]repo update 26-Cogs`
- `[p]repo update 26-Cogs Laggrons-Dumb-Cogs`

**Arguments**

- `[repos...]` The name or names of repos to update. If omitted, all repos are updated.

**Usage:** `<@1275521742961508432>repo update`

### repo add

**Description:** Add a new repo.

Examples:
- `[p]repo add 26-Cogs https://github.com/Twentysix26/x26-Cogs`
- `[p]repo add Laggrons-Dumb-Cogs https://github.com/retke/Laggrons-Dumb-Cogs v3`

Repo names can only contain characters A-z, numbers, underscores, hyphens, and dots (but they cannot start or end with a dot).

The branch will be the default branch if not specified.

**Arguments**

- `<name>` The name given to the repo.
- `<repo_url>` URL to the cog branch. Usually GitHub or GitLab.
- `[branch]` Optional branch to install cogs from.

**Usage:** `<@1275521742961508432>repo add`

### cog

**Description:** Base command for cog installation management commands.

**Usage:** `<@1275521742961508432>cog`

### cog unpin

**Description:** Unpin cogs - this will remove the update lock from those cogs.

Examples:
- `[p]cog unpin defender`
- `[p]cog unpin updated_cog1 updated_cog2`

**Arguments**

- `<cogs...>` The cog or cogs to unpin. Must already be installed and pinned.

**Usage:** `<@1275521742961508432>cog unpin`

### cog updatetoversion

**Description:** Update all cogs, or ones of your choosing to chosen revision of one repo.

Note that update doesn't mean downgrade and therefore `revision`
has to be newer than the version that cog currently has installed. If you want to
downgrade the cog, uninstall and install it again.

See `[p]cog installversion` for an explanation of `revision`.

Examples:
- `[p]cog updatetoversion Broken-Repo e798cc268e199612b1316a3d1f193da0770c7016 cog_name`
- `[p]cog updatetoversion True Broken-Repo 6107c0770ad391f1d3a6131b216991e862cc897e cog_name`

**Arguments**

- `[reload]` Whether to reload cogs immediately after update or not.
- `<repo>` The repo or repos to update all cogs from.
- `<revision>` The revision to update to.
- `[cogs...]` The cog or cogs to update.

**Usage:** `<@1275521742961508432>cog updatetoversion`

### cog info

**Description:** List information about a single cog.

Example:
- `[p]cog info 26-Cogs defender`

**Arguments**

- `<repo>` The repo to get cog info from.
- `<cog>` The cog to get info on.

**Usage:** `<@1275521742961508432>cog info`

### cog pin

**Description:** Pin cogs - this will lock cogs on their current version.

Examples:
- `[p]cog pin defender`
- `[p]cog pin outdated_cog1 outdated_cog2`

**Arguments**

- `<cogs...>` The cog or cogs to pin. Must already be installed.

**Usage:** `<@1275521742961508432>cog pin`

### cog reinstallreqs

**Description:** This command should not be used unless Red specifically asks for it.

This command will reinstall cog requirements and shared libraries for all installed cogs.

Red might ask the owner to use this when it clears contents of the lib folder
because of change in minor version of Python.

**Usage:** `<@1275521742961508432>cog reinstallreqs`

### cog install

**Description:** Install a cog from the given repo.

Examples:
- `[p]cog install 26-Cogs defender`
- `[p]cog install Laggrons-Dumb-Cogs say roleinvite`

**Arguments**

- `<repo>` The name of the repo to install cogs from.
- `<cogs...>` The cog or cogs to install.

**Usage:** `<@1275521742961508432>cog install`

### cog update

**Description:** Update all cogs, or ones of your choosing.

Examples:
- `[p]cog update`
- `[p]cog update True`
- `[p]cog update defender`
- `[p]cog update True defender`

**Arguments**

- `[reload]` Whether to reload cogs immediately after update or not.
- `[cogs...]` The cog or cogs to update. If omitted, all cogs are updated.

**Usage:** `<@1275521742961508432>cog update`

### cog list

**Description:** List all available cogs from a single repo.

Example:
- `[p]cog list 26-Cogs`

**Arguments**

- `<repo>` The repo to list cogs from.

**Usage:** `<@1275521742961508432>cog list`

### cog uninstall

**Description:** Uninstall cogs.

You may only uninstall cogs which were previously installed
by Downloader.

Examples:
- `[p]cog uninstall defender`
- `[p]cog uninstall say roleinvite`

**Arguments**

- `<cogs...>` The cog or cogs to uninstall.

**Usage:** `<@1275521742961508432>cog uninstall`

### cog updateallfromrepos

**Description:** Update all cogs from repos of your choosing.

Examples:
- `[p]cog updateallfromrepos 26-Cogs`
- `[p]cog updateallfromrepos True 26-Cogs`
- `[p]cog updateallfromrepos Laggrons-Dumb-Cogs 26-Cogs`

**Arguments**

- `[reload]` Whether to reload cogs immediately after update or not.
- `<repos...>` The repo or repos to update all cogs from.

**Usage:** `<@1275521742961508432>cog updateallfromrepos`

### cog installversion

**Description:** Install a cog from the specified revision of given repo.

Revisions are "commit ids" that point to the point in the code when a specific change was made.
The latest revision can be found in the URL bar for any GitHub repo by [pressing "y" on that repo](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/getting-permanent-links-to-files#press-y-to-permalink-to-a-file-in-a-specific-commit).

Older revisions can be found in the URL bar by [viewing the commit history of any repo](https://cdn.discordapp.com/attachments/133251234164375552/775760247787749406/unknown.png)

Example:
- `[p]cog installversion Broken-Repo e798cc268e199612b1316a3d1f193da0770c7016 cog_name`

**Arguments**

- `<repo>` The name of the repo to install cogs from.
- `<revision>` The revision to install from.
- `<cogs...>` The cog or cogs to install.

**Usage:** `<@1275521742961508432>cog installversion`

### cog listpinned

**Description:** List currently pinned cogs.

**Usage:** `<@1275521742961508432>cog listpinned`

### cog checkforupdates

**Description:** Check for available cog updates (including pinned cogs).

This command doesn't update cogs, it only checks for updates.
Use `[p]cog update` to update cogs.

**Usage:** `<@1275521742961508432>cog checkforupdates`

### findcog

**Description:** Find which cog a command comes from.

This will only work with loaded cogs.

Example:
- `[p]findcog ping`

**Arguments**

- `<command_name>` The command to search for.

**Usage:** `<@1275521742961508432>findcog`

