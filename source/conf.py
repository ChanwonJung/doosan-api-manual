# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Doosan Robotics API Manual'
copyright = '2025, Doosan Robotics'
author = 'Doosan Robotics'
version = '1.33.1'
release = '1.33.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_multiversion",
    "sphinx.ext.githubpages",
]

import os
import re
import subprocess

def _build_smv_branch_whitelist():
    """
    Dynamically include ALL branches detected by git.
    No filtering.
    """
    repo_root = os.path.dirname(__file__)

    try:
        # List ALL local branches
        out = subprocess.check_output(
            ["git", "branch", "--format", "%(refname:short)"],
            cwd=repo_root,
            text=True,
        )
    except Exception:
        # If git unavailable (CI with shallow clone), fallback to main only
        return r"^(main)$"

    branches = []
    for line in out.splitlines():
        name = line.strip()
        if not name:
            continue
        branches.append(name)   # include EVERYTHING

    if not branches:
        return r"^(main)$"

    escaped = [re.escape(b) for b in branches]
    regex = r"^(" + "|".join(escaped) + r")$"
    return regex

# Override whitelist dynamically
smv_branch_whitelist = _build_smv_branch_whitelist()

templates_path = ['_templates']
exclude_patterns = ['_build', '_site', 'Thumbs.db', '.DS_Store']

rst_prolog = """
.. |br| raw:: html

   <br />
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# Add custom CSS
html_css_files = ['manual.css']

# Change doc title
html_title = 'Doosan Robotics API Manual Guide v1.33.1'
html_logo = 'tutorials/images/etc/Doosan_logo.png' # logo
# html_favicon = '_static/favicon.ico'

html_sidebars = {
    '**': [
        'localtoc.html',
        'relations.html',
        'searchbox.html',
        'versions.html',
    ],
}

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'titles_only': False,
}