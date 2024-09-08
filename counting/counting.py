import random
from typing import Optional
from redbot.core import commands, Config
from redbot.core.bot import Red
import discord
from datetime import datetime

from Star_Utils import Cog, Settings, Loop

class Counting(Cog):
    """An advanced counting game cog with multiple features and extensive customization."""

    def __init__(self, bot: Red):
        self.bot = bot

        self.default_correct_emoji = "<a:Tick:1279795666507272225>"
        self.default_wrong_emoji = "<a:Wrong:1279795741300097025>"

        self.config = Config.get_conf(self, identifier=271828, force_registration=True)
        self.config.register_global(
            current_number=0,
            channel_id=None,
            leaderboard={},
            correct_emote=self.default_correct_emoji,
            wrong_emote=self.default_wrong_emoji,
            shame_role=None,
            last_counter_id=None,
            default_roasts=[
                "{display_name} couldn't even count to {next_number}! Maybe try using your fingers next time?",
                "Looks like {display_name} skipped a few math classes... Back to square one!",
                "{display_name}, is that your final answer? Because it's definitely wrong!",
                "{display_name}'s counting skills are as impressive as their ability to divide by zero.",
                "{display_name}, are you sure you're not a calculator in disguise? Because your math is off!",
            ],
            success_message="Great job, {display_name}! The next number is {next_number}.",
            failure_message="Oops, {display_name}! You messed up. The number was {expected_number}.",
            linked_channels=[],
            global_current_number=0,
            global_last_counter_id=None,
            global_leaderboard={},
        )

        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group="global",
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
            global_path=[],  # Ensure global path is empty
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
        loop = Loop(
            cog=self,
            name="DailyLeaderboardReset",
            function=self.reset_leaderboard_daily,
            days=1
        )
        self.loops.append(loop)

    async def reset_leaderboard_daily(self):
        """Reset the leaderboard daily."""
        # Reset leaderboard globally
        await self.config.global_leaderboard.set({})
        self.log_action("info", "Global leaderboard reset.")

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
        if channel is None:
            channel = await ctx.guild.create_text_channel(name="counting-game")
            await ctx.send(f"Counting game channel created: {channel.mention}. Please set the shame role (optional) using `countingsetshamerole`.")
        else:
            await ctx.send(f"Counting game channel set to {channel.mention}. Please set the shame role (optional) using `countingsetshamerole`.")

        await self.config.channel_id.set(channel.id)
        await self.config.current_number.set(0)
        await self.config.leaderboard.set({})
        await self.config.last_counter_id.set(None)

        self.log_action("info", f"Counting channel set to {channel.id}.")

    @commands.command()
    async def countingsetshamerole(self, ctx, shame_role: discord.Role):
        """Sets the shame role for incorrect counting (optional)."""
        await self.config.shame_role.set(shame_role.id)
        await ctx.send(f"Shame role for counting set to {shame_role.mention}")
        self.log_action("info", f"Shame role set to {shame_role.id}.")

    @commands.command()
    async def countingsetemotes(self, ctx, correct_emote: str, wrong_emote: str):
        """Sets the emotes for correct and wrong counts."""
        await self.config.correct_emote.set(correct_emote)
        await self.config.wrong_emote.set(wrong_emote)
        await ctx.send("Emotes updated successfully.")
        self.log_action("info", f"Correct emote set to {correct_emote}, wrong emote set to {wrong_emote}.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Handles messages in both local and global counting channels."""
        if message.author.bot:
            return

        # Handle local counting
        local_channel_id = await self.config.channel_id()
        if message.channel.id == local_channel_id:
            await self.handle_local_counting(message)

        # Handle global counting
        linked_channels = await self.config.linked_channels()
        if message.channel.id in linked_channels:
            await self.handle_global_counting(message)

    async def handle_local_counting(self, message: discord.Message):
        """Handle the local counting logic."""
        guild_config = await self.config.all()
        try:
            next_number = int(message.content)
            last_counter_id = guild_config["last_counter_id"]
            if next_number == guild_config["current_number"] + 1 and message.author.id != last_counter_id:
                await self.config.current_number.set(next_number)
                await self.config.last_counter_id.set(message.author.id)

                correct_emote = guild_config.get("correct_emote", self.default_correct_emoji)
                if isinstance(correct_emote, str):
                    await message.add_reaction(correct_emote)

                leaderboard = guild_config["leaderboard"]
                user_id = str(message.author.id)
                leaderboard[user_id] = leaderboard.get(user_id, 0) + 1
                await self.config.leaderboard.set(leaderboard)

                self.log_action("info", f"{message.author.display_name} counted correctly to {next_number}.")

            else:
                wrong_emote = guild_config.get("wrong_emote", self.default_wrong_emoji)
                if isinstance(wrong_emote, str):
                    await message.add_reaction(wrong_emote)

                await self.config.current_number.set(0)
                await self.config.last_counter_id.set(None)

                self.log_action("warning", f"{message.author.display_name} counted incorrectly.")

        except ValueError:
            pass  # Ignore non-numeric messages

    async def handle_global_counting(self, message: discord.Message):
        """Handle the global counting logic."""
        try:
            next_number = int(message.content)
            global_current_number = await self.config.global_current_number()
            global_last_counter_id = await self.config.global_last_counter_id()

            if next_number == global_current_number + 1 and message.author.id != global_last_counter_id:
                await self.config.global_current_number.set(next_number)
                await self.config.global_last_counter_id.set(message.author.id)

                # Use the default correct emoji
                correct_emote = self.default_correct_emoji
                if isinstance(correct_emote, str):
                    await message.add_reaction(correct_emote)

                # Update global leaderboard
                global_leaderboard = await self.config.global_leaderboard()
                user_key = f"{message.guild.id}-{message.author.id}"
                global_leaderboard[user_key] = global_leaderboard.get(user_key, 0) + 1
                await self.config.global_leaderboard.set(global_leaderboard)

                # Relay the message to all linked channels
                linked_channels = await self.config.linked_channels()
                for channel_id in linked_channels:
                    if channel_id != message.channel.id:
                        channel = self.bot.get_channel(channel_id)
                        if channel:
                            await channel.send(f"{message.author.display_name}: {next_number}")

            else:
                # Use the default wrong emoji
                wrong_emote = self.default_wrong_emoji
                if isinstance(wrong_emote, str):
                    await message.add_reaction(wrong_emote)

                await message.delete()

        except ValueError:
            await message.delete()

    @commands.command()
    async def currentnumber(self, ctx):
        """Displays the current number in the local counting game."""
        current_number = await self.config.current_number()
        await ctx.send(f"The current local number is: {current_number}")

    @commands.command()
    async def countinglb(self, ctx):
        """Displays the local leaderboard in an embed."""
        leaderboard = await self.config.leaderboard()
        if leaderboard:
            sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
            embed = discord.Embed(title="Local Counting Game Leaderboard", color=discord.Color.blue())
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
        """Resets the local counting game."""
        if mode not in ["sequential", "reverse", None]:
            await ctx.send("Invalid mode. Please choose 'sequential', 'reverse', or leave empty for both.")
            return

        if mode in ["sequential", None]:
            await self.config.current_number.set(0)
            await self.config.leaderboard.set({})
            await self.config.last_counter_id.set(None)

        if mode in ["reverse", None]:
            await self.config.current_number.set(100000)
            await self.config.leaderboard.set({})
            await self.config.last_counter_id.set(None)

        await ctx.send(f"The local counting game{' for ' + mode if mode else ''} has been reset.")
        self.log_action("info", "Local counting game reset.")

    @commands.group(name="globalcounting", invoke_without_command=True)
    async def globalcounting(self, ctx: commands.Context):
        """Manage global counting settings."""
        await ctx.send_help(ctx.command)

    @globalcounting.command(name="set")
    async def globalcountingset(self, ctx: commands.Context):
        """Link the current channel to the global counting network."""
        linked_channels = await self.config.linked_channels()
        if ctx.channel.id not in linked_channels:
            linked_channels.append(ctx.channel.id)
            await self.config.linked_channels.set(linked_channels)
            await ctx.send("This channel has been linked to the global counting network.")
        else:
            await ctx.send("This channel is already linked to the global counting network.")

    @globalcounting.command(name="unset")
    async def globalcountingunset(self, ctx: commands.Context):
        """Unlink the current channel from the global counting network."""
        linked_channels = await self.config.linked_channels()
        if ctx.channel.id in linked_channels:
            linked_channels.remove(ctx.channel.id)
            await self.config.linked_channels.set(linked_channels)
            await ctx.send("This channel has been unlinked from the global counting network.")
        else:
            await ctx.send("This channel is not linked to the global counting network.")

    @commands.command()
    async def globalcurrentnumber(self, ctx: commands.Context):
        """Displays the current number in the global counting game."""
        global_current_number = await self.config.global_current_number()
        await ctx.send(f"The current global number is: {global_current_number}")

    @commands.command()
    async def globallb(self, ctx: commands.Context):
        """Displays the global leaderboard."""
        global_leaderboard = await self.config.global_leaderboard()
        if global_leaderboard:
            sorted_leaderboard = sorted(global_leaderboard.items(), key=lambda item: item[1], reverse=True)
            embed = discord.Embed(title="Global Counting Game Leaderboard", color=discord.Color.green())
            for user_key, score in sorted_leaderboard[:10]:  # Show top 10
                guild_id, user_id = map(int, user_key.split('-'))
                guild = self.bot.get_guild(guild_id)
                user = guild.get_member(user_id) if guild else None
                if user:
                    embed.add_field(name=f"{guild.name} - {user.display_name}", value=score, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("The global leaderboard is empty.")
