import pytest
from calculator import add, subtract, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

