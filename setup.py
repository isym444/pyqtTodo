from setuptools import setup
import os

# Set ARCHFLAGS to build for Intel architecture
os.environ["ARCHFLAGS"] = "-arch x86_64"

APP = ['main.py']  # Replace with your main Python file
DATA_FILES = []  # Add any additional resources if needed
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6'],
    'includes': ['sip', 'PyQt6'],
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
