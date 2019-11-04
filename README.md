Python Docs Sphinx Theme (technopathy.club Edition)
===================================================

Forked from: https://github.com/python/python-docs-theme

This is the theme for the Python documentation!

Note that when adopting this theme, you're also borrowing an element of the
trust and credibility established by the CPython core developers over the
years. That's fine, and you're welcome to do so for other Python community
projects if you so choose, but please keep in mind that in doing so you're also
choosing to accept some of the responsibility for maintaining that collective
trust.

To use the theme, install it into your docs build environment via ``pip``:

``pip install python-docs-theme-technopathy``


In source/conf.py:

``
html_theme = 'python_docs_theme_technopathy'
html_context = {'github_repo_url': 'https://github.com/username/repo',
                'github_repo_name': project}
``

Howto: [https://www.technopathy.club/2019/11/03/use-python-sphinx-on-github-pages-with-html-and-an-indivdual-template/](https://www.technopathy.club/2019/11/03/use-python-sphinx-on-github-pages-with-html-and-an-indivdual-template/)