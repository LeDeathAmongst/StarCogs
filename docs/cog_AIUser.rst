AIUser
======

Human-like Discord interactions powered by OpenAI (or compatible endpoints) for messages (and images).

# /chat (Slash Command)
Talk directly to this bot's AI. Ask it anything you want!<br/>
 - Usage: `/chat <text>`
 - `text:` (Required) The prompt you want to send to the AI.

Extended Arg Info
> ### text: str
> - Autocomplete: False
> 
> The prompt you want to send to the AI.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
# <@1275521742961508432>aiuserowner
For some settings that apply bot-wide.<br/>
 - Usage: `<@1275521742961508432>aiuserowner`
=======
# ,aiuserowner
For some settings that apply bot-wide.<br/>
 - Usage: `,aiuserowner`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
 - Aliases: `ai_userowner`


<<<<<<< HEAD
## <@1275521742961508432>aiuserowner prompt
Set the global default prompt for aiuser.<br/>

Leave blank to delete the currently set global prompt, and use the build-in default prompt.<br/>

**Arguments**<br/>
    - `prompt` The prompt to set.<br/>
 - Usage: `<@1275521742961508432>aiuserowner prompt <prompt>`
Extended Arg Info
> ### prompt: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aiuserowner importconfig
Imports a config from json file (:warning: No checks are done)<br/>

 Make sure your new config is valid, and the old config is backed up.<br/>

:warning: JSON backend only<br/>
 - Usage: `<@1275521742961508432>aiuserowner importconfig`


## <@1275521742961508432>aiuserowner timeout
Sets the request timeout to the OpenAI endpoint <br/>
 - Usage: `<@1275521742961508432>aiuserowner timeout <seconds>`
=======
## ,aiuserowner timeout
Sets the request timeout to the OpenAI endpoint <br/>
 - Usage: `,aiuserowner timeout <seconds>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiuserowner exportconfig
Exports the current config to a json file<br/>

:warning: JSON backend only<br/>
 - Usage: `<@1275521742961508432>aiuserowner exportconfig`


## <@1275521742961508432>aiuserowner endpoint
Sets the OpenAI endpoint to a custom one (must be OpenAI API compatible)<br/>

Reset to official OpenAI endpoint with `<@1275521742961508432>aiuseradmin endpoint clear`<br/>
 - Usage: `<@1275521742961508432>aiuserowner endpoint <url>`
=======
## ,aiuserowner exportconfig
Exports the current config to a json file<br/>

:warning: JSON backend only<br/>
 - Usage: `,aiuserowner exportconfig`


## ,aiuserowner endpoint
Sets the OpenAI endpoint to a custom one (must be OpenAI API compatible)<br/>

Reset to official OpenAI endpoint with `,aiuseradmin endpoint clear`<br/>
 - Usage: `,aiuserowner endpoint <url>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### url: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiuserowner maxpromptlength
Sets the maximum character length of a prompt that can set by admins in any server.<br/>

(Does not apply to already set prompts, only new ones)<br/>
 - Usage: `<@1275521742961508432>aiuserowner maxpromptlength <length>`
=======
## ,aiuserowner maxpromptlength
Sets the maximum character length of a prompt that can set by admins in any server.<br/>

(Does not apply to already set prompts, only new ones)<br/>
 - Usage: `,aiuserowner maxpromptlength <length>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### length: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiuserowner maxtopiclength
Sets the maximum character length of a random prompt that can set by any server.<br/>

(Does not apply to already set prompts, only new ones)<br/>
 - Usage: `<@1275521742961508432>aiuserowner maxtopiclength <length>`
=======
## ,aiuserowner maxtopiclength
Sets the maximum character length of a random prompt that can set by any server.<br/>

(Does not apply to already set prompts, only new ones)<br/>
 - Usage: `,aiuserowner maxtopiclength <length>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### length: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
# <@1275521742961508432>aiuser
Utilize OpenAI to reply to messages and images in approved channels and by opt-in users<br/>
 - Usage: `<@1275521742961508432>aiuser`
=======
## ,aiuserowner prompt
Set the global default prompt for aiuser.<br/>

Leave blank to delete the currently set global prompt, and use the build-in default prompt.<br/>

**Arguments**<br/>
    - `prompt` The prompt to set.<br/>
 - Usage: `,aiuserowner prompt <prompt>`
Extended Arg Info
> ### prompt: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,aiuserowner importconfig
Imports a config from json file (:warning: No checks are done)<br/>

 Make sure your new config is valid, and the old config is backed up.<br/>

:warning: JSON backend only<br/>
 - Usage: `,aiuserowner importconfig`


# ,aiuser
Utilize OpenAI to reply to messages and images in approved channels and by opt-in users<br/>
 - Usage: `,aiuser`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `ai_user`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>aiuser randommessage
Configure the random message event<br/>
**(Must be enabled by bot owner first using `<@1275521742961508432>aiuser random toggle`)**<br/>

Every 33 minutes, a RNG roll will determine if a random message will be sent using a random prompt from a given list.<br/>

Whitelisted channels must have a hour pass without a message sent in it for a random message to be sent. Last message author must not be this bot.<br/>

(All subcommands per server)<br/>
 - Usage: `<@1275521742961508432>aiuser randommessage`
 - Restricted to: `ADMIN`


### <@1275521742961508432>aiuser randommessage toggle
Toggles random message events <br/>
 - Usage: `<@1275521742961508432>aiuser randommessage toggle`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>aiuser randommessage remove
Removes a prompt (by number) from the list<br/>
 - Usage: `<@1275521742961508432>aiuser randommessage remove <number>`
 - Aliases: `rm and delete`
=======
## ,aiuser history
Change the prompt context settings for the current server<br/>

The most recent messages that are within the time gap and message limits are used to create context.<br/>
Context is used to help the LLM generate a response.<br/>
 - Usage: `,aiuser history`
 - Restricted to: `BOT_OWNER`
 - Aliases: `context`


