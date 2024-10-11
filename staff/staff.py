import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box, pagify
from typing import Dict, List, Optional, Union
import asyncio
import datetime
from Star_Utils import Cog, Buttons, Dropdown, Modal, Loop, CogsUtils

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

        self.init_logger()
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
        self.logger.info("Running performance review loop")
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
                # Implement your performance review logic here
                # For example, you could update the performance score based on activity
                # or other metrics you define
                self.logger.debug(f"Reviewing performance for {member.name}")

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
        modal = Modal(
            title="Add New Hierarchy",
            inputs=[
                {"label": "Hierarchy Name", "style": discord.TextStyle.short, "custom_id": "name", "required": True},
            ],
            function=self.handle_add_hierarchy_modal
        )

        await interaction.response.send_modal(modal)

    async def handle_add_hierarchy_modal(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput]):
        name = inputs[0].value
        await self.add_hierarchy_levels(interaction, name)

    async def add_hierarchy_levels(self, interaction: discord.Interaction, hierarchy_name: str):
        roles = interaction.guild.roles
        options = [{"label": role.name, "value": str(role.id)} for role in roles if role.name != "@everyone"]

        view = Dropdown(
            placeholder="Select roles for levels",
            options=options,
            min_values=1,
            max_values=len(options),
            function=lambda v, i, vals: self.handle_add_hierarchy_levels(v, i, vals, hierarchy_name)
        )
        await interaction.response.send_message("Select roles for each level in the hierarchy:", view=view)

    async def handle_add_hierarchy_levels(self, view: Dropdown, interaction: discord.Interaction, values: List[str], hierarchy_name: str):
        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name in hierarchies:
                return await interaction.response.send_message("A hierarchy with this name already exists.", ephemeral=True)

            levels = {str(i+1): interaction.guild.get_role(int(role_id)).name for i, role_id in enumerate(values)}
            role_ids = {str(i+1): int(role_id) for i, role_id in enumerate(values)}
            hierarchies[hierarchy_name] = {"levels": levels, "role_ids": role_ids}

        await interaction.response.send_message(f"Hierarchy '{hierarchy_name}' created with levels: {', '.join(levels.values())}", ephemeral=True)
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
            {"label": "Add Level", "value": "add_level"},
            {"label": "Remove Level", "value": "remove_level"},
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

        if action == "add_level":
            await self.add_level_modal(interaction, hierarchy_name)
        elif action == "remove_level":
            await self.remove_level_dropdown(interaction, hierarchy_name)
        elif action == "set_role":
            await self.set_role_dropdown(interaction, hierarchy_name)
        elif action == "back":
            await self.send_hierarchy_menu(interaction)

    async def add_level_modal(self, interaction: discord.Interaction, hierarchy_name: str):
        modal = Modal(
            title=f"Add Level to {hierarchy_name}",
            inputs=[
                {"label": "Level Name", "style": discord.TextStyle.short, "custom_id": "level_name", "required": True}
            ],
            function=lambda m, i, inputs: self.handle_add_level(m, i, inputs, hierarchy_name)
        )

        await interaction.response.send_modal(modal)

    async def handle_add_level(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput], hierarchy_name: str):
        level_name = inputs[0].value

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name not in hierarchies:
                return await interaction.response.send_message("Hierarchy not found.", ephemeral=True)

            new_level = str(len(hierarchies[hierarchy_name]['levels']) + 1)
            hierarchies[hierarchy_name]['levels'][new_level] = level_name

        await interaction.response.send_message(f"Added level {new_level}: {level_name} to {hierarchy_name}", ephemeral=True)
        await self.edit_hierarchy_menu(interaction, hierarchy_name)

    async def remove_level_dropdown(self, interaction: discord.Interaction, hierarchy_name: str):
        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name not in hierarchies:
                return await interaction.response.send_message("Hierarchy not found.", ephemeral=True)

            levels = hierarchies[hierarchy_name]['levels']

            if not levels:
                return await interaction.response.send_message("This hierarchy has no levels to remove.", ephemeral=True)

            options = [{"label": f"Level {level}: {name}", "value": level} for level, name in levels.items()]
            view = Dropdown(
                placeholder="Select a level to remove",
                options=options,
                min_values=1,
                max_values=1,
                function=lambda v, i, vals: self.handle_remove_level(v, i, vals, hierarchy_name)
            )
            await interaction.response.edit_message(content="Select a level to remove:", view=view)

    async def handle_remove_level(self, view: Dropdown, interaction: discord.Interaction, values: List[str], hierarchy_name: str):
        level_to_remove = values[0]

        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            del hierarchies[hierarchy_name]['levels'][level_to_remove]
            if level_to_remove in hierarchies[hierarchy_name]['role_ids']:
                del hierarchies[hierarchy_name]['role_ids'][level_to_remove]

        await interaction.response.send_message(f"Removed level {level_to_remove} from {hierarchy_name}", ephemeral=True)
        await self.edit_hierarchy_menu(interaction, hierarchy_name)

    async def set_role_dropdown(self, interaction: discord.Interaction, hierarchy_name: str):
        async with self.config.guild(interaction.guild).hierarchies() as hierarchies:
            if hierarchy_name not in hierarchies:
                return await interaction.response.send_message("Hierarchy not found.", ephemeral=True)

            levels = hierarchies[hierarchy_name]['levels']

            if not levels:
                return await interaction.response.send_message("This hierarchy has no levels to set roles for.", ephemeral=True)

            options = [{"label": f"Level {level}: {name}", "value": level} for level, name in levels.items()]
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
        embed = discord.Embed(title="Staff Hierarchies", color=discord.Color.blue())
        for name, data in hierarchies.items():
            levels = "\n".join([f"{level}: {role}" for level, role in data['levels'].items()])
            embed.add_field(name=name, value=levels, inline=False)
        await interaction.response.edit_message(embed=embed)

    async def send_staff_menu(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Manage Staff", description="Select an action to manage staff members.", color=discord.Color.gold())

        options = [
            {"label": "Add Staff", "value": "add_staff"},
            {"label": "Remove Staff", "value": "remove_staff"},
            {"label": "Promote Staff", "value": "promote_staff"},
            {"label": "Demote Staff", "value": "demote_staff"},
            {"label": "View Staff Info", "value": "staff_info"},
            {"label": "List Staff", "value": "list_staff"},
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
        options = [{"label": f"Level {level}: {name}", "value": level} for level, name in levels.items()]
        view = Dropdown(
            placeholder="Select a level",
            options=options,
            min_values=1,
            max_values=1,
            function=lambda v, i, vals: self.handle_add_staff_level(v, i, vals, user, hierarchy)
        )
        await interaction.response.edit_message(content=f"Select a level for {user.name} in {hierarchy}:", view=view)

    async def handle_add_staff_level(self, view: Dropdown, interaction: discord.Interaction, values: List[str], user: discord.Member, hierarchy: str):
        level = int(values[0])
        await self.add_staff_member(interaction, user, hierarchy, level)

    async def add_staff_member(self, interaction: discord.Interaction, user: discord.Member, hierarchy: str, level: int):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) in staff_members:
                return await interaction.response.send_message("This user is already a staff member.", ephemeral=True)

            staff_member = StaffMember(user.id, hierarchy, level)
            staff_members[str(user.id)] = staff_member.__dict__

        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        if hierarchy in hierarchies and str(level) in hierarchies[hierarchy]['role_ids']:
            role_id = hierarchies[hierarchy]['role_ids'][str(level)]
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
        if staff_member.hierarchy not in hierarchies:
            return await interaction.response.send_message("Invalid hierarchy for this staff member.", ephemeral=True)

        current_hierarchy = hierarchies[staff_member.hierarchy]
        next_level = str(staff_member.level + 1)

        if next_level not in current_hierarchy['levels']:
            # Move to the next hierarchy
            hierarchy_keys = list(hierarchies.keys())
            current_index = hierarchy_keys.index(staff_member.hierarchy)
            if current_index + 1 < len(hierarchy_keys):
                next_hierarchy = hierarchy_keys[current_index + 1]
                next_level = "1"
            else:
                return await interaction.response.send_message("This staff member is already at the highest level in the highest hierarchy.", ephemeral=True)
        else:
            next_hierarchy = staff_member.hierarchy

        await self.update_staff_member(interaction, user, next_hierarchy, int(next_level))

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
        if staff_member.hierarchy not in hierarchies:
            return await interaction.response.send_message("Invalid hierarchy for this staff member.", ephemeral=True)

        current_hierarchy = hierarchies[staff_member.hierarchy]
        prev_level = str(staff_member.level - 1)

        if prev_level not in current_hierarchy['levels']:
            # Move to the previous hierarchy
            hierarchy_keys = list(hierarchies.keys())
            current_index = hierarchy_keys.index(staff_member.hierarchy)
            if current_index > 0:
                prev_hierarchy = hierarchy_keys[current_index - 1]
                prev_level = str(len(hierarchies[prev_hierarchy]['levels']))
            else:
                return await interaction.response.send_message("This staff member is already at the lowest level in the lowest hierarchy.", ephemeral=True)
        else:
            prev_hierarchy = staff_member.hierarchy

        await self.update_staff_member(interaction, user, prev_hierarchy, int(prev_level))

    async def update_staff_member(self, interaction: discord.Interaction, user: discord.Member, hierarchy: str, level: int):
        async with self.config.guild(interaction.guild).staff_members() as staff_members:
            if str(user.id) not in staff_members:
                return await interaction.response.send_message("This user is not a staff member.", ephemeral=True)

            staff_member = StaffMember(**staff_members[str(user.id)])
            old_hierarchy = staff_member.hierarchy
            old_level = staff_member.level

            staff_member.hierarchy = hierarchy
            staff_member.level = level
            staff_members[str(user.id)] = staff_member.__dict__

        hierarchies = await self.config.guild(interaction.guild).hierarchies()
        if old_hierarchy in hierarchies and str(old_level) in hierarchies[old_hierarchy]['role_ids']:
            old_role_id = hierarchies[old_hierarchy]['role_ids'][str(old_level)]
            old_role = interaction.guild.get_role(old_role_id)
            if old_role:
                await user.remove_roles(old_role)

        if hierarchy in hierarchies and str(level) in hierarchies[hierarchy]['role_ids']:
            new_role_id = hierarchies[hierarchy]['role_ids'][str(level)]
            new_role = interaction.guild.get_role(new_role_id)
            if new_role:
                await user.add_roles(new_role)

        await interaction.response.send_message(f"{user.mention}'s staff status has been updated to level {level} in the {hierarchy} hierarchy.", ephemeral=True)
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
        level_name = hierarchy.get('levels', {}).get(str(staff_member.level), "Unknown")

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
                level_name = hierarchies.get(member.hierarchy, {}).get('levels', {}).get(str(member.level), "Unknown")
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

    async def send_settings_menu(self, interaction: discord.Interaction):
        settings = await self.config.guild(interaction.guild).settings()

        embed = discord.Embed(title="Staffer Settings", description="Current settings:", color=discord.Color.purple())
        embed.add_field(name="Auto Role Update", value="Enabled" if settings['auto_role_update'] else "Disabled", inline=False)
        embed.add_field(name="Performance Review Interval", value=f"{settings['performance_review_interval']} days", inline=False)
        embed.add_field(name="Warning Threshold", value=str(settings['warning_threshold']), inline=False)

        options = [
            {"label": "Toggle Auto Role Update", "value": "toggle_auto_role"},
            {"label": "Set Review Interval", "value": "set_review_interval"},
            {"label": "Set Warning Threshold", "value": "set_warning_threshold"},
            {"label": "Back to Main Menu", "value": "back"}
        ]

        view = Dropdown(
            placeholder="Select a setting to change",
            options=options,
            function=self.handle_settings_menu,
            infinity=True
        )
        await interaction.response.edit_message(embed=embed, view=view)

    async def handle_settings_menu(self, view: Dropdown, interaction: discord.Interaction, values: List[str]):
        action = values[0]

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
        modal = Modal(
            title="Set Review Interval",
            inputs=[
                {"label": "Interval (in days)", "style": discord.TextStyle.short, "custom_id": "interval", "required": True}
            ],
            function=self.handle_set_review_interval
        )

        await interaction.response.send_modal(modal)

    async def handle_set_review_interval(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput]):
        interval = int(inputs[0].value)
        async with self.config.guild(interaction.guild).settings() as settings:
            settings['performance_review_interval'] = interval

        await interaction.response.send_message(f"Performance review interval set to {interval} days.", ephemeral=True)
        await self.send_settings_menu(interaction)

    async def set_warning_threshold_modal(self, interaction: discord.Interaction):
        modal = Modal(
            title="Set Warning Threshold",
            inputs=[
                {"label": "Threshold", "style": discord.TextStyle.short, "custom_id": "threshold", "required": True}
            ],
            function=self.handle_set_warning_threshold
        )

        await interaction.response.send_modal(modal)

    async def handle_set_warning_threshold(self, modal: Modal, interaction: discord.Interaction, inputs: List[discord.ui.TextInput]):
        threshold = int(inputs[0].value)
        async with self.config.guild(interaction.guild).settings() as settings:
            settings['warning_threshold'] = threshold

        await interaction.response.send_message(f"Warning threshold set to {threshold}.", ephemeral=True)
        await self.send_settings_menu(interaction)

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
                        await self.add_staff_member(None, after, hierarchy, int(level))
                    else:
                        await self.update_staff_member(None, after, hierarchy, int(level))
                    return
