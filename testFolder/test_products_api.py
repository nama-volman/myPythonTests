
import pytest
import requests 
import random

BASE_URL = "https://dummyjson.com"
get_URL = "https://dummyjson.com/products"

@pytest.mark.parametrize(
    "product_id",
    [
        pytest.param(1, id="first-product"),
        pytest.param(2, id="second-product"),
        pytest.param(3, id="third-product"),
    ],
)
def test_get_product_by_id(product_id):
    # TODO 1: Send a GET request to /products/{product_id}
    response = requests.get(f"{get_URL}/{product_id}")
    # TODO 2: Assert that the status code is 200
    assert response.status_code == 200
    # TODO 3: Parse the JSON response
    parsed_data = response.json()
    # TODO 4: Assert that the returned ID matches product_id
    assert parsed_data.get("id") == product_id
    # TODO 5: Assert that the response contains a title and price
    title = ["",{},None]
    price = [{}, None]
    assert  parsed_data.get("title") != any(title) and parsed_data.get("price") != any(price)
    


@pytest.mark.parametrize(
    "search_term",
    [
        pytest.param("phone", id="search-phone"),
        pytest.param("laptop", id="search-laptop"),
    ],
)
def test_search_products(search_term):
    # TODO: Send GET /products/search with q=search_term
    response = requests.get(f"{get_URL}/search?q={search_term}")
    # TODO: Assert status code and response structure
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data.get("products"), list)
    assert data.get("total")
    assert data.get("skip")==0
    assert data.get("limit")
    # TODO: Verify the search behavior against the API's documented contract
    itemInProduct = data.get("products")
    for item in itemInProduct:
        jsonToText = f"{item}".lower()
        assert search_term.lower() in jsonToText, (f"'{search_term}' not found in product- {item.get('id')}.")




@pytest.mark.parametrize(
    "limit",
    [
        pytest.param(1, id="one-result"),
        pytest.param(5, id="five-results"),
    ],
)
def test_product_limit(limit):
    # TODO: Send GET /products with the limit query parameter
    response = requests.get(f"{get_URL}?limit={limit}")
    # TODO: Assert status code
    assert response.status_code == 200
    # TODO: Assert len(response["products"]) <= limit
    data = response.json()
    assert len(data.get("products")) <= limit
    # TODO: Check the response pagination metadata
    assert data.get("limit") == limit
    assert "total" in data and isinstance(data.get("total"), int)
    assert "skip" in data and isinstance(data.get("skip"), int)
    assert "limit" in data and isinstance(data.get("limit"), int)