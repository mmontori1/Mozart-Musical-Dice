# script for building the Mozart Dice application
# Usage:
#     python setup.py py2app

from distutils.core import setup
import py2app

OPTIONS = {
	# 'iconfile': 'treble.icns',
	'resources': 'waves'
}

setup(
    app = ['gui.py'],
    name = 'Mozart Dice',
    options = {'py2app': OPTIONS},
)