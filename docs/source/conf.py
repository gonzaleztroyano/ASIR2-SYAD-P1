# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Proyecto Seguridad y Alta Disponibilidad - Trimestre 1'
copyright = '2021, Pablo González, CC BY 2.5 ES'
author = 'Pablo González Troyano - 2º ASIR - IES Villablanca'

release = '1.1'
version = '1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Modificar el FAVICON -- 
html_favicon = 'https://carpet4you.site/images/carpet_yellowline_32.png'

# -- Quitar las flechitas entre las páginas -- 
html_theme_options = {
    'prev_next_buttons_location': 'none',

}