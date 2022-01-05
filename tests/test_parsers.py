# -*- coding: utf-8 -*-
from datetime import date
import pytest
from STD_creator.xlsx_parsers import hyphen_replase, split_by_space, load_scroll, parse_list_file, get_list_filenames, get_zero_date_set

SCROLL_PATH = 'tests/fixtures/files/scroll.xlsx'

DEF_COL = {
    'names': 'designation',
    'quantity': 'quantity',
    'labor': 'labor',
    'code': 'code',
    'date': 'date'
}

MIN_DATE = date(2018, 7, 1)
MAX_DATE = date(2018, 8, 15)

@pytest.mark.parametrize("in_str,out_str", [
    ('6680.05774.00.00.000 пресс-форма на модель №3 детали "Венец сопловой"', '6680.05774.00.00.000 пресс-форма на модель №3 детали "Венец сопловой"'),
    ('6680.05784.00.000.00 стапель', '6680.05784.00.000.00 стапель'),
    ('6680.05772.00.00.000 пресс-форма на венец сопловой №1', '6680.05772.00.00.000 пресс-форма на венец сопловой №1'),
    ('6680-05770-00.000.00 пресс-форма на пакет лопаток', '6680.05770.00.000.00 пресс-форма на пакет лопаток'),
    ('6680.05782.00.00.000 пресс-форма на образцы', '6680.05782.00.00.000 пресс-форма на образцы'),
    ('6146-00712-00.00.00 ролик для накатки спиральных канавок', '6146.00712.00.00.00 ролик для накатки спиральных канавок'),
    ('6680-05775-00.000.00 пресс-форма для стержня на "Ротор"', '6680.05775.00.000.00 пресс-форма для стержня на "Ротор"'),
    ('6680.05783.00.00.000 прессформа', '6680.05783.00.00.000 прессформа'),
    ('6146-00711-00.00.00 ролик для накатки спиральных канавок', '6146.00711.00.00.00 ролик для накатки спиральных канавок')])
def test_hyphen_replase(in_str, out_str):
    assert hyphen_replase(in_str) == out_str


@pytest.mark.parametrize("in_str,out", [
    ('6680.05774.00.00.000 пресс-форма на модель №3 детали "Венец сопловой"', ('6680.05774.00.00.000', 'пресс-форма на модель №3 детали "Венец сопловой"')),
    ('6680.05784.00.000.00 стапель', ('6680.05784.00.000.00', 'стапель')),
    ('6680.05772.00.00.000 пресс-форма на венец сопловой №1', ('6680.05772.00.00.000', 'пресс-форма на венец сопловой №1')),
    ('6680-05770-00.000.00 пресс-форма на пакет лопаток', ('6680-05770-00.000.00', 'пресс-форма на пакет лопаток')),
    ('6680.05782.00.00.000 пресс-форма на образцы', ('6680.05782.00.00.000', 'пресс-форма на образцы')),
    ('6146-00712-00.00.00 ролик для накатки спиральных канавок', ('6146-00712-00.00.00',  'ролик для накатки спиральных канавок')),
    ('6680-05775-00.000.00 пресс-форма для стержня на "Ротор"', ('6680-05775-00.000.00', 'пресс-форма для стержня на "Ротор"')),
    ('6680.05783.00.00.000 прессформа', ('6680.05783.00.00.000', 'прессформа')),
    ('6146-00711-00.00.00 ролик для накатки спиральных канавок', ('6146-00711-00.00.00', 'ролик для накатки спиральных канавок')),
    ('6364-24494-00.000.00', ('6364-24494-00.000.00', '6364-24494-00.000.00'))])
def test_split_by_space(in_str, out):
    assert split_by_space(in_str) == out


def test_load_scroll_columns():
    data = load_scroll(SCROLL_PATH, {'min': MIN_DATE, 'max': MAX_DATE})
    assert list(data.columns) == [DEF_COL['names'], DEF_COL['quantity'], DEF_COL['labor'], DEF_COL['date'], DEF_COL['code']]
    tested_data = data.loc[data[DEF_COL['names']] == 'стапель']
    assert tested_data[DEF_COL['names']].values[0] == 'стапель'
    assert tested_data[DEF_COL['code']].values[0] == '6680.05784.00.000.00'
    assert tested_data[DEF_COL['labor']].values[0] == 418.4


@pytest.mark.parametrize("filename,line_count", [
    ('tests/fixtures/files/6538-1091.txt', 11),
    ('tests/fixtures/files/6312-09007.txt', 4),
    ('tests/fixtures/files/6262-00643.txt', 4),
    ('tests/fixtures/files/6799-00373.txt', 11)])
def test_parse_list_file(filename, line_count):
    data = parse_list_file(filename)
    assert data.shape[0] == line_count


def test_get_list_filenames():
    folder_path = 'tests/fixtures/files'
    test_list = get_list_filenames(folder_path)
    assert len(test_list) == 114


def test_get_zero_df():
    data = get_zero_date_set()
    assert data.shape[0] == 0
    assert len(data.columns) == 18
    assert 'working_out' in data.columns.values
