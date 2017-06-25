# -*- coding: utf-8 -*-
from distutils.core import setup
import py2app

APP = ['gui.py']
APP_NAME = "Mozart Dice"
OPTIONS = {
	'iconfile': 'images/dice.icns',
	'resources': 'waves, images',
	'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Randomly compose a Mozart Song!",
        'CFBundleIdentifier': "com.mmontori1.MozartDice",
        'CFBundleVersion': "1.0",
        'CFBundleShortVersionString': "1.0",
        'NSHumanReadableCopyright': u"Copyright © 2017, Mariano Montori, All Rights Reserved"
    }
}

setup(
    app = APP,
    name = APP_NAME,
    options = {'py2app': OPTIONS},
)