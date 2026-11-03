import pytest
import math

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b

@pytest.mark.check
def test_positive_test_sum():
    result = add(0.2,0.1)
    assert result == pytest.approx(0.3)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_sqrt():
    assert math.sqrt(-4) == 2

