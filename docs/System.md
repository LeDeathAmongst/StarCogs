Get system metrics.<br/><br/>Most commands work on all OSes or omit certian information.<br/>See the help for individual commands for detailed limitations.

# ,systeminfo

 - Usage: `,systeminfo`
# ,system
Get information about your system metrics.<br/>

Most commands work on all OSes or omit certian information.<br/>
See the help for individual commands for detailed limitations.<br/>
 - Usage: `,system`
## ,system sensors
Get sensor metrics.<br/>

This will return any data about temperature and fan sensors it can find.<br/>
If there is no name for an individual sensor, it will use the name of the<br/>
group instead.<br/>

Platforms: Linux<br/>
 - Usage: `,system sensors [fahrenheit=False]`
 - Aliases: `temp, temperature, fan, and fans`
Extended Arg Info
> ### fahrenheit: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## ,system red
See what resources Starfire is using.<br/>

Platforms: Windows, Linux, Mac OS<br/>
Note: SWAP memory information is only available on Linux.<br/>
 - Usage: `,system red`
## ,system processes
Get an overview of the status of currently running processes.<br/>

Platforms: Windows, Linux, Mac OS<br/>
 - Usage: `,system processes`
 - Aliases: `proc`
## ,system all
Get an overview of the current system metrics, similar to `top`.<br/>

This will show CPU utilisation, RAM usage and uptime as well as<br/>
active processes.<br/>

Platforms: Windows, Linux, Mac OS<br/>
Note: This command appears to be very slow in Windows.<br/>
 - Usage: `,system all`
 - Aliases: `overview and top`
## ,system network
Get network stats. They may have overflowed and reset at some point.<br/>

Platforms: Windows, Linux, Mac OS<br/>
 - Usage: `,system network`
 - Aliases: `net`
## ,system uptime
Get the system boot time and how long ago it was.<br/>

Platforms: Windows, Linux, Mac OS<br/>
 - Usage: `,system uptime`
 - Aliases: `up`
## ,system mem
Get infomation about memory usage.<br/>

This will show memory available as a percent, memory used and available as well<br/>
as the total amount. Data is provided for both physical and SWAP RAM.<br/>

Platforms: Windows, Linux, Mac OS<br/>
 - Usage: `,system mem`
 - Aliases: `memory and ram`
## ,system users
Get information about logged in users.<br/>

This will show the user name, what terminal they're logged in at,<br/>
and when they logged in.<br/>

Platforms: Windows, Linux, Mac OS<br/>
Note: PID is not available on Windows. Terminal is usually `Unknown`<br/>
 - Usage: `,system users`
## ,system cpu
Get metrics about the CPU.<br/>

This will show the CPU usage as a percent for each core, and frequency depending on<br/>
platform.<br/>
It will also show the time spent idle, user and system as well as uptime.<br/>

Platforms: Windows, Linux, Mac OS<br/>
Note: CPU frequency is nominal and overall on Windows and Mac OS,<br/>
on Linux it's current and per-core.<br/>
 - Usage: `,system cpu`
## ,system disk
Get infomation about disks connected to the system.<br/>

This will show the space used, total space, filesystem and<br/>
mount point (if you're on Linux make sure it's not potentially<br/>
sensitive if running the command a public space).<br/>

If `ignore_loop` is set to `True`, this will ignore any loop (fake) devices on Linux.<br/>

Platforms: Windows, Linux, Mac OS<br/>
Note: Mount point is basically useless on Windows as it's the<br/>
same as the drive name, though it's still shown.<br/>
 - Usage: `,system disk [ignore_loop=True]`
 - Aliases: `df`
Extended Arg Info
> ### ignore_loop: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```
