from advanced import power, mod

def test_power():
    assert power(2, 3) == 8
    assert power(-2, 3) == -8
    assert power(0, 5) == 0
    assert power(5, 0) == 1

def test_mod():
    assert mod(10, 3) == 1
    assert mod(10, 5) == 0
    assert mod(0, 1) == 0
    assert mod(10, -3) == -2
