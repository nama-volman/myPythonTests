import pytest

def add(a, b):
    return a + b

def add3(a, b, c):
    return a + b +c

def test_add_two_positive_numbers():
    result= add(2, 3)
    print ("you dont see me, bat i'm here")
    assert result ==5

@pytest.mark.skip
@pytest.mark.smoke
def test_add_two_negaitive_numbers():
    result= add(-2, -3)
    assert result ==-5


@pytest.mark.check
def test_add_three_positive_numbers():
    result= add3(2, 3, 1)
    print ("you dont see me, bat i'm here")
    assert result ==6

def test_add_three_negaitive_numbers():
    result= add3(2, 3, 1)
    print ("you dont see me, bat i'm here")
    assert result ==6


def test_total():
    actual = 7*6
    expected = 42
    assert actual == expected

def test_total():
    actual = 25*5
    expected =125
    assert actual == expected



def test_total2():
    actual = 7*6
    expected = 41
    if actual!=expected:
        raise Exception('failed')


def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b




def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def add(a, b):
    return a + b
def test_positive_test_sum():
    result = add(0.1, 0.2)
    assert result == pytest.approx(0.3)