# AIUser Help

### chat

**Description:** No description provided.

**Usage:** `<@1275521742961508432>chat`

### aiuserowner

**Description:** For some settings that apply bot-wide.

**Usage:** `<@1275521742961508432>aiuserowner`

### aiuserowner endpoint

**Description:** Sets the OpenAI endpoint to a custom one (must be OpenAI API compatible)

Reset to official OpenAI endpoint with `[p]aiuseradmin endpoint clear`

**Usage:** `<@1275521742961508432>aiuserowner endpoint`

### aiuserowner maxpromptlength

**Description:** Sets the maximum character length of a prompt that can set by admins in any server.

(Does not apply to already set prompts, only new ones)

**Usage:** `<@1275521742961508432>aiuserowner maxpromptlength`

### aiuserowner maxtopiclength

**Description:** Sets the maximum character length of a random prompt that can set by any server.

(Does not apply to already set prompts, only new ones)

**Usage:** `<@1275521742961508432>aiuserowner maxtopiclength`

### aiuserowner exportconfig

**Description:** Exports the current config to a json file

:warning: JSON backend only

**Usage:** `<@1275521742961508432>aiuserowner exportconfig`

### aiuserowner prompt

**Description:** Set the global default prompt for aiuser.

Leave blank to delete the currently set global prompt, and use the build-in default prompt.

**Arguments**
    - `prompt` The prompt to set.

**Usage:** `<@1275521742961508432>aiuserowner prompt`

### aiuserowner importconfig

**Description:** Imports a config from json file (:warning: No checks are done)

 Make sure your new config is valid, and the old config is backed up.

:warning: JSON backend only

**Usage:** `<@1275521742961508432>aiuserowner importconfig`

### aiuserowner timeout

**Description:** Sets the request timeout to the OpenAI endpoint 

**Usage:** `<@1275521742961508432>aiuserowner timeout`

### aiuser

**Description:** Utilize OpenAI to reply to messages and images in approved channels and by opt-in users

**Usage:** `<@1275521742961508432>aiuser`

### aiuser forget

**Description:** Forces the bot to forget the current conversation up to this point

This is useful if the LLM is stuck doing unwanted behaviour or giving undesirable results.
See `[p]aiuser triggers public_forget` to allow non-admins to use this command.

**Usage:** `<@1275521742961508432>aiuser forget`

### aiuser response

**Description:** Change settings used for generated responses

(All subcommands are per server)

**Usage:** `<@1275521742961508432>aiuser response`

### aiuser response parameters

**Description:** Set custom parameters for an endpoint using a JSON code block

To reset parameters to default, use `[p]aiuser response parameters reset`
To show current parameters, use `[p]aiuser response parameters show`

Example command:
`[p]aiuser response parameters ```{"frequency_penalty": 2.0, "max_tokens": 200}``` `

