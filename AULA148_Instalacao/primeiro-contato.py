"""

PyQT é um toolkit desenvolvido em C++ utilizado em vários programas
para criação de aplicações GUI (Interface gráfica).

pip install pyqt5
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()  # central widget
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 21px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)  # adicionando o botão no layout

        self.btn.clicked.connect(self.falaOi)

        self.setCentralWidget(self.cw)

    def falaOi(self):
        print('Olá mundo')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()

    app.show()
    qt.exec_()
