import sys,os
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtCore import Qt
import sqlite3
from details_window import DetailsWindow
from ui_files.mainwindow_ui import Ui_MainWindow
from utils import resource_path


basedir = os.path.dirname(__file__)

class Dashboard(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi(resource_path(os.path.join('ui_files', 'mainwindow.ui')), self)
        self.setupUi(self)
        self.conn, self.cursor = self.init_db()
        
        self.date_input = self.dateEdit
        self.todo_input = self.lineEdit
        self.description_input = self.plainTextEdit
        self.add_button = self.pushButton
        self.list_view = self.listWidget
        self.remove_button = self.pushButton_2
        
        self.date_input.setDate(QtCore.QDate.currentDate())
        
        self.load_todos()
        self.add_button.clicked.connect(self.add_todo)
        self.remove_button.clicked.connect(self.remove_todo)
        self.list_view.itemDoubleClicked.connect(self.show_details)
        
        self.details_window = [] #array of DetailsWindow(not inforced)

        #press enter to add todo
        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.handle_enter_pressed)

        #Shift + Eneter to new line in the description field
        self.description_input.installEventFilter(self)

    # event of Shfit + Enter to new line in the description field
    def eventFilter(self, obj, event):
        if obj == self.description_input and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Return and not event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
                # press Enter to add todo
                self.handle_enter_pressed()
                return True
            elif event.key() == Qt.Key.Key_Return and event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
                # press Shift + Enter to new line in the description field
                cursor = self.description_input.textCursor()
                cursor.insertText("\n")
                return True
        return super().eventFilter(obj, event)

    # event of Enter key to add todo
    def handle_enter_pressed(self):
        if self.todo_input.text():
            self.add_todo()
        
    def init_db(self):
        db_path = resource_path('todo.db')
        if not os.path.exists(db_path):
            print("Database does not exist. It will be created.")
        else:
            print("Database found at:", db_path)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS todos (date DATE, todo TEXT, description TEXT)")
        return conn, cursor
    
    def load_todos(self):
        self.cursor.execute("SELECT * FROM todos")
        self.rows = self.cursor.fetchall()
        for row in self.rows:
            self.list_view.addItem(f"{row[0]} - {row[1]}")
    
    def add_todo(self):
        if self.todo_input.text() == "":
            return
        
        date = self.date_input.date()
        todo = self.todo_input.text()
        description = self.description_input.toPlainText()
        self.list_view.addItem(f"{date.toString()} - {todo}")
        
        self.cursor.execute("INSERT INTO todos VALUES (?, ?, ?)", (date.toString(), todo, description))
        self.conn.commit()
        
        self.date_input.setDate(QtCore.QDate.currentDate())
        self.todo_input.clear()
        self.description_input.clear()
        
        self.refresh_rows()
    
    def remove_todo(self):
        current_row = self.list_view.currentRow()
        if current_row != -1 and current_row < len(self.rows):
            self.cursor.execute("DELETE FROM todos WHERE date = ? AND todo = ? AND description = ?", self.rows[current_row])
            self.conn.commit()
            self.list_view.takeItem(current_row)
            self.refresh_rows()
    
    def refresh_rows(self):
        self.cursor.execute("SELECT * FROM todos")
        self.rows = self.cursor.fetchall()
    
    def show_details(self):
        current_row = self.list_view.currentRow()
        if current_row != -1:
            item_text = self.list_view.item(current_row).text()
            date, todo = item_text.split(" - ", 1)
            self.cursor.execute("SELECT description FROM todos WHERE date = ? AND todo = ?", (date, todo))
            row = self.cursor.fetchone()
            if row:
                print(self.details_window)
                d_window = DetailsWindow() #creates detailWindow
                d_window.show_details(todo,date,row[0])
                d_window.on_closed.connect(self.closed_detail_window) # connects on_closed with function
                self.details_window.append(d_window) #appends detailWindow to currectly opened array of detailWindows
                print(self.details_window)
    
    def closeEvent(self, event):
        self.conn.close()
        event.accept()

    def closed_detail_window(self,window):
        if window in self.details_window: #if found in array of instanced detailWindow
            self.details_window.remove(window) # then remove window