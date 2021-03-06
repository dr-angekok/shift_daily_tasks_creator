from STD_creator.stuff import StaffingTable

STUFF_PATH = 'tests/fixtures/files/stuffing.xlsx'

COLUMN ={
    'NAMES': 'names',
    'PROFESSION': 'profession',
    'NUMBER': 'tnumber',
}


def test_stuffing():
    base = StaffingTable(STUFF_PATH)
    for col in base.columns:
        assert col in COLUMN.values()
    assert base.columns_count == 40
    assert 'токарь' in base.reduced_professions_set
    assert base.rnd_profession in base.reduced_professions_set
    tested_names = base.get_names('токарь')
    assert 'Лавров Владимир Михайлович' in tested_names
    assert base.get_rnd_names_set('токарь')[0] in tested_names


