Generate anime images with NovelAI v3.

# /imagine (Slash Command)
Generate AI images with Dall-E 3.<br/>
 - Usage: `/imagine <prompt> [prompt_style]`
 - `prompt:` (Required) Your prompt will get adjusted by OpenAI.
 - `prompt_style:` (Optional) Dall-E will always edit your prompt before generating.

 - Checks: `Server Only`
Extended Arg Info
> ### prompt: str
> - Autocomplete: False
> 
> Your prompt will get adjusted by OpenAI.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### prompt_style: str
> - Autocomplete: False
> - Default: detail
> - Choices: ['Add detail', "Don't add detail"]
> 
> Dall-E will always edit your prompt before generating.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# <@1275521742961508432>dalleset
Configure /imagine bot-wide.<br/>
 - Usage: `<@1275521742961508432>dalleset`
 - Restricted to: `BOT_OWNER`
## <@1275521742961508432>dalleset cooldown
Time in seconds between a user's generation ends and they can start a new one.<br/>
 - Usage: `<@1275521742961508432>dalleset cooldown <seconds>`
Extended Arg Info
> ### seconds: Optional[int]
> ```
> A number without decimal places.
> ```
## <@1275521742961508432>dalleset vip
Manage the VIP list which skips the cooldown.<br/>
 - Usage: `<@1275521742961508432>dalleset vip`
### <@1275521742961508432>dalleset vip list
Show all users in the VIP list.<br/>
 - Usage: `<@1275521742961508432>dalleset vip list`
### <@1275521742961508432>dalleset vip remove
Remove a list of users from the VIP list.<br/>
 - Usage: `<@1275521742961508432>dalleset vip remove <users>`
Extended Arg Info
> ### users: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### <@1275521742961508432>dalleset vip add
Add a list of users to the VIP list.<br/>
 - Usage: `<@1275521742961508432>dalleset vip add <users>`
Extended Arg Info
> ### users: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
