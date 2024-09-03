# Shell Help

### shell

**Description:** Run shell command.

**Usage:** `<@1275521742961508432>shell`

### shellq

**Description:** Run shell command quietly.

If command's exit code is 0, `[p]shellq` will only send a tick reaction.
Otherwise, the result will be shown as with regular `[p]shell` command.

**Usage:** `<@1275521742961508432>shellq`

### killshells

**Description:** Kill all shell processes started by Shell cog.

**Usage:** `<@1275521742961508432>killshells`

### shellset

**Description:** Manage settings of the Shell cog.

**Usage:** `<@1275521742961508432>shellset`

### shellset shell

**Description:** Set a replacement shell for the default ``/bin/sh``.

This needs to be a full path to the replacement shell.
The input is not validated.

Only works on POSIX systems.

**Usage:** `<@1275521742961508432>shellset shell`

### shellset shell reset

**Description:** Reset the replacement shell back to the default.

**Usage:** `<@1275521742961508432>shellset shell reset`

