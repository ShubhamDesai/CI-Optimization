from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama") is True
    assert is_palindrome("Hello") is False

