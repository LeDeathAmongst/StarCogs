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

        os.makedirs(backup_path, exist_ok=True)

        cog_list = [cog.strip() for cog in cogs.split(',')] if cogs else None

        updated_files = 0
        for root, dirs, files in os.walk(datapath):
            for file in files:
                if file.endswith('.py'):
                    cog_name = file[:-3]
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
                    cog_name = file[:-3]
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
            shutil.rmtree(backup_path)
            await ctx.send("Backup directory has been removed.")

    async def update_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.readlines()

        updated = False
        new_content = []
        in_class = False
        skip_block = False
        in_import_block = False

        for i, line in enumerate(content):
            # Check if we're in an import block
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                in_import_block = True
                new_content.append(line)
                continue
            elif in_import_block and not (line.strip().startswith('import ') or line.strip().startswith('from ')):
                in_import_block = False

            # Skip replacements if we're in an import block
            if not in_import_block:
                # Replace 'AAA3A_utils' with 'Star_Utils'
                if 'AAA3A_utils' in line:
                    line = line.replace('AAA3A_utils', 'Star_Utils')
                    updated = True

                # Check for class definition
                if 'class' in line and ':' in line:
                    in_class = True
                    if 'commands.Cog' in line:
                        line = line.replace('commands.Cog', 'Cog')
                        updated = True

                # Handle Cog.listener
                if 'Cog.listener' in line:
                    if in_class:
                        line = line.replace('Cog.listener', 'commands.Cog.listener')
                    else:
                        line = line.replace('Cog.listener', 'commands.Cog.listener')
                    updated = True

                # Replace 'Cog' with 'commands.Cog' outside of class definition
                if not in_class and re.search(r'\bCog\b', line):
                    line = re.sub(r'\bCog\b', 'commands.Cog', line)
                    updated = True

            # Remove lines with __author__, __authors__, __version__, __contributors__, or similar
            if re.match(r'\s*__(?:author|authors|version|contributors|[a-z_]+)__\s*=', line):
                updated = True
                continue

            # Check for format_help_for_context method
            if 'def format_help_for_context' in line:
                skip_block = True
                updated = True
                continue

            # If we're skipping a block and find a line that's not indented, stop skipping
            if skip_block and not line.startswith((' ', '\t')):
                skip_block = False

            # Add the line if we're not skipping
            if not skip_block:
                new_content.append(line)

        # Add import statement if 'Cog' was found in class definition
        if in_class:
            for i, line in enumerate(new_content):
                if line.strip().startswith('import ') or line.strip().startswith('from '):
                    continue
                else:
                    new_content.insert(i, 'from Star_Utils import Cog\n')
                    updated = True
                    break

        if updated:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(new_content)

        return updated
