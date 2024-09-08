from StarUtils import Cog, settings
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

        # Use Star_Utils.settings
        _settings: typing.Dict[str, typing.Dict[str, typing.Any]] = {
            "locked_commands": {
                "converter": dict,
                "description": "Dictionary of locked commands with their required roles.",
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
    async def lock(self, ctx: commands.Context):
        """Base command for locking commands or cogs."""
        pass

    @lock.command()
    async def command(self, ctx: commands.Context, command_name: str, *roles: Role):
        """Lock a specific command behind roles."""
        async with self.config.locked_commands() as locked_commands:
            locked_commands[command_name] = [role.id for role in roles]
        await ctx.send(f"Command `{command_name}` is now locked for roles: {', '.join(role.name for role in roles)}")

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        """Listener to check for locked commands."""
        locked_commands = await self.config.locked_commands()
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

def setup(bot: Red):
    bot.add_cog(RoleLocker(bot))
