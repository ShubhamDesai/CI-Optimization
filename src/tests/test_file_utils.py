import os
from file_utils import write_file,read_file

def test_write_and_read_file():
    test_path = 'test.txt'
    write_file(test_path, 'Hello, World!')
    assert read_file(test_path) == 'Hello, World!'
    os.remove(test_path)
