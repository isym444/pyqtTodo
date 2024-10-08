import sys
from PyQt6 import QtWidgets, uic, QtCore
import sqlite3
from PyQt6.QtCore import QResource
import resources_rc
from dashboard import Dashboard
from details_window import DetailsWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QResource.registerResource("resources.qrc")
    
    main_window = Dashboard()
    main_window.show()
    
    sys.exit(app.exec())
