.. image:: https://img.shields.io/pypi/dm/python-docs-theme-technopathy.svg?label=PyPI%20downloads&color=orange
   :alt: PyPi downloads

Python Docs Sphinx Theme (technopathy.club Edition)
===================================================
Forked from https://github.com/python/python-docs-theme

Installation
------------
To use the theme, install it into your docs build environment via ``pip``:

pip install python-docs-theme-technopathy

https://pypi.org/project/python-docs-theme-technopathy/

Howto
-----
https://www.technopathy.club/2019/11/03/use-python-sphinx-on-github-pages-with-html-and-an-indivdual-template/

Documentation
-------------
settings for source/conf.py:

html_theme = \'python_docs_theme_technopathy\'
html_context = \{\'github_user_name\': \'your_user\', \'github_repo_name\': \'your_repository\', \'project_name\': project\}


elements are inherited by:

https://github.com/sphinx-doc/sphinx/tree/master/sphinx/themes/default
https://github.com/sphinx-doc/sphinx/tree/master/sphinx/themes/basic
