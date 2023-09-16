from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    jar_default = Jar()
    assert jar_default.capacity == 12
    assert jar_default.size == 0

    with pytest.raises(ValueError):
        Jar("invalid")
    with pytest.raises(ValueError):
        Jar(-5)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)

    jar.withdraw(2)
    assert jar.size == 1
    assert str(jar) == "🍪"

    with pytest.raises(ValueError):
        jar.withdraw(2)

    with pytest.raises(ValueError):
        jar.withdraw(-1)
