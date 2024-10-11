import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from typing import Dict, List, Optional
import asyncio
import datetime
from Star_Utils import Cog, Buttons, Dropdown, Modal

class StaffHierarchy:
    def __init__(self, name: str, levels: Dict[int, str], role_ids: Dict[int, int]):
        self.name = name
        self.levels = levels
        self.role_ids = role_ids

class StaffMember:
    def __init__(self, user_id: int, hierarchy: str, level: int):
        self.user_id = user_id
        self.hierarchy = hierarchy
        self.level = level
        self.join_date = datetime.datetime.utcnow()
        self.performance_score = 0
        self.warnings = 0
        self.notes = []

class StaffFlow(Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)

        default_guild = {
            "hierarchies": {},
            "staff_members": {},
            "staff_channels": {},
            "settings": {
                "auto_role_update": True,
                "performance_review_interval": 30,  # days
                "warning_threshold": 3
            }
        }

        self.config.register_guild(**default_guild)

    @commands.group(name="staffflow", invoke_without_command=True)
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def staffflow(self, ctx: commands.Context):
        """Staffer management system"""
        if ctx.invoked_subcommand is None:
            await self.send_main_menu(ctx)

    @staffflow.group(name="hierarchy", invoke_without_command=True)
    async def hierarchy(self, ctx: commands.Context):
        """Manage staff hierarchies"""
        if ctx.invoked_subcommand is None:
            await self.send_hierarchy_menu(ctx)

    @hierarchy.command(name="add")
    async def add_hierarchy(self, ctx: commands.Context, name: str):
        """Add a new hierarchy"""
        await self.add_hierarchy_modal(ctx, name)

    @hierarchy.command(name="edit")
    async def edit_hierarchy(self, ctx: commands.Context, name: str):
        """Edit an existing hierarchy"""
        await self.edit_hierarchy_menu(ctx, name)

    @hierarchy.command(name="delete")
    async def delete_hierarchy(self, ctx: commands.Context, name: str):
        """Delete a hierarchy"""
        await self.delete_hierarchy_confirm(ctx, name)

    @hierarchy.command(name="list")
    async def list_hierarchies(self, ctx: commands.Context):
        """List all hierarchies"""
        hierarchies = await self.config.guild(ctx.guild).hierarchies()
        embed = discord.Embed(title="Staff Hierarchies", color=discord.Color.blue())
        for name, data in hierarchies.items():
            levels = "\n".join([f"{level}: {role}" for level, role in data['levels'].items()])
            embed.add_field(name=name, value=levels, inline=False)
        await ctx.send(embed=embed)

    @staffflow.group(name="staff", invoke_without_command=True)
    async def staff(self, ctx: commands.Context):
        """Manage staff members"""
        if ctx.invoked_subcommand is None:
            await self.send_staff_menu(ctx)

    @staff.command(name="add")
    async def add_staff(self, ctx: commands.Context, user: discord.Member, hierarchy: str, level: int):
        """Add a new staff member"""
        await self.add_staff_member(ctx, user, hierarchy, level)

    @staff.command(name="remove")
    async def remove_staff(self, ctx: commands.Context, user: discord.Member):
        """Remove a staff member"""
        await self.remove_staff_member(ctx, user)

    @staff.command(name="promote")
    async def promote_staff(self, ctx: commands.Context, user: discord.Member):
        """Promote a staff member"""
        await self.promote_staff_member(ctx, user)

    @staff.command(name="demote")
    async def demote_staff(self, ctx: commands.Context, user: discord.Member):
        """Demote a staff member"""
        await self.demote_staff_member(ctx, user)

    @staff.command(name="info")
    async def staff_info(self, ctx: commands.Context, user: discord.Member):
        """View staff member information"""
        await self.show_staff_info(ctx, user)

    @staff.command(name="list")
    async def list_staff(self, ctx: commands.Context, hierarchy: Optional[str] = None):
        """List all staff members or staff in a specific hierarchy"""
        await self.list_staff_members(ctx, hierarchy)

    @staffflow.group(name="settings", invoke_without_command=True)
    async def settings(self, ctx: commands.Context):
        """Manage Staffer settings"""
        if ctx.invoked_subcommand is None:
            await self.send_settings_menu(ctx)

    @settings.command(name="autorole")
    async def set_auto_role(self, ctx: commands.Context, enabled: bool):
        """Enable or disable automatic role updates"""
        async with self.config.guild(ctx.guild).settings() as settings:
            settings['auto_role_update'] = enabled
        await ctx.send(f"Automatic role updates {'enabled' if enabled else 'disabled'}.")

    @settings.command(name="reviewinterval")
    async def set_review_interval(self, ctx: commands.Context, days: int):
        """Set the interval for performance reviews"""
        async with self.config.guild(ctx.guild).settings() as settings:
            settings['performance_review_interval'] = days
        await ctx.send(f"Performance review interval set to {days} days.")

    @settings.command(name="warningthreshold")
    async def set_warning_threshold(self, ctx: commands.Context, threshold: int):
        """Set the warning threshold for staff members"""
        async with self.config.guild(ctx.guild).settings() as settings:
            settings['warning_threshold'] = threshold
        await ctx.send(f"Warning threshold set to {threshold}.")

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        """Listen for role updates and update staff status if necessary"""
        if before.roles == after.roles:
            return

        settings = await self.config.guild(after.guild).settings()
        if not settings['auto_role_update']:
            return

        hierarchies = await self.config.guild(after.guild).hierarchies()
        staff_members = await self.config.guild(after.guild).staff_members()

        for hierarchy, data in hierarchies.items():
            for level, role_id in data['role_ids'].items():
                role = after.guild.get_role(role_id)
                if role and role in after.roles and role not in before.roles:
                    if str(after.id) not in staff_members:
                        await self.add_staff_member(None, after, hierarchy, int(level), auto=True)
                    else:
                        await self.update_staff_member(None, after, hierarchy, int(level), auto=True)
                    return

    async def add_staff_member(self, ctx: Optional[commands.Context], user: discord.Member, hierarchy: str, level: int, auto: bool = False):
        async with self.config.guild(user.guild).staff_members() as staff_members:
            if str(user.id) in staff_members:
                if not auto:
                    await ctx.send("This user is already a staff member.")
                return

            staff_member = StaffMember(user.id, hierarchy, level)
            staff_members[str(user.id)] = staff_member.__dict__

        hierarchies = await self.config.guild(user.guild).hierarchies()
        if hierarchy in hierarchies and str(level) in hierarchies[hierarchy]['role_ids']:
            role_id = hierarchies[hierarchy]['role_ids'][str(level)]
            role = user.guild.get_role(role_id)
            if role:
                await user.add_roles(role)

        if not auto:
            await ctx.send(f"{user.mention} has been added as a level {level} staff member in the {hierarchy} hierarchy.")
        else:
            channel_id = await self.config.guild(user.guild).staff_channels.get("log_channel")
            if channel_id:
                channel = user.guild.get_channel(channel_id)
                if channel:
                    await channel.send(f"{user.mention} has been automatically added as a level {level} staff member in the {hierarchy} hierarchy.")

    async def update_staff_member(self, ctx: Optional[commands.Context], user: discord.Member, hierarchy: str, level: int, auto: bool = False):
        async with self.config.guild(user.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                if not auto:
                    await ctx.send("This user is not a staff member.")
                return

            staff_member = StaffMember(**staff_members[str(user.id)])
            old_hierarchy = staff_member.hierarchy
            old_level = staff_member.level

            staff_member.hierarchy = hierarchy
            staff_member.level = level
            staff_members[str(user.id)] = staff_member.__dict__

        hierarchies = await self.config.guild(user.guild).hierarchies()
        if old_hierarchy in hierarchies and str(old_level) in hierarchies[old_hierarchy]['role_ids']:
            old_role_id = hierarchies[old_hierarchy]['role_ids'][str(old_level)]
            old_role = user.guild.get_role(old_role_id)
            if old_role:
                await user.remove_roles(old_role)

        if hierarchy in hierarchies and str(level) in hierarchies[hierarchy]['role_ids']:
            new_role_id = hierarchies[hierarchy]['role_ids'][str(level)]
            new_role = user.guild.get_role(new_role_id)
            if new_role:
                await user.add_roles(new_role)

        if not auto:
            await ctx.send(f"{user.mention}'s staff status has been updated to level {level} in the {hierarchy} hierarchy.")
        else:
            channel_id = await self.config.guild(user.guild).staff_channels.get("log_channel")
            if channel_id:
                channel = user.guild.get_channel(channel_id)
                if channel:
                    await channel.send(f"{user.mention}'s staff status has been automatically updated to level {level} in the {hierarchy} hierarchy.")

    async def remove_staff_member(self, ctx: commands.Context, user: discord.Member):
        async with self.config.guild(ctx.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                await ctx.send("This user is not a staff member.")
                return

            staff_member = StaffMember(**staff_members.pop(str(user.id)))

        hierarchies = await self.config.guild(ctx.guild).hierarchies()
        if staff_member.hierarchy in hierarchies and str(staff_member.level) in hierarchies[staff_member.hierarchy]['role_ids']:
            role_id = hierarchies[staff_member.hierarchy]['role_ids'][str(staff_member.level)]
            role = ctx.guild.get_role(role_id)
            if role:
                await user.remove_roles(role)

        await ctx.send(f"{user.mention} has been removed from the staff team.")

    async def promote_staff_member(self, ctx: commands.Context, user: discord.Member):
        async with self.config.guild(ctx.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                await ctx.send("This user is not a staff member.")
                return

            staff_member = StaffMember(**staff_members[str(user.id)])

        hierarchies = await self.config.guild(ctx.guild).hierarchies()
        if staff_member.hierarchy not in hierarchies:
            await ctx.send("Invalid hierarchy for this staff member.")
            return

        hierarchy = hierarchies[staff_member.hierarchy]
        next_level = str(staff_member.level + 1)

        if next_level not in hierarchy['levels']:
            await ctx.send("This staff member is already at the highest level in their hierarchy.")
            return

        await self.update_staff_member(ctx, user, staff_member.hierarchy, int(next_level))

    async def demote_staff_member(self, ctx: commands.Context, user: discord.Member):
        async with self.config.guild(ctx.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                await ctx.send("This user is not a staff member.")
                return

            staff_member = StaffMember(**staff_members[str(user.id)])

        hierarchies = await self.config.guild(ctx.guild).hierarchies()
        if staff_member.hierarchy not in hierarchies:
            await ctx.send("Invalid hierarchy for this staff member.")
            return

        hierarchy = hierarchies[staff_member.hierarchy]
        prev_level = str(staff_member.level - 1)

        if prev_level not in hierarchy['levels']:
            await ctx.send("This staff member is already at the lowest level in their hierarchy.")
            return

        await self.update_staff_member(ctx, user, staff_member.hierarchy, int(prev_level))

    async def show_staff_info(self, ctx: commands.Context, user: discord.Member):
        async with self.config.guild(ctx.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                await ctx.send("This user is not a staff member.")
                return

            staff_member = StaffMember(**staff_members[str(user.id)])

        hierarchies = await self.config.guild(ctx.guild).hierarchies()
        hierarchy = hierarchies.get(staff_member.hierarchy, {})
        level_name = hierarchy.get('levels', {}).get(str(staff_member.level), "Unknown")

        embed = discord.Embed(title=f"Staff Info - {user.name}", color=discord.Color.blue())
        embed.add_field(name="Hierarchy", value=staff_member.hierarchy, inline=False)
        embed.add_field(name="Level", value=f"{staff_member.level} ({level_name})", inline=False)
        embed.add_field(name="Join Date", value=staff_member.join_date.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Performance Score", value=staff_member.performance_score, inline=False)
        embed.add_field(name="Warnings", value=staff_member.warnings, inline=False)

        if staff_member.notes:
            embed.add_field(name="Notes", value="\n".join(staff_member.notes), inline=False)

        await ctx.send(embed=embed)

    async def list_staff_members(self, ctx: commands.Context, hierarchy: Optional[str] = None):
        staff_members = await self.config.guild(ctx.guild).staff_members()
        hierarchies = await self.config.guild(ctx.guild).hierarchies()

        if hierarchy and hierarchy not in hierarchies:
            await ctx.send("Invalid hierarchy specified.")
            return

        embed = discord.Embed(title="Staff Members", color=discord.Color.blue())

        for member_id, member_data in staff_members.items():
            member = StaffMember(**member_data)
            if hierarchy and member.hierarchy != hierarchy:
                continue

            user = ctx.guild.get_member(member.user_id)
            if user:
                level_name = hierarchies.get(member.hierarchy, {}).get('levels', {}).get(str(member.level), "Unknown")
                embed.add_field(name=user.name, value=f"Hierarchy: {member.hierarchy}\nLevel: {member.level} ({level_name})", inline=False)

        if not embed.fields:
            await ctx.send("No staff members found.")
        else:
            await ctx.send(embed=embed)

    async def send_main_menu(self, ctx: commands.Context):
        embed = discord.Embed(title="Staffer Management", description="Select an option to manage your staff team.", color=discord.Color.blue())

        buttons = [
            {"style": discord.ButtonStyle.primary, "label": "Manage Hierarchies", "custom_id": "hierarchies"},
            {"style": discord.ButtonStyle.primary, "label": "Manage Staff", "custom_id": "staff"},
            {"style": discord.ButtonStyle.primary, "label": "View Statistics", "custom_id": "stats"},
            {"style": discord.ButtonStyle.secondary, "label": "Settings", "custom_id": "settings"}
        ]

        view = Buttons(timeout=None, buttons=buttons, function=self.handle_main_menu)
        if interaction.response.is_done():
            await interaction.followup.send(embed=embed, view=view)
        else:
            await interaction.response.send_message(embed=embed, view=view)

    async def handle_main_menu(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]

        if action == "hierarchies":
            await self.send_hierarchy_menu(interaction)
        elif action == "staff":
            await self.send_staff_menu(interaction)
        elif action == "stats":
            await self.send_stats(interaction)
        elif action == "settings":
            await self.send_settings_menu(interaction)

    async def send_hierarchy_menu(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Manage Hierarchies", description="Select an action to manage hierarchies.", color=discord.Color.green())

        buttons = [
            {"style": discord.ButtonStyle.primary, "label": "Add Hierarchy", "custom_id": "add_hierarchy"},
            {"style": discord.ButtonStyle.primary, "label": "Edit Hierarchy", "custom_id": "edit_hierarchy"},
            {"style": discord.ButtonStyle.danger, "label": "Delete Hierarchy", "custom_id": "delete_hierarchy"},
            {"style": discord.ButtonStyle.secondary, "label": "Back", "custom_id": "back"}
        ]

        view = Buttons(timeout=None, buttons=buttons, function=self.handle_hierarchy_menu)
        await interaction.response.send_message(embed=embed, view=view)

    async def handle_hierarchy_menu(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]

        if action == "add_hierarchy":
            await self.add_hierarchy_modal(interaction)
        elif action == "edit_hierarchy":
            await self.edit_hierarchy_dropdown(interaction)
        elif action == "delete_hierarchy":
            await self.delete_hierarchy_dropdown(interaction)
        elif action == "back":
            await self.send_main_menu(interaction)

    async def add_hierarchy_modal(self, interaction: discord.Interaction):
        modal = Modal(title="Add New Hierarchy", inputs=[
            {"label": "Hierarchy Name", "style": discord.TextStyle.short, "custom_id": "name", "required": True},
            {"label": "Levels (comma-separated)", "style": discord.TextStyle.paragraph, "custom_id": "levels", "required": True}
        ])

        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            return await interaction.followup.send("Hierarchy creation timed out.", ephemeral=True)

        name = inputs[0].value
        levels = [level.strip() for level in inputs[1].value.split(",")]

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if name in hierarchies:
                return await modal_interaction.response.send_message("A hierarchy with this name already exists.", ephemeral=True)

            hierarchies[name] = {"levels": {str(i+1): level for i, level in enumerate(levels)}, "role_ids": {}}

        await modal_interaction.response.send_message(f"Hierarchy '{name}' created with levels: {', '.join(levels)}", ephemeral=True)

    async def edit_hierarchy_dropdown(self, interaction: discord.Interaction):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        if not hierarchies:
            return await interaction.response.send_message("No hierarchies exist yet.", ephemeral=True)

        options = [{"label": name, "value": name} for name in hierarchies.keys()]
        select_menu = Dropdown(placeholder="Select a hierarchy to edit", options=options, min_values=1, max_values=1)

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: List[str]):
            await self.edit_hierarchy_menu(interaction, values[0])

        select_menu.function = handle_selection
        await interaction.response.send_message("Select a hierarchy to edit:", view=select_menu)

    async def edit_hierarchy_menu(self, interaction: discord.Interaction, hierarchy_name: str):
        embed = discord.Embed(title=f"Edit Hierarchy: {hierarchy_name}", description="Select an action to edit the hierarchy.", color=discord.Color.orange())

        buttons = [
            {"style": discord.ButtonStyle.primary, "label": "Add Level", "custom_id": "add_level"},
            {"style": discord.ButtonStyle.primary, "label": "Remove Level", "custom_id": "remove_level"},
            {"style": discord.ButtonStyle.primary, "label": "Set Role", "custom_id": "set_role"},
            {"style": discord.ButtonStyle.secondary, "label": "Back", "custom_id": "back"}
        ]

        view = Buttons(timeout=None, buttons=buttons, function=lambda v, i: self.handle_edit_hierarchy_menu(v, i, hierarchy_name))
        await interaction.response.send_message(embed=embed, view=view)

    async def handle_edit_hierarchy_menu(self, view: Buttons, interaction: discord.Interaction, hierarchy_name: str):
        action = interaction.data["custom_id"]

        if action == "add_level":
            await self.add_level_modal(interaction, hierarchy_name)
        elif action == "remove_level":
            await self.remove_level_dropdown(interaction, hierarchy_name)
        elif action == "set_role":
            await self.set_role_dropdown(interaction, hierarchy_name)
        elif action == "back":
            await self.send_hierarchy_menu(interaction)

    async def add_level_modal(self, interaction: discord.Interaction, hierarchy_name: str):
        modal = Modal(title=f"Add Level to {hierarchy_name}", inputs=[
            {"label": "Level Name", "style": discord.TextStyle.short, "custom_id": "level_name", "required": True}
        ])

        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            return await interaction.followup.send("Level addition timed out.", ephemeral=True)

        level_name = inputs[0].value

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name not in hierarchies:
                return await modal_interaction.response.send_message("Hierarchy not found.", ephemeral=True)

            new_level = str(len(hierarchies[hierarchy_name]['levels']) + 1)
            hierarchies[hierarchy_name]['levels'][new_level] = level_name

        await modal_interaction.response.send_message(f"Added level {new_level}: {level_name} to {hierarchy_name}", ephemeral=True)

    async def remove_level_dropdown(self, interaction: discord.Interaction, hierarchy_name: str):
        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name not in hierarchies:
                return await interaction.response.send_message("Hierarchy not found.", ephemeral=True)

            levels = hierarchies[hierarchy_name]['levels']

            if not levels:
                return await interaction.response.send_message("This hierarchy has no levels to remove.", ephemeral=True)

            options = [{"label": f"Level {level}: {name}", "value": level} for level, name in levels.items()]
            select_menu = Dropdown(placeholder="Select a level to remove", options=options, min_values=1, max_values=1)

            async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: List[str]):
                level_to_remove = values[0]
                del hierarchies[hierarchy_name]['levels'][level_to_remove]
                if level_to_remove in hierarchies[hierarchy_name]['role_ids']:
                    del hierarchies[hierarchy_name]['role_ids'][level_to_remove]
                await interaction.response.send_message(f"Removed level {level_to_remove} from {hierarchy_name}", ephemeral=True)

            select_menu.function = handle_selection
            await interaction.response.send_message("Select a level to remove:", view=select_menu)

    async def set_role_dropdown(self, interaction: discord.Interaction, hierarchy_name: str):
        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name not in hierarchies:
                return await interaction.response.send_message("Hierarchy not found.", ephemeral=True)

            levels = hierarchies[hierarchy_name]['levels']

            if not levels:
                return await interaction.response.send_message("This hierarchy has no levels to set roles for.", ephemeral=True)

            options = [{"label": f"Level {level}: {name}", "value": level} for level, name in levels.items()]
            select_menu = Dropdown(placeholder="Select a level to set role", options=options, min_values=1, max_values=1)

            async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: List[str]):
                level = values[0]
                await self.set_role_modal(interaction, hierarchy_name, level)

            select_menu.function = handle_selection
            await interaction.response.send_message("Select a level to set role:", view=select_menu)

    async def set_role_modal(self, interaction: discord.Interaction, hierarchy_name: str, level: str):
        modal = Modal(title=f"Set Role for {hierarchy_name} Level {level}", inputs=[
            {"label": "Role ID", "style": discord.TextStyle.short, "custom_id": "role_id", "required": True}
        ])

        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            return await interaction.followup.send("Role setting timed out.", ephemeral=True)

        role_id = int(inputs[0].value)
        role = interaction.guild.get_role(role_id)

        if not role:
            return await modal_interaction.response.send_message("Invalid role ID.", ephemeral=True)

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            hierarchies[hierarchy_name]['role_ids'][level] = role_id

        await modal_interaction.response.send_message(f"Set {role.name} as the role for level {level} in {hierarchy_name}", ephemeral=True)

    async def delete_hierarchy_dropdown(self, interaction: discord.Interaction):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        if not hierarchies:
            return await interaction.response.send_message("No hierarchies exist to delete.", ephemeral=True)

        options = [{"label": name, "value": name} for name in hierarchies.keys()]
        select_menu = Dropdown(placeholder="Select a hierarchy to delete", options=options, min_values=1, max_values=1)

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: List[str]):
            hierarchy_to_delete = values[0]
            await self.delete_hierarchy_confirm(interaction, hierarchy_to_delete)

        select_menu.function = handle_selection
        await interaction.response.send_message("Select a hierarchy to delete:", view=select_menu)

    async def delete_hierarchy_confirm(self, interaction: discord.Interaction, hierarchy_name: str):
        embed = discord.Embed(title=f"Confirm Deletion: {hierarchy_name}", description="Are you sure you want to delete this hierarchy? This action cannot be undone.", color=discord.Color.red())

        buttons = [
            {"style": discord.ButtonStyle.danger, "label": "Delete", "custom_id": "confirm_delete"},
            {"style": discord.ButtonStyle.secondary, "label": "Cancel", "custom_id": "cancel_delete"}
        ]

        view = Buttons(timeout=None, buttons=buttons, function=lambda v, i: self.handle_delete_hierarchy_confirm(v, i, hierarchy_name))
        await interaction.response.send_message(embed=embed, view=view)

    async def handle_delete_hierarchy_confirm(self, view: Buttons, interaction: discord.Interaction, hierarchy_name: str):
        action = interaction.data["custom_id"]

        if action == "confirm_delete":
            async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
                if hierarchy_name in hierarchies:
                    del hierarchies[hierarchy_name]
                    await interaction.response.send_message(f"Hierarchy '{hierarchy_name}' has been deleted.", ephemeral=True)
                else:
                    await interaction.response.send_message("Hierarchy not found.", ephemeral=True)
        elif action == "cancel_delete":
            await interaction.response.send_message("Hierarchy deletion cancelled.", ephemeral=True)

    async def send_staff_menu(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Manage Staff", description="Select an action to manage staff members.", color=discord.Color.gold())

        buttons = [
            {"style": discord.ButtonStyle.primary, "label": "Add Staff", "custom_id": "add_staff"},
            {"style": discord.ButtonStyle.primary, "label": "Remove Staff", "custom_id": "remove_staff"},
            {"style": discord.ButtonStyle.primary, "label": "Promote Staff", "custom_id": "promote_staff"},
            {"style": discord.ButtonStyle.primary, "label": "Demote Staff", "custom_id": "demote_staff"},
            {"style": discord.ButtonStyle.secondary, "label": "Back", "custom_id": "back"}
        ]

        view = Buttons(timeout=None, buttons=buttons, function=self.handle_staff_menu)
        await interaction.response.send_message(embed=embed, view=view)

    async def handle_staff_menu(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]

        if action == "add_staff":
            await self.add_staff_modal(interaction)
        elif action == "remove_staff":
            await self.remove_staff_dropdown(interaction)
        elif action == "promote_staff":
            await self.promote_staff_dropdown(interaction)
        elif action == "demote_staff":
            await self.demote_staff_dropdown(interaction)
        elif action == "back":
            await self.send_main_menu(interaction)

    async def add_staff_modal(self, interaction: discord.Interaction):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        hierarchy_options = [{"label": name, "value": name} for name in hierarchies.keys()]

        modal = Modal(title="Add Staff Member", inputs=[
            {"label": "User ID", "style": discord.TextStyle.short, "custom_id": "user_id", "required": True},
            {"label": "Hierarchy", "style": discord.TextStyle.short, "custom_id": "hierarchy", "required": True},
            {"label": "Level", "style": discord.TextStyle.short, "custom_id": "level", "required": True}
        ])

        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            return await interaction.followup.send("Staff addition timed out.", ephemeral=True)

        user_id = int(inputs[0].value)
        hierarchy = inputs[1].value
        level = int(inputs[2].value)

        user = interaction.guild.get_member(user_id)
        if not user:
            return await modal_interaction.response.send_message("User not found in the server.", ephemeral=True)

        if hierarchy not in hierarchies:
            return await modal_interaction.response.send_message("Invalid hierarchy specified.", ephemeral=True)

        if str(level) not in hierarchies[hierarchy]['levels']:
            return await modal_interaction.response.send_message("Invalid level specified for the chosen hierarchy.", ephemeral=True)

        await self.add_staff_member(modal_interaction, user, hierarchy, level)

    async def remove_staff_dropdown(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()

        if not staff_members:
            return await interaction.response.send_message("There are no staff members to remove.", ephemeral=True)

        options = [{"label": f"{interaction.guild.get_member(int(user_id)).name}", "value": user_id} for user_id in staff_members.keys() if interaction.guild.get_member(int(user_id))]
        select_menu = Dropdown(placeholder="Select a staff member to remove", options=options, min_values=1, max_values=1)

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: List[str]):
            user_id = int(values[0])
            user = interaction.guild.get_member(user_id)
            if user:
                await self.remove_staff_member(interaction, user)
            else:
                await interaction.response.send_message("Selected user not found in the server.", ephemeral=True)

        select_menu.function = handle_selection
        await interaction.response.send_message("Select a staff member to remove:", view=select_menu)

    async def promote_staff_dropdown(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()

        if not staff_members:
            return await interaction.response.send_message("There are no staff members to promote.", ephemeral=True)

        options = [{"label": f"{interaction.guild.get_member(int(user_id)).name}", "value": user_id} for user_id in staff_members.keys() if interaction.guild.get_member(int(user_id))]
        select_menu = Dropdown(placeholder="Select a staff member to promote", options=options, min_values=1, max_values=1)

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: List[str]):
            user_id = int(values[0])
            user = interaction.guild.get_member(user_id)
            if user:
                await self.promote_staff_member(interaction, user)
            else:
                await interaction.response.send_message("Selected user not found in the server.", ephemeral=True)

        select_menu.function = handle_selection
        await interaction.response.send_message("Select a staff member to promote:", view=select_menu)

    async def demote_staff_dropdown(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()

        if not staff_members:
            return await interaction.response.send_message("There are no staff members to demote.", ephemeral=True)

        options = [{"label": f"{interaction.guild.get_member(int(user_id)).name}", "value": user_id} for user_id in staff_members.keys() if interaction.guild.get_member(int(user_id))]
        select_menu = Dropdown(placeholder="Select a staff member to demote", options=options, min_values=1, max_values=1)

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: List[str]):
            user_id = int(values[0])
            user = interaction.guild.get_member(user_id)
            if user:
                await self.demote_staff_member(interaction, user)
            else:
                await interaction.response.send_message("Selected user not found in the server.", ephemeral=True)

        select_menu.function = handle_selection
        await interaction.response.send_message("Select a staff member to demote:", view=select_menu)

    async def send_stats(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        embed = discord.Embed(title="Staff Statistics", color=discord.Color.blue())
        embed.add_field(name="Total Staff Members", value=str(len(staff_members)), inline=False)

        for hierarchy in hierarchies:
            staff_in_hierarchy = [member for member in staff_members.values() if member['hierarchy'] == hierarchy]
            embed.add_field(name=f"{hierarchy} Staff", value=str(len(staff_in_hierarchy)), inline=True)

        await interaction.response.send_message(embed=embed)

    async def send_settings_menu(self, interaction: discord.Interaction):
        settings = await self.config.guild(interaction.guild).settings()

        embed = discord.Embed(title="Staffer Settings", description="Current settings:", color=discord.Color.purple())
        embed.add_field(name="Auto Role Update", value="Enabled" if settings['auto_role_update'] else "Disabled", inline=False)
        embed.add_field(name="Performance Review Interval", value=f"{settings['performance_review_interval']} days", inline=False)
        embed.add_field(name="Warning Threshold", value=str(settings['warning_threshold']), inline=False)

        buttons = [
            {"style": discord.ButtonStyle.primary, "label": "Toggle Auto Role Update", "custom_id": "toggle_auto_role"},
            {"style": discord.ButtonStyle.primary, "label": "Set Review Interval", "custom_id": "set_review_interval"},
            {"style": discord.ButtonStyle.primary, "label": "Set Warning Threshold", "custom_id": "set_warning_threshold"},
            {"style": discord.ButtonStyle.secondary, "label": "Back", "custom_id": "back"}
        ]

        view = Buttons(timeout=None, buttons=buttons, function=self.handle_settings_menu)
        await interaction.response.send_message(embed=embed, view=view)

    async def handle_settings_menu(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]

        if action == "toggle_auto_role":
            await self.toggle_auto_role(interaction)
        elif action == "set_review_interval":
            await self.set_review_interval_modal(interaction)
        elif action == "set_warning_threshold":
            await self.set_warning_threshold_modal(interaction)
        elif action == "back":
            await self.send_main_menu(interaction)

    async def toggle_auto_role(self, interaction: discord.Interaction):
        async with self.config.guild(interaction.guild).settings() as settings:
            settings['auto_role_update'] = not settings['auto_role_update']
            new_state = "enabled" if settings['auto_role_update'] else "disabled"

        await interaction.response.send_message(f"Auto role update has been {new_state}.", ephemeral=True)
        await self.send_settings_menu(interaction)

    async def set_review_interval_modal(self, interaction: discord.Interaction):
        modal = Modal(title="Set Review Interval", inputs=[
            {"label": "Interval (in days)", "style": discord.TextStyle.short, "custom_id": "interval", "required": True}
        ])

        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            return await interaction.followup.send("Setting review interval timed out.", ephemeral=True)

        interval = int(inputs[0].value)
        async with self.config.guild(interaction.guild).settings() as settings:
            settings['performance_review_interval'] = interval

        await modal_interaction.response.send_message(f"Performance review interval set to {interval} days.", ephemeral=True)
        await self.send_settings_menu(interaction)

    async def set_warning_threshold_modal(self, interaction: discord.Interaction):
        modal = Modal(title="Set Warning Threshold", inputs=[
            {"label": "Threshold", "style": discord.TextStyle.short, "custom_id": "threshold", "required": True}
        ])

        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            return await interaction.followup.send("Setting warning threshold timed out.", ephemeral=True)

        threshold = int(inputs[0].value)
        async with self.config.guild(interaction.guild).settings() as settings:
            settings['warning_threshold'] = threshold

        await modal_interaction.response.send_message(f"Warning threshold set to {threshold}.", ephemeral=True)
        await self.send_settings_menu(interaction)
