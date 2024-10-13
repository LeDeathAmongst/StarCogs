Copy the Red Audio settings over to PyLav

# ,plmigrate-revert
Reverts the Playlist migration which can cause broken autoplaylists.<br/>

Please note that this will replace any settings already in PyLav.<br/>

If you are sure you want to proceed please run this command again with the confirm argument set to 1<br/>
i.e `,plmigrate-revert 1`<br/>
 - Usage: `,plmigrate-revert <confirm>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# ,plm-playlists
Migrate Audio Playlists to PyLav<br/>

If you are sure you want to proceed please run this command again with the confirmation argument set to 1<br/>
i.e `,pl,-playlists 1`<br/>

Do Note this is a best effort task, somethings may not migrate.<br/>
 - Usage: `,plm-playlists <confirm>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
