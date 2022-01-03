import configparser
import os
from pathlib import Path
from datetime import date


MIN_DATE = date(2018, 7, 1)
MAX_DATE = date(2018, 8, 15)


class CrudConfig:
    def __init__(self, path=os.getcwd()):
        self.config = configparser.ConfigParser()
        self.path = os.path.join(path, 'settings.ini')
        if not os.path.exists(self.path):
            self.create_config()
        self.config.read(self.path)

    @property
    def in_folder_path(self):
        path = self.config.get('folders', 'in_folder_path', fallback=None)
        return path

    @property
    def out_folder_path(self):
        path = self.config.get('folders', 'out_folder_path', fallback=None)
        return path

    @property
    def template_path(self):
        path = self.config.get('files', 'template_path', fallback=None)
        return path

    @property
    def scroll_path(self):
        path = self.config.get('files', 'scroll_path', fallback=None)
        return path

    @property
    def stuffing_path(self):
        path = self.config.get('files', 'stuffing_path', fallback=None)
        return path

    def in_folder_path_set(self, path):
        self.config.set('folders', 'in_folder_path', path)
        self.config_save()

    def out_folder_path_set(self, path):
        self.config.set('folders', 'out_folder_path', path)
        self.config_save()

    def template_path_set(self, path):
        self.config.set('files', 'template_path', path)
        self.config_save()

    def scroll_path_set(self, path):
        self.config.set('files', 'scroll_path', path)
        self.config_save()

    def stuffing_path_set(self, path):
        self.config.set('files', 'stuffing_path', path)
        self.config_save()

    def config_save(self):
        if not os.path.exists(self.path):
            file = Path(self.path)
            file.touch(exist_ok=True)
        with open(self.path, "w") as config_file:
            self.config.write(config_file)

    def default_date_set(self):
        max_date = MAX_DATE.strftime('%d/%m/%Y')
        min_date = MIN_DATE.strftime('%d/%m/%Y')
        self.config.set('date_time', 'min_date', min_date)
        self.config.set('date_time', 'max_date', max_date)
        self.config_save()

    @property
    def get_dates(self):
        min_date = self.config.get('date_time', 'min_date', fallback=MAX_DATE.strftime('%Y/%m/%d'))
        max_date = self.config.get('date_time', 'max_date', fallback=MIN_DATE.strftime('%Y/%m/%d'))
        max_date_set = map(int, max_date.split('/'))
        min_date_set = map(int, min_date.split('/'))
        return {'min': date(*min_date_set), 'max': date(*max_date_set)}

    def create_config(self):
        self.config.add_section('folders')
        self.config.add_section('files')
        self.config.add_section('date_time')
        self.in_folder_path_set('/')
        self.out_folder_path_set('/')
        self.template_path_set('/')
        self.scroll_path_set('/')
        self.stuffing_path_set('/')
        self.default_date_set()
        self.config_save()
