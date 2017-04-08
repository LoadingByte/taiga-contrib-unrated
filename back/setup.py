#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from taiga_contrib_unrated import __version__ as version

setup(
    name = 'taiga-contrib-unrated',
    version = ':versiontools:taiga_contrib_unrated:',
    description = 'Taiga contrib plugin that extends Taiga to fit our needs at Unrated Film Industries.',
    long_description = 'Taiga contrib plugin that extends Taiga to fit our needs at Unrated Film Industries.',
    keywords = 'taiga, unrated, unratedfilmindustries',
    author = 'LoadingByte',
    author_email = 'kontakt@unratedfilmindustries.de',
    url = 'https://www.unratedfilmindustries.de',
    license = 'GPL',
    include_package_data = True,
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
