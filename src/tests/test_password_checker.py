from password_checker import is_strong_password

def test_is_strong_password():
    # Valid strong passwords
    assert is_strong_password("StrongPass1!") is True
    assert is_strong_password("Valid$Password123") is True
    assert is_strong_password("Another@Strong1") is True

    # Too short
    assert is_strong_password("Shrt1!") is False  # Less than 8 characters

    # Missing components
    assert is_strong_password("NoNumbers!") is False  # Missing digits
    assert is_strong_password("nouppercase1!") is False  # Missing uppercase letters
    assert is_strong_password("NOLOWERCASE1!") is False  # Missing lowercase letters
    assert is_strong_password("NoSpecialChar1") is False  # Missing special characters

    # Edge cases
    assert is_strong_password("12345678!") is False  # Only numbers and special character
    assert is_strong_password("Password!") is False  # Missing digits
    assert is_strong_password("Pass1234") is False  # Missing special characters
    assert is_strong_password("!@#$%^&*()") is False  # Only special characters

    # Valid edge cases
    assert is_strong_password("A1!bcdef") is True  # Exactly 8 characters meeting all criteria
    assert is_strong_password("Abcdefghijklmnop1!") is True  # Long password meeting all criteria
