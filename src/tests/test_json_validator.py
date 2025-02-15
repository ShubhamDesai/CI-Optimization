import pytest
from json_validator import is_valid_json  # Replace 'your_module' with the actual module name

def test_valid_json():
    # Test with a simple valid JSON string
    assert is_valid_json('{"name": "John", "age": 30}') is True

    # Test with a valid JSON array
    assert is_valid_json('["apple", "banana", "cherry"]') is True

    # Test with a nested JSON object
    assert is_valid_json('{"person": {"name": "John", "age": 30}, "city": "New York"}') is True

def test_invalid_json():
    # Test with a missing closing brace
    assert is_valid_json('{"name": "John", "age": 30') is False

    # Test with single quotes instead of double quotes
    assert is_valid_json("{'name': 'John', 'age': 30}") is False

    # Test with an extra comma
    assert is_valid_json('{"name": "John", "age": 30,}') is False

    # Test with an invalid JSON array
    assert is_valid_json('["apple", "banana",]') is False

def test_edge_cases():
    # Test with an empty string
    assert is_valid_json('') is False

    # Test with a non-JSON string
    assert is_valid_json('Hello, World!') is False

    # Test with a number (valid JSON)
    assert is_valid_json('123') is True

    # Test with a boolean (valid JSON)
    assert is_valid_json('true') is True

    # Test with null (valid JSON)
    assert is_valid_json('null') is True

    # Test with whitespace (invalid JSON)
    assert is_valid_json('   ') is False

    # Test with special characters
    assert is_valid_json('@#$%^&*') is False
