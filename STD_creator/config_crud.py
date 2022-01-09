import configparser
import os
from pathlib import Path
from datetime import date


MIN_DATE = date(2018, 7, 1)
MAX_DATE = date(2018, 8, 15)


DEF_COMPARISON = {
    'токарь': 'токарная',
    'фрезеровщик': 'фрезерная',
    'шлифовщик': 'шлифовальная',
    'токарь-расточник': 'расточная',
    'слесарь-инструментальщик': 'слесарная',
}

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
        max_date = MAX_DATE.strftime('%Y/%m/%d')
        min_date = MIN_DATE.strftime('%Y/%m/%d')
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

    @property
    def get_account(self):
        return int(self.config.get('others', 'account', fallback='2307000'))

    @property
    def get_shop(self):
        return self.config.get('others', 'shop', fallback='34')
    @property
    def depth(self):
        return int(self.config.get('others', 'depth', fallback=6))

    def create_config(self):
        self.config.add_section('folders')
        self.config.add_section('files')
        self.config.add_section('date_time')
        self.config.add_section('others')
        self.in_folder_path_set('/')
        self.out_folder_path_set('/')
        self.template_path_set('/')
        self.scroll_path_set('/')
        self.stuffing_path_set('/')
        self.default_date_set()
        self.config.set('others', 'account', '2307000')
        self.config.set('others', 'shop', '34')
        self.config.set('others', 'depth', '6')
        self.config_save()


class ComparisonIni:
    def __init__(self, path=os.getcwd()):
        self.config = configparser.ConfigParser()
        self.path = os.path.join(path, 'comparison.ini')
        if not os.path.exists(self.path):
            self.create_config()
        self.config.read(self.path)

    def config_save(self):
        if not os.path.exists(self.path):
            file = Path(self.path)
            file.touch(exist_ok=True)
        with open(self.path, "w") as config_file:
            self.config.write(config_file)

    def create_config(self):
        self.config['comparison'] = DEF_COMPARISON
        self.config_save()

    @property
    def prof(self):
        items = self.config['comparison']
        return items
