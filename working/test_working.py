import pytest
from working import convert

def test_valid_first():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_second():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_third():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9 AM to 5:60 PM")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")