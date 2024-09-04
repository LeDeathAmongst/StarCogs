from Star_Utils import Cog
from redbot.core import commands
from redbot.core.bot import Red
import discord
import re

class DynamicPrefix(Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Ignore messages sent by bots or without content
        if message.author.bot or not message.content:
            return

        # Define the dynamic prefix pattern
        dynamic_prefix = r'\[p\]'

        # Check if the message contains the dynamic prefix
        if re.search(dynamic_prefix, message.content):
            # Get the bot's current prefix
            prefixes = await self.bot.get_prefix(message)
            if not prefixes:
                return  # No prefix found; this shouldn't happen, but just in case

            # Replace [p] with the first available prefix
            new_content = re.sub(dynamic_prefix, prefixes[0], message.content, count=1)

            # Create a new message object with the updated content
            # Instead of creating a completely new object, we modify the content temporarily
            original_content = message.content
            message.content = new_content

            try:
                # Process the command with the updated message content
                await self.bot.process_commands(message)
            finally:
                # Restore the original content to avoid side effects
                message.content = original_content
