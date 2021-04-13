import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()

    app.show()
    qt.exec_()
