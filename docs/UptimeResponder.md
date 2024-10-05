A cog for responding to pings form various uptime monitoring services,<br/>such as UptimeRobot, Pingdom, Uptime.com, or self-hosted ones like UptimeKuma or Upptime.<br/><br/>The web server will run in the background whenever the cog is loaded on the specified port.<br/><br/>It will respond with status code 200 when a request is made to the root URL.<br/><br/>If you want to use this with an external service, you will need to set up port forwarding.<br/>Make sure you are aware of the security risk of exposing your machine to the internet.

# <@1275521742961508432>uptimeresponderinfo

 - Usage: `<@1275521742961508432>uptimeresponderinfo`
# <@1275521742961508432>uptimeresponderport
Get or set the port to run the simple web server on.<br/>

Run the command on it's own (`<@1275521742961508432>uptimeresponderport`) to see what it's<br/>
set to at the moment, and to set it run `<@1275521742961508432>uptimeresponderport 8080`, for example.<br/>
 - Usage: `<@1275521742961508432>uptimeresponderport [port=None]`
 - Restricted to: `BOT_OWNER`
Extended Arg Info
> ### port: Optional[int] = None
> ```
> A number without decimal places.
> ```
