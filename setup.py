#!/usr/bin/env python

from setuptools import setup


# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

# get __version__
import re
PACKAGE_NAME = 'suntime'
version_line = open(path.join(this_directory, PACKAGE_NAME, 'version.py'), "rt").read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)

setup(name='suntime-yasirroni',
      version=__version__,
      description='Simple sunset and sunrise time calculation python library',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Krzysztof Stopa',
      url='https://github.com/yasirroni/suntime/tree/optimize',
      copyright='Copyright 2019 SatAgro',
      license='LGPLv3',
      packages=['suntime'],
      install_requires=['python-dateutil']
)
