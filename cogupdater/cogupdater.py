import os
import re
import shutil
from redbot.core import commands
from redbot.core import Config

class CogUpdater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {"datapath": "", "backup_path": ""}
        self.config.register_global(**default_global)

    @commands.command()
    @commands.is_owner()
    async def set_datapath(self, ctx, path: str):
        """Set the path to the cog data directory."""
        await self.config.datapath.set(path)
        backup_path = os.path.join(path, "cog_backups")
        await self.config.backup_path.set(backup_path)
        await ctx.send(f"Data path set to: {path}\nBackup path set to: {backup_path}")

    @commands.command()
    @commands.is_owner()
    async def update_cogs(self, ctx, *, cogs: str = None):
        """Update specified cogs or all cogs if none specified."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath:
            await ctx.send("Please set the data path first using `set_datapath`.")
            return

        # Create backup directory
        os.makedirs(backup_path, exist_ok=True)

        cog_list = [cog.strip() for cog in cogs.split(',')] if cogs else None

        updated_files = 0
        for root, dirs, files in os.walk(datapath):
            for file in files:
                if file.endswith('.py'):
                    cog_name = file[:-3]  # Remove .py extension
                    if cog_list and cog_name not in cog_list:
                        continue

                    filepath = os.path.join(root, file)
                    relative_path = os.path.relpath(filepath, datapath)
                    backup_file = os.path.join(backup_path, relative_path)
                    os.makedirs(os.path.dirname(backup_file), exist_ok=True)
                    shutil.copy2(filepath, backup_file)
                    updated = await self.update_file(filepath)
                    if updated:
                        updated_files += 1

        if cog_list:
            await ctx.send(f"Updated {updated_files} files for cogs: {', '.join(cog_list)}. Backups created in {backup_path}")
        else:
            await ctx.send(f"Updated {updated_files} files across all cogs. Backups created in {backup_path}")

    @commands.command()
    @commands.is_owner()
    async def undo_updates(self, ctx, *, cogs: str = None):
        """Undo the updates made to specified cogs or all cogs if none specified."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath or not backup_path:
            await ctx.send("Please set the data path first using `set_datapath`.")
            return

        cog_list = [cog.strip() for cog in cogs.split(',')] if cogs else None

        restored_files = 0
        for root, dirs, files in os.walk(backup_path):
            for file in files:
                if file.endswith('.py'):
                    cog_name = file[:-3]  # Remove .py extension
                    if cog_list and cog_name not in cog_list:
                        continue

                    backup_file = os.path.join(root, file)
                    relative_path = os.path.relpath(backup_file, backup_path)
                    original_file = os.path.join(datapath, relative_path)
                    shutil.copy2(backup_file, original_file)
                    restored_files += 1

        if cog_list:
            await ctx.send(f"Restored {restored_files} files for cogs: {', '.join(cog_list)}.")
        else:
            await ctx.send(f"Restored {restored_files} files across all cogs.")
            # Remove the entire backup directory only if restoring all cogs
            shutil.rmtree(backup_path)
            await ctx.send("Backup directory has been removed.")

    async def update_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.readlines()

        updated = False
        new_content = []
        cog_in_class = False

        for i, line in enumerate(content):
            # Replace 'AAA3A_utils' with 'Star_Utils'
            if 'AAA3A_utils' in line:
                line = line.replace('AAA3A_utils', 'Star_Utils')
                updated = True

            # Check for 'commands.Cog' in class definition
            if 'class' in line and 'commands.Cog' in line:
                line = line.replace('commands.Cog', 'Cog')
                cog_in_class = True
                updated = True

            # Remove __author__, __version__, and __contributors__
            if any(attr in line for attr in ['__author__', '__version__', '__contributors__']):
                updated = True
                continue

            new_content.append(line)

        # Add import statement if 'Cog' was found in class definition
        if cog_in_class:
            new_content.insert(2, 'from Star_Utils import Cog\n')
            updated = True

        # Remove the format_help_for_context method
        content_str = ''.join(new_content)
        content_str = re.sub(
            r'def format_help_for_context\(self, ctx\):.*?return info\n',
            '',
            content_str,
            flags=re.DOTALL
        )

        if updated:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content_str)

        return updated
