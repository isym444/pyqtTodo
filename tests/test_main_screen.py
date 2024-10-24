import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
import sys
import sqlite3

from dashboard import Dashboard

class TestDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the QApplication instance
        cls.app = QApplication(sys.argv)

    def setUp(self):
        # Set up an in-memory SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE todos (date DATE, todo TEXT, description TEXT)")

        # Patch the database connection in the TodoApp class to use the in-memory database
        patcher = patch('dashboard.Dashboard.init_db', return_value=(self.conn, self.cursor))
        self.addCleanup(patcher.stop)
        patcher.start()

        # Initialize the main window after patching the DB
        self.todo_app = Dashboard()
        # self.todo_app.show()
    
    def test_add_todo(self):
        # Access the UI elements from the instance of TodoApp
        todo_input = self.todo_app.lineEdit
        add_button = self.todo_app.pushButton
        list_view = self.todo_app.listWidget

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

    def test_remove_todo(self):
        # Access the UI elements from the instance of TodoApp
        todo_input = self.todo_app.lineEdit
        add_button = self.todo_app.pushButton
        list_view = self.todo_app.listWidget
        remove_button = self.todo_app.pushButton_2

        # Add a todo item
        todo_input.setText("Test Todo Item")
        QTest.mouseClick(add_button, Qt.MouseButton.LeftButton)

        # Verify that the item was added to the list
        self.assertEqual(list_view.count(), 1)

        # Select the item in the list
        list_view.setCurrentRow(0)

        # Simulate clicking the remove button
        QTest.mouseClick(remove_button, Qt.MouseButton.LeftButton)

        # Verify that the item was removed from the list
        self.assertEqual(list_view.count(), 0)

        # Verify that the item was removed from the in-memory database
        self.cursor.execute("SELECT * FROM todos")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 0)
    
    def test_show_details(self):
        # Add a todo item
        self.todo_app.todo_input.setText("Test Todo for Details")
        QTest.mouseClick(self.todo_app.add_button, Qt.MouseButton.LeftButton)

        # Verify that the item is added to the list
        self.assertEqual(self.todo_app.list_view.count(), 1)

        # Manually trigger the show_details method
        self.todo_app.list_view.setCurrentRow(0)
        self.todo_app.show_details()

        # Check if a DetailsWindow instance was created and shown
        if self.todo_app.details_window:
            self.todo_app.details_window[-1].show()

        # Ensure a DetailsWindow instance was created
        self.assertEqual(len(self.todo_app.details_window), 1)

        # Check if the last DetailsWindow is visible
        self.assertTrue(self.todo_app.details_window[-1].isVisible())


    @classmethod
    def tearDownClass(cls):
        cls.app.quit()


if __name__ == "__main__":
    unittest.main()