#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, find_namespace_packages

with open("README.MD", "r") as fh:
    long_description = fh.read()

setup(name='form_cluster_test',
      version='0.1.0',
      description='Form Cluster Test Framework',
      long_description=long_description,
      author='zhuxu',
      author_email='zhuxu1993@outlook.com',
      url='https://www.python.org/',
      keywords='ga nn',
      packages=find_namespace_packages(include=['form_cluster_test']),
      include_package_data=True,
      install_requires=['xlrd', 'xlwt', 'xmltodict>=0.12'],
      python_requires='>=3'
      )
