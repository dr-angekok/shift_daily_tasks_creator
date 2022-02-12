COL = {
    'COUNT': 'count',
    'SHOP': 'shop',
    'YEAR': 'year',
    'MONTH': 'month',
    'KIND': 'kind',
    'BRIGADE': 'brigade',
    'ACCOUNT': 'account',
    'TNUMBER': 'tnumber',
    'NAMES': 'names',
    'PROFESSION': 'profession',
    'BARCODE': 'barcode',
    'CODE': 'code',
    'DESIGNATION': 'designation',
    'OPERATION': 'operation',
    'LABOR': 'labor',
    'QUANTITY': 'quantity',
    'WORKING_OUT': 'working_out',
    'DATE': 'date',
}

COL_COMPARISON = {
    'Профессия по назначению': COL['PROFESSION'],
    'Фамилия Имя Отчество': COL['NAMES'],
    'Табельный номер': COL['TNUMBER'],
}

COMPARES = {
    r'^\s{8}': (('слесарь-инструментальщик', 0),),
    r'ГОСТ\d{4,5}-\d{2,}': (
        ('токарь', 0.3),
        ('токарь', 0.25),
        ('фрезеровщик', 0.13),
        ('шлифовщик', 0.16),
        ('слесарь-инструментальщик', 0.03),
    ),

}