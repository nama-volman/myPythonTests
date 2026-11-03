import pytest

@pytest.fixture
def myfixture():
    print("This fixture is running")
    return "fixture OK"

def test_test1 (myfixture):
    print(f"Test 1 got fixture: {myfixture}")