#!/usr/bin/env python
from setuptools import setup

setup(
    name='publish_test',
    version='0.0.1',
    description='A test of publishing to PyPI using CircleCI on merge into master',
    author='Michael Overmeyer',
    author_email='test@example.com',

    packages=['publish_test'],
    test_suite='tests',

    classifiers=[],
    keywords='',
)
