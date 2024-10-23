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
    async def update_cogs(self, ctx):
        """Update cogs in the data directory."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath:
            await ctx.send("Please set the data path first using `set_datapath`.")
            return

        # Create backup directory
        os.makedirs(backup_path, exist_ok=True)

        updated_files = 0
        for root, dirs, files in os.walk(datapath):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    relative_path = os.path.relpath(filepath, datapath)
                    backup_file = os.path.join(backup_path, relative_path)
                    os.makedirs(os.path.dirname(backup_file), exist_ok=True)
                    shutil.copy2(filepath, backup_file)
                    updated = await self.update_file(filepath)
                    if updated:
                        updated_files += 1

        await ctx.send(f"Updated {updated_files} files. Backups created in {backup_path}")

    @commands.command()
    @commands.is_owner()
    async def undo_updates(self, ctx):
        """Undo the updates made to cogs."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath or not backup_path:
            await ctx.send("Please set the data path first using `set_datapath`.")
            return

        restored_files = 0
        for root, dirs, files in os.walk(backup_path):
            for file in files:
                if file.endswith('.py'):
                    backup_file = os.path.join(root, file)
                    relative_path = os.path.relpath(backup_file, backup_path)
                    original_file = os.path.join(datapath, relative_path)
                    shutil.copy2(backup_file, original_file)
                    restored_files += 1

        # Remove the backup directory
        shutil.rmtree(backup_path)

        await ctx.send(f"Restored {restored_files} files. Backups have been removed.")

    async def update_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace 'commands.Cog' with 'Cog' only in class definitions
        content = re.sub(r'(class\s+\w+\s*\(\s*)commands\.Cog', r'\1Cog', content)

        # Replace 'AAA3A_utils' with 'Star_Utils' if 'Cog' is present in class definition
        if re.search(r'class\s+\w+\s*\(\s*Cog', content):
            content = content.replace('AAA3A_utils', 'Star_Utils')

        # Remove __author__, __version__, and __contributors__
        content = re.sub(r'__author__\s*=.*\n', '', content)
        content = re.sub(r'__version__\s*=.*\n', '', content)
        content = re.sub(r'__contributors__\s*=.*\n', '', content)

        # Remove the format_help_for_context method
        content = re.sub(
            r'def format_help_for_context\(self, ctx\):.*?return info\n',
            '',
            content,
            flags=re.DOTALL
        )

        # Write the updated content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

        return True
