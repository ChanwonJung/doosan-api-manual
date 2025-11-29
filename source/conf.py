# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Doosan Robotics API Manual'
copyright = '2025, Doosan Robotics'
author = 'Doosan Robotics'
version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
]

templates_path = ['_templates']
exclude_patterns = []

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
html_title = 'Doosan Robotics API Manual Guide v2.0'
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