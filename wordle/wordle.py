import discord
from redbot.core import commands, Config
import random
import asyncio
from PIL import Image, ImageDraw, ImageFont
import io
import aiohttp
import json
import tempfile
import os

from Star_Utils import Cog, CogsUtils

class Wordle(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "leaderboard": {},
            "stats": {}
        }
        default_user = {
            "word_length": 5,
            "max_tries": 6,
            "colorblind": False,
            "hard_mode": False
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)
        self.games = {}
        self.session = aiohttp.ClientSession()
        self.font_path = None
        self.word_lists = self.load_words_from_file()

    def load_words_from_file(self):
        word_lists = {i: [] for i in range(3, 13)}
        file_path = os.path.join(os.path.dirname(__file__), "wordle_words.txt")

        try:
            with open(file_path, 'r') as file:
                for word in file:
                    word = word.strip().upper()
                    length = len(word)
                    if 3 <= length <= 12:
                        word_lists[length].append(word)
        except FileNotFoundError:
            print(f"Word file not found: {file_path}")

        return word_lists

    def get_random_word(self, length):
        if length in self.word_lists and self.word_lists[length]:
            return random.choice(self.word_lists[length])
        else:
            return None
 
    def cog_unload(self):
        asyncio.create_task(self.session.close())
        if self.font_path and os.path.exists(self.font_path):
            os.remove(self.font_path)

    async def fetch_google_font(self):
        if self.font_path and os.path.exists(self.font_path):
            return self.font_path

        font_url = "https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap"
        async with self.session.get(font_url) as resp:
            if resp.status == 200:
                css = await resp.text()
                font_url = css.split("url(")[1].split(")")[0]

                async with self.session.get(font_url) as font_resp:
                    if font_resp.status == 200:
                        font_data = await font_resp.read()
                        with tempfile.NamedTemporaryFile(delete=False, suffix=".ttf") as temp_font:
                            temp_font.write(font_data)
                            self.font_path = temp_font.name
                        return self.font_path

        return None

    @commands.group()
    async def wordle(self, ctx):
        """Wordle game commands"""
        pass

    @wordle.command(name="start")
    async def wordle_start(self, ctx):
        """Start a new Wordle game."""
        if ctx.author.id in self.games:
            await ctx.send("You already have an active game!")
            return

        settings = await self.config.user(ctx.author).all()
        word = await self.get_random_word(settings['word_length'])
        if not word:
            await ctx.send("Failed to get a word. Please try again later.")
            return

        self.games[ctx.author.id] = {
            "word": word,
            "guesses": [],
            "tries": settings['max_tries'],
            "settings": settings
        }
        await ctx.send(f"New Wordle game started! You have {settings['max_tries']} tries to guess the {settings['word_length']}-letter word.")
        await self.send_wordle_image(ctx, self.games[ctx.author.id])

    @wordle.command(name="guess")
    async def wordle_guess(self, ctx, guess: str):
        """Make a guess in your active Wordle game."""
        if ctx.author.id not in self.games:
            await ctx.send("You don't have an active game! Start one with `!wordle start`")
            return

        game = self.games[ctx.author.id]
        guess = guess.upper()

        if len(guess) != len(game['word']):
            await ctx.send(f"Your guess must be a {len(game['word'])}-letter word!")
            return

        if game['settings']['hard_mode'] and len(game['guesses']) > 0:
            last_guess = game['guesses'][-1]
            for i, (last, current) in enumerate(zip(last_guess, guess)):
                if last == game['word'][i] and current != last:
                    await ctx.send(f"Hard mode: You must use the correct letter '{last}' in position {i+1}")
                    return

        game["guesses"].append(guess)
        game["tries"] -= 1

        if guess == game["word"]:
            await ctx.send("Congratulations! You've guessed the word!")
            await self.send_wordle_image(ctx, game)
            await self.update_stats(ctx.author, True, len(game['guesses']))
            del self.games[ctx.author.id]
        elif game["tries"] == 0:
            await ctx.send(f"Game over! The word was {game['word']}.")
            await self.send_wordle_image(ctx, game)
            await self.update_stats(ctx.author, False, len(game['guesses']))
            del self.games[ctx.author.id]
        else:
            await self.send_wordle_image(ctx, game)

    @wordle.command(name="settings")
    async def wordle_settings(self, ctx, setting: str, value: str):
        """Change your Wordle game settings."""
        valid_settings = {
            "word_length": (3, 12),
            "max_tries": (1, 20),
            "colorblind": ("true", "false"),
            "hard_mode": ("true", "false")
        }

        if setting not in valid_settings:
            await ctx.send(f"Invalid setting. Valid settings are: {', '.join(valid_settings.keys())}")
            return

        if setting in ("word_length", "max_tries"):
            try:
                value = int(value)
                if value < valid_settings[setting][0] or value > valid_settings[setting][1]:
                    raise ValueError
            except ValueError:
                await ctx.send(f"{setting} must be between {valid_settings[setting][0]} and {valid_settings[setting][1]}")
                return
        elif setting in ("colorblind", "hard_mode"):
            if value.lower() not in valid_settings[setting]:
                await ctx.send(f"{setting} must be either 'true' or 'false'")
                return
            value = value.lower() == "true"

        await self.config.user(ctx.author).set_raw(setting, value=value)
        await ctx.send(f"{setting} has been set to {value}")

    @wordle.command(name="stats")
    async def wordle_stats(self, ctx, user: discord.User = None):
        """View Wordle statistics for a user."""
        user = user or ctx.author
        stats = await self.config.stats.get_raw(str(user.id), default={})
        if not stats:
            await ctx.send(f"{user.name} hasn't played any Wordle games yet.")
            return

        games_played = stats.get("games_played", 0)
        games_won = stats.get("games_won", 0)
        win_percentage = (games_won / games_played) * 100 if games_played > 0 else 0
        average_guesses = stats.get("total_guesses", 0) / games_won if games_won > 0 else 0

        embed = discord.Embed(title=f"Wordle Stats for {user.name}", color=discord.Color.blue())
        embed.add_field(name="Games Played", value=games_played)
        embed.add_field(name="Games Won", value=games_won)
        embed.add_field(name="Win Percentage", value=f"{win_percentage:.2f}%")
        embed.add_field(name="Average Guesses", value=f"{average_guesses:.2f}")

        await ctx.send(embed=embed)

    @wordle.command(name="leaderboard")
    async def wordle_leaderboard(self, ctx):
        """View the Wordle leaderboard."""
        leaderboard = await self.config.leaderboard()
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

        embed = discord.Embed(title="Wordle Leaderboard", color=discord.Color.gold())
        for i, (user_id, score) in enumerate(sorted_leaderboard[:10], 1):
            user = self.bot.get_user(int(user_id))
            username = user.name if user else f"User {user_id}"
            embed.add_field(name=f"{i}. {username}", value=f"Score: {score}", inline=False)

        await ctx.send(embed=embed)

    async def send_wordle_image(self, ctx, game):
        image = await self.create_wordle_image(game)
        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='wordle.png'))

    async def create_wordle_image(self, game):
        word_length = len(game['word'])
        width, height = word_length * 60, game['settings']['max_tries'] * 60
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)

        font_path = await self.fetch_google_font()
        if not font_path:
            # Fallback to a system font if Google Font fails
            font = ImageFont.load_default()
        else:
            font = ImageFont.truetype(font_path, 36)

        colors = {
            'correct': 'green' if not game['settings']['colorblind'] else 'orange',
            'present': 'yellow' if not game['settings']['colorblind'] else 'blue',
            'absent': 'lightgray'
        }

        for i, guess in enumerate(game["guesses"]):
            for j, letter in enumerate(guess):
                color = colors['absent']
                if letter == game["word"][j]:
                    color = colors['correct']
                elif letter in game["word"]:
                    color = colors['present']

                draw.rectangle([j*60, i*60, (j+1)*60, (i+1)*60], fill=color, outline='black')
                draw.text((j*60+20, i*60+10), letter, fill='black', font=font)

        return image

    async def update_stats(self, user, won, guesses):
        async with self.config.stats.get_raw(str(user.id), default={}) as stats:
            stats["games_played"] = stats.get("games_played", 0) + 1
            if won:
                stats["games_won"] = stats.get("games_won", 0) + 1
                stats["total_guesses"] = stats.get("total_guesses", 0) + guesses

        async with self.config.leaderboard() as leaderboard:
            leaderboard[str(user.id)] = leaderboard.get(str(user.id), 0) + (10 if won else 1)
