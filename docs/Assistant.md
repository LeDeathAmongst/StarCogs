# Assistant Help

### draw

**Description:** No description provided.

**Usage:** `<@1275521742961508432>draw`

### chathelp

**Description:** Get help using assistant

**Usage:** `<@1275521742961508432>chathelp`

### chat

**Description:** Chat with [botname]!

Conversations are *Per* user *Per* channel, meaning a conversation you have in one channel will be kept in memory separately from another conversation in a separate channel

**Optional Arguments**
`--outputfile <filename>` - uploads a file with the reply instead (no spaces)
`--extract` - extracts code blocks from the reply
`--last` - resends the last message of the conversation

**Example**
`[p]chat write a python script that prints "Hello World!"`
- Including `--outputfile hello.py` will output a file containing the whole response.
- Including `--outputfile hello.py --extract` will output a file containing just the code blocks and send the rest as text.
- Including `--extract` will send the code separately from the reply

**Usage:** `<@1275521742961508432>chat`

### convostats

**Description:** Check the token and message count of yourself or another user's conversation for this channel

Conversations are *Per* user *Per* channel, meaning a conversation you have in one channel will be kept in memory separately from another conversation in a separate channel

Conversations are only stored in memory until the bot restarts or the cog reloads

**Usage:** `<@1275521742961508432>convostats`

### convoclear

**Description:** Reset your conversation with the bot

This will clear all message history between you and the bot for this channel

**Usage:** `<@1275521742961508432>convoclear`

### convopop

**Description:** Pop the last message from your conversation

**Usage:** `<@1275521742961508432>convopop`

### convocopy

**Description:** Copy the conversation to another channel, thread, or forum

**Usage:** `<@1275521742961508432>convocopy`

### convoprompt

**Description:** Set a system prompt for this conversation!

This allows customization of assistant behavior on a per channel basis!

