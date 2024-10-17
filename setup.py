from setuptools import setup

APP = ['main.py']  # Replace with the main entry point of your PyQt6 app
DATA_FILES = []  # Any additional data files you want to include
OPTIONS = {
    'argv_emulation': True,  # Helps with file handling in GUI apps
    'packages': ['PyQt6'],  # Include necessary packages like PyQt6
    'iconfile': 'app_icon.icns',  # Optional: specify the path to your app icon
    'plist': {
        'CFBundleName': 'YourAppName',  # Replace with your app name
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'CFBundleIdentifier': 'com.yourname.yourappname',  # Replace with your app identifier
    },
}

setup(
    app=APP,
    name='YourAppName',  # Replace with your app name
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
