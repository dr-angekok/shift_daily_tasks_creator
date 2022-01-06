from PyQt5 import QtWidgets
from ui_design import Ui_MainWindow
import sys
from STD_creator import config_crud, xlsx_parsers, stuff


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
        if self.config.scroll_path != '/':
            self.load_scroll()
        if self.config.stuffing_path != '/':
            self.load_stuffing_table()
        if self.config.template_path != '/':
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
        self.Stuffing = stuff.StaffingTable(self.config.stuffing_path)
        self.StaffingIndicator.setText('Присутствует')
        self.print('Загружено штатное')

    def load_scroll(self):
        self.Scroll = xlsx_parsers.load_scroll(self.config.scroll_path, self.config.get_dates)
        self.ScrpLcdNumber.display(self.Scroll.shape[0])
        self.print('Загружен список шифров')

    def filename_to_config_save(self, selector):
        command = {
            'template': [self.config.template_path_set, 'Шаблон сохранения', self.TemplateIndicator.setText('Присутствует')],
            'stuffing': [self.config.stuffing_path_set, 'Штатное расписание', self.load_stuffing_table()],

        }
        filename = self.file_chooser(command[selector][1])[0]
        if filename:
            command[selector][0](filename)
            command[selector][2]

    def template_choose(self):
        self.filename_to_config_save('template')
        self.print('Загружен шаблон')
        
    def stuffing_choose(self):
        self.filename_to_config_save('stuffing')

    def script_choose(self):
        filename = self.file_chooser('Список шифров')[0]
        if filename:
            self.config.scroll_path_set(filename)
            self.load_scroll()

    def in_folder_choose(self):
        self.InFolderPath = self.folder_chooser('Входящая папка')
        
    def out_folder_choose(self):
        self.OutFolderPath = self.folder_chooser('Исходящая папка')

    def folder_chooser(self, description):
        file_name = QtWidgets.QFileDialog.getExistingDirectory(self, description, '.', QtWidgets.QFileDialog.ShowDirsOnly)
        print(file_name)
        return file_name

    def file_chooser(self, description):
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            self, description, filter="Exel table(*.xls *.xlsx)"
        )
        return file_name

    def print(self, text):
        self.statusBar().showMessage(text)
        self.statusbar.repaint()

    def compill(self):
        pass


if __name__ == '__main__':
    main()
