"""

PyQT é um toolkit desenvolvido em C++ utilizado em vários programas
para criação de aplicações GUI (Interface gráfica).

pip install pyqt5
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()

    app.show()
    qt.exec_()
