import pytest
from unittest.mock import patch
import product_service as ps
import random

#task 1
@patch('product_service.fetch_product')
def test_title_returned_on_success(mock_fetch):
    mock_fetch.return_value = {"id": 1 , "title": "table"}
    result = ps.get_product_name(1)
    assert result == "table"


#task 2
@patch('product_service.fetch_product')
def test_missing_title(mock_fetch):
    mock_fetch.return_value = {"id": 1}
    with pytest.raises(ValueError, match="Product title is missing"):
        ps.get_product_name(1)


#task 3
@patch('product_service.fetch_product')
def test_timeout(mock_fetch):
    mock_fetch.side_effect = TimeoutError("request timed out")
    with pytest.raises(TimeoutError, match="timed out"):
         ps.get_product_name(1)


#task 4
@patch('product_service.fetch_product')
def test_called_correct_id(mock_fetch):
    product_id = random.randint(1,100)
    mock_fetch.return_value = {"id": product_id , "title": "chair"}
    result = ps.get_product_name(product_id)
    mock_fetch.assert_called_once_with(product_id)
