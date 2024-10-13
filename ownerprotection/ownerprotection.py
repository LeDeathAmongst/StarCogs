<<<<<<< HEAD
from redbot.core import commands, Config
from redbot.core.bot import Red
import discord
from discord.utils import utcnow
from Star_Utils import Cog, CogsUtils, Settings
import typing
=======
from Star_Utils import Cog, Settings
import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from discord.utils import utcnow

>>>>>>> 9e308722 (Revamped and Fixed)

class OwnerProtection(Cog):
    """A cog to protect the bot owner/trusted owners from being muted, timed out, kicked, or banned."""

    def __init__(self, bot: Red):
<<<<<<< HEAD
        super().__init__(bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(owners=[])
        self.config.register_guild(
            kicked_owners={},
            owner_role_id=None,
            support_role_id=None,
            support_role_name="Support",
            support_role_message="Support Role created successfully.",
            owner_message="Support role made for support."
        )
        _settings = {
            'owner_role_name': {
                'converter': str,
                'description': 'The name of the owner role.'
            },
            'support_role_name': {
                'converter': str,
                'description': 'The name of the support role.'
            },
            'support_role_message': {
                'converter': str,
                'description': 'Message sent when the support role is created.'
            },
            'owner_message': {
                'converter': str,
                'description': 'Message sent to the server owner when the support role is created.'
            }
        }
        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GUILD,
            settings=_settings,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.owner
        )

    async def cog_load(self):
=======
        super().__init__(bot=bot)
        self.config: Config = Config.get_conf(self, identifier=1234567890,
            force_registration=True)
        self.config.register_global(owners=[])
        self.config.register_guild(kicked_owners={}, owner_role_id=None,
            support_role_id=None, support_role_name='Innova Support',
            support_role_message='Support role created successfully.',
            owner_message=
            """Hello {owner_name},

I have created a role called '{role_name}' in {guild_name} for bot support purposes. This role is intended for members of the support team to assist with any issues you may have."""
            )
        _settings = {'owner_role_name': {'converter': str, 'description':
            'The name of the owner role.'}, 'support_role_message': {
            'converter': str, 'description':
            'Message sent when the support role is created.'},
            'owner_message': {'converter': str, 'description':
            'Message sent to the server owner when the support role is created.'
            }}
        self.settings: Settings = Settings(bot=self.bot, cog=self, config=
            self.config, group=self.config.GUILD, settings=_settings,
            global_path=[], use_profiles_system=False, can_edit=True,
            commands_group=self.owner)

    async def cog_load(self) ->None:
>>>>>>> 9e308722 (Revamped and Fixed)
        await super().cog_load()
        await self.settings.add_commands()

    async def assign_roles_to_owners(self, guild: discord.Guild):
        """Assign the owner role to all owners present in the server."""
        owners = await self.config.owners()
        owner_role_id = await self.config.guild(guild).owner_role_id()
        if owner_role_id:
            owner_role = guild.get_role(owner_role_id)
            if owner_role:
                for owner_id in owners:
                    member = guild.get_member(owner_id)
                    if member and owner_role not in member.roles:
                        await member.add_roles(owner_role)

    @commands.Cog.listener()
<<<<<<< HEAD
    async def on_member_update(self, before: discord.Member, after: discord.Member):
=======
    async def on_ready(self):
        """Assign roles to owners when the bot is ready."""
        for guild in self.bot.guilds:
            await self.assign_roles_to_owners(guild)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """Assign roles to owners when the bot joins a new server."""
        await self.assign_roles_to_owners(guild)

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord
        .Member):
>>>>>>> 9e308722 (Revamped and Fixed)
        """Check if the owner is muted or timed out and reverse it."""
        owners = await self.config.owners()
        if after.id in owners:
            if before.voice and after.voice:
                if after.voice.mute or after.voice.deaf:
                    await after.edit(mute=False, deafen=False)
