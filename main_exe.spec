# -*- mode: python ; coding: utf-8 -*-
import sys
import os

# Function to collect necessary imports and data files for PySide2
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all hidden imports for PySide2
hiddenimports = collect_submodules('PySide2')
datas = collect_data_files('PySide2', subdir='Qt5')

# Define paths (adjust as necessary)
pathex = ['.', './src']  # Adjust paths based on your source structure

a = Analysis(
    ['main.py'],  # Your main Python script
    pathex=pathex,
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    exclude_binaries=False,
    name='BestTodo',  # Name of your application
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # GUI app (no terminal)
    disable_windowed_traceback=False,
    target_arch='x86_64',  # Set for 64-bit Windows
    codesign_identity=None,
    entitlements_file=None,
    icon='app-icon.ico'  # Path to your icon (Windows .ico file)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='BestTodo',
    distpath='./dist',  # Where the executable will be placed
    workpath='./build',  # Temporary build path
    workpath_clean=True,  # Automatically clean the workpath after the build
)
