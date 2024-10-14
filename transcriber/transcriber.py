import io
import discord
from redbot.core import commands, data_manager
import chat_exporter
from datetime import datetime
import os

class Transcriber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.base_path = data_manager.cog_data_path(self) / "transcripts"
        self.url_base = "https://ufw.prismbot.icu/assets/"  # Update this to your actual URL

    async def create_directory(self):
        os.makedirs(self.base_path, exist_ok=True)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def transcribe(self, ctx, limit: int = 100):
        """Create and save a transcript of the current channel"""
        await self.create_directory()

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

            # Save transcript to local file
            file_path = self.base_path / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(transcript)

            # Generate the URL for the saved transcript
            # Note: This URL won't work unless you set up your web server to serve files from this location
            transcript_url = f"{self.url_base}{filename}"

            await ctx.send(f"Transcript saved. Note: The following URL won't work unless properly configured: {transcript_url}")

            # Send as a file attachment
            file = discord.File(io.BytesIO(transcript.encode()), filename=filename)
            await ctx.send("Here's the transcript file:", file=file)

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
