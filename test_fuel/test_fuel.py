import pytest
from fuel import convert, gauge

def test_valid():
    assert convert("3/4") == 75

def test_ValueError():
    with pytest.raises(ValueError):
        convert("5/4")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"