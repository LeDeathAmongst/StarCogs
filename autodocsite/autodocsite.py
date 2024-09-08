from redbot.core import commands, Config
from redbot.core.bot import Red
import discord
import typing
import os
import shutil
import yaml
from io import BytesIO
from zipfile import ZIP_DEFLATED, ZipFile
from Star_Utils import Cog, Settings
from .formatter import CustomCmdFmt, IGNORE
from tabulate import tabulate
import functools

PRIVILEGE_LEVELS = ["user", "mod", "admin", "guildowner", "botowner"]

class AutoDocs(Cog):
    def __init__(self, bot: Red) -> None:
        super().__init__(bot=bot)

        self.config: Config = Config.get_conf(
            self,
            identifier=159096775493115543881107426517572342387,
            force_registration=True,
        )

        self.config.register_global(
            repo_dir="/root/StarCogs",
            custom_domain="docs.prismbot.icu",
            site_name="FuturoBot Documentation",
            theme_name="dracula",
            use_directory_urls=False,
            include_hidden=False,
            include_help=True,
            max_privilege_level="guildowner",
            min_privilege_level="user",
            replace_botname=True,
            extended_info=True,
            embedding_style=False
        )

        _settings: typing.Dict[str, typing.Dict[str, typing.Any]] = {
            "repo_dir": {
                "converter": str,
                "description": "Repository directory for documentation.",
            },
            "custom_domain": {
                "converter": str,
                "description": "Custom domain for documentation site.",
            },
            "site_name": {
                "converter": str,
                "description": "The name of the documentation site.",
            },
            "theme_name": {
                "converter": str,
                "description": "The theme name for the documentation site.",
            },
            "use_directory_urls": {
                "converter": bool,
                "description": "Whether to use directory URLs.",
            },
            "include_hidden": {
                "converter": bool,
                "description": "Include hidden commands in the documentation.",
            },
            "include_help": {
                "converter": bool,
                "description": "Include help text in the documentation.",
            },
            "max_privilege_level": {
                "converter": str,
                "description": "Maximum privilege level for commands.",
            },
            "min_privilege_level": {
                "converter": str,
                "description": "Minimum privilege level for commands.",
            },
            "replace_botname": {
                "converter": bool,
                "description": "Replace bot name placeholders in documentation.",
            },
            "extended_info": {
                "converter": bool,
                "description": "Include extended information in documentation.",
            },
            "embedding_style": {
                "converter": bool,
                "description": "Use embedding style in documentation.",
            },
        }

        self.settings: Settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GLOBAL,
            settings=_settings,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.setautodocs,
        )

    async def cog_load(self) -> None:
        await super().cog_load()

    async def cog_unload(self) -> None:
        await super().cog_unload()

    def generate_readme(self, cog: commands.Cog, prefix: str, replace_botname: bool,
                        extended_info: bool, include_hidden: bool, include_help: bool,
                        max_privilege_level: str, min_privilege_level: str = "user",
                        embedding_style: bool = False) -> str:
        columns = ["Name", "Text"]
        rows = []
        cog_name = cog.qualified_name
        docs = f"# {cog_name} Documentation\n\n"
        if include_help:
            cog_help = getattr(cog, 'cog_description', None)
            if cog_help:
                docs += f"{cog_help}\n\n"
                rows.append([f"{cog_name} cog description", cog_help])

        max_level_index = PRIVILEGE_LEVELS.index(max_privilege_level)
        min_level_index = PRIVILEGE_LEVELS.index(min_privilege_level)

        for cmd in cog.walk_commands():
            if cmd.hidden and not include_hidden:
                continue
            if PRIVILEGE_LEVELS.index(cmd.extras.get("privilege_level", "user")) > max_level_index:
                continue
            if PRIVILEGE_LEVELS.index(cmd.extras.get("privilege_level", "user")) < min_level_index:
                continue
            c = CustomCmdFmt(
                self.bot,
                cmd,
                prefix,
                replace_botname,
                extended_info,
                max_privilege_level,
                embedding_style,
                min_privilege_level,
            )
            doc = c.get_doc()
            if not doc:
                continue
            docs += doc
            rows.append([cmd.name, doc])

        table_str = tabulate(rows, headers=columns, tablefmt="pipe")
        docs += "\n\n" + table_str
        return docs

    @commands.is_owner()
    @commands.group()
    async def setautodocs(self, ctx: commands.Context) -> None:
        """Configure AutoDocs settings globally."""
        pass

    @setautodocs.command()
    async def generate(self, ctx: commands.Context):
        """Generate the documentation."""
        repo_dir = await self.config.repo_dir()
        docs_dir = os.path.join(repo_dir, "docs")

        if os.path.exists(docs_dir):
            shutil.rmtree(docs_dir)
        os.makedirs(docs_dir)

        prefix = (await self.bot.get_valid_prefixes(ctx.guild))[0].strip()

        for cog_name, cog in sorted(self.bot.cogs.items(), key=lambda item: item[0].lower()):
            docs = self.generate_readme(
                cog,
                prefix=prefix,
                replace_botname=await self.config.replace_botname(),
                extended_info=await self.config.extended_info(),
                include_hidden=await self.config.include_hidden(),
                include_help=await self.config.include_help(),
                max_privilege_level=await self.config.max_privilege_level(),
                min_privilege_level=await self.config.min_privilege_level(),
                embedding_style=await self.config.embedding_style(),
            )
            filename = os.path.join(docs_dir, f"{cog_name}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(docs)

        await ctx.send("Documentation generated.")

class AutoDocSite(Cog):
    def __init__(self, bot: Red) -> None:
        super().__init__(bot=bot)

        self.config: Config = Config.get_conf(
            self,
            identifier=159096775493115543881107426517572342387,
            force_registration=True,
        )

        self.config.register_global(
            repo_dir="/root/PBCogs",
            custom_domain="docs.prismbot.icu",
            site_name="FuturoBot Documentation",
            theme_name="dracula",
            use_directory_urls=False,
            include_hidden=False,
            include_help=True,
            max_privilege_level="guildowner",
            min_privilege_level="user",
            replace_botname=True,
            extended_info=True,
            embedding_style=False,
            invite_link="https://discord.com/oauth2/authorize?client_id=1230169850446479370&scope=bot+applications.commands&permissions=8",
            support_server="https://discord.gg/9f7WV6V8ud",
            custom_footer="Created by [Rosie](https://github.com/PBOwner) with <3"
        )

        _settings: typing.Dict[str, typing.Dict[str, typing.Any]] = {
            "repo_dir": {
                "converter": str,
                "description": "Repository directory for documentation.",
            },
            "custom_domain": {
                "converter": str,
                "description": "Custom domain for documentation site.",
            },
            "site_name": {
                "converter": str,
                "description": "The name of the documentation site.",
            },
            "theme_name": {
                "converter": str,
                "description": "The theme name for the documentation site.",
            },
            "use_directory_urls": {
                "converter": bool,
                "description": "Whether to use directory URLs.",
            },
            "include_hidden": {
                "converter": bool,
                "description": "Include hidden commands in the documentation.",
            },
            "include_help": {
                "converter": bool,
                "description": "Include help text in the documentation.",
            },
            "max_privilege_level": {
                "converter": str,
                "description": "Maximum privilege level for commands.",
            },
            "min_privilege_level": {
                "converter": str,
                "description": "Minimum privilege level for commands.",
            },
            "replace_botname": {
                "converter": bool,
                "description": "Replace bot name placeholders in documentation.",
            },
            "extended_info": {
                "converter": bool,
                "description": "Include extended information in documentation.",
            },
            "embedding_style": {
                "converter": bool,
                "description": "Use embedding style in documentation.",
            },
            "invite_link": {
                "converter": str,
                "description": "Invite link for the bot.",
            },
            "support_server": {
                "converter": str,
                "description": "Support server link.",
            },
            "custom_footer": {
                "converter": str,
                "description": "Custom footer for the documentation site.",
            },
        }

        self.settings: Settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GLOBAL,
            settings=_settings,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.setautodocsite,
        )

    async def cog_load(self) -> None:
        await super().cog_load()

    async def cog_unload(self) -> None:
        await super().cog_unload()

    @commands.is_owner()
    @commands.group()
    async def setautodocsite(self, ctx: commands.Context) -> None:
        """Configure AutoDocSite settings globally."""
        pass

    @setautodocsite.command()
    async def generate(self, ctx: commands.Context):
        """Generate the documentation site."""
        repo_dir = await self.config.repo_dir()
        docs_dir = os.path.join(repo_dir, "docs")
        mkdocs_config_path = os.path.join(repo_dir, "mkdocs.yml")

        if os.path.exists(docs_dir):
            shutil.rmtree(docs_dir)
        os.makedirs(docs_dir)

        with open(os.path.join(docs_dir, "CNAME"), "w") as f:
            f.write(await self.config.custom_domain())

        index_content = f"""
# Welcome to the Docs

Welcome to the official documentation site for **{await self.config.site_name()}**!
        """
        with open(os.path.join(docs_dir, "index.md"), "w") as f:
            f.write(index_content)

        prefix = (await self.bot.get_valid_prefixes(ctx.guild))[0].strip()
        for cog_name, cog in sorted(self.bot.cogs.items(), key=lambda item: item[0].lower()):
            docs = self.generate_readme(
                cog,
                prefix=prefix,
                replace_botname=await self.config.replace_botname(),
                extended_info=await self.config.extended_info(),
                include_hidden=await self.config.include_hidden(),
                include_help=await self.config.include_help(),
                max_privilege_level=await self.config.max_privilege_level(),
                min_privilege_level=await self.config.min_privilege_level(),
                embedding_style=await self.config.embedding_style(),
            )
            filename = os.path.join(docs_dir, f"{cog_name}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(docs)

        meta_config = {
            "site_name": await self.config.site_name(),
            "site_url": f"https://{await self.config.custom_domain()}/",
            "theme": {
                "name": await self.config.theme_name()
            },
            "use_directory_urls": await self.config.use_directory_urls(),
            "nav": [
                {"Home": "index.md"},
                {"Cogs": []}
            ],
            "extra": {
                "footer": await self.config.custom_footer()
            }
        }

        for cog_name, cog in sorted(self.bot.cogs.items(), key=lambda item: item[0].lower()):
            meta_config["nav"][1]["Cogs"].append({cog_name: f"{cog_name}.md"})

        with open(mkdocs_config_path, "w", encoding="utf-8") as f:
            f.write(yaml.dump(meta_config, default_flow_style=False))

        os.chdir(repo_dir)

        mkdocs_path = "/root/innova/bin/mkdocs"  # Replace with the actual path to mkdocs if needed

        os.system("git pull origin gh-pages")

        os.system(f"{mkdocs_path} build")
        os.system(f"{mkdocs_path} gh-deploy")

        await ctx.send(f"Documentation site has been generated and deployed to GitHub Pages.\nYou can view it here: {await self.config.custom_domain()}")
