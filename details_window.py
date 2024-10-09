from PyQt6 import QtWidgets, uic
import sys,os
from ui_files.anotherwindow_ui import Ui_MainWindow
from utils import resource_path


class DetailsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # uic.loadUi(resource_path(os.path.join('ui_files', 'anotherwindow.ui')), self)
        self.setupUi(self)
        
    def show_details(self, todo, date, description):
        self.findChild(QtWidgets.QLabel, 'todo_field').setText(todo)
        self.findChild(QtWidgets.QLabel, 'date_field').setText(date)
        self.findChild(QtWidgets.QLabel, 'description_field').setText(description)
        self.show()