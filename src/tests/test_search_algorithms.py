from search_algorithms import linear_search,binary_search

def test_linear_search():
    assert linear_search([1, 2, 3], 2) == 1
    assert linear_search([1, 2, 3], 4) == -1

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
