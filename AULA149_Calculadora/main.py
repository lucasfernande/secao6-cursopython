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
            lambda: self.display.setText(''),
            'background: #ff8c00; color: white; font-weight: bold; border: none; border-radius: 5px'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<--'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: #483d8b; color: white; font-weight: bold; border: none; border-radius: 5px'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton('**'), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_equal,
            'background: #008000; color: white; font-weight: bold; border: none; border-radius: 5px'
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # o QSizePolicy serve para expandir
        # os botões automaticamente

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        btn.setStyleSheet('font-size: 20px; border: 1px solid #c0c0c0; border-radius: 5px')

        if not func:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(func)

        if style:
            btn.setStyleSheet('font-size: 20px;' + style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_equal(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )

        except Exception as e:
            self.display.setText('Operação inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()

    calculadora.show()
    qt.exec_()
