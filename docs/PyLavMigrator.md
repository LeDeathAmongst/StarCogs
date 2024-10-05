Copy the Red Audio settings over to PyLav

# <@1275521742961508432>plmigrate-revert
Reverts the Playlist migration which can cause broken autoplaylists.<br/>

Please note that this will replace any settings already in PyLav.<br/>

If you are sure you want to proceed please run this command again with the confirm argument set to 1<br/>
i.e `<@1275521742961508432>plmigrate-revert 1`<br/>
 - Usage: `<@1275521742961508432>plmigrate-revert <confirm>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# <@1275521742961508432>plm-playlists
Migrate Audio Playlists to PyLav<br/>

If you are sure you want to proceed please run this command again with the confirmation argument set to 1<br/>
i.e `<@1275521742961508432>pl,-playlists 1`<br/>

Do Note this is a best effort task, somethings may not migrate.<br/>
 - Usage: `<@1275521742961508432>plm-playlists <confirm>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
