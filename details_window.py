from PyQt6 import QtWidgets, uic
import sys,os
from ui_files.anotherwindow_ui import Ui_MainWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller sets this attribute and extracts files into _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class DetailsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # uic.loadUi(resource_path(os.path.join('ui_files', 'anotherwindow.ui')), self)
        self.setupUi(self)
        
    def show_details(self, todo, date, description):
        self.findChild(QtWidgets.QLabel, 'label_4').setText(todo)
        self.findChild(QtWidgets.QLabel, 'label_5').setText(date)
        self.findChild(QtWidgets.QLabel, 'label_6').setText(description)
        self.show()