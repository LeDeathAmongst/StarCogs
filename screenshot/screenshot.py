import io
import logging
import platform
import subprocess
import asyncio
import discord
from redbot.core import commands
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Star_Utils.menus import Menu
from Star_Utils.settings import Settings
from Star_Utils.cogsutils import CogsUtils

log = logging.getLogger("star.screenshot")

class Screenshot(CogsUtils):
    """
    A cog for interactive browsing of websites through Discord.
    """

    def __init__(self, bot):
        super().__init__(bot=bot, cog=self)
        self.bot = bot
        self.ensure_chrome_installed()
        self.old_browse = self.bot.get_command("screenshot")
        if self.old_browse:
            self.bot.remove_command("screenshot")

        # Initialize settings
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=Config.GUILD,
            settings={
                "enabled": {
                    "path": ["enabled"],
                    "converter": bool,
                    "description": "Enable or disable the interactive browsing functionality.",
                    "usage": "enabled",
                }
            },
        )
        asyncio.create_task(self.settings.add_commands())

    def cog_unload(self):
        if self.old_browse:
            try:
                self.bot.remove_command("screenshot")
            except Exception as e:
                log.error(f"Error removing screenshot command: {e}")
            self.bot.add_command(self.old_screenshot)

    def ensure_chrome_installed(self):
        os_name = platform.system()

        if os_name == "Linux":
            try:
                subprocess.run(["google-chrome", "--version"], check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                log.info("Google Chrome not found. Installing...")
                subprocess.run([
                    "wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
                ], check=True)
                subprocess.run(["sudo", "apt", "install", "./google-chrome-stable_current_amd64.deb", "-y"], check=True)
                subprocess.run(["rm", "google-chrome-stable_current_amd64.deb"], check=True)

        elif os_name == "Darwin":
            try:
                subprocess.run(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"], check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                log.info("Google Chrome not found. Please install it manually from https://www.google.com/chrome/")

        elif os_name == "Windows":
            try:
                subprocess.run(["chrome", "--version"], check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                log.info("Google Chrome not found. Please install it manually from https://www.google.com/chrome/")

    @commands.bot_has_permissions(embed_links=True, attach_files=True)
    @commands.command(name="screenshot", aliases=["ss"])
    async def _screenshot(self, ctx: commands.Context, url: str):
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        # Create buttons for navigation and interaction
        view = discord.ui.View(timeout=180)
        view.add_item(discord.ui.Button(label="Refresh", style=discord.ButtonStyle.primary, custom_id="refresh"))
        view.add_item(discord.ui.Button(label="Scroll Down", style=discord.ButtonStyle.secondary, custom_id="scroll_down"))
        view.add_item(discord.ui.Button(label="Scroll Up", style=discord.ButtonStyle.secondary, custom_id="scroll_up"))
        view.add_item(discord.ui.Button(label="Click Element", style=discord.ButtonStyle.success, custom_id="click_element"))
        view.add_item(discord.ui.Button(label="Screenshot", style=discord.ButtonStyle.danger, custom_id="screenshot"))

        async def button_callback(interaction: discord.Interaction):
            await interaction.response.defer()
            if interaction.data['custom_id'] == 'refresh':
                await self.refresh_page(ctx, url)
            elif interaction.data['custom_id'] == 'scroll_down':
                await self.scroll_page(ctx, url, "down")
            elif interaction.data['custom_id'] == 'scroll_up':
                await self.scroll_page(ctx, url, "up")
            elif interaction.data['custom_id'] == 'click_element':
                await self.click_element(ctx, url)
            elif interaction.data['custom_id'] == 'screenshot':
                await self.take_screenshot_and_send(ctx, url)

        for button in view.children:
            button.callback = button_callback

        await ctx.send(f"Interactive browsing session started for {url}. Use the buttons below to interact.", view=view)

    async def refresh_page(self, ctx, url):
        await self.take_screenshot_and_send(ctx, url)

    async def scroll_page(self, ctx, url, direction):
        async with ctx.typing():
            loop = asyncio.get_event_loop()
            screenshot = await loop.run_in_executor(None, self.scroll_and_screenshot, url, direction)

            if screenshot is None:
                await ctx.send("An error occurred during scrolling.")
                return

            file_ = io.BytesIO(screenshot)
            file_.seek(0)
            file = discord.File(file_, "screenshot.png")
            file_.close()

            embed = discord.Embed(
                description=f"Scrolled {direction} on [*{url}*]({url})", color=discord.Color.blue()
            )
            embed.set_image(url="attachment://screenshot.png")

            await ctx.send(embed=embed, file=file)

    async def click_element(self, ctx, url):
        await ctx.send("Please specify the element to click (e.g., by CSS selector).")

    async def take_screenshot_and_send(self, ctx, url):
        async with ctx.typing():
            loop = asyncio.get_event_loop()
            site_name, screenshot = await loop.run_in_executor(None, self.take_screenshot, url)

            if screenshot is None:
                await ctx.send("An error occurred while taking the screenshot.")
                return

            file_ = io.BytesIO(screenshot)
            file_.seek(0)
            file = discord.File(file_, "screenshot.png")
            file_.close()

            embed = discord.Embed(
                description=f"# [*{site_name}*]({url})", color=discord.Color.blue()
            )
            embed.set_image(url="attachment://screenshot.png")

            await ctx.send(embed=embed, file=file)

    def take_screenshot(self, url: str):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-software-rasterizer")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=chrome_options
        )

        try:
            driver.get(url)
            self.handle_cookies(driver)
            site_name = driver.title
            screenshot = driver.get_screenshot_as_png()
            return site_name, screenshot
        except Exception as e:
            log.error(f"Error during screenshot: {e}")
            return None, None
        finally:
            driver.quit()

    def scroll_and_screenshot(self, url, direction):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-software-rasterizer")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=chrome_options
        )

        try:
            driver.get(url)
            self.handle_cookies(driver)
            if direction == "down":
                driver.execute_script("window.scrollBy(0, window.innerHeight);")
            elif direction == "up":
                driver.execute_script("window.scrollBy(0, -window.innerHeight);")
            screenshot = driver.get_screenshot_as_png()
            return screenshot
        except Exception as e:
            log.error(f"Error during scrolling: {e}")
            return None
        finally:
            driver.quit()

    def handle_cookies(self, driver):
        """
        Attempts to handle cookie consent prompts by clicking common "Accept All" buttons.
        """
        try:
            driver.execute_script("""
                document.cookie = 'cookieconsent_status=allow; path=/; domain=' + document.domain;
                localStorage.setItem('cookieconsent_status', 'allow');
            """)

            cookie_selectors = [
                "button[aria-label='Accept all']",
                "button[aria-label='Zustimmen']",
                "button[title='Accept all']",
                "button:contains('Accept all')",
                "button:contains('I agree')",
                "button:contains('Allow all')",
                "button:contains('Accept & continue')",
                "button:contains('Agree')",
                "button:contains('OK')",
                "button:contains('Got it')",
                "button:contains('Accept cookies')",
                "button:contains('Yes, I agree')",
                "button:contains('Continue')",
                "button:contains('Consent')",
                "button:contains('Accept and close')",
                "button:contains('Allow cookies')",
                "button:contains('Accept')",
                "button:contains('Acknowledge')",
                "button[aria-label='Agree to all']",
                "button[title='Agree']",
                "button[title='Accept']",
                "[id^='accept']",
                "[class*='accept']",
                "[class*='consent']",
                "[class*='agree']",
                "[class*='cookie']",
                "[id^='consent']",
                "[id^='agree']",
                "[data-testid='cookie-accept']",
                "#cookie-accept-button",
                ".cookie-consent-accept",
                "div.cookie-banner button",
                "div.consent-banner button",
            ]

            for selector in cookie_selectors:
                try:
                    WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    ).click()
                    log.info(f"Clicked cookie consent button with selector: {selector}")
                    break
                except Exception as e:
                    log.debug(f"Selector {selector} not found or clickable: {e}")
        except Exception as e:
            log.error(f"Error handling cookies: {e}")

async def setup(bot):
    old_screenshot = bot.get_command("screenshot")
    if old_screenshot:
        bot.remove_command(old_screenshot.name)

    cog = Screenshot(bot)
    await bot.add_cog(cog)
