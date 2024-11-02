# src/tests/test_statistics.py

from statistics import mean, median

def test_mean():
    assert mean([1, 2, 3]) == 2
    assert mean([]) == 0

def test_median():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5
