# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "Starfire Documentations"
copyright = "2023 - Present | Star"

# -- General configuration ---------------------------------------------------

extensions = ["myst_parser","sphinx_rtd_theme"]
templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store", ".venv", "venv"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphyinx_theme"
html_title = "Starfire Docs"

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'includehidden': False,
    'titles_only': False,
    "display_github": True,
    "github_user": "LeDeathAmongst",
    "github_repo": "StarCogs",
    "github_version": "master",
    "description": "Starfire Documentations site"
}

html_context = {
    "style": ""
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
source_suffix = ".md"

# Master document
master_doc = "index"
