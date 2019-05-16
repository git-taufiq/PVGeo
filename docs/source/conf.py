# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shutil
import faulthandler
faulthandler.enable()

# Add PVGeo to the path
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(path)
sys.path.insert(0, path)
sys.path.insert(0, '/Users/bane/Documents/OpenGeoVis/Software/gendocs/')


# Mock the paraview module to build pvmacros docs
import mock

MOCK_MODULES = ['paraview', 'paraview.simple', 'discretize', 'pyproj']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()
autodoc_mock_imports = ['paraview']


# # Automattically generat source pages:
# os.system('python ./make_files.py')

import PVGeo, pvmacros # for documenting
from gendocs import Generator

append_material = """

.. toctree::
   :maxdepth: 2
   :caption: Examples
   :hidden:

   about-examples.rst
   examples/index

"""

extra = """

.. toctree::
   :maxdepth: 2
   :caption: Development Guide
   :hidden:

   dev-guide/contributing
   dev-guide/repo-structure
   dev-guide/templates
   dev-guide/snippets/index
   dev-guide/resources

"""

# Automatically generate documentaion pages
Generator().DocumentPackages([PVGeo, pvmacros],
            index_base='../index_base.rst',
            showprivate=True,
            notify=False,
            intro_pages=['overview/why-pvgeo',
                         'overview/getting-started',
                         'overview/featured',
                         'overview/agu-2018',
                        ],
            append_material=append_material,
            extra=extra,
            )

import pyvista
import numpy as np
# Manage errors
pyvista.set_error_output_file('errors.txt')
# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True # Not necessary - simply an insurance policy
# Preferred plotting style for documentation
pyvista.set_plot_theme('document')


# -- Project information -----------------------------------------------------

project = 'PVGeo'
copyright = u'2018-2019, Bane Sullivan, http:://banesullivan.com'
author = 'Bane Sullivan'
html_show_copyright = False
html_show_sphinx = False

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    'sphinxcontrib.napoleon',
    'sphinx_copybutton',
    'sphinx_gallery.gen_gallery'
]

linkcheck_retries = 3
linkcheck_timeout = 500

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'canonical_url': 'http://docs.pvgeo.org/',
    'analytics_id': 'UA-115959679-6',
    'display_version': False,

}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PVGeoDoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PVGeo.tex', 'PVGeo Documentation',
     'Bane Sullivan', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pvgeo', 'PVGeo Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PVGeo', 'PVGeo Documentation',
     author, 'PVGeo', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True



# -- Sphinx Gallery Options
from sphinx_gallery.sorting import FileNameSortKey
# thumb_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'PVGeo_icon_horiz.png')
sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": [
        "../../examples/",
    ],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Patter to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": False,
    # Modules for which function level galleries are created.  In
    "doc_module": "PVGeo",
    "image_scrapers": (pyvista.Scraper(), 'matplotlib'),
    "thumbnail_size": (350, 350),
    # 'default_thumb_file': thumb_path,
}


def setup(app):
    app.add_stylesheet("style.css")
    app.add_stylesheet("copybutton.css")