from json_utils import json_to_dict,dict_to_json,json

def test_json_to_dict():
    json_str = '{"name": "Alice", "age": 30}'
    assert json_to_dict(json_str) == {"name": "Alice", "age": 30}

def test_dict_to_json():
    dictionary = {"name": "Bob", "age": 25}
    assert dict_to_json(dictionary) == '{"name": "Bob", "age": 25}'