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

        # Define global settings schema
        self.config.register_global(
            allowed_cogs=[],
            allowed_commands=[],
            role_tiers={},
            role_limits={}
        )

        self.cache: typing.Dict[str, typing.List[str]] = {"allowed_cogs": [], "allowed_commands": []}

        # Use Star_Utils.settings
        _settings: typing.Dict[str, typing.Dict[str, typing.Any]] = {
            "allowed_cogs": {
                "converter": list,
                "description": "List of globally allowed cogs.",
                "hidden": True,
                "no_slash": True,
            },
            "allowed_commands": {
                "converter": list,
                "description": "List of globally allowed commands.",
                "hidden": True,
                "no_slash": True,
            },
            "role_tiers": {
                "converter": dict,
                "description": "Dictionary of role tiers.",
                "hidden": True,
                "no_slash": True,
            },
            "role_limits": {
                "converter": dict,
                "description": "Dictionary of role limits with required member count.",
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

    async def cog_load(self) -> None:
        await super().cog_load()
        data = await self.config.all()
        if data["allowed_cogs"] or data["allowed_commands"]:
            self.cache = data
        self.bot.add_check(self.bot_check)

    async def cog_unload(self) -> None:
        self.bot.remove_check(self.bot_check)
        await super().cog_unload()

    async def bot_check(self, ctx: commands.Context) -> bool:
        # Allow rolelock commands for admins or users with manage_guild permission
        if ctx.command.root_parent and ctx.command.root_parent.name == "rolelock":
            return True
        if not await self.check_command(ctx):
            raise commands.CheckFailure(
                "Only specific cogs and commands are allowed globally. Ask a bot owner in the support server for access, or buy premium if applicable."
            )
        return True

    async def check_command(self, ctx: commands.Context, command: typing.Optional[commands.Command] = None) -> bool:
        if command is None:
            command = ctx.command
            if isinstance(command, commands.Group):
                view = ctx.view
                previous = view.index
                view.skip_ws()
                trigger = view.get_word()
                invoked_subcommand = command.all_commands.get(trigger, None)
                view.index = previous
                if invoked_subcommand is not None or not command.invoke_without_command:
                    return True

        # Check if the user has the required roles
        user_roles = {role.id for role in ctx.author.roles}
        role_tiers = await self.config.role_tiers()
        user_tiers = self.get_user_tiers(user_roles, role_tiers)

        # Check role limits
        role_limits = await self.config.role_limits()
        for role in ctx.author.roles:
            if role.id in role_limits and len(role.members) < role_limits[role.id]:
                await ctx.send(f"Role `{role.name}` requires at least `{role_limits[role.id]}` members to access this command.")
                ctx.command.reset_cooldown(ctx)
                raise commands.CheckFailure()

        # Global access control
        return (
            ctx.author.id in ctx.bot.owner_ids
            or ctx.guild is None
            or (
                command is None
                or command.cog is None
                or isinstance(command, commands.commands._AlwaysAvailableCommand)
                or command.qualified_name == "help"
                or (command.cog is not None and command.cog.qualified_name in ("Core", self.qualified_name))
            )
            or (
                (
                    command.cog is not None
                    and command.cog.qualified_name in self.cache["allowed_cogs"]
                ) or any(
                    command.qualified_name.split(" ")[:len(allowed_command.split(" "))] == allowed_command.split(" ")
                    for allowed_command in self.cache["allowed_commands"]
                )
            )
            or any(tier in user_tiers for tier in self.cache["allowed_cogs"] + self.cache["allowed_commands"])
        )

    def get_user_tiers(self, user_roles: typing.Set[int], role_tiers: typing.Dict[str, typing.List[int]]) -> typing.Set[str]:
        """Get the tiers a user belongs to based on their roles."""
        user_tiers = set()
        for tier, role_ids in role_tiers.items():
            if any(role_id in user_roles for role_id in role_ids):
                user_tiers.add(tier)
        return user_tiers

    @commands.group()
    @commands.admin_or_permissions(manage_guild=True)
    async def rolelock(self, ctx: commands.Context):
        """Base command for locking commands or cogs."""
        pass

    @rolelock.command()
    async def command(self, ctx: commands.Context, command_name: str, *tiers: str):
        """Lock a specific command behind tiers."""
        async with self.config.locked_commands() as locked_commands:
            locked_commands[command_name] = tiers
        await ctx.send(f"Command `{command_name}` is now locked for tiers: {', '.join(tiers)}")

    @rolelock.command()
    async def removecommand(self, ctx: commands.Context, command_name: str):
        """Remove a command from being locked."""
        async with self.config.locked_commands() as locked_commands:
            if command_name in locked_commands:
                del locked_commands[command_name]
                await ctx.send(f"Command `{command_name}` is no longer locked.")
            else:
                await ctx.send(f"Command `{command_name}` was not locked.")

    @rolelock.command()
    async def cog(self, ctx: commands.Context, cog_name: str, *tiers: str):
        """Lock an entire cog behind tiers."""
        qualified_name = self.get_cog_qualified_name(cog_name)
        if not qualified_name:
            await ctx.send(f"Cog `{cog_name}` not found.")
            return

        async with self.config.locked_cogs() as locked_cogs:
            locked_cogs[qualified_name] = tiers
        await ctx.send(f"Cog `{qualified_name}` is now locked for tiers: {', '.join(tiers)}")

    @rolelock.command()
    async def removecog(self, ctx: commands.Context, cog_name: str):
        """Remove a cog from being locked."""
        qualified_name = self.get_cog_qualified_name(cog_name)
        if not qualified_name:
            await ctx.send(f"Cog `{cog_name}` not found.")
            return

        async with self.config.locked_cogs() as locked_cogs:
            if qualified_name in locked_cogs:
                del locked_cogs[qualified_name]
                await ctx.send(f"Cog `{qualified_name}` is no longer locked.")
            else:
                await ctx.send(f"Cog `{qualified_name}` was not locked.")

    @rolelock.command()
    async def setrolelimit(self, ctx: commands.Context, role: Role, member_count: int):
        """Set a member count limit for a role to access commands or cogs."""
        async with self.config.role_limits() as role_limits:
            role_limits[role.id] = member_count
        await ctx.send(f"Role `{role.name}` now requires at least `{member_count}` members to access locked commands or cogs.")

    def get_cog_qualified_name(self, cog_name: str) -> typing.Optional[str]:
        """Get the qualified name of a cog."""
        cog = self.bot.get_cog(cog_name)
        if cog:
            print(f"Found cog: {cog.qualified_name}")  # Debugging line
            return cog.qualified_name
        print(f"Cog not found: {cog_name}")  # Debugging line
        return None

    async def red_get_help_for(self, ctx: commands.Context, command_or_cog):
        """Override help menu to hide locked commands and cogs."""
        if isinstance(command_or_cog, commands.Cog):
            if command_or_cog.qualified_name not in self.cache["allowed_cogs"]:
                return None
        elif isinstance(command_or_cog, commands.Command):
            if command_or_cog.qualified_name not in self.cache["allowed_commands"]:
                return None
        return await super().red_get_help_for(ctx, command_or_cog)
