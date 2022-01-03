from STD_creator.stuff import StaffingTable

STUFF_PATH = 'tests/fixtures/files/stuffing.xlsx'

COLUMN ={
    'NAMES': 'name',
    'PROFESSION': 'prof',
    'NUMBER': 'numb',
}


def test_stuffing():
    base = StaffingTable(STUFF_PATH)
    for col in base.columns:
        assert col in COLUMN.values()
    assert base.columns_count == 69
