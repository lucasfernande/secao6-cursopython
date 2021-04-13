from desafiocpf2 import validaCPF
from geradordecpf import geraCPF
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow

class CPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn_gera_cpf.clicked.connect(self.gera_cpf)
        self.btn_valida_cpf.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.label_retorno.setText(geraCPF())

    def valida_cpf(self):
        cpf = self.input_valida_cpf.text()
        self.label_retorno.setText(str(validaCPF(cpf)))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cpf = CPF()

    cpf.show()
    qt.exec_()
