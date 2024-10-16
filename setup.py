from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6'],
    'includes': ['sip', 'PyQt6.QtWidgets', 'PyQt6.QtGui', 'PyQt6.QtCore'],
    'plist': {
        'LSArchitecturePriority': ['x86_64', 'arm64'],  # Universal対応に設定（x86_64とarm64の順に優先）
    },
    'arch': 'universal2',  # Universal2バイナリの生成を指定
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)