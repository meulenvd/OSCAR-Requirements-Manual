# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# import os
# import re

# import wmo_sphinx_theme


# -- Project information -----------------------------------------------------

project = 'OSCAR Requirements Manual for PoC'
copyright = '2024, WMO'
author = 'WMO'

# author = 'World Meteorological Organization (WMO)'
# license = 'This work is licensed under a Creative Commons Attribution 4.0 International License'  # noqa
# copyright = '2021-2023, ' + author + ' ' + license

# The full version, including alpha/beta/rc tags
today_fmt = '%Y-%m-%d'
version = '0.1'
release = '0.1.1'
today = '2024-08-31'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windows-sidebar.html', 'searchbox.html'],
}

# html_theme = 'wmo_sphinx_theme'
# html_theme_path = wmo_sphinx_theme.get_html_theme_path()
# html_css_files = [
#    'wmo.css'
#]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
