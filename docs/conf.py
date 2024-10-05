exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", "venv"]
html_css_files = ["literals.css"]
extensions = ["myst_parser"]
templates_path = ["_templates"]

html_context = {
    "display_github": True,
    "github_user": "LeDeathAmongst",
    "github_repo": "StarCogs",
    "github_version": "main",
}

master_doc = "index"
html_theme = "furo"
source_suffix = ".md"
master_doc = "index"
exclude_patterns = []
add_function_parentheses = True

project = "StarCogs"
copyright = "2023 - Present | Star"
