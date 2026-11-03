import pytest;

def add(a, b):
    return a + b

def add3(a, b, c):
    return a + b +c

def test_add_two_positive_numbers1():
    result= add(2, 3)
    print ("you dont see me, bat i'm here")
    assert result ==5


@pytest.mark.smoke
def test_add_two_negaitive_numbers1():
    result= add(-2, -3)
    assert result ==-5


@pytest.mark.fire
def test_add_three_positive_numbers1():
    result= add3(2, 3, 1)
    print ("you dont see me, bat i'm here")
    assert result ==6

def test_add_three_negaitive_numbers1():
    result= add3(2, 3, 1)
    print ("you dont see me, bat i'm here")
    assert result ==6


def test_total1():
    actual = 7*6
    expected = 42
    assert actual == expected

def test_total1():
    actual = 25*5
    expected =125
    assert actual == expected