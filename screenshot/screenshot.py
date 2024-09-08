<<<<<<< HEAD
from Star_Utils import Cog
=======
import io
import logging
import platform
import subprocess
import asyncio
>>>>>>> 845e6b14be2c7555d4a776d458d36009ed5af226
import discord
from redbot.core import commands, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Star_Utils import Cog
from Star_Utils.menus import Menu
from Star_Utils.settings import Settings
from Star_Utils.cogsutils import CogsUtils

log = logging.getLogger("star.screenshot")

class Screenshot(Cog, CogsUtils):
    """
    A cog for interactive browsing of websites through Discord.
    """

<<<<<<< HEAD

class Screenshot(Cog):

=======
>>>>>>> 845e6b14be2c7555d4a776d458d36009ed5af226
    def __init__(self, bot):
        self.bot = bot
        self.ensure_chrome_installed()
        self.old_browse = self.bot.get_command("screenshot")
        if self.old_browse:
            self.bot.remove_command("screenshot")

<<<<<<< HEAD
    @commands.hybrid_command(name='screenshot', with_app_command=True,
        description='Takes a screenshot of the provided website URL.')
    async def screenshot(self, ctx: commands.Context, url: str):
        await ctx.send('Taking screenshot...')
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        gecko_driver_path = '/usr/local/bin/geckodriver'
        driver = webdriver.Firefox(service=FirefoxService(executable_path=
            gecko_driver_path), options=options)
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.TAG_NAME, 'body')))
            screenshot_path = os.path.join(tempfile.gettempdir(),
                'screenshot.png')
            driver.save_screenshot(screenshot_path)
            await ctx.send(file=discord.File(screenshot_path))
        except TimeoutException:
            await ctx.send(
                'Failed to load the website within the timeout period.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
        finally:
            driver.quit()
=======
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

        # Initialize the WebDriver
        self.driver = None

    def cog_unload(self):
        if self.old_browse:
            try:
                self.bot.remove_command("screenshot")
            except Exception as e:
                log.error(f"Error removing screenshot command: {e}")
            self.bot.add_command(self.old_browse)

        # Quit the WebDriver
        if self.driver:
            self.driver.quit()

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

    def get_driver(self):
        if self.driver is None:
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

            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=chrome_options
            )
        return self.driver

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

        # Restrict interaction to the command invoker
        async def interaction_check(interaction: discord.Interaction) -> bool:
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("You are not allowed to use this interaction.", ephemeral=True)
                return False
            return True

        view.interaction_check = interaction_check

        async def button_callback(interaction: discord.Interaction):
            await interaction.response.defer()
            if interaction.data['custom_id'] == 'refresh':
                await self.update_embed_with_view(ctx, url, interaction.message)
            elif interaction.data['custom_id'] == 'scroll_down':
                await self.scroll_page(ctx, url, "down", interaction.message)
            elif interaction.data['custom_id'] == 'scroll_up':
                await self.scroll_page(ctx, url, "up", interaction.message)
            elif interaction.data['custom_id'] == 'click_element':
                await self.list_clickable_elements(ctx, url, interaction.message)
            elif interaction.data['custom_id'] == 'screenshot':
                await self.send_screenshot(ctx, url)

        for button in view.children:
            button.callback = button_callback

        # Initial embed with the first view of the website
        await self.update_embed_with_view(ctx, url, None, view)

    async def update_embed_with_view(self, ctx, url, message=None, view=None):
        async with ctx.typing():
            loop = asyncio.get_event_loop()
            site_name, screenshot = await loop.run_in_executor(None, self.take_screenshot, url)

            if screenshot is None:
                await ctx.send("An error occurred while updating the view.")
                return

            file_ = io.BytesIO(screenshot)
            file_.seek(0)
            file = discord.File(file_, "screenshot.png")
            file_.close()

            embed = discord.Embed(
                description=f"# [*{site_name}*]({url})", color=discord.Color.blue()
            )
            embed.set_image(url="attachment://screenshot.png")

            if message:
                await message.edit(embed=embed, attachments=[file], view=view)
            else:
                await ctx.send(embed=embed, file=file, view=view)

    async def scroll_page(self, ctx, url, direction, message):
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

            await message.edit(embed=embed, attachments=[file])

    async def list_clickable_elements(self, ctx, url, message):
        async with ctx.typing():
            loop = asyncio.get_event_loop()
            elements = await loop.run_in_executor(None, self.get_clickable_elements, url)

            if not elements:
                await ctx.send("No clickable elements found.")
                return

            view = discord.ui.View(timeout=180)
            for element in elements:
                button = discord.ui.Button(label=element['text'], style=discord.ButtonStyle.secondary, custom_id=element['selector'])
                button.callback = lambda inter: self.click_element(ctx, url, inter.custom_id, message)
                view.add_item(button)

            await ctx.send("Which Element?", view=view)

    async def click_element(self, ctx, url, selector, message):
        async with ctx.typing():
            loop = asyncio.get_event_loop()
            screenshot = await loop.run_in_executor(None, self.click_and_screenshot, url, selector)

            if screenshot is None:
                await ctx.send("An error occurred while clicking the element.")
                return

            file_ = io.BytesIO(screenshot)
            file_.seek(0)
            file = discord.File(file_, "screenshot.png")
            file_.close()

            embed = discord.Embed(
                description=f"Clicked element on [*{url}*]({url})", color=discord.Color.blue()
            )
            embed.set_image(url="attachment://screenshot.png")

            await message.edit(embed=embed, attachments=[file])

    async def send_screenshot(self, ctx, url):
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
        driver = self.get_driver()
        try:
            driver.get(url)
            self.handle_cookies(driver)
            site_name = driver.title
            screenshot = driver.get_screenshot_as_png()
            return site_name, screenshot
        except Exception as e:
            log.error(f"Error during screenshot: {e}")
            return None, None

    def scroll_and_screenshot(self, url, direction):
        driver = self.get_driver()
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

    def get_clickable_elements(self, url):
        driver = self.get_driver()
        try:
            driver.get(url)
            self.handle_cookies(driver)
            elements = driver.find_elements(By.CSS_SELECTOR, "a, button")
            clickable_elements = [{"text": e.text or e.get_attribute("href") or "Unnamed", "selector": e.get_attribute("outerHTML")} for e in elements]
            return clickable_elements
        except Exception as e:
            log.error(f"Error finding clickable elements: {e}")
            return []

    def click_and_screenshot(self, url, selector):
        driver = self.get_driver()
        try:
            driver.get(url)
            self.handle_cookies(driver)
            element = driver.find_element(By.CSS_SELECTOR, selector)
            element.click()
            screenshot = driver.get_screenshot_as_png()
            return screenshot
        except Exception as e:
            log.error(f"Error clicking element: {e}")
            return None

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
>>>>>>> 845e6b14be2c7555d4a776d458d36009ed5af226
