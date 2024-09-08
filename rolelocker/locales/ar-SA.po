from Star_Utils import Cog, Settings
from redbot.core import commands, Config
from redbot.core.bot import Red
from discord import Role
import typing

class RoleLocker(Cog):
    def __init__(self, bot: Red) -> None:
        super().__init__(bot=bot)

        # Initialize settings
        self.config: Config = Config.get_conf(
            self,
            identifier=159096775493115543881107426517572342387,  # Unique identifier for your cog
            force_registration=True,
        )

        # Define settings schema
        self.config.register_global(locked_commands={})
        self.config.register_global(locked_cogs={})

        # Use Star_Utils.settings
        _settings: typing.Dict[str, typing.Dict[str, typing.Any]] = {
            "locked_commands": {
                "converter": dict,
                "description": "Dictionary of locked commands with their required roles.",
                "hidden": True,
                "no_slash": True,
            },
            "locked_cogs": {
                "converter": dict,
                "description": "Dictionary of locked cogs with their required roles.",
                "hidden": True,
                "no_slash": True,
            },
        }

        self.settings: Settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GLOBAL,
            settings=_settings,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.setrolelocker,
        )

    @commands.group()
    @commands.admin_or_permissions(manage_guild=True)
    async def rolelock(self, ctx: commands.Context):
        """Base command for locking commands or cogs."""
        pass

    @rolelock.command()
    async def command(self, ctx: commands.Context, command_name: str, *roles: Role):
        """Lock a specific command behind roles."""
        async with self.config.locked_commands() as locked_commands:
            locked_commands[command_name] = [role.id for role in roles]
        await ctx.send(f"Command `{command_name}` is now locked for roles: {', '.join(role.name for role in roles)}")

    @rolelock.command()
    async def cog(self, ctx: commands.Context, cog_name: str, *roles: Role):
        """Lock an entire cog behind roles."""
        async with self.config.locked_cogs() as locked_cogs:
            locked_cogs[cog_name] = [role.id for role in roles]
        await ctx.send(f"Cog `{cog_name}` is now locked for roles: {', '.join(role.name for role in roles)}")

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        """Listener to check for locked commands."""
        locked_commands = await self.config.locked_commands()
        locked_cogs = await self.config.locked_cogs()

        # Check if the entire cog is locked
        if ctx.cog.qualified_name in locked_cogs:
            required_roles = locked_cogs[ctx.cog.qualified_name]
            if not any(role.id in required_roles for role in ctx.author.roles):
                await ctx.send("You do not have permission to use commands from this cog.")
                ctx.command.reset_cooldown(ctx)
                raise commands.CheckFailure()

        # Check if the specific command is locked
        if ctx.command.name in locked_commands:
            required_roles = locked_commands[ctx.command.name]
            if not any(role.id in required_roles for role in ctx.author.roles):
                await ctx.send("You do not have permission to use this command.")
                ctx.command.reset_cooldown(ctx)
                raise commands.CheckFailure()

    @commands.is_owner()
    @commands.group()
    async def setrolelocker(self, ctx: commands.Context):
        """Configure RoleLocker settings."""
        pass

    async def red_get_help_for(self, ctx: commands.Context, command_or_cog):
        """Override help menu to hide locked commands and cogs."""
        if isinstance(command_or_cog, commands.Cog):
            locked_cogs = await self.config.locked_cogs()
            if command_or_cog.qualified_name in locked_cogs:
                required_roles = locked_cogs[command_or_cog.qualified_name]
                if not any(role.id in required_roles for role in ctx.author.roles):
                    return None

        elif isinstance(command_or_cog, commands.Command):
            locked_commands = await self.config.locked_commands()
            if command_or_cog.name in locked_commands:
                required_roles = locked_commands[command_or_cog.name]
                if not any(role.id in required_roles for role in ctx.author.roles):
                    return None

        return await super().red_get_help_for(ctx, command_or_cog)
