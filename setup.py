#!/usr/bin/env python

import io
from setuptools import setup

with io.open('README.md', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='python-docs-theme-technopathy',
    version='0.8.5',
    description='A responsive sphinx theme for github pages based on python-docs-theme',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Oliver Zehentleitner',
    url='https://www.lucit.tech',
    packages=['python_docs_theme_technopathy'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'python_docs_theme_technopathy = python_docs_theme_technopathy',
        ]
    },
    project_urls={
        'Source': 'https://github.com/oliver-zehentleitner/python-docs-theme-technopathy',
        'Howto': 'https://www.technopathy.club/2019/11/03/use-python-sphinx-on-github-pages-with-html-and-an-indivdual-template/',
        'Author': 'https://about.me/oliver-zehentleitner',
    },

    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python :: 3',
    ],
)
