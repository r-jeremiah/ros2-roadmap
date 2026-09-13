# Configuration file for the Sphinx documentation builder.

project = 'ROS 2 Roadmap'
copyright = '2026, Robotics Engineering Team'
author = 'Engineering Team'

# -- General configuration ------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# MyST settings for markdown enhancements
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# -- Options for HTML output ----------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']