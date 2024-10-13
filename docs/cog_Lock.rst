Lock
====

Advanced channel and server locking.

<<<<<<< HEAD
# <@1275521742961508432>lock
=======
# ,lock
>>>>>>> 9e308722 (Revamped and Fixed)
Lock a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Examples:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>lock #testing`<br/>
- `<@1275521742961508432>lock 133251234164375552 @members`<br/>
 - Usage: `<@1275521742961508432>lock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


## <@1275521742961508432>lock server
=======
- `,lock #testing`<br/>
- `,lock 133251234164375552 @members`<br/>
 - Usage: `,lock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


## ,lock server
>>>>>>> 9e308722 (Revamped and Fixed)
Lock the server.<br/>

Provide a role if you would like to lock if for that role.<br/>

**Example:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>lock server @members`<br/>
 - Usage: `<@1275521742961508432>lock server <roles>`


# <@1275521742961508432>unlock
=======
- `,lock server @members`<br/>
 - Usage: `,lock server <roles>`


# ,unlock
>>>>>>> 9e308722 (Revamped and Fixed)
Unlock a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Examples:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>unlock #testing`<br/>
- `<@1275521742961508432>unlock 133251234164375552 true`<br/>
 - Usage: `<@1275521742961508432>unlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


## <@1275521742961508432>unlock server
=======
- `,unlock #testing`<br/>
- `,unlock 133251234164375552 true`<br/>
 - Usage: `,unlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


## ,unlock server
>>>>>>> 9e308722 (Revamped and Fixed)
Unlock the server.<br/>

Provide a role if you would unlock it for that role.<br/>

**Examples:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>unlock server @members`<br/>
 - Usage: `<@1275521742961508432>unlock server <roles>`


# <@1275521742961508432>viewlock
=======
- `,unlock server @members`<br/>
 - Usage: `,unlock server <roles>`


# ,viewlock
>>>>>>> 9e308722 (Revamped and Fixed)
Prevent users from viewing a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Example:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>viewlock #testing`<br/>
- `<@1275521742961508432>viewlock 133251234164375552 @nubs`<br/>
 - Usage: `<@1275521742961508432>viewlock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


# <@1275521742961508432>unviewlock
=======
- `,viewlock #testing`<br/>
- `,viewlock 133251234164375552 @nubs`<br/>
 - Usage: `,viewlock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`


# ,unviewlock
>>>>>>> 9e308722 (Revamped and Fixed)
Allow users to view a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Example:**<br/>
<<<<<<< HEAD
- `<@1275521742961508432>unviewlock #testing true`<br/>
- `<@1275521742961508432>unviewlock 133251234164375552 @boosters`<br/>
 - Usage: `<@1275521742961508432>unviewlock [channel=None] [state=None] [roles_or_members=None]`
=======
- `,unviewlock #testing true`<br/>
- `,unviewlock 133251234164375552 @boosters`<br/>
 - Usage: `,unviewlock [channel=None] [state=None] [roles_or_members=None]`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `ADMIN`


