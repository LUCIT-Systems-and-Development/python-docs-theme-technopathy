#!/usr/bin/env python

import io

from setuptools import setup

# README into long description
with io.open('README.rst', encoding='utf-8') as readme_file:
    long_description = readme_file.read()


setup(
    name='python-docs-theme-technopathy',
    # Version is date based as year.month[.serial], where serial is used
    # if multiple releases are needed to address build failures.
    version='0.1.0',
    description='Sphinx template for github pages',
    long_description=long_description,
    author='Oliver Zehentleitner',
    url='https://about.me/oliver-zehentleitner',
    packages=['python_docs_theme_technopathy'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'python_docs_theme_technopathy = python_docs_theme_technopathy',
        ]
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
