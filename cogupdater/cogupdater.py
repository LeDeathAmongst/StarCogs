import os
import re
import shutil
from redbot.core import commands, Config
from Star_Utils import Cog

class CogUpdater(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {"datapath": "", "backup_path": ""}
        self.config.register_global(**default_global)

    @commands.command()
    @commands.is_owner()
    async def setpath(self, ctx, path: str):
        """Set the path to the cog data directory."""
        await self.config.datapath.set(path)
        backup_path = os.path.join(path, "cog_backups")
        await self.config.backup_path.set(backup_path)
        await ctx.send(f"Data path set to: {path}\nBackup path set to: {backup_path}")

    @commands.command()
    @commands.is_owner()
    async def updatecogs(self, ctx, *, cogs: str = None):
        """Update specified cogs or all cogs if none specified."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath:
            await ctx.send("Please set the data path first using `setpath`.")
            return

        os.makedirs(backup_path, exist_ok=True)

        cog_list = [cog.strip() for cog in cogs.split(',')] if cogs else None

        updated_files = 0
        for root, dirs, files in os.walk(datapath):
            for file in files:
                if file.endswith('.py'):
                    cog_name = os.path.splitext(file)[0]
                    if cog_list and cog_name not in cog_list:
                        continue

                    filepath = os.path.join(root, file)
                    relative_path = os.path.relpath(filepath, datapath)
                    backup_file = os.path.join(backup_path, relative_path)
                    os.makedirs(os.path.dirname(backup_file), exist_ok=True)
                    shutil.copy2(filepath, backup_file)

                    if file == '__init__.py':
                        updated = await self.update_init_file(filepath)
                    else:
                        updated = await self.update_file(filepath)

                    if updated:
                        updated_files += 1

        if cog_list:
            await ctx.send(f"Updated {updated_files} files for cogs: {', '.join(cog_list)}. Backups created in {backup_path}")
        else:
            await ctx.send(f"Updated {updated_files} files across all cogs. Backups created in {backup_path}")

    @commands.command()
    @commands.is_owner()
    async def undoupdates(self, ctx, *, cogs: str = None):
        """Undo the updates made to specified cogs or all cogs if none specified."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath or not backup_path:
            await ctx.send("Please set the data path first using `setpath`.")
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
        in_init = False
        has_init = False
        skip_block = False
        in_import_block = False
        has_star_utils_import = False
        version_added = False

        for i, line in enumerate(content):
            # Check if we're in an import block and for existing Star_Utils or AAA3A_utils import
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                in_import_block = True
                if 'Star_Utils' in line or 'AAA3A_utils' in line:
                    has_star_utils_import = True
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

                # Check for __init__ method
                if 'def __init__' in line:
                    in_init = True
                    has_init = True

                # Replace super().__init__() with super().__init__(bot) in __init__ method
                if in_init and 'super().__init__()' in line:
                    line = line.replace('super().__init__()', 'super().__init__(bot)')
                    updated = True

                # Fix Cog.__init__() missing 'bot' argument
                if 'Cog.__init__()' in line:
                    line = line.replace('Cog.__init__()', 'Cog.__init__(bot)')
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

            # Handle __version__ and remove other similar attributes
            if re.match(r'\s*__(?:author|authors|contributors|[a-z_]+)__\s*=', line):
                if '__version__' in line:
                    line = '__version__ = "1.0.0"\n'
                    version_added = True
                    updated = True
                else:
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

            # Reset in_init when leaving the __init__ method
            if in_init and not line.strip():
                in_init = False

            # Add the line if we're not skipping
            if not skip_block:
                new_content.append(line)

        # Add __version__ if it wasn't found in the file
        if not version_added:
            new_content.insert(0, '__version__ = "1.0.0"\n')
            updated = True

        # Add import statement if 'Cog' was found in class definition and no existing Star_Utils import
        if in_class and not has_star_utils_import:
            for i, line in enumerate(new_content):
                if line.strip().startswith('import ') or line.strip().startswith('from '):
                    continue
                else:
                    new_content.insert(i, 'from Star_Utils import Cog\n')
                    updated = True
                    break

        # Add __init__ method if it doesn't exist
        if in_class and not has_init:
            init_method = [
                '    def __init__(self, bot):\n',
                '        super().__init__(bot)\n'
            ]
            # Find the position to insert the __init__ method (after class definition)
            for i, line in enumerate(new_content):
                if 'class' in line and ':' in line:
                    new_content[i+1:i+1] = init_method
                    updated = True
                    break

        if updated:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(new_content)

        return updated

    async def update_init_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.readlines()

        updated = False
        new_content = []
        class_name = None

        for line in content:
            if line.strip().startswith('class ') and line.strip().endswith(':'):
                class_name = line.strip().split()[1].split('(')[0]

            if 'bot.add_cog' in line:
                if class_name:
                    new_line = f"    await bot.add_cog({class_name}(bot))\n"
                    if new_line != line:
                        line = new_line
                        updated = True

            new_content.append(line)

        if updated:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(new_content)

        return updated
