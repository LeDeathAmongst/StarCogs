import random
from typing import Optional
from redbot.core import commands
from redbot.core.bot import Red
import discord
from datetime import datetime

from Star_Utils import Cog, Settings, Loop

class Counting(Cog):
    """An advanced counting game cog with multiple features and extensive customization."""

    def __init__(self, bot: Red):
        super().__init__(bot)  # Ensure the base class is initialized
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

        # Initialize logs dictionary
        self.logs = {}

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
            # Log the reset action
            self.log_action("info", f"Leaderboard reset for guild {guild_id}.")

    def log_action(self, level: str, message: str):
        """Log an action in the logs dictionary."""
        if level not in self.logs:
            self.logs[level] = []
        self.logs[level].append({
            "time": datetime.utcnow(),
            "levelname": level.upper(),
            "message": message,
            "exc_info": None
        })

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

        await self.config.guild(guild).channel_id.set(channel.id)
        await self.config.guild(guild).current_number.set(0)
        await self.config.guild(guild).leaderboard.set({})
        await self.config.guild(guild).last_counter_id.set(None)

        # Log the channel setup
        self.log_action("info", f"Counting channel set to {channel.id} in guild {guild.id}.")

    @commands.command()
    async def countingsetshamerole(self, ctx, shame_role: discord.Role):
        """Sets the shame role for incorrect counting (optional)."""
        await self.config.guild(ctx.guild).shame_role.set(shame_role.id)
        await ctx.send(f"Shame role for counting set to {shame_role.mention}")

        # Log the shame role setup
        self.log_action("info", f"Shame role set to {shame_role.id} in guild {ctx.guild.id}.")

    @commands.command()
    async def countingsetemotes(self, ctx, correct_emote: str, wrong_emote: str):
        """Sets the emotes for correct and wrong counts."""
        await self.config.guild(ctx.guild).correct_emote.set(correct_emote)
        await self.config.guild(ctx.guild).wrong_emote.set(wrong_emote)
        await ctx.send("Emotes updated successfully.")

        # Log the emote setup
        self.log_action("info", f"Correct emote set to {correct_emote}, wrong emote set to {wrong_emote} in guild {ctx.guild.id}.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Handles messages in the counting game channel."""
        if message.author.bot:
            return

        guild = message.guild
        guild_config = await self.config.guild(guild).all()

        if guild_config["channel_id"] == message.channel.id:
            try:
                next_number = int(message.content)
                last_counter_id = guild_config["last_counter_id"]
                if next_number == guild_config["current_number"] + 1 and message.author.id != last_counter_id:
                    await self.config.guild(guild).current_number.set(next_number)
                    await self.config.guild(guild).last_counter_id.set(message.author.id)

                    # Use the correct emoji
                    correct_emote = guild_config.get("correct_emote", self.default_correct_emoji)
                    await message.add_reaction(correct_emote)

                    leaderboard = guild_config["leaderboard"]
                    user_id = str(message.author.id)
                    leaderboard[user_id] = leaderboard.get(user_id, 0) + 1
                    await self.config.guild(guild).leaderboard.set(leaderboard)

                    success_message = guild_config.get("success_message", "Great job, {display_name}! The next number is {next_number}.")
                    await message.channel.send(success_message.format(display_name=message.author.display_name, next_number=next_number + 1))

                    # Log the successful count
                    self.log_action("info", f"{message.author.display_name} counted correctly to {next_number} in guild {message.guild.id}.")

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

                    await self.config.guild(guild).current_number.set(0)  # Reset to 0
                    await self.config.guild(guild).last_counter_id.set(None)

                    # Log the incorrect count
                    self.log_action("warning", f"{message.author.display_name} counted incorrectly in guild {message.guild.id}.")

            except ValueError:
                pass  # Ignore non-numeric messages

    @commands.command()
    async def currentnumber(self, ctx):
        """Displays the current number in the counting game."""
        current_number = await self.config.guild(ctx.guild).current_number()
        await ctx.send(f"The current number is: {current_number}")

    @commands.command(aliases=["countingboard", "countingleaderboard"])
    async def countinglb(self, ctx):
        """Displays the leaderboard in an embed."""
        leaderboard = await self.config.guild(ctx.guild).leaderboard()
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
            await self.config.guild(ctx.guild).current_number.set(0)
            await self.config.guild(ctx.guild).leaderboard.set({})
            await self.config.guild(ctx.guild).last_counter_id.set(None)

        if mode in ["reverse", None]:
            await self.config.guild(ctx.guild).current_number.set(100000)
            await self.config.guild(ctx.guild).leaderboard.set({})
            await self.config.guild(ctx.guild).last_counter_id.set(None)

        await ctx.send(f"The counting game{' for ' + mode if mode else ''} has been reset.")

        # Log the reset action
        self.log_action("info", f"Counting game reset in guild {ctx.guild.id}.")
