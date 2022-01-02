import pandas as pd
import openpyxl
import re
from random import randrange
from datetime import timedelta, date


COL = {
    'NAMES': 'names',
    'QUANTITY': 'quantity',
    'LABOR': 'labor',
    'CODE': 'code',
    'DATE': 'date'
}


def save_with_template(filename, template_file_name, data_frame):
    wb = openpyxl.load_workbook(filename=template_file_name)
    sheet = wb.active

    for number, row in enumerate(data_frame.values):
        new_row = [
            number + 1,
            row[0],
            row[1],
            734,
            row[2],
            row[3],
            row[4],
            round(row[5] / 8.2, 2),
            row[6],
        ]
        sheet.append(new_row)
    wb.save(filename)


def hyphen_replase(in_string):
    out_string = re.sub(r'(?<=[\d{4,}])-', '.', in_string)
    out_string = re.sub(r'(\.)(?![\d])', ' ', out_string)
    return out_string


def split_by_space(in_string):
    out_string_set = re.split(r'(?<=[\d]) ', in_string, maxsplit=1)
    if len(out_string_set) < 2:
        out_string_set.append(out_string_set[0])
    return out_string_set[0], out_string_set[1]


def convert_to_rnd_date(in_date, dates_set):
    if in_date is not pd.NaT:
        return in_date
    delta = dates_set['max'] - dates_set['min']
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    out_date = dates_set['min'] + timedelta(seconds=random_second)
    return out_date


def load_scroll(filename, dates_set):
    data = pd.read_excel(filename)
    data.drop(data.columns[[1, 3, 4, 6]], axis=1, inplace=True)
    data.columns = [COL['NAMES'], COL['QUANTITY'], COL['LABOR'], COL['DATE']]
    data[COL['DATE']] = data[COL['DATE']].apply(lambda d: convert_to_rnd_date(d, dates_set))
    data.dropna(inplace=True)
    data[COL['NAMES']] = data[COL['NAMES']].apply(hyphen_replase)
    data['splits_names'] = data[COL['NAMES']].apply(lambda line: split_by_space(line)[1])
    data[COL['CODE']] = data[COL['NAMES']].apply(lambda line: split_by_space(line)[0])
    data[COL['NAMES']] = data['splits_names']
    data.drop(['splits_names'], axis=1, inplace=True)
    pd.set_option('max_columns', 4)
    return data
