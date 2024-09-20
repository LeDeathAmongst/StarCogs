# System Help

### system

**Description:** Get information about your system metrics.

Most commands work on all OSes or omit certian information.
See the help for individual commands for detailed limitations.

**Usage:** `<@1275521742961508432>system`

### system all

**Description:** Get an overview of the current system metrics, similar to `top`.

This will show CPU utilisation, RAM usage and uptime as well as
active processes.

Platforms: Windows, Linux, Mac OS
Note: This command appears to be very slow in Windows.

**Usage:** `<@1275521742961508432>system all`

### system disk

**Description:** Get infomation about disks connected to the system.

This will show the space used, total space, filesystem and
mount point (if you're on Linux make sure it's not potentially
sensitive if running the command a public space).

If `ignore_loop` is set to `True`, this will ignore any loop (fake) devices on Linux.

Platforms: Windows, Linux, Mac OS
Note: Mount point is basically useless on Windows as it's the
same as the drive name, though it's still shown.

**Usage:** `<@1275521742961508432>system disk`

### system processes

**Description:** Get an overview of the status of currently running processes.

Platforms: Windows, Linux, Mac OS

**Usage:** `<@1275521742961508432>system processes`

### system sensors

**Description:** Get sensor metrics.

This will return any data about temperature and fan sensors it can find.
If there is no name for an individual sensor, it will use the name of the
group instead.

Platforms: Linux

**Usage:** `<@1275521742961508432>system sensors`

### system red

**Description:** See what resources [botname] is using.

Platforms: Windows, Linux, Mac OS
Note: SWAP memory information is only available on Linux.

**Usage:** `<@1275521742961508432>system red`

### system mem

**Description:** Get infomation about memory usage.

This will show memory available as a percent, memory used and available as well
as the total amount. Data is provided for both physical and SWAP RAM.

Platforms: Windows, Linux, Mac OS

**Usage:** `<@1275521742961508432>system mem`

### system network

**Description:** Get network stats. They may have overflowed and reset at some point.

Platforms: Windows, Linux, Mac OS

**Usage:** `<@1275521742961508432>system network`

### system cpu

**Description:** Get metrics about the CPU.

This will show the CPU usage as a percent for each core, and frequency depending on
platform.
It will also show the time spent idle, user and system as well as uptime.

Platforms: Windows, Linux, Mac OS
Note: CPU frequency is nominal and overall on Windows and Mac OS,
on Linux it's current and per-core.

**Usage:** `<@1275521742961508432>system cpu`

### system users

**Description:** Get information about logged in users.

This will show the user name, what terminal they're logged in at,
and when they logged in.

Platforms: Windows, Linux, Mac OS
Note: PID is not available on Windows. Terminal is usually `Unknown`

**Usage:** `<@1275521742961508432>system users`

### system uptime

**Description:** Get the system boot time and how long ago it was.

Platforms: Windows, Linux, Mac OS

**Usage:** `<@1275521742961508432>system uptime`

