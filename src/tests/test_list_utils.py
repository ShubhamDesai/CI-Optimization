from list_utils import flatten_list,unique_elements

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([]) == []

def test_unique_elements():
    assert unique_elements([1, 2, 2, 3]) == [1, 2, 3]
    assert unique_elements([]) == []
