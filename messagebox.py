from PyQt5.QtWidgets import QWidget, QMessageBox
import sys


class MessageBox(QWidget):
    def __init__(self, title, message):
        super().__init__()
        self.title = title
        self.message = message
        self.left = 600
        self.top = 300
        self.width = 640
        self.height = 300
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        QMessageBox.question(self, self.title, self.message, QMessageBox.Ok)
        self.show()

        sys.exit(0)
