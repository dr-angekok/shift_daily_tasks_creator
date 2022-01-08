import pandas as pd
from collections import Counter
from random import choice
from STD_creator.collumn_comparison import COL, COL_COMPARISON


DEF_COMPARISON = {
    'токарь': 'токарная',
    'фрезеровщик': 'фрезерная',
    'шлифовщик': 'шлифовальная',
    'токарь-расточник': 'расточная',
    'слесарь': 'слесарная',
}


class StaffingTable:
    def __init__(self, filename, comparison=DEF_COMPARISON):
        loaded_base = pd.read_excel(filename)
        loaded_base.dropna(inplace=True)
        self.comparison = comparison
        
        self.base = pd.DataFrame()
        for key in COL_COMPARISON:
            self.base[COL_COMPARISON[key]] = loaded_base[key]
        self.base[COL['PROFESSION']] = self.base[COL['PROFESSION']].apply(self._prof_clear)
        self.base.dropna(inplace=True)


    @property
    def columns(self):
        return self.base.columns.values

    @property
    def columns_count(self):
        return self.base.shape[0]

    @property
    def reduced_professions_set(self):
        profession_count = Counter(self.base[COL['PROFESSION']])
        min_count = min(profession_count.values())
        reduced_count = {}
        for key in profession_count:
            reduced_count[key] = round(profession_count[key] / min_count)
        profession_set = []
        for key in reduced_count:
            for _ in range(reduced_count[key]):
                profession_set.append(key)
        return profession_set

    @property
    def rnd_fixed_names_set(self):
        names_set = {}
        for profession in self.reduced_professions_set:
            names_set[profession] = self.get_rnd_names_set(profession)
        return names_set

    def _prof_clear(self, item):
        if item in self.comparison.keys():
            return item
        return pd.NaT

    def get_names(self, profession):
        lines = self.base[self.base[COL['PROFESSION']] == profession]
        clear_lines = lines.drop(COL['PROFESSION'], axis=1)
        return clear_lines.values

    def get_rnd_names_set(self, profession):
        return choice(self.get_names(profession))
    
    @property
    def rnd_profession(self):
        return choice(self.reduced_professions_set)
