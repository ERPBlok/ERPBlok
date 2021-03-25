#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for erpblok"""

from setuptools import setup, find_packages
import os

version = "0.1.0"
here = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(here, 'README.rst'), 'r', encoding='utf-8'
) as readme_file:
    readme = readme_file.read()

with open(
    os.path.join(here, 'CHANGELOG.rst'), 'r', encoding='utf-8'
) as changelog_file:
    changelog = changelog_file.read()

requirements = [
    'sqlalchemy',
    'anyblok',
    'anyblok-mixins',
    'psycopg2-binary',
    'anyblok_furetui',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='erpblok',
    version=version,
    description="A short description of the Anyblok based project",
    long_description=readme + '\n\n' + changelog,
    author="Your name",
    author_email='Your address email (eq. you@example.com)',
    url='https://github.com/Your github username/erpblok',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'erpblok=erpblok.erpblok:Erpblok',
            'erpblok-blok-manager=erpblok.blokmanager:BlokManager',
            'erpblok-project=erpblok.project:Project',
            'erpblok-compta=erpblok.compta:Compta',
         ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='erpblok',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
