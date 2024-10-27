import asyncio
import threading
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import box
from redbot.core.bot import Red
import discord
import aiohttp
import logging
from typing import Optional

# Assuming webserver.py is in the same directory as this cog
from .webserversite import start_webserver, app

log = logging.getLogger("red.webserver")

class WebServerCog(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_global = {
            "webserver_port": 8000,
            "log_channel": None,
            "max_log_entries": 100,
            "public_key": None,
            "application_id": None,
        }
        self.config.register_global(**default_global)
        self.webserver_thread: Optional[threading.Thread] = None
        self.log_entries = []
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        asyncio.create_task(self.session.close())
        if self.webserver_thread:
            # Implement a way to stop the webserver gracefully
            app.shutdown()
            self.webserver_thread.join()

    @commands.group()
    @commands.is_owner()
    async def webserver(self, ctx: commands.Context):
        """Manage the webserver settings."""
        pass

    @webserver.command(name="start")
    async def webserver_start(self, ctx: commands.Context):
        """Start the webserver."""
        if self.webserver_thread:
            await ctx.send("Webserver is already running.")
            return

        port = await self.config.webserver_port()
        public_key = await self.config.public_key()
        application_id = await self.config.application_id()

        if not public_key or not application_id:
            await ctx.send("Please set the public key and application ID before starting the webserver.")
            return

        def run_webserver():
            asyncio.set_event_loop(asyncio.new_event_loop())
            start_webserver(self.bot, port, public_key, application_id)

        self.webserver_thread = threading.Thread(target=run_webserver)
        self.webserver_thread.start()
        await ctx.send(f"Webserver started on port {port}.")

    @webserver.command(name="stop")
    async def webserver_stop(self, ctx: commands.Context):
        """Stop the webserver."""
        if not self.webserver_thread:
            await ctx.send("Webserver is not running.")
            return

        app.shutdown()
        self.webserver_thread.join()
        self.webserver_thread = None
        await ctx.send("Webserver stopped.")

    @webserver.command(name="setport")
    async def set_port(self, ctx: commands.Context, port: int):
        """Set the port for the webserver."""
        await self.config.webserver_port.set(port)
        await ctx.send(f"Webserver port set to {port}. Restart the webserver for changes to take effect.")

    @webserver.command(name="setlogchannel")
    async def set_log_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for webserver logs."""
        await self.config.log_channel.set(channel.id)
        await ctx.send(f"Log channel set to {channel.mention}")

    @webserver.command(name="setmaxlogs")
    async def set_max_logs(self, ctx: commands.Context, max_logs: int):
        """Set the maximum number of log entries to keep."""
        await self.config.max_log_entries.set(max_logs)
        await ctx.send(f"Maximum log entries set to {max_logs}")

    @webserver.command(name="setpublickey")
    async def set_public_key(self, ctx: commands.Context, public_key: str):
        """Set the public key for Discord interaction verification."""
        await self.config.public_key.set(public_key)
        await ctx.send("Public key set. Restart the webserver for changes to take effect.")

    @webserver.command(name="setappid")
    async def set_application_id(self, ctx: commands.Context, app_id: str):
        """Set the application ID for invite links."""
        await self.config.application_id.set(app_id)
        await ctx.send("Application ID set. Restart the webserver for changes to take effect.")

    @webserver.command(name="status")
    async def webserver_status(self, ctx: commands.Context):
        """Show the current status and settings of the webserver."""
        config = await self.config.all()
        status = "Running" if self.webserver_thread else "Stopped"
        log_channel = self.bot.get_channel(config['log_channel'])
        log_channel_mention = log_channel.mention if log_channel else "Not set"

        status_msg = (
            f"Webserver Status: {status}\n"
            f"Port: {config['webserver_port']}\n"
            f"Log Channel: {log_channel_mention}\n"
            f"Max Log Entries: {config['max_log_entries']}\n"
            f"Public Key: {config['public_key'][:10]}... (truncated)\n"
            f"Application ID: {config['application_id']}"
        )
        await ctx.send(box(status_msg))

    async def log_to_website(self, data: dict):
        """Log data to the website and Discord channel if set."""
        max_logs = await self.config.max_log_entries()
        self.log_entries.append(data)
        if len(self.log_entries) > max_logs:
            self.log_entries = self.log_entries[-max_logs:]

        log_channel_id = await self.config.log_channel()
        if log_channel_id:
            channel = self.bot.get_channel(log_channel_id)
            if channel:
                embed = discord.Embed(title="Webserver Log", color=discord.Color.blue())
                for key, value in data.items():
                    embed.add_field(name=key, value=str(value), inline=False)
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """Log when the bot joins a new guild."""
        await self.log_to_website({
            "event": "Guild Join",
            "guild_name": guild.name,
            "guild_id": guild.id,
            "member_count": guild.member_count
        })

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """Log when the bot leaves a guild."""
        await self.log_to_website({
            "event": "Guild Leave",
            "guild_name": guild.name,
            "guild_id": guild.id
        })

async def setup(bot: Red):
    await bot.add_cog(WebServerCog(bot))
