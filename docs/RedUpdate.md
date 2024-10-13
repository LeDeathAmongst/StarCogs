Update [botname] to latest dev/stable changes.

# ,redupdateset
Setting commands for redupdate cog.<br/>
 - Usage: `,redupdateset`
 - Restricted to: `BOT_OWNER`
 - Aliases: `redset`
## ,redupdateset version
Shows information about the cog.<br/>
 - Usage: `,redupdateset version`
## ,redupdateset reseturl
Reset the url to default.<br/>
 - Usage: `,redupdateset reseturl`
## ,redupdateset settings
Show the url for redupdate cog.<br/>
 - Usage: `,redupdateset settings`
## ,redupdateset url
Set your custom fork url of red.<br/>

Has to be a valid link such as `git+https://github.com/Cog-Creators/Red-DiscordBot` else it will not work.<br/>
 - Usage: `,redupdateset url`
## ,redupdateset whatlink
Show what a valid link looks like.<br/>
 - Usage: `,redupdateset whatlink`
 - Aliases: `whaturl`
# ,updatered
update Starfire to latest changes.<br/>

it will update to latest stable changes by default unless you specify `dev` as version.<br/>

Arguments:<br/>
- `[version]`: `dev` to update to latest dev changes. `stable` by default already.<br/>
 - Usage: `,updatered <version>`
 - Restricted to: `BOT_OWNER`
# ,forkupdate
Update Starfire to your fork.<br/>

This will update to your fork and not to red's main repo. Make sure you have set the url using `redset url` before using this command.<br/>

Note: If you do not have a fork, you can use `updatered` to update to latest stable changes.<br/>
 - Usage: `,forkupdate`
 - Restricted to: `BOT_OWNER`
 - Aliases: `updatefork, fupd, and updf`
