#!/usr/bin/env python

from setuptools import setup, find_packages
import os

VERSION='1.0'

setup(name='mobi.interfaces',
      version=VERSION,
      description='Mobile libs interfaces package',
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      author='Antonin Amand at Infrae',
      author_email='info@infrae.com',
      url='http://infrae.com/',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['mobi'],
      install_requires=[
        'zope.interface',
        'zope.schema',
      ],
     )
