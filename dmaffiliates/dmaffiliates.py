from redbot.core import commands, Config, checks
from discord.ext import commands as ext_commands
import discord
import re

class DMAffiliates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)

        default_guild = {
            "welcome_message": None,
            "buttons": []
        }

        self.config.register_guild(**default_guild)

    @commands.group()
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def dmaffiliate(self, ctx):
        """Group command for managing DMAffiliates settings."""
        pass

    @dmaffiliate.command()
    async def setmessage(self, ctx, *, message: str):
        """Set the welcome message to send to new members."""
        await self.config.guild(ctx.guild).welcome_message.set(message)
        await ctx.send("Welcome message set!")

    @dmaffiliate.command()
    async def addbutton(self, ctx, label: str, *, message: str):
        """Add buttons from a message containing links."""
        links = re.findall(r'(http[s]?://\S+)', message)
        if not links:
            await ctx.send("No valid links found in the message.")
            return

        async with self.config.guild(ctx.guild).buttons() as buttons:
            for url in links:
                if len(buttons) >= 25:
                    await ctx.send("You can only add up to 25 buttons.")
                    return
                buttons.append({"label": label, "url": url})
        await ctx.send(f"Buttons for '{label}' added!")

    @dmaffiliate.command()
    async def clearbuttons(self, ctx):
        """Clear all buttons."""
        await self.config.guild(ctx.guild).buttons.set([])
        await ctx.send("All buttons cleared!")

    @dmaffiliate.command()
    async def removebutton(self, ctx, index: int):
        """Remove a button by its index (starting from 1)."""
        async with self.config.guild(ctx.guild).buttons() as buttons:
            if 1 <= index <= len(buttons):
                removed_button = buttons.pop(index - 1)
                await ctx.send(f"Button '{removed_button['label']}' removed!")
            else:
                await ctx.send("Invalid button index.")

    @dmaffiliate.command()
    async def preview(self, ctx):
        """Preview the welcome message with buttons."""
        welcome_message = await self.config.guild(ctx.guild).welcome_message()
        buttons = await self.config.guild(ctx.guild).buttons()

        if welcome_message:
            await ctx.send(content=welcome_message)
        else:
            await ctx.send("No welcome message configured.")

        if buttons:
            view = discord.ui.View()
            for button in buttons:
                view.add_item(discord.ui.Button(label=button["label"], url=button["url"]))
            await ctx.send("Here is a preview of the buttons:", view=view)
        else:
            await ctx.send("No buttons configured.")

    @ext_commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        welcome_message = await self.config.guild(guild).welcome_message()

        if welcome_message:
            try:
                await member.send(content=welcome_message)
                print(f"Sent welcome message to {member.name}.")
            except discord.Forbidden:
                print(f"Could not send welcome message to {member.name}.")

async def setup(bot):
    await bot.add_cog(DMAffiliates(bot))
