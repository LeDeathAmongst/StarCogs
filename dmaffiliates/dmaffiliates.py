from redbot.core import commands, Config, checks

from Star_Utils import Cog

class DMAffiliate(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)

        default_guild = {
            "message": None,
            "buttons": []
        }

        self.config.register_guild(**default_guild)

    @commands.group()
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def dmaffiliate(self, ctx):
        """Group command for managing dmaffiliate settings."""
        pass

    @dmaffiliate.command()
    async def setmessage(self, ctx, *, message: str):
        """Set the message to send to new members."""
        await self.config.guild(ctx.guild).message.set(message)
        await ctx.send("Message set!")

    @dmaffiliate.command()
    async def addbutton(self, ctx, label: str, url: str):
        """Add a button to the message."""
        async with self.config.guild(ctx.guild).buttons() as buttons:
            if len(buttons) >= 25:
                await ctx.send("You can only add up to 25 buttons.")
                return
            buttons.append({"label": label, "url": url})
        await ctx.send(f"Button '{label}' added!")

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

    @ext_commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        message = await self.config.guild(guild).message()
        buttons = await self.config.guild(guild).buttons()

        if message and buttons:
            view = discord.ui.View()
            for button in buttons:
                view.add_item(discord.ui.Button(label=button["label"], url=button["url"]))

            try:
                await member.send(content=message, view=view)
                print(f"Sent welcome message to {member.name}.")
            except discord.Forbidden:
                print(f"Could not send welcome message to {member.name}.")

async def setup(bot):
    await bot.add_cog(DMAffiliate(bot))
