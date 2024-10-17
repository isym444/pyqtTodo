from setuptools import setup

APP = ['main.py']  # Replace with your main Python script
DATA_FILES = []  # Add any additional files your app needs
OPTIONS = {
    'argv_emulation': True,  # Enable for macOS drag-and-drop
    'packages': ['PyQt6'],  # Include necessary packages
    'plist': {
        'CFBundleName': 'YourAppName',  # App name as displayed in macOS
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'CFBundleIdentifier': 'com.yourname.yourappname',  # Customize with your app's identifier
    },
}

setup(
    app=APP,
    name='YourAppName',  # Customize your app name
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
