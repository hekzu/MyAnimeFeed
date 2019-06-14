from PyQt5.QtWidgets import QWidget, QMessageBox
import PyQt5
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

    def center(self):
        frame_gm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(
            PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        center_point = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())

    def init_ui(self):
        self.center()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        QMessageBox.question(self, self.title, self.message, QMessageBox.Ok)
        self.show()

        sys.exit(0)
