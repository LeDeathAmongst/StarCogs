Dashboard
=========

Interact with your bot through a web Dashboard!

<<<<<<< HEAD
# <@1275521742961508432>dashboard (Hybrid Command)
Get the link to the Dashboard.<br/>
 - Usage: `<@1275521742961508432>dashboard`
 - Slash Usage: `/dashboard`


# <@1275521742961508432>setdashboard (Hybrid Command)
Configure Dashboard.<br/>
 - Usage: `<@1275521742961508432>setdashboard`
=======
# ,dashboard (Hybrid Command)
Get the link to the Dashboard.<br/>
 - Usage: `,dashboard`
 - Slash Usage: `/dashboard`


# ,setdashboard (Hybrid Command)
Configure Dashboard.<br/>
 - Usage: `,setdashboard`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setdashboard`
 - Restricted to: `BOT_OWNER`


<<<<<<< HEAD
## <@1275521742961508432>setdashboard metawebsitedescription (Hybrid Command)
The website short description to use.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `<@1275521742961508432>setdashboard metawebsitedescription <value>`
 - Slash Usage: `/setdashboard metawebsitedescription <value>`
Extended Arg Info
> ### value: str
=======
## ,setdashboard secret (Hybrid Command)
Set the client secret needed for Discord OAuth.<br/>
 - Usage: `,setdashboard secret [secret]`
 - Slash Usage: `/setdashboard secret [secret]`
Extended Arg Info
> ### secret: str = None
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setdashboard showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `<@1275521742961508432>setdashboard showsettings [with_dev=False]`
 - Slash Usage: `/setdashboard showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdashboard allowunsecurehttprequests (Hybrid Command)
Allow unsecure http requests. This is not recommended for production, but required if you can't set up a SSL certificate.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdashboard allowunsecurehttprequests <value>`
 - Slash Usage: `/setdashboard allowunsecurehttprequests <value>`
 - Aliases: `allowunsecure`
=======
## ,setdashboard allinone (Hybrid Command)
Run the Dashboard in the bot process, without having to open another window. You have to install Red-Dashboard in your bot venv with Pip and reload the cog.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setdashboard allinone <value>`
 - Slash Usage: `/setdashboard allinone <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setdashboard metaicon (Hybrid Command)
=======
## ,setdashboard metaicon (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
The website icon to use.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setdashboard metaicon <value>`
=======
 - Usage: `,setdashboard metaicon <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setdashboard metaicon <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setdashboard metatitle (Hybrid Command)
The website title to use.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `<@1275521742961508432>setdashboard metatitle <value>`
 - Slash Usage: `/setdashboard metatitle <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setdashboard supportserver (Hybrid Command)
=======
## ,setdashboard showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `,setdashboard showsettings [with_dev=False]`
 - Slash Usage: `/setdashboard showsettings [with_dev=False]`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setdashboard supportserver (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Set the support server url of your bot.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setdashboard supportserver <value>`
=======
 - Usage: `,setdashboard supportserver <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setdashboard supportserver <value>`
 - Aliases: `support`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setdashboard defaultbackgroundtheme (Hybrid Command)
Set the default Background theme of the dashboard.<br/>

Default value: `white`<br/>
Dev: `typing.Literal['white', 'dark']`<br/>
 - Usage: `<@1275521742961508432>setdashboard defaultbackgroundtheme <value>`
 - Slash Usage: `/setdashboard defaultbackgroundtheme <value>`


## <@1275521742961508432>setdashboard redirecturi (Hybrid Command)
=======
## ,setdashboard redirecturi (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
The redirect uri to use for the Discord OAuth.<br/>

Default value: `None`<br/>
Dev: `<class 'dashboard.dashboard.RedirectURIConverter'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setdashboard redirecturi <value>`
=======
 - Usage: `,setdashboard redirecturi <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setdashboard redirecturi <value>`
 - Aliases: `redirect`


<<<<<<< HEAD
## <@1275521742961508432>setdashboard metadescription (Hybrid Command)
=======
## ,setdashboard allowunsecurehttprequests (Hybrid Command)
Allow unsecure http requests. This is not recommended for production, but required if you can't set up a SSL certificate.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `,setdashboard allowunsecurehttprequests <value>`
 - Slash Usage: `/setdashboard allowunsecurehttprequests <value>`
 - Aliases: `allowunsecure`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## ,setdashboard metatitle (Hybrid Command)
