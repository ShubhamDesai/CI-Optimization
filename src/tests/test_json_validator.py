import pytest
from json_validator import is_valid_json

def test_valid_json():
    valid_json = '{"name": "John Doe", "age": 30, "email": "john.doe@example.com"}'
    assert is_valid_json(valid_json) is True

def test_missing_field():
    missing_email_json = '{"name": "John Doe", "age": 30}'
    assert is_valid_json(missing_email_json) is False

def test_invalid_age_type():
    invalid_age_json = '{"name": "John Doe", "age": "thirty", "email": "john.doe@example.com"}'
    assert is_valid_json(invalid_age_json) is False

def test_invalid_email_format():
    invalid_email_json = '{"name": "John Doe", "age": 30, "email": "john.doe@com"}'
    assert is_valid_json(invalid_email_json) is False

def test_invalid_json_syntax():
    invalid_json = '{"name": "John Doe", "age": 30, "email": "john.doe@example.com",}'
    assert is_valid_json(invalid_json) is False
