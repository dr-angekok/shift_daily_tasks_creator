from os import walk, path

import pandas as pd
import openpyxl
import re
from random import randrange
from datetime import timedelta
from STD_creator.collumn_comparison import COL


def save_with_template(filename, template_file_name, data_frame):
    wb = openpyxl.load_workbook(filename=template_file_name)
    sheet = wb.active
    columns = data_frame.columns
    for number, values in enumerate(data_frame.values):
        row = dict(zip(columns, values))
        new_row = [
            number + 1,
            row[COL['SHOP']],
            row[COL['YEAR']],
            row[COL['MONTH']],
            row[COL['KIND']],
            row[COL['BRIGADE']],
            row[COL['ACCOUNT']],
            row[COL['TNUMBER']],
            row[COL['NAMES']],
            row[COL['PROFESSION']],
            row[COL['BARCODE']],
            row[COL['CODE']],
            row[COL['DESIGNATION']],
            row[COL['OPERATION']],
            row[COL['LABOR']],
            row[COL['QUANTITY']],
            row[COL['WORKING_OUT']],
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
    data.columns = [COL['DESIGNATION'], COL['QUANTITY'], COL['LABOR'], COL['DATE']]
    data[COL['DATE']] = data[COL['DATE']].apply(lambda d: convert_to_rnd_date(d, dates_set))
    data.dropna(inplace=True)
    data[COL['DESIGNATION']] = data[COL['DESIGNATION']].apply(hyphen_replase)
    data['splits_des'] = data[COL['DESIGNATION']].apply(lambda line: split_by_space(line)[1])
    data[COL['CODE']] = data[COL['DESIGNATION']].apply(lambda line: split_by_space(line)[0])
    data[COL['DESIGNATION']] = data['splits_des']
    data.drop(['splits_des'], axis=1, inplace=True)
    return data


def parse_list_file(filename):
    with open(filename,'r', encoding='cp1251') as f:
        raw_file = f.read()
    text = re.sub(r'\s\s+|(\d{2}\.){2}\d{4}\s(\d{1,2}:){2}\d{2}\D{3}', ' ', raw_file)
    text = re.sub(r'\s{3}', '\n', text)
    text_set = re.split(r'\n', text)
    text_set.pop(0)
    list_set = []
    for item in text_set:
        splited_list = item.split(' ')
        splited_list.pop(0)
        if not splited_list:
            break
        if len(splited_list) == 4:
            list_set.append(splited_list)
        else:
            names = ''.join(splited_list[2:-2])
            list_set.append([splited_list[0], splited_list[1], names, splited_list[-1]])
    data = pd.DataFrame(list_set, columns=[COL['BARCODE'], COL['CODE'], COL['DESIGNATION'], COL['QUANTITY']])
    data.dropna(inplace=True)
    return data


def get_list_filenames(folder_path):
    filename_list = []
    for root, dirs, files in walk(folder_path):
        for filename in files:
            if filename.split('.')[-1] == 'txt':
                filename_list.append(path.join(folder_path, filename))
    return filename_list

def get_zero_date_set():
    data = pd.DataFrame(columns=COL.values())
    data.loc[0] = [0 for _ in range(18)]
    return data
