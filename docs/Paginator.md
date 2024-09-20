# Paginator Help

### paginator

**Description:** Commands to manage paginators.

JSON example:
    https://pastebin.com/DiuFREBW

YAML example:
    https://pastebin.com/e9ZvhYUn

**Usage:** `<@1275521742961508432>paginator`

### paginator create

**Description:** Initiate a new paginator group.

**Usage:** `<@1275521742961508432>paginator create`

### paginator removepage

**Description:** Remove a page from a paginator group.

**Usage:** `<@1275521742961508432>paginator removepage`

### paginator info

**Description:** Get information about a paginator group.

**Usage:** `<@1275521742961508432>paginator info`

### paginator addpage

**Description:** Add a page to a paginator group.

**Usage:** `<@1275521742961508432>paginator addpage`

### paginator addpage fromjson

**Description:** Add a page to a paginator group.

The `page` argument should be a pastebin link containing valid json.
If `index` is not provided, the page will be added to the end of the paginator group.
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.

Example JSON: https://pastebin.com/DiuFREBW

**Usage:** `<@1275521742961508432>paginator addpage fromjson`

### paginator addpage fromyaml

**Description:** Add a page to a paginator group.

The `page` argument should be a pastebin link containing valid yaml.
If `index` is not provided, the page will be added to the end of the paginator group.
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.


Example YAML: https://pastebin.com/e9ZvhYUn

**Usage:** `<@1275521742961508432>paginator addpage fromyaml`

### paginator delete

**Description:** Delete a paginator group.

**Usage:** `<@1275521742961508432>paginator delete`

### paginator start

**Description:** Starts a paginator of the given group name

**Usage:** `<@1275521742961508432>paginator start`

### paginator editpage

**Description:** Edit a page in a paginator group.

**Usage:** `<@1275521742961508432>paginator editpage`

### paginator raw

**Description:** Get the raw JSON of a paginator group's page.

**Usage:** `<@1275521742961508432>paginator raw`

### paginator list

**Description:** List all paginator groups in the server.

**Usage:** `<@1275521742961508432>paginator list`

