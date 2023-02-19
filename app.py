from windows.window import MyWindow, QApplication
from PyQt6 import QtCore
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)  # salom
    win = MyWindow()
    win.setWindowState(QtCore.Qt.WindowState.WindowActive)
    win.show()
    app.exec()  # qwertyui
