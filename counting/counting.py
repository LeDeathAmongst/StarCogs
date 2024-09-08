import random
from typing import Optional, Dict
from redbot.core import commands
from redbot.core.bot import Red
import discord

from Star_Utils import Cog, Settings, Loop

class Counting(Cog):
    """An advanced counting game cog with multiple features and extensive customization."""

    def __init__(self, bot: Red):
        self.bot = bot

        # Define default animated emojis as strings
        self.default_correct_emoji = "<a:Tick:1279795666507272225>"
        self.default_wrong_emoji = "<a:Wrong:1279795741300097025>"

        # Initialize settings using the Settings class from Star_Utils
        self.config = Settings(
            bot=self.bot,
            cog=self,
            config=None,
            group="counting",
            settings={
                "current_number": {
                    "converter": int,
                    "description": "Current number in the counting game.",
                },
                "channel_id": {
                    "converter": Optional[int],
                    "description": "Channel ID for the counting game.",
                },
                "leaderboard": {
                    "converter": dict,
                    "description": "Leaderboard for the counting game.",
                },
                "correct_emote": {
                    "converter": str,
                    "description": "Emote for correct counts.",
                },
                "wrong_emote": {
                    "converter": str,
                    "description": "Emote for wrong counts.",
                },
                "shame_role": {
                    "converter": Optional[int],
                    "description": "Role ID for shaming incorrect counters.",
                },
                "last_counter_id": {
                    "converter": Optional[int],
                    "description": "ID of the last user who counted correctly.",
                },
                "default_roasts": {
                    "converter": list,
                    "description": "Default roasts for incorrect counting.",
                },
                "success_message": {
                    "converter": str,
                    "description": "Message for successful counting.",
                },
                "failure_message": {
                    "converter": str,
                    "description": "Message for failed counting.",
                },
            },
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
        )

        # Initialize a list to store loops
        self.loops = []

        # Start any loops needed by the cog
        self.start_loops()

    def start_loops(self):
        """Start any loops needed by the cog."""
        # Example: Start a loop that checks and resets the leaderboard every day
        loop = Loop(
            cog=self,
            name="DailyLeaderboardReset",
            function=self.reset_leaderboard_daily,
            days=1
        )
        self.loops.append(loop)

    async def reset_leaderboard_daily(self):
        """Reset the leaderboard daily."""
        guilds = await self.config.all_guilds()
        for guild_id, data in guilds.items():
            data["leaderboard"] = {}
            await self.config.guild_from_id(guild_id).leaderboard.set({})

    async def cog_unload(self):
        """Ensure all loops are stopped when the cog is unloaded."""
        for loop in self.loops:
            loop.stop_all()

    @commands.command()
    async def countingsetchannel(self, ctx, channel: Optional[discord.TextChannel] = None):
        """Sets the channel for the counting game. If no channel is provided, a new one is created."""
        guild = ctx.guild

        if channel is None:
            channel = await guild.create_text_channel(name="counting-game")
            await ctx.send(f"Counting game channel created: {channel.mention}. Please set the shame role (optional) using `countingsetshamerole`.")
        else:
            await ctx.send(f"Counting game channel set to {channel.mention}. Please set the shame role (optional) using `countingsetshamerole`.")

        self.config.settings["channel_id"]["converter"] = channel.id
        self.config.settings["current_number"]["converter"] = 1
        self.config.settings["leaderboard"]["converter"] = {}
        self.config.settings["last_counter_id"]["converter"] = None

    @commands.command()
    async def countingsetshamerole(self, ctx, shame_role: discord.Role):
        """Sets the shame role for incorrect counting (optional)."""
        self.config.settings["shame_role"]["converter"] = shame_role.id
        await ctx.send(f"Shame role for counting set to {shame_role.mention}")

    @commands.command()
    async def countingsetemotes(self, ctx, correct_emote: str, wrong_emote: str):
        """Sets the emotes for correct and wrong counts."""
        self.config.settings["correct_emote"]["converter"] = correct_emote
        self.config.settings["wrong_emote"]["converter"] = wrong_emote
        await ctx.send("Emotes updated successfully.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Handles messages in the counting game channel."""
        if message.author.bot:
            return

        guild_config = {key: setting["converter"] for key, setting in self.config.settings.items()}
        if guild_config["channel_id"] == message.channel.id:
            try:
                next_number = int(message.content)
                last_counter_id = guild_config["last_counter_id"]
                if next_number == guild_config["current_number"] + 1 and message.author.id != last_counter_id:
                    self.config.settings["current_number"]["converter"] = next_number
                    self.config.settings["last_counter_id"]["converter"] = message.author.id

                    # Use the correct emoji
                    correct_emote = guild_config.get("correct_emote", self.default_correct_emoji)
                    await message.add_reaction(correct_emote)

                    leaderboard = guild_config["leaderboard"]
                    user_id = str(message.author.id)
                    leaderboard[user_id] = leaderboard.get(user_id, 0) + 1
                    self.config.settings["leaderboard"]["converter"] = leaderboard

                    success_message = guild_config.get("success_message", "Great job, {display_name}! The next number is {next_number}.")
                    await message.channel.send(success_message.format(display_name=message.author.display_name, next_number=next_number + 1))

                else:
                    # Use the wrong emoji
                    wrong_emote = guild_config.get("wrong_emote", self.default_wrong_emoji)
                    await message.add_reaction(wrong_emote)

                    failure_message = guild_config.get("failure_message", "Oops, {display_name}! You messed up. The number was {expected_number}.")
                    await message.channel.send(failure_message.format(display_name=message.author.display_name, expected_number=guild_config["current_number"] + 1))

                    if guild_config["shame_role"]:
                        shame_role = message.guild.get_role(guild_config["shame_role"])
                        if shame_role:
                            await message.author.add_roles(shame_role, reason="Wrong count or double counting")
                            await message.channel.set_permissions(shame_role, send_messages=False)

                        roasts = guild_config.get("default_roasts", [
                            f"{message.author.display_name} couldn't even count to {guild_config['current_number'] + 1}! Maybe try using your fingers next time?",
                            f"Looks like {message.author.display_name} skipped a few math classes... Back to square one!",
                            f"{message.author.display_name}, is that your final answer? Because it's definitely wrong!",
                            f"{message.author.display_name}'s counting skills are as impressive as their ability to divide by zero.",
                            f"{message.author.display_name}, are you sure you're not a calculator in disguise? Because your math is off!",
                        ])
                        roast = random.choice(roasts)
                        await message.channel.send(embed=discord.Embed(description=roast, color=discord.Color.red()))

                    self.config.settings["current_number"]["converter"] = 1
                    self.config.settings["last_counter_id"]["converter"] = None

            except ValueError:
                pass  # Ignore non-numeric messages

    @commands.command()
    async def currentnumber(self, ctx):
        """Displays the current number in the counting game."""
        current_number = self.config.settings["current_number"]["converter"]
        await ctx.send(f"The current number is: {current_number}")

    @commands.command(aliases=["countingboard", "countingleaderboard"])
    async def countinglb(self, ctx):
        """Displays the leaderboard in an embed."""
        leaderboard = self.config.settings["leaderboard"]["converter"]
        if leaderboard:
            sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
            embed = discord.Embed(title="Counting Game Leaderboard", color=discord.Color.blue())
            for user_id, score in sorted_leaderboard[:10]:  # Show top 10
                user = self.bot.get_user(int(user_id))
                if user:
                    embed.add_field(name=user.name, value=score, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("The leaderboard is empty.")

    @commands.guildowner()
    @commands.command(name="reset")
    async def reset_game(self, ctx: commands.Context, mode: Optional[str] = None):
        """Resets the counting game."""
        if mode not in ["sequential", "reverse", None]:
            await ctx.send("Invalid mode. Please choose 'sequential', 'reverse', or leave empty for both.")
            return

        if mode in ["sequential", None]:
            self.config.settings["current_number"]["converter"] = 0
            self.config.settings["leaderboard"]["converter"] = {}
            self.config.settings["last_counter_id"]["converter"] = None

        if mode in ["reverse", None]:
            self.config.settings["current_number"]["converter"] = 100000
            self.config.settings["leaderboard"]["converter"] = {}
            self.config.settings["last_counter_id"]["converter"] = None

        await ctx.send(f"The counting game{' for ' + mode if mode else ''} has been reset.")
