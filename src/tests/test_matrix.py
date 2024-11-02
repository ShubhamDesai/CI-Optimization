# src/tests/test_matrix.py

from matrix import matrix_addition, matrix_multiplication

def test_matrix_addition():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    assert matrix_addition(a, b) == [[6, 8], [10, 12]]

def test_matrix_multiplication():
    a = [[1, 2], [3, 4]]
    b = [[2, 0], [1, 2]]
    assert matrix_multiplication(a, b) == [[4, 4], [10, 8]]
