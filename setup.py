#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

NAME = 'django_currency_field'
VERSION = '0.1.0'


base_dir = os.path.dirname(__file__)

install_requires = [
	'Django >= 3.0.1'
]

setup(
	name=NAME,
	version=VERSION,
	description='A Precision Bigint model field that avoids floats & decimals',
	author='Daniel Bernal',
	author_email='d@contemporary.io',
	package_dir={'': '.'},
	packages=find_packages(where='.', exclude=[]),
	install_requires=install_requires,
	python_requires='>=3.6',
	keywords=['django', 'currency', 'models', 'financial'],
)
