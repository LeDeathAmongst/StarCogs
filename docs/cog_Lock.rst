Lock
====

Advanced channel and server locking.

# <@1275521742961508432>lock
Lock a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Examples:**<br/>
- `<@1275521742961508432>lock #testing`<br/>
- `<@1275521742961508432>lock 133251234164375552 @members`<br/>
 - Usage: `<@1275521742961508432>lock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


## <@1275521742961508432>lock server
Lock the server.<br/>

Provide a role if you would like to lock if for that role.<br/>

**Example:**<br/>
- `<@1275521742961508432>lock server @members`<br/>
 - Usage: `<@1275521742961508432>lock server <roles>`


# <@1275521742961508432>unlock
Unlock a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Examples:**<br/>
- `<@1275521742961508432>unlock #testing`<br/>
- `<@1275521742961508432>unlock 133251234164375552 true`<br/>
 - Usage: `<@1275521742961508432>unlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


## <@1275521742961508432>unlock server
Unlock the server.<br/>

Provide a role if you would unlock it for that role.<br/>

**Examples:**<br/>
- `<@1275521742961508432>unlock server @members`<br/>
 - Usage: `<@1275521742961508432>unlock server <roles>`


# <@1275521742961508432>viewlock
Prevent users from viewing a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Example:**<br/>
- `<@1275521742961508432>viewlock #testing`<br/>
- `<@1275521742961508432>viewlock 133251234164375552 @nubs`<br/>
 - Usage: `<@1275521742961508432>viewlock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


# <@1275521742961508432>unviewlock
Allow users to view a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Example:**<br/>
- `<@1275521742961508432>unviewlock #testing true`<br/>
- `<@1275521742961508432>unviewlock 133251234164375552 @boosters`<br/>
 - Usage: `<@1275521742961508432>unviewlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