The website title to use.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,setdashboard metatitle <value>`
 - Slash Usage: `/setdashboard metatitle <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,setdashboard metadescription (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
The website long description to use.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setdashboard metadescription <value>`
=======
 - Usage: `,setdashboard metadescription <value>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setdashboard metadescription <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>setdashboard defaultsidenavtheme (Hybrid Command)
=======
## ,setdashboard resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `,setdashboard resetsetting <setting>`
 - Slash Usage: `/setdashboard resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,setdashboard defaultsidenavtheme (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Set the default Sidenav theme of the dashboard.<br/>

Default value: `white`<br/>
Dev: `typing.Literal['white', 'dark']`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setdashboard defaultsidenavtheme <value>`
 - Slash Usage: `/setdashboard defaultsidenavtheme <value>`


## <@1275521742961508432>setdashboard flaskflags (Hybrid Command)
The flags used to setting the webserver if `all_in_one` is enabled. They are the cli flags of `reddash` without `--rpc-port`.<br/>

Default value: `[]`<br/>
Dev: `Greedy[StrConverter]`<br/>
 - Usage: `<@1275521742961508432>setdashboard flaskflags <value>`
 - Slash Usage: `/setdashboard flaskflags <value>`


## <@1275521742961508432>setdashboard modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `<@1275521742961508432>setdashboard modalconfig [confirmation=False]`
=======
 - Usage: `,setdashboard defaultsidenavtheme <value>`
 - Slash Usage: `/setdashboard defaultsidenavtheme <value>`


## ,setdashboard modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `,setdashboard modalconfig [confirmation=False]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Slash Usage: `/setdashboard modalconfig [confirmation=False]`
 - Aliases: `configmodal`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```


<<<<<<< HEAD
## <@1275521742961508432>setdashboard defaultcolor (Hybrid Command)
=======
## ,setdashboard flaskflags (Hybrid Command)
The flags used to setting the webserver if `all_in_one` is enabled. They are the cli flags of `reddash` without `--rpc-port`.<br/>

Default value: `[]`<br/>
Dev: `Greedy[StrConverter]`<br/>
 - Usage: `,setdashboard flaskflags <value>`
 - Slash Usage: `/setdashboard flaskflags <value>`


## ,setdashboard metawebsitedescription (Hybrid Command)
The website short description to use.<br/>

Default value: `None`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `,setdashboard metawebsitedescription <value>`
 - Slash Usage: `/setdashboard metawebsitedescription <value>`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,setdashboard defaultcolor (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
Set the default Color of the dashboard.<br/>

Default value: `success`<br/>
Dev: `typing.Literal['success', 'danger', 'primary', 'info', 'warning', 'dark']`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setdashboard defaultcolor <value>`
 - Slash Usage: `/setdashboard defaultcolor <value>`


## <@1275521742961508432>setdashboard allinone (Hybrid Command)
Run the Dashboard in the bot process, without having to open another window. You have to install Red-Dashboard in your bot venv with Pip and reload the cog.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `<@1275521742961508432>setdashboard allinone <value>`
 - Slash Usage: `/setdashboard allinone <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>setdashboard disabledthirdparties (Hybrid Command)
=======
 - Usage: `,setdashboard defaultcolor <value>`
 - Slash Usage: `/setdashboard defaultcolor <value>`


## ,setdashboard defaultbackgroundtheme (Hybrid Command)
Set the default Background theme of the dashboard.<br/>

Default value: `white`<br/>
Dev: `typing.Literal['white', 'dark']`<br/>
 - Usage: `,setdashboard defaultbackgroundtheme <value>`
 - Slash Usage: `/setdashboard defaultbackgroundtheme <value>`


## ,setdashboard disabledthirdparties (Hybrid Command)
>>>>>>> 9e308722 (Revamped and Fixed)
The third parties to disable.<br/>

Default value: `[]`<br/>
Dev: `Greedy[ThirdPartyConverter]`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>setdashboard disabledthirdparties <value>`
 - Slash Usage: `/setdashboard disabledthirdparties <value>`


## <@1275521742961508432>setdashboard secret (Hybrid Command)
Set the client secret needed for Discord OAuth.<br/>
 - Usage: `<@1275521742961508432>setdashboard secret [secret]`
 - Slash Usage: `/setdashboard secret [secret]`
Extended Arg Info
> ### secret: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>setdashboard resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `<@1275521742961508432>setdashboard resetsetting <setting>`
 - Slash Usage: `/setdashboard resetsetting <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


=======
 - Usage: `,setdashboard disabledthirdparties <value>`
 - Slash Usage: `/setdashboard disabledthirdparties <value>`


>>>>>>> 9e308722 (Revamped and Fixed)
