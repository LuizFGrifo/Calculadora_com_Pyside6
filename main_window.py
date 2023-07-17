from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                               QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Titulo da janela
        self.setWindowTitle('Calculator by Grifo')

    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()  # Se ajusta ao tamanho da janela
        self.setFixedSize(self.width(), self.height())

    # Função para evitar ficar usando muitas coisas com '.'
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
