from fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
