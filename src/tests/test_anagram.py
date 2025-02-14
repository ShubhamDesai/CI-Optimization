def test_are_anagrams():
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("hello", "world") is False
