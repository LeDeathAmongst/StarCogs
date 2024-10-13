Advanced channel and server locking.

# ,lock
Lock a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Examples:**<br/>
- `,lock #testing`<br/>
- `,lock 133251234164375552 @members`<br/>
 - Usage: `,lock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
## ,lock server
Lock the server.<br/>

Provide a role if you would like to lock if for that role.<br/>

**Example:**<br/>
- `,lock server @members`<br/>
 - Usage: `,lock server <roles>`
# ,unlock
Unlock a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Examples:**<br/>
- `,unlock #testing`<br/>
- `,unlock 133251234164375552 true`<br/>
 - Usage: `,unlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
## ,unlock server
Unlock the server.<br/>

Provide a role if you would unlock it for that role.<br/>

**Examples:**<br/>
- `,unlock server @members`<br/>
 - Usage: `,unlock server <roles>`
# ,viewlock
Prevent users from viewing a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Example:**<br/>
- `,viewlock #testing`<br/>
- `,viewlock 133251234164375552 @nubs`<br/>
 - Usage: `,viewlock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
# ,unviewlock
Allow users to view a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Example:**<br/>
- `,unviewlock #testing true`<br/>
- `,unviewlock 133251234164375552 @boosters`<br/>
 - Usage: `,unviewlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
