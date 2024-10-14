import io
import discord
from redbot.core import commands
import chat_exporter
from datetime import datetime
import os

class Transcriber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.base_path = "/usr/share/assets"
        self.url_base = "https://ufw.prismbot.icu/assets/"

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def transcribe(self, ctx, limit: int = 100):
        """Create and save a transcript of the current channel"""
        try:
            transcript = await chat_exporter.export(
                channel=ctx.channel,
                limit=limit,
                bot=self.bot,
                tz_info="America/New_York",  # EST timezone
            )

            if transcript is None:
                await ctx.send("No messages to export.")
                return

            filename = f"transcript_{ctx.channel.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

            # Save transcript to local file server
            file_path = os.path.join(self.base_path, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(transcript)

            # Generate the URL for the saved transcript
            transcript_url = f"{self.url_base}{filename}"

            await ctx.send(f"Transcript saved and available at: {transcript_url}")

            # Optionally, also send as a file attachment
            file = discord.File(io.BytesIO(transcript.encode()), filename=filename)
            await ctx.send("Here's also a copy of the transcript:", file=file)

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
