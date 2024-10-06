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
import sqlite3
from PyQt6.QtCore import QResource
import resources_rc

# images contained in the resources.qrc file
QResource.registerResource("resources.qrc")

app = QtWidgets.QApplication(sys.argv)

# creating a connection to the database
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS todos (date DATE, todo TEXT, description TEXT)")


# lodding the ui file
window = uic.loadUi("mainwindow.ui")
another_window = uic.loadUi("anotherwindow.ui")

# setting the ui elements
date_input = window.dateEdit
todo_input = window.lineEdit
description_input = window.plainTextEdit
add_button = window.pushButton
list_view = window.listWidget
menu_bar = window.menuBar
status_bar = window.statusBar
remove_button = window.pushButton_2


# setting the date to the current date
date_input.setDate(QtCore.QDate.currentDate())

# adding the todos from the database to the list view
cursor.execute("SELECT * FROM todos")
rows = cursor.fetchall()

for row in rows:
    list_view.addItem(f"{row[0]} - {row[1]}")

def add_todo():
    if todo_input.text() == "":
        return
    date = date_input.date()
    todo = todo_input.text()
    description = description_input.toPlainText()
    list_view.addItem(f"{date.toString()} - {todo}")
    cursor.execute("INSERT INTO todos VALUES (?, ?, ?)", (date.toString(), todo, description))
    conn.commit()   
    date_input.setDate(QtCore.QDate.currentDate())
    todo_input.clear()
    description_input.clear()
    cursor.execute("SELECT * FROM todos")
    global rows
    rows = cursor.fetchall()
    print(rows)


def remove_todo():
    current_row = list_view.currentRow()
    if current_row != -1 and current_row < len(rows):
        cursor.execute("DELETE FROM todos WHERE date = ? AND todo = ? AND description = ?", (rows[current_row]))
        conn.commit()
        list_view.takeItem(current_row)
        cursor.execute("SELECT * FROM todos")
        rows = cursor.fetchall()
        print(rows)


def show_details():
    current_row = list_view.currentRow()
    if current_row != -1:
        item_text = list_view.item(current_row).text()
        date, todo = item_text.split(" - ", 1)
        cursor.execute("SELECT description FROM todos WHERE date = ? AND todo = ?", (date, todo))
        row = cursor.fetchone()
        if row:
            # assuming label_4, label_5, label_6 exist in another_window.ui
            another_window.findChild(QtWidgets.QLabel, 'label_4').setText(todo)
            another_window.findChild(QtWidgets.QLabel, 'label_5').setText(date)
            another_window.findChild(QtWidgets.QLabel, 'label_6').setText(row[0])
            another_window.show()

# connecting the add button to the add_todo function
add_button.clicked.connect(add_todo)
remove_button.clicked.connect(remove_todo)
list_view.itemDoubleClicked.connect(show_details)


window.show()
app.exec()

# closing the connection to the database
conn.close()
