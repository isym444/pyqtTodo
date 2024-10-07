from PyQt6 import QtWidgets, uic

class DetailsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("anotherwindow.ui", self)
        
    def show_details(self, todo, date, description):
        self.findChild(QtWidgets.QLabel, 'label_4').setText(todo)
        self.findChild(QtWidgets.QLabel, 'label_5').setText(date)
        self.findChild(QtWidgets.QLabel, 'label_6').setText(description)
        self.show()