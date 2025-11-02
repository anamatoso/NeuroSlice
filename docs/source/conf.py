# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
""" Sphinx configuration for NeuroSlice documentation. """
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

PROJECT = 'NeuroSlice'
COPYRIGHT = '2025, Ana Matoso'
AUTHOR = 'Ana Matoso'
RELEASE = '1.0.1'
VERSION = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
]

# Extension settings
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

NAPOLEON_GOOGLE_STYLE = True
NAPOLEON_NUMPY_STYLE = True
NAPOLEON_USE_PARAM = True
NAPOLEON_USE_RTYPE = True

AUTOSUMMARY_GENERATE = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'nibabel': ('https://nipy.org/nibabel/', None),
}

templates_path = ['_templates']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

HTML_THEME = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False
}

html_static_path = ['_static']
templates_path = ['_templates']

# Custom CSS
html_css_files = [
    'custom.css',
]

HTML_SHOW_SOURCELINK = True
HTML_SHOW_SPHINX = False

# Output options
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
