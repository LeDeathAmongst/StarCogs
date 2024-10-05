# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "StarCogs"
copyright = "2023 - Present | Star"

# -- General configuration ---------------------------------------------------

extensions = ["myst_parser","sphinx_rtd_theme"]
templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store", ".venv", "venv"]

# -- Options for HTML output -------------------------------------------------

html_theme = "topos-theme"

# GitHub integration
html_context = {
    "display_github": True,
    "github_user": "LeDeathAmongst",
    "github_repo": "StarCogs",
    "github_version": "main",
}

# Source file suffix
source_suffix = ".rst"

# Master document
master_doc = "index"
