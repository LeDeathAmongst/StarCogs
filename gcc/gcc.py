import discord
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n

_ = Translator("GCC", __file__)

@cog_i18n(_)
class GCC(commands.Cog):
    """Manage global custom commands."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)  # Replace with a unique identifier
        self.config.register_global(commands={})

    @commands.group(name="gcc", invoke_without_command=True)
    @commands.is_owner()
    async def gcc(self, ctx: commands.Context):
        """Base command for managing global custom commands."""
        await ctx.send_help(ctx.command)

    @gcc.command(name="create")
    @commands.is_owner()
    async def gcc_create(self, ctx: commands.Context, name: str, description: str, *, content: str):
        """Create a global custom command.

        **Arguments:**
        - `<name>` The name of the command.
        - `<description>` The description of the command.
        - `<content>` The content to return when the command is invoked.
        """
        commands = await self.config.commands()
        if name in commands:
            await ctx.send(_("A command with this name already exists."))
            return

        commands[name] = {
            "description": description,
            "content": content,
        }
        await self.config.commands.set(commands)
        await ctx.send(_("Global custom command `{}` created successfully.").format(name))

    @gcc.command(name="edit")
    @commands.is_owner()
    async def gcc_edit(self, ctx: commands.Context, name: str, description: str = None, *, content: str = None):
        """Edit a global custom command.

        **Arguments:**
        - `<name>` The name of the command.
        - `[description]` The new description of the command.
        - `[content]` The new content to return when the command is invoked.
        """
        commands = await self.config.commands()
        if name not in commands:
            await ctx.send(_("A command with this name does not exist."))
            return

        if description:
            commands[name]["description"] = description
        if content:
            commands[name]["content"] = content

        await self.config.commands.set(commands)
        await ctx.send(_("Global custom command `{}` edited successfully.").format(name))

    @gcc.command(name="delete")
    @commands.is_owner()
    async def gcc_delete(self, ctx: commands.Context, name: str):
        """Delete a global custom command.

        **Arguments:**
        - `<name>` The name of the command.
        """
        commands = await self.config.commands()
        if name not in commands:
            await ctx.send(_("A command with this name does not exist."))
            return

        del commands[name]
        await self.config.commands.set(commands)
        await ctx.send(_("Global custom command `{}` deleted successfully.").format(name))

    @commands.Cog.listener()
    async def on_message_without_command(self, message: discord.Message):
        if message.author.bot:
            return

        ctx = await self.bot.get_context(message)
        if ctx.valid:
            return

        commands = await self.config.commands()
        if message.content in commands:
            await message.channel.send(commands[message.content]["content"])

def setup(bot: Red):
    bot.add_cog(GCC(bot))
