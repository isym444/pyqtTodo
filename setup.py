from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['PyQt6'],
    'includes': ['sip', 'PyQt6.QtWidgets', 'PyQt6.QtGui', 'PyQt6.QtCore'],
    'plist': {
        'LSArchitecturePriority': ['arm64', 'x86_64'],  # どちらもサポート
    },
    'frameworks': ['/System/Library/Frameworks/Carbon.framework']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
