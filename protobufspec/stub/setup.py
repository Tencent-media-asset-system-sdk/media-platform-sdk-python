# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages
from setuptools import setup

if sys.version_info < (3, 6):
    raise RuntimeError("It requires Python 3.6+")

name = "trpc_media_aivideoprocess"
version = "0.1.0"
packages = find_packages()

setup(
    name=name,
    version=version,
    packages=packages,
    author='',
    author_email='',
    maintainer='',
    maintainer_email='',
    url='',
    license='',
    description='stub package',
    package_data={'': ['*.proto']},

)
