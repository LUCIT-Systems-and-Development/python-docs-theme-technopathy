#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='python-docs-theme-technopathy',
    version='0.2.0',
    description='A full width sphinx template for github pages based on python-docs-theme',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Oliver Zehentleitner',
    url='https://about.me/oliver-zehentleitner',
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
    },

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