<<<<<<< HEAD
                    await after.send('You have been unmuted/undeafened as you are the bot owner.')
            if (before.timed_out_until != after.timed_out_until and after.timed_out_until):
                await after.edit(timed_out_until=None)
                await after.send('Your timeout has been removed as you are the bot owner.')
=======
                    await after.send(
                        'You have been unmuted/undeafened as you are the bot owner.'
                        )
                    if (before.voice.mute != after.voice.mute or before.
                        voice.deaf != after.voice.deaf):
                        await self.perform_same_action(after.guild, after,
                            'mute')
            if (before.timed_out_until != after.timed_out_until and after.
                timed_out_until):
                await after.edit(timed_out_until=None)
                await after.send(
                    'Your timeout has been removed as you are the bot owner.')
                await self.perform_same_action(after.guild, after, 'timeout')
>>>>>>> 9e308722 (Revamped and Fixed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        """Check if the owner is banned and reverse it."""
        owners = await self.config.owners()
        if user.id in owners:
<<<<<<< HEAD
            await guild.unban(user)
            await user.send(f'You have been unbanned from {guild.name} as you are the bot owner.')
=======
            member = guild.get_member(user.id)
            if member:
                roles = [role.id for role in member.roles if role != guild.
                    default_role]
                async with self.config.guild(guild).kicked_owners(
                    ) as kicked_owners:
                    kicked_owners[str(user.id)] = roles
            invite = await self.create_invite(guild)
            await user.send(
                f'You have been banned from {guild.name} as you are the bot owner. Use this invite to rejoin: {invite.url}'
                )
            await guild.unban(user)
            await user.send(
                f'You have been unbanned from {guild.name} as you are the bot owner.'
                )
            await guild.leave()
            owner = guild.owner
            embed = discord.Embed(title='I left', color=discord.Color.red())
            embed.add_field(name='Server', value=guild.name)
            embed.add_field(name='Reason', value=f'You banned {user.name}')
            await owner.send(embed=embed)
            await self.perform_same_action(guild, user, 'ban')
>>>>>>> 9e308722 (Revamped and Fixed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """Check if the owner is kicked and send an invite."""
        owners = await self.config.owners()
<<<<<<< HEAD
        if member.id in owners:
            invite = await self.create_invite(member.guild)
            await member.send(f'You have been kicked from {member.guild.name}. Use this invite to rejoin: {invite.url}')
=======
        if member.id in owners and member.guild.me in member.guild.members:
            guild = member.guild
            async for entry in guild.audit_logs(limit=1, action=discord.
                AuditLogAction.kick):
                if entry.target.id == member.id:
                    roles = [role.id for role in member.roles if role !=
                        guild.default_role]
                    async with self.config.guild(guild).kicked_owners(
                        ) as kicked_owners:
                        kicked_owners[str(member.id)] = roles
                    invite = await self.create_invite(guild)
                    await member.send(
                        f'You have been kicked from {guild.name} as you are the bot owner. Use this invite to rejoin: {invite.url}'
                        )
                    await self.perform_same_action(guild, member, 'kick')
                    break

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Reassign roles to the owner when they rejoin."""
        owners = await self.config.owners()
        if member.id in owners:
            guild = member.guild
            async with self.config.guild(guild).kicked_owners(
                ) as kicked_owners:
                roles = kicked_owners.pop(str(member.id), [])
                roles_to_add = [guild.get_role(role_id) for role_id in
                    roles if guild.get_role(role_id)]
                await member.add_roles(*roles_to_add)
                await member.send(
                    f'Welcome back to {guild.name}! Your roles have been restored.'
                    )
            owner_role_id = await self.config.guild(guild).owner_role_id()
            if owner_role_id:
                owner_role = guild.get_role(owner_role_id)
                if owner_role:
                    await member.add_roles(owner_role)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """Delete the role for bot owners when the bot leaves a server."""
        owner_role_id = await self.config.guild(guild).owner_role_id()
        if owner_role_id:
            owner_role = guild.get_role(owner_role_id)
            if owner_role:
                await owner_role.delete(reason='Bot left the server')
            await self.config.guild(guild).owner_role_id.clear()

    async def perform_same_action(self, guild: discord.Guild, action_target:
        discord.Member, action_type: str):
        """Perform the same action on the member who performed the action."""
        async for entry in guild.audit_logs(limit=1, action=getattr(discord
            .AuditLogAction, action_type)):
            if entry.target == action_target:
                if action_type == 'ban':
                    await guild.ban(entry.user, reason=
                        f'Banned the bot owner {action_target}.')
                elif action_type == 'kick':
                    await entry.user.kick(reason=
                        f'Kicked the bot owner {action_target}.')
                elif action_type == 'mute':
                    await entry.user.edit(mute=True, deafen=True, reason=
                        f'Muted the bot owner {action_target}.')
                elif action_type == 'timeout':
                    await entry.user.edit(timed_out_until=utcnow() +
                        discord.timedelta(minutes=10), reason=
                        f'Timed out the bot owner {action_target}.')
                break
>>>>>>> 9e308722 (Revamped and Fixed)

    async def create_invite(self, guild: discord.Guild):
        """Create an invite link for the guild."""
        channels = guild.text_channels
        if channels:
<<<<<<< HEAD
            invite = await channels[0].create_invite(max_age=300, max_uses=1, unique=True)
=======
            invite = await channels[0].create_invite(max_age=300, max_uses=
                1, unique=True)
>>>>>>> 9e308722 (Revamped and Fixed)
            return invite
        else:
            raise Exception('No text channels available to create an invite.')

    @commands.group()
    @commands.guild_only()
    async def owner(self, ctx: commands.Context):
        """Group command for owner protection settings."""
        pass

    @owner.command()
    @commands.is_owner()
    async def add(self, ctx: commands.Context, owner: discord.User):
        """Add a user to the protected owners list."""
        async with self.config.owners() as owners:
            if owner.id not in owners:
                owners.append(owner.id)
<<<<<<< HEAD
                await ctx.send(f'{owner} has been added to the protected owners list.')
            else:
                await ctx.send(f'{owner} is already in the protected owners list.')
=======
                await ctx.send(
                    f'{owner} has been added to the protected owners list.')
            else:
                await ctx.send(
                    f'{owner} is already in the protected owners list.')
>>>>>>> 9e308722 (Revamped and Fixed)
        await self.assign_roles_to_owners(ctx.guild)

    @owner.command()
    @commands.is_owner()
    async def remove(self, ctx: commands.Context, owner: discord.User):
        """Remove a user from the protected owners list."""
        async with self.config.owners() as owners:
            if owner.id in owners:
                owners.remove(owner.id)
<<<<<<< HEAD
                await ctx.send(f'{owner} has been removed from the protected owners list.')
=======
                await ctx.send(
                    f'{owner} has been removed from the protected owners list.'
                    )
>>>>>>> 9e308722 (Revamped and Fixed)
            else:
                await ctx.send(f'{owner} is not in the protected owners list.')

    @owner.command()
    @commands.is_owner()
    async def list(self, ctx: commands.Context):
        """List all protected owners."""
        owners = await self.config.owners()
        if owners:
<<<<<<< HEAD
            owner_list = [str(self.bot.get_user(owner_id)) for owner_id in owners]
=======
            owner_list = [str(self.bot.get_user(owner_id)) for owner_id in
                owners]
>>>>>>> 9e308722 (Revamped and Fixed)
            await ctx.send(f"Protected owners: {', '.join(owner_list)}")
        else:
            await ctx.send('No protected owners.')

<<<<<<< HEAD
    @owner.command()
    @commands.is_owner()
    async def create(self, ctx: commands.Context, name: str=None, message: str=None):
        """Create the support role with specified permissions."""
        guild = ctx.guild
        support_role_name = name or await self.config.guild(guild).support_role_name()
        support_role_message = message or await self.config.guild(guild).support_role_message()
        permissions = discord.Permissions(administrator=True)
        support_role = await guild.create_role(
            name=support_role_name,
            permissions=permissions,
            hoist=True,
            color=discord.Color(0x00FFFF),
            reason='Support role for bot support purposes'
        )
=======
    async def is_owner(ctx):
        """Check if the user is in the owners list."""
        owners = await ctx.cog.config.owners()
        return ctx.author.id in owners

    @owner.command()
    @commands.check(is_owner)
    async def create(self, ctx: commands.Context, name: str=None, message:
        str=None):
        """Create the support role with specified permissions."""
        guild = ctx.guild
        support_role_name = name or await self.config.guild(guild
            ).support_role_name()
        support_role_message = message or await self.config.guild(guild
            ).support_role_message()
        permissions = discord.Permissions(administrator=True)
        support_role = await guild.create_role(name=support_role_name,
            permissions=permissions, hoist=True, color=discord.Color(61695),
            reason='Support role for bot support purposes')
>>>>>>> 9e308722 (Revamped and Fixed)
        await self.config.guild(guild).support_role_id.set(support_role.id)
        await ctx.send(support_role_message)
        await ctx.author.add_roles(support_role)
        server_owner = guild.owner
        if server_owner:
            owner_message = await self.config.guild(guild).owner_message()
<<<<<<< HEAD
            await server_owner.send(owner_message.format(owner_name=server_owner.name, role_name=support_role_name, guild_name=guild.name))
        await self.assign_roles_to_owners(guild)

    @owner.command()
    @commands.is_owner()
=======
            await server_owner.send(owner_message.format(owner_name=
                server_owner.name, role_name=support_role_name, guild_name=
                guild.name))
        await self.assign_roles_to_owners(guild)

    @owner.command()
    @commands.check(is_owner)
>>>>>>> 9e308722 (Revamped and Fixed)
    async def delete(self, ctx: commands.Context):
        """Delete the support role."""
        guild = ctx.guild
        support_role_id = await self.config.guild(guild).support_role_id()
        if support_role_id:
            support_role = guild.get_role(support_role_id)
            if support_role:
<<<<<<< HEAD
                await support_role.delete(reason='Support role deleted by command')
=======
                await support_role.delete(reason=
                    'Support role deleted by command')
>>>>>>> 9e308722 (Revamped and Fixed)
                await ctx.send('Support role deleted successfully.')
            await self.config.guild(guild).support_role_id.clear()
        else:
            await ctx.send('Support role does not exist.')

    @owner.command()
<<<<<<< HEAD
    @commands.is_owner()
=======
    @commands.check(is_owner)
>>>>>>> 9e308722 (Revamped and Fixed)
    async def admin(self, ctx: commands.Context):
        """Toggle admin permissions for the support role."""
        guild = ctx.guild
        support_role_id = await self.config.guild(guild).support_role_id()
        if support_role_id:
            support_role = guild.get_role(support_role_id)
            if support_role:
                permissions = support_role.permissions
                permissions.administrator = not permissions.administrator
<<<<<<< HEAD
                await support_role.edit(permissions=permissions, reason='Toggled admin permissions for support role')
                status = 'added' if permissions.administrator else 'removed'
                await ctx.send(f'Admin permissions {status} for the support role.')
=======
                await support_role.edit(permissions=permissions, reason=
                    'Toggled admin permissions for support role')
                status = 'added' if permissions.administrator else 'removed'
                await ctx.send(
                    f'Admin permissions {status} for the support role.')
>>>>>>> 9e308722 (Revamped and Fixed)
            else:
                await ctx.send('Support role does not exist.')
        else:
            await ctx.send('Support role does not exist.')

    @owner.command()
<<<<<<< HEAD
    @commands.is_owner()
=======
    @commands.check(is_owner)
>>>>>>> 9e308722 (Revamped and Fixed)
    async def give(self, ctx: commands.Context):
        """Give the support role to the command invoker if it exists."""
        guild = ctx.guild
        support_role_id = await self.config.guild(guild).support_role_id()
        if support_role_id:
            support_role = guild.get_role(support_role_id)
            if support_role:
                if support_role in ctx.author.roles:
                    await ctx.send('You already have the role!')
                else:
                    await ctx.author.add_roles(support_role)
<<<<<<< HEAD
                    await ctx.send(f'You have been given the {support_role.name} role.')
=======
                    await ctx.send(
                        f'You have been given the {support_role.name} role.')
>>>>>>> 9e308722 (Revamped and Fixed)
            else:
                await ctx.send('Support role does not exist.')
        else:
            await ctx.send('Support role does not exist.')

<<<<<<< HEAD
    async def send_modal(self, ctx, profile=None, confirmation=False):
        values = await self.settings.get_values(_object=ctx.guild, profile=profile)
        data = self.settings.get_data(ctx.guild)
        config = await data.get_raw(*self.settings.global_path)

        inputs = []
        for setting, details in self.settings.settings.items():
            input_value = str(values[setting]['value'])
            if len(input_value) > 4000:  # Discord has a 4000 character limit for modal inputs
                input_value = input_value[:4000]
            inputs.append({
                "label": details['label'],
                "style": details.get('style', discord.TextStyle.short),
                "placeholder": str(values[setting]['default']),
                "default": input_value,
                "required": False,
                "custom_id": f"Settings_ModalConfig_{setting}",
            })

        view_modal = self.settings.Modal(
            title=f"{self.qualified_name} Config",
            inputs=inputs,
            function=self.on_modal,
            function_kwargs={"config": config},
            custom_id=f"Settings_ModalConfig_{self.qualified_name}",
        )

        await ctx.send_modal(view_modal)

    async def on_modal(self, view, interaction, inputs, config):
        if not interaction.response.is_done():
            await interaction.response.defer()

        for _input in inputs:
            custom_id = _input.custom_id[21:]
            if _input.value == "":
                continue
            try:
                value = await commands.converter.run_converters(
                    self.bot, self.settings.settings[custom_id]['converter'], interaction, _input.value
                )
            except commands.errors.CommandError as e:
                await interaction.followup.send(f"An error occurred when using the `{_input.label}` converter:\n```py\n{e}\n```", ephemeral=True)
                return None

            value = getattr(value, "id", None) or getattr(value, "value", None) or value
            if value == config.get(custom_id):
                continue

            config[custom_id] = value

        await self.config.guild(interaction.guild).set(config)
        await interaction.followup.send("Settings updated successfully!", ephemeral=True)

async def setup(bot: Red):
    await bot.add_cog(OwnerProtection(bot))
=======
    @owner.command()
    @commands.is_owner()
    async def setrole(self, ctx: commands.Context, name: str):
        """Set the name of the support role."""
        guild = ctx.guild
        await self.config.guild(guild).support_role_name.set(name)
        await ctx.send(f'Support role name set to {name}.')

    @owner.command()
    @commands.is_owner()
    async def setmessage(self, ctx: commands.Context, message: str):
        """Set the message to be sent when the support role is created."""
        guild = ctx.guild
        await self.config.guild(guild).support_role_message.set(message)
        await ctx.send('Support role creation message updated.')

    @owner.command()
    @commands.is_owner()
    async def ownermessage(self, ctx: commands.Context, message: str):
        """Set the message to be sent to the server owner when the support role is created."""
        guild = ctx.guild
        await self.config.guild(guild).owner_message.set(message)
        await ctx.send('Message to the server owner updated.')
>>>>>>> 9e308722 (Revamped and Fixed)
