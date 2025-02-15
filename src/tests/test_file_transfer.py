
# test_file_transfer.py

from file_transfer import simulate_file_transfer

def test_simulate_file_transfer():
    result = simulate_file_transfer()
    assert result == "File Transfer Complete"
