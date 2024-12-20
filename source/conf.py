# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Obsidian Demo'
copyright = '2024, Anton Shiryaev'
author = 'Anton Shiryaev'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
]

source_suffix = {
   '.rst': 'restructuredtext',
   '.md': 'markdown',
}

myst_enable_extensions = [
    "dollarmath",  # Включает поддержку формул в двух долларах
]

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"


mermaid_params = [
   '--theme', 'forest',  # Устанавливает тему для диаграмм
   '--width', '100%',    # Устанавливает ширину диаграмм
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
