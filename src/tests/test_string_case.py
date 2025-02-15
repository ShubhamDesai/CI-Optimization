from string_case import to_lowercase,to_uppercase

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("WORLD") == "WORLD"

def test_to_lowercase():
    assert to_lowercase("HELLO") == "hello"
    assert to_lowercase("world") == "world"
