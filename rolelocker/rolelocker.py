from Star_Utils import Cog, Settings
from redbot.core import commands, Config
from redbot.core.bot import Red
from discord import Role
import discord
import typing

class RoleLocker(Cog):
    def __init__(self, bot: Red) -> None:
        super().__init__(bot=bot)

        # Initialize settings
        self.config: Config = Config.get_conf(
            self,
            identifier=159096775493115543881107426517572342387,
            force_registration=True,
        )

        # Define global settings schema
        self.config.register_global(
            locked_cogs={},
            locked_commands={},
            role_tiers={},
            role_limits={}
        )

        # Use Star_Utils.settings
        _settings: typing.Dict[str, typing.Dict[str, typing.Any]] = {
            "locked_cogs": {
                "converter": dict,
                "description": "Dictionary of locked cogs with tiers.",
                "hidden": True,
                "no_slash": True,
            },
            "locked_commands": {
                "converter": dict,
                "description": "Dictionary of locked commands with tiers.",
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
                "description": "Dictionary of role limits with maximum member count.",
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
                "You do not have permission to use this command."
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
            if role.id in role_limits and len(role.members) > role_limits[role.id]:
                await ctx.send(f"Role `{role.name}` cannot have more than `{role_limits[role.id]}` members.")
                ctx.command.reset_cooldown(ctx)
                raise commands.CheckFailure()

        # Access control based on locked cogs and commands
        locked_cogs = await self.config.locked_cogs()
        locked_commands = await self.config.locked_commands()

        # Check if the entire cog is locked
        if command.cog and command.cog.qualified_name in locked_cogs:
            required_tiers = locked_cogs[command.cog.qualified_name]
            if not any(tier in user_tiers for tier in required_tiers):
                return False

        # Check if the specific command is locked
        if command.qualified_name in locked_commands:
            required_tiers = locked_commands[command.qualified_name]
            if not any(tier in user_tiers for tier in required_tiers):
                return False

        return True

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
    async def tierlist(self, ctx: commands.Context):
        """List all tiers and the roles in them."""
        role_tiers = await self.config.role_tiers()
        if not role_tiers:
            await ctx.send("There are no tiers set up.")
            return

        description = []
        for tier_name, role_ids in role_tiers.items():
            roles = [ctx.guild.get_role(role_id) for role_id in role_ids]
            role_names = [f"<:dot:1279793197165314059> {role.name}" for role in roles if role is not None]
            description.append(f"**{tier_name}**: {', '.join(role_names)}")

        embed = discord.Embed(
            title="Role Tiers",
            description="\n".join(description),
            color=await ctx.embed_color()
        )
        await ctx.send(embed=embed)

    @rolelock.command()
    async def usertiers(self, ctx: commands.Context):
        """Display the user's tiers and locked cogs/commands."""
        user_roles = {role.id for role in ctx.author.roles}
        role_tiers = await self.config.role_tiers()
        user_tiers = self.get_user_tiers(user_roles, role_tiers)

        locked_cogs = await self.config.locked_cogs()
        locked_commands = await self.config.locked_commands()

        user_locked_cogs = [cog for cog, tiers in locked_cogs.items() if not any(tier in user_tiers for tier in tiers)]
        user_locked_commands = [command for command, tiers in locked_commands.items() if not any(tier in user_tiers for tier in tiers)]

        embed = discord.Embed(
            title=f"{ctx.author.display_name}'s Tiers and Locked Access",
            color=await ctx.embed_color()
        )
        embed.add_field(name="Tiers", value=", ".join(user_tiers) if user_tiers else "None", inline=False)
        embed.add_field(name="Locked Cogs", value=", ".join(user_locked_cogs) if user_locked_cogs else "None", inline=False)
        embed.add_field(name="Locked Commands", value=", ".join(user_locked_commands) if user_locked_commands else "None", inline=False)

        await ctx.send(embed=embed)

    @rolelock.command()
    async def tierinfo(self, ctx: commands.Context, tier_name: str):
        """Display the commands, roles, and cogs locked in a specific tier."""
        role_tiers = await self.config.role_tiers()
        if tier_name not in role_tiers:
            await ctx.send(f"Tier `{tier_name}` does not exist.")
            return

        roles = [ctx.guild.get_role(role_id) for role_id in role_tiers[tier_name]]
        role_names = [f"<:dot:1279793197165314059> {role.name}" for role in roles if role is not None]

        locked_cogs = await self.config.locked_cogs()
        locked_commands = await self.config.locked_commands()
        tier_locked_cogs = [cog for cog, tiers in locked_cogs.items() if tier_name in tiers]
        tier_locked_commands = [command for command, tiers in locked_commands.items() if tier_name in tiers]

        embed = discord.Embed(
            title=f"Tier `{tier_name}` Information",
            color=await ctx.embed_color()
        )
        embed.add_field(name="Roles", value=", ".join(role_names) if role_names else "None", inline=False)
        embed.add_field(name="Locked Cogs", value=", ".join(tier_locked_cogs) if tier_locked_cogs else "None", inline=False)
        embed.add_field(name="Locked Commands", value=", ".join(tier_locked_commands) if tier_locked_commands else "None", inline=False)

        await ctx.send(embed=embed)

    def get_cog_qualified_name(self, cog_name: str) -> typing.Optional[str]:
        """Get the qualified name of a cog."""
        cog = self.bot.get_cog(cog_name)
        if cog:
            return cog.qualified_name
        return None

    async def red_get_help_for(self, ctx: commands.Context, command_or_cog):
        """Override help menu to hide locked commands and cogs."""
        locked_cogs = await self.config.locked_cogs()
        locked_commands = await self.config.locked_commands()
        user_roles = {role.id for role in ctx.author.roles}
        role_tiers = await self.config.role_tiers()
        user_tiers = self.get_user_tiers(user_roles, role_tiers)

        if isinstance(command_or_cog, commands.Cog):
            if command_or_cog.qualified_name in locked_cogs:
                required_tiers = locked_cogs[command_or_cog.qualified_name]
                if not any(tier in user_tiers for tier in required_tiers):
                    return None
                # Hide commands within locked cogs
                for command in command_or_cog.get_commands():
                    if command.qualified_name in locked_commands:
                        required_tiers = locked_commands[command.qualified_name]
                        if not any(tier in user_tiers for tier in required_tiers):
                            command.hidden = True
        elif isinstance(command_or_cog, commands.Command):
            if command_or_cog.qualified_name in locked_commands:
                required_tiers = locked_commands[command_or_cog.qualified_name]
                if not any(tier in user_tiers for tier in required_tiers):
                    return None

        return await super().red_get_help_for(ctx, command_or_cog)

    @commands.is_owner()
    @commands.group()
    async def setrolelocker(self, ctx: commands.Context) -> None:
        """Configure RoleLocker settings globally."""
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

    @setrolelocker.command()
    async def setrolelimit(self, ctx: commands.Context, role: Role, max_members: int):
        """Set a maximum member count limit for a role."""
        async with self.config.role_limits() as role_limits:
            role_limits[role.id] = max_members
        await ctx.send(f"Role `{role.name}` cannot have more than `{max_members}` members.")
