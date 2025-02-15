from data_validation import is_email_valid,is_phone_number_valid

def test_is_email_valid():
    assert is_email_valid("test@example.com") is True
    assert is_email_valid("invalid-email") is False

def test_is_phone_number_valid():
    assert is_phone_number_valid("1234567890") is True
    assert is_phone_number_valid("12345") is False
