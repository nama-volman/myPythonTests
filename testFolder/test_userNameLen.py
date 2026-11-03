import pytest


@pytest.mark.parametrize(
    "username, expected",
    [
        pytest.param("myUsername",True, id="valid"),
        pytest.param("usr", False, id="too short"),
        pytest.param("myUsernameIsVeryLong", False, id="Very Long"),  
],
)


def test_usernameValid(username, expected):
    print("\nThe username is: ", username)
    assert isPasswordValid(username) == expected

def isPasswordValid(name):
    lenUsername = len(name)
    return lenUsername> 3 and  lenUsername< 12
