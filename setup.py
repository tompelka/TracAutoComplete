#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

PACKAGE = 'autocomplete'
VERSION = '0.0.1'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Switch complete filed for ticket to 100% when ticket is closed.',
    author="Tomas Pelka",
    license='GPL',
    url='https://github.com/tompelka/TracAutoComplete',
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {'trac.plugins': ['autocomplete = autocomplete']},
    zip_safe = True
)
