from STD_creator import config_crud
import os
from datetime import date

SETTINGS_INI_PATH = 'tests/fixtures'

MIN_DATE = date(2018, 7, 1)
MAX_DATE = date(2018, 8, 15)


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
    assert config.get_dates == {'min': MIN_DATE, 'max': MAX_DATE}
    assert config.get_account == 2307000


def test_read_comparison(tmpdir):
    config = config_crud.ComparisonIni(tmpdir)
    assert 'токарь' in config.prof.keys()
    assert config.prof['токарь'] == 'токарная'

def test_read_comparison_template():
    config = config_crud.ComparisonIni(SETTINGS_INI_PATH)
    assert 'фрезеровщик' in config.prof.keys()
    assert config.prof['фрезеровщик'] == 'фрезерная'
