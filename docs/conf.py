"""Documentation-only build: no runtime imports, datasets, weights, or GPU."""
project = "DeepWonder3D user guide"
author = "Neurallabware"
copyright = "2026, Neurallabware"
extensions = ["myst_parser", "sphinx.ext.mathjax"]
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "furo"
html_title = project
myst_enable_extensions = ["colon_fence", "deflist"]
html_theme_options = {
    "source_repository": "https://github.com/Neurallabware/DeepWonder3D/",
    "source_branch": "main",
    "source_directory": "docs/",
}
