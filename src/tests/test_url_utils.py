from url_utils import get_domain,get_path

def test_get_domain():
    assert get_domain("https://www.example.com/path") == "www.example.com"
    assert get_domain("http://example.com") == "example.com"

def test_get_path():
    assert get_path("https://www.example.com/path") == "/path"
    assert get_path("http://example.com") == ""
