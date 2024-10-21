# -*- mode: python ; coding: utf-8 -*-
import sys
import os
import glob

# Function to collect all files in ui_files directory
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect necessary hidden imports and data files for PyQt6
hiddenimports = collect_submodules('PyQt6')
datas = collect_data_files('PyQt6', subdir='Qt6')

a = Analysis(
    ['main.py'],  # Your main Python script
    pathex=[],
    binaries=[],
    datas=datas,  # Include the collected data files
    hiddenimports=hiddenimports,  # Include the hidden imports
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6'],
    noarchive=False,
    optimize=0,
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
    name='main',  # App name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Suppress console (equivalent to --windowed)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    osx_bundle_identifier='com.example.myapp',  # macOS bundle identifier
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='main'  # Name for the collected output
)
