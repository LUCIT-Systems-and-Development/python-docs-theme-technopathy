[![GitHub Release](https://img.shields.io/github/release/oliver-zehentleitner/python-docs-theme-technopathy.svg?label=github)](https://github.com/oliver-zehentleitner/python-docs-theme-technopathy/releases)
[![PyPi Release](https://img.shields.io/pypi/v/python-docs-theme-technopathy?color=blue)](https://pypi.org/project/python-docs-theme-technopathy/)
[![Downloads](https://pepy.tech/badge/python-docs-theme-technopathy)](https://pepy.tech/project/python-docs-theme-technopathy)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-docs-theme-technopathy.svg) 
![PyPI - Status](https://img.shields.io/pypi/status/python-docs-theme-technopathy.svg) 
[![Github](https://img.shields.io/badge/source-github-orange)](https://github.com/oliver-zehentleitner/python-docs-theme-technopathy)

# Python Docs Sphinx Theme (technopathy.club Edition)
Forked from https://github.com/python/python-docs-theme

## Installation

To use the theme, install it into your docs build environment via `pip`:
```
pip install python-docs-theme-technopathy
```
https://pypi.org/project/python-docs-theme-technopathy/

## Howto
https://www.technopathy.club/2019/11/03/use-python-sphinx-on-github-pages-with-html-and-an-indivdual-theme/

## Documentation
Settings for source/conf.py:
```
html_theme = 'python_docs_theme_technopathy'

html_context = {'github_user_name': 'your_user', 'github_repo_name': 'your_repository', 'project_name': project, 'show_github_download_btn': True}
```
Demo conf.py: https://github.com/oliver-zehentleitner/python-simplemachinesforum/blob/master/sphinx/source/conf.py

### Elements are inherited by:
- https://github.com/sphinx-doc/sphinx/tree/master/sphinx/themes/default
- https://github.com/sphinx-doc/sphinx/tree/master/sphinx/themes/basic
