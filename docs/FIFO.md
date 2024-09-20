# FIFO Help

### fifoclear

**Description:** Debug command to clear all current fifo data

**Usage:** `<@1275521742961508432>fifoclear`

### fifo

**Description:** Base command for handling scheduling of tasks

**Usage:** `<@1275521742961508432>fifo`

### fifo set

**Description:** Sets a different author or in a different channel for execution of a task.

**Usage:** `<@1275521742961508432>fifo set`

### fifo add

**Description:** Add a new task to this guild's task list

**Usage:** `<@1275521742961508432>fifo add`

### fifo addtrigger

**Description:** Add a new trigger for a task from the current guild.

**Usage:** `<@1275521742961508432>fifo addtrigger`

### fifo addtrigger relative

**Description:** Add a "run once" trigger at a time relative from now to the specified task

**Usage:** `<@1275521742961508432>fifo addtrigger relative`

### fifo addtrigger cron

**Description:** Add a cron "time of day" trigger to the specified task

See https://crontab.guru/ for help generating the cron_str

**Usage:** `<@1275521742961508432>fifo addtrigger cron`

### fifo addtrigger interval

**Description:** Add an interval trigger to the specified task

**Usage:** `<@1275521742961508432>fifo addtrigger interval`

### fifo addtrigger date

**Description:** Add a "run once" datetime trigger to the specified task

**Usage:** `<@1275521742961508432>fifo addtrigger date`

### fifo list

**Description:** Lists all current tasks and their triggers.

Do `[p]fifo list True` to see tasks from all guilds

**Usage:** `<@1275521742961508432>fifo list`

### fifo pause

**Description:** Provide a task name to pause execution of a task

Otherwise pauses execution of all tasks on all guilds

**Usage:** `<@1275521742961508432>fifo pause`

### fifo delete

**Description:** Deletes a task from this guild's task list

**Usage:** `<@1275521742961508432>fifo delete`

### fifo printschedule

**Description:** Print the current schedule of execution.

Useful for debugging.

**Usage:** `<@1275521742961508432>fifo printschedule`

### fifo wakeup

**Description:** Debug command to fix missed executions.

If you see a negative "Next run time" when adding a trigger, this may help resolve it.
Check the logs when using this command.

**Usage:** `<@1275521742961508432>fifo wakeup`

### fifo cleartriggers

**Description:** Removes all triggers from specified task

Useful to start over with new trigger

**Usage:** `<@1275521742961508432>fifo cleartriggers`

### fifo checktask

**Description:** Returns the next 10 scheduled executions of the task

**Usage:** `<@1275521742961508432>fifo checktask`

### fifo details

**Description:** Provide all the details on the specified task name

**Usage:** `<@1275521742961508432>fifo details`

### fifo resume

**Description:** Provide a task name to resume execution of a task.

Otherwise resumes execution of all tasks on all guilds
If the task isn't currently scheduled, will schedule it

**Usage:** `<@1275521742961508432>fifo resume`

