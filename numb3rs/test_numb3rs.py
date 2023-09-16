from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True

def test_invalid():
    assert validate("275.3.6.28") == False
    assert validate("1.2.3.1000") == False

def test_string():
    assert validate("cat") == False

def test_first_byte():
    assert validate("1.300.300.300") == False