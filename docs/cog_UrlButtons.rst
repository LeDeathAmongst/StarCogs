UrlButtons
==========

A cog to have url-buttons!

# ,urlbuttons (Hybrid Command)
Group of commands to use UrlButtons.<br/>
 - Usage: `,urlbuttons`
 - Slash Usage: `/urlbuttons`
 - Restricted to: `ADMIN`
 - Checks: `server_only`


## ,urlbuttons bulk (Hybrid Command)
Add a url-button for a message.<br/>

```,urlbuttons bulk <message> :red_circle:|<https://github.com/Cog-Creators/Red-DiscordBot> :smiley:|<https://github.com/Cog-Creators/Red-SmileyBot> :green_circle:|<https://github.com/Cog-Creators/Green-DiscordBot>```
 - Usage: `,urlbuttons bulk <message> <url_buttons>`
 - Slash Usage: `/urlbuttons bulk <message> <url_buttons>`
 - Checks: `server_only`


## ,urlbuttons list (Hybrid Command)
List all url-buttons of this server or display the settings for a specific one.<br/>
 - Usage: `,urlbuttons list [message=None]`
 - Slash Usage: `/urlbuttons list [message=None]`
 - Checks: `server_only`


## ,urlbuttons purge (Hybrid Command)
Clear all url-buttons for a server.<br/>
 - Usage: `,urlbuttons purge`
 - Slash Usage: `/urlbuttons purge`
 - Checks: `server_only`


## ,urlbuttons clear (Hybrid Command)
Clear all url-buttons for a message.<br/>
 - Usage: `,urlbuttons clear <message>`
 - Slash Usage: `/urlbuttons clear <message>`
 - Checks: `server_only`


## ,urlbuttons remove (Hybrid Command)
Remove a url-button for a message.<br/>

Use `,urlbuttons list <message>` to find the config identifier.<br/>
 - Usage: `,urlbuttons remove <message> <config_identifier>`
 - Slash Usage: `/urlbuttons remove <message> <config_identifier>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### config_identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,urlbuttons add (Hybrid Command)
Add a url-button for a message.<br/>
 - Usage: `,urlbuttons add <message> <url> <emoji> [text_button]`
 - Slash Usage: `/urlbuttons add <message> <url> <emoji> [text_button]`
 - Aliases: `+`
 - Checks: `server_only`


