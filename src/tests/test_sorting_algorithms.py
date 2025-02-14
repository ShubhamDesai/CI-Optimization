from sorting_algorithms import bubble_sort,quick_sort

def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([]) == []

def test_quick_sort():
    assert quick_sort([3, 2, 1]) == [1, 2, 3]
    assert quick_sort([]) == []