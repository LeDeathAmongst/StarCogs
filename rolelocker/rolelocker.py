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
        self.config.register_global(role_tiers={})

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
            "role_tiers": {
                "converter": dict,
                "description": "Dictionary of role tiers.",
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
        cog_name = self.get_cog_qualified_name(cog_name)
        if not cog_name:
            await ctx.send(f"Cog `{cog_name}` not found.")
            return

        async with self.config.locked_cogs() as locked_cogs:
            locked_cogs[cog_name] = tiers
        await ctx.send(f"Cog `{cog_name}` is now locked for tiers: {', '.join(tiers)}")

    @rolelock.command()
    async def removecog(self, ctx: commands.Context, cog_name: str):
        """Remove a cog from being locked."""
        cog_name = self.get_cog_qualified_name(cog_name)
        if not cog_name:
            await ctx.send(f"Cog `{cog_name}` not found.")
            return

        async with self.config.locked_cogs() as locked_cogs:
            if cog_name in locked_cogs:
                del locked_cogs[cog_name]
                await ctx.send(f"Cog `{cog_name}` is no longer locked.")
            else:
                await ctx.send(f"Cog `{cog_name}` was not locked.")

    def get_cog_qualified_name(self, cog_name: str) -> typing.Optional[str]:
        """Get the qualified name of a cog."""
        cog = self.bot.get_cog(cog_name)
        if cog:
            return cog.qualified_name
        return None

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        """Listener to check for locked commands."""
        locked_commands = await self.config.locked_commands()
        locked_cogs = await self.config.locked_cogs()
        role_tiers = await self.config.role_tiers()

        user_tiers = self.get_user_tiers(ctx.author.roles, role_tiers)

        # Check if the entire cog is locked
        if ctx.cog.qualified_name in locked_cogs:
            required_tiers = locked_cogs[ctx.cog.qualified_name]
            if not any(tier in user_tiers for tier in required_tiers):
                await ctx.send("You do not have permission to use commands from this cog.")
                ctx.command.reset_cooldown(ctx)
                raise commands.CheckFailure()

        # Check if the specific command is locked
        if ctx.command.name in locked_commands:
            required_tiers = locked_commands[ctx.command.name]
            if not any(tier in user_tiers for tier in required_tiers):
                await ctx.send("You do not have permission to use this command.")
                ctx.command.reset_cooldown(ctx)
                raise commands.CheckFailure()

    def get_user_tiers(self, roles: typing.List[Role], role_tiers: typing.Dict[str, typing.List[int]]) -> typing.Set[str]:
        """Get the tiers a user belongs to based on their roles."""
        user_tiers = set()
        for tier, role_ids in role_tiers.items():
            if any(role.id in role_ids for role in roles):
                user_tiers.add(tier)
        return user_tiers

    @commands.is_owner()
    @commands.group()
    async def setrolelocker(self, ctx: commands.Context):
        """Configure RoleLocker settings."""
        pass

    @setrolelocker.command()
    async def addtier(self, ctx: commands.Context, tier_name: str, *roles: Role):
        """Add roles to a specific tier."""
        async with self.config.role_tiers() as role_tiers:
            role_tiers[tier_name] = [role.id for role in roles]
        await ctx.send(f"Tier `{tier_name}` now includes roles: {', '.join(role.name for role in roles)}")

    @setrolelocker.command()
    async def removetier(self, ctx: commands.Context, tier_name: str, *roles: Role):
        """Remove roles from a specific tier."""
        async with self.config.role_tiers() as role_tiers:
            if tier_name in role_tiers:
                role_tiers[tier_name] = [role_id for role_id in role_tiers[tier_name] if role_id not in [role.id for role in roles]]
                await ctx.send(f"Roles removed from tier `{tier_name}`: {', '.join(role.name for role in roles)}")
            else:
                await ctx.send(f"Tier `{tier_name}` does not exist.")

    async def red_get_help_for(self, ctx: commands.Context, command_or_cog):
        """Override help menu to hide locked commands and cogs."""
        if isinstance(command_or_cog, commands.Cog):
            locked_cogs = await self.config.locked_cogs()
            if command_or_cog.qualified_name in locked_cogs:
                required_tiers = locked_cogs[command_or_cog.qualified_name]
                user_tiers = self.get_user_tiers(ctx.author.roles, await self.config.role_tiers())
                if not any(tier in user_tiers for tier in required_tiers):
                    return None

        elif isinstance(command_or_cog, commands.Command):
            locked_commands = await self.config.locked_commands()
            if command_or_cog.name in locked_commands:
                required_tiers = locked_commands[command_or_cog.name]
                user_tiers = self.get_user_tiers(ctx.author.roles, await self.config.role_tiers())
                if not any(tier in user_tiers for tier in required_tiers):
                    return None

        return await super().red_get_help_for(ctx, command_or_cog)
