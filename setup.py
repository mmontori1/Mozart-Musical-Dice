from distutils.core import setup
import py2app

OPTIONS = {
	# 'iconfile': 'treble.icns',
	'resources': 'waves, dice'
}

setup(
    app = ['gui.py'],
    name = 'Mozart Dice',
    options = {'py2app': OPTIONS},
)