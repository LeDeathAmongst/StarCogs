from Star_Utils import Cog, Settings, Menu
from redbot.core import commands, Config
from redbot.core.bot import Red
from discord import Role, Embed
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
            role_limits={},
            role_tiers={}
        )

        # Use Star_Utils.settings
        _settings: typing.Dict[str, typing.Dict[str, typing.Any]] = {
            "locked_cogs": {
                "converter": dict,
                "description": "Dictionary of locked cogs with required roles.",
                "hidden": True,
                "no_slash": True,
            },
            "locked_commands": {
                "converter": dict,
                "description": "Dictionary of locked commands with required roles.",
                "hidden": True,
                "no_slash": True,
            },
            "role_limits": {
                "converter": dict,
                "description": "Dictionary of role limits with maximum member count.",
                "hidden": True,
                "no_slash": True,
            },
            "role_tiers": {
                "converter": dict,
                "description": "Dictionary of roles organized into tiers.",
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
        if ctx.command.root_parent and ctx.command.root_parent.name == "rolelock":
            return True
        if not await self.check_command(ctx):
            raise commands.CheckFailure(
                "You do not have permission to use this command."
            )
        return True

    async def check_command(self, ctx: commands.Context, command: typing.Optional[commands.Command] = None) -> bool:
        if ctx.author.id in ctx.bot.owner_ids:
            return True

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

        user_roles = {role.id for role in ctx.author.roles}
        role_limits = await self.config.role_limits()

        for role in ctx.author.roles:
            if role.id in role_limits and len(role.members) > role_limits[role.id]:
                await ctx.send(f"Role `{role.name}` cannot have more than `{role_limits[role.id]}` members.")
                ctx.command.reset_cooldown(ctx)
                raise commands.CheckFailure()

        locked_cogs = await self.config.locked_cogs()
        locked_commands = await self.config.locked_commands()

        if command.cog and command.cog.qualified_name in locked_cogs:
            required_roles = locked_cogs[command.cog.qualified_name]
            if not any(role in user_roles for role in required_roles):
                return False

        if command.qualified_name in locked_commands:
            required_roles = locked_commands[command.qualified_name]
            if not any(role in user_roles for role in required_roles):
                return False

        return True

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
    async def removecommand(self, ctx: commands.Context, command_name: str):
        """Remove a command from being locked."""
        async with self.config.locked_commands() as locked_commands:
            if command_name in locked_commands:
                del locked_commands[command_name]
                await ctx.send(f"Command `{command_name}` is no longer locked.")
            else:
                await ctx.send(f"Command `{command_name}` was not locked.")

    @rolelock.command()
    async def cog(self, ctx: commands.Context, cog_name: str, *roles: Role):
        """Lock an entire cog behind roles."""
        qualified_name = self.get_cog_qualified_name(cog_name)
        if not qualified_name:
            await ctx.send(f"Cog `{cog_name}` not found.")
            return

        async with self.config.locked_cogs() as locked_cogs:
            locked_cogs[qualified_name] = [role.id for role in roles]
        await ctx.send(f"Cog `{qualified_name}` is now locked for roles: {', '.join(role.name for role in roles)}")

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
    async def rolelist(self, ctx: commands.Context):
        """List all roles and the commands/cogs they unlock."""
        locked_cogs = await self.config.locked_cogs()
        locked_commands = await self.config.locked_commands()

        description = []
        for cog, roles in locked_cogs.items():
            role_names = [ctx.guild.get_role(role_id).name for role_id in roles if ctx.guild.get_role(role_id)]
            description.append(f"**{cog}**: {', '.join(role_names)}")

        for command, roles in locked_commands.items():
            role_names = [ctx.guild.get_role(role_id).name for role_id in roles if ctx.guild.get_role(role_id)]
            description.append(f"**{command}**: {', '.join(role_names)}")

        embed = discord.Embed(
            title="Locked Roles",
            description="\n".join(description) if description else "No roles are currently locked.",
            color=await ctx.embed_color()
        )
        await ctx.send(embed=embed)

    @rolelock.command()
    async def tierinfo(self, ctx: commands.Context, tier_name: str):
        """Display the roles in a specific tier."""
        role_tiers = await self.config.role_tiers()
        if tier_name not in role_tiers:
            await ctx.send(f"Tier `{tier_name}` does not exist.")
            return

        roles = [ctx.guild.get_role(role_id) for role_id in role_tiers[tier_name]]
        role_names = [f"<:dot:1279793197165314059> {role.name}" for role in roles if role is not None]

        members = set()
        for role in roles:
            if role is not None:
                members.update(role.members)

        member_names = [member.display_name for member in members]

        embed = discord.Embed(
            title=f"Tier `{tier_name}` Information",
            color=await ctx.embed_color()
        )
        embed.add_field(name="Roles", value=", ".join(role_names) if role_names else "None", inline=False)
        embed.add_field(name="Members", value=", ".join(member_names) if member_names else "None", inline=False)

        await ctx.send(embed=embed)

    @rolelock.command()
    async def tierlist(self, ctx: commands.Context):
        """List all tiers and the roles in them."""
        role_tiers = await self.config.role_tiers()
        if not role_tiers:
            await ctx.send("There are no tiers set up.")
            return

        pages = []
        for tier_name, role_ids in role_tiers.items():
            roles = [ctx.guild.get_role(role_id) for role_id in role_ids]
            role_names = [f"<:dot:1279793197165314059> {role.name}" for role in roles if role is not None]
            embed = discord.Embed(
                title=f"Tier `{tier_name}`",
                description="\n".join(role_names) if role_names else "None",
                color=await ctx.embed_color()
            )
            pages.append({"embed": embed})

        await Menu(pages=pages).start(ctx)

    def get_cog_qualified_name(self, cog_name: str) -> typing.Optional[str]:
        """Get the qualified name of a cog."""
        cog = self.bot.get_cog(cog_name)
        if cog:
            return cog.qualified_name
        return None

    async def red_get_help_for(self, ctx: commands.Context, command_or_cog):
        """Override help menu to hide locked commands and cogs."""
        if ctx.author.id in ctx.bot.owner_ids:
            return await super().red_get_help_for(ctx, command_or_cog)

        locked_cogs = await self.config.locked_cogs()
        locked_commands = await self.config.locked_commands()
        user_roles = {role.id for role in ctx.author.roles}

        if isinstance(command_or_cog, commands.Cog):
            if command_or_cog.qualified_name in locked_cogs:
                required_roles = locked_cogs[command_or_cog.qualified_name]
                if not any(role in user_roles for role in required_roles):
                    return None
                # Hide commands within locked cogs
                for command in command_or_cog.get_commands():
                    if command.qualified_name in locked_commands:
                        required_roles = locked_commands[command.qualified_name]
                        if not any(role in user_roles for role in required_roles):
                            command.hidden = True
        elif isinstance(command_or_cog, commands.Command):
            if command_or_cog.qualified_name in locked_commands:
                required_roles = locked_commands[command_or_cog.qualified_name]
                if not any(role in user_roles for role in required_roles):
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
