# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "StarCogs"
copyright = "2023 - Present | Star"

# -- General configuration ---------------------------------------------------

extensions = ["myst_parser","sphinx_rtd_theme"]
templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store", ".venv", "venv"]

# -- Options for HTML output -------------------------------------------------

html_theme = "renku-sphinx-theme"
html_title = "Starfire Docs"

# GitHub integration
html_context = {
    "display_github": True,
    "github_user": "LeDeathAmongst",
    "github_repo": "StarCogs",
    "github_version": "main",
    "style": "literal.css"
#    "site_name": 'Starfire Docs',
#    "bot_name": 'Starfire',
#    "prefix": ',',
#    "invite_link": 'https://discord.com/oauth2/authorize?client_id=1275521742961508432',
#    "support_server": 'https://discord.gg/HXdan6NnfJ',
}

rst_epilog = """
.. |site_name| replace:: Starfire Docs
.. |bot_name| replace:: Starfire
.. |prefix| replace:: ,
.. |invite_link| replace:: https://discord.com/oauth2/authorize?client_id=1275521742961508432
.. |support_server| replace:: https://discord.gg/HXdan6NnfJ
"""
# Source file suffix
source_suffix = ".rst"

# Master document
master_doc = "index"
