from PyQt5 import QtWidgets
from ui_design import Ui_MainWindow
import sys
from STD_creator import config_crud, xlsx_parsers, stuff
from os import walk, path
from STD_creator.compilators import std_compilator


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

        self.config = config_crud.CrudConfig()
        if self.config.in_folder_path != '/':
            self.load_list_filenames()
        if self.config.out_folder_path != '/':
            self.out_folder_files_count()
        if self.config.scroll_path != '/':
            self.load_scroll()
        if self.config.stuffing_path != '/':
            self.load_stuffing_table()
        if path.isfile(self.config.template_path):
            self.TemplateIndicator.setText('Присутствует')

        self.InFolderButton.clicked.connect(self.in_folder_choose)
        self.OutFolderButton.clicked.connect(self.out_folder_choose)
        self.ScriptButton.clicked.connect(self.script_choose)
        self.StaffingButton.clicked.connect(self.stuffing_choose)
        self.TemplateButton.clicked.connect(self.template_choose)
        self.CompillButton.clicked.connect(self.compill)

    def load_list_filenames(self):
        self.FileNamesList = xlsx_parsers.get_list_filenames(self.config.in_folder_path)
        self.InLcdNumber.display(len(self.FileNamesList))

    def load_stuffing_table(self):
        try:
            self.Stuffing = stuff.StaffingTable(self.config.stuffing_path)
        except KeyError:
            self.print('Штатное не содержит нужных колонок')
            self.config.stuffing_path_set('/')
            self.StaffingIndicator.setText('Отсутсвует')
        except FileNotFoundError:
            self.print('Фаил штатного отсутсвует')
            self.config.stuffing_path_set('/')
            self.StaffingIndicator.setText('Отсутсвует')
        else:
            self.StaffingIndicator.setText('Присутствует')

    def load_scroll(self):
        try:
            self.Scroll = xlsx_parsers.load_scroll(self.config.scroll_path, self.config.get_dates)
            self.ScrpLcdNumber.display(self.Scroll.shape[0])
        except ValueError:
            self.print('Список не содержит нужных колонок')
            self.config.scroll_path_set('/')
            self.ScrpLcdNumber.display('err')
        except IndexError:
            self.print('Список не содержит нужных колонок')
            self.config.scroll_path_set('err')
            self.ScrpLcdNumber.display(0)
        except FileNotFoundError:
            self.print('Список шифров недоступен')
            self.config.scroll_path_set('/')
            self.ScrpLcdNumber.display(0)

    def template_choose(self):
        filename = self.file_chooser('Шаблон')[0]
        if filename:
            self.config.template_path_set(filename)
            self.TemplateIndicator.setText('Присутствует')
        self.print('Загружен шаблон')
        
    def stuffing_choose(self):
        filename = self.file_chooser('Штатное расписание')[0]
        if filename:
            self.config.stuffing_path_set(filename)
            self.load_stuffing_table()

    def script_choose(self):
        filename = self.file_chooser('Список шифров')[0]
        if filename:
            self.config.scroll_path_set(filename)
            self.load_scroll()

    def in_folder_choose(self):
        folder_name = self.folder_chooser('Входящая папка')
        if folder_name:
            self.config.in_folder_path_set(folder_name)
            self.load_list_filenames()

    def out_folder_files_count(self):
        try:
            file_count = len(list(walk(self.config.out_folder_path))[0][2])
        except IndexError:
            self.print('Папка выхода недоступна')
            self.config.out_folder_path_set('/')
            self.OutLcdNumber.display('err')
        else:
            self.OutLcdNumber.display(file_count)
        
    def out_folder_choose(self):
        folder_name = self.folder_chooser('Исходящая папка')
        if folder_name:
            self.config.out_folder_path_set(folder_name)
            self.out_folder_files_count()

    def folder_chooser(self, description):
        file_name = QtWidgets.QFileDialog.getExistingDirectory(self, description, '/')
        return file_name

    def file_chooser(self, description):
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            self, description, filter="Exel table(*.xls *.xlsx)"
        )
        return file_name

    def print(self, text):
        delay = 3000
        self.statusBar().showMessage(text, delay)
        self.statusbar.repaint()

    def set_indicate(self, percent):
        self.progressBar.setValue(percent)
        self.progressBar.repaint()

    def compill(self):
        self.print('Компилирую')
        try:
            std_compilator(self.set_indicate, self.config)
        except IsADirectoryError:
            self.print('Не все настройки внесены, останов')
        except FileNotFoundError:
            self.print('Один из файлов отсутсвует, останов')
        except IndexError:
            self.print('Повреждена структура файла, останов')
        except KeyError:
            self.print('Нет нужных колонок, останов')
        except Exception as e:
            self.print(e.message)
        else:
            self.out_folder_files_count()
            self.print('Готово')


if __name__ == '__main__':
    main()
