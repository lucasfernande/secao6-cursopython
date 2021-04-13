import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.display = QLineEdit()

        self.setWindowTitle('Calculadora')  # setando o título da janela
        self.setFixedSize(400, 400)  # setando um tamanho fixo para a janela

        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: black; font-size: 28px}'
        )

        # QPushButton('Texto do Botao', linha, coluna, linhas ocupadas, colunas ocupadas)
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText('')
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1)

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('÷'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('x'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1)

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # o QSizePolicy serve para expandir
        # os botões automaticamente

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, func=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not func:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(func)

        btn.setStyleSheet('font-size: 20px')
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()

    calculadora.show()
    qt.exec_()
