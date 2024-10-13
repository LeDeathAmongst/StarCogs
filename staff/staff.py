<<<<<<< HEAD
import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box, pagify
from typing import Dict, List, Optional, Union
import asyncio
import datetime
import traceback
from Star_Utils import Cog, Buttons, Dropdown, Modal, Loop, CogsUtils

class StaffHierarchy:
    def __init__(self, name: str, levels: Dict[str, Dict[str, str]], role_ids: Dict[str, int]):
        self.name = name
        self.levels = levels
        self.role_ids = role_ids

class StaffMember:
    def __init__(self, user_id: int, hierarchy: str, level: str):
        self.user_id = user_id
        self.hierarchy = hierarchy
        self.level = level
        self.join_date = datetime.datetime.utcnow()
        self.performance_score = 0
        self.warnings = 0
        self.notes = []

class Staffer(Cog):
    def __init__(self, bot: Red):
        super().__init__(bot=bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.active_messages = {}

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

        self.logs = CogsUtils.get_logger(cog=self)
        self.loops = []

        self.init_loops()

    def init_loops(self):
        self.loops.append(
            Loop(
                cog=self,
                name="Performance Review",
                function=self.performance_review_loop,
                hours=24,
                wait_raw=True,
            )
        )

    async def cog_load(self):
        for loop in self.loops:
            loop.start()

    async def cog_unload(self):
        for loop in self.loops:
            loop.stop_all()

    async def performance_review_loop(self):
        self.logs.info("Running performance review loop")
        all_guilds = await self.config.all_guilds()
        for guild_id, guild_data in all_guilds.items():
            guild = self.bot.get_guild(int(guild_id))
            if not guild:
                continue
            staff_members = guild_data.get("staff_members", {})
            for member_id, member_data in staff_members.items():
                member = guild.get_member(int(member_id))
                if not member:
                    continue
                self.logs.debug(f"Reviewing performance for {member.name}")
                # Implement your performance review logic here

    @commands.group(name="staffer", invoke_without_command=True)
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def staffer(self, ctx: commands.Context):
        """Staffer management system"""
        if ctx.invoked_subcommand is None:
            await self.send_main_menu(ctx)

    async def send_main_menu(self, ctx_or_interaction: Union[commands.Context, discord.Interaction]):
        embed = discord.Embed(title="Staffer Management", description="Select an option to manage your staff team.", color=discord.Color.blue())

        options = [
            {"label": "Manage Hierarchies", "value": "hierarchies"},
            {"label": "Manage Staff", "value": "staff"},
            {"label": "View Statistics", "value": "stats"},
            {"label": "Settings", "value": "settings"}
        ]

        view = Dropdown(
            placeholder="Select an option",
            options=options,
            function=self.handle_main_menu,
            infinity=True
        )

        if isinstance(ctx_or_interaction, discord.Interaction):
            if ctx_or_interaction.response.is_done():
                message = await ctx_or_interaction.followup.send(embed=embed, view=view)
            else:
                await ctx_or_interaction.response.send_message(embed=embed, view=view)
                message = await ctx_or_interaction.original_response()
        else:
            message = await ctx_or_interaction.send(embed=embed, view=view)

        self.active_messages[ctx_or_interaction.guild.id] = message.id

    async def handle_main_menu(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        action = values[0]

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

        options = [
            {"label": "Add Hierarchy", "value": "add_hierarchy"},
            {"label": "Edit Hierarchy", "value": "edit_hierarchy"},
            {"label": "Delete Hierarchy", "value": "delete_hierarchy"},
            {"label": "List Hierarchies", "value": "list_hierarchies"},
            {"label": "Back to Main Menu", "value": "back"}
        ]

        view = Dropdown(
            placeholder="Select an action",
            options=options,
            function=self.handle_hierarchy_menu,
            infinity=True
        )
        await interaction.response.edit_message(embed=embed, view=view)

    async def handle_hierarchy_menu(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        action = values[0]

        if action == "add_hierarchy":
            await self.add_hierarchy_modal(interaction)
        elif action == "edit_hierarchy":
            await self.edit_hierarchy_dropdown(interaction)
        elif action == "delete_hierarchy":
            await self.delete_hierarchy_dropdown(interaction)
        elif action == "list_hierarchies":
            await self.list_hierarchies(interaction)
        elif action == "back":
            await self.send_main_menu(interaction)

    async def add_hierarchy_modal(self, interaction: discord.Interaction):
        example = (
            "Example configuration:\n"
            "Trial Mod\n"
            "Mod\n"
            "Senior Mod\n"
            "- Management\n"
            "Chief Security Officer\n"
            "- Next hierarchy"
        )
        modal = Modal(
            title="Add New Hierarchy",
            inputs=[
                {"label": "Hierarchy Name", "style": discord.TextStyle.short, "custom_id": "name", "required": True},
                {"label": "Levels (one per line, use '-' for promo)", "style": discord.TextStyle.paragraph, "custom_id": "levels", "required": True, "placeholder": example},
            ],
            function=self.handle_add_hierarchy_modal
        )

        await interaction.response.send_modal(modal)

    async def handle_add_hierarchy_modal(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput]):
        hierarchy_name = inputs[0].value
        levels_input = inputs[1].value.split('\n')

        levels = {}
        current_level = 0
        for line in levels_input:
            line = line.strip()
            if line.startswith('- '):
                if current_level == 0:
                    await interaction.response.send_message("Invalid format: Promotion path specified before any level.", ephemeral=True)
                    return
                promotion = line[2:].strip()
                if promotion == "Next hierarchy":
                    levels[str(current_level)]["next_hierarchy"] = True
                else:
                    levels[str(current_level)]["next"] = promotion
            else:
                current_level += 1
                levels[str(current_level)] = {"name": line, "next": None}

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name in hierarchies:
                return await interaction.response.send_message("A hierarchy with this name already exists.", ephemeral=True)

            hierarchies[hierarchy_name] = {"levels": levels, "role_ids": {}}

        await interaction.response.send_message(f"Hierarchy '{hierarchy_name}' created with {len(levels)} levels.", ephemeral=True)
        await self.send_hierarchy_menu(interaction)

    async def edit_hierarchy_dropdown(self, interaction: discord.Interaction):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        if not hierarchies:
            return await interaction.response.send_message("No hierarchies exist yet.", ephemeral=True)

        options = [{"label": name, "value": name} for name in hierarchies.keys()]
        view = Dropdown(
            placeholder="Select a hierarchy to edit",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_edit_hierarchy_selection
        )
        await interaction.response.edit_message(content="Select a hierarchy to edit:", view=view)

    async def handle_edit_hierarchy_selection(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        hierarchy_name = values[0]
        await self.edit_hierarchy_menu(interaction, hierarchy_name)

    async def edit_hierarchy_menu(self, interaction: discord.Interaction, hierarchy_name: str):
        embed = discord.Embed(title=f"Edit Hierarchy: {hierarchy_name}", description="Select an action to edit the hierarchy.", color=discord.Color.orange())

        options = [
            {"label": "Edit Levels", "value": "edit_levels"},
            {"label": "Set Role", "value": "set_role"},
            {"label": "Back to Hierarchy Menu", "value": "back"}
        ]

        view = Dropdown(
            placeholder="Select an action",
            options=options,
            min_values=1,
            max_values=1,
            function=lambda v, i, vals: self.handle_edit_hierarchy_menu(v, i, vals, hierarchy_name)
        )
        await interaction.response.edit_message(embed=embed, view=view)

    async def handle_edit_hierarchy_menu(self, view: Dropdown, interaction: discord.Interaction, values: List[str], hierarchy_name: str):
        action = values[0]

        if action == "edit_levels":
            await self.edit_levels_modal(interaction, hierarchy_name)
        elif action == "set_role":
            await self.set_role_dropdown(interaction, hierarchy_name)
        elif action == "back":
            await self.send_hierarchy_menu(interaction)

    async def edit_levels_modal(self, interaction: discord.Interaction, hierarchy_name: str):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        current_levels = hierarchies[hierarchy_name]['levels']

        current_config = "\n".join([f"{level['name']}" + (f"\n- {level['next']}" if level['next'] else "") for level in current_levels.values()])

        modal = Modal(
            title=f"Edit Levels for {hierarchy_name}",
            inputs=[
                {"label": "Levels (one per line, use '-' for promotion paths)", "style": discord.TextStyle.paragraph, "custom_id": "levels", "required": True, "value": current_config},
            ],
            function=lambda m, i, inputs: self.handle_edit_levels(m, i, inputs, hierarchy_name)
        )

        await interaction.response.send_modal(modal)

    async def handle_edit_levels(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput], hierarchy_name: str):
        levels_input = inputs[0].value.split('\n')

        levels = {}
        current_level = 0
        for line in levels_input:
            line = line.strip()
            if line.startswith('- '):
                if current_level == 0:
                    await interaction.response.send_message("Invalid format: Promotion path specified before any level.", ephemeral=True)
                    return
                promotion = line[2:].strip()
                if promotion == "Next hierarchy":
                    levels[str(current_level)]["next_hierarchy"] = True
                else:
                    levels[str(current_level)]["next"] = promotion
            else:
                current_level += 1
                levels[str(current_level)] = {"name": line, "next": None}

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            hierarchies[hierarchy_name]['levels'] = levels

        await interaction.response.send_message(f"Levels for '{hierarchy_name}' have been updated.", ephemeral=True)
        await self.edit_hierarchy_menu(interaction, hierarchy_name)

    async def set_role_dropdown(self, interaction: discord.Interaction, hierarchy_name: str):
        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name not in hierarchies:
                return await interaction.response.send_message("Hierarchy not found.", ephemeral=True)

            levels = hierarchies[hierarchy_name]['levels']

            if not levels:
                return await interaction.response.send_message("This hierarchy has no levels to set roles for.", ephemeral=True)

            options = [{"label": f"Level {level}: {data['name']}", "value": level} for level, data in levels.items()]
            view = Dropdown(
                placeholder="Select a level to set role",
                options=options,
                min_values=1,
                max_values=1,
                function=lambda v, i, vals: self.handle_set_role(v, i, vals, hierarchy_name)
            )
            await interaction.response.edit_message(content="Select a level to set role:", view=view)

    async def handle_set_role(self, view: Dropdown, interaction: discord.Interaction, values: List[str], hierarchy_name: str):
        level = values[0]
        await self.set_role_modal(interaction, hierarchy_name, level)

    async def set_role_modal(self, interaction: discord.Interaction, hierarchy_name: str, level: str):
        modal = Modal(
            title=f"Set Role for {hierarchy_name} Level {level}",
            inputs=[
                {"label": "Role ID", "style": discord.TextStyle.short, "custom_id": "role_id", "required": True}
            ],
            function=lambda m, i, inputs: self.handle_set_role_modal(m, i, inputs, hierarchy_name, level)
        )

        await interaction.response.send_modal(modal)

    async def handle_set_role_modal(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput], hierarchy_name: str, level: str):
        role_id = int(inputs[0].value)
        role = interaction.guild.get_role(role_id)

        if not role:
            return await interaction.response.send_message("Invalid role ID.", ephemeral=True)

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            hierarchies[hierarchy_name]['role_ids'][level] = role_id

        await interaction.response.send_message(f"Set {role.name} as the role for level {level} in {hierarchy_name}", ephemeral=True)
        await self.edit_hierarchy_menu(interaction, hierarchy_name)

    async def delete_hierarchy_dropdown(self, interaction: discord.Interaction):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        if not hierarchies:
            return await interaction.response.send_message("No hierarchies exist to delete.", ephemeral=True)

        options = [{"label": name, "value": name} for name in hierarchies.keys()]
        view = Dropdown(
            placeholder="Select a hierarchy to delete",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_delete_hierarchy_selection
        )
        await interaction.response.edit_message(content="Select a hierarchy to delete:", view=view)

    async def handle_delete_hierarchy_selection(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        hierarchy_to_delete = values[0]
        await self.delete_hierarchy_confirm(interaction, hierarchy_to_delete)

    async def delete_hierarchy_confirm(self, interaction: discord.Interaction, hierarchy_name: str):
        embed = discord.Embed(title=f"Confirm Deletion: {hierarchy_name}", description="Are you sure you want to delete this hierarchy? This action cannot be undone.", color=discord.Color.red())

        options = [
            {"label": "Confirm Delete", "value": "confirm_delete"},
            {"label": "Cancel", "value": "cancel_delete"}
        ]

        view = Dropdown(
            placeholder="Select an action",
            options=options,
            min_values=1,
            max_values=1,
            function=lambda v, i, vals: self.handle_delete_hierarchy_confirm(v, i, vals, hierarchy_name)
        )
        await interaction.response.edit_message(embed=embed, view=view)

    async def handle_delete_hierarchy_confirm(self, view: Dropdown, interaction: discord.Interaction, values: List[str], hierarchy_name: str):
        action = values[0]

        if action == "confirm_delete":
            async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
                if hierarchy_name in hierarchies:
                    del hierarchies[hierarchy_name]
                    await interaction.response.send_message(f"Hierarchy '{hierarchy_name}' has been deleted.", ephemeral=True)
                else:
                    await interaction.response.send_message("Hierarchy not found.", ephemeral=True)
        elif action == "cancel_delete":
            await interaction.response.send_message("Hierarchy deletion cancelled.", ephemeral=True)

        await self.send_hierarchy_menu(interaction)

    async def list_hierarchies(self, interaction: discord.Interaction):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        if not hierarchies:
            return await interaction.response.send_message("No hierarchies exist yet.", ephemeral=True)

        embed = discord.Embed(title="Hierarchies", color=discord.Color.blue())

        for name, data in hierarchies.items():
            levels = "\n".join([f"{level}: {info['name']}" for level, info in data['levels'].items()])
            embed.add_field(name=name, value=levels, inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def send_staff_menu(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Manage Staff", description="Select an action to manage staff members.", color=discord.Color.green())

        options = [
            {"label": "Add Staff Member", "value": "add_staff"},
            {"label": "Remove Staff Member", "value": "remove_staff"},
            {"label": "Promote Staff Member", "value": "promote_staff"},
            {"label": "Demote Staff Member", "value": "demote_staff"},
            {"label": "View Staff Info", "value": "staff_info"},
            {"label": "List Staff Members", "value": "list_staff"},
            {"label": "Back to Main Menu", "value": "back"}
        ]

        view = Dropdown(
            placeholder="Select an action",
            options=options,
            function=self.handle_staff_menu,
            infinity=True
        )
        await interaction.response.edit_message(embed=embed, view=view)

    async def handle_staff_menu(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        action = values[0]

        if action == "add_staff":
            await self.add_staff_dropdown(interaction)
        elif action == "remove_staff":
            await self.remove_staff_dropdown(interaction)
        elif action == "promote_staff":
            await self.promote_staff_dropdown(interaction)
        elif action == "demote_staff":
            await self.demote_staff_dropdown(interaction)
        elif action == "staff_info":
            await self.staff_info_dropdown(interaction)
        elif action == "list_staff":
            await self.list_staff_dropdown(interaction)
        elif action == "back":
            await self.send_main_menu(interaction)

    async def add_staff_dropdown(self, interaction: discord.Interaction):
        members = interaction.guild.members
        options = [{"label": member.name, "value": str(member.id)} for member in members]
        view = Dropdown(
            placeholder="Select a user",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_add_staff_user
        )
        await interaction.response.edit_message(content="Select a user to add as staff:", view=view)

    async def handle_add_staff_user(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        user_id = int(values[0])
        user = interaction.guild.get_member(user_id)
        await self.add_staff_hierarchy_dropdown(interaction, user)

    async def add_staff_hierarchy_dropdown(self, interaction: discord.Interaction, user: discord.Member):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        options = [{"label": name, "value": name} for name in hierarchies.keys()]
        view = Dropdown(
            placeholder="Select a hierarchy",
            options=options,
            min_values=1,
            max_values=1,
            function=lambda v, i, vals: self.handle_add_staff_hierarchy(v, i, vals, user)
        )
        await interaction.response.edit_message(content=f"Select a hierarchy for {user.name}:", view=view)

    async def handle_add_staff_hierarchy(self, view: Dropdown, interaction: discord.Interaction, values: List[str], user: discord.Member):
        hierarchy = values[0]
        await self.add_staff_level_dropdown(interaction, user, hierarchy)

    async def add_staff_level_dropdown(self, interaction: discord.Interaction, user: discord.Member, hierarchy: str):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        levels = hierarchies[hierarchy]['levels']
        options = [{"label": f"Level {level}: {data['name']}", "value": level} for level, data in levels.items()]
        view = Dropdown(
            placeholder="Select a level",
            options=options,
            min_values=1,
            max_values=1,
            function=lambda v, i, vals: self.handle_add_staff_level(v, i, vals, user, hierarchy)
        )
        await interaction.response.edit_message(content=f"Select a level for {user.name} in {hierarchy}:", view=view)

    async def handle_add_staff_level(self, view: Dropdown, interaction: discord.Interaction, values: List[str], user: discord.Member, hierarchy: str):
        level = values[0]
        await self.add_staff_member(interaction, user, hierarchy, level)

    async def add_staff_member(self, interaction: discord.Interaction, user: discord.Member, hierarchy: str, level: str):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) in staff_members:
                return await interaction.response.send_message("This user is already a staff member.", ephemeral=True)

            staff_member = StaffMember(user.id, hierarchy, level)
            staff_members[str(user.id)] = staff_member.__dict__

        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        if hierarchy in hierarchies and level in hierarchies[hierarchy]['role_ids']:
            role_id = hierarchies[hierarchy]['role_ids'][level]
            role = interaction.guild.get_role(role_id)
            if role:
                await user.add_roles(role)

        await interaction.response.send_message(f"{user.mention} has been added as a level {level} staff member in the {hierarchy} hierarchy.", ephemeral=True)
        await self.send_staff_menu(interaction)

    async def remove_staff_dropdown(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()
        options = [{"label": interaction.guild.get_member(int(user_id)).name, "value": user_id} for user_id in staff_members.keys() if interaction.guild.get_member(int(user_id))]
        view = Dropdown(
            placeholder="Select a staff member to remove",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_remove_staff
        )
        await interaction.response.edit_message(content="Select a staff member to remove:", view=view)

    async def handle_remove_staff(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        user_id = int(values[0])
        user = interaction.guild.get_member(user_id)
        await self.remove_staff_modal(interaction, user)

    async def remove_staff_modal(self, interaction: discord.Interaction, user: discord.Member):
        modal = Modal(
            title=f"Remove Staff: {user.name}",
            inputs=[
                {"label": "Reason", "style": discord.TextStyle.paragraph, "custom_id": "reason", "required": True},
                {"label": "Hierarchy (optional)", "style": discord.TextStyle.short, "custom_id": "hierarchy", "required": False, "placeholder": "Only if removing from one hierarchy"}
            ],
            function=lambda m, i, inputs: self.handle_remove_staff_modal(m, i, inputs, user)
        )

        await interaction.response.send_modal(modal)

    async def handle_remove_staff_modal(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput], user: discord.Member):
        reason = inputs[0].value
        hierarchy = inputs[1].value if inputs[1].value else None

        await self.remove_staff_member(interaction, user, reason, hierarchy)

    async def remove_staff_member(self, interaction: discord.Interaction, user: discord.Member, reason: str, hierarchy: Optional[str] = None):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                return await interaction.response.send_message("This user is not a staff member.", ephemeral=True)

            if hierarchy:
                if staff_members[str(user.id)]['hierarchy'] != hierarchy:
                    return await interaction.response.send_message(f"This user is not in the {hierarchy} hierarchy.", ephemeral=True)
                del staff_members[str(user.id)]
            else:
                del staff_members[str(user.id)]

        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        staff_hierarchy = hierarchies.get(hierarchy or staff_members[str(user.id)]['hierarchy'], {})
        if 'role_ids' in staff_hierarchy:
            role_id = staff_hierarchy['role_ids'].get(str(staff_members[str(user.id)]['level']))
            if role_id:
                role = interaction.guild.get_role(role_id)
                if role:
                    await user.remove_roles(role)

        await interaction.response.send_message(f"{user.mention} has been removed from the staff team.\nReason: {reason}", ephemeral=True)
        await self.send_staff_menu(interaction)

    async def promote_staff_dropdown(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()
        options = [{"label": interaction.guild.get_member(int(user_id)).name, "value": user_id} for user_id in staff_members.keys() if interaction.guild.get_member(int(user_id))]
        view = Dropdown(
            placeholder="Select a staff member to promote",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_promote_staff
        )
        await interaction.response.edit_message(content="Select a staff member to promote:", view=view)

    async def handle_promote_staff(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        user_id = int(values[0])
        user = interaction.guild.get_member(user_id)
        await self.promote_staff_member(interaction, user)

    async def promote_staff_member(self, interaction: discord.Interaction, user: discord.Member):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                return await interaction.response.send_message("This user is not a staff member.", ephemeral=True)

            staff_member = StaffMember(**staff_members[str(user.id)])

        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        current_hierarchy = hierarchies[staff_member.hierarchy]
        current_level = current_hierarchy['levels'][staff_member.level]

        if current_level['next'] is None:
            if 'next_hierarchy' in current_level:
                # Find the first level of the next hierarchy
                next_hierarchy = next(iter(hierarchies.keys()))
                next_level = "1"
            else:
                return await interaction.response.send_message("This staff member is already at the highest level.", ephemeral=True)
        else:
            next_hierarchy = staff_member.hierarchy
            next_level = current_level['next']

        # If the next level is in a different hierarchy, find it
        if next_hierarchy == staff_member.hierarchy and next_level not in current_hierarchy['levels']:
            for hier_name, hier_data in hierarchies.items():
                if next_level in hier_data['levels']:
                    next_hierarchy = hier_name
                    break

        await self.update_staff_member(interaction, user, next_hierarchy, next_level)

    async def demote_staff_dropdown(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()
        options = [{"label": interaction.guild.get_member(int(user_id)).name, "value": user_id} for user_id in staff_members.keys() if interaction.guild.get_member(int(user_id))]
        view = Dropdown(
            placeholder="Select a staff member to demote",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_demote_staff
        )
        await interaction.response.edit_message(content="Select a staff member to demote:", view=view)

    async def handle_demote_staff(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        user_id = int(values[0])
        user = interaction.guild.get_member(user_id)
        await self.demote_staff_member(interaction, user)

    async def demote_staff_member(self, interaction: discord.Interaction, user: discord.Member):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                return await interaction.response.send_message("This user is not a staff member.", ephemeral=True)

            staff_member = StaffMember(**staff_members[str(user.id)])

        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        current_hierarchy = hierarchies[staff_member.hierarchy]
        current_level = current_hierarchy['levels'][staff_member.level]

        prev_level = None
        prev_hierarchy = staff_member.hierarchy

        # Find the previous level in the current hierarchy
        for level, data in current_hierarchy['levels'].items():
            if data['next'] == staff_member.level:
                prev_level = level
                break

        # If not found, check other hierarchies
        if prev_level is None:
            for hier_name, hier_data in hierarchies.items():
                for level, data in hier_data['levels'].items():
                    if data.get('next') == staff_member.level and hier_data.get('next_hierarchy') == staff_member.hierarchy:
                        prev_level = level
                        prev_hierarchy = hier_name
                        break
                if prev_level:
                    break

        if prev_level is None:
            return await interaction.response.send_message("This staff member is already at the lowest level.", ephemeral=True)

        await self.update_staff_member(interaction, user, prev_hierarchy, prev_level)

    async def update_staff_member(self, interaction: discord.Interaction, user: discord.Member, new_hierarchy: str, new_level: str):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                return await interaction.response.send_message("This user is not a staff member.", ephemeral=True)

            staff_member = StaffMember(**staff_members[str(user.id)])
            old_hierarchy = staff_member.hierarchy
            old_level = staff_member.level

            staff_member.hierarchy = new_hierarchy
            staff_member.level = new_level
            staff_members[str(user.id)] = staff_member.__dict__

        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        # Remove old role
        if old_hierarchy in hierarchies and old_level in hierarchies[old_hierarchy]['role_ids']:
            old_role_id = hierarchies[old_hierarchy]['role_ids'][old_level]
            old_role = interaction.guild.get_role(old_role_id)
            if old_role:
                await user.remove_roles(old_role)

        # Add new role
        if new_hierarchy in hierarchies and new_level in hierarchies[new_hierarchy]['role_ids']:
            new_role_id = hierarchies[new_hierarchy]['role_ids'][new_level]
            new_role = interaction.guild.get_role(new_role_id)
            if new_role:
                await user.add_roles(new_role)

        await interaction.response.send_message(f"{user.mention}'s staff status has been updated to {new_level} in the {new_hierarchy} hierarchy.", ephemeral=True)
        await self.send_staff_menu(interaction)

    async def staff_info_dropdown(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()
        options = [{"label": interaction.guild.get_member(int(user_id)).name, "value": user_id} for user_id in staff_members.keys() if interaction.guild.get_member(int(user_id))]
        view = Dropdown(
            placeholder="Select a staff member",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_staff_info
        )
        await interaction.response.edit_message(content="Select a staff member to view info:", view=view)

    async def handle_staff_info(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        user_id = int(values[0])
        user = interaction.guild.get_member(user_id)
        await self.show_staff_info(interaction, user)

    async def show_staff_info(self, interaction: discord.Interaction, user: discord.Member):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                return await interaction.response.send_message("This user is not a staff member.", ephemeral=True)

            staff_member = StaffMember(**staff_members[str(user.id)])

        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        hierarchy = hierarchies.get(staff_member.hierarchy, {})
        level_name = hierarchy.get('levels', {}).get(staff_member.level, {}).get('name', "Unknown")

        embed = discord.Embed(title=f"Staff Info - {user.name}", color=discord.Color.blue())
        embed.add_field(name="Hierarchy", value=staff_member.hierarchy, inline=False)
        embed.add_field(name="Level", value=f"{staff_member.level} ({level_name})", inline=False)
        embed.add_field(name="Join Date", value=staff_member.join_date.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Performance Score", value=staff_member.performance_score, inline=False)
        embed.add_field(name="Warnings", value=staff_member.warnings, inline=False)

        if staff_member.notes:
            embed.add_field(name="Notes", value="\n".join(staff_member.notes), inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def list_staff_dropdown(self, interaction: discord.Interaction):
        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        options = [{"label": "All Staff", "value": "all"}] + [{"label": name, "value": name} for name in hierarchies.keys()]
        view = Dropdown(
            placeholder="Select a hierarchy or all staff",
            options=options,
            min_values=1,
            max_values=1,
            function=self.handle_list_staff
        )
        await interaction.response.edit_message(content="Select a hierarchy to list staff or choose 'All Staff':", view=view)

    async def handle_list_staff(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        hierarchy = values[0] if values[0] != "all" else None
        await self.list_staff_members(interaction, hierarchy)

    async def list_staff_members(self, interaction: discord.Interaction, hierarchy: Optional[str] = None):
        staff_members = await self.config.guild(interaction.guild).staff_members()
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        if hierarchy and hierarchy not in hierarchies:
            return await interaction.response.send_message("Invalid hierarchy specified.", ephemeral=True)

        embed = discord.Embed(title="Staff Members", color=discord.Color.blue())

        for member_id, member_data in staff_members.items():
            member = StaffMember(**member_data)
            if hierarchy and member.hierarchy != hierarchy:
                continue

            user = interaction.guild.get_member(member.user_id)
            if user:
                level_name = hierarchies.get(member.hierarchy, {}).get('levels', {}).get(member.level, {}).get('name', "Unknown")
                embed.add_field(name=user.name, value=f"Hierarchy: {member.hierarchy}\nLevel: {member.level} ({level_name})", inline=False)

        if not embed.fields:
            await interaction.response.send_message("No staff members found.", ephemeral=True)
        else:
            await interaction.response.send_message(embed=embed, ephemeral=True)

    async def send_stats(self, interaction: discord.Interaction):
        staff_members = await self.config.guild(interaction.guild).staff_members()
        hierarchies = await self.config.guild(interaction.guild).hierarchies()

        embed = discord.Embed(title="Staff Statistics", color=discord.Color.blue())
        embed.add_field(name="Total Staff Members", value=str(len(staff_members)), inline=False)

        for hierarchy in hierarchies:
            staff_in_hierarchy = [member for member in staff_members.values() if member['hierarchy'] == hierarchy]
            embed.add_field(name=f"{hierarchy} Staff", value=str(len(staff_in_hierarchy)), inline=True)

        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
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
                        await self.add_staff_member(None, after, hierarchy, level)
                    else:
                        await self.update_staff_member(None, after, hierarchy, level)
                    return

    @commands.is_owner()
    @commands.command()
    async def getlogs(self, ctx: commands.Context, level: str = "all"):
        """Get logs for the Staffer cog."""
        if level == "stats":
            message = "---------- Logs Stats ----------"
            for _level, logs in self.logs.items():
                message += f"\n{_level}: {len(logs)}"
            await ctx.send(box(message, lang="py"))
            return
        if level != "all" and (self.logs.get(level, None) is None or self.logs.get(level, None) == []):
            await ctx.send("No logs found for this level.")
            return
        if level == "all":
            data = []
            for _level in self.logs:
                data.extend(iter(self.logs[_level]))
        else:
            data = list(self.logs.get(level))
        result = []
        for log in data:
            name = self.logs.name
            time = log["time"]
            asctime = time.strftime("%Y-%m-%d %H:%M:%S")
            levelname = log["levelname"]
            message = log["message"]
            exc_info = log["exc_info"]
            if exc_info is None:
                exc_info = ""
            else:
                exc_info = "".join(traceback.format_exception(type(exc_info), exc_info, exc_info.__traceback__))
            result.append(box(CogsUtils.replace_var_paths(f"[{asctime}] {levelname} [{name}] {message}\n{exc_info}")[:2000-10], lang="py"))
        for page in pagify("\n".join(result), page_length=1990):
            await ctx.send(page)

    @commands.is_owner()
    @commands.command()
    async def getdebugloopsstatus(self, ctx: commands.Context):
        """Get debug loops status for the Staffer cog."""
        embeds = [loop.get_debug_embed() for loop in self.loops]
        for embed in embeds:
            await ctx.send(embed=embed)
=======
from Star_Utils import Cog
import discord
from redbot.core import Config, checks, commands


class StaffManager(Cog):
    """Cog for managing staff members in a Discord server."""

    def __init__(self, bot):
        self.bot = bot
        self.staff_updates_channel = None
        self.blacklist_channel = None
        self.loa_requests_channel = None
        self.loa_role = None
        self.resignation_requests_channel = None
        self.config = Config.get_conf(self, identifier='staffmanager',
            force_registration=True)
        self.config.register_global(staff_updates_channel=None,
            blacklist_channel=None, loa_requests_channel=None, loa_role=
            None, resignation_requests_channel=None, loa_requests={},
            resignation_requests={})

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setupdates(self, ctx, channel: discord.TextChannel):
        """Set the channel for staff update messages."""
        self.staff_updates_channel = channel
        await self.config.staff_updates_channel.set(channel.id)
        await ctx.send(f'Staff updates channel set to {channel.mention}')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setblacklist(self, ctx, channel: discord.TextChannel):
        """Set the channel for blacklist messages."""
        await self.config.blacklist_channel.set(channel.id)
        await ctx.send(f'Blacklist channel set to {channel.mention}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handle command errors."""
        if isinstance(error, commands.CheckFailure):
            await self.send_channel_not_set_message(ctx, ctx.command.name)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def fire(self, ctx, member: discord.Member, role: discord.Role):
        """Fire a staff member."""
        await member.remove_roles(role)
        embed = discord.Embed(title='Staff Fired', color=discord.Color.red())
        embed.add_field(name='Username', value=member.name, inline=False)
        embed.add_field(name='User ID', value=member.id, inline=False)
        embed.add_field(name='Position', value=role.name, inline=False)
        embed.add_field(name='Issuer', value=ctx.author.name, inline=False)
        await self.staff_updates_channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def hire(self, ctx, member: discord.Member, role: discord.Role):
        """Hire a new staff member."""
        await member.add_roles(role)
        embed = discord.Embed(title='Staff Hired', color=discord.Color.green())
        embed.add_field(name='Username', value=member.name, inline=False)
        embed.add_field(name='User ID', value=member.id, inline=False)
        embed.add_field(name='Position', value=role.name, inline=False)
        embed.add_field(name='Issuer', value=ctx.author.name, inline=False)
        await self.staff_updates_channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def demote(self, ctx, member: discord.Member, old_role: discord.
        Role, new_role: discord.Role):
        """Demote a staff member."""
        await member.remove_roles(old_role)
        await member.add_roles(new_role)
        embed = discord.Embed(title='Staff Demoted', color=discord.Color.
            orange())
        embed.add_field(name='Username', value=member.name, inline=False)
        embed.add_field(name='User ID', value=member.id, inline=False)
        embed.add_field(name='Position', value=new_role.name, inline=False)
        embed.add_field(name='Old Position', value=old_role.name, inline=False)
        embed.add_field(name='Issuer', value=ctx.author.name, inline=False)
        await self.staff_updates_channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def promote(self, ctx, member: discord.Member, old_role: discord.
        Role, new_role: discord.Role):
        """Promote a staff member."""
        await member.remove_roles(old_role)
        await member.add_roles(new_role)
        embed = discord.Embed(title='Staff Promoted', color=discord.Color.
            blue())
        embed.add_field(name='Username', value=member.name, inline=False)
        embed.add_field(name='User ID', value=member.id, inline=False)
        embed.add_field(name='Position', value=new_role.name, inline=False)
        embed.add_field(name='Old Position', value=old_role.name, inline=False)
        embed.add_field(name='Issuer', value=ctx.author.name, inline=False)
        await self.staff_updates_channel.send(embed=embed)

    @commands.command(name='staffblacklist')
    @commands.has_permissions(ban_members=True)
    async def staffblacklist(self, ctx, member: discord.Member, reason: str,
        proof: str):
        """Blacklist a staff member."""
        try:
            await member.send(
                f'You have been blacklisted from {ctx.guild.name} for: {reason}. If you wish to appeal, please contact {ctx.guild.owner.mention} or the Support team.'
                )
        except discord.Forbidden:
            await ctx.send(
                f'Failed to send a DM to {member.name}. They will still be blacklisted.'
                )
        await member.ban(reason=reason)
        embed = discord.Embed(title='Staff Blacklisted', color=discord.
            Color.dark_red())
        embed.add_field(name='Username', value=member.name, inline=False)
        embed.add_field(name='User ID', value=member.id, inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.add_field(name='Proof', value=proof, inline=False)
        channel = await self.config.blacklist_channel()
        if channel:
            await channel.send(embed=embed)
        else:
            await self.send_channel_reminder(ctx, 'staffblacklist')

    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def loa(self, ctx):
        """Group command for managing leave of absence requests."""
        if ctx.invoked_subcommand is None:
            await ctx.send(
                'Invalid subcommand passed. Use `loa request`, `loa approve`, `loa deny`, `loa channel`, or `loa role`.'
                )

    @loa.command()
    @commands.has_permissions(manage_channels=True)
    async def channel(self, ctx, channel: discord.TextChannel):
        """Set the channel for LOA request messages."""
        self.loa_requests_channel = channel
        await self.config.loa_requests_channel.set(channel.id)
        await ctx.send(f'LOA requests channel set to {channel.mention}')

    @loa.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, role: discord.Role):
        """Set the role to be assigned during LOA."""
        self.loa_role = role
        await self.config.loa_role.set(role.id)
        await ctx.send(f'LOA role set to {role.name}')

    @loa.command()
    async def request(self, ctx, duration: str, reason: str):
        """Request a leave of absence."""
        loa_requests = await self.config.loa_requests()
        user_id = ctx.author.id
        loa_requests[user_id] = {'user': ctx.author.id, 'duration':
            duration, 'reason': reason, 'approved_by': None}
        await self.config.loa_requests.set(loa_requests)
        loa_requests_channel_id = await self.config.loa_requests_channel()
        loa_requests_channel = self.bot.get_channel(loa_requests_channel_id)
        if loa_requests_channel:
            embed = discord.Embed(title='LOA Request', color=discord.Color.
                yellow())
            embed.add_field(name='User', value=ctx.author.name, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='Duration', value=duration, inline=False)
            embed.add_field(name='User ID', value=ctx.author.id, inline=False)
            embed.set_footer(text=
                'Do `loa approve <user_id>` or `loa deny <user_id>`')
            await loa_requests_channel.send(embed=embed)
        await ctx.send(
            f'Leave of Absence request submitted for {duration} due to {reason}.'
            )

    @loa.command()
    async def approve(self, ctx, user_id: int):
        """Approve a leave of absence request."""
        loa_requests = await self.config.loa_requests()
        if user_id in loa_requests and loa_requests[user_id]['approved_by'
            ] is None:
            loa_requests[user_id]['approved_by'] = ctx.author.id
            await self.config.loa_requests.set(loa_requests)
            user = self.bot.get_user(loa_requests[user_id]['user'])
            loa_role_id = await self.config.loa_role()
            loa_role = ctx.guild.get_role(loa_role_id)
            if loa_role:
                await user.add_roles(loa_role)
            embed = discord.Embed(title='Leave of Absence', color=discord.
                Color.green())
            embed.add_field(name='User', value=user.name, inline=False)
            embed.add_field(name='Duration', value=loa_requests[user_id][
                'duration'], inline=False)
            embed.add_field(name='Reason', value=loa_requests[user_id][
                'reason'], inline=False)
            embed.add_field(name='Approved by', value=ctx.author.name,
                inline=False)
            await self.staff_updates_channel.send(embed=embed)
            await ctx.send(
                f'Leave of Absence request for {user.name} approved.')
        else:
            await ctx.send(
                f'Leave of Absence request for user ID {user_id} not found or already approved.'
                )

    @loa.command()
    async def deny(self, ctx, user_id: int):
        """Deny a leave of absence request."""
        loa_requests = await self.config.loa_requests()
        if user_id in loa_requests:
            del loa_requests[user_id]
            await self.config.loa_requests.set(loa_requests)
            await ctx.send(
                f'Leave of Absence request for user ID {user_id} denied and removed.'
                )
        else:
            await ctx.send(
                f'Leave of Absence request for user ID {user_id} not found.')

    @loa.command()
    async def end(self, ctx, user_id: int):
        """End a leave of absence."""
        loa_requests = await self.config.loa_requests()
        if user_id in loa_requests and loa_requests[user_id]['approved_by'
            ] is not None:
            user = self.bot.get_user(loa_requests[user_id]['user'])
            loa_role_id = await self.config.loa_role()
            loa_role = ctx.guild.get_role(loa_role_id)
            if loa_role:
                await user.remove_roles(loa_role)
            del loa_requests[user_id]
            await self.config.loa_requests.set(loa_requests)
            embed = discord.Embed(title='Leave of Absence Ended', color=
                discord.Color.red())
            embed.add_field(name='User', value=user.name, inline=False)
            embed.add_field(name='User ID', value=user.id, inline=False)
            await self.staff_updates_channel.send(embed=embed)
            await ctx.send(f'Leave of Absence for {user.name} has ended.')
        else:
            await ctx.send(
                f'Leave of Absence for user ID {user_id} not found or not approved.'
                )

    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def resign(self, ctx):
        """Group command for managing resignation requests."""
        if ctx.invoked_subcommand is None:
            await ctx.send(
                'Invalid subcommand passed. Use `resign request`, `resign accept`, `resign deny`, or `resign channel`.'
                )

    @resign.command()
    async def request(self, ctx, reason: str):
        """Request a resignation."""
        resignation_requests = await self.config.resignation_requests()
        user_id = ctx.author.id
        resignation_requests[user_id] = {'user': ctx.author.id, 'reason':
            reason, 'approved_by': None}
        await self.config.resignation_requests.set(resignation_requests)
        resignation_requests_channel_id = (await self.config.
            resignation_requests_channel())
        resignation_requests_channel = self.bot.get_channel(
            resignation_requests_channel_id)
        if resignation_requests_channel:
            embed = discord.Embed(title='Resignation Request', color=
                discord.Color.yellow())
            embed.add_field(name='User', value=ctx.author.name, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='User ID', value=ctx.author.id, inline=False)
            embed.set_footer(text=
                'Do `resign accept <user_id>` or `resign deny <user_id>`')
            await resignation_requests_channel.send(embed=embed)
        await ctx.send(f'Resignation request submitted due to {reason}.')

    @resign.command()
    async def accept(self, ctx, user_id: int):
        """Accept a resignation request."""
        resignation_requests = await self.config.resignation_requests()
        if user_id in resignation_requests and resignation_requests[user_id][
            'approved_by'] is None:
            resignation_requests[user_id]['approved_by'] = ctx.author.id
            await self.config.resignation_requests.set(resignation_requests)
            user = self.bot.get_user(resignation_requests[user_id]['user'])
            embed = discord.Embed(title='Staff Member Resigned', color=
                discord.Color.red())
            embed.add_field(name='Former Staff', value=user.name, inline=False)
            embed.add_field(name='Reason', value=resignation_requests[
                user_id]['reason'], inline=False)
            embed.add_field(name='Approved by', value=ctx.author.name,
                inline=False)
            staff_updates_channel_id = await self.config.staff_updates_channel(
                )
            staff_updates_channel = self.bot.get_channel(
                staff_updates_channel_id)
            if staff_updates_channel:
                await staff_updates_channel.send(embed=embed)
            await ctx.send(f'Resignation request for {user.name} accepted.')
        else:
            await ctx.send(
                f'Resignation request for user ID {user_id} not found or already accepted.'
                )

    @resign.command()
    async def deny(self, ctx, user_id: int):
        """Deny a resignation request."""
        resignation_requests = await self.config.resignation_requests()
        if user_id in resignation_requests:
            del resignation_requests[user_id]
            await self.config.resignation_requests.set(resignation_requests)
            await ctx.send(
                f'Resignation request for user ID {user_id} denied and removed.'
                )
        else:
            await ctx.send(
                f'Resignation request for user ID {user_id} not found.')

    @resign.command()
    @commands.has_permissions(manage_channels=True)
    async def channel(self, ctx, channel: discord.TextChannel):
        """Set the channel for resignation request messages."""
        self.resignation_requests_channel = channel
        await self.config.resignation_requests_channel.set(channel.id)
        await ctx.send(f'Resignation requests channel set to {channel.mention}'
            )


def setup(bot):
    bot.add_cog(StaffManager(bot))
>>>>>>> 9e308722 (Revamped and Fixed)
