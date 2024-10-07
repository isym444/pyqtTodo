# N.B. run with: python -m unittest tests.main_screen_tests
import unittest
from unittest.mock import patch
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
import os
import sqlite3
import sys

# Import app
import main


class TestTodoApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the QApplication
        cls.app = QApplication(sys.argv)

    def setUp(self):
        # Set up an in-memory SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE todos (date DATE, todo TEXT, description TEXT)")

        # Patch the database connection in main to use the in-memory DB
        patcher = patch('main.init_db', return_value=(self.conn, self.cursor))
        self.addCleanup(patcher.stop)
        patcher.start()

        # Re-initialize the window after patching the DB
        main.conn, main.cursor = main.init_db(self.conn)  # Ensure window uses in-memory DB
        main.window.listWidget.clear()  # Clear the list widget to start fresh
        main.cursor.execute("SELECT * FROM todos")  # Reload data from the in-memory DB

    def test_add_todo(self):
        # Access the UI elements directly from the global window object
        todo_input = main.window.lineEdit
        add_button = main.window.pushButton
        list_view = main.window.listWidget

        # Simulate typing a todo item
        todo_input.setText("Test Todo Item")

        # Simulate clicking the add button
        QTest.mouseClick(add_button, Qt.MouseButton.LeftButton)

        # Verify that the item was added to the list
        self.assertEqual(list_view.count(), 1)
        self.assertIn("Test Todo Item", list_view.item(0).text())

        # Verify that the item was added to the in-memory database
        self.cursor.execute("SELECT * FROM todos")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Test Todo Item")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

if __name__ == "__main__":
    unittest.main()

