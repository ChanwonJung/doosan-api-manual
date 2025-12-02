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

LATEST_VERSION = None

def _get_origin_branches():
    repo_root = os.path.dirname(__file__)
    try:
        out = subprocess.check_output(
            ["git", "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin"],
            cwd=repo_root,
            text=True,
        )
    except Exception:
        return []

    branches = []
    for line in out.splitlines():
        ref = line.strip()
        if not ref:
            continue

        # Convert "origin/GL013301" → "GL013301"
        parts = ref.split("/", 1)
        name = parts[1] if len(parts) == 2 else parts[0]

        branches.append(name)

    return branches

def _detect_latest_version(branches):
    """
    Detects the highest GL version based on numeric suffix.
    Example:
        branches = ["GL013300", "GL013301"]
        → returns "GL013301"
    """
    pattern = re.compile(r"^GL(\d+)$")
    candidates = []

    for name in branches:
        m = pattern.match(name)
        if m:
            num = int(m.group(1))
            candidates.append((num, name))

    if not candidates:
        return None

    candidates.sort()
    return candidates[-1][1]   # return highest-numbered GL branch

def _build_smv_branch_whitelist():

    global LATEST_VERSION
    branches = _get_origin_branches()

    # detect latest GL version automatically
    detected = _detect_latest_version(branches)
    if detected:
        LATEST_VERSION = detected
    else:
        # If no GL pattern exists:
        if branches:
            LATEST_VERSION = branches[0]
        else:
            # Emergency fallback when no git branch info available
            LATEST_VERSION = "GL013301"

    # If no branches found → allow only the detected latest version
    if not branches:
        return rf"^({re.escape(LATEST_VERSION)})$"

    # Allow ALL branches dynamically
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