import os
import re
from redbot.core import commands
from redbot.core import Config

class CogUpdater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {"datapath": ""}
        self.config.register_global(**default_global)

    @commands.command()
    @commands.is_owner()
    async def set_datapath(self, ctx, path: str):
        """Set the path to the cog data directory."""
        await self.config.datapath.set(path)
        await ctx.send(f"Data path set to: {path}")

    @commands.command()
    @commands.is_owner()
    async def update_cogs(self, ctx):
        """Update cogs in the data directory."""
        datapath = await self.config.datapath()
        if not datapath:
            await ctx.send("Please set the data path first using `set_datapath`.")
            return

        updated_files = 0
        for root, dirs, files in os.walk(datapath):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    updated = await self.update_file(filepath)
                    if updated:
                        updated_files += 1

        await ctx.send(f"Updated {updated_files} files.")

    async def update_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace 'commands.Cog' with 'Cog'
        content = content.replace('commands.Cog', 'Cog')

        # Replace 'AAA3A_utils' with 'Star_Utils' if 'Cog' is present
        if 'Cog' in content:
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
