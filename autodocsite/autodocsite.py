import os
import shutil
import logging
from io import BytesIO
from typing import List, Literal, Optional, Tuple
import yaml

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n, set_contextual_locales_from_guild

from .formatter import IGNORE, CustomCmdFmt

log = logging.getLogger("fb.fbcogs.autodocsite")
_ = Translator("AutoDocs", __file__)

# redgettext -D autodocs.py converters.py formatter.py
@cog_i18n(_)
class AutoDocSite(commands.Cog):
    """
    Automatically generate a documentation site for every cog in the bot.
    """

    def format_help_for_context(self, ctx):
        helpcmd = super().format_help_for_context(ctx)
        txt = _("{}\nCog Version: {}\nAuthor: {}").format(helpcmd, self.__version__, self.__author__)
        return txt

    async def red_delete_data_for_user(self, *, requester, user_id: int):
        """No data to delete"""

    def __init__(self, bot: Red, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    def generate_readme(
        self,
        cog: commands.Cog,
        prefix: str,
        replace_botname: bool,
        extended_info: bool,
        include_hidden: bool,
        include_help: bool,
        max_privilege_level: str,
        min_privilage_level: str = "user",
        embedding_style: bool = False,
    ) -> str:
        docs = ""
        cog_name = cog.qualified_name
        if include_help:
            helptxt = _("Help")
            docs += f"# {cog_name} {helptxt}\n\n"
            cog_help = cog.help if cog.help else None
            if not embedding_style and cog_help:
                cog_help = cog_help.replace("\n", "<br/>")
            if cog_help:
                docs += f"{cog_help}\n\n"

        for cmd in cog.walk_app_commands():
            c = CustomCmdFmt(
                self.bot,
                cmd,
                prefix,
                replace_botname,
                extended_info,
                max_privilege_level,
                embedding_style,
                min_privilage_level,
            )
            doc = c.get_doc()
            if not doc:
                continue
            docs += doc

        ignored = []
        for cmd in cog.walk_commands():
            if cmd.hidden and not include_hidden:
                continue
            c = CustomCmdFmt(
                self.bot,
                cmd,
                prefix,
                replace_botname,
                extended_info,
                max_privilege_level,
                embedding_style,
                min_privilage_level,
            )
            doc = c.get_doc()
            if doc is None:
                ignored.append(cmd.qualified_name)
            if not doc:
                continue
            skip = False
            for i in ignored:
                if i in cmd.qualified_name:
                    skip = True
            if skip:
                continue
            docs += doc
        return docs

    @commands.command()
    @commands.is_owner()
    async def gendocs(self, ctx: commands.Context):
        """
        Generate a documentation site for every cog in the bot.
        """
        await set_contextual_locales_from_guild(self.bot, ctx.guild)
        async with ctx.typing():
            repo_dir = "/root/PBCogs"  # Replace with the path to your GitHub repository
            docs_dir = os.path.join(repo_dir, "docs")
            mkdocs_config_path = os.path.join(repo_dir, "mkdocs.yml")

            if os.path.exists(docs_dir):
                shutil.rmtree(docs_dir)
            os.makedirs(docs_dir)

            # Create CNAME file for custom domain
            custom_domain = "docs.prismbot.icu"  # Replace with your custom domain
            with open(os.path.join(docs_dir, "CNAME"), "w") as f:
                f.write(custom_domain)

            # Create index.md file
            index_content = """
# Welcome to the Docs

Welcome to the official documentation site for **FuturoBot**! This site provides comprehensive information on how to use and configure the various features and commands available in the bot.

## Introduction

**FuturoBot** is a powerful and versatile bot designed to enhance your Discord server experience. With a wide range of features, including moderation tools, fun commands, and utility functions, **Your Bot Name** is the perfect addition to any server.

## Getting Started

To get started with **FuturoBot**, follow these simple steps:

1. **Invite the Bot**: Use the invite link to add the bot to your Discord server.
2. **Set Up Permissions**: Ensure the bot has the necessary permissions to function correctly.
3. **Configure the Bot**: Use the configuration commands to set up the bot according to your preferences.

For detailed instructions, refer to the [Getting Started Guide](getting_started.md).

## Commands

### General Commands

**FuturoBot** offers a variety of general commands to enhance your server experience. These commands include:

- `,help`: Displays a list of available commands.
- `,info bot`: Provides information about the bot.
- `,ping`: Checks the bot's response time.

### Moderation Commands

Moderation commands help you manage your server effectively. These commands include:

- `,ban [user] [reason]`: Bans a user from the server.
- `,kick [user] [reason]`: Kicks a user from the server.
- `,mute [user] [duration]`: Mutes a user for a specified duration.
- Theres a ton more, just take a look at the different features!
### Fun Commands

Add some fun to your server with these entertaining commands:

- `,joke`: Tells a random joke.
- `,slots`: Play some slots, using the bot's currency
- `,cah`: Play a game of Cards Against Humanity
- Theres a ton more, just take a look at the different features!

## Configuration

To configure **Your Bot Name**, use the following commands:

- `,prefix [prefix]`: Changes the command prefix.

## FAQ

### How do I invite the bot to my server?

Use the invite link provided [here](https://discord.com/oauth2/authorize?client_id=1230169850446479370&scope=bot+applications.commands&permissions=8) to add the bot to your server.

### How do I report a bug or request a feature?

To report a bug, please join the support server and create a ticket. To request a feature, use `,fr submit <feature>` where `<feature>` is the feature you desire.

For more frequently asked questions, refer to the [FAQ](faq.md) section.

## Support

If you need assistance or have any questions, please join our [Support Server](https://discord.gg/9f7WV6V8ud).

Thank you for using **FuturoBot**! We hope you enjoy all the features and functionality it has to offer.
            """
            with open(os.path.join(docs_dir, "index.md"), "w") as f:
                f.write(index_content)

            mkdocs_config = {
                "site_name": "FuturoBot Documentation",
                "site_url": f"https://{custom_domain}/",  # Use your custom domain
                "theme": {
                    "name": "material"
                },
                "use_directory_urls": False,
                "nav": [{"Home": "index.md"}]
            }

            prefix = (await self.bot.get_valid_prefixes(ctx.guild))[0].strip()

            for cog_name, cog in self.bot.cogs.items():
                if cog_name in IGNORE:
                    continue
                docs = self.generate_readme(
                    cog,
                    prefix=prefix,
                    replace_botname=True,
                    extended_info=True,
                    include_hidden=False,
                    include_help=True,
                    max_privilege_level="botowner",
                )
                filename = os.path.join(docs_dir, f"{cog_name}.md")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(docs)
                mkdocs_config["nav"].append({cog_name: f"{cog_name}.md"})

            with open(mkdocs_config_path, "w", encoding="utf-8") as f:
                f.write(yaml.dump(mkdocs_config, default_flow_style=False))

            # Change to the repository directory
            os.chdir(repo_dir)

            mkdocs_path = "/root/fb/bin/mkdocs"  # Replace with the actual path to mkdocs if needed
            os.system(f"{mkdocs_path} build")
            os.system(f"{mkdocs_path} gh-deploy")

            site_url = f"https://{custom_domain}/"
            await ctx.send(f"Documentation site has been generated and deployed to GitHub Pages.\nYou can view it here: {site_url}")
