import configparser
import os
from pathlib import Path


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

    def create_config(self):
        self.config.add_section('folders')
        self.config.add_section('files')
        self.in_folder_path_set('/')
        self.out_folder_path_set('/')
        self.template_path_set('/')
        self.scroll_path_set('/')
        self.stuffing_path_set('/')
        self.config_save()
