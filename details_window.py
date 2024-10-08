from PyQt6 import QtWidgets, uic

class DetailsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("anotherwindow.ui", self)
        
    def show_details(self, todo, date, description):
        self.findChild(QtWidgets.QLabel, 'todo_field').setText(todo)
        self.findChild(QtWidgets.QLabel, 'date_field').setText(date)
        self.findChild(QtWidgets.QLabel, 'description_field').setText(description)
        self.show()