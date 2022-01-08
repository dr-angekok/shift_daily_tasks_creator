import pandas as pd
import numpy as np
from STD_creator.config_crud import ComparisonIni
from STD_creator.stuff import StaffingTable
from STD_creator import xlsx_parsers
from STD_creator.collumn_comparison import COL
import os
import re


NORMALS = (
    ('токарь', 0.3),
    ('токарь', 0.25),
    ('фрезеровщик', 0.13),
    ('шлифовщик', 0.16),
    ('слесарь-инструментальщик', 0.03),
)

def get_coeff(quantity):
    if quantity:
        return np.random.normal(loc=50) * int(quantity)
    return 0


def get_scroll_line(code, scroll):
    result = None
    code = code.replace('-', '.')
    for index, row in scroll.iterrows():
        if code in row[COL['CODE']]:
            result = row
            break
    return result


def std_compilator(indicator, config):
    pd.options.mode.chained_assignment = None
    files_list = xlsx_parsers.get_list_filenames(config.in_folder_path)
    indicator_scale = len(files_list)
    stuffing_table = StaffingTable(config.stuffing_path)
    comparisons = ComparisonIni()
    scroll = xlsx_parsers.load_scroll(config.scroll_path, config.get_dates)
    for indicator_step, filename in enumerate(files_list):
        out_data = xlsx_parsers.get_zero_date_set()
        input_data = xlsx_parsers.parse_list_file(filename)
        for index, row in input_data.iterrows():
            std_rows = xlsx_parsers.get_zero_date_set()
            fixed_names_set = stuffing_table.rnd_fixed_names_set
            if re.search(r'ГОСТ\d{4,5}-\d{2,}', row[COL['DESIGNATION']]):
                for line_index, profession_set in enumerate(NORMALS):
                    line = xlsx_parsers.get_zero_date_set()
                    line[COL['PROFESSION']] = profession_set[0]
                    line[COL['LABOR']] = profession_set[1]
                    name_set = stuffing_table.get_rnd_names_set(profession_set[0])
                    line[COL['NAMES']] = name_set[0]
                    line[COL['TNUMBER']] = name_set[1]
                    line[COL['OPERATION']] = line[COL['PROFESSION']].apply(lambda x: comparisons.prof[x])
                    for column in row.keys():
                        line[column].loc[0] = row[column]
                    std_rows.loc[line_index + 1] = line.loc[0]
            else:
                for line_index in range(round(np.random.normal(loc=6))):
                    line = xlsx_parsers.get_zero_date_set()
                    line[COL['PROFESSION']] = stuffing_table.rnd_profession
                    name_set = fixed_names_set[line[COL['PROFESSION']].values[0]]
                    line[COL['NAMES']] = name_set[0]
                    line[COL['TNUMBER']] = name_set[1]
                    line[COL['OPERATION']] = line[COL['PROFESSION']].apply(lambda x: comparisons.prof[x])
                    for column in row.keys():
                        line[column].loc[0] = row[column]
                    std_rows.loc[line_index + 1] = line.loc[0]
            out_data = pd.concat([out_data, std_rows])
        out_data.dropna(inplace=True)
        out_data[COL['SHOP']] = config.get_shop
        out_data[COL['ACCOUNT']] = config.get_account
        out_data[COL['KIND']] = 1

        out_data.drop(out_data.loc[0].index, inplace=True)
        base_filename, _ = os.path.splitext(os.path.basename(filename))

        scroll_line = get_scroll_line(base_filename, scroll)
        error_folder = 'errors'

        if scroll_line is not None:
            error_folder = ''
            out_data[COL['YEAR']] = scroll_line[COL['DATE']].timetuple()[0]
            out_data[COL['MONTH']] = scroll_line[COL['DATE']].timetuple()[1]

            out_data[COL['QUANTITY']] = out_data[COL['QUANTITY']].apply(lambda x: int(x) if x else 1)
            out_data['coeff'] = out_data[COL['QUANTITY']].apply(lambda x: abs(np.random.normal(loc=10, scale=6)) * x)
            coeff_summ = out_data['coeff'].sum()
            out_data[COL['LABOR']] = round(scroll_line[COL['LABOR']] / coeff_summ * out_data['coeff'] / out_data[COL['QUANTITY']], 2)
            out_data[COL['WORKING_OUT']] = out_data[COL['LABOR']] * out_data[COL['QUANTITY']]

        out_filename = os.path.join(config.out_folder_path, error_folder, base_filename + '.xlsx')
        xlsx_parsers.save_with_template(out_filename, config.template_path, out_data)
        indicator(round(indicator_step / indicator_scale * 100) + 1)
