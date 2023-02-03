from lkf_tools import process_dataset

def test_import():
    assert 1==1

def test_load_data():
    lkf_data = process_dataset('./data/McGill_e2_1997_daily_means.nc',
                           output_path='./data/lkfs/McGill/')

def test_detect_lkfs():
    lkf_data = process_dataset('./data/McGill_e2_1997_daily_means.nc',
                           output_path='./data/lkfs/McGill/')
    lkf_data.detect_lkfs(indexes=[0,1])

