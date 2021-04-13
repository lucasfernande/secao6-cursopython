import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn_escolher_arquivo.clicked.connect(self.abrir_img)
        self.btn_redimensionar.clicked.connect(self.redimensionar)
        self.btn_salvar.clicked.connect(self.salvar)

    def abrir_img(self):
        img, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Selecionar imagem',
            r'C:\Users\lucas\Pictures',
        )

        self.input_arquivo.setText(img)
        self.original_img = QPixmap(img)
        self.label_IMG.setPixmap(self.original_img)
        self.input_largura.setText(str(self.original_img.width()))  # pegando a largura da foto
        self.input_altura.setText(str(self.original_img.height()))  # pegando a altura da foto

    def redimensionar(self):
        largura = int(self.input_largura.text())

        self.nova_img = self.original_img.scaledToWidth(largura)
        self.label_IMG.setPixmap(self.nova_img)

        self.input_largura.setText(str(self.nova_img.width()))
        self.input_altura.setText(str(self.nova_img.height()))

    def salvar(self):
        img, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            r'C:\Users\lucas\Desktop',
        )

        self.nova_img.save(img, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()

    app.show()
    qt.exec_()