Check out [This Guide](https://platform.openai.com/docs/guides/prompt-engineering) for prompting help.

**Usage:** `<@1275521742961508432>convoprompt`

### convoshow

**Description:** View the current transcript of a conversation

This is mainly here for moderation purposes

**Usage:** `<@1275521742961508432>convoshow`

### query

**Description:** Fetch related embeddings according to the current topn setting along with their scores

You can use this to fine-tune the minimum relatedness for your assistant

**Usage:** `<@1275521742961508432>query`

### assistant

**Description:** Setup the assistant

You will need an **[api key](https://platform.openai.com/account/api-keys)** from OpenAI to use ChatGPT and their other models.

**Usage:** `<@1275521742961508432>assistant`

### assistant minlength

**Description:** set min character length for questions

Set to 0 to respond to anything

**Usage:** `<@1275521742961508432>assistant minlength`

### assistant wipecog

**Description:** Wipe all settings and data for entire cog

**Usage:** `<@1275521742961508432>assistant wipecog`

### assistant exportcsv

**Description:** Export embeddings to a .csv file

**Note:** csv exports do not include the embedding values

**Usage:** `<@1275521742961508432>assistant exportcsv`

### assistant frequency

**Description:** Set the frequency penalty for the model (-2.0 to 2.0)
- Defaults is 0

Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

**Usage:** `<@1275521742961508432>assistant frequency`

### assistant functioncalls

**Description:** Toggle whether GPT can call functions

**Usage:** `<@1275521742961508432>assistant functioncalls`

### assistant relatedness

**Description:** Set the minimum relatedness an embedding must be to include with the prompt

Relatedness threshold between 0 and 1 to include in embeddings during chat

Questions are converted to embeddings and compared against stored embeddings to pull the most relevant, this is the score that is derived from that comparison

**Hint**: The closer to 1 you get, the more deterministic and accurate the results may be, just don't be *too* strict or there wont be any results.

**Usage:** `<@1275521742961508432>assistant relatedness`

### assistant override

**Description:** Override settings for specific roles

**NOTE**
If a user has two roles with override settings, override associated with the higher role will be used.

**Usage:** `<@1275521742961508432>assistant override`

### assistant override model

**Description:** Assign a role to use a model

*Specify same role and model to remove the override*

**Usage:** `<@1275521742961508432>assistant override model`

### assistant override maxtime

**Description:** Assign a max retention time override to a role

*Specify same role and time to remove the override*

**Usage:** `<@1275521742961508432>assistant override maxtime`

### assistant override maxretention

**Description:** Assign a max message retention override to a role

*Specify same role and retention amount to remove the override*

**Usage:** `<@1275521742961508432>assistant override maxretention`

### assistant override maxresponsetokens

**Description:** Assign a max response token override to a role

Set to 0 for response tokens to be dynamic

*Specify same role and token count to remove the override*

**Usage:** `<@1275521742961508432>assistant override maxresponsetokens`

### assistant override maxtokens

**Description:** Assign a max token override to a role

*Specify same role and token count to remove the override*

**Usage:** `<@1275521742961508432>assistant override maxtokens`

### assistant openaikey

**Description:** Set your OpenAI key

**Usage:** `<@1275521742961508432>assistant openaikey`

### assistant resetglobalembeddings

**Description:** Wipe saved embeddings for all servers

This will delete any and all saved embedding training data for the assistant.

**Usage:** `<@1275521742961508432>assistant resetglobalembeddings`

### assistant questionmark

**Description:** Toggle whether questions need to end with **__?__**

**Usage:** `<@1275521742961508432>assistant questionmark`

### assistant importcsv

**Description:** Import embeddings to use with the assistant

Args:
    overwrite (bool): overwrite embeddings with existing entry names

This will read excel files too

**Usage:** `<@1275521742961508432>assistant importcsv`

### assistant collab

**Description:** Toggle collaborative conversations

Multiple people speaking in a channel will be treated as a single conversation.

**Usage:** `<@1275521742961508432>assistant collab`

### assistant sysoverride

**Description:** Toggle allowing per-conversation system prompt overriding

**Usage:** `<@1275521742961508432>assistant sysoverride`

### assistant maxrecursion

**Description:** Set the maximum function calls allowed in a row

This sets how many times the model can call functions in a row

Only the following models can call functions at the moment
- gpt-3.5-turbo
- gpt-3.5-turbo-16k
- gpt-4
- gpt-4-32k

**Usage:** `<@1275521742961508432>assistant maxrecursion`

### assistant embedmodel

**Description:** Set the OpenAI Embedding model to use

**Usage:** `<@1275521742961508432>assistant embedmodel`

### assistant exportjson

**Description:** Export embeddings to a json file

**Usage:** `<@1275521742961508432>assistant exportjson`

### assistant tutor

**Description:** Add/Remove items from the tutor list.

If using OpenAI's function calling and talking to a tutor, the AI is able to create its own embeddings to remember later

`role_or_member` can be a member or role

**Usage:** `<@1275521742961508432>assistant tutor`

### assistant backupcog

**Description:** Take a backup of the cog

- This does not backup conversation data

**Usage:** `<@1275521742961508432>assistant backupcog`

### assistant toggledraw

**Description:** Toggle the draw command on or off

**Usage:** `<@1275521742961508432>assistant toggledraw`

### assistant presence

**Description:** Set the presence penalty for the model (-2.0 to 2.0)
- Defaults is 0

Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

**Usage:** `<@1275521742961508432>assistant presence`

### assistant regexblacklist

**Description:** Remove certain words/phrases in the bot's responses

**Usage:** `<@1275521742961508432>assistant regexblacklist`

### assistant braveapikey

**Description:** Enables use of the `search_internet` function

Get your API key **[Here](https://brave.com/search/api/)**

**Usage:** `<@1275521742961508432>assistant braveapikey`

### assistant system

**Description:** Set the system prompt for GPT to use

Check out [This Guide](https://platform.openai.com/docs/guides/prompt-engineering) for prompting help.

**Placeholders**
- **botname**: [botname]
- **timestamp**: discord timestamp
- **day**: Mon-Sun
- **date**: MM-DD-YYYY
- **time**: HH:MM AM/PM
- **timetz**: HH:MM AM/PM Timezone
- **members**: server member count
- **username**: user's name
- **displayname**: user's display name
- **roles**: the names of the user's roles
- **rolementions**: the mentions of the user's roles
- **avatar**: the user's avatar url
- **owner**: the owner of the server
- **servercreated**: the create date/time of the server
- **server**: the name of the server
- **py**: python version
- **dpy**: discord.py version
- **red**: red version
- **cogs**: list of currently loaded cogs
- **channelname**: name of the channel the conversation is taking place in
- **channelmention**: current channel mention
- **topic**: topic of current channel (if not forum or thread)
- **banktype**: whether the bank is global or not
- **currency**: currency name
- **bank**: bank name
- **balance**: the user's current balance

**Usage:** `<@1275521742961508432>assistant system`

### assistant importjson

**Description:** Import embeddings to use with the assistant

Args:
    overwrite (bool): overwrite embeddings with existing entry names

**Usage:** `<@1275521742961508432>assistant importjson`

### assistant view

**Description:** View current settings

To send in current channel, use `[p]assistant view false`

**Usage:** `<@1275521742961508432>assistant view`

### assistant resolution

**Description:** Switch vision resolution between high and low for relevant GPT-4-Turbo models

**Usage:** `<@1275521742961508432>assistant resolution`

### assistant maxretention

**Description:** Set the max messages for a conversation

Conversation retention is cached and gets reset when the bot restarts or the cog reloads.

Regardless of this number, the initial prompt and internal system message are always included,
this only applies to any conversation between the user and bot after that.

Set to 0 to disable conversation retention

**Note:** *actual message count may exceed the max retention during an API call*

**Usage:** `<@1275521742961508432>assistant maxretention`

### assistant restorecog

**Description:** Restore the cog from a backup

**Usage:** `<@1275521742961508432>assistant restorecog`

### assistant timezone

**Description:** Set the timezone used for prompt placeholders

**Usage:** `<@1275521742961508432>assistant timezone`

### assistant resetembeddings

**Description:** Wipe saved embeddings for the assistant

This will delete any and all saved embedding training data for the assistant.

**Usage:** `<@1275521742961508432>assistant resetembeddings`

### assistant listentobots

**Description:** Toggle whether the assistant listens to other bots

**NOT RECOMMENDED FOR PUBLIC BOTS!**

**Usage:** `<@1275521742961508432>assistant listentobots`

### assistant seed

**Description:** Make the model more deterministic by setting a seed for the model.
- Default is None

If specified, the system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.

**Usage:** `<@1275521742961508432>assistant seed`

### assistant regexfailblock

**Description:** Toggle whether failed regex blocks the assistant's reply

Some regexes can cause [catastrophically backtracking](https://www.rexegg.com/regex-explosive-quantifiers.html)
The bot can safely handle if this happens and will either continue on, or block the response.

**Usage:** `<@1275521742961508432>assistant regexfailblock`

### assistant channel

**Description:** Set the channel for the assistant

**Usage:** `<@1275521742961508432>assistant channel`

### assistant maxtokens

**Description:** Set the max tokens that the bot will send to the model

**Tips**
- Max tokens are a soft cap, sometimes messages can be a little over
- If you set max tokens too high the cog will auto-adjust to 100 less than the models natural cap
- Ideally set max to 500 less than that models maximum, to allow adequate responses

Using more than the model can handle will raise exceptions.

**Usage:** `<@1275521742961508432>assistant maxtokens`

### assistant importexcel

**Description:** Import embeddings from an .xlsx file

Args:
    overwrite (bool): overwrite embeddings with existing entry names

**Usage:** `<@1275521742961508432>assistant importexcel`

### assistant channelprompt

**Description:** Set a channel specific system prompt

**Usage:** `<@1275521742961508432>assistant channelprompt`

### assistant maxtime

**Description:** Set the conversation expiration time

Regardless of this number, the initial prompt and internal system message are always included,
this only applies to any conversation between the user and bot after that.

Set to 0 to store conversations indefinitely or until the bot restarts or cog is reloaded

**Usage:** `<@1275521742961508432>assistant maxtime`

### assistant resetconversations

**Description:** Wipe saved conversations for the assistant in this server

This will delete any and all saved conversations for the assistant.

**Usage:** `<@1275521742961508432>assistant resetconversations`

### assistant resetglobalconversations

**Description:** Wipe saved conversations for the assistant in all servers

This will delete any and all saved conversations for the assistant.

**Usage:** `<@1275521742961508432>assistant resetglobalconversations`

### assistant prompt

**Description:** Set the initial prompt for GPT to use

Check out [This Guide](https://platform.openai.com/docs/guides/prompt-engineering) for prompting help.

**Placeholders**
- **botname**: [botname]
- **timestamp**: discord timestamp
- **day**: Mon-Sun
- **date**: MM-DD-YYYY
- **time**: HH:MM AM/PM
- **timetz**: HH:MM AM/PM Timezone
- **members**: server member count
- **username**: user's name
- **displayname**: user's display name
- **roles**: the names of the user's roles
- **rolementions**: the mentions of the user's roles
- **avatar**: the user's avatar url
- **owner**: the owner of the server
- **servercreated**: the create date/time of the server
- **server**: the name of the server
- **py**: python version
- **dpy**: discord.py version
- **red**: red version
- **cogs**: list of currently loaded cogs
- **channelname**: name of the channel the conversation is taking place in
- **channelmention**: current channel mention
- **topic**: topic of current channel (if not forum or thread)
- **banktype**: whether the bank is global or not
- **currency**: currency name
- **bank**: bank name
- **balance**: the user's current balance

**Usage:** `<@1275521742961508432>assistant prompt`

### assistant questionmode

**Description:** Toggle question mode

If question mode is on, embeddings will only be sourced during the first message of a conversation and messages that end in **?**

**Usage:** `<@1275521742961508432>assistant questionmode`

### assistant blacklist

**Description:** Add/Remove items from the blacklist

`channel_role_member` can be a member, role, channel, or category channel

**Usage:** `<@1275521742961508432>assistant blacklist`

### assistant mentionrespond

**Description:** Toggle whether the bot responds to mentions in any channel

**Usage:** `<@1275521742961508432>assistant mentionrespond`

### assistant maxresponsetokens

**Description:** Set the max response tokens the model can respond with

Set to 0 for response tokens to be dynamic

**Usage:** `<@1275521742961508432>assistant maxresponsetokens`

### assistant model

**Description:** Set the OpenAI model to use

**NOTE**
Specifying a model without it's identifier (like `gpt-3.5-turbo` instead of `gpt-3.5-turbo-0125`)
will sometimes lose the ability to call functions in parallel for some reason, this is an OpenAI issue.

**Usage:** `<@1275521742961508432>assistant model`

### assistant refreshembeds

**Description:** Refresh embedding weights

*This command can be used when changing the embedding model*

Embeddings that were created using OpenAI cannot be use with the self-hosted model and vice versa

**Usage:** `<@1275521742961508432>assistant refreshembeds`

### assistant resetusage

**Description:** Reset the token usage stats for this server

**Usage:** `<@1275521742961508432>assistant resetusage`

### assistant exportexcel

**Description:** Export embeddings to an .xlsx file

**Note:** csv exports do not include the embedding values

**Usage:** `<@1275521742961508432>assistant exportexcel`

### assistant temperature

**Description:** Set the temperature for the model (0.0 - 2.0)
- Defaults is 1

Closer to 0 is more concise and accurate while closer to 2 is more imaginative

**Usage:** `<@1275521742961508432>assistant temperature`

### assistant topn

**Description:** Set the embedding inclusion amout

Top N is the amount of embeddings to include with the initial prompt

**Usage:** `<@1275521742961508432>assistant topn`

### assistant persist

**Description:** Toggle persistent conversations

**Usage:** `<@1275521742961508432>assistant persist`

### assistant usage

**Description:** View the token usage stats for this server

**Usage:** `<@1275521742961508432>assistant usage`

### assistant channelpromptshow

**Description:** Show the channel specific system prompt

**Usage:** `<@1275521742961508432>assistant channelpromptshow`

### assistant toggle

**Description:** Toggle the assistant on or off

**Usage:** `<@1275521742961508432>assistant toggle`

### assistant embedmethod

**Description:** Cycle between embedding methods

**Dynamic** embeddings mean that the embeddings pulled are dynamically appended to the initial prompt for each individual question.
When each time the user asks a question, the previous embedding is replaced with embeddings pulled from the current question, this reduces token usage significantly

**Static** embeddings are applied in front of each user message and get stored with the conversation instead of being replaced with each question.

**Hybrid** embeddings are a combination, with the first embedding being stored in the conversation and the rest being dynamic, this saves a bit on token usage.

**User** embeddings are injected into the beginning of the prompt as the first user message.

Dynamic embeddings are helpful for Q&A, but not so much for chat when you need to retain the context pulled from the embeddings. The hybrid method is a good middle ground

**Usage:** `<@1275521742961508432>assistant embedmethod`

### assistant mention

**Description:** Toggle whether to ping the user on replies

**Usage:** `<@1275521742961508432>assistant mention`

### embeddings

**Description:** Manage embeddings for training

Embeddings are used to optimize training of the assistant and minimize token usage.

By using this the bot can store vast amounts of contextual information without going over the token limit.

**Note**
You can enter a search query with this command to bring up the menu and go directly to that embedding selection.

**Usage:** `<@1275521742961508432>embeddings`

### customfunctions

**Description:** Add custom function calls for Assistant to use

**READ**
- [Function Call Docs](https://platform.openai.com/docs/guides/gpt/function-calling)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb)
- [JSON Schema Reference](https://json-schema.org/understanding-json-schema/)

The following objects are passed by default as keyword arguments.
- **user**: the user currently chatting with the bot (discord.Member)
- **channel**: channel the user is chatting in (TextChannel|Thread|ForumChannel)
- **guild**: current guild (discord.Guild)
- **bot**: the bot object (Red)
- **conf**: the config model for Assistant (GuildSettings)
- All functions **MUST** include `*args, **kwargs` in the params and return a string
```python
# Can be either sync or async
async def func(*args, **kwargs) -> str:
```
Only bot owner can manage this, guild owners can see descriptions but not code

**Usage:** `<@1275521742961508432>customfunctions`

