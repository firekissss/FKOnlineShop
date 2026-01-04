import pytest

from src.order import Order
from src.product import Product


def test_order_creation():
    product = Product("продукт", "айфон 100 ультра про макс", 1000000.0, 5)
    order = Order("заказ", "доставка бесплатно", product, 3)

    assert order.product is product
    assert order.quantity == 3
    assert order.total_price == 3000000.0


def test_order_incorrect_amount():
    product = Product("продукт", "айфон 100 ультра про макс", 1000000.0, 5)
    with pytest.raises(ValueError):
        Order("something", "description", product, 6)
    with pytest.raises(ValueError):
        Order("something", "description", product, 0)
    with pytest.raises(ValueError):
        Order("something", "description", product, -3)


def test_order_str():
    product = Product("продукт", "айфон 100 ультра про макс", 1000000.0, 5)
    order = Order("заказ", "доставка бесплатно", product, 3)
    result = str(order)
    assert "продукт" in result
    assert "3" in result
    assert "3000000" in result
