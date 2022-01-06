from PyQt5 import QtWidgets
from ui_design import Ui_MainWindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.print('Запущен')

    def folder_chooser(self, description):
        file_name = QtWidgets.QFileDialog.getExistingDirectory(self, description, ".")
        return file_name

    def file_chooser(self, description):
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            self, description, filter="Exel table(*.xls *.xlsx)"
        )
        return file_name

    def print(self, text):
        self.statusBar().showMessage(text)
        self.statusbar.repaint()


if __name__ == '__main__':
    main()
