import random
from typing import Optional, Dict
from redbot.core import commands
from redbot.core.bot import Red
import discord
from discord import PartialEmoji

from Star_Utils import Cog, Settings, Loop

class Counting(Cog):
    """An advanced counting game cog with multiple features and extensive customization."""

    def __init__(self, bot: Red):
        self.bot = bot

        self.default_correct_emoji = PartialEmoji(name="Tick", id=1279795666507272225, animated=True)
        self.default_wrong_emoji = PartialEmoji(name="Wrong", id=1279795741300097025, animated=True)

        # Initialize settings using the Settings class from Star_Utils
        self.config = Settings(
            bot=self.bot,
            cog=self,
            config=None,
            group="counting",
            settings={
                "default_correct_emote": {
                    "converter": str,
                    "description": "Default emote for correct counts.",
                },
                "default_wrong_emote": {
                    "converter": str,
                    "description": "Default emote for wrong counts.",
                },
                "default_roasts": {
                    "converter": list,
                    "description": "Default roasts for incorrect counting.",
                },
                "joke_numbers": {
                    "converter": dict,
                    "description": "Joke numbers with custom emotes.",
                },
                "current_number": {
                    "converter": int,
                    "description": "Current number in the counting game.",
                },
                "sequential_channel_id": {
                    "converter": Optional[int],
                    "description": "Channel ID for sequential counting.",
                },
                "reverse_channel_id": {
                    "converter": Optional[int],
                    "description": "Channel ID for reverse counting.",
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
                "roasts": {
                    "converter": list,
                    "description": "Custom roasts for incorrect counting.",
                },
                "counting_mode": {
                    "converter": str,
                    "description": "Mode of counting: sequential, reverse, or both.",
                },
                "success_message": {
                    "converter": str,
                    "description": "Message for successful counting.",
                },
                "failure_message": {
                    "converter": str,
                    "description": "Message for failed counting.",
                },
                "joke_emotes": {
                    "converter": dict,
                    "description": "Custom emotes for joke numbers.",
                },
            },
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
        )

    @commands.guild_only()
    @commands.group(name="counting", invoke_without_command=True)
    async def counting(self, ctx: commands.Context):
        """Base command for the counting game."""
        await ctx.send_help(ctx.command)
    
    @commands.admin()
    @counting.command(name="setchannel")
    async def set_channel(self, ctx: commands.Context, channel: discord.TextChannel, mode: str):
        """Sets the channel for the counting game."""
        if mode not in ["sequential", "reverse"]:
            await ctx.send("Invalid mode. Please choose 'sequential' or 'reverse'.")
            return

        if mode == "sequential":
            self.config.settings["sequential_channel_id"]["converter"] = channel.id
            await ctx.send(f"Sequential counting channel set to {channel.mention}.")
        elif mode == "reverse":
            self.config.settings["reverse_channel_id"]["converter"] = channel.id
            await ctx.send(f"Reverse counting channel set to {channel.mention}.")

        self.config.settings["current_number"]["converter"] = 1 if mode == "sequential" else 100
        self.config.settings["leaderboard"]["converter"] = {}
        self.config.settings["last_counter_id"]["converter"] = None

    @commands.admin()
    @counting.command(name="setshamerole")
    async def set_shame_role(self, ctx: commands.Context, shame_role: discord.Role):
        """Sets the shame role for incorrect counting (optional)."""
        self.config.settings["shame_role"]["converter"] = shame_role.id
        await ctx.send(f"Shame role for counting set to {shame_role.mention}")

    @commands.admin()
    @counting.command(name="setemotes")
    async def set_emotes(self, ctx: commands.Context, correct_emote: str, wrong_emote: str):
        """Sets the emotes for correct and wrong counts."""
        self.config.settings["correct_emote"]["converter"] = correct_emote
        self.config.settings["wrong_emote"]["converter"] = wrong_emote
        await ctx.send("Emotes updated successfully.")

    @commands.admin()
    @counting.command(name="setmessages")
    async def set_messages(self, ctx: commands.Context, success_message: str, failure_message: str):
        """Sets custom success and failure messages for counting."""
        self.config.settings["success_message"]["converter"] = success_message
        self.config.settings["failure_message"]["converter"] = failure_message
        await ctx.send("Messages updated successfully.")

    @commands.admin()
    @counting.command(name="setmode")
    async def set_mode(self, ctx: commands.Context, mode: str):
        """Sets the counting mode (sequential, reverse, or both)."""
        if mode not in ["sequential", "reverse", "both"]:
            await ctx.send("Invalid mode. Please choose 'sequential', 'reverse', or 'both'.")
            return
        self.config.settings["counting_mode"]["converter"] = mode
        await ctx.send(f"Counting mode set to {mode}.")

    @commands.admin()
    @counting.command(name="setjokeemotes")
    async def set_joke_emotes(self, ctx: commands.Context, number: int, emote: str):
        """Sets a custom emote for a specific joke number."""
        joke_emotes = self.config.settings["joke_emotes"]["converter"]
        joke_emotes[str(number)] = emote
        self.config.settings["joke_emotes"]["converter"] = joke_emotes
        await ctx.send(f"Joke emote for {number} set to {emote}.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Handles messages in the counting game channels."""
        if message.author.bot:
            return

        guild_config = {key: setting["converter"] for key, setting in self.config.settings.items()}
        mode = guild_config["counting_mode"]
        if (mode in ["sequential", "both"] and guild_config["sequential_channel_id"] == message.channel.id) or \
           (mode in ["reverse", "both"] and guild_config["reverse_channel_id"] == message.channel.id):

            try:
                next_number = int(message.content)
                last_counter_id = guild_config["last_counter_id"]
                current_number = guild_config["current_number"]

                if message.channel.id == guild_config["sequential_channel_id"]:
                    expected_number = current_number + 1
                elif message.channel.id == guild_config["reverse_channel_id"]:
                    expected_number = current_number - 1

                if next_number == expected_number and message.author.id != last_counter_id:
                    self.config.settings["current_number"]["converter"] = next_number
                    self.config.settings["last_counter_id"]["converter"] = message.author.id
                    await message.add_reaction(guild_config["correct_emote"] or self.config.settings["default_correct_emote"]["converter"])

                    leaderboard = guild_config["leaderboard"]
                    user_id = str(message.author.id)
                    leaderboard[user_id] = leaderboard.get(user_id, 0) + 1
                    self.config.settings["leaderboard"]["converter"] = leaderboard

                    success_message = guild_config["success_message"].format(
                        display_name=message.author.display_name, next_number=next_number + 1
                    )
                    await message.channel.send(success_message)

                    # React with joke emotes if applicable
                    joke_emote = guild_config["joke_emotes"].get(str(next_number)) or self.config.settings["joke_numbers"]["converter"].get(str(next_number))
                    if joke_emote:
                        await message.add_reaction(joke_emote)

                else:
                    await message.add_reaction(guild_config["wrong_emote"] or self.config.settings["default_wrong_emote"]["converter"])

                    failure_message = guild_config["failure_message"].format(
                        display_name=message.author.display_name, expected_number=expected_number
                    )
                    await message.channel.send(failure_message)

                    if guild_config["shame_role"]:
                        shame_role = message.guild.get_role(guild_config["shame_role"])
                        await message.author.add_roles(shame_role, reason="Wrong count or double counting")
                        await message.channel.set_permissions(shame_role, send_messages=False)

                        roast = random.choice(guild_config["roasts"] or self.config.settings["default_roasts"]["converter"]).format(
                            display_name=message.author.display_name, next_number=expected_number
                        )
                        await message.channel.send(embed=discord.Embed(description=roast, color=discord.Color.red()))

                    reset_number = 1 if message.channel.id == guild_config["sequential_channel_id"] else 100
                    self.config.settings["current_number"]["converter"] = reset_number
                    self.config.settings["last_counter_id"]["converter"] = None

            except ValueError:
                pass  # Ignore non-numeric messages

    @counting.command(name="currentnumber")
    async def current_number(self, ctx: commands.Context):
        """Displays the current number in the counting game."""
        current_number = self.config.settings["current_number"]["converter"]
        await ctx.send(f"The current number is: {current_number}")

    @counting.command(name="leaderboard", aliases=["lb"])
    async def leaderboard(self, ctx: commands.Context):
        """Displays the leaderboard in an embed."""
        leaderboard = self.config.settings["leaderboard"]["converter"]
        if leaderboard:
            sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
            embed = discord.Embed(title="Counting Game Leaderboard", color=discord.Color.blue())
            for user_id, score in sorted_leaderboard[:10]:  # Show top 10
                user = self.bot.get_user(int(user_id))
                embed.add_field(name=user.name, value=score, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("The leaderboard is empty.")

    @commands.guildowner()
    @counting.command(name="reset")
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
