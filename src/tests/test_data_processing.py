# test_data_processing.py

from data_processing import process_large_dataset

def test_process_large_dataset():
    result = process_large_dataset()
    assert result == "Processing Complete"
