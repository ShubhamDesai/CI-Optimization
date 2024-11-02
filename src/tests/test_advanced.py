# src/tests/test_advanced.py

from advanced import power, mod

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_mod():
    assert mod(10, 3) == 1
    assert mod(10, 5) == 0
