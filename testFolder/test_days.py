import pytest


@pytest.mark.parametrize(
    "day",
    [
        pytest.param("Sun", id="Sunday"),
        pytest.param("Mon", id="Monday"),
        pytest.param("Tue", id="Tuesday"),  
],
)


def test_print_day(day):
    print("\ntoday is: ", day)
    assert True

