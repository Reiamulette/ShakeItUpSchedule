# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import os

@pytest.mark.datafiles('CPAC2019.xlsx')
def test_load_data(datafiles):
    path = str(datafiles)
    assert len(os.lisdir(path)) == 1
    assert os.path.isfile(os.path.join(path,'CPAC2019.xlsx'))
    assert len(datafiles.listdir()) == 1
    assert (datafiles/'CPAC2019.xlsx').check(file = 1)

#def test_day_time():
