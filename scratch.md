pyside6-rcc -o resources_rc.py resources.qrc
<!-- pyrcc6 -o resources_rc.py resources.qrc -->
pyinstaller --onefile --windowed --exclude PySide6 main.py