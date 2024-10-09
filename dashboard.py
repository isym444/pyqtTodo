import sys,os
from PyQt6 import QtWidgets, uic, QtCore
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
        
        self.details_window = DetailsWindow(self)
        
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
                self.details_window.show_details(todo, date, row[0])
    
    def closeEvent(self, event):
        self.conn.close()
        event.accept()