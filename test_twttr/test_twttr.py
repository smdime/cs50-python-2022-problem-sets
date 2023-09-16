from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_with_numbers():
    assert shorten("CS50") == "CS50"

def test_all_vowels():
    assert shorten("aeiouAEIOU") ==  ""