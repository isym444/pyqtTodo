# import sys
# import random
# from PySide6 import QtCore, QtWidgets, QtGui


# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)

#         self.button.clicked.connect(self.magic)

#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()

#     sys.exit(app.exec())


import sys
from PyQt6 import QtWidgets, uic, QtCore

app = QtWidgets.QApplication(sys.argv)


# lodding the ui file
window = uic.loadUi("mainwindow.ui")

# setting the ui elements
date_input = window.dateEdit
todo_input = window.lineEdit
add_button = window.pushButton
list_view = window.listWidget
menu_bar = window.menuBar
status_bar = window.statusBar
remove_button = window.pushButton_2


# setting the date to the current date
date_input.setDate(QtCore.QDate.currentDate())


def add_todo():
    date = date_input.date()
    todo = todo_input.text()
    list_view.addItem(f"{date.toString()} - {todo}")
    date_input.setDate(QtCore.QDate.currentDate())
    todo_input.clear()


def remove_todo():
    current_row = list_view.currentRow()
    if current_row != -1:
        list_view.takeItem(current_row)


# connecting the add button to the add_todo function
add_button.clicked.connect(add_todo)
remove_button.clicked.connect(remove_todo)

window.show()
app.exec()
