# script for building the Mozart Dice application
# Usage:
#     python setup.py py2app

from distutils.core import setup
import py2app

setup(
    app=['run.py'],
)