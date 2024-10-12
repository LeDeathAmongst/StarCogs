from redbot.core import commands, Config
import discord
from datetime import datetime
from discord.ext import tasks

class ThemedChanger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)

        # Define default themes with nicknames and avatar URLs
        default_themes = {
            "New Year": {
                "nickname": "Happy New Year!",
                "avatar": "https://example.com/newyear_avatar.png"  # Replace with actual URL
            },
            "Valentine's Day": {
                "nickname": "Love is in the air!",
                "avatar": "https://example.com/valentine_avatar.png"
            },
            "St. Patrick's Day": {
                "nickname": "Feeling Lucky!",
                "avatar": "https://example.com/stpat_avatar.png"
            },
            "Fourth of July": {
                "nickname": "Happy Independence Day!",
                "avatar": "https://example.com/fourthofjuly_avatar.png"
            },
            "Halloween": {
                "nickname": "Spooky Bot!",
                "avatar": "https://example.com/halloween_avatar.png"
            },
            "Thanksgiving": {
                "nickname": "Thankful Bot!",
                "avatar": "https://example.com/thanksgiving_avatar.png"
            },
            "Christmas": {
                "nickname": "Merry Christmas!",
                "avatar": "https://example.com/christmas_avatar.png"
            },
        }

        self.config.register_global(themes=default_themes)

        # Start the theme changer loop
        self.change_theme.start()

    def cog_unload(self):
        self.change_theme.stop()

    @tasks.loop(hours=1)  # Check every hour
    async def change_theme(self):
        current_theme = self.get_current_theme()
        if current_theme:
            await self.update_bot_theme(current_theme)

    def get_current_theme(self):
        """Determine the current theme based on the date."""
        now = datetime.now()

        # Example logic for determining the theme based on the date
        if now.month == 1 and now.day <= 5:  # New Year theme
            return "New Year"
        elif now.month == 2 and now.day == 14:  # Valentine's Day theme
            return "Valentine's Day"
        elif now.month == 3 and now.day == 17:  # St. Patrick's Day theme
            return "St. Patrick's Day"
        elif now.month == 7 and now.day == 4:  # Fourth of July theme
            return "Fourth of July"
        elif now.month == 10 and now.day == 31:  # Halloween theme
            return "Halloween"
        elif now.month == 11 and now.day == 4:  # Thanksgiving (4th Thursday of November)
            if now.weekday() == 3 and (22 <= now.day <= 28):  # Make sure it's the right week
                return "Thanksgiving"
        elif now.month == 12:  # Christmas theme
            return "Christmas"

        return None  # No theme matches

    async def update_bot_theme(self, theme_name):
        """Update the bot's nickname and avatar based on the current theme."""
        themes = await self.config.themes()
        theme = themes.get(theme_name)

        if theme:
            nickname = theme.get("nickname")
            avatar_url = theme.get("avatar")

            # Change nickname
            try:
                await self.bot.user.edit(nick=nickname)
                print(f"Nickname changed to '{nickname}'")
            except discord.Forbidden:
                print(f"Failed to change nickname to '{nickname}': Missing permissions.")

            # Change avatar
            try:
                if avatar_url:
                    async with self.bot.session.get(avatar_url) as response:
                        if response.status == 200:
                            avatar_data = await response.read()
                            await self.bot.user.edit(avatar=avatar_data)
                            print("Avatar updated.")
            except discord.Forbidden:
                print("Failed to change avatar: Missing permissions.")
            except Exception as e:
                print(f"Error updating avatar: {e}")

    @commands.command()
    @commands.is_owner()
    async def set_theme(self, ctx, holiday: str, nickname: str, avatar_url: str):
        """Set the nickname and avatar for a specific holiday."""
        themes = await self.config.themes()

        if holiday in themes:
            themes[holiday]["nickname"] = nickname
            themes[holiday]["avatar"] = avatar_url
            await self.config.themes.set(themes)
            await ctx.send(f"Updated {holiday} theme: Nickname set to '{nickname}' and avatar updated.")
        else:
            await ctx.send(f"Holiday '{holiday}' not found. Available holidays: {', '.join(themes.keys())}")

async def setup(bot):
    await bot.add_cog(ThemedChanger(bot))
