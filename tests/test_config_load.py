from STD_creator import config_crud
import os

SETTINGS_INI_PATH = 'tests/fixtures'


def test_init(tmpdir):
    config = config_crud.CrudConfig(tmpdir)
    testpath = os.path.join(tmpdir, 'settings.ini')
    assert config.path == testpath
    assert os.path.exists(testpath)
    assert config.in_folder_path == '/'
    assert config.scroll_path == '/'


def test_r_w(tmpdir):
    config = config_crud.CrudConfig(tmpdir)
    config.in_folder_path_set('/test')
    config.out_folder_path_set('/test')
    config = config_crud.CrudConfig(tmpdir)
    assert config.in_folder_path == '/test'
    assert config.out_folder_path == '/test'


def test_read():
    config = config_crud.CrudConfig(SETTINGS_INI_PATH)
    assert config.stuffing_path == 'tests/fixtures/files/stuffing.xlsx'
    assert config.scroll_path == 'tests/fixtures/files/scroll.xlsx'
    assert config.template_path == 'tests/fixtures/files/template.xlsx'
