#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='playmobile.interfaces',
      version='0.1dev',
      description='Mobile Device management',
      author='Infrae',
      author_email='info@infrae.com',
      url='infrae.com',
      packages=find_packages('src'),
      install_requires=[
        'zope.interface',
        'zope.schema',
      ],
     )
