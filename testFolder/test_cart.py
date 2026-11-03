from cart import total


def test_total(cart, product):
    cart.append(product)
    assert total(cart) == 50