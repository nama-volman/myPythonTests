
 
# conftest.py
import pytest
 
@pytest.fixture
def product():
    return {"name": "Keyboard", "price": 50}
 
@pytest.fixture
def cart():
    return []
 
