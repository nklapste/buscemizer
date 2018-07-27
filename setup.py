#!/usr/bin/python
# -*- coding: utf-8 -*-

"""setup.py for buscemizer"""

import codecs
import re
import sys
import os
from setuptools import setup, find_packages
from setuptools.command.test import test


def find_version(*file_paths):
    with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *file_paths), 'r') as fp:
        version_file = fp.read()
    m = re.search(r"^__version__ = \((\d+), ?(\d+), ?(\d+)\)", version_file, re.M)
    if m:
        return "{}.{}.{}".format(*m.groups())
    raise RuntimeError("Unable to find a valid version")


NAME = "buscemizer"
VERSION = find_version("buscemizer", "__init__.py")
DESCRIPTION = "Add Steve Buscemi's beautiful facial features to facial photos!"


class Pylint(test):
    def run_tests(self):
        from pylint.lint import Run
        errno = Run([NAME, "--persistent", "y", "--rcfile", ".pylintrc"])


class PyTest(test):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = "-v --cov={}".format(NAME)

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme(),
    packages=find_packages(exclude=["test"]),
    package_data={
        "": ["README.rst"],
        "buscemizer": ["images/*.png"]
    },
    entry_points={
        "console_scripts": [
            "buscemizer = buscemizer.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=[
        "face-recognition>=1.2.2,<2.0.0",
        "pillow>=5.2.0,<6.0.0",
        "numpy>=1.15.0,<2.0.0"
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-timeout",
        "pylint>=1.9.1,<2.0.0",
    ],
    extras_require={
        "docs": [
            "sphinx>=1.7.5,<2.0.0",
            "sphinx_rtd_theme>=0.3.1,<1.0.0",
            "sphinx-autodoc-typehints>=1.3.0,<2.0.0",
            "sphinx-argparse>=0.2.2,<1.0.0",
        ]
    },
    cmdclass={"test": PyTest, "lint": Pylint},
)
