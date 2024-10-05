FIFO
====

Simple Scheduling Cog

Named after the simplest scheduling algorithm: First In First Out

# <@1275521742961508432>fifoclear
Debug command to clear all current fifo data<br/>
 - Usage: `<@1275521742961508432>fifoclear`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


# <@1275521742961508432>fifo
Base command for handling scheduling of tasks<br/>
 - Usage: `<@1275521742961508432>fifo`
 - Restricted to: `BOT_OWNER`
 - Checks: `server_only`


## <@1275521742961508432>fifo printschedule
Print the current schedule of execution.<br/>

Useful for debugging.<br/>
 - Usage: `<@1275521742961508432>fifo printschedule`


## <@1275521742961508432>fifo add
Add a new task to this server's task list<br/>
 - Usage: `<@1275521742961508432>fifo add <task_name> <command_to_execute>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### command_to_execute: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>fifo wakeup
Debug command to fix missed executions.<br/>

If you see a negative "Next run time" when adding a trigger, this may help resolve it.<br/>
Check the logs when using this command.<br/>
 - Usage: `<@1275521742961508432>fifo wakeup`


## <@1275521742961508432>fifo set
Sets a different author or in a different channel for execution of a task.<br/>
 - Usage: `<@1275521742961508432>fifo set <task_name> <author_or_channel>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### author_or_channel: Union[discord.member.Member, discord.channel.TextChannel]
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


## <@1275521742961508432>fifo addtrigger
Add a new trigger for a task from the current server.<br/>
 - Usage: `<@1275521742961508432>fifo addtrigger`
 - Aliases: `trigger`


### <@1275521742961508432>fifo addtrigger relative
Add a "run once" trigger at a time relative from now to the specified task<br/>
 - Usage: `<@1275521742961508432>fifo addtrigger relative <task_name> <time_from_now>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>fifo addtrigger interval
Add an interval trigger to the specified task<br/>
 - Usage: `<@1275521742961508432>fifo addtrigger interval <task_name> <interval_str>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>fifo addtrigger date
Add a "run once" datetime trigger to the specified task<br/>
 - Usage: `<@1275521742961508432>fifo addtrigger date <task_name> <datetime_str>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


### <@1275521742961508432>fifo addtrigger cron
Add a cron "time of day" trigger to the specified task<br/>

See https://crontab.guru/ for help generating the cron_str<br/>
 - Usage: `<@1275521742961508432>fifo addtrigger cron <task_name> [optional_tz=None] <cron_str>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>fifo resume
Provide a task name to resume execution of a task.<br/>

Otherwise resumes execution of all tasks on all servers<br/>
If the task isn't currently scheduled, will schedule it<br/>
 - Usage: `<@1275521742961508432>fifo resume [task_name=None]`
Extended Arg Info
> ### task_name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>fifo pause
Provide a task name to pause execution of a task<br/>

Otherwise pauses execution of all tasks on all servers<br/>
 - Usage: `<@1275521742961508432>fifo pause [task_name=None]`
Extended Arg Info
> ### task_name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>fifo details
Provide all the details on the specified task name<br/>
 - Usage: `<@1275521742961508432>fifo details <task_name>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>fifo list
Lists all current tasks and their triggers.<br/>

Do `<@1275521742961508432>fifo list True` to see tasks from all servers<br/>
 - Usage: `<@1275521742961508432>fifo list [all_servers=False]`
Extended Arg Info
> ### all_servers: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```


## <@1275521742961508432>fifo cleartriggers
Removes all triggers from specified task<br/>

Useful to start over with new trigger<br/>
 - Usage: `<@1275521742961508432>fifo cleartriggers <task_name>`
 - Aliases: `cleartrigger`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>fifo checktask
Returns the next 10 scheduled executions of the task<br/>
 - Usage: `<@1275521742961508432>fifo checktask <task_name>`
 - Aliases: `checkjob and check`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


## <@1275521742961508432>fifo delete
Deletes a task from this server's task list<br/>
 - Usage: `<@1275521742961508432>fifo delete <task_name>`
Extended Arg Info
> ### task_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


