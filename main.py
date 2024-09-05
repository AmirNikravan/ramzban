from PySide6.QtCore import Qt
from ui_main import *
from PySide6.QtWidgets import QMainWindow, QApplication
import sys
class mainWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())