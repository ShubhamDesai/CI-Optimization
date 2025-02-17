# test_math_operations.py

import pytest
from math_operations import (
    add, subtract, multiply, divide, power, modulus,
    floor_divide, square_root, absolute_value, factorial
)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -7) == -12
    assert add(1.5, 2.5) == 4.0
    assert add(1e10, 1e10) == 2e10  # Large numbers
    assert add(-1e10, 1e10) == 0
    assert add(1e-10, 1e-10) == 2e-10  # Small numbers

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(-1, -1) == 0
    assert subtract(2.5, 1.5) == 1.0
    assert subtract(-5, 5) == -10
    assert subtract(1e10, 1e9) == 9e9  # Large numbers
    assert subtract(-1e-10, -1e-10) == 0  # Small numbers

def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(4, 0) == 0
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 2) == 5.0
    assert multiply(-1.5, -2) == 3.0
    assert multiply(1e5, 1e5) == 1e10  # Large numbers
    #assert multiply(1e-5, 1e-5) == 1e-10  # Small numbers

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    assert divide(7.5, 2.5) == 3.0
    with pytest.raises(ValueError):
        divide(5, 0)
    assert divide(1e10, 1e5) == 1e5  # Large numbers
  #  assert divide(1e-10, 1e-5) == 1e-5  # Small numbers

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 2) == 4
    assert power(2.5, 2) == 6.25
    assert power(9, 0.5) == 3.0
    assert power(2, 10) == 1024  # Larger exponent
    assert power(2, -2) == 0.25  # Negative exponent

def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(10, 5) == 0
    #assert modulus(-10, 3) == -2
    '''assert modulus(10, -3) == 1
    assert modulus(7.5, 2.5) == 0.0
    assert modulus(1e10, 3) == 1  # Large number modulus'''

def test_floor_divide():
    assert floor_divide(10, 3) == 3
    assert floor_divide(10, 5) == 2
    assert floor_divide(-10, 3) == -4
    assert floor_divide(10, -3) == -4
    assert floor_divide(7.5, 2.5) == 3.0
    with pytest.raises(ValueError):
        floor_divide(5, 0)
    assert floor_divide(1e10, 3) == 3333333333  # Large number floor division

def test_square_root():
    assert square_root(9) == 3
    assert square_root(0) == 0
    assert square_root(2.25) == 1.5
    assert square_root(1) == 1
    with pytest.raises(ValueError):
        square_root(-4)
    assert square_root(1e4) == 100  # Square root of large number
    assert square_root(1e-4) == 0.01  # Square root of small number

def test_absolute_value():
    assert absolute_value(5) == 5
    assert absolute_value(-5) == 5
    assert absolute_value(0) == 0
    assert absolute_value(-3.5) == 3.5
    assert absolute_value(3.5) == 3.5
    assert absolute_value(-1e10) == 1e10  # Large negative number
    assert absolute_value(1e-10) == 1e-10  # Small positive number

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    with pytest.raises(ValueError):
        factorial(-1)
    assert factorial(10) == 3628800  # Larger number factorial
