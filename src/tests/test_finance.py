import pytest
from finance import simple_interest, compound_interest

def test_simple_interest():
    assert simple_interest(1000, 5, 2) == 100
    assert simple_interest(0, 5, 2) == 0
    assert simple_interest(1000, 0, 2) == 0
    assert simple_interest(1000, 5, 0) == 0

def test_compound_interest():
    result = compound_interest(1000, 5, 2, 4)
    assert round(result, 5) == 104.4861
    assert compound_interest(0, 5, 2, 4) == 0
    assert compound_interest(1000, 0, 2, 4) == 0
    assert compound_interest(1000, 5, 0, 4) == 0
