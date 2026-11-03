import pytest

# @pytest.fixture
# def user():
#     return {"name": "Ari", "active": True}

# def test_user_is_active(user):
#     assert user["active"] is True

# def test_user_name(user):
#     assert user["name"] is "Ari"

# def test_user_is_active_with_get(user):
#     assert user.get("active") is True

 
# @pytest.fixture (scope="module")
# def shared_value():
#     print("CREATING FIXTURE")
#     return ["one"]

# @pytest.mark.smoke3
# def test_one(shared_value):
#     shared_value.append("two")
#     assert "two" in shared_value

# @pytest.mark.smoke3
# def test_two(shared_value):
#     assert "one" in shared_value

#dependent fixture
# @pytest.fixture
# def user():
#     print("Creating user")
#     return {"id": 7, "name": "Ari"}


# @pytest.fixture
# def authenticated_client(user):
#     print("Creating authenticated client")
#     return {
#         "user": user,
#         "token": "test-token",
#     }


# @pytest.fixture
# def profile_page(user):
#     print("Creating profile page")
#     return {
#         "username": user["name"],
#         "url": f"/users/{user['id']}",
#     }


# def test_user_profile(authenticated_client, profile_page):
#     assert authenticated_client["user"]["name"] == "Ari"
#     assert profile_page["username"] == "Ari"
#     assert profile_page["url"] == "/users/7"

# @pytest.fixture
# def temporary_user():
#     print("\nSETUP: create user")
#     setupArray = []
#     user = {"name": "Ari", "active": True}
#     setupArray.append(user)
#     yield user
#     setupArray.remove(user)
#     print("\nTEARDOWN: User removed")
 
# def test_user_is_active1(temporary_user):
#     assert temporary_user["active"] == True
# def test_user_is_active2(temporary_user):
#     assert temporary_user["active"] == True

 
# @pytest.fixture(scope="module")
# def shared_value():
#     print("CREATING FIXTURE")
#     return ["one"]
 
# @pytest.mark.smoke3
# def test_one(shared_value):
#     print(f"Shared value fixture: {shared_value}")
#     shared_value.append("three")
#     assert "three" in shared_value
 
# @pytest.mark.smoke3
# def test_two(shared_value):
#     print(f"Shared value fixture: {shared_value}")
#     assert "two" in shared_value

import pytest
@pytest.fixture (scope="module")
def user():
    return {
        "name": "Alice",
        "role": "admin",
        "active": True
    }
@pytest.fixture(scope="module")
def product():
    return{
        "name": "Keyboard" ,
        "price": 49.99 ,
        "in_stock": True
    }

def test_user_name(user):
    assert user["name"] == "Alice"
def test_user_is_admin(user):
    assert user["role"] == "admin"
def test_user_is_active(user):
    assert user["active"] is True
def test_product_name(product):
    assert product["name"] == "Keyboard"
def test_product_price(product):
    assert product["price"] == 49.99
def test_product_is_in_stock(product):
    assert product["in_stock"] is True