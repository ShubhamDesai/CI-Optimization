import pytest
from main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -7) == -12

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(-1, -1) == 0
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(4, 0) == 0
    assert multiply(-2, 5) == -10
    assert multiply(-3, -3) == 9
#for triggering CI"

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError):
        divide(5, 0)
