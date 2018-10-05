#!/usr/bin/env python
import os
import sys
from setuptools import setup
from setuptools.command.install import install

VERSION = "0.0.1"


class VerifyVersionCommand(install):
    # https://circleci.com/blog/continuously-deploying-python-packages-to-pypi-with-circleci/
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG').strip('v')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name='publish_test',
    version=VERSION,
    description='A test of publishing to PyPI using CircleCI on merge into master',
    author='Michael Overmeyer',
    author_email='test@example.com',

    packages=['publish_test'],
    test_suite='tests',

    classifiers=[],
    keywords='',
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
