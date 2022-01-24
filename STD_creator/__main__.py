from STD_creator import ui
from sys import argv
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(argv)
    window = ui.App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()