import pytest
from statistics import mean, median

def test_mean():
    assert mean([1, 2, 3]) == 2
    assert mean([]) == 0
    assert mean([1.5, 2.5, 3.5]) == 2.5
    assert mean([-1, -2, -3]) == -2
    assert mean([0, 0, 0]) == 0

def test_median():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([3, 1, 2]) == 2
    assert median([4, 1, 3, 2]) == 2.5
    assert median([1]) == 1
