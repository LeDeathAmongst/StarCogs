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
            allowed_cogs=[],  # Changed from locked_cogs to allowed_cogs
            allowed_commands=[],  # Changed from locked_commands to allowed_commands
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
        )

    @commands.is_owner()
    @commands.group()
    async def setrolelocker(self, ctx: commands.Context) -> None:
        """Configure RoleLocker settings globally."""
        pass

    @setrolelocker.command()
    async def addcog(self, ctx: commands.Context, *, cog: commands.converter.CogConverter) -> None:
        """Add a cog to the allowed cogs list globally."""
        async with self.config.allowed_cogs() as allowed_cogs:
            if cog.qualified_name in allowed_cogs:
                raise commands.BadArgument("This cog is already in the allowed cogs list.")
            allowed_cogs.append(cog.qualified_name)
        self.cache["allowed_cogs"] = allowed_cogs

    @setrolelocker.command()
    async def addcommand(self, ctx: commands.Context, *, command: commands.converter.CommandConverter) -> None:
        """Add a command to the allowed commands list globally."""
        async with self.config.allowed_commands() as allowed_commands:
            if command.qualified_name in allowed_commands:
                raise commands.BadArgument("This command is already in the allowed commands list.")
            allowed_commands.append(command.qualified_name)
        self.cache["allowed_commands"] = allowed_commands

    @setrolelocker.command()
    async def removecog(self, ctx: commands.Context, *, cog: commands.converter.CogConverter) -> None:
        """Remove a cog from the allowed cogs list globally."""
        async with self.config.allowed_cogs() as allowed_cogs:
            if cog.qualified_name not in allowed_cogs:
                raise commands.BadArgument("This cog isn't in the allowed cogs list.")
            allowed_cogs.remove(cog.qualified_name)
        self.cache["allowed_cogs"] = allowed_cogs

    @setrolelocker.command()
    async def removecommand(self, ctx: commands.Context, *, command: commands.converter.CommandConverter) -> None:
        """Remove a command from the allowed commands list globally."""
        async with self.config.allowed_commands() as allowed_commands:
            if command.qualified_name not in allowed_commands:
                raise commands.BadArgument("This command isn't in the allowed commands list.")
            allowed_commands.remove(command.qualified_name)
        self.cache["allowed_commands"] = allowed_commands

    @setrolelocker.command()
    async def clear(self, ctx: commands.Context) -> None:
        """Clear the allowed cogs and commands list globally."""
        await self.config.clear()
        self.cache = {"allowed_cogs": [], "allowed_commands": []}

    async def red_get_help_for(self, ctx: commands.Context, command_or_cog):
        """Override help menu to hide locked commands and cogs."""
        if isinstance(command_or_cog, commands.Cog):
            if command_or_cog.qualified_name not in self.cache["allowed_cogs"]:
                return None
        elif isinstance(command_or_cog, commands.Command):
            if command_or_cog.qualified_name not in self.cache["allowed_commands"]:
                return None
        return await super().red_get_help_for(ctx, command_or_cog)
