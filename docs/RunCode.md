# RunCode Help

### runcode

**Description:** Run a code in a langage, with Wandbox API.

Arguments:
- `verbose`: Without this mode, only the programme output will be sent, without any additional information. In case of an error, it will be used automatically.
- `language`: If not specified, the command will try to "guess" with the file extension or Discord Markdown syntax.
- `parameters`: Optional option to send with the request. `engine:1/cpython-3.10.2`, `input:<input>`, `compiler_options:option1|option2|option3` and `runtime_options:option1|option2|option3`.
- `code`: May be normal code, but also an attached file, or a link from [pastebin](https://pastebin.com), [Github gist](https://gist.github.com) or another "raw" website.
          If you use a link, your command must end with this syntax: `link=<link>` (no space around `=`). You may also not provide it and upload an attachment instead.

**Usage:** `<@1275521742961508432>runcode`

### runtio

**Description:** Run a code in a langage, with Tio API.

Arguments:
- `verbose`: Without this mode, only the programme output will be sent, without any additional information. In case of an error, it will be used automatically.
- `language`: If not specified, the command will try to "guess" with the file extension or Discord Markdown syntax.
- `parameters`: Optional option to send with the request. `inputs:input1|input2|input3`, `compiler_flags:flag1|flag2|flag3`, `command_line_options:option1|option2|option3` and `args:arg1|arg2|arg3`.
- `code`: May be normal code, but also an attached file, or a link from [pastebin](https://pastebin.com), [Github gist](https://gist.github.com) or another "raw" website.
          If you use a link, your command must end with this syntax: `link=<link>` (no space around `=`). You may also not provide it and upload an attachment instead.

**Usage:** `<@1275521742961508432>runtio`

### setruncode

**Description:** View RunCode options.

**Usage:** `<@1275521742961508432>setruncode`

### setruncode listidentifiers

**Description:** Lists all the languages identifiers recognized by the bot, only for Wandbox API.

**Usage:** `<@1275521742961508432>setruncode listidentifiers`

### setruncode listengines

**Description:** Shows a list of all the available engines for a specified language, only for Wandbox API.

Arguments:
- `language`: The language name.

**Usage:** `<@1275521742961508432>setruncode listengines`

### setruncode listextensions

**Description:** Lists all the languages extensions.

**Usage:** `<@1275521742961508432>setruncode listextensions`

### setruncode listlanguages

**Description:** Shows a list of all the available languages, or Wandbox or Tio API.

**Usage:** `<@1275521742961508432>setruncode listlanguages`

