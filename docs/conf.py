# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "Starfire Documentations"
copyright = "2023 - Present | Star"

# -- General configuration ---------------------------------------------------

extensions = ["myst_parser","sphinx_rtd_theme"]
templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store", ".venv", "venv"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_title = "Starfire Docs"

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "navbar_align": "content",
    "primary_sidebar_end": ["sidebar-ethical-ads"],
    "article_footer_items": ["contentinfo", "last-updated", "edit-this-page"],
    "navigation_with_keys": True,
    "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_links": [
        {"name": "Home", "url": "index"},
        {"name": "Features", "url": "features"},
        {"name": "Support", "url": "support"},
    ],
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
