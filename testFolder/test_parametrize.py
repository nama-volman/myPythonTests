import pytest

def add(a, b):
    return a+b


@pytest.mark.parametrize(
    "a, b, expected, name",
    [
        pytest.param(2, 3, 5, "positive-numbers", id="positive-numbers"),
        pytest.param(0, 5, 5, "zero-plus-positive", id="zero-plus-positive"),
        pytest.param(-2, 3, 1, "negative-plus-positive",  id="negative-plus-positive"),
    ],
)


def test_add(a, b, expected, name):
    print("\nranning test: ", name)
    assert add(a, b) == expected