See [here](https://platform.openai.com/docs/api-reference/chat/create) for possible parameters
Some parameters are blocked.

**Usage:** `<@1275521742961508432>aiuser response parameters`

### aiuser response toggleoptinembed

**Description:** Toggles warning embed about opt-in on or off

**Usage:** `<@1275521742961508432>aiuser response toggleoptinembed`

### aiuser response removelist

**Description:** Manage the list of regex patterns to remove from responses
        

**Usage:** `<@1275521742961508432>aiuser response removelist`

### aiuser response removelist reset

**Description:** Reset the list of regexes to default 

**Usage:** `<@1275521742961508432>aiuser response removelist reset`

### aiuser response removelist add

**Description:** Add a regex pattern to the list of patterns to remove from responses

**Usage:** `<@1275521742961508432>aiuser response removelist add`

### aiuser response removelist show

**Description:** Show the current regex patterns of strings to removed from responses 

**Usage:** `<@1275521742961508432>aiuser response removelist show`

### aiuser response removelist remove

**Description:** Remove a regex pattern (by number) from the list

**Usage:** `<@1275521742961508432>aiuser response removelist remove`

### aiuser response weights

**Description:** Bias the LLM for/against certain words (tokens)

See [here](https://help.openai.com/en/articles/5247780-using-logit-bias-to-define-token-probability) for additional info.

(All subcommands are per server)

**Usage:** `<@1275521742961508432>aiuser response weights`

### aiuser response weights add

**Description:** Sets weight for a specific word

Will also use all possible tokens for a word when setting weight
See [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) for detailed text to token conversion.

*Arguments*
- `word` The word to set weight for
- `weight` The weight to set (`-100` to `100`)

**Usage:** `<@1275521742961508432>aiuser response weights add`

### aiuser response weights remove

**Description:** Removes weight for a specific word

*Arguments*
    - `word` The word to remove

**Usage:** `<@1275521742961508432>aiuser response weights remove`

### aiuser response weights list

**Description:** Show weights

**Usage:** `<@1275521742961508432>aiuser response weights list`

### aiuser add

**Description:** Adds a channel to the whitelist

**Arguments**
    - `channel` A mention of the channel

**Usage:** `<@1275521742961508432>aiuser add`

### aiuser percent

**Description:** Change the bot's response chance for a server (or a provided user, role, and channel)

If multiple percentage can be used, the most specific percentage will be used, eg. it will go for: member > role > channel > server

**Arguments**
    - `mention` (Optional) A mention of a user, role, or channel
    - `percent` (Optional) A number between 0 and 100, if omitted, will reset to using other percentages
(Setting is per server)

**Usage:** `<@1275521742961508432>aiuser percent`

### aiuser imagerequest

**Description:** Generate self-portrait images based on user request (on trigger words / LLM decision)

See [here](https://github.com/zhaobenny/bz-cogs/tree/main/aiuser#image-requests-%EF%B8%8F)

(All subcommands are per server)

**Usage:** `<@1275521742961508432>aiuser imagerequest`

### aiuser imagerequest toggle

**Description:** Toggle requests to endpoint

**Usage:** `<@1275521742961508432>aiuser imagerequest toggle`

### aiuser imagerequest subject

**Description:** The subject in Stable Diffusion requests (needed to better hint SD prompt generation by LLM)

If the subject is well known in the SD model, use it here eg. `katsuragi misato`
Else use a generic subject eg. `man` or `woman`

**Usage:** `<@1275521742961508432>aiuser imagerequest subject`

### aiuser imagerequest trigger

**Description:** Set trigger words to detect image requests

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger`

### aiuser imagerequest trigger list

**Description:** Show the trigger words list

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger list`

### aiuser imagerequest trigger sclear

**Description:** Clear the second person words list to default

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger sclear`

### aiuser imagerequest trigger add

**Description:** Add a word to the trigger words list

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger add`

### aiuser imagerequest trigger slist

**Description:** Show the second person words list

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger slist`

### aiuser imagerequest trigger sadd

**Description:** Add a word to the second person words list (to replace with subject) 

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger sadd`

### aiuser imagerequest trigger sremove

**Description:** Remove a word from the second person words list

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger sremove`

### aiuser imagerequest trigger clear

**Description:** Clear the trigger words list to default

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger clear`

### aiuser imagerequest trigger remove

**Description:** Remove a word from the trigger words list

**Usage:** `<@1275521742961508432>aiuser imagerequest trigger remove`

### aiuser imagerequest preprompt

**Description:** This text will always be sent as part of the prompt in Stable Diffusion requests

(Set LORAs here if supported eg. `<lora: name: weight>`)

**Usage:** `<@1275521742961508432>aiuser imagerequest preprompt`

### aiuser imagerequest config

**Description:** Show current settings

**Usage:** `<@1275521742961508432>aiuser imagerequest config`

### aiuser imagerequest parameters

**Description:** Set compatible parameters (depends on interface, eg. see [here](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for A1111)

Example command:
`[p]aiuser imagerequest parameters ```{"sampler_name": "Euler a", "steps": 20}``` `

**Usage:** `<@1275521742961508432>aiuser imagerequest parameters`

### aiuser imagerequest reduce_calls

**Description:** Disables a LLM check on validating image requests

:warning: Will trigger image generation based ONLY on keywords instead of checking with the LLM

**Usage:** `<@1275521742961508432>aiuser imagerequest reduce_calls`

### aiuser imagerequest endpoint

**Description:** Set compatible image generation endpoint (eg. for local A1111 include `/sdapi/v1/txt2img`)

If set to `dall-e-3` or `dall-e-2`, image requests will use OpenAI's DALL·E models at 1024x1024 SD resolution.

**Usage:** `<@1275521742961508432>aiuser imagerequest endpoint`

### aiuser optout

**Description:** Opt out of sending your messages / images to OpenAI or another endpoint (bot-wide)

This will prevent the bot from replying to your messages or using your messages.

**Usage:** `<@1275521742961508432>aiuser optout`

### aiuser optinbydefault

**Description:** Toggles whether users are opted in by default in this server

This command is disabled for servers with more than 150 members.

**Usage:** `<@1275521742961508432>aiuser optinbydefault`

### aiuser imagescan

**Description:** Change the image scan setting

Go [here](https://github.com/zhaobenny/bz-cogs/tree/main/aiuser#image-scanning-%EF%B8%8F) for more info.

(All subcommands are per server)

**Usage:** `<@1275521742961508432>aiuser imagescan`

### aiuser imagescan mode

**Description:** Set method for scanning images


**Arguments**
- `mode` One of the following: `local`, `ai-horde`, `supported-llm`

**Usage:** `<@1275521742961508432>aiuser imagescan mode`

### aiuser imagescan maxsize

**Description:** Set max download size in Megabytes for image scanning 

**Usage:** `<@1275521742961508432>aiuser imagescan maxsize`

### aiuser imagescan model

**Description:** Set the specific LLM used in the `supported-llm` mode


**Arguments**
    - `model_name` Name of a compatible model

**Usage:** `<@1275521742961508432>aiuser imagescan model`

### aiuser imagescan toggle

**Description:** Toggle image scanning 

**Usage:** `<@1275521742961508432>aiuser imagescan toggle`

### aiuser trigger

**Description:** Configure trigger settings for the bot to respond to

(All subcommands per server)

**Usage:** `<@1275521742961508432>aiuser trigger`

### aiuser trigger public_forget

**Description:** Toggles whether anyone can use the forget command, or only moderators 

**Usage:** `<@1275521742961508432>aiuser trigger public_forget`

### aiuser trigger minlength

**Description:** Set the minimum length of messages that the bot will respond to

**Usage:** `<@1275521742961508432>aiuser trigger minlength`

### aiuser trigger reply_to_mentions

**Description:** Toggles if the bot will always reply to mentions/replies 

**Usage:** `<@1275521742961508432>aiuser trigger reply_to_mentions`

### aiuser trigger conversation_reply_percent

**Description:** Set a different percentage chance of the bot continuing to reply within `conversation_reply_time` time frame

**Usage:** `<@1275521742961508432>aiuser trigger conversation_reply_percent`

### aiuser trigger whitelist

**Description:** If configured, only whitelisted roles / users can trigger a response in whitelisted channels
        

**Usage:** `<@1275521742961508432>aiuser trigger whitelist`

### aiuser trigger whitelist list

**Description:** Show the whitelist 

**Usage:** `<@1275521742961508432>aiuser trigger whitelist list`

### aiuser trigger whitelist clear

**Description:** Clear the whitelist, allowing anyone to trigger LLM in whitelisted channels 

**Usage:** `<@1275521742961508432>aiuser trigger whitelist clear`

### aiuser trigger whitelist add

**Description:** Add a role/user to the whitelist 

**Usage:** `<@1275521742961508432>aiuser trigger whitelist add`

### aiuser trigger whitelist remove

**Description:** Remove a user/role from the whitelist 

**Usage:** `<@1275521742961508432>aiuser trigger whitelist remove`

### aiuser trigger conversation_reply_time

**Description:** Set the max time frame in seconds for the bot to have a `conversation_reply_percent` chance of replying to a message 
When `conversation_reply_time` have lapsed for the last bot message, `conversation_reply_percent` will not be used.

**Usage:** `<@1275521742961508432>aiuser trigger conversation_reply_time`

### aiuser trigger ignore

**Description:** Messages matching this regex won't be replied to or seen, by the bot 

**Usage:** `<@1275521742961508432>aiuser trigger ignore`

### aiuser config

**Description:** Returns current config

(Current config per server)

**Usage:** `<@1275521742961508432>aiuser config`

### aiuser functions

**Description:** Settings to manage function calling

(All subcommands are per server)

**Usage:** `<@1275521742961508432>aiuser functions`

### aiuser functions location

**Description:** Set the location where the bot will canonically be in

Used for some functions.

**Arguments**
- `latitude` decimal latitude
- `longitude` decimal longitude

**Usage:** `<@1275521742961508432>aiuser functions location`

### aiuser functions noresponse

**Description:** Enable/disable the functionality for the LLM to choose to not respond and ignore messages.

Temperamental, may require additional prompting to work better.

**Usage:** `<@1275521742961508432>aiuser functions noresponse`

### aiuser functions weather

**Description:** Enable/disable a group of functions to getting weather using Open-Meteo

See [Open-Meteo terms](https://open-meteo.com/en/terms) for their free API

**Usage:** `<@1275521742961508432>aiuser functions weather`

### aiuser functions scrape

**Description:** Enable/disable the functionality for the LLM to open URLs in messages

(May not be called if the link generated an Discord embed)

**Usage:** `<@1275521742961508432>aiuser functions scrape`

### aiuser functions search

**Description:** Enable/disable searching/scraping the Internet using Serper.dev 

**Usage:** `<@1275521742961508432>aiuser functions search`

### aiuser functions toggle

**Description:** Toggle functions calling

Requires a model that is whitelisted for function calling
If enabled, the LLM will call functions to generate responses when needed
This will generate additional API calls and token usage!

**Usage:** `<@1275521742961508432>aiuser functions toggle`

### aiuser remove

**Description:** Remove a channel from the whitelist

**Arguments**
    - `channel` A mention of the channel

**Usage:** `<@1275521742961508432>aiuser remove`

### aiuser randommessage

**Description:** Configure the random message event
**(Must be enabled by bot owner first using `[p]aiuser random toggle`)**

Every 33 minutes, a RNG roll will determine if a random message will be sent using a random prompt from a given list.

Whitelisted channels must have a hour pass without a message sent in it for a random message to be sent. Last message author must not be this bot.

(All subcommands per server)

**Usage:** `<@1275521742961508432>aiuser randommessage`

### aiuser randommessage remove

**Description:** Removes a prompt (by number) from the list

**Usage:** `<@1275521742961508432>aiuser randommessage remove`

### aiuser randommessage add

**Description:** Add a new prompt to be used in random messages

**Usage:** `<@1275521742961508432>aiuser randommessage add`

### aiuser randommessage percent

**Description:** Sets the chance that a random message will be sent every 33 minutes

**Arguments**
    - `percent` A number between 0 and 100

**Usage:** `<@1275521742961508432>aiuser randommessage percent`

### aiuser randommessage show

**Description:** Lists prompts to used in random messages 

**Usage:** `<@1275521742961508432>aiuser randommessage show`

### aiuser randommessage toggle

**Description:** Toggles random message events 

**Usage:** `<@1275521742961508432>aiuser randommessage toggle`

### aiuser randommessage reset

**Description:** Resets the random prompt list to the default

**Usage:** `<@1275521742961508432>aiuser randommessage reset`

### aiuser model

**Description:** Changes chat completion model

 To see a list of available models, use `[p]aiuser model list`
 (Setting is per server)

**Arguments**
    - `model` The model to use eg. `gpt-4`

**Usage:** `<@1275521742961508432>aiuser model`

### aiuser optin

**Description:** Opt in of sending your messages / images to OpenAI or another endpoint (bot-wide)

This will allow the bot to reply to your messages or use your messages.

**Usage:** `<@1275521742961508432>aiuser optin`

### aiuser prompt

**Description:** Change the prompt settings for the current server

(All subcommands are per server)

**Usage:** `<@1275521742961508432>aiuser prompt`

### aiuser prompt show

**Description:** Show the prompt for the server (or provided user/channel)
**Arguments**
    - `mention` *(Optional)* User or channel

**Usage:** `<@1275521742961508432>aiuser prompt show`

### aiuser prompt show server

**Description:** Show the current server prompt 

**Usage:** `<@1275521742961508432>aiuser prompt show server`

### aiuser prompt show channels

**Description:** Show all channels with custom prompts 

**Usage:** `<@1275521742961508432>aiuser prompt show channels`

### aiuser prompt show members

**Description:** Show all users with custom prompts 

**Usage:** `<@1275521742961508432>aiuser prompt show members`

### aiuser prompt show roles

**Description:** Show all roles with custom prompts 

**Usage:** `<@1275521742961508432>aiuser prompt show roles`

### aiuser prompt set

**Description:** Set a custom prompt or preset for the server (or provided channel/role/member)

If multiple prompts can be used, the most specific prompt will be used, eg. it will go for: member > role > channel > server

**Arguments**
    - `mention` *(Optional)* A specific user or channel
    - `prompt` *(Optional)* The prompt (or name of a preset) to set. If blank, will remove current prompt.
    - `<ATTACHMENT>` *(Optional)* An `.txt` file to use as the prompt

**Usage:** `<@1275521742961508432>aiuser prompt set`

### aiuser prompt reset

**Description:** Reset ALL prompts in this guild to default (inc. channels and members) 

**Usage:** `<@1275521742961508432>aiuser prompt reset`

### aiuser prompt preset

**Description:** Manage presets for the current server
        

**Usage:** `<@1275521742961508432>aiuser prompt preset`

### aiuser prompt preset show

**Description:** Show all presets for the current server 

**Usage:** `<@1275521742961508432>aiuser prompt preset show`

### aiuser prompt preset add

**Description:** Add a new preset to the presets list

**Arguments**
    - `prompt` The prompt to set. Use `|` to separate the preset name (no spaces) from the prompt at the start. eg. `preset_name|prompt_text`

**Usage:** `<@1275521742961508432>aiuser prompt preset add`

### aiuser prompt preset remove

**Description:** Remove a preset by its name from the presets list

**Arguments**
    - `preset` The name of the preset to remove

**Usage:** `<@1275521742961508432>aiuser prompt preset remove`

### aiuser history

**Description:** Change the prompt context settings for the current server

The most recent messages that are within the time gap and message limits are used to create context.
Context is used to help the LLM generate a response.

**Usage:** `<@1275521742961508432>aiuser history`

### aiuser history backread

**Description:** Set max amount of messages to be used as context

(Increasing the number of messages will increase the cost of the response, messages will be added until the LLM's token limit is reached)

**Usage:** `<@1275521742961508432>aiuser history backread`

### aiuser history time

**Description:** Set max time (sec) messages can be apart before no more can be added

eg. if set to 60, once messsages are more than 60 seconds apart, more messages will not be added.

Helpful to prevent the LLM from mixing up context from different conversations.

**Usage:** `<@1275521742961508432>aiuser history time`

### aiuser history customtokenlimit

**Description:** Set a LLM's custom maximum context limit (for local LLMs or those not listed in `aiuser/common/constants.py`.).

If not set, a safe default or saved limit from `aiuser/common/constants.py` is used.

**Usage:** `<@1275521742961508432>aiuser history customtokenlimit`

