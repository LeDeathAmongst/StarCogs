# UpdateRed Help

### update

**Description:** Update Red with pip.

The optional `version` argument can be set to any one of the
following:
 - `stable` (default) - Update to the latest release on PyPI.
 - `pre` - Update to the latest pre-release, if available.
 - `dev` - Update from source control, i.e. V3/develop on
 GitHub.
 - Any specific version, e.g. `3.0.0b19`.

You may also specify any number of `extras`, which are extra
requirements you wish to install with Red. For example, to
update mongo requirements with Red, run the command with
`[p]update <version> mongo`.

Please note that when specifying any invalid arguments, the cog
will naively try to run the update command with those arguments,
possibly resulting in a misleading error message.

**Usage:** `<@1275521742961508432>update`

### urlupdate

**Description:** Update Red directly from a pip-installable URL.

**Usage:** `<@1275521742961508432>urlupdate`

