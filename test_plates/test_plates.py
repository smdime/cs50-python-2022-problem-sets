from plates import is_valid

def test_zero():
    assert is_valid("ABC012") == False

def test_one():
    assert is_valid("A") == False

def test_two():
    assert is_valid("AA") == True

def test_three():
    assert is_valid("A50") == False

def test_four():
    assert is_valid("CS50") == True

def test_five():
    assert is_valid("AB123D") == False

def test_six():
    assert is_valid("ABC123") == True

def test_seven():
    assert is_valid("ABCD123") == False

def test_not_alnum():
    assert is_valid("ABC!@#") == False