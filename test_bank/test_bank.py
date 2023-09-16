from bank import value

def test_hello():
    assert value("hello, world") == 0

def test_start_h():
    assert value("hey") == 20

def test_not_start_h():
    assert value("what's up") == 100

def test_case_insensitive():
    assert value("HEY") == 20