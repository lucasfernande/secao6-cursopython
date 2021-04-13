import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.setWindowTitle('Calculadora')  # setando o título da janela
        self.setFixedSize(400, 400)  # setando um tamanho fixo para a janela

        self.setCentralWidget(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()

    calculadora.show()
    qt.exec_()
