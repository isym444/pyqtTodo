from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6'],  # PyQt6パッケージを含める
    'includes': ['PyQt6.QtWidgets', 'PyQt6.QtCore', 'PyQt6.QtGui'],
    'frameworks': [
        '$VIRTUAL_ENV/lib/python3.9/site-packages/PyQt6/Qt6/lib/QtWidgets.framework',
        '$VIRTUAL_ENV/lib/python3.9/site-packages/PyQt6/Qt6/lib/QtCore.framework',
        '$VIRTUAL_ENV/lib/python3.9/site-packages/PyQt6/Qt6/lib/QtGui.framework'
    ],
    'plist': {
        'CFBundleName': 'YourAppName',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'CFBundleIdentifier': 'com.yourname.yourappname',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
