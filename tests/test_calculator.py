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

import math_utils

def test_add():
    assert math_utils.add(1, 2) == 3
    assert math_utils.add(-1, -1) == -2

def test_subtract():
    assert math_utils.subtract(5, 3) == 2
    assert math_utils.subtract(0, 5) == -5

def test_divide():
    assert math_utils.divide(10, 2) == 5
    assert math_utils.divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        math_utils.divide(5, 0)

