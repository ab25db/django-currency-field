#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

NAME = 'django_currency_field'
VERSION = '0.1.2'


base_dir = os.path.dirname(__file__)

install_requires = [
	'Django >= 3.0.1'
]
with open("README.md", "r") as fh:
	long_description = fh.read()


setup(
	name=NAME,
	version=VERSION,
	description='A Precision Bigint model field that avoids floats & decimals',
	long_description=long_description,
	long_description_content_type="text/markdown",
	author='Daniel Bernal',
	author_email='d@contemporary.io',
	url='https://github.com/ab25db/django-currency-field',
	package_dir={'': 'src'},
	packages=find_packages(where='src', exclude=[]),
	install_requires=install_requires,
	python_requires='>=3.6',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	keywords=['django', 'currency', 'models', 'financial'],
)
