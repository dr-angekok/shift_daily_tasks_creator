import pandas as pd

COLUMN ={
    'NAMES': 'name',
    'PROFESSION': 'prof',
    'NUMBER': 'numb',
}

COL_COMPARISON = {
    'Профессия по назначению': COLUMN['PROFESSION'],
    'Фамилия Имя Отчество': COLUMN['NAMES'],
    'Табельный номер': COLUMN['NUMBER'],
}


class StaffingTable:
    def __init__(self, filename):
        loaded_base = pd.read_excel(filename)
        loaded_base.dropna(inplace=True)
        
        self.base = pd.DataFrame()
        for key in COL_COMPARISON.keys():
            self.base[COL_COMPARISON[key]] = loaded_base[key]


    @property
    def columns(self):
        return self.base.columns.values

    @property
    def columns_count(self):
        return self.base.shape[0]
