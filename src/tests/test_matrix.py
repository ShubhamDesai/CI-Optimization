from matrix import matrix_addition, matrix_multiplication

def test_matrix_addition():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    assert matrix_addition(a, b) == [[6, 8], [10, 12]]

    c = [[-1, -2], [-3, -4]]
    d = [[1, 2], [3, 4]]
    assert matrix_addition(c, d) == [[0, 0], [0, 0]]

    e = [[0, 0], [0, 0]]
    f = [[0, 0], [0, 0]]
    assert matrix_addition(e, f) == [[0, 0], [0, 0]]

def test_matrix_multiplication():
    a = [[1, 2], [3, 4]]
    b = [[2, 0], [1, 2]]
    assert matrix_multiplication(a, b) == [[4, 4], [10, 8]]

    c = [[0, 0], [0, 0]]
    d = [[1, 2], [3, 4]]
    assert matrix_multiplication(c, d) == [[0, 0], [0, 0]]

    e = [[1, 2], [3, 4]]
    f = [[0, 0], [0, 0]]
    assert matrix_multiplication(e, f) == [[0, 0], [0, 0]]
