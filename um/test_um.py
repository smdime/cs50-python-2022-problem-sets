from um import count

def test_um_once():
    assert count("hello, um, world") == 1

def test_no_um():
    assert count("yummy") == 0

def test_case_insensitivity():
    assert count("Um..UM...Ahem!") == 2