### ,aiuser history backread
Set max amount of messages to be used as context<br/>

(Increasing the number of messages will increase the cost of the response, messages will be added until the LLM's token limit is reached)<br/>
 - Usage: `,aiuser history backread <new_value>`
 - Aliases: `messages and size`
Extended Arg Info
> ### new_value: int
> ```
> A number without decimal places.
> ```


### ,aiuser history customtokenlimit
Set a LLM's custom maximum context limit (for local LLMs or those not listed in `aiuser/common/constants.py`.).<br/>

If not set, a safe default or saved limit from `aiuser/common/constants.py` is used.<br/>
 - Usage: `,aiuser history customtokenlimit <new_value>`
Extended Arg Info
> ### new_value: Optional[int]
> ```
> A number without decimal places.
> ```


### ,aiuser history time
Set max time (sec) messages can be apart before no more can be added<br/>

eg. if set to 60, once messsages are more than 60 seconds apart, more messages will not be added.<br/>

Helpful to prevent the LLM from mixing up context from different conversations.<br/>
 - Usage: `,aiuser history time <new_value>`
 - Aliases: `gap`
Extended Arg Info
> ### new_value: int
> ```
> A number without decimal places.
> ```


## ,aiuser imagerequest
Generate self-portrait images based on user request (on trigger words / LLM decision)<br/>

See [here](https://github.com/zhaobenny/bz-cogs/tree/main/aiuser#image-requests-%EF%B8%8F)<br/>

(All subcommands are per server)<br/>
 - Usage: `,aiuser imagerequest`
 - Restricted to: `BOT_OWNER`


### ,aiuser imagerequest toggle
Toggle requests to endpoint<br/>
 - Usage: `,aiuser imagerequest toggle`


### ,aiuser imagerequest subject
The subject in Stable Diffusion requests (needed to better hint SD prompt generation by LLM)<br/>

If the subject is well known in the SD model, use it here eg. `katsuragi misato`<br/>
Else use a generic subject eg. `man` or `woman`<br/>
 - Usage: `,aiuser imagerequest subject <subject>`
Extended Arg Info
> ### subject: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,aiuser imagerequest trigger
Set trigger words to detect image requests<br/>
 - Usage: `,aiuser imagerequest trigger`


#### ,aiuser imagerequest trigger sremove
Remove a word from the second person words list<br/>
 - Usage: `,aiuser imagerequest trigger sremove <word>`
 - Aliases: `removesecond`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser imagerequest trigger remove
Remove a word from the trigger words list<br/>
 - Usage: `,aiuser imagerequest trigger remove <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser imagerequest trigger list
Show the trigger words list<br/>
 - Usage: `,aiuser imagerequest trigger list`
 - Aliases: `show`


#### ,aiuser imagerequest trigger sclear
Clear the second person words list to default<br/>
 - Usage: `,aiuser imagerequest trigger sclear`
 - Aliases: `clearsecond`


#### ,aiuser imagerequest trigger add
Add a word to the trigger words list<br/>
 - Usage: `,aiuser imagerequest trigger add <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser imagerequest trigger slist
Show the second person words list<br/>
 - Usage: `,aiuser imagerequest trigger slist`
 - Aliases: `showsecond and sshow`


#### ,aiuser imagerequest trigger sadd
Add a word to the second person words list (to replace with subject) <br/>
 - Usage: `,aiuser imagerequest trigger sadd <word>`
 - Aliases: `addsecond`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser imagerequest trigger clear
Clear the trigger words list to default<br/>
 - Usage: `,aiuser imagerequest trigger clear`


### ,aiuser imagerequest preprompt
This text will always be sent as part of the prompt in Stable Diffusion requests<br/>

(Set LORAs here if supported eg. `<lora: name: weight>`)<br/>
 - Usage: `,aiuser imagerequest preprompt <preprompt>`
Extended Arg Info
> ### preprompt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,aiuser imagerequest captionprompt
Set the prompt that creates the caption for the image generation<br/>
 - Usage: `,aiuser imagerequest captionprompt <prompt>`
Extended Arg Info
> ### prompt: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,aiuser imagerequest parameters
Set compatible parameters (depends on interface, eg. see (https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for A1111)<br/>

Example command:<br/>
`,aiuser imagerequest parameters ```{"sampler_name": "Euler a", "steps": 20}``` `<br/>
 - Usage: `,aiuser imagerequest parameters <json_block>`
Extended Arg Info
> ### json_block: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,aiuser imagerequest config
Show current settings<br/>
 - Usage: `,aiuser imagerequest config`


### ,aiuser imagerequest reduce_calls
Disables a LLM check on validating image requests<br/>

:warning: Will trigger image generation based ONLY on keywords instead of checking with the LLM<br/>
 - Usage: `,aiuser imagerequest reduce_calls`


### ,aiuser imagerequest endpoint
Set compatible image generation endpoint (eg. for local A1111 include `/sdapi/v1/txt2img`)<br/>

If set to `dall-e-3` or `dall-e-2`, image requests will use OpenAI's DALL·E models at 1024x1024 SD resolution.<br/>
 - Usage: `,aiuser imagerequest endpoint <url>`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,aiuser imagescan
Change the image scan setting<br/>

Go [here](https://github.com/zhaobenny/bz-cogs/tree/main/aiuser#image-scanning-%EF%B8%8F) for more info.<br/>

(All subcommands are per server)<br/>
 - Usage: `,aiuser imagescan`
 - Restricted to: `BOT_OWNER`


### ,aiuser imagescan model
Set the specific LLM used in the `supported-llm` mode<br/>


**Arguments**<br/>
    - `model_name` Name of a compatible model<br/>
 - Usage: `,aiuser imagescan model <model_name>`
Extended Arg Info
> ### model_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,aiuser imagescan toggle
Toggle image scanning <br/>
 - Usage: `,aiuser imagescan toggle`


### ,aiuser imagescan mode
Set method for scanning images<br/>


**Arguments**<br/>
- `mode` One of the following: `local`, `ai-horde`, `supported-llm`<br/>
 - Usage: `,aiuser imagescan mode <mode>`
Extended Arg Info
> ### mode: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,aiuser imagescan maxsize
Set max download size in Megabytes for image scanning <br/>
 - Usage: `,aiuser imagescan maxsize <size>`
Extended Arg Info
> ### size: float
> ```
> A number with or without decimal places.
> ```


## ,aiuser response
Change settings used for generated responses<br/>

(All subcommands are per server)<br/>
 - Usage: `,aiuser response`
 - Restricted to: `ADMIN`


### ,aiuser response removelist
Manage the list of regex patterns to remove from responses<br/>
        <br/>
 - Usage: `,aiuser response removelist`


#### ,aiuser response removelist add
Add a regex pattern to the list of patterns to remove from responses<br/>
 - Usage: `,aiuser response removelist add <regex_pattern>`
Extended Arg Info
> ### regex_pattern: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser response removelist reset
Reset the list of regexes to default <br/>
 - Usage: `,aiuser response removelist reset`


#### ,aiuser response removelist remove
Remove a regex pattern (by number) from the list<br/>
 - Usage: `,aiuser response removelist remove <number>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
### <@1275521742961508432>aiuser randommessage add
Add a new prompt to be used in random messages<br/>
 - Usage: `<@1275521742961508432>aiuser randommessage add <prompt>`
 - Aliases: `a`
Extended Arg Info
> ### prompt: str
=======
#### ,aiuser response removelist show
Show the current regex patterns of strings to removed from responses <br/>
 - Usage: `,aiuser response removelist show`


### ,aiuser response parameters
Set custom parameters for an endpoint using a JSON code block<br/>

To reset parameters to default, use `,aiuser response parameters reset`<br/>
To show current parameters, use `,aiuser response parameters show`<br/>

Example command:<br/>
`,aiuser response parameters ```{"frequency_penalty": 2.0, "max_tokens": 200}``` `<br/>

See [here](https://platform.openai.com/docs/api-reference/chat/create) for possible parameters<br/>
Some parameters are blocked.<br/>
 - Usage: `,aiuser response parameters <json_block>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### json_block: str
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
### <@1275521742961508432>aiuser randommessage show
Lists prompts to used in random messages <br/>
 - Usage: `<@1275521742961508432>aiuser randommessage show`
 - Aliases: `list`


### <@1275521742961508432>aiuser randommessage reset
Resets the random prompt list to the default<br/>
 - Usage: `<@1275521742961508432>aiuser randommessage reset`


### <@1275521742961508432>aiuser randommessage percent
Sets the chance that a random message will be sent every 33 minutes<br/>

**Arguments**<br/>
    - `percent` A number between 0 and 100<br/>
 - Usage: `<@1275521742961508432>aiuser randommessage percent <percent>`
 - Aliases: `set and chance`
Extended Arg Info
> ### percent: float
=======
### ,aiuser response weights
Bias the LLM for/against certain words (tokens)<br/>

See [here](https://help.openai.com/en/articles/5247780-using-logit-bias-to-define-token-probability) for additional info.<br/>

(All subcommands are per server)<br/>
 - Usage: `,aiuser response weights`
 - Restricted to: `ADMIN`
 - Aliases: `logit_bias and bias`


#### ,aiuser response weights list
Show weights<br/>
 - Usage: `,aiuser response weights list`
 - Aliases: `show`


#### ,aiuser response weights remove
Removes weight for a specific word<br/>

*Arguments*<br/>
    - `word` The word to remove<br/>
 - Usage: `,aiuser response weights remove <word>`
 - Aliases: `delete`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser response weights add
Sets weight for a specific word<br/>

Will also use all possible tokens for a word when setting weight<br/>
See [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) for detailed text to token conversion.<br/>

*Arguments*<br/>
- `word` The word to set weight for<br/>
- `weight` The weight to set (`-100` to `100`)<br/>
 - Usage: `,aiuser response weights add <word> <weight>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### weight: int
> ```
> A number without decimal places.
> ```


### ,aiuser response toggleoptinembed
Toggles warning embed about opt-in on or off<br/>
 - Usage: `,aiuser response toggleoptinembed`


## ,aiuser trigger
Configure trigger settings for the bot to respond to<br/>

(All subcommands per server)<br/>
 - Usage: `,aiuser trigger`
 - Restricted to: `ADMIN`


### ,aiuser trigger minlength
Set the minimum length of messages that the bot will respond to<br/>
 - Usage: `,aiuser trigger minlength <length>`
 - Aliases: `min_length`
Extended Arg Info
> ### length: int
> ```
> A number without decimal places.
> ```


### ,aiuser trigger conversation_reply_time
Set the max time frame in seconds for the bot to have a `conversation_reply_percent` chance of replying to a message <br/>
When `conversation_reply_time` have lapsed for the last bot message, `conversation_reply_percent` will not be used.<br/>
 - Usage: `,aiuser trigger conversation_reply_time <seconds>`
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```


### ,aiuser trigger public_forget
Toggles whether anyone can use the forget command, or only moderators <br/>
 - Usage: `,aiuser trigger public_forget`


### ,aiuser trigger conversation_reply_percent
Set a different percentage chance of the bot continuing to reply within `conversation_reply_time` time frame<br/>
 - Usage: `,aiuser trigger conversation_reply_percent <percent>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### percent: int
> ```
> A number without decimal places.
> ```


### ,aiuser trigger reply_to_mentions
Toggles if the bot will always reply to mentions/replies <br/>
 - Usage: `,aiuser trigger reply_to_mentions`
 - Restricted to: `BOT_OWNER`
 - Aliases: `mentions_replies`


### ,aiuser trigger whitelist
If configured, only whitelisted roles / users can trigger a response in whitelisted channels<br/>
        <br/>
 - Usage: `,aiuser trigger whitelist`
 - Aliases: `whitelists`


#### ,aiuser trigger whitelist add
Add a role/user to the whitelist <br/>
 - Usage: `,aiuser trigger whitelist add <new>`
Extended Arg Info
> ### new: Union[discord.role.Role, discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


#### ,aiuser trigger whitelist clear
Clear the whitelist, allowing anyone to trigger LLM in whitelisted channels <br/>
 - Usage: `,aiuser trigger whitelist clear`


#### ,aiuser trigger whitelist remove
Remove a user/role from the whitelist <br/>
 - Usage: `,aiuser trigger whitelist remove <rm>`
Extended Arg Info
> ### rm: Union[discord.role.Role, discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


#### ,aiuser trigger whitelist list
Show the whitelist <br/>
 - Usage: `,aiuser trigger whitelist list`
 - Aliases: `show`


### ,aiuser trigger ignore
Messages matching this regex won't be replied to or seen, by the bot <br/>
 - Usage: `,aiuser trigger ignore <regex_pattern>`
 - Aliases: `ignoreregex`
Extended Arg Info
> ### regex_pattern: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## ,aiuser functions
Settings to manage function calling<br/>

(All subcommands are per server)<br/>
 - Usage: `,aiuser functions`
 - Restricted to: `BOT_OWNER`


### ,aiuser functions location
Set the location where the bot will canonically be in<br/>

Used for some functions.<br/>

**Arguments**<br/>
- `latitude` decimal latitude<br/>
- `longitude` decimal longitude<br/>
 - Usage: `,aiuser functions location <latitude> <longitude>`
Extended Arg Info
> ### latitude: float
> ```
> A number with or without decimal places.
> ```
> ### longitude: float
>>>>>>> 9e308722 (Revamped and Fixed)
> ```
> A number with or without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiuser config
Returns current config<br/>

(Current config per server)<br/>
 - Usage: `<@1275521742961508432>aiuser config`
 - Aliases: `settings and showsettings`


## <@1275521742961508432>aiuser remove
=======
### ,aiuser functions noresponse
Enable/disable the functionality for the LLM to choose to not respond and ignore messages.<br/>

Temperamental, may require additional prompting to work better.<br/>
 - Usage: `,aiuser functions noresponse`


### ,aiuser functions weather
Enable/disable a group of functions to getting weather using Open-Meteo<br/>

See [Open-Meteo terms](https://open-meteo.com/en/terms) for their free API<br/>
 - Usage: `,aiuser functions weather`


### ,aiuser functions scrape
Enable/disable the functionality for the LLM to open URLs in messages<br/>

(May not be called if the link generated an Discord embed)<br/>
 - Usage: `,aiuser functions scrape`


### ,aiuser functions search
Enable/disable searching/scraping the Internet using Serper.dev <br/>
 - Usage: `,aiuser functions search`


### ,aiuser functions toggle
Toggle functions calling<br/>

Requires a model that is whitelisted for function calling<br/>
If enabled, the LLM will call functions to generate responses when needed<br/>
This will generate additional API calls and token usage!<br/>
 - Usage: `,aiuser functions toggle`


## ,aiuser remove
>>>>>>> 9e308722 (Revamped and Fixed)
Remove a channel from the whitelist<br/>

**Arguments**<br/>
    - `channel` A mention of the channel<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiuser remove <channel>`
=======
 - Usage: `,aiuser remove <channel>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


<<<<<<< HEAD
## <@1275521742961508432>aiuser model
Changes chat completion model<br/>

 To see a list of available models, use `<@1275521742961508432>aiuser model list`<br/>
=======
## ,aiuser model
Changes chat completion model<br/>

 To see a list of available models, use `,aiuser model list`<br/>
>>>>>>> 9e308722 (Revamped and Fixed)
 (Setting is per server)<br/>

**Arguments**<br/>
    - `model` The model to use eg. `gpt-4`<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiuser model <model>`
=======
 - Usage: `,aiuser model <model>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### model: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiuser functions
Settings to manage function calling<br/>

(All subcommands are per server)<br/>
 - Usage: `<@1275521742961508432>aiuser functions`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>aiuser functions scrape
Enable/disable the functionality for the LLM to open URLs in messages<br/>

(May not be called if the link generated an Discord embed)<br/>
 - Usage: `<@1275521742961508432>aiuser functions scrape`


### <@1275521742961508432>aiuser functions search
Enable/disable searching/scraping the Internet using Serper.dev <br/>
 - Usage: `<@1275521742961508432>aiuser functions search`


### <@1275521742961508432>aiuser functions location
Set the location where the bot will canonically be in<br/>

Used for some functions.<br/>

**Arguments**<br/>
- `latitude` decimal latitude<br/>
- `longitude` decimal longitude<br/>
 - Usage: `<@1275521742961508432>aiuser functions location <latitude> <longitude>`
Extended Arg Info
> ### latitude: float
> ```
> A number with or without decimal places.
> ```
> ### longitude: float
> ```
> A number with or without decimal places.
> ```


### <@1275521742961508432>aiuser functions toggle
Toggle functions calling<br/>

Requires a model that is whitelisted for function calling<br/>
If enabled, the LLM will call functions to generate responses when needed<br/>
This will generate additional API calls and token usage!<br/>
 - Usage: `<@1275521742961508432>aiuser functions toggle`


### <@1275521742961508432>aiuser functions noresponse
Enable/disable the functionality for the LLM to choose to not respond and ignore messages.<br/>

Temperamental, may require additional prompting to work better.<br/>
 - Usage: `<@1275521742961508432>aiuser functions noresponse`


### <@1275521742961508432>aiuser functions weather
Enable/disable a group of functions to getting weather using Open-Meteo<br/>

See [Open-Meteo terms](https://open-meteo.com/en/terms) for their free API<br/>
 - Usage: `<@1275521742961508432>aiuser functions weather`


## <@1275521742961508432>aiuser prompt
Change the prompt settings for the current server<br/>

(All subcommands are per server)<br/>
 - Usage: `<@1275521742961508432>aiuser prompt`
 - Restricted to: `ADMIN`


### <@1275521742961508432>aiuser prompt reset
Reset ALL prompts in this server to default (inc. channels and members) <br/>
 - Usage: `<@1275521742961508432>aiuser prompt reset`


### <@1275521742961508432>aiuser prompt set
=======
## ,aiuser optout
Opt out of sending your messages / images to OpenAI or another endpoint (bot-wide)<br/>

This will prevent the bot from replying to your messages or using your messages.<br/>
 - Usage: `,aiuser optout`


## ,aiuser randommessage
Configure the random message event<br/>
**(Must be enabled by bot owner first using `,aiuser random toggle`)**<br/>

Every 33 minutes, a RNG roll will determine if a random message will be sent using a random prompt from a given list.<br/>

Whitelisted channels must have a hour pass without a message sent in it for a random message to be sent. Last message author must not be this bot.<br/>

(All subcommands per server)<br/>
 - Usage: `,aiuser randommessage`
 - Restricted to: `ADMIN`


### ,aiuser randommessage remove
Removes a prompt (by number) from the list<br/>
 - Usage: `,aiuser randommessage remove <number>`
 - Aliases: `rm and delete`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


### ,aiuser randommessage add
Add a new prompt to be used in random messages<br/>
 - Usage: `,aiuser randommessage add <prompt>`
 - Aliases: `a`
Extended Arg Info
> ### prompt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### ,aiuser randommessage toggle
Toggles random message events <br/>
 - Usage: `,aiuser randommessage toggle`
 - Restricted to: `BOT_OWNER`


### ,aiuser randommessage show
Lists prompts to used in random messages <br/>
 - Usage: `,aiuser randommessage show`
 - Aliases: `list`


### ,aiuser randommessage percent
Sets the chance that a random message will be sent every 33 minutes<br/>

**Arguments**<br/>
    - `percent` A number between 0 and 100<br/>
 - Usage: `,aiuser randommessage percent <percent>`
 - Aliases: `set and chance`
Extended Arg Info
> ### percent: float
> ```
> A number with or without decimal places.
> ```


### ,aiuser randommessage reset
Resets the random prompt list to the default<br/>
 - Usage: `,aiuser randommessage reset`


## ,aiuser config
Returns current config<br/>

(Current config per server)<br/>
 - Usage: `,aiuser config`
 - Aliases: `settings and showsettings`


## ,aiuser add
Adds a channel to the whitelist<br/>

**Arguments**<br/>
    - `channel` A mention of the channel<br/>
 - Usage: `,aiuser add <channel>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     


## ,aiuser optin
Opt in of sending your messages / images to OpenAI or another endpoint (bot-wide)<br/>

This will allow the bot to reply to your messages or use your messages.<br/>
 - Usage: `,aiuser optin`


## ,aiuser prompt
Change the prompt settings for the current server<br/>

(All subcommands are per server)<br/>
 - Usage: `,aiuser prompt`
 - Restricted to: `ADMIN`


### ,aiuser prompt set
>>>>>>> 9e308722 (Revamped and Fixed)
Set a custom prompt or preset for the server (or provided channel/role/member)<br/>

If multiple prompts can be used, the most specific prompt will be used, eg. it will go for: member > role > channel > server<br/>

**Arguments**<br/>
    - `mention` *(Optional)* A specific user or channel<br/>
    - `prompt` *(Optional)* The prompt (or name of a preset) to set. If blank, will remove current prompt.<br/>
    - `<ATTACHMENT>` *(Optional)* An `.txt` file to use as the prompt<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiuser prompt set <mention> <prompt>`
=======
 - Usage: `,aiuser prompt set <mention> <prompt>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Aliases: `custom and customize`
Extended Arg Info
> ### mention: Union[discord.member.Member, discord.role.Role, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType]
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
> ### prompt: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
### <@1275521742961508432>aiuser prompt show
Show the prompt for the server (or provided user/channel)<br/>
**Arguments**<br/>
    - `mention` *(Optional)* User or channel<br/>
 - Usage: `<@1275521742961508432>aiuser prompt show <mention>`
=======
### ,aiuser prompt preset
Manage presets for the current server<br/>
        <br/>
 - Usage: `,aiuser prompt preset`


#### ,aiuser prompt preset add
Add a new preset to the presets list<br/>

**Arguments**<br/>
    - `prompt` The prompt to set. Use `|` to separate the preset name (no spaces) from the prompt at the start. eg. `preset_name|prompt_text`<br/>
 - Usage: `,aiuser prompt preset add <prompt>`
 - Aliases: `a`
Extended Arg Info
> ### prompt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser prompt preset remove
Remove a preset by its name from the presets list<br/>

**Arguments**<br/>
    - `preset` The name of the preset to remove<br/>
 - Usage: `,aiuser prompt preset remove <preset>`
 - Aliases: `rm and delete`
Extended Arg Info
> ### preset: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### ,aiuser prompt preset show
Show all presets for the current server <br/>
 - Usage: `,aiuser prompt preset show`
 - Aliases: `list`


### ,aiuser prompt reset
Reset ALL prompts in this server to default (inc. channels and members) <br/>
 - Usage: `,aiuser prompt reset`


### ,aiuser prompt show
Show the prompt for the server (or provided user/channel)<br/>
**Arguments**<br/>
    - `mention` *(Optional)* User or channel<br/>
 - Usage: `,aiuser prompt show <mention>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### mention: Union[discord.member.Member, discord.role.Role, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType]
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


<<<<<<< HEAD
#### <@1275521742961508432>aiuser prompt show roles
Show all roles with custom prompts <br/>
 - Usage: `<@1275521742961508432>aiuser prompt show roles`


#### <@1275521742961508432>aiuser prompt show channels
Show all channels with custom prompts <br/>
 - Usage: `<@1275521742961508432>aiuser prompt show channels`


#### <@1275521742961508432>aiuser prompt show members
Show all users with custom prompts <br/>
 - Usage: `<@1275521742961508432>aiuser prompt show members`
 - Aliases: `users`


#### <@1275521742961508432>aiuser prompt show server
Show the current server prompt <br/>
 - Usage: `<@1275521742961508432>aiuser prompt show server`
 - Aliases: `server`


### <@1275521742961508432>aiuser prompt preset
Manage presets for the current server<br/>
        <br/>
 - Usage: `<@1275521742961508432>aiuser prompt preset`


#### <@1275521742961508432>aiuser prompt preset show
Show all presets for the current server <br/>
 - Usage: `<@1275521742961508432>aiuser prompt preset show`
 - Aliases: `list`


#### <@1275521742961508432>aiuser prompt preset remove
Remove a preset by its name from the presets list<br/>

**Arguments**<br/>
    - `preset` The name of the preset to remove<br/>
 - Usage: `<@1275521742961508432>aiuser prompt preset remove <preset>`
 - Aliases: `rm and delete`
Extended Arg Info
> ### preset: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>aiuser prompt preset add
Add a new preset to the presets list<br/>

**Arguments**<br/>
    - `prompt` The prompt to set. Use `|` to separate the preset name (no spaces) from the prompt at the start. eg. `preset_name|prompt_text`<br/>
 - Usage: `<@1275521742961508432>aiuser prompt preset add <prompt>`
 - Aliases: `a`
Extended Arg Info
> ### prompt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aiuser percent
=======
#### ,aiuser prompt show members
Show all users with custom prompts <br/>
 - Usage: `,aiuser prompt show members`
 - Aliases: `users`


#### ,aiuser prompt show channels
Show all channels with custom prompts <br/>
 - Usage: `,aiuser prompt show channels`


#### ,aiuser prompt show roles
Show all roles with custom prompts <br/>
 - Usage: `,aiuser prompt show roles`


#### ,aiuser prompt show server
Show the current server prompt <br/>
 - Usage: `,aiuser prompt show server`
 - Aliases: `server`


## ,aiuser percent
>>>>>>> 9e308722 (Revamped and Fixed)
Change the bot's response chance for a server (or a provided user, role, and channel)<br/>

If multiple percentage can be used, the most specific percentage will be used, eg. it will go for: member > role > channel > server<br/>

**Arguments**<br/>
    - `mention` (Optional) A mention of a user, role, or channel<br/>
    - `percent` (Optional) A number between 0 and 100, if omitted, will reset to using other percentages<br/>
(Setting is per server)<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>aiuser percent <mention> <percent>`
=======
 - Usage: `,aiuser percent <mention> <percent>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### mention: Union[discord.member.Member, discord.role.Role, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType]
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
> ### percent: Optional[float]
> ```
> A number with or without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>aiuser optin
Opt in of sending your messages / images to OpenAI or another endpoint (bot-wide)<br/>

This will allow the bot to reply to your messages or use your messages.<br/>
 - Usage: `<@1275521742961508432>aiuser optin`


## <@1275521742961508432>aiuser history
Change the prompt context settings for the current server<br/>

The most recent messages that are within the time gap and message limits are used to create context.<br/>
Context is used to help the LLM generate a response.<br/>
 - Usage: `<@1275521742961508432>aiuser history`
 - Restricted to: `BOT_OWNER`
 - Aliases: `context`


### <@1275521742961508432>aiuser history customtokenlimit
Set a LLM's custom maximum context limit (for local LLMs or those not listed in `aiuser/common/constants.py`.).<br/>

If not set, a safe default or saved limit from `aiuser/common/constants.py` is used.<br/>
 - Usage: `<@1275521742961508432>aiuser history customtokenlimit <new_value>`
Extended Arg Info
> ### new_value: Optional[int]
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>aiuser history time
Set max time (sec) messages can be apart before no more can be added<br/>

eg. if set to 60, once messsages are more than 60 seconds apart, more messages will not be added.<br/>

Helpful to prevent the LLM from mixing up context from different conversations.<br/>
 - Usage: `<@1275521742961508432>aiuser history time <new_value>`
 - Aliases: `gap`
Extended Arg Info
> ### new_value: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>aiuser history backread
Set max amount of messages to be used as context<br/>

(Increasing the number of messages will increase the cost of the response, messages will be added until the LLM's token limit is reached)<br/>
 - Usage: `<@1275521742961508432>aiuser history backread <new_value>`
 - Aliases: `messages and size`
Extended Arg Info
> ### new_value: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>aiuser imagerequest
Generate self-portrait images based on user request (on trigger words / LLM decision)<br/>

See [here](https://github.com/zhaobenny/bz-cogs/tree/main/aiuser#image-requests-%EF%B8%8F)<br/>

(All subcommands are per server)<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>aiuser imagerequest captionprompt
Set the prompt that creates the caption for the image generation<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest captionprompt <prompt>`
Extended Arg Info
> ### prompt: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser imagerequest parameters
Set compatible parameters (depends on interface, eg. see (https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for A1111)<br/>

Example command:<br/>
`<@1275521742961508432>aiuser imagerequest parameters ```{"sampler_name": "Euler a", "steps": 20}``` `<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest parameters <json_block>`
Extended Arg Info
> ### json_block: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser imagerequest config
Show current settings<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest config`


### <@1275521742961508432>aiuser imagerequest reduce_calls
Disables a LLM check on validating image requests<br/>

:warning: Will trigger image generation based ONLY on keywords instead of checking with the LLM<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest reduce_calls`


### <@1275521742961508432>aiuser imagerequest trigger
Set trigger words to detect image requests<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger`


#### <@1275521742961508432>aiuser imagerequest trigger sadd
Add a word to the second person words list (to replace with subject) <br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger sadd <word>`
 - Aliases: `addsecond`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>aiuser imagerequest trigger sremove
Remove a word from the second person words list<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger sremove <word>`
 - Aliases: `removesecond`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>aiuser imagerequest trigger clear
Clear the trigger words list to default<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger clear`


#### <@1275521742961508432>aiuser imagerequest trigger remove
Remove a word from the trigger words list<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger remove <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>aiuser imagerequest trigger sclear
Clear the second person words list to default<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger sclear`
 - Aliases: `clearsecond`


#### <@1275521742961508432>aiuser imagerequest trigger list
Show the trigger words list<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger list`
 - Aliases: `show`


#### <@1275521742961508432>aiuser imagerequest trigger slist
Show the second person words list<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger slist`
 - Aliases: `showsecond and sshow`


#### <@1275521742961508432>aiuser imagerequest trigger add
Add a word to the trigger words list<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest trigger add <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser imagerequest endpoint
Set compatible image generation endpoint (eg. for local A1111 include `/sdapi/v1/txt2img`)<br/>

If set to `dall-e-3` or `dall-e-2`, image requests will use OpenAI's DALL·E models at 1024x1024 SD resolution.<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest endpoint <url>`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser imagerequest toggle
Toggle requests to endpoint<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest toggle`


### <@1275521742961508432>aiuser imagerequest subject
The subject in Stable Diffusion requests (needed to better hint SD prompt generation by LLM)<br/>

If the subject is well known in the SD model, use it here eg. `katsuragi misato`<br/>
Else use a generic subject eg. `man` or `woman`<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest subject <subject>`
Extended Arg Info
> ### subject: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser imagerequest preprompt
This text will always be sent as part of the prompt in Stable Diffusion requests<br/>

(Set LORAs here if supported eg. `<lora: name: weight>`)<br/>
 - Usage: `<@1275521742961508432>aiuser imagerequest preprompt <preprompt>`
Extended Arg Info
> ### preprompt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aiuser forget
Forces the bot to forget the current conversation up to this point<br/>

This is useful if the LLM is stuck doing unwanted behaviour or giving undesirable results.<br/>
See `<@1275521742961508432>aiuser triggers public_forget` to allow non-admins to use this command.<br/>
 - Usage: `<@1275521742961508432>aiuser forget`
 - Aliases: `lobotomize`


## <@1275521742961508432>aiuser optout
Opt out of sending your messages / images to OpenAI or another endpoint (bot-wide)<br/>

This will prevent the bot from replying to your messages or using your messages.<br/>
 - Usage: `<@1275521742961508432>aiuser optout`


## <@1275521742961508432>aiuser optinbydefault
Toggles whether users are opted in by default in this server<br/>

This command is disabled for servers with more than 150 members.<br/>
 - Usage: `<@1275521742961508432>aiuser optinbydefault`
 - Restricted to: `ADMIN`


## <@1275521742961508432>aiuser response
Change settings used for generated responses<br/>

(All subcommands are per server)<br/>
 - Usage: `<@1275521742961508432>aiuser response`
 - Restricted to: `ADMIN`


### <@1275521742961508432>aiuser response removelist
Manage the list of regex patterns to remove from responses<br/>
        <br/>
 - Usage: `<@1275521742961508432>aiuser response removelist`


#### <@1275521742961508432>aiuser response removelist reset
Reset the list of regexes to default <br/>
 - Usage: `<@1275521742961508432>aiuser response removelist reset`


#### <@1275521742961508432>aiuser response removelist show
Show the current regex patterns of strings to removed from responses <br/>
 - Usage: `<@1275521742961508432>aiuser response removelist show`


#### <@1275521742961508432>aiuser response removelist add
Add a regex pattern to the list of patterns to remove from responses<br/>
 - Usage: `<@1275521742961508432>aiuser response removelist add <regex_pattern>`
Extended Arg Info
> ### regex_pattern: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>aiuser response removelist remove
Remove a regex pattern (by number) from the list<br/>
 - Usage: `<@1275521742961508432>aiuser response removelist remove <number>`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>aiuser response parameters
Set custom parameters for an endpoint using a JSON code block<br/>

To reset parameters to default, use `<@1275521742961508432>aiuser response parameters reset`<br/>
To show current parameters, use `<@1275521742961508432>aiuser response parameters show`<br/>

Example command:<br/>
`<@1275521742961508432>aiuser response parameters ```{"frequency_penalty": 2.0, "max_tokens": 200}``` `<br/>

See [here](https://platform.openai.com/docs/api-reference/chat/create) for possible parameters<br/>
Some parameters are blocked.<br/>
 - Usage: `<@1275521742961508432>aiuser response parameters <json_block>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### json_block: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser response toggleoptinembed
Toggles warning embed about opt-in on or off<br/>
 - Usage: `<@1275521742961508432>aiuser response toggleoptinembed`


### <@1275521742961508432>aiuser response weights
Bias the LLM for/against certain words (tokens)<br/>

See [here](https://help.openai.com/en/articles/5247780-using-logit-bias-to-define-token-probability) for additional info.<br/>

(All subcommands are per server)<br/>
 - Usage: `<@1275521742961508432>aiuser response weights`
 - Restricted to: `ADMIN`
 - Aliases: `logit_bias and bias`


#### <@1275521742961508432>aiuser response weights list
Show weights<br/>
 - Usage: `<@1275521742961508432>aiuser response weights list`
 - Aliases: `show`


#### <@1275521742961508432>aiuser response weights remove
Removes weight for a specific word<br/>

*Arguments*<br/>
    - `word` The word to remove<br/>
 - Usage: `<@1275521742961508432>aiuser response weights remove <word>`
 - Aliases: `delete`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


#### <@1275521742961508432>aiuser response weights add
Sets weight for a specific word<br/>

Will also use all possible tokens for a word when setting weight<br/>
See [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) for detailed text to token conversion.<br/>

*Arguments*<br/>
- `word` The word to set weight for<br/>
- `weight` The weight to set (`-100` to `100`)<br/>
 - Usage: `<@1275521742961508432>aiuser response weights add <word> <weight>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### weight: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>aiuser trigger
Configure trigger settings for the bot to respond to<br/>

(All subcommands per server)<br/>
 - Usage: `<@1275521742961508432>aiuser trigger`
 - Restricted to: `ADMIN`


### <@1275521742961508432>aiuser trigger conversation_reply_time
Set the max time frame in seconds for the bot to have a `conversation_reply_percent` chance of replying to a message <br/>
When `conversation_reply_time` have lapsed for the last bot message, `conversation_reply_percent` will not be used.<br/>
 - Usage: `<@1275521742961508432>aiuser trigger conversation_reply_time <seconds>`
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>aiuser trigger whitelist
If configured, only whitelisted roles / users can trigger a response in whitelisted channels<br/>
        <br/>
 - Usage: `<@1275521742961508432>aiuser trigger whitelist`
 - Aliases: `whitelists`


#### <@1275521742961508432>aiuser trigger whitelist add
Add a role/user to the whitelist <br/>
 - Usage: `<@1275521742961508432>aiuser trigger whitelist add <new>`
Extended Arg Info
> ### new: Union[discord.role.Role, discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


#### <@1275521742961508432>aiuser trigger whitelist clear
Clear the whitelist, allowing anyone to trigger LLM in whitelisted channels <br/>
 - Usage: `<@1275521742961508432>aiuser trigger whitelist clear`


#### <@1275521742961508432>aiuser trigger whitelist list
Show the whitelist <br/>
 - Usage: `<@1275521742961508432>aiuser trigger whitelist list`
 - Aliases: `show`


#### <@1275521742961508432>aiuser trigger whitelist remove
Remove a user/role from the whitelist <br/>
 - Usage: `<@1275521742961508432>aiuser trigger whitelist remove <rm>`
Extended Arg Info
> ### rm: Union[discord.role.Role, discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     


### <@1275521742961508432>aiuser trigger ignore
Messages matching this regex won't be replied to or seen, by the bot <br/>
 - Usage: `<@1275521742961508432>aiuser trigger ignore <regex_pattern>`
 - Aliases: `ignoreregex`
Extended Arg Info
> ### regex_pattern: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser trigger public_forget
Toggles whether anyone can use the forget command, or only moderators <br/>
 - Usage: `<@1275521742961508432>aiuser trigger public_forget`


### <@1275521742961508432>aiuser trigger conversation_reply_percent
Set a different percentage chance of the bot continuing to reply within `conversation_reply_time` time frame<br/>
 - Usage: `<@1275521742961508432>aiuser trigger conversation_reply_percent <percent>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### percent: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>aiuser trigger minlength
Set the minimum length of messages that the bot will respond to<br/>
 - Usage: `<@1275521742961508432>aiuser trigger minlength <length>`
 - Aliases: `min_length`
Extended Arg Info
> ### length: int
> ```
> A number without decimal places.
> ```


### <@1275521742961508432>aiuser trigger reply_to_mentions
Toggles if the bot will always reply to mentions/replies <br/>
 - Usage: `<@1275521742961508432>aiuser trigger reply_to_mentions`
 - Restricted to: `BOT_OWNER`
 - Aliases: `mentions_replies`


## <@1275521742961508432>aiuser imagescan
Change the image scan setting<br/>

Go [here](https://github.com/zhaobenny/bz-cogs/tree/main/aiuser#image-scanning-%EF%B8%8F) for more info.<br/>

(All subcommands are per server)<br/>
 - Usage: `<@1275521742961508432>aiuser imagescan`
 - Restricted to: `BOT_OWNER`


### <@1275521742961508432>aiuser imagescan maxsize
Set max download size in Megabytes for image scanning <br/>
 - Usage: `<@1275521742961508432>aiuser imagescan maxsize <size>`
Extended Arg Info
> ### size: float
> ```
> A number with or without decimal places.
> ```


### <@1275521742961508432>aiuser imagescan mode
Set method for scanning images<br/>


**Arguments**<br/>
- `mode` One of the following: `local`, `ai-horde`, `supported-llm`<br/>
 - Usage: `<@1275521742961508432>aiuser imagescan mode <mode>`
Extended Arg Info
> ### mode: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>aiuser imagescan toggle
Toggle image scanning <br/>
 - Usage: `<@1275521742961508432>aiuser imagescan toggle`


### <@1275521742961508432>aiuser imagescan model
Set the specific LLM used in the `supported-llm` mode<br/>


**Arguments**<br/>
    - `model_name` Name of a compatible model<br/>
 - Usage: `<@1275521742961508432>aiuser imagescan model <model_name>`
Extended Arg Info
> ### model_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>aiuser add
Adds a channel to the whitelist<br/>

**Arguments**<br/>
    - `channel` A mention of the channel<br/>
 - Usage: `<@1275521742961508432>aiuser add <channel>`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
=======
## ,aiuser optinbydefault
Toggles whether users are opted in by default in this server<br/>

This command is disabled for servers with more than 150 members.<br/>
 - Usage: `,aiuser optinbydefault`
 - Restricted to: `ADMIN`


## ,aiuser forget
Forces the bot to forget the current conversation up to this point<br/>

This is useful if the LLM is stuck doing unwanted behaviour or giving undesirable results.<br/>
See `,aiuser triggers public_forget` to allow non-admins to use this command.<br/>
 - Usage: `,aiuser forget`
 - Aliases: `lobotomize`
>>>>>>> 9e308722 (Revamped and Fixed)


