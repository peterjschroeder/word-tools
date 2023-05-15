#!/usr/bin/env python3

from distutils.core import setup
from setuptools import setup, find_packages

setup(
        name='word-tools', 
        version='0.1', 
        description='Word tools', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/world-tools',
        scripts=['rhyme', 'synonym'],
        install_requires=['git+https://github.com/peterjschroeder/python-abbreviate.git']
)